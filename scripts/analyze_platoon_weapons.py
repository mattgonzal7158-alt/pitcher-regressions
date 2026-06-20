from __future__ import annotations

from pathlib import Path

import numpy as np
import pandas as pd


INPUT_PATH = Path("data/processed/pitch_leaderboard_splits.csv")
OUTPUT_PATH = Path("data/processed/platoon_weapon_scores.csv")
REPORT_PATH = Path("reports/platoon_weapon_report.md")

BALANCED_GAP_MAX = 3.0
KILLER_GAP_MIN = 5.0
REVERSE_TYPICAL_GAP_MIN = 2.0
WEAPON_SCORE_MIN = 55.0

REQUIRED_COLUMNS = {
    "pitcher_name",
    "pitcher_id",
    "pitcher_team",
    "pitch_type",
    "batter_side",
    "split_pitch_count",
    "pitch_value_20_80",
    "location_score_20_80",
    "final_pitch_score",
    "final_pitch_score_0_100",
}


def normalize_batter_side(series: pd.Series) -> pd.Series:
    side = series.astype("string").str.upper().str.strip()
    return side.replace({"RIGHT": "R", "LEFT": "L", "RHH": "R", "LHH": "L"})


def prepare_splits(df: pd.DataFrame) -> pd.DataFrame:
    missing = sorted(REQUIRED_COLUMNS.difference(df.columns))
    if missing:
        raise ValueError(f"Missing required split leaderboard columns: {missing}")

    work = df[list(REQUIRED_COLUMNS)].copy()
    work["batter_side"] = normalize_batter_side(work["batter_side"])
    numeric_columns = [
        "split_pitch_count",
        "pitch_value_20_80",
        "location_score_20_80",
        "final_pitch_score",
        "final_pitch_score_0_100",
    ]
    for column in numeric_columns:
        work[column] = pd.to_numeric(work[column], errors="coerce")

    return work.dropna(
        subset=[
            "pitcher_name",
            "pitch_type",
            "batter_side",
            "final_pitch_score",
        ]
    )


def pivot_split_scores(splits: pd.DataFrame) -> pd.DataFrame:
    keys = ["pitcher_name", "pitcher_id", "pitcher_team", "pitch_type"]
    pivot = splits.pivot_table(
        index=keys,
        columns="batter_side",
        values=[
            "split_pitch_count",
            "pitch_value_20_80",
            "location_score_20_80",
            "final_pitch_score",
            "final_pitch_score_0_100",
        ],
        aggfunc="first",
    )
    pivot.columns = [f"{metric}_vs_{side.lower()}hh" for metric, side in pivot.columns]
    pivot = pivot.reset_index()

    required_scores = ["final_pitch_score_vs_rhh", "final_pitch_score_vs_lhh"]
    return pivot.dropna(subset=required_scores).copy()


def categorize(row: pd.Series) -> str:
    gap = row["platoon_gap"]
    abs_gap = abs(gap)
    typical_gap = row["pitch_type_median_gap"]
    score_rhh = row["final_pitch_score_vs_rhh"]
    score_lhh = row["final_pitch_score_vs_lhh"]
    stronger_score = max(score_rhh, score_lhh)

    if abs_gap <= BALANCED_GAP_MAX:
        return "Balanced Weapon"
    if (
        abs_gap >= KILLER_GAP_MIN
        and abs(typical_gap) >= REVERSE_TYPICAL_GAP_MIN
        and np.sign(gap) != np.sign(typical_gap)
        and stronger_score >= WEAPON_SCORE_MIN
    ):
        return "Reverse Split Weapon"
    if gap >= KILLER_GAP_MIN:
        return "Right-Handed Killer"
    if gap <= -KILLER_GAP_MIN:
        return "Left-Handed Killer"
    return "Balanced Weapon"


def create_platoon_scores(splits: pd.DataFrame) -> pd.DataFrame:
    scored = pivot_split_scores(splits)
    scored["platoon_gap"] = (
        scored["final_pitch_score_vs_rhh"] - scored["final_pitch_score_vs_lhh"]
    )
    scored["absolute_platoon_gap"] = scored["platoon_gap"].abs()
    scored["average_final_pitch_score"] = scored[
        ["final_pitch_score_vs_rhh", "final_pitch_score_vs_lhh"]
    ].mean(axis=1)
    scored["minimum_final_pitch_score"] = scored[
        ["final_pitch_score_vs_rhh", "final_pitch_score_vs_lhh"]
    ].min(axis=1)
    scored["stronger_side"] = np.select(
        [
            scored["platoon_gap"].gt(BALANCED_GAP_MAX),
            scored["platoon_gap"].lt(-BALANCED_GAP_MAX),
        ],
        ["RHH", "LHH"],
        default="Balanced",
    )

    pitch_type_medians = (
        scored.groupby("pitch_type")["platoon_gap"]
        .median()
        .rename("pitch_type_median_gap")
        .reset_index()
    )
    scored = scored.merge(pitch_type_medians, on="pitch_type", how="left")
    scored["platoon_category"] = scored.apply(categorize, axis=1)
    scored["right_handed_killer_rank"] = (
        scored["platoon_gap"].rank(method="first", ascending=False).astype(int)
    )
    scored["left_handed_killer_rank"] = (
        scored["platoon_gap"].rank(method="first", ascending=True).astype(int)
    )
    scored["balanced_rank"] = (
        scored["average_final_pitch_score"].where(
            scored["absolute_platoon_gap"].le(BALANCED_GAP_MAX)
        )
        .rank(method="first", ascending=False)
    )

    columns = [
        "pitcher_name",
        "pitcher_id",
        "pitcher_team",
        "pitch_type",
        "split_pitch_count_vs_rhh",
        "split_pitch_count_vs_lhh",
        "pitch_value_20_80_vs_rhh",
        "pitch_value_20_80_vs_lhh",
        "location_score_20_80_vs_rhh",
        "location_score_20_80_vs_lhh",
        "final_pitch_score_vs_rhh",
        "final_pitch_score_vs_lhh",
        "final_pitch_score_0_100_vs_rhh",
        "final_pitch_score_0_100_vs_lhh",
        "platoon_gap",
        "absolute_platoon_gap",
        "average_final_pitch_score",
        "minimum_final_pitch_score",
        "pitch_type_median_gap",
        "stronger_side",
        "platoon_category",
        "right_handed_killer_rank",
        "left_handed_killer_rank",
        "balanced_rank",
    ]
    return scored[columns].sort_values(
        ["absolute_platoon_gap", "average_final_pitch_score"], ascending=[False, False]
    )


def fmt(value: float, digits: int = 1) -> str:
    return "" if pd.isna(value) else f"{value:.{digits}f}"


def leaderboard_table(df: pd.DataFrame, rows: int = 20) -> list[str]:
    columns = [
        "Pitcher",
        "Team",
        "Pitch Type",
        "RHH",
        "LHH",
        "Gap",
        "Avg",
        "R Pitches",
        "L Pitches",
        "Category",
    ]
    lines = [
        "| " + " | ".join(columns) + " |",
        "|" + "|".join(["---"] * len(columns)) + "|",
    ]
    for row in df.head(rows).itertuples(index=False):
        lines.append(
            "| "
            + " | ".join(
                [
                    str(row.pitcher_name),
                    str(row.pitcher_team),
                    str(row.pitch_type),
                    fmt(row.final_pitch_score_vs_rhh),
                    fmt(row.final_pitch_score_vs_lhh),
                    fmt(row.platoon_gap),
                    fmt(row.average_final_pitch_score),
                    f"{int(row.split_pitch_count_vs_rhh):,}",
                    f"{int(row.split_pitch_count_vs_lhh):,}",
                    str(row.platoon_category),
                ]
            )
            + " |"
        )
    return lines


def write_report(platoon_scores: pd.DataFrame, input_rows: int) -> None:
    right_killers = platoon_scores.loc[
        (platoon_scores["platoon_gap"].ge(KILLER_GAP_MIN))
        & (platoon_scores["final_pitch_score_vs_rhh"].ge(WEAPON_SCORE_MIN))
    ].sort_values(["platoon_gap", "final_pitch_score_vs_rhh"], ascending=[False, False])
    left_killers = platoon_scores.loc[
        (platoon_scores["platoon_gap"].le(-KILLER_GAP_MIN))
        & (platoon_scores["final_pitch_score_vs_lhh"].ge(WEAPON_SCORE_MIN))
    ].sort_values(["platoon_gap", "final_pitch_score_vs_lhh"], ascending=[True, False])
    balanced = platoon_scores.loc[
        (platoon_scores["absolute_platoon_gap"].le(BALANCED_GAP_MAX))
        & (platoon_scores["minimum_final_pitch_score"].ge(WEAPON_SCORE_MIN))
    ].sort_values(["average_final_pitch_score", "absolute_platoon_gap"], ascending=[False, True])
    category_counts = (
        platoon_scores["platoon_category"].value_counts().rename_axis("category")
    )

    lines = [
        "# Platoon Weapon Report",
        "",
        f"- Input file: `{INPUT_PATH}`",
        f"- Output file: `{OUTPUT_PATH}`",
        f"- Input split rows: {input_rows:,}",
        f"- Pitcher + pitch type rows with both RHH and LHH scores: {len(platoon_scores):,}",
        f"- Platoon gap: `score_vs_rhh - score_vs_lhh`",
        "- Positive gap means the pitch grades better versus RHH. Negative gap means it grades better versus LHH.",
        "- Reverse Split Weapon is defined from this file only: the pitch's gap is at least 5 points and opposite the typical median gap for that pitch type.",
        "",
        "## Category Counts",
        "",
        "| Category | Count |",
        "|---|---:|",
    ]
    for category, count in category_counts.items():
        lines.append(f"| {category} | {count:,} |")

    lines.extend(
        [
            "",
            "## Top 20 Right-Handed Killing Pitches",
            "",
            *leaderboard_table(right_killers, rows=20),
            "",
            "## Top 20 Left-Handed Killing Pitches",
            "",
            *leaderboard_table(left_killers, rows=20),
            "",
            "## Top 20 Balanced Pitches",
            "",
            *leaderboard_table(balanced, rows=20),
            "",
            "## Pitch Type Typical Gaps",
            "",
            "| Pitch Type | Median Gap | Rows |",
            "|---|---:|---:|",
        ]
    )
    type_summary = (
        platoon_scores.groupby("pitch_type")
        .agg(median_gap=("platoon_gap", "median"), rows=("platoon_gap", "size"))
        .reset_index()
        .sort_values("median_gap", ascending=False)
    )
    for row in type_summary.itertuples(index=False):
        lines.append(f"| {row.pitch_type} | {row.median_gap:.1f} | {int(row.rows):,} |")

    REPORT_PATH.write_text("\n".join(lines), encoding="utf-8")


def main() -> None:
    splits_df = pd.read_csv(INPUT_PATH)
    splits = prepare_splits(splits_df)
    platoon_scores = create_platoon_scores(splits)

    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    REPORT_PATH.parent.mkdir(parents=True, exist_ok=True)
    platoon_scores.to_csv(OUTPUT_PATH, index=False)
    write_report(platoon_scores, input_rows=len(splits_df))

    print(f"Wrote platoon scores: {OUTPUT_PATH}")
    print(f"Wrote report: {REPORT_PATH}")
    print(f"Pitcher + pitch type rows with both sides: {len(platoon_scores):,}")
    print("\nTop 10 RHH weapons:")
    print(
        platoon_scores.sort_values("platoon_gap", ascending=False)
        [
            [
                "pitcher_name",
                "pitcher_team",
                "pitch_type",
                "final_pitch_score_vs_rhh",
                "final_pitch_score_vs_lhh",
                "platoon_gap",
                "platoon_category",
            ]
        ]
        .head(10)
        .to_string(index=False)
    )


if __name__ == "__main__":
    main()
