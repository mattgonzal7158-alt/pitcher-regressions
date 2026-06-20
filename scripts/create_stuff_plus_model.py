from __future__ import annotations

from pathlib import Path

import numpy as np
import pandas as pd


INPUT_PATH = Path("data/processed/master_pitch_evaluation_table.csv")
OUTPUT_PATH = Path("data/processed/stuff_plus_scores.csv")
REPORT_PATH = Path("reports/stuff_plus_report.md")

DEPENDENT = "final_pitch_score_20_80"
PREDICTORS = [
    "IVB",
    "HB",
    "velocity",
    "spin_rate",
    "extension",
    "release_height",
    "release_side",
]
MIN_PITCH_TYPE_ROWS = 30

ID_COLUMNS = [
    "pitcher_name",
    "pitcher_id",
    "pitcher_team",
    "pitch_type",
    "batter_side",
    "pitch_count",
    "batted_ball_count",
    "final_pitch_score_20_80",
    "final_pitch_score_0_100",
    "overall_rank",
    "pitch_type_rank",
    "pitch_type_batter_side_rank",
    "archetype",
    "cluster",
]


def percentile_rank(values: pd.Series) -> pd.Series:
    return values.rank(method="average", pct=True).mul(100)


def standardize(frame: pd.DataFrame, predictors: list[str]) -> tuple[pd.DataFrame, pd.Series, pd.Series]:
    means = frame[predictors].mean()
    stds = frame[predictors].std(ddof=0).replace(0, np.nan)
    z = (frame[predictors] - means) / stds
    return z.fillna(0.0), means, stds


def fit_ols(x: pd.DataFrame, y: pd.Series) -> tuple[np.ndarray, np.ndarray, float]:
    x_matrix = np.column_stack([np.ones(len(x)), x.to_numpy(dtype=float)])
    y_values = y.to_numpy(dtype=float)
    coefficients, _, _, _ = np.linalg.lstsq(x_matrix, y_values, rcond=None)
    predictions = x_matrix @ coefficients
    total_ss = np.sum((y_values - y_values.mean()) ** 2)
    residual_ss = np.sum((y_values - predictions) ** 2)
    r_squared = np.nan if np.isclose(total_ss, 0) else 1 - residual_ss / total_ss
    return coefficients, predictions, r_squared


def prepare_model_data(df: pd.DataFrame) -> tuple[pd.DataFrame, list[str]]:
    warnings: list[str] = []
    required = [DEPENDENT, "pitch_type", *PREDICTORS]
    missing = [column for column in required if column not in df.columns]
    if missing:
        raise ValueError(f"Missing required columns: {missing}")

    model_df = df.copy()
    for column in [DEPENDENT, *PREDICTORS]:
        model_df[column] = pd.to_numeric(model_df[column], errors="coerce")
    before = len(model_df)
    model_df = model_df.dropna(subset=[DEPENDENT, "pitch_type", *PREDICTORS]).copy()
    dropped = before - len(model_df)
    if dropped:
        warnings.append(f"Dropped {dropped:,} rows with missing target or predictor values.")
    return model_df, warnings


def fit_pooled_model(model_df: pd.DataFrame) -> tuple[pd.DataFrame, dict[str, object]]:
    z, means, stds = standardize(model_df, PREDICTORS)
    dummies = pd.get_dummies(model_df["pitch_type"], prefix="pitch_type", drop_first=True)
    dummies = dummies.astype(float)
    x = pd.concat([z, dummies], axis=1)
    coefficients, predictions, r_squared = fit_ols(x, model_df[DEPENDENT])
    model_info = {
        "model_name": "Fallback pooled fixed effects",
        "pitch_type": "Pooled",
        "model_type": "pooled_fixed_effects",
        "row_count": len(model_df),
        "r_squared": r_squared,
        "intercept": coefficients[0],
        "features": list(x.columns),
        "coefficients": coefficients[1:],
        "means": means,
        "stds": stds,
        "dummy_columns": list(dummies.columns),
    }
    prediction_df = pd.DataFrame(
        {
            "source_index": model_df.index,
            "stuff_plus_raw_pooled": predictions,
        }
    )
    return prediction_df, model_info


def fit_pitch_type_models(
    model_df: pd.DataFrame,
) -> tuple[pd.DataFrame, list[dict[str, object]], pd.DataFrame]:
    pooled_predictions, pooled_info = fit_pooled_model(model_df)
    predictions = pooled_predictions.copy()
    predictions["stuff_plus_raw"] = predictions["stuff_plus_raw_pooled"]
    predictions["stuff_plus_model_type"] = "pooled_fixed_effects"
    predictions["stuff_plus_model_pitch_type"] = "Pooled"

    model_infos: list[dict[str, object]] = [pooled_info]
    per_type_predictions = []
    pitch_counts = model_df["pitch_type"].value_counts()
    eligible_pitch_types = pitch_counts.loc[pitch_counts.ge(MIN_PITCH_TYPE_ROWS)].index

    for pitch_type in sorted(eligible_pitch_types):
        subset = model_df.loc[model_df["pitch_type"].eq(pitch_type)].copy()
        z, means, stds = standardize(subset, PREDICTORS)
        coefficients, fitted, r_squared = fit_ols(z, subset[DEPENDENT])
        model_infos.append(
            {
                "model_name": f"{pitch_type} model",
                "pitch_type": pitch_type,
                "model_type": "pitch_type_specific",
                "row_count": len(subset),
                "r_squared": r_squared,
                "intercept": coefficients[0],
                "features": PREDICTORS,
                "coefficients": coefficients[1:],
                "means": means,
                "stds": stds,
                "dummy_columns": [],
            }
        )
        per_type_predictions.append(
            pd.DataFrame(
                {
                    "source_index": subset.index,
                    "stuff_plus_raw_type": fitted,
                    "stuff_plus_model_type": "pitch_type_specific",
                    "stuff_plus_model_pitch_type": pitch_type,
                }
            )
        )

    if per_type_predictions:
        type_predictions = pd.concat(per_type_predictions, ignore_index=True)
        predictions = predictions.merge(type_predictions, on="source_index", how="left")
        predictions["stuff_plus_raw"] = predictions["stuff_plus_raw_type"].fillna(
            predictions["stuff_plus_raw"]
        )
        predictions["stuff_plus_model_type"] = predictions[
            "stuff_plus_model_type_y"
        ].fillna(predictions["stuff_plus_model_type_x"])
        predictions["stuff_plus_model_pitch_type"] = predictions[
            "stuff_plus_model_pitch_type_y"
        ].fillna(predictions["stuff_plus_model_pitch_type_x"])
        predictions = predictions[
            [
                "source_index",
                "stuff_plus_raw",
                "stuff_plus_model_type",
                "stuff_plus_model_pitch_type",
            ]
        ]

    summary_rows = []
    for info in model_infos:
        summary_rows.append(
            {
                "model_name": info["model_name"],
                "pitch_type": info["pitch_type"],
                "model_type": info["model_type"],
                "row_count": info["row_count"],
                "r_squared": info["r_squared"],
                "intercept": info["intercept"],
            }
        )
    return predictions, model_infos, pd.DataFrame(summary_rows)


def variable_importance(model_infos: list[dict[str, object]]) -> pd.DataFrame:
    rows = []
    for info in model_infos:
        for feature, coefficient in zip(info["features"], info["coefficients"]):
            if feature not in PREDICTORS:
                continue
            rows.append(
                {
                    "pitch_type": info["pitch_type"],
                    "model_type": info["model_type"],
                    "variable": feature,
                    "standardized_coefficient": coefficient,
                    "absolute_importance": abs(coefficient),
                }
            )
    return pd.DataFrame(rows).sort_values(
        ["pitch_type", "absolute_importance"], ascending=[True, False]
    )


def create_scores(master: pd.DataFrame) -> tuple[pd.DataFrame, pd.DataFrame, pd.DataFrame, list[str]]:
    model_df, warnings = prepare_model_data(master)
    predictions, model_infos, summary = fit_pitch_type_models(model_df)
    importance = variable_importance(model_infos)

    scored = model_df.merge(predictions, left_index=True, right_on="source_index", how="left")
    scored["stuff_plus_20_80"] = (
        50
        + 10
        * (
            (scored["stuff_plus_raw"] - scored["stuff_plus_raw"].mean())
            / scored["stuff_plus_raw"].std(ddof=0)
        )
    ).clip(20, 80)
    scored["stuff_plus_0_100"] = percentile_rank(scored["stuff_plus_raw"])
    scored["stuff_plus_rank"] = (
        scored["stuff_plus_raw"].rank(method="first", ascending=False).astype(int)
    )
    scored["stuff_plus_pitch_type_rank"] = (
        scored.groupby("pitch_type")["stuff_plus_raw"]
        .rank(method="first", ascending=False)
        .astype(int)
    )

    for column in ID_COLUMNS:
        if column not in scored.columns:
            scored[column] = pd.NA

    columns = [
        *ID_COLUMNS,
        *PREDICTORS,
        "stuff_plus_raw",
        "stuff_plus_20_80",
        "stuff_plus_0_100",
        "stuff_plus_rank",
        "stuff_plus_pitch_type_rank",
        "stuff_plus_model_type",
        "stuff_plus_model_pitch_type",
    ]
    scored = scored[columns].sort_values("stuff_plus_rank")
    return scored, summary, importance, warnings


def format_number(value: float, digits: int = 2) -> str:
    return "" if pd.isna(value) else f"{value:.{digits}f}"


def leaderboard_table(df: pd.DataFrame, rows: int = 25) -> list[str]:
    columns = [
        "Rank",
        "Pitcher",
        "Team",
        "Pitch Type",
        "Side",
        "Stuff+",
        "Stuff %",
        "Final",
        "Velo",
        "IVB",
        "HB",
        "Spin",
        "Model",
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
                    str(int(row.stuff_plus_rank)),
                    str(row.pitcher_name),
                    str(row.pitcher_team),
                    str(row.pitch_type),
                    side,
                    format_number(row.stuff_plus_20_80, 1),
                    format_number(row.stuff_plus_0_100, 1),
                    format_number(row.final_pitch_score_20_80, 1),
                    format_number(row.velocity, 1),
                    format_number(row.IVB, 1),
                    format_number(row.HB, 1),
                    format_number(row.spin_rate, 0),
                    str(row.stuff_plus_model_type),
                ]
            )
            + " |"
        )
    return lines


def write_report(
    scored: pd.DataFrame,
    summary: pd.DataFrame,
    importance: pd.DataFrame,
    warnings: list[str],
) -> None:
    lines = [
        "# Stuff+ Movement Model",
        "",
        f"- Input file: `{INPUT_PATH}`",
        f"- Output file: `{OUTPUT_PATH}`",
        f"- Scored rows: {len(scored):,}",
        f"- Dependent variable: `{DEPENDENT}`",
        f"- Predictors: {', '.join(f'`{p}`' for p in PREDICTORS)}",
        f"- Pitch-type-specific model minimum: {MIN_PITCH_TYPE_ROWS} rows",
        "- Low-sample pitch types use the fallback pooled model with pitch type fixed effects.",
        "",
        "## Warnings",
        "",
    ]
    lines.extend([f"- {warning}" for warning in warnings] if warnings else ["- None."])

    lines.extend(
        [
            "",
            "## Model Summaries",
            "",
            "| Model | Type | Rows | R-squared | Intercept |",
            "|---|---|---:|---:|---:|",
        ]
    )
    for row in summary.sort_values(["model_type", "pitch_type"]).itertuples(index=False):
        lines.append(
            f"| {row.pitch_type} | {row.model_type} | {int(row.row_count):,} | "
            f"{format_number(row.r_squared, 4)} | {format_number(row.intercept, 2)} |"
        )

    lines.extend(["", "## Variable Importance by Pitch Type", ""])
    for pitch_type, group in importance.groupby("pitch_type"):
        lines.extend([f"### {pitch_type}", ""])
        lines.extend(
            [
                "| Variable | Standardized Coefficient | Absolute Importance |",
                "|---|---:|---:|",
            ]
        )
        for row in group.itertuples(index=False):
            lines.append(
                f"| `{row.variable}` | {row.standardized_coefficient:.3f} | "
                f"{row.absolute_importance:.3f} |"
            )
        lines.append("")

    lines.extend(
        [
            "## Top 25 Stuff+ Pitches",
            "",
            *leaderboard_table(scored, rows=25),
            "",
            "## Top 10 Stuff+ by Pitch Type",
            "",
        ]
    )
    for pitch_type, group in scored.groupby("pitch_type"):
        lines.extend([f"### {pitch_type}", ""])
        lines.extend(leaderboard_table(group.sort_values("stuff_plus_pitch_type_rank"), rows=10))
        lines.append("")

    REPORT_PATH.write_text("\n".join(lines), encoding="utf-8")


def main() -> None:
    master = pd.read_csv(INPUT_PATH)
    scored, summary, importance, warnings = create_scores(master)

    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    REPORT_PATH.parent.mkdir(parents=True, exist_ok=True)
    scored.to_csv(OUTPUT_PATH, index=False)
    write_report(scored, summary, importance, warnings)

    print(f"Wrote Stuff+ scores: {OUTPUT_PATH}")
    print(f"Wrote report: {REPORT_PATH}")
    print(f"Scored rows: {len(scored):,}")
    print("\nModel summaries:")
    print(summary.to_string(index=False))
    print("\nTop 20 Stuff+ pitches:")
    print(
        scored[
            [
                "stuff_plus_rank",
                "pitcher_name",
                "pitcher_team",
                "pitch_type",
                "batter_side",
                "stuff_plus_20_80",
                "stuff_plus_0_100",
                "final_pitch_score_20_80",
            ]
        ]
        .head(20)
        .to_string(index=False)
    )


if __name__ == "__main__":
    main()
