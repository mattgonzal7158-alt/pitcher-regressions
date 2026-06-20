from __future__ import annotations

from pathlib import Path

import pandas as pd


INPUT_PATHS = {
    "pitch_value": Path("data/processed/pitch_value_scores_with_type_rank.csv"),
    "location_scores": Path("data/processed/location_scores.csv"),
    "split_leaderboards": Path("data/processed/pitch_leaderboard_splits.csv"),
    "platoon_weapons": Path("data/processed/platoon_weapon_scores.csv"),
    "movement_model": Path("data/processed/pitch_value_movement_model_data.csv"),
    "archetypes": Path("data/processed/pitch_movement_archetypes.csv"),
}
OUTPUT_PATH = Path("data/processed/master_pitch_evaluation_table.csv")
REPORT_PATH = Path("reports/master_pitch_evaluation_table_report.md")

PITCH_TYPE_NORMALIZATION = {
    "Fastball": "Four-Seam",
    "Two-Seam": "Sinker",
}

FINAL_COLUMNS = [
    "pitcher_name",
    "pitcher_id",
    "pitcher_team",
    "pitch_type",
    "batter_side",
    "pitch_count",
    "batted_ball_count",
    "raw_pitch_score_20_80",
    "raw_pitch_score_0_100",
    "location_score_20_80",
    "location_score_0_100",
    "final_pitch_score_20_80",
    "final_pitch_score_0_100",
    "overall_rank",
    "pitch_type_rank",
    "pitch_type_batter_side_rank",
    "platoon_gap",
    "better_side",
    "platoon_category",
    "IVB",
    "HB",
    "velocity",
    "spin_rate",
    "extension",
    "release_height",
    "release_side",
    "movement_quality_20_80",
    "movement_quality_0_100",
    "archetype",
    "cluster",
]


def load_inputs() -> tuple[dict[str, pd.DataFrame], list[str]]:
    frames: dict[str, pd.DataFrame] = {}
    warnings: list[str] = []
    for name, path in INPUT_PATHS.items():
        if not path.exists():
            warnings.append(f"Missing input file: `{path}`")
            print(f"WARNING: Missing input file: {path}")
            continue
        frames[name] = pd.read_csv(path)
    return frames, warnings


def normalize_pitch_type(series: pd.Series) -> pd.Series:
    return series.astype("string").replace(PITCH_TYPE_NORMALIZATION)


def normalize_batter_side(series: pd.Series) -> pd.Series:
    side = series.astype("string").str.upper().str.strip()
    return side.replace({"RIGHT": "R", "LEFT": "L", "RHH": "R", "LHH": "L"})


def normalize_pitcher_id(series: pd.Series) -> pd.Series:
    numeric = pd.to_numeric(series, errors="coerce")
    return numeric.astype("Int64").astype("string")


def add_keys(df: pd.DataFrame) -> pd.DataFrame:
    work = df.copy()
    if "pitch_type" in work.columns:
        work["pitch_type"] = normalize_pitch_type(work["pitch_type"])
    if "batter_side" in work.columns:
        work["batter_side"] = normalize_batter_side(work["batter_side"])
    if "pitcher_id" in work.columns:
        work["pitcher_id_key"] = normalize_pitcher_id(work["pitcher_id"])
    return work


def require_columns(
    df: pd.DataFrame,
    columns: list[str],
    source_name: str,
    warnings: list[str],
) -> list[str]:
    available = [column for column in columns if column in df.columns]
    missing = [column for column in columns if column not in df.columns]
    for column in missing:
        warning = f"`{source_name}` missing expected column `{column}`"
        warnings.append(warning)
        print(f"WARNING: {warning}")
    return available


def select_if_available(
    df: pd.DataFrame,
    columns: list[str],
    source_name: str,
    warnings: list[str],
) -> pd.DataFrame:
    return df[require_columns(df, columns, source_name, warnings)].copy()


def create_spine(frames: dict[str, pd.DataFrame], warnings: list[str]) -> pd.DataFrame:
    if "split_leaderboards" in frames:
        split = add_keys(frames["split_leaderboards"])
        columns = [
            "pitcher_name",
            "pitcher_id",
            "pitcher_id_key",
            "pitcher_team",
            "pitch_type",
            "batter_side",
            "split_pitch_count",
            "pitch_value_pitch_count",
            "pitch_value_20_80",
            "pitch_value_0_100",
            "location_score_20_80",
            "location_score_0_100",
            "final_pitch_score",
            "final_pitch_score_0_100",
            "overall_rank",
            "pitch_type_rank",
            "pitch_type_batter_side_rank",
        ]
        spine = select_if_available(split, columns, "split_leaderboards", warnings)
        rename_map = {
            "split_pitch_count": "pitch_count",
            "pitch_value_20_80": "raw_pitch_score_20_80",
            "pitch_value_0_100": "raw_pitch_score_0_100",
            "final_pitch_score": "final_pitch_score_20_80",
        }
        return spine.rename(columns=rename_map)

    if "location_scores" in frames:
        warning = (
            "`pitch_leaderboard_splits.csv` missing; using `location_scores.csv` "
            "as the pitcher + pitch type + batter side spine."
        )
        warnings.append(warning)
        print(f"WARNING: {warning}")
        location = add_keys(frames["location_scores"])
        columns = [
            "pitcher_name",
            "pitcher_id",
            "pitcher_id_key",
            "pitcher_team",
            "pitch_type",
            "batter_side",
            "pitch_count",
            "location_score_20_80",
            "location_score_0_100",
        ]
        return select_if_available(location, columns, "location_scores", warnings)

    if "pitch_value" in frames:
        warning = (
            "No handedness-specific file found; using Pitch Value as a non-split "
            "spine with blank batter side."
        )
        warnings.append(warning)
        print(f"WARNING: {warning}")
        pitch_value = add_keys(frames["pitch_value"])
        pitch_value["batter_side"] = pd.NA
        columns = [
            "pitcher_name",
            "pitcher_id",
            "pitcher_id_key",
            "pitcher_team",
            "pitch_type",
            "batter_side",
            "pitch_count",
            "pitch_value_20_80",
            "pitch_value_0_100",
            "overall_rank",
            "pitch_type_rank",
        ]
        spine = select_if_available(pitch_value, columns, "pitch_value", warnings)
        return spine.rename(
            columns={
                "pitch_value_20_80": "raw_pitch_score_20_80",
                "pitch_value_0_100": "raw_pitch_score_0_100",
            }
        )

    warning = "No usable input files found for a master table."
    warnings.append(warning)
    print(f"WARNING: {warning}")
    return pd.DataFrame(columns=FINAL_COLUMNS)


def merge_pitch_value(
    master: pd.DataFrame, frames: dict[str, pd.DataFrame], warnings: list[str]
) -> pd.DataFrame:
    if "pitch_value" not in frames:
        return master
    pitch_value = add_keys(frames["pitch_value"])
    columns = [
        "pitcher_name",
        "pitcher_id_key",
        "pitcher_team",
        "pitch_type",
        "pitch_count",
        "batted_ball_count",
        "pitch_value_20_80",
        "pitch_value_0_100",
    ]
    pitch_value = select_if_available(pitch_value, columns, "pitch_value", warnings)
    pitch_value = pitch_value.rename(
        columns={
            "pitch_count": "pitch_value_pitch_count_total",
            "pitch_value_20_80": "raw_pitch_score_20_80_from_pitch_value",
            "pitch_value_0_100": "raw_pitch_score_0_100_from_pitch_value",
        }
    )
    merged = master.merge(
        pitch_value,
        on=["pitcher_name", "pitcher_id_key", "pitcher_team", "pitch_type"],
        how="left",
    )
    merged["pitch_count"] = merged.get("pitch_count", pd.Series(dtype="float64")).fillna(
        merged.get("pitch_value_pitch_count_total")
    )
    for target, source in [
        ("raw_pitch_score_20_80", "raw_pitch_score_20_80_from_pitch_value"),
        ("raw_pitch_score_0_100", "raw_pitch_score_0_100_from_pitch_value"),
    ]:
        if target in merged.columns and source in merged.columns:
            merged[target] = merged[target].fillna(merged[source])
        elif source in merged.columns:
            merged[target] = merged[source]
    return merged


def merge_platoon(
    master: pd.DataFrame, frames: dict[str, pd.DataFrame], warnings: list[str]
) -> pd.DataFrame:
    if "platoon_weapons" not in frames:
        return master
    platoon = add_keys(frames["platoon_weapons"])
    columns = [
        "pitcher_name",
        "pitcher_id_key",
        "pitcher_team",
        "pitch_type",
        "platoon_gap",
        "stronger_side",
        "platoon_category",
    ]
    platoon = select_if_available(platoon, columns, "platoon_weapons", warnings)
    platoon = platoon.rename(columns={"stronger_side": "better_side"})
    return master.merge(
        platoon,
        on=["pitcher_name", "pitcher_id_key", "pitcher_team", "pitch_type"],
        how="left",
    )


def merge_movement(
    master: pd.DataFrame, frames: dict[str, pd.DataFrame], warnings: list[str]
) -> pd.DataFrame:
    source_name = "archetypes" if "archetypes" in frames else "movement_model"
    if source_name not in frames:
        return master

    movement = add_keys(frames[source_name])
    columns = [
        "pitcher_name",
        "pitcher_id_key",
        "pitcher_team",
        "pitch_type",
        "ivb",
        "hb",
        "velocity",
        "spin_rate",
        "extension",
        "release_height",
        "release_side",
        "movement_quality_0_100",
        "archetype",
        "cluster",
    ]
    movement = select_if_available(movement, columns, source_name, warnings)
    rename_map = {"ivb": "IVB", "hb": "HB"}
    movement = movement.rename(columns=rename_map)
    if "movement_quality_0_100" in movement.columns:
        movement["movement_quality_20_80"] = (
            20 + 0.6 * movement["movement_quality_0_100"]
        )
    else:
        warnings.append(
            f"`{source_name}` missing `movement_quality_0_100`; "
            "`movement_quality_20_80` cannot be derived."
        )
    return master.merge(
        movement,
        on=["pitcher_name", "pitcher_id_key", "pitcher_team", "pitch_type"],
        how="left",
    )


def finalize_columns(master: pd.DataFrame, warnings: list[str]) -> pd.DataFrame:
    for column in FINAL_COLUMNS:
        if column not in master.columns:
            master[column] = pd.NA
            warning = f"Final output missing source for `{column}`; filled with blank values."
            warnings.append(warning)
            print(f"WARNING: {warning}")

    master = master[FINAL_COLUMNS].copy()
    master = master.loc[:, ~master.columns.duplicated()]
    return master.sort_values(
        ["overall_rank", "pitcher_name", "pitch_type", "batter_side"],
        na_position="last",
    )


def table_lines(df: pd.DataFrame, rows: int = 25) -> list[str]:
    columns = [
        "Rank",
        "Pitcher",
        "Team",
        "Pitch Type",
        "Side",
        "Pitches",
        "Raw",
        "Loc",
        "Final",
        "Final %",
        "Archetype",
        "Platoon",
    ]
    lines = [
        "| " + " | ".join(columns) + " |",
        "|" + "|".join(["---"] * len(columns)) + "|",
    ]
    for row in df.head(rows).itertuples(index=False):
        side = "" if pd.isna(row.batter_side) else f"{row.batter_side}HH"
        lines.append(
            "| "
            + " | ".join(
                [
                    "" if pd.isna(row.overall_rank) else str(int(row.overall_rank)),
                    str(row.pitcher_name),
                    str(row.pitcher_team),
                    str(row.pitch_type),
                    side,
                    "" if pd.isna(row.pitch_count) else f"{int(row.pitch_count):,}",
                    "" if pd.isna(row.raw_pitch_score_20_80) else f"{row.raw_pitch_score_20_80:.1f}",
                    "" if pd.isna(row.location_score_20_80) else f"{row.location_score_20_80:.1f}",
                    "" if pd.isna(row.final_pitch_score_20_80) else f"{row.final_pitch_score_20_80:.1f}",
                    "" if pd.isna(row.final_pitch_score_0_100) else f"{row.final_pitch_score_0_100:.1f}",
                    "" if pd.isna(row.archetype) else str(row.archetype),
                    "" if pd.isna(row.platoon_category) else str(row.platoon_category),
                ]
            )
            + " |"
        )
    return lines


def write_report(master: pd.DataFrame, warnings: list[str]) -> None:
    available_columns = [column for column in FINAL_COLUMNS if column in master.columns]
    top_final = master.dropna(subset=["final_pitch_score_20_80"]).sort_values(
        "final_pitch_score_20_80", ascending=False
    )

    lines = [
        "# Master Pitch Evaluation Table",
        "",
        f"- Output file: `{OUTPUT_PATH}`",
        f"- Row count: {len(master):,}",
        "",
        "## Available Columns",
        "",
    ]
    lines.extend(f"- `{column}`" for column in available_columns)
    lines.extend(["", "## Missing Column Warnings", ""])
    if warnings:
        lines.extend(f"- {warning}" for warning in warnings)
    else:
        lines.append("- None.")

    lines.extend(
        [
            "",
            "## Top 25 Final Pitch Scores",
            "",
            *table_lines(top_final, rows=25),
            "",
            "## Top 10 by Pitch Type and Batter Side",
            "",
        ]
    )
    grouped = top_final.groupby(["pitch_type", "batter_side"], dropna=False)
    for (pitch_type, batter_side), group in grouped:
        side = "" if pd.isna(batter_side) else f" vs {batter_side}HH"
        lines.extend([f"### {pitch_type}{side}", ""])
        lines.extend(table_lines(group, rows=10))
        lines.append("")

    REPORT_PATH.write_text("\n".join(lines), encoding="utf-8")


def main() -> None:
    frames, warnings = load_inputs()
    master = create_spine(frames, warnings)
    master = merge_pitch_value(master, frames, warnings)
    master = merge_platoon(master, frames, warnings)
    master = merge_movement(master, frames, warnings)
    master = finalize_columns(master, warnings)

    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    REPORT_PATH.parent.mkdir(parents=True, exist_ok=True)
    master.to_csv(OUTPUT_PATH, index=False)
    write_report(master, warnings)

    print(f"Wrote master table: {OUTPUT_PATH}")
    print(f"Wrote report: {REPORT_PATH}")
    print(f"Rows: {len(master):,}")
    print(f"Columns: {len(master.columns):,}")


if __name__ == "__main__":
    main()
