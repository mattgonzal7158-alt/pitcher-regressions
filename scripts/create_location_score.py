from __future__ import annotations

from pathlib import Path

import numpy as np
import pandas as pd


PITCH_INPUT_PATH = Path("data/processed/2026-data-with-woba-xwoba.parquet")
GRID_INPUT_PATH = Path("data/processed/location_value_grid.csv")
OUTPUT_PATH = Path("data/processed/location_scores.csv")
REPORT_PATH = Path("reports/location_score_report.md")

BIN_SIZE = 0.25
MIN_PITCHES = 25

PITCH_TYPE_NORMALIZATION = {
    "Fastball": "Four-Seam",
    "Two-Seam": "Sinker",
}

PITCH_REQUIRED_COLUMNS = {
    "pitcher_name",
    "pitcher_id",
    "pitcher_team",
    "pitch_type",
    "batter_side_canonical",
    "pitch_location_plate_loc_side_x",
    "pitch_location_plate_loc_height_x",
}

GRID_REQUIRED_COLUMNS = {
    "pitch_type",
    "batter_side",
    "side_bin",
    "height_bin",
    "pitch_type_batter_side_avg",
    "smoothed_xwoba",
}


def normalize_pitch_type(series: pd.Series) -> pd.Series:
    return series.astype("string").replace(PITCH_TYPE_NORMALIZATION)


def normalize_batter_side(series: pd.Series) -> pd.Series:
    side = series.astype("string").str.upper().str.strip()
    return side.replace({"RIGHT": "R", "LEFT": "L", "RHH": "R", "LHH": "L"})


def location_bin(values: pd.Series) -> pd.Series:
    numeric = pd.to_numeric(values, errors="coerce")
    return np.floor(numeric / BIN_SIZE) * BIN_SIZE


def percentile_rank(values: pd.Series) -> pd.Series:
    return values.rank(method="average", pct=True).mul(100)


def prepare_pitch_data(df: pd.DataFrame) -> pd.DataFrame:
    missing = sorted(PITCH_REQUIRED_COLUMNS.difference(df.columns))
    if missing:
        raise ValueError(f"Missing required pitch columns: {missing}")

    work = df[list(PITCH_REQUIRED_COLUMNS)].copy()
    work = work.rename(
        columns={
            "batter_side_canonical": "batter_side",
            "pitch_location_plate_loc_side_x": "plate_loc_side",
            "pitch_location_plate_loc_height_x": "plate_loc_height",
        }
    )
    work["pitch_type"] = normalize_pitch_type(work["pitch_type"])
    work["batter_side"] = normalize_batter_side(work["batter_side"])
    work["side_bin"] = location_bin(work["plate_loc_side"])
    work["height_bin"] = location_bin(work["plate_loc_height"])

    return work.dropna(
        subset=[
            "pitcher_name",
            "pitch_type",
            "batter_side",
            "side_bin",
            "height_bin",
        ]
    )


def prepare_location_grid(grid: pd.DataFrame) -> pd.DataFrame:
    missing = sorted(GRID_REQUIRED_COLUMNS.difference(grid.columns))
    if missing:
        raise ValueError(f"Missing required grid columns: {missing}")

    work = grid[
        [
            "pitch_type",
            "batter_side",
            "side_bin",
            "height_bin",
            "pitch_type_batter_side_avg",
            "smoothed_xwoba",
        ]
    ].copy()
    work["pitch_type"] = normalize_pitch_type(work["pitch_type"])
    work["batter_side"] = normalize_batter_side(work["batter_side"])
    work["side_bin"] = pd.to_numeric(work["side_bin"], errors="coerce")
    work["height_bin"] = pd.to_numeric(work["height_bin"], errors="coerce")
    work["pitch_type_batter_side_avg"] = pd.to_numeric(
        work["pitch_type_batter_side_avg"], errors="coerce"
    )
    work["smoothed_xwoba"] = pd.to_numeric(work["smoothed_xwoba"], errors="coerce")
    work = work.dropna(
        subset=[
            "pitch_type",
            "batter_side",
            "side_bin",
            "height_bin",
            "pitch_type_batter_side_avg",
            "smoothed_xwoba",
        ]
    )
    work["location_advantage"] = (
        work["pitch_type_batter_side_avg"] - work["smoothed_xwoba"]
    )
    work = work.rename(
        columns={
            "pitch_type_batter_side_avg": "league_average_pitch_type_side_xwoba",
            "smoothed_xwoba": "grid_xwoba",
        }
    )
    return work


def assign_location_advantage(pitches: pd.DataFrame, grid: pd.DataFrame) -> pd.DataFrame:
    merge_keys = ["pitch_type", "batter_side", "side_bin", "height_bin"]
    assigned = pitches.merge(grid, on=merge_keys, how="inner")
    return assigned


def add_scores(grouped: pd.DataFrame) -> pd.DataFrame:
    scored = grouped.loc[grouped["pitch_count"].ge(MIN_PITCHES)].copy()
    scored["location_score_raw"] = scored["average_location_advantage"]
    raw_mean = scored["location_score_raw"].mean()
    raw_std = scored["location_score_raw"].std(ddof=0)

    if raw_std and not np.isclose(raw_std, 0):
        scored["location_score_20_80"] = (
            50 + 10 * ((scored["location_score_raw"] - raw_mean) / raw_std)
        ).clip(20, 80)
    else:
        scored["location_score_20_80"] = 50.0

    scored["location_score_0_100"] = percentile_rank(scored["location_score_raw"])
    scored["overall_rank"] = (
        scored["location_score_raw"].rank(method="first", ascending=False).astype(int)
    )
    scored["pitch_type_side_rank"] = (
        scored.groupby(["pitch_type", "batter_side"])["location_score_raw"]
        .rank(method="first", ascending=False)
        .astype(int)
    )
    return scored.sort_values("overall_rank")


def create_location_scores(assigned: pd.DataFrame) -> pd.DataFrame:
    grouped = (
        assigned.groupby(
            [
                "pitcher_name",
                "pitcher_id",
                "pitcher_team",
                "pitch_type",
                "batter_side",
            ],
            dropna=False,
        )
        .agg(
            pitch_count=("location_advantage", "size"),
            average_location_advantage=("location_advantage", "mean"),
            median_location_advantage=("location_advantage", "median"),
            average_grid_xwoba=("grid_xwoba", "mean"),
            league_average_pitch_type_side_xwoba=(
                "league_average_pitch_type_side_xwoba",
                "mean",
            ),
        )
        .reset_index()
    )
    return add_scores(grouped)


def format_float(value: float, digits: int = 4) -> str:
    return "" if pd.isna(value) else f"{value:.{digits}f}"


def leaderboard_table(scored: pd.DataFrame, rows: int = 30) -> list[str]:
    columns = [
        "Rank",
        "Pitcher",
        "Team",
        "Pitch Type",
        "Batter Side",
        "Pitches",
        "Avg Adv",
        "Median Adv",
        "Grid xwOBA",
        "League xwOBA",
        "LS 20-80",
        "LS 0-100",
        "Type/Side Rank",
    ]
    lines = [
        "| " + " | ".join(columns) + " |",
        "|" + "|".join(["---"] * len(columns)) + "|",
    ]
    for row in scored.head(rows).itertuples(index=False):
        lines.append(
            "| "
            + " | ".join(
                [
                    str(row.overall_rank),
                    str(row.pitcher_name),
                    str(row.pitcher_team),
                    str(row.pitch_type),
                    f"{row.batter_side}HH",
                    f"{int(row.pitch_count):,}",
                    format_float(row.average_location_advantage),
                    format_float(row.median_location_advantage),
                    format_float(row.average_grid_xwoba),
                    format_float(row.league_average_pitch_type_side_xwoba),
                    f"{row.location_score_20_80:.1f}",
                    f"{row.location_score_0_100:.1f}",
                    str(row.pitch_type_side_rank),
                ]
            )
            + " |"
        )
    return lines


def write_report(scored: pd.DataFrame, assigned_count: int) -> None:
    lines = [
        "# Location Score Report",
        "",
        f"- Pitch input file: `{PITCH_INPUT_PATH}`",
        f"- Location grid input file: `{GRID_INPUT_PATH}`",
        f"- Output file: `{OUTPUT_PATH}`",
        f"- Assigned pitch rows: {assigned_count:,}",
        f"- Qualified pitcher + pitch type + batter side rows: {len(scored):,}",
        f"- Qualification: at least {MIN_PITCHES} pitches with an assigned location grid value",
        "- Score direction: higher is better; positive location advantage means the pitch was located in a lower-xwOBA grid cell than the pitch type + batter side league average.",
        "- Pitch type normalization: `Fastball` is grouped with `Four-Seam`; `Two-Seam` is grouped with `Sinker`.",
        "",
        "## Method",
        "",
        "Each pitch is assigned to its 0.25 foot plate-location bin and joined to the matching pitch type + batter side Location Value grid.",
        "",
        "`location_advantage = league_average_pitch_type_side_xwoba - grid_xwoba`",
        "",
        "Here, `grid_xwoba` is the empirical-Bayes-smoothed xwOBA from the Location Value grid. Positive values mean the pitch was thrown to a better-than-average location for that exact pitch type and batter side.",
        "",
        "Scores are aggregated by pitcher, normalized pitch type, and batter side:",
        "",
        "- `location_score_raw`: average location advantage.",
        "- `location_score_20_80`: scouting-style scale, mean 50 and 10 points per standard deviation, clipped from 20 to 80.",
        "- `location_score_0_100`: percentile rank of `location_score_raw` among qualified rows.",
        "",
        "## Top Location Scores",
        "",
        *leaderboard_table(scored, rows=30),
        "",
        "## Top Location Scores by Pitch Type and Batter Side",
        "",
    ]

    for (pitch_type, batter_side), group in scored.groupby(["pitch_type", "batter_side"]):
        lines.extend([f"### {pitch_type} vs {batter_side}HH", ""])
        lines.extend(leaderboard_table(group.sort_values("pitch_type_side_rank"), rows=15))
        lines.append("")

    REPORT_PATH.write_text("\n".join(lines), encoding="utf-8")


def main() -> None:
    pitch_df = pd.read_parquet(PITCH_INPUT_PATH)
    grid_df = pd.read_csv(GRID_INPUT_PATH)

    pitches = prepare_pitch_data(pitch_df)
    grid = prepare_location_grid(grid_df)
    assigned = assign_location_advantage(pitches, grid)
    scored = create_location_scores(assigned)

    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    REPORT_PATH.parent.mkdir(parents=True, exist_ok=True)
    scored.to_csv(OUTPUT_PATH, index=False)
    write_report(scored, assigned_count=len(assigned))

    print(f"Wrote location scores: {OUTPUT_PATH}")
    print(f"Wrote report: {REPORT_PATH}")
    print(f"Assigned pitch rows: {len(assigned):,}")
    print(f"Qualified pitcher + pitch type + batter side rows: {len(scored):,}")
    print("\nTop 20 location scores:")
    print(
        scored[
            [
                "overall_rank",
                "pitcher_name",
                "pitcher_team",
                "pitch_type",
                "batter_side",
                "pitch_count",
                "average_location_advantage",
                "median_location_advantage",
                "location_score_20_80",
                "location_score_0_100",
            ]
        ]
        .head(20)
        .to_string(index=False)
    )


if __name__ == "__main__":
    main()
