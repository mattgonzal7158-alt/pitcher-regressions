from __future__ import annotations

from pathlib import Path

import pandas as pd


PITCH_VALUE_PATH = Path("data/processed/pitch_value_scores_with_type_rank.csv")
LOCATION_SCORE_PATH = Path("data/processed/location_scores.csv")
OUTPUT_PATH = Path("data/processed/pitch_leaderboard_splits.csv")
REPORT_PATH = Path("reports/pitch_leaderboard_splits.md")

PITCH_VALUE_WEIGHT = 0.70
LOCATION_SCORE_WEIGHT = 0.30

PITCH_TYPE_NORMALIZATION = {
    "Fastball": "Four-Seam",
    "Two-Seam": "Sinker",
}

PITCH_VALUE_COLUMNS = {
    "pitcher_name",
    "pitcher_id",
    "pitcher_team",
    "pitch_type",
    "pitch_count",
    "xwoba_frontier",
    "pitch_value_raw",
    "pitch_value_20_80",
    "pitch_value_0_100",
    "overall_rank",
    "pitch_type_rank",
}

LOCATION_SCORE_COLUMNS = {
    "pitcher_name",
    "pitcher_id",
    "pitcher_team",
    "pitch_type",
    "batter_side",
    "pitch_count",
    "average_location_advantage",
    "median_location_advantage",
    "location_score_raw",
    "location_score_20_80",
    "location_score_0_100",
}


def normalize_pitch_type(series: pd.Series) -> pd.Series:
    return series.astype("string").replace(PITCH_TYPE_NORMALIZATION)


def normalize_batter_side(series: pd.Series) -> pd.Series:
    side = series.astype("string").str.upper().str.strip()
    return side.replace({"RIGHT": "R", "LEFT": "L", "RHH": "R", "LHH": "L"})


def normalize_pitcher_id(series: pd.Series) -> pd.Series:
    numeric = pd.to_numeric(series, errors="coerce")
    return numeric.astype("Int64").astype("string")


def percentile_rank(values: pd.Series) -> pd.Series:
    return values.rank(method="average", pct=True).mul(100)


def prepare_pitch_value(df: pd.DataFrame) -> pd.DataFrame:
    missing = sorted(PITCH_VALUE_COLUMNS.difference(df.columns))
    if missing:
        raise ValueError(f"Missing required Pitch Value columns: {missing}")

    work = df[list(PITCH_VALUE_COLUMNS)].copy()
    work["pitch_type"] = normalize_pitch_type(work["pitch_type"])
    work["pitcher_id_key"] = normalize_pitcher_id(work["pitcher_id"])
    work = work.rename(
        columns={
            "pitch_count": "pitch_value_pitch_count",
            "xwoba_frontier": "pitch_value_xwoba_frontier",
            "overall_rank": "pitch_value_overall_rank",
            "pitch_type_rank": "pitch_value_pitch_type_rank",
        }
    )
    return work


def prepare_location_score(df: pd.DataFrame) -> pd.DataFrame:
    missing = sorted(LOCATION_SCORE_COLUMNS.difference(df.columns))
    if missing:
        raise ValueError(f"Missing required Location Score columns: {missing}")

    work = df[list(LOCATION_SCORE_COLUMNS)].copy()
    work["pitch_type"] = normalize_pitch_type(work["pitch_type"])
    work["batter_side"] = normalize_batter_side(work["batter_side"])
    work["pitcher_id_key"] = normalize_pitcher_id(work["pitcher_id"])
    work = work.rename(columns={"pitch_count": "split_pitch_count"})
    return work


def create_split_leaderboard(
    pitch_value: pd.DataFrame, location_score: pd.DataFrame
) -> pd.DataFrame:
    merge_keys = ["pitcher_name", "pitcher_id_key", "pitcher_team", "pitch_type"]
    joined = location_score.merge(
        pitch_value.drop(columns=["pitcher_id"]),
        on=merge_keys,
        how="inner",
        suffixes=("", "_pitch_value"),
    )
    joined = joined.rename(columns={"pitcher_id": "pitcher_id"})
    joined["final_pitch_score_raw"] = (
        PITCH_VALUE_WEIGHT * joined["pitch_value_20_80"]
        + LOCATION_SCORE_WEIGHT * joined["location_score_20_80"]
    )
    joined["final_pitch_score"] = joined["final_pitch_score_raw"]
    joined["final_pitch_score_0_100"] = percentile_rank(joined["final_pitch_score_raw"])
    joined["overall_rank"] = (
        joined["final_pitch_score_raw"]
        .rank(method="first", ascending=False)
        .astype(int)
    )
    joined["pitch_type_rank"] = (
        joined.groupby("pitch_type")["final_pitch_score_raw"]
        .rank(method="first", ascending=False)
        .astype(int)
    )
    joined["pitch_type_batter_side_rank"] = (
        joined.groupby(["pitch_type", "batter_side"])["final_pitch_score_raw"]
        .rank(method="first", ascending=False)
        .astype(int)
    )

    columns = [
        "overall_rank",
        "pitch_type_rank",
        "pitch_type_batter_side_rank",
        "pitcher_name",
        "pitcher_id",
        "pitcher_team",
        "pitch_type",
        "batter_side",
        "split_pitch_count",
        "pitch_value_pitch_count",
        "pitch_value_20_80",
        "pitch_value_0_100",
        "location_score_20_80",
        "location_score_0_100",
        "average_location_advantage",
        "median_location_advantage",
        "final_pitch_score_raw",
        "final_pitch_score",
        "final_pitch_score_0_100",
        "pitch_value_raw",
        "location_score_raw",
        "pitch_value_xwoba_frontier",
        "pitch_value_overall_rank",
        "pitch_value_pitch_type_rank",
    ]
    return joined[columns].sort_values("overall_rank")


def format_float(value: float, digits: int = 1) -> str:
    return "" if pd.isna(value) else f"{value:.{digits}f}"


def format_advantage(value: float) -> str:
    return "" if pd.isna(value) else f"{value:.4f}"


def leaderboard_table(df: pd.DataFrame, rows: int = 30) -> list[str]:
    columns = [
        "Rank",
        "Pitcher",
        "Team",
        "Pitch Type",
        "Batter Side",
        "Split Pitches",
        "PVS",
        "Loc",
        "Final",
        "Final %",
        "Avg Loc Adv",
        "Type Rank",
        "Type/Side Rank",
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
                    str(row.overall_rank),
                    str(row.pitcher_name),
                    str(row.pitcher_team),
                    str(row.pitch_type),
                    f"{row.batter_side}HH",
                    f"{int(row.split_pitch_count):,}",
                    format_float(row.pitch_value_20_80),
                    format_float(row.location_score_20_80),
                    format_float(row.final_pitch_score),
                    format_float(row.final_pitch_score_0_100),
                    format_advantage(row.average_location_advantage),
                    str(row.pitch_type_rank),
                    str(row.pitch_type_batter_side_rank),
                ]
            )
            + " |"
        )
    return lines


def write_report(leaderboard: pd.DataFrame, pitch_value_rows: int, location_rows: int) -> None:
    lines = [
        "# Handedness-Specific Pitch Leaderboards",
        "",
        f"- Pitch Value input: `{PITCH_VALUE_PATH}` ({pitch_value_rows:,} rows)",
        f"- Location Score input: `{LOCATION_SCORE_PATH}` ({location_rows:,} rows)",
        f"- Output file: `{OUTPUT_PATH}`",
        f"- Joined leaderboard rows: {len(leaderboard):,}",
        f"- Formula: `{PITCH_VALUE_WEIGHT:.2f} * pitch_value_20_80 + {LOCATION_SCORE_WEIGHT:.2f} * location_score_20_80`",
        "- Pitch Value is pitcher + pitch type level; Location Score supplies the batter-side split.",
        "- Higher scores are better.",
        "",
        "## Method",
        "",
        "The leaderboard joins Pitch Value to Location Score by pitcher, team, and normalized pitch type. Because the Pitch Value table is not handedness-specific, each pitcher-pitch Pitch Value is paired with its available LHH and/or RHH Location Score rows.",
        "",
        "`final_pitch_score_raw` and `final_pitch_score` are the weighted 20-80 blend. `final_pitch_score_0_100` is the percentile rank of that blended score among all split rows.",
        "",
        "## Overall Leaderboard",
        "",
        *leaderboard_table(leaderboard, rows=40),
        "",
        "## Pitch Type + Batter Side Leaderboards",
        "",
    ]

    for (pitch_type, batter_side), group in leaderboard.groupby(["pitch_type", "batter_side"]):
        lines.extend([f"### {pitch_type} vs {batter_side}HH", ""])
        lines.extend(
            leaderboard_table(
                group.sort_values("pitch_type_batter_side_rank"),
                rows=25,
            )
        )
        lines.append("")

    REPORT_PATH.write_text("\n".join(lines), encoding="utf-8")


def main() -> None:
    pitch_value_df = pd.read_csv(PITCH_VALUE_PATH)
    location_score_df = pd.read_csv(LOCATION_SCORE_PATH)

    pitch_value = prepare_pitch_value(pitch_value_df)
    location_score = prepare_location_score(location_score_df)
    leaderboard = create_split_leaderboard(pitch_value, location_score)

    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    REPORT_PATH.parent.mkdir(parents=True, exist_ok=True)
    leaderboard.to_csv(OUTPUT_PATH, index=False)
    write_report(
        leaderboard,
        pitch_value_rows=len(pitch_value_df),
        location_rows=len(location_score_df),
    )

    print(f"Wrote split leaderboard: {OUTPUT_PATH}")
    print(f"Wrote report: {REPORT_PATH}")
    print(f"Joined leaderboard rows: {len(leaderboard):,}")
    print("\nTop 20 split pitches:")
    print(
        leaderboard[
            [
                "overall_rank",
                "pitcher_name",
                "pitcher_team",
                "pitch_type",
                "batter_side",
                "split_pitch_count",
                "pitch_value_20_80",
                "location_score_20_80",
                "final_pitch_score",
                "final_pitch_score_0_100",
            ]
        ]
        .head(20)
        .to_string(index=False)
    )


if __name__ == "__main__":
    main()
