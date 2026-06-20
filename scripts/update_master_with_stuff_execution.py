from __future__ import annotations

from pathlib import Path

import pandas as pd


MASTER_PATH = Path("data/processed/master_pitch_evaluation_table.csv")
STUFF_PATH = Path("data/processed/stuff_plus_scores.csv")
EXECUTION_PATH = Path("data/processed/execution_plus_scores.csv")
OUTPUT_PATH = Path("data/processed/master_pitch_evaluation_table_v2.csv")
REPORT_PATH = Path("reports/master_pitch_evaluation_table_v2_report.md")

JOIN_KEYS = ["pitcher_name", "pitcher_id_key", "pitcher_team", "pitch_type", "batter_side"]

STUFF_COLUMNS = [
    "stuff_plus_raw",
    "stuff_plus_20_80",
    "stuff_plus_0_100",
]
EXECUTION_COLUMNS = [
    "execution_raw",
    "execution_plus_20_80",
    "execution_plus_0_100",
    "execution_quadrant",
]
OUTPUT_RENAME = {
    "execution_quadrant": "quadrant_label",
}


def normalize_pitcher_id(series: pd.Series) -> pd.Series:
    numeric = pd.to_numeric(series, errors="coerce")
    return numeric.astype("Int64").astype("string")


def normalize_batter_side(series: pd.Series) -> pd.Series:
    side = series.astype("string").str.upper().str.strip()
    return side.replace({"RIGHT": "R", "LEFT": "L", "RHH": "R", "LHH": "L"})


def add_join_keys(df: pd.DataFrame) -> pd.DataFrame:
    work = df.copy()
    if "pitcher_id" in work.columns:
        work["pitcher_id_key"] = normalize_pitcher_id(work["pitcher_id"])
    if "batter_side" in work.columns:
        work["batter_side"] = normalize_batter_side(work["batter_side"])
    return work


def required_columns(
    df: pd.DataFrame, columns: list[str], source_name: str
) -> list[str]:
    missing = [column for column in columns if column not in df.columns]
    if missing:
        raise ValueError(f"{source_name} missing required columns: {missing}")
    return columns


def dedupe_before_join(df: pd.DataFrame, source_name: str) -> pd.DataFrame:
    duplicated = df.duplicated(JOIN_KEYS, keep=False)
    if duplicated.any():
        duplicate_count = int(duplicated.sum())
        print(
            f"WARNING: {source_name} has {duplicate_count:,} duplicate key rows; "
            "keeping the first occurrence."
        )
        return df.drop_duplicates(JOIN_KEYS, keep="first")
    return df


def update_master(
    master: pd.DataFrame, stuff: pd.DataFrame, execution: pd.DataFrame
) -> tuple[pd.DataFrame, dict[str, int]]:
    master = add_join_keys(master)
    stuff = add_join_keys(stuff)
    execution = add_join_keys(execution)

    required_columns(master, JOIN_KEYS, "master")
    required_columns(stuff, [*JOIN_KEYS, *STUFF_COLUMNS], "stuff_plus_scores")
    required_columns(execution, [*JOIN_KEYS, *EXECUTION_COLUMNS], "execution_plus_scores")

    stuff_join = dedupe_before_join(stuff[[*JOIN_KEYS, *STUFF_COLUMNS]], "Stuff+")
    execution_join = dedupe_before_join(
        execution[[*JOIN_KEYS, *EXECUTION_COLUMNS]], "Execution+"
    )

    for column in [*STUFF_COLUMNS, *EXECUTION_COLUMNS, *OUTPUT_RENAME.values()]:
        if column in master.columns:
            master = master.drop(columns=column)

    updated = master.merge(stuff_join, on=JOIN_KEYS, how="left")
    stuff_matches = int(updated["stuff_plus_raw"].notna().sum())
    updated = updated.merge(execution_join, on=JOIN_KEYS, how="left")
    execution_matches = int(updated["execution_raw"].notna().sum())
    updated = updated.rename(columns=OUTPUT_RENAME)

    updated = updated.drop(columns=["pitcher_id_key"])
    stats = {
        "master_rows": len(master),
        "stuff_rows": len(stuff),
        "execution_rows": len(execution),
        "stuff_matches": stuff_matches,
        "execution_matches": execution_matches,
        "output_rows": len(updated),
    }
    return updated, stats


def format_value(value: object) -> str:
    if pd.isna(value):
        return ""
    if isinstance(value, float):
        return f"{value:.1f}"
    return str(value)


def table_lines(df: pd.DataFrame, rows: int = 25) -> list[str]:
    columns = [
        "Pitcher",
        "Team",
        "Pitch Type",
        "Side",
        "Final",
        "Stuff+",
        "Execution+",
        "Quadrant",
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
                    str(row.pitcher_name),
                    str(row.pitcher_team),
                    str(row.pitch_type),
                    side,
                    format_value(row.final_pitch_score_20_80),
                    format_value(row.stuff_plus_20_80),
                    format_value(row.execution_plus_20_80),
                    "" if pd.isna(row.quadrant_label) else str(row.quadrant_label),
                ]
            )
            + " |"
        )
    return lines


def write_report(updated: pd.DataFrame, stats: dict[str, int]) -> None:
    missing_stuff = stats["output_rows"] - stats["stuff_matches"]
    missing_execution = stats["output_rows"] - stats["execution_matches"]
    top = updated.dropna(subset=["final_pitch_score_20_80"]).sort_values(
        "final_pitch_score_20_80", ascending=False
    )
    quadrant_counts = (
        updated["quadrant_label"].fillna("<missing>").value_counts().rename_axis("quadrant")
    )

    lines = [
        "# Master Pitch Evaluation Table v2",
        "",
        f"- Master input: `{MASTER_PATH}` ({stats['master_rows']:,} rows)",
        f"- Stuff+ input: `{STUFF_PATH}` ({stats['stuff_rows']:,} rows)",
        f"- Execution+ input: `{EXECUTION_PATH}` ({stats['execution_rows']:,} rows)",
        f"- Output file: `{OUTPUT_PATH}`",
        f"- Output rows: {stats['output_rows']:,}",
        f"- Stuff+ matched rows: {stats['stuff_matches']:,}",
        f"- Execution+ matched rows: {stats['execution_matches']:,}",
        f"- Rows missing Stuff+: {missing_stuff:,}",
        f"- Rows missing Execution+: {missing_execution:,}",
        "",
        "## Added Columns",
        "",
        "- `stuff_plus_raw`",
        "- `stuff_plus_20_80`",
        "- `stuff_plus_0_100`",
        "- `execution_raw`",
        "- `execution_plus_20_80`",
        "- `execution_plus_0_100`",
        "- `quadrant_label`",
        "",
        "## Quadrant Counts",
        "",
        "| Quadrant | Rows |",
        "|---|---:|",
    ]
    for quadrant, count in quadrant_counts.items():
        lines.append(f"| {quadrant} | {count:,} |")

    lines.extend(
        [
            "",
            "## Top 25 Final Pitch Scores",
            "",
            *table_lines(top, rows=25),
        ]
    )
    REPORT_PATH.write_text("\n".join(lines), encoding="utf-8")


def main() -> None:
    master = pd.read_csv(MASTER_PATH)
    stuff = pd.read_csv(STUFF_PATH)
    execution = pd.read_csv(EXECUTION_PATH)
    updated, stats = update_master(master, stuff, execution)

    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    REPORT_PATH.parent.mkdir(parents=True, exist_ok=True)
    updated.to_csv(OUTPUT_PATH, index=False)
    write_report(updated, stats)

    print(f"Wrote master v2 table: {OUTPUT_PATH}")
    print(f"Wrote report: {REPORT_PATH}")
    print(f"Rows: {stats['output_rows']:,}")
    print(f"Stuff+ matches: {stats['stuff_matches']:,}")
    print(f"Execution+ matches: {stats['execution_matches']:,}")


if __name__ == "__main__":
    main()
