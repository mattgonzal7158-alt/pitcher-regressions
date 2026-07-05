from __future__ import annotations

from pathlib import Path

import numpy as np
import pandas as pd


INPUT_PATH = Path("data/processed/pitcher_pitch_type_xwoba_metrics.csv")
OUTPUT_PATH = Path("data/processed/pitch_value_scores.csv")
TYPE_RANK_OUTPUT_PATH = Path("data/processed/pitch_value_scores_with_type_rank.csv")
REPORT_PATH = Path("reports/pitch_value_score_leaderboards.md")

MIN_PITCHES = 50
MIN_BATTED_BALLS = 10

PREDICTORS = [
    "whiff_pct",
    "csw_pct",
    "putaway_pct",
    "k_pct",
    "avg_exit_velocity",
    "hardhit_pct",
    "barrel_pct",
    "sweetspot_pct",
]

COMPONENT_SCORES = {
    "groundball": {
        "metric": "groundball_pct",
        "label": "Ground Ball",
        "higher_is_better": True,
    },
    "strikeout": {
        "metric": "k_pct",
        "label": "Strikeout",
        "higher_is_better": True,
    },
    "line_drive": {
        "metric": "line_drive_pct",
        "label": "Line Drive Suppression",
        "higher_is_better": False,
    },
    "flyball": {
        "metric": "flyball_pct",
        "label": "Fly Ball Suppression",
        "higher_is_better": False,
    },
}

# Frozen score weights from the original xwOBA calibration.
# Positive weights raise expected damage, so Pitch Value Score uses the
# negative weighted sum: higher score means lower expected damage.
STANDARDIZED_COEFFICIENTS = {
    "whiff_pct": 0.003254,
    "csw_pct": 0.029336,
    "putaway_pct": -0.014520,
    "k_pct": -0.043673,
    "avg_exit_velocity": 0.589000,
    "hardhit_pct": 0.239017,
    "barrel_pct": -0.049151,
    "sweetspot_pct": 0.303807,
}

LEADERBOARD_GROUPS = {
    "Four-Seams": ["Four-Seam"],
    "Sinkers": ["Sinker"],
    "Sliders": ["Slider"],
    "Curveballs": ["Curveball"],
    "Changeups": ["Changeup"],
}


def percentile_rank(values: pd.Series) -> pd.Series:
    return values.rank(method="average", pct=True).mul(100)


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
        score_raw.rank(method="first", ascending=False).astype(int)
    )
    df[f"{prefix}_score_pitch_type_rank"] = (
        df.groupby("pitch_type")[f"{prefix}_score_raw"]
        .rank(method="first", ascending=False)
        .astype(int)
    )
    return df


def add_pitch_value_scores(df: pd.DataFrame) -> pd.DataFrame:
    model_df = df.loc[
        df["pitch_count"].ge(MIN_PITCHES)
        & df["batted_ball_count"].ge(MIN_BATTED_BALLS)
    ].copy()
    model_df = model_df.dropna(subset=["xwoba_frontier", *PREDICTORS])

    means = model_df[PREDICTORS].mean()
    stds = model_df[PREDICTORS].std(ddof=0).replace(0, np.nan)

    weighted_damage = pd.Series(0.0, index=model_df.index)
    for variable in PREDICTORS:
        z_value = (model_df[variable] - means[variable]) / stds[variable]
        model_df[f"{variable}_z"] = z_value
        model_df[f"{variable}_score_component"] = -STANDARDIZED_COEFFICIENTS[variable] * z_value
        weighted_damage += STANDARDIZED_COEFFICIENTS[variable] * z_value

    model_df["pitch_value_raw"] = -weighted_damage
    raw_mean = model_df["pitch_value_raw"].mean()
    raw_std = model_df["pitch_value_raw"].std(ddof=0)
    model_df["pitch_value_20_80"] = (
        50 + 10 * ((model_df["pitch_value_raw"] - raw_mean) / raw_std)
    ).clip(20, 80)
    model_df["pitch_value_0_100"] = percentile_rank(model_df["pitch_value_raw"])
    model_df["overall_rank"] = model_df["pitch_value_raw"].rank(
        method="first", ascending=False
    ).astype(int)
    model_df["pitch_type_rank"] = (
        model_df.groupby("pitch_type")["pitch_value_raw"]
        .rank(method="first", ascending=False)
        .astype(int)
    )
    for prefix, config in COMPONENT_SCORES.items():
        model_df = add_component_score(
            model_df,
            prefix=prefix,
            metric=config["metric"],
            higher_is_better=config["higher_is_better"],
        )

    return model_df.sort_values("overall_rank")


def format_rate(value: float) -> str:
    return "" if pd.isna(value) else f"{value * 100:.1f}%"


def leaderboard_table(df: pd.DataFrame, rows: int = 25) -> list[str]:
    columns = [
        "Rank",
        "Pitcher",
        "Team",
        "Pitch Type",
        "Pitches",
        "BBE",
        "xwOBA",
        "PVS 20-80",
        "PVS 0-100",
        "EV",
        "Whiff%",
        "K%",
        "HardHit%",
        "SweetSpot%",
        "GB Score",
        "K Score",
        "LD Supp",
        "FB Supp",
        "Pitch Type Rank",
    ]
    lines = ["| " + " | ".join(columns) + " |", "|" + "|".join(["---"] * len(columns)) + "|"]
    for row in df.head(rows).itertuples(index=False):
        lines.append(
            "| "
            + " | ".join(
                [
                    str(row.overall_rank),
                    str(row.pitcher_name),
                    str(row.pitcher_team),
                    str(row.pitch_type),
                    f"{int(row.pitch_count):,}",
                    f"{int(row.batted_ball_count):,}",
                    f"{row.xwoba_frontier:.3f}",
                    f"{row.pitch_value_20_80:.1f}",
                    f"{row.pitch_value_0_100:.1f}",
                    f"{row.avg_exit_velocity:.1f}",
                    format_rate(row.whiff_pct),
                    format_rate(row.k_pct),
                    format_rate(row.hardhit_pct),
                    format_rate(row.sweetspot_pct),
                    f"{row.groundball_score_20_80:.1f}",
                    f"{row.strikeout_score_20_80:.1f}",
                    f"{row.line_drive_score_20_80:.1f}",
                    f"{row.flyball_score_20_80:.1f}",
                    str(row.pitch_type_rank),
                ]
            )
            + " |"
        )
    return lines


def write_report(scored: pd.DataFrame, output_path: Path) -> None:
    lines = [
        "# Frontier League Pitch Value Score",
        "",
        f"- Input file: `{INPUT_PATH}`",
        f"- Output file: `{output_path}`",
        f"- Qualified pitcher-pitch types scored: {len(scored):,}",
        f"- Qualification: at least {MIN_PITCHES} pitches and {MIN_BATTED_BALLS} tracked batted balls",
        "- Score direction: higher is better, meaning lower expected xwOBA damage based on the frozen standardized score weights.",
        "- Pitch type normalization: `Fastball` is grouped with `Four-Seam`; `Two-Seam` is grouped with `Sinker`.",
        "",
        "## What The Score Means",
        "",
        "Pitch Value Score is a pitch-level quality grade. Higher is better. A high score means that a pitcher-pitch type has a strong mix of miss, strike, and contact-management traits associated with lower expected damage.",
        "",
        "This is not a full pitcher grade. It grades one pitch type for one pitcher. A pitcher can have an elite individual pitch and still have a weaker overall arsenal, command profile, workload, or role fit.",
        "",
        "The score is built so the interpretation is familiar:",
        "",
        "- `50` on the 20-80 scale is league average among qualified pitcher-pitch types.",
        "- `60` is roughly one standard deviation better than average.",
        "- `70` is roughly two standard deviations better than average.",
        "- `80` is the top-end cap used for the report.",
        "- `pitch_value_0_100` is the pitch's percentile rank among qualified pitcher-pitch types.",
        "",
        "## Inputs",
        "",
        "The score starts from pitcher + pitch type aggregates. Each row represents one pitch type thrown by one pitcher, not a single pitch. To reduce noise, only rows with enough volume are scored.",
        "",
        "Pitch type labels are normalized before scoring: `Fastball` and `Four-Seam` are one pitch type labeled `Four-Seam`, while `Two-Seam` and `Sinker` are one pitch type labeled `Sinker`.",
        "",
        "| Input Metric | Baseball Meaning | Score Direction |",
        "|---|---|---|",
        "| Whiff% | Ability to miss bats when hitters swing. | Higher is generally better, but this frozen score weight is small after contact metrics are included. |",
        "| CSW% | Called strikes plus whiffs per pitch. | Measures count-control and bat-missing. |",
        "| PutAway% | Strikeouts per two-strike pitch. | Higher means the pitch can finish plate appearances. |",
        "| K% | Strikeouts per terminal PA-ending pitch for that pitch type. | Higher means stronger bat-missing/finishing results. |",
        "| Average Exit Velocity | How hard tracked batted balls are hit. | Lower is better. |",
        "| HardHit% | Share of batted balls at least 95 mph. | Lower is better. |",
        "| Barrel% | Share of batted balls in an approximate barrel launch/EV zone. | Lower is usually better, but the multivariate coefficient is conditional on EV/HardHit/SweetSpot. |",
        "| SweetSpot% | Share of batted balls launched from 8 to 32 degrees. | Lower is better for pitchers because this is a productive launch window. |",
        "| GroundBall% | Share of tracked batted balls launched below 10 degrees. | Higher is better in the Ground Ball component score. |",
        "| LineDrive% | Share of tracked batted balls launched from 10 to 25 degrees. | Lower is better in the Line Drive Suppression component score. |",
        "| FlyBall% | Share of tracked batted balls launched above 25 degrees. | Lower is better in the Fly Ball Suppression component score. |",
        "",
        "## Score Method",
        "",
        "The score uses frozen standardized weights on the miss and contact metrics. Those weights encode how strongly each metric is associated with expected damage in the scoring system.",
        "",
        "Each metric is standardized across qualified pitcher-pitch type rows. The standardized score weight is applied to estimate xwOBA pressure, then the sign is reversed so lower-xwOBA traits score higher.",
        "",
        "`pitch_value_raw = -sum(standardized_weight * metric_z)`",
        "",
        "- `pitch_value_20_80`: scouting-style scale, mean 50 and 10 points per standard deviation, clipped from 20 to 80.",
        "- `pitch_value_0_100`: percentile rank of `pitch_value_raw` among qualified pitcher-pitch types.",
        "- `overall_rank`: rank across all qualified pitcher-pitch types.",
        "- `pitch_type_rank`: rank within that exact pitch type label.",
        "",
        "Because the sign is reversed, a metric with a positive damage weight hurts the Pitch Value Score when it is high. A metric with a negative damage weight helps the score when it is high.",
        "",
        "## Component Scores",
        "",
        "The output also includes standalone component scores for ground-ball tendency, strikeout ability, line-drive suppression, and fly-ball suppression. Each component has a raw score, a 20-80 score, a percentile, an overall rank, and a pitch-type rank.",
        "",
        "| Component | Metric | Direction |",
        "|---|---|---|",
        *[
            (
                f"| `{prefix}_score` | `{config['metric']}` | "
                f"{'higher metric scores better' if config['higher_is_better'] else 'lower metric scores better'} |"
            )
            for prefix, config in COMPONENT_SCORES.items()
        ],
        "",
        "A component score of `50` is league average among qualified pitcher-pitch types; `60` is one standard deviation better. Component ranks sort highest score first.",
        "",
        "## Methodology Notes",
        "",
        "- The scoring model is descriptive. It identifies which observed pitch-level outcomes were associated with lower expected damage in this dataset.",
        "- Contact quality carries much of the weight because average exit velocity, SweetSpot%, and HardHit% are the strongest damage signals in the current score.",
        "- Miss metrics still matter for baseball evaluation, but in this multivariate score they receive less weight when contact quality already captures most of the damage signal.",
        "- Small samples can still move the leaderboards. The qualification filter helps, but the score should be read with pitch count and batted-ball count nearby.",
        "- The score does not directly include command, sequencing, handedness splits, game context, injury risk, or scouting grades.",
        "",
        "## Top 25 Pitches in the League",
        "",
        *leaderboard_table(scored, rows=25),
        "",
        "## Leaderboards by Pitch Family",
        "",
    ]

    for title, pitch_types in LEADERBOARD_GROUPS.items():
        subset = scored.loc[scored["pitch_type"].isin(pitch_types)].copy()
        lines.extend([f"### {title}", ""])
        if subset.empty:
            lines.append("No qualified pitches.")
        else:
            lines.extend(leaderboard_table(subset, rows=25))
        lines.append("")

    lines.extend(
        [
            "## Standardized Coefficients Used",
            "",
            "| Metric | Standardized Coefficient | Score Direction |",
            "|---|---:|---|",
        ]
    )
    for metric, coefficient in STANDARDIZED_COEFFICIENTS.items():
        direction = "helps score when lower" if coefficient > 0 else "helps score when higher"
        lines.append(f"| `{metric}` | {coefficient:.6f} | {direction} |")

    REPORT_PATH.write_text("\n".join(lines), encoding="utf-8")


def main() -> None:
    df = pd.read_csv(INPUT_PATH)
    missing = sorted(
        {
            "pitcher_name",
            "pitcher_team",
            "pitch_type",
            "pitch_count",
            "batted_ball_count",
            "xwoba_frontier",
            *PREDICTORS,
            *(config["metric"] for config in COMPONENT_SCORES.values()),
        }.difference(df.columns)
    )
    if missing:
        raise ValueError(f"Missing required columns: {missing}")

    scored = add_pitch_value_scores(df)
    output_path = OUTPUT_PATH
    try:
        scored.to_csv(output_path, index=False)
        scored.to_csv(TYPE_RANK_OUTPUT_PATH, index=False)
    except PermissionError:
        output_path = TYPE_RANK_OUTPUT_PATH
        scored.to_csv(output_path, index=False)

    write_report(scored, output_path)

    print(f"Wrote scores: {output_path}")
    if output_path != TYPE_RANK_OUTPUT_PATH:
        print(f"Wrote type-rank scores: {TYPE_RANK_OUTPUT_PATH}")
    print(f"Wrote leaderboards: {REPORT_PATH}")
    print(f"Qualified pitcher-pitch types: {len(scored):,}")
    print("\nTop 25 pitches:")
    print(
        scored[
            [
                "overall_rank",
                "pitcher_name",
                "pitcher_team",
                "pitch_type",
                "pitch_count",
                "batted_ball_count",
                "xwoba_frontier",
                "pitch_value_20_80",
                "pitch_value_0_100",
            ]
        ]
        .head(25)
        .to_string(index=False)
    )


if __name__ == "__main__":
    main()
