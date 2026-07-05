from __future__ import annotations

from pathlib import Path

import pandas as pd


INPUT_PATH = Path("data/processed/master_pitch_evaluation_table_v2.csv")
OUTPUT_PATH = Path("data/processed/final_scouting_leaderboards.csv")
REPORT_PATH = Path("reports/final_scouting_leaderboards.md")

ROWS_PER_BOARD: int | None = None
ONE_SIDE_GAP_MIN = 5.0

DISPLAY_COLUMNS = [
    "pitcher_name",
    "pitcher_team",
    "pitch_type",
    "batter_side",
    "pitch_count",
    "final_pitch_score_20_80",
    "raw_pitch_score_20_80",
    "groundball_score_20_80",
    "groundball_score_rank",
    "groundball_score_pitch_type_rank",
    "strikeout_score_20_80",
    "strikeout_score_rank",
    "strikeout_score_pitch_type_rank",
    "line_drive_score_20_80",
    "line_drive_score_rank",
    "line_drive_score_pitch_type_rank",
    "flyball_score_20_80",
    "flyball_score_rank",
    "flyball_score_pitch_type_rank",
    "location_score_20_80",
    "stuff_plus_20_80",
    "execution_plus_20_80",
    "movement_quality_20_80",
    "archetype",
    "platoon_category",
    "quadrant_label",
    "overall_rank",
    "pitch_type_rank",
    "pitch_type_batter_side_rank",
]


def require_columns(df: pd.DataFrame) -> None:
    missing = sorted(set(DISPLAY_COLUMNS).difference(df.columns))
    if missing:
        raise ValueError(f"Missing required columns: {missing}")


def numeric_sort(df: pd.DataFrame, column: str, ascending: bool = False) -> pd.DataFrame:
    work = df.copy()
    work[column] = pd.to_numeric(work[column], errors="coerce")
    return work.dropna(subset=[column]).sort_values(column, ascending=ascending)


def build_leaderboards(df: pd.DataFrame) -> dict[str, pd.DataFrame]:
    final_df = numeric_sort(df, "final_pitch_score_20_80")
    stuff_df = numeric_sort(df, "stuff_plus_20_80")
    execution_df = numeric_sort(df, "execution_plus_20_80")
    location_df = numeric_sort(df, "location_score_20_80")
    groundball_df = numeric_sort(df, "groundball_score_20_80")
    strikeout_df = numeric_sort(df, "strikeout_score_20_80")
    line_drive_df = numeric_sort(df, "line_drive_score_20_80")
    flyball_df = numeric_sort(df, "flyball_score_20_80")

    vs_rhh = numeric_sort(df.loc[df["batter_side"].eq("R")], "final_pitch_score_20_80")
    vs_lhh = numeric_sort(df.loc[df["batter_side"].eq("L")], "final_pitch_score_20_80")

    development = numeric_sort(
        df.loc[df["quadrant_label"].eq("Development Target")],
        "stuff_plus_20_80",
    )
    balanced = numeric_sort(
        df.loc[df["platoon_category"].eq("Balanced Weapon")],
        "final_pitch_score_20_80",
    )

    one_side_mask = df["platoon_category"].isin(
        ["Right-Handed Killer", "Left-Handed Killer", "Reverse Split Weapon"]
    )
    if "platoon_gap" in df.columns:
        gap = pd.to_numeric(df["platoon_gap"], errors="coerce").abs()
        one_side_mask = one_side_mask | gap.ge(ONE_SIDE_GAP_MIN)
    one_side = numeric_sort(df.loc[one_side_mask], "final_pitch_score_20_80")

    return {
        "Best Overall Pitches": final_df,
        "Best Stuff+": stuff_df,
        "Best Execution+": execution_df,
        "Best Location Score": location_df,
        "Best Ground Ball Score": groundball_df,
        "Best Strikeout Score": strikeout_df,
        "Best Line Drive Suppression": line_drive_df,
        "Best Fly Ball Suppression": flyball_df,
        "Best vs RHH": vs_rhh,
        "Best vs LHH": vs_lhh,
        "Best Development Targets": development,
        "Best Balanced Weapons": balanced,
        "Best One-Side Weapons": one_side,
    }


def create_output(leaderboards: dict[str, pd.DataFrame]) -> pd.DataFrame:
    rows = []
    for name, board in leaderboards.items():
        subset = board.copy()
        subset.insert(0, "leaderboard_rank", range(1, len(subset) + 1))
        subset.insert(0, "leaderboard", name)
        rows.append(subset[["leaderboard", "leaderboard_rank", *DISPLAY_COLUMNS]])
    return pd.concat(rows, ignore_index=True) if rows else pd.DataFrame()


def fmt(value: object, digits: int = 1) -> str:
    if pd.isna(value):
        return ""
    if isinstance(value, float):
        return f"{value:.{digits}f}"
    return str(value)


def report_table(board: pd.DataFrame, rows: int | None = ROWS_PER_BOARD) -> list[str]:
    columns = [
        "Rank",
        "Pitcher",
        "Team",
        "Pitch",
        "Side",
        "Pitches",
        "Final",
        "Raw",
        "GB",
        "K",
        "LD Supp",
        "FB Supp",
        "Loc",
        "Stuff+",
        "Exec+",
        "Move",
        "Archetype",
        "Platoon",
        "Quadrant",
    ]
    lines = [
        "| " + " | ".join(columns) + " |",
        "|" + "|".join(["---"] * len(columns)) + "|",
    ]
    report_rows = board if rows is None else board.head(rows)
    for rank, row in enumerate(report_rows.itertuples(index=False), start=1):
        side = "" if pd.isna(row.batter_side) else f"{row.batter_side}HH"
        lines.append(
            "| "
            + " | ".join(
                [
                    str(rank),
                    str(row.pitcher_name),
                    str(row.pitcher_team),
                    str(row.pitch_type),
                    side,
                    "" if pd.isna(row.pitch_count) else f"{int(row.pitch_count):,}",
                    fmt(row.final_pitch_score_20_80),
                    fmt(row.raw_pitch_score_20_80),
                    fmt(row.groundball_score_20_80),
                    fmt(row.strikeout_score_20_80),
                    fmt(row.line_drive_score_20_80),
                    fmt(row.flyball_score_20_80),
                    fmt(row.location_score_20_80),
                    fmt(row.stuff_plus_20_80),
                    fmt(row.execution_plus_20_80),
                    fmt(row.movement_quality_20_80),
                    "" if pd.isna(row.archetype) else str(row.archetype),
                    "" if pd.isna(row.platoon_category) else str(row.platoon_category),
                    "" if pd.isna(row.quadrant_label) else str(row.quadrant_label),
                ]
            )
            + " |"
        )
    return lines


def write_report(leaderboards: dict[str, pd.DataFrame], output_rows: int) -> None:
    lines = [
        "# Final Scouting Leaderboards",
        "",
        f"- Input file: `{INPUT_PATH}`",
        f"- CSV output: `{OUTPUT_PATH}`",
        f"- Leaderboard rows exported: {output_rows:,}",
        "- Rows per leaderboard: all qualifying rows",
        "",
    ]
    for name, board in leaderboards.items():
        lines.extend([f"## {name}", ""])
        if board.empty:
            lines.append("No qualifying rows.")
        else:
            lines.extend(report_table(board))
        lines.append("")

    REPORT_PATH.write_text("\n".join(lines), encoding="utf-8")


def main() -> None:
    df = pd.read_csv(INPUT_PATH)
    require_columns(df)
    leaderboards = build_leaderboards(df)
    output = create_output(leaderboards)

    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    REPORT_PATH.parent.mkdir(parents=True, exist_ok=True)
    output.to_csv(OUTPUT_PATH, index=False)
    write_report(leaderboards, output_rows=len(output))

    print(f"Wrote final scouting leaderboard CSV: {OUTPUT_PATH}")
    print(f"Wrote report: {REPORT_PATH}")
    print(f"Exported leaderboard rows: {len(output):,}")


if __name__ == "__main__":
    main()
