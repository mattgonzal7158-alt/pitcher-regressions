from __future__ import annotations

from pathlib import Path

import numpy as np
import pandas as pd


MASTER_PATH = Path("data/processed/master_pitch_evaluation_table.csv")
STUFF_PATH = Path("data/processed/stuff_plus_scores.csv")
OUTPUT_PATH = Path("data/processed/execution_plus_scores.csv")
REPORT_PATH = Path("reports/execution_plus_report.md")

HIGH_SCORE_CUTOFF = 50.0

JOIN_KEYS = ["pitcher_name", "pitcher_id_key", "pitcher_team", "pitch_type", "batter_side"]


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


def percentile_rank(values: pd.Series) -> pd.Series:
    return values.rank(method="average", pct=True).mul(100)


def quadrant_label(row: pd.Series) -> str:
    high_stuff = row["stuff_plus_20_80"] >= HIGH_SCORE_CUTOFF
    high_execution = row["execution_plus_20_80"] >= HIGH_SCORE_CUTOFF
    if high_stuff and high_execution:
        return "Elite Weapon"
    if high_stuff and not high_execution:
        return "Development Target"
    if not high_stuff and high_execution:
        return "Command/Deception Weapon"
    return "Low Priority"


def create_execution_scores(master: pd.DataFrame, stuff: pd.DataFrame) -> pd.DataFrame:
    required_master = {"final_pitch_score_20_80", "pitcher_name", "pitcher_id", "pitcher_team", "pitch_type", "batter_side"}
    required_stuff = {
        "pitcher_name",
        "pitcher_id",
        "pitcher_team",
        "pitch_type",
        "batter_side",
        "stuff_plus_raw",
        "stuff_plus_20_80",
        "stuff_plus_0_100",
        "stuff_plus_model_type",
        "stuff_plus_model_pitch_type",
    }
    missing_master = sorted(required_master.difference(master.columns))
    missing_stuff = sorted(required_stuff.difference(stuff.columns))
    if missing_master:
        raise ValueError(f"Missing required master columns: {missing_master}")
    if missing_stuff:
        raise ValueError(f"Missing required Stuff+ columns: {missing_stuff}")

    master = add_join_keys(master)
    stuff = add_join_keys(stuff)
    stuff_columns = [
        *JOIN_KEYS,
        "stuff_plus_raw",
        "stuff_plus_20_80",
        "stuff_plus_0_100",
        "stuff_plus_rank",
        "stuff_plus_pitch_type_rank",
        "stuff_plus_model_type",
        "stuff_plus_model_pitch_type",
    ]
    stuff_columns = [column for column in stuff_columns if column in stuff.columns]

    joined = master.merge(stuff[stuff_columns], on=JOIN_KEYS, how="inner")
    joined["final_pitch_score_20_80"] = pd.to_numeric(
        joined["final_pitch_score_20_80"], errors="coerce"
    )
    joined["stuff_plus_raw"] = pd.to_numeric(joined["stuff_plus_raw"], errors="coerce")
    joined = joined.dropna(subset=["final_pitch_score_20_80", "stuff_plus_raw"]).copy()

    joined["execution_raw"] = joined["final_pitch_score_20_80"] - joined["stuff_plus_raw"]
    raw_std = joined["execution_raw"].std(ddof=0)
    if raw_std and not np.isclose(raw_std, 0):
        joined["execution_plus_20_80"] = (
            50 + 10 * ((joined["execution_raw"] - joined["execution_raw"].mean()) / raw_std)
        ).clip(20, 80)
    else:
        joined["execution_plus_20_80"] = 50.0
    joined["execution_plus_0_100"] = percentile_rank(joined["execution_raw"])
    joined["execution_plus_rank"] = (
        joined["execution_raw"].rank(method="first", ascending=False).astype(int)
    )
    joined["execution_plus_pitch_type_rank"] = (
        joined.groupby("pitch_type")["execution_raw"]
        .rank(method="first", ascending=False)
        .astype(int)
    )
    joined["execution_quadrant"] = joined.apply(quadrant_label, axis=1)

    columns = [
        "pitcher_name",
        "pitcher_id",
        "pitcher_team",
        "pitch_type",
        "batter_side",
        "pitch_count",
        "batted_ball_count",
        "raw_pitch_score_20_80",
        "location_score_20_80",
        "final_pitch_score_20_80",
        "final_pitch_score_0_100",
        "stuff_plus_raw",
        "stuff_plus_20_80",
        "stuff_plus_0_100",
        "execution_raw",
        "execution_plus_20_80",
        "execution_plus_0_100",
        "execution_plus_rank",
        "execution_plus_pitch_type_rank",
        "execution_quadrant",
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
        "archetype",
        "cluster",
        "stuff_plus_model_type",
        "stuff_plus_model_pitch_type",
    ]
    for column in columns:
        if column not in joined.columns:
            joined[column] = pd.NA
    return joined[columns].sort_values("execution_plus_rank")


def fmt(value: float, digits: int = 1) -> str:
    return "" if pd.isna(value) else f"{value:.{digits}f}"


def leaderboard_table(df: pd.DataFrame, rows: int = 25) -> list[str]:
    columns = [
        "Rank",
        "Pitcher",
        "Team",
        "Pitch Type",
        "Side",
        "Final",
        "Stuff+",
        "Exec+",
        "Exec Raw",
        "Quadrant",
        "Archetype",
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
                    str(int(row.execution_plus_rank)),
                    str(row.pitcher_name),
                    str(row.pitcher_team),
                    str(row.pitch_type),
                    side,
                    fmt(row.final_pitch_score_20_80),
                    fmt(row.stuff_plus_20_80),
                    fmt(row.execution_plus_20_80),
                    fmt(row.execution_raw, 2),
                    str(row.execution_quadrant),
                    "" if pd.isna(row.archetype) else str(row.archetype),
                ]
            )
            + " |"
        )
    return lines


def quadrant_table(scored: pd.DataFrame) -> list[str]:
    grouped = (
        scored.groupby("execution_quadrant")
        .agg(
            rows=("execution_quadrant", "size"),
            avg_final=("final_pitch_score_20_80", "mean"),
            avg_stuff=("stuff_plus_20_80", "mean"),
            avg_execution=("execution_plus_20_80", "mean"),
        )
        .reset_index()
        .sort_values("rows", ascending=False)
    )
    lines = [
        "| Quadrant | Rows | Avg Final | Avg Stuff+ | Avg Execution+ |",
        "|---|---:|---:|---:|---:|",
    ]
    for row in grouped.itertuples(index=False):
        lines.append(
            f"| {row.execution_quadrant} | {int(row.rows):,} | "
            f"{row.avg_final:.1f} | {row.avg_stuff:.1f} | {row.avg_execution:.1f} |"
        )
    return lines


def write_report(scored: pd.DataFrame) -> None:
    development_targets = scored.loc[
        scored["execution_quadrant"].eq("Development Target")
    ].sort_values(["stuff_plus_20_80", "execution_plus_20_80"], ascending=[False, True])
    elite_weapons = scored.loc[
        scored["execution_quadrant"].eq("Elite Weapon")
    ].sort_values(["final_pitch_score_20_80", "stuff_plus_20_80"], ascending=[False, False])

    lines = [
        "# Execution+ Report",
        "",
        f"- Master input file: `{MASTER_PATH}`",
        f"- Stuff+ input file: `{STUFF_PATH}`",
        f"- Output file: `{OUTPUT_PATH}`",
        f"- Scored rows: {len(scored):,}",
        "",
        "## Method",
        "",
        "`execution_raw = final_pitch_score_20_80 - stuff_plus_raw`",
        "",
        "Execution+ captures how much a pitch's actual final score exceeds, or falls short of, its movement/release-only expected score.",
        "",
        "Quadrant labels use `50` as the high/low cutoff on both 20-80 scales:",
        "",
        "- High Stuff+, low Execution+: Development Target.",
        "- Low Stuff+, high Execution+: Command/Deception Weapon.",
        "- High Stuff+, high Execution+: Elite Weapon.",
        "- Low Stuff+, low Execution+: Low Priority.",
        "",
        "## Quadrant Table",
        "",
        *quadrant_table(scored),
        "",
        "## Top 25 Execution+",
        "",
        *leaderboard_table(scored.sort_values("execution_plus_rank"), rows=25),
        "",
        "## Top 25 Development Targets",
        "",
        *leaderboard_table(development_targets, rows=25),
        "",
        "## Top 25 Elite Weapons",
        "",
        *leaderboard_table(elite_weapons, rows=25),
    ]
    REPORT_PATH.write_text("\n".join(lines), encoding="utf-8")


def main() -> None:
    master = pd.read_csv(MASTER_PATH)
    stuff = pd.read_csv(STUFF_PATH)
    scored = create_execution_scores(master, stuff)

    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    REPORT_PATH.parent.mkdir(parents=True, exist_ok=True)
    scored.to_csv(OUTPUT_PATH, index=False)
    write_report(scored)

    print(f"Wrote Execution+ scores: {OUTPUT_PATH}")
    print(f"Wrote report: {REPORT_PATH}")
    print(f"Scored rows: {len(scored):,}")
    print("\nQuadrants:")
    print(scored["execution_quadrant"].value_counts().to_string())


if __name__ == "__main__":
    main()
