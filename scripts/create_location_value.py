from __future__ import annotations

from pathlib import Path
import re

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


INPUT_PATH = Path("data/processed/2026-data-with-woba-xwoba.parquet")
OUTPUT_PATH = Path("data/processed/location_value_grid.csv")
PLOTS_DIR = Path("plots/location_value")

BIN_SIZE = 0.25
SMOOTHING_WEIGHT = 100

PITCH_TYPE_NORMALIZATION = {
    "Fastball": "Four-Seam",
    "Two-Seam": "Sinker",
}

REQUIRED_COLUMNS = {
    "pitch_type",
    "batter_side_canonical",
    "pitch_location_plate_loc_side_x",
    "pitch_location_plate_loc_height_x",
    "xwoba_frontier",
}


def normalize_pitch_type(series: pd.Series) -> pd.Series:
    return series.astype("string").replace(PITCH_TYPE_NORMALIZATION)


def normalize_batter_side(series: pd.Series) -> pd.Series:
    side = series.astype("string").str.upper().str.strip()
    return side.replace({"RIGHT": "R", "LEFT": "L", "RHH": "R", "LHH": "L"})


def location_bin(values: pd.Series) -> pd.Series:
    numeric = pd.to_numeric(values, errors="coerce")
    return np.floor(numeric / BIN_SIZE) * BIN_SIZE


def slugify(value: object) -> str:
    cleaned = re.sub(r"[^A-Za-z0-9]+", "_", str(value)).strip("_").lower()
    return cleaned or "unknown"


def prepare_pitch_data(df: pd.DataFrame) -> pd.DataFrame:
    missing = sorted(REQUIRED_COLUMNS.difference(df.columns))
    if missing:
        raise ValueError(f"Missing required columns: {missing}")

    work = df[list(REQUIRED_COLUMNS)].copy()
    work = work.rename(
        columns={
            "batter_side_canonical": "batter_side",
            "pitch_location_plate_loc_side_x": "plate_loc_side",
            "pitch_location_plate_loc_height_x": "plate_loc_height",
        }
    )
    work["pitch_type"] = normalize_pitch_type(work["pitch_type"])
    work["batter_side"] = normalize_batter_side(work["batter_side"])
    work["plate_loc_side"] = pd.to_numeric(work["plate_loc_side"], errors="coerce")
    work["plate_loc_height"] = pd.to_numeric(work["plate_loc_height"], errors="coerce")
    work["xwoba_frontier"] = pd.to_numeric(work["xwoba_frontier"], errors="coerce")
    work["side_bin"] = location_bin(work["plate_loc_side"])
    work["height_bin"] = location_bin(work["plate_loc_height"])
    work["side_bin_center"] = work["side_bin"] + BIN_SIZE / 2
    work["height_bin_center"] = work["height_bin"] + BIN_SIZE / 2

    return work.dropna(
        subset=[
            "pitch_type",
            "batter_side",
            "side_bin",
            "height_bin",
        ]
    )


def create_location_grid(pitches: pd.DataFrame) -> pd.DataFrame:
    group_keys = ["pitch_type", "batter_side"]
    cell_keys = [
        "pitch_type",
        "batter_side",
        "side_bin",
        "height_bin",
        "side_bin_center",
        "height_bin_center",
    ]

    baselines = (
        pitches.groupby(group_keys, dropna=False)["xwoba_frontier"]
        .agg(
            pitch_type_batter_side_xwoba_count="count",
            pitch_type_batter_side_avg="mean",
        )
        .reset_index()
    )
    pitch_counts = (
        pitches.groupby(group_keys, dropna=False)
        .size()
        .rename("pitch_type_batter_side_count")
        .reset_index()
    )
    baselines = pitch_counts.merge(baselines, on=group_keys, how="left")

    grid = (
        pitches.groupby(cell_keys, dropna=False)["xwoba_frontier"]
        .agg(cell_count="size", xwoba_observation_count="count", cell_avg_xwoba="mean")
        .reset_index()
        .merge(baselines, on=group_keys, how="left")
    )
    grid = grid.dropna(subset=["pitch_type_batter_side_avg"])
    grid["cell_avg_for_smoothing"] = grid["cell_avg_xwoba"].fillna(
        grid["pitch_type_batter_side_avg"]
    )
    grid["smoothed_xwoba"] = (
        (grid["cell_count"] * grid["cell_avg_for_smoothing"])
        + (SMOOTHING_WEIGHT * grid["pitch_type_batter_side_avg"])
    ) / (grid["cell_count"] + SMOOTHING_WEIGHT)
    grid["location_value"] = (
        grid["pitch_type_batter_side_avg"] - grid["smoothed_xwoba"]
    )
    grid["location_value_per_100"] = grid["location_value"] * 100
    grid["bin_size_ft"] = BIN_SIZE
    grid["smoothing_weight"] = SMOOTHING_WEIGHT

    columns = [
        "pitch_type",
        "batter_side",
        "side_bin",
        "height_bin",
        "side_bin_center",
        "height_bin_center",
        "cell_count",
        "xwoba_observation_count",
        "cell_avg_xwoba",
        "pitch_type_batter_side_count",
        "pitch_type_batter_side_xwoba_count",
        "pitch_type_batter_side_avg",
        "smoothed_xwoba",
        "location_value",
        "location_value_per_100",
        "bin_size_ft",
        "smoothing_weight",
    ]
    return grid[columns].sort_values(
        ["pitch_type", "batter_side", "height_bin", "side_bin"]
    )


def plot_heatmap(group: pd.DataFrame, pitch_type: str, batter_side: str) -> None:
    pivot = group.pivot(
        index="height_bin_center",
        columns="side_bin_center",
        values="location_value_per_100",
    ).sort_index(ascending=True)

    if pivot.empty:
        return

    max_abs = np.nanmax(np.abs(pivot.to_numpy(dtype=float)))
    if not np.isfinite(max_abs):
        return
    color_limit = max(max_abs, 0.5)
    fig_width = max(7.0, min(13.0, pivot.shape[1] * 0.32))
    fig_height = max(6.0, min(10.0, pivot.shape[0] * 0.32))

    fig, ax = plt.subplots(figsize=(fig_width, fig_height))
    image = ax.imshow(
        pivot.to_numpy(dtype=float),
        origin="lower",
        aspect="auto",
        cmap="RdYlBu",
        vmin=-color_limit,
        vmax=color_limit,
    )

    x_labels = [f"{value:.2f}" for value in pivot.columns]
    y_labels = [f"{value:.2f}" for value in pivot.index]
    ax.set_xticks(range(len(x_labels)), labels=x_labels, rotation=90, fontsize=7)
    ax.set_yticks(range(len(y_labels)), labels=y_labels, fontsize=7)
    ax.set_xlabel("Plate Location Side Bin Center (ft)")
    ax.set_ylabel("Plate Location Height Bin Center (ft)")
    ax.set_title(f"Location Value: {pitch_type} vs {batter_side}HH")

    colorbar = fig.colorbar(image, ax=ax)
    colorbar.set_label("Location Value per 100 points of xwOBA")

    fig.tight_layout()
    output = PLOTS_DIR / f"{slugify(pitch_type)}_vs_{slugify(batter_side)}hh.png"
    fig.savefig(output, dpi=160)
    plt.close(fig)


def make_heatmaps(grid: pd.DataFrame) -> None:
    PLOTS_DIR.mkdir(parents=True, exist_ok=True)
    for old_plot in PLOTS_DIR.glob("*.png"):
        old_plot.unlink()
    for (pitch_type, batter_side), group in grid.groupby(["pitch_type", "batter_side"]):
        plot_heatmap(group, str(pitch_type), str(batter_side))


def main() -> None:
    df = pd.read_parquet(INPUT_PATH)
    pitches = prepare_pitch_data(df)
    grid = create_location_grid(pitches)

    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    grid.to_csv(OUTPUT_PATH, index=False)
    make_heatmaps(grid)

    combo_count = grid[["pitch_type", "batter_side"]].drop_duplicates().shape[0]
    print(f"Wrote location grid: {OUTPUT_PATH}")
    print(f"Wrote heatmaps to: {PLOTS_DIR}")
    print(f"Pitch type + batter side grids: {combo_count:,}")
    print(f"Location cells: {len(grid):,}")


if __name__ == "__main__":
    main()
