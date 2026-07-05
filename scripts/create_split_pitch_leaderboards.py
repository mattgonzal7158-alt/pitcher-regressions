from __future__ import annotations

from pathlib import Path

import numpy as np
import pandas as pd


PITCH_DATA_PATH = Path("data/processed/2026-data-with-woba-xwoba.parquet")
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
COMPONENT_SCORE_COLUMNS = [
    "k_pct",
    "groundball_pct",
    "line_drive_pct",
    "flyball_pct",
    "groundball_score_20_80",
    "groundball_score_0_100",
    "groundball_score_rank",
    "groundball_score_pitch_type_rank",
    "strikeout_score_20_80",
    "strikeout_score_0_100",
    "strikeout_score_rank",
    "strikeout_score_pitch_type_rank",
    "line_drive_score_20_80",
    "line_drive_score_0_100",
    "line_drive_score_rank",
    "line_drive_score_pitch_type_rank",
    "flyball_score_20_80",
    "flyball_score_0_100",
    "flyball_score_rank",
    "flyball_score_pitch_type_rank",
]
COMPONENT_SCORE_CONFIG = {
    "groundball": ("groundball_pct", True),
    "strikeout": ("k_pct", True),
    "line_drive": ("line_drive_pct", False),
    "flyball": ("flyball_pct", False),
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


def safe_rate(numerator: pd.Series, denominator: pd.Series) -> pd.Series:
    return numerator.div(denominator.replace(0, np.nan))


def clean_bool(series: pd.Series) -> pd.Series:
    return series.fillna(False).astype(bool)


def add_component_score(
    df: pd.DataFrame,
    *,
    prefix: str,
    metric: str,
    higher_is_better: bool,
) -> pd.DataFrame:
    metric_values = pd.to_numeric(df[metric], errors="coerce")
    mean = metric_values.mean()
    std = metric_values.std(ddof=0)
    if std and not np.isclose(std, 0):
        metric_z = (metric_values - mean) / std
    else:
        metric_z = pd.Series(0.0, index=df.index)

    score_raw = metric_z if higher_is_better else -metric_z
    df[f"{prefix}_score_raw"] = score_raw
    df[f"{prefix}_score_20_80"] = (50 + 10 * score_raw).clip(20, 80)
    df[f"{prefix}_score_0_100"] = percentile_rank(score_raw)
    df[f"{prefix}_score_rank"] = (
        score_raw.rank(method="first", ascending=False).astype("Int64")
    )
    df[f"{prefix}_score_pitch_type_rank"] = (
        df.groupby(["pitch_type", "batter_side"])[f"{prefix}_score_raw"]
        .rank(method="first", ascending=False)
        .astype("Int64")
    )
    return df


def prepare_split_components(df: pd.DataFrame) -> pd.DataFrame:
    required = {
        "pitcher_name",
        "pitcher_id",
        "pitcher_team",
        "pitch_type",
        "batter_side_canonical",
        "pitch_call",
        "kor_bb",
        "play_result",
        "hit_launch_angle_y",
        "xwoba_frontier",
    }
    missing = sorted(required.difference(df.columns))
    if missing:
        raise ValueError(f"Missing required split component columns: {missing}")

    pitch_call = df["pitch_call"].astype("string")
    kor_bb = df["kor_bb"].astype("string")
    play_result = df["play_result"].astype("string")
    launch_angle = pd.to_numeric(df["hit_launch_angle_y"], errors="coerce")

    strikeout = clean_bool(kor_bb.eq("Strikeout"))
    terminal_pa = (
        strikeout
        | clean_bool(kor_bb.eq("Walk"))
        | play_result.notna()
        | clean_bool(pitch_call.eq("Hit By Pitch"))
    )
    batted_ball = df["xwoba_frontier"].notna()
    ground_ball = launch_angle.lt(10)
    line_drive = launch_angle.between(10, 25, inclusive="both")
    fly_ball = launch_angle.gt(25)

    work = df[
        [
            "pitcher_name",
            "pitcher_id",
            "pitcher_team",
            "pitch_type",
            "batter_side_canonical",
        ]
    ].copy()
    work = work.rename(columns={"batter_side_canonical": "batter_side"})
    work["pitch_type"] = normalize_pitch_type(work["pitch_type"])
    work["batter_side"] = normalize_batter_side(work["batter_side"])
    work["pitcher_id_key"] = normalize_pitcher_id(work["pitcher_id"])
    work["strikeout_count"] = strikeout.astype(int)
    work["terminal_pa_count"] = terminal_pa.astype(int)
    work["batted_ball_count"] = batted_ball.astype(int)
    work["groundball_count"] = (ground_ball & batted_ball).astype(int)
    work["line_drive_count"] = (line_drive & batted_ball).astype(int)
    work["flyball_count"] = (fly_ball & batted_ball).astype(int)

    grouped = (
        work.groupby(
            [
                "pitcher_name",
                "pitcher_id_key",
                "pitcher_team",
                "pitch_type",
                "batter_side",
            ],
            dropna=False,
        )
        .agg(
            split_strikeout_count=("strikeout_count", "sum"),
            split_terminal_pa_count=("terminal_pa_count", "sum"),
            split_batted_ball_count=("batted_ball_count", "sum"),
            split_groundball_count=("groundball_count", "sum"),
            split_line_drive_count=("line_drive_count", "sum"),
            split_flyball_count=("flyball_count", "sum"),
        )
        .reset_index()
    )
    grouped["k_pct"] = safe_rate(
        grouped["split_strikeout_count"], grouped["split_terminal_pa_count"]
    )
    grouped["groundball_pct"] = safe_rate(
        grouped["split_groundball_count"], grouped["split_batted_ball_count"]
    )
    grouped["line_drive_pct"] = safe_rate(
        grouped["split_line_drive_count"], grouped["split_batted_ball_count"]
    )
    grouped["flyball_pct"] = safe_rate(
        grouped["split_flyball_count"], grouped["split_batted_ball_count"]
    )
    return grouped


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
    pitch_value: pd.DataFrame,
    location_score: pd.DataFrame,
    split_components: pd.DataFrame,
) -> pd.DataFrame:
    merge_keys = ["pitcher_name", "pitcher_id_key", "pitcher_team", "pitch_type"]
    joined = location_score.merge(
        pitch_value.drop(columns=["pitcher_id"]),
        on=merge_keys,
        how="inner",
        suffixes=("", "_pitch_value"),
    )
    joined = joined.rename(columns={"pitcher_id": "pitcher_id"})
    joined = joined.merge(
        split_components,
        on=[*merge_keys, "batter_side"],
        how="left",
        validate="one_to_one",
    )
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
    for prefix, (metric, higher_is_better) in COMPONENT_SCORE_CONFIG.items():
        joined = add_component_score(
            joined,
            prefix=prefix,
            metric=metric,
            higher_is_better=higher_is_better,
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
        "split_batted_ball_count",
        "split_terminal_pa_count",
        "split_strikeout_count",
        "split_groundball_count",
        "split_line_drive_count",
        "split_flyball_count",
        *[column for column in COMPONENT_SCORE_COLUMNS if column in joined.columns],
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
        f"- Split component input: `{PITCH_DATA_PATH}`",
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
        "Ground-ball, strikeout, line-drive, and fly-ball component scores are calculated separately for each pitcher + pitch type + batter side row, then ranked within the split leaderboard. Higher strikeout and ground-ball rates score better; lower line-drive and fly-ball rates score better.",
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
    pitch_df = pd.read_parquet(PITCH_DATA_PATH)

    pitch_value = prepare_pitch_value(pitch_value_df)
    location_score = prepare_location_score(location_score_df)
    split_components = prepare_split_components(pitch_df)
    leaderboard = create_split_leaderboard(
        pitch_value, location_score, split_components
    )

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
