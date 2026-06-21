from __future__ import annotations

from pathlib import Path

import numpy as np
import pandas as pd


INPUT_PATH = Path("data/processed/2026-data-with-woba-xwoba.parquet")
OUTPUT_PATH = Path("data/processed/pitcher_pitch_type_xwoba_metrics.csv")

DEPENDENT = "xwoba_frontier"
PITCH_TYPE_NORMALIZATION = {
    "Fastball": "Four-Seam",
    "Two-Seam": "Sinker",
}


def normalize_pitch_type(series: pd.Series) -> pd.Series:
    return series.astype("string").replace(PITCH_TYPE_NORMALIZATION)


def is_barrel(exit_velocity: pd.Series, launch_angle: pd.Series) -> pd.Series:
    ev = pd.to_numeric(exit_velocity, errors="coerce")
    la = pd.to_numeric(launch_angle, errors="coerce")
    expansion = (ev - 98).clip(lower=0)
    lower_bound = (26 - expansion).clip(lower=8)
    upper_bound = (30 + expansion).clip(upper=50)
    return ev.ge(98) & la.ge(lower_bound) & la.le(upper_bound)


def safe_rate(numerator: pd.Series, denominator: pd.Series) -> pd.Series:
    return numerator.div(denominator.replace(0, np.nan))


def clean_bool(series: pd.Series) -> pd.Series:
    return series.fillna(False).astype(bool)


def aggregate_pitch_metrics(df: pd.DataFrame) -> pd.DataFrame:
    pitch_call = df["pitch_call"].astype("string")
    kor_bb = df["kor_bb"].astype("string")
    play_result = df["play_result"].astype("string")
    exit_velocity = pd.to_numeric(df["hit_launch_exit_speed_y"], errors="coerce")
    launch_angle = pd.to_numeric(df["hit_launch_angle_y"], errors="coerce")

    swing = clean_bool(
        pitch_call.isin(
            [
                "Strike Swinging",
                "Foul Ball Not Fieldable",
                "Foul Ball Fieldable",
                "In Play",
            ]
        )
    )
    whiff = clean_bool(pitch_call.eq("Strike Swinging"))
    called_strike = clean_bool(pitch_call.isin(["Strike Called", "Automatic Strike"]))
    csw = whiff | called_strike
    two_strike = pd.to_numeric(df["game_state_strikes"], errors="coerce").eq(2)
    strikeout = clean_bool(kor_bb.eq("Strikeout"))
    terminal_pa = (
        strikeout
        | clean_bool(kor_bb.eq("Walk"))
        | play_result.notna()
        | clean_bool(pitch_call.eq("Hit By Pitch"))
    )
    batted_ball = df[DEPENDENT].notna()
    hard_hit = exit_velocity.ge(95)
    barrel = is_barrel(exit_velocity, launch_angle)
    sweet_spot = launch_angle.between(8, 32, inclusive="both")

    work = df[
        [
            "pitcher_name",
            "pitcher_id",
            "pitcher_team",
            "pitch_type",
            DEPENDENT,
        ]
    ].copy()
    work["pitch_type"] = normalize_pitch_type(work["pitch_type"])
    work["pitch_count"] = 1
    work["swing_count"] = swing.astype(int)
    work["whiff_count"] = whiff.astype(int)
    work["csw_count"] = csw.astype(int)
    work["two_strike_pitch_count"] = two_strike.astype(int)
    work["strikeout_count"] = strikeout.astype(int)
    work["terminal_pa_count"] = terminal_pa.astype(int)
    work["batted_ball_count"] = batted_ball.astype(int)
    work["hardhit_count"] = (hard_hit & batted_ball).astype(int)
    work["barrel_count"] = (barrel & batted_ball).astype(int)
    work["sweetspot_count"] = (sweet_spot & batted_ball).astype(int)
    work["exit_velocity_sum"] = exit_velocity.where(batted_ball).fillna(0)

    grouped = (
        work.groupby(["pitcher_name", "pitcher_id", "pitcher_team", "pitch_type"], dropna=False)
        .agg(
            pitch_count=("pitch_count", "sum"),
            swing_count=("swing_count", "sum"),
            whiff_count=("whiff_count", "sum"),
            csw_count=("csw_count", "sum"),
            two_strike_pitch_count=("two_strike_pitch_count", "sum"),
            strikeout_count=("strikeout_count", "sum"),
            terminal_pa_count=("terminal_pa_count", "sum"),
            batted_ball_count=("batted_ball_count", "sum"),
            hardhit_count=("hardhit_count", "sum"),
            barrel_count=("barrel_count", "sum"),
            sweetspot_count=("sweetspot_count", "sum"),
            exit_velocity_sum=("exit_velocity_sum", "sum"),
            xwoba_frontier=(DEPENDENT, "mean"),
        )
        .reset_index()
    )

    grouped["whiff_pct"] = safe_rate(grouped["whiff_count"], grouped["swing_count"])
    grouped["csw_pct"] = safe_rate(grouped["csw_count"], grouped["pitch_count"])
    grouped["putaway_pct"] = safe_rate(grouped["strikeout_count"], grouped["two_strike_pitch_count"])
    grouped["k_pct"] = safe_rate(grouped["strikeout_count"], grouped["terminal_pa_count"])
    grouped["avg_exit_velocity"] = safe_rate(grouped["exit_velocity_sum"], grouped["batted_ball_count"])
    grouped["hardhit_pct"] = safe_rate(grouped["hardhit_count"], grouped["batted_ball_count"])
    grouped["barrel_pct"] = safe_rate(grouped["barrel_count"], grouped["batted_ball_count"])
    grouped["sweetspot_pct"] = safe_rate(grouped["sweetspot_count"], grouped["batted_ball_count"])
    return grouped


def main() -> None:
    df = pd.read_parquet(INPUT_PATH)
    required = {
        "pitcher_name",
        "pitcher_id",
        "pitcher_team",
        "pitch_type",
        "pitch_call",
        "kor_bb",
        "play_result",
        "game_state_strikes",
        "hit_launch_exit_speed_y",
        "hit_launch_angle_y",
        DEPENDENT,
    }
    missing = sorted(required.difference(df.columns))
    if missing:
        raise ValueError(f"Missing required columns: {missing}")

    aggregate_df = aggregate_pitch_metrics(df)
    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    aggregate_df.to_csv(OUTPUT_PATH, index=False)

    qualified = aggregate_df.loc[
        aggregate_df["pitch_count"].ge(50)
        & aggregate_df["batted_ball_count"].ge(10)
        & aggregate_df[DEPENDENT].notna()
    ]
    print(f"Wrote pitch type metrics: {OUTPUT_PATH}")
    print(f"Pitcher-pitch type rows: {len(aggregate_df):,}")
    print(f"Qualified scoring rows before metric null filters: {len(qualified):,}")


if __name__ == "__main__":
    main()
