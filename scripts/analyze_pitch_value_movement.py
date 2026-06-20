from __future__ import annotations

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from scipy import stats
from sklearn.metrics import r2_score


PITCH_DATA_PATH = Path("data/processed/2026-data-with-woba-xwoba.parquet")
SCORE_PATH = Path("data/processed/pitch_value_scores.csv")
OUTPUT_PATH = Path("data/processed/pitch_value_movement_model_data.csv")
REPORT_PATH = Path("reports/pitch_value_movement_report.md")
COEFFICIENTS_PATH = Path("data/processed/pitch_value_movement_regression_coefficients.csv")
CORRELATIONS_PATH = Path("data/processed/pitch_value_movement_correlations.csv")
PLOTS_DIR = Path("plots/pitch_value_movement")

DEPENDENT = "pitch_value_20_80"
PREDICTORS = [
    "ivb",
    "hb",
    "spin_rate",
    "velocity",
    "extension",
    "release_height",
    "release_side",
]
INTERACTIONS = {
    "ivb_x_velocity": ("ivb", "velocity"),
    "hb_x_velocity": ("hb", "velocity"),
    "spin_x_velocity": ("spin_rate", "velocity"),
}

MOVEMENT_COLUMNS = {
    "ivb": "pitch_movement_induced_vert_break_x",
    "hb": "pitch_movement_horz_break_x",
    "spin_rate": "pitch_release_spin_rate_x",
    "velocity": "pitch_release_rel_speed_x",
    "extension": "pitch_release_extension_x",
    "release_height": "pitch_release_rel_height_x",
    "release_side": "pitch_release_rel_side_x",
}

LABELS = {
    "ivb": "IVB",
    "hb": "HB",
    "spin_rate": "Spin Rate",
    "velocity": "Velocity",
    "extension": "Extension",
    "release_height": "Release Height",
    "release_side": "Release Side",
    "ivb_x_velocity": "IVB x Velocity",
    "hb_x_velocity": "HB x Velocity",
    "spin_x_velocity": "Spin x Velocity",
}

CORRELATION_TARGETS = [
    "pitch_value_20_80",
    "xwoba_frontier",
    "whiff_pct",
    "csw_pct",
    "k_pct",
    "avg_exit_velocity",
    "hardhit_pct",
    "sweetspot_pct",
]

PITCH_TYPE_NORMALIZATION = {
    "Fastball": "Four-Seam",
    "Two-Seam": "Sinker",
}


def normalize_pitch_type(series: pd.Series) -> pd.Series:
    return series.astype("string").replace(PITCH_TYPE_NORMALIZATION)


def pitcher_id_key(series: pd.Series) -> pd.Series:
    numeric = pd.to_numeric(series, errors="coerce")
    key = numeric.round().astype("Int64").astype("string")
    return key.fillna("<MISSING>")


def fit_ols(x: pd.DataFrame, y: pd.Series) -> tuple[pd.DataFrame, np.ndarray, float]:
    x_matrix = np.column_stack([np.ones(len(x)), x.to_numpy(dtype=float)])
    y_values = y.to_numpy(dtype=float)
    coefficients, _, _, _ = np.linalg.lstsq(x_matrix, y_values, rcond=None)
    predictions = x_matrix @ coefficients
    residuals = y_values - predictions
    dof = len(y_values) - x_matrix.shape[1]
    mse = np.sum(residuals**2) / dof
    covariance = mse * np.linalg.pinv(x_matrix.T @ x_matrix)
    standard_errors = np.sqrt(np.diag(covariance))
    t_values = coefficients / standard_errors
    p_values = 2 * stats.t.sf(np.abs(t_values), dof)
    table = pd.DataFrame(
        {
            "variable": ["Intercept", *x.columns],
            "coefficient": coefficients,
            "std_error": standard_errors,
            "t_stat": t_values,
            "p_value": p_values,
        }
    )
    return table, predictions, r2_score(y_values, predictions)


def make_model_frame() -> pd.DataFrame:
    pitch_cols = [
        "pitcher_name",
        "pitcher_id",
        "pitcher_team",
        "pitch_type",
        *MOVEMENT_COLUMNS.values(),
    ]
    pitch_df = pd.read_parquet(PITCH_DATA_PATH, columns=pitch_cols)
    pitch_df["pitch_type"] = normalize_pitch_type(pitch_df["pitch_type"])
    pitch_df["pitcher_id_key"] = pitcher_id_key(pitch_df["pitcher_id"])
    for output_name, source_name in MOVEMENT_COLUMNS.items():
        pitch_df[output_name] = pd.to_numeric(pitch_df[source_name], errors="coerce")
    movement = (
        pitch_df.groupby(["pitcher_name", "pitcher_id_key", "pitcher_team", "pitch_type"], dropna=False)
        [PREDICTORS]
        .mean()
        .reset_index()
    )

    scores = pd.read_csv(SCORE_PATH)
    scores["pitcher_id_key"] = pitcher_id_key(scores["pitcher_id"])
    merge_keys = ["pitcher_name", "pitcher_id_key", "pitcher_team", "pitch_type"]
    merged = scores.merge(movement, on=merge_keys, how="left", validate="one_to_one")
    return merged.dropna(subset=[DEPENDENT, *PREDICTORS]).copy()


def standardize_features(model_df: pd.DataFrame) -> tuple[pd.DataFrame, pd.Series, pd.Series]:
    means = model_df[PREDICTORS].mean()
    stds = model_df[PREDICTORS].std(ddof=0).replace(0, np.nan)
    z = (model_df[PREDICTORS] - means) / stds
    for interaction, (left, right) in INTERACTIONS.items():
        z[interaction] = z[left] * z[right]
    return z, means, stds


def vif_statistics(x: pd.DataFrame) -> pd.DataFrame:
    rows = []
    for column in x.columns:
        others = [candidate for candidate in x.columns if candidate != column]
        x_matrix = np.column_stack([np.ones(len(x)), x[others].to_numpy(dtype=float)])
        y_values = x[column].to_numpy(dtype=float)
        coefficients, _, _, _ = np.linalg.lstsq(x_matrix, y_values, rcond=None)
        predictions = x_matrix @ coefficients
        r_squared = r2_score(y_values, predictions)
        vif = np.inf if np.isclose(1 - r_squared, 0) else 1 / (1 - r_squared)
        rows.append({"variable": column, "vif": vif})
    return pd.DataFrame(rows)


def movement_correlations(model_df: pd.DataFrame) -> pd.DataFrame:
    available_targets = [target for target in CORRELATION_TARGETS if target in model_df.columns]
    rows = []
    for movement in PREDICTORS:
        for target in available_targets:
            valid = model_df[[movement, target]].dropna()
            if len(valid) < 3:
                correlation = np.nan
                p_value = np.nan
            else:
                correlation, p_value = stats.pearsonr(valid[movement], valid[target])
            rows.append(
                {
                    "movement_trait": movement,
                    "target": target,
                    "correlation": correlation,
                    "p_value": p_value,
                }
            )
    return pd.DataFrame(rows)


def make_effect_plots(model_df: pd.DataFrame) -> None:
    PLOTS_DIR.mkdir(exist_ok=True)
    for variable in PREDICTORS:
        fig, ax = plt.subplots(figsize=(8, 6))
        ax.scatter(model_df[variable], model_df[DEPENDENT], s=20, alpha=0.55, color="#2f6690")
        fit = np.polyfit(model_df[variable], model_df[DEPENDENT], deg=1)
        x_line = np.linspace(model_df[variable].min(), model_df[variable].max(), 100)
        ax.plot(x_line, fit[0] * x_line + fit[1], color="#b44b35", linewidth=2)
        ax.set_title(f"{LABELS[variable]} vs Pitch Value Score")
        ax.set_xlabel(LABELS[variable])
        ax.set_ylabel("Pitch Value Score (20-80)")
        fig.tight_layout()
        fig.savefig(PLOTS_DIR / f"effect_{variable}.png", dpi=160)
        plt.close(fig)


def make_correlation_heatmap(correlations: pd.DataFrame) -> None:
    pivot = correlations.pivot(index="movement_trait", columns="target", values="correlation")
    ordered_rows = [row for row in PREDICTORS if row in pivot.index]
    ordered_cols = [col for col in CORRELATION_TARGETS if col in pivot.columns]
    pivot = pivot.loc[ordered_rows, ordered_cols]

    fig, ax = plt.subplots(figsize=(11, 6.5))
    image = ax.imshow(pivot, vmin=-1, vmax=1, cmap="coolwarm")
    ax.set_xticks(
        range(len(pivot.columns)),
        [LABELS.get(col, col) for col in pivot.columns],
        rotation=45,
        ha="right",
    )
    ax.set_yticks(range(len(pivot.index)), [LABELS.get(row, row) for row in pivot.index])
    for row_index in range(pivot.shape[0]):
        for col_index in range(pivot.shape[1]):
            value = pivot.iloc[row_index, col_index]
            ax.text(
                col_index,
                row_index,
                "" if pd.isna(value) else f"{value:.2f}",
                ha="center",
                va="center",
                fontsize=8,
            )
    ax.set_title("Movement Trait Correlations")
    fig.colorbar(image, ax=ax, label="Pearson correlation")
    fig.tight_layout()
    fig.savefig(PLOTS_DIR / "movement_correlation_heatmap.png", dpi=160)
    plt.close(fig)


def predict_from_raw(
    raw_row: pd.DataFrame,
    means: pd.Series,
    stds: pd.Series,
    coefficients: pd.Series,
    features: list[str],
) -> np.ndarray:
    z = (raw_row[PREDICTORS] - means) / stds
    for interaction, (left, right) in INTERACTIONS.items():
        z[interaction] = z[left] * z[right]
    matrix = np.column_stack([np.ones(len(z)), z[features].to_numpy(dtype=float)])
    return matrix @ coefficients.to_numpy(dtype=float)


def make_partial_dependence_plots(
    model_df: pd.DataFrame,
    means: pd.Series,
    stds: pd.Series,
    coefficient_table: pd.DataFrame,
    features: list[str],
) -> None:
    coefficients = coefficient_table.set_index("variable").loc[["Intercept", *features], "coefficient"]
    base = pd.DataFrame([model_df[PREDICTORS].median()])

    for variable in PREDICTORS:
        grid = np.linspace(model_df[variable].quantile(0.05), model_df[variable].quantile(0.95), 120)
        rows = pd.concat([base] * len(grid), ignore_index=True)
        rows[variable] = grid
        predictions = predict_from_raw(rows, means, stds, coefficients, features)

        fig, ax = plt.subplots(figsize=(8, 6))
        ax.plot(grid, predictions, color="#1f6f50", linewidth=2.5)
        ax.set_title(f"Partial Dependence: {LABELS[variable]}")
        ax.set_xlabel(LABELS[variable])
        ax.set_ylabel("Predicted Pitch Value Score")
        fig.tight_layout()
        fig.savefig(PLOTS_DIR / f"partial_dependence_{variable}.png", dpi=160)
        plt.close(fig)

    for interaction, (movement, velocity) in INTERACTIONS.items():
        x_grid = np.linspace(model_df[movement].quantile(0.05), model_df[movement].quantile(0.95), 70)
        y_grid = np.linspace(model_df[velocity].quantile(0.05), model_df[velocity].quantile(0.95), 70)
        xx, yy = np.meshgrid(x_grid, y_grid)
        rows = pd.concat([base] * xx.size, ignore_index=True)
        rows[movement] = xx.ravel()
        rows[velocity] = yy.ravel()
        predictions = predict_from_raw(rows, means, stds, coefficients, features).reshape(xx.shape)

        fig, ax = plt.subplots(figsize=(8, 6))
        contour = ax.contourf(xx, yy, predictions, levels=18, cmap="viridis")
        ax.set_title(f"Partial Dependence: {LABELS[interaction]}")
        ax.set_xlabel(LABELS[movement])
        ax.set_ylabel("Velocity")
        fig.colorbar(contour, ax=ax, label="Predicted Pitch Value Score")
        fig.tight_layout()
        fig.savefig(PLOTS_DIR / f"partial_dependence_{interaction}.png", dpi=160)
        plt.close(fig)


def format_p(value: float) -> str:
    return "<0.0001" if value < 0.0001 else f"{value:.4f}"


def write_report(
    model_df: pd.DataFrame,
    base_table: pd.DataFrame,
    interaction_table: pd.DataFrame,
    base_r2: float,
    interaction_r2: float,
    vif: pd.DataFrame,
    correlations: pd.DataFrame,
) -> None:
    final = interaction_table.merge(vif, on="variable", how="left")
    importance = final.loc[final["variable"].ne("Intercept")].copy()
    importance["importance"] = importance["coefficient"].abs()
    importance = importance.sort_values("importance", ascending=False)
    positive = importance.loc[importance["coefficient"].gt(0)].sort_values("coefficient", ascending=False)
    pvs_corr = (
        correlations.loc[correlations["target"].eq(DEPENDENT)]
        .copy()
        .sort_values("correlation", ascending=False)
    )
    xwoba_corr = (
        correlations.loc[correlations["target"].eq("xwoba_frontier")]
        .copy()
        .sort_values("correlation", ascending=True)
    )

    lines = [
        "# Pitch Movement Traits and Pitch Value Score",
        "",
        f"- Pitch-level source: `{PITCH_DATA_PATH}`",
        f"- Score source: `{SCORE_PATH}`",
        f"- Model data output: `{OUTPUT_PATH}`",
        f"- Regression coefficient output: `{COEFFICIENTS_PATH}`",
        f"- Movement correlation output: `{CORRELATIONS_PATH}`",
        f"- Groups modeled: {len(model_df):,}",
        "- Pitch type normalization: `Fastball` is grouped with `Four-Seam`; `Two-Seam` is grouped with `Sinker`.",
        f"- Dependent variable: `{DEPENDENT}`",
        "- Predictors were standardized before fitting; coefficients are Pitch Value Score points per one standard deviation.",
        "",
        "## Executive Summary",
        "",
        f"- Movement traits explain a modest share of Pitch Value Score variation: main-effects R-squared `{base_r2:.4f}`, interaction-model R-squared `{interaction_r2:.4f}`.",
        "- The clearest positive regression signals are `Spin x Velocity` and `Spin Rate`. In baseball terms, spin appears most valuable when it is paired with enough velocity to make the shape play.",
        "- Velocity is negative after controlling for pitch shape and spin. That should not be read as 'velocity is bad'; it means harder pitches in this league-level, pitch-type-mixed sample did not automatically grade better once movement and spin were included.",
        "- HB is negative in the interaction model, meaning more positive HB is associated with lower Pitch Value Score after controlling for the other movement traits.",
        "- IVB, extension, release height, and release side are weaker signals in this model.",
        "",
        "## How To Read The Regression",
        "",
        "All movement predictors were standardized before modeling. A coefficient of `+1.00` means that a one-standard-deviation increase in that trait is associated with a one-point increase in Pitch Value Score, holding the other modeled traits constant. A negative coefficient means the trait is associated with a lower Pitch Value Score after controls.",
        "",
        "Correlation is different from regression. The correlation tables show raw one-to-one relationships. The regression coefficients show conditional relationships after the other movement traits are included. When those disagree, it usually means pitch traits overlap with pitch type, role, or each other.",
        "",
        "## Models Fit",
        "",
        "| Model | Predictors | R-squared |",
        "|---|---|---:|",
        f"| Main effects | IVB, HB, spin rate, velocity, extension, release height, release side | {base_r2:.4f} |",
        f"| Main effects + interactions | Main effects plus IVB x velocity, HB x velocity, spin x velocity | {interaction_r2:.4f} |",
        "",
        "## Movement Correlations",
        "",
        "Raw correlations show how each movement trait relates to Pitch Value Score and xwOBA without controlling for the other traits. Positive correlation with Pitch Value Score is good. Negative correlation with `xwoba_frontier`, average exit velocity, HardHit%, or SweetSpot% is generally good for pitchers.",
        "",
        "### Correlation With Pitch Value Score",
        "",
        "| Trait | Correlation | P-value |",
        "|---|---:|---:|",
    ]
    for row in pvs_corr.itertuples(index=False):
        lines.append(
            f"| `{LABELS.get(row.movement_trait, row.movement_trait)}` | "
            f"{row.correlation:.4f} | {format_p(row.p_value)} |"
        )

    lines.extend(
        [
            "",
            "### Correlation With xwOBA",
            "",
            "| Trait | Correlation | P-value |",
            "|---|---:|---:|",
        ]
    )
    for row in xwoba_corr.itertuples(index=False):
        lines.append(
            f"| `{LABELS.get(row.movement_trait, row.movement_trait)}` | "
            f"{row.correlation:.4f} | {format_p(row.p_value)} |"
        )

    lines.extend(
        [
        "",
        "## Main Effects Model",
        "",
        "| Variable | Coefficient | P-value |",
        "|---|---:|---:|",
        ]
    )
    for row in base_table.itertuples(index=False):
        label = LABELS.get(row.variable, row.variable)
        lines.append(f"| `{label}` | {row.coefficient:.4f} | {format_p(row.p_value)} |")

    lines.extend(
        [
            "",
            "## Interaction Model",
            "",
            "| Variable | Std. Coef | P-value | VIF |",
            "|---|---:|---:|---:|",
        ]
    )
    for row in final.itertuples(index=False):
        label = LABELS.get(row.variable, row.variable)
        vif_value = "" if pd.isna(row.vif) else f"{row.vif:.2f}"
        lines.append(f"| `{label}` | {row.coefficient:.4f} | {format_p(row.p_value)} | {vif_value} |")

    lines.extend(
        [
            "",
            "## Variable Importance",
            "",
            "| Rank | Variable | Std. Coef | Direction |",
            "|---:|---|---:|---|",
        ]
    )
    for rank, row in enumerate(importance.itertuples(index=False), start=1):
        label = LABELS.get(row.variable, row.variable)
        direction = "higher pitch value" if row.coefficient > 0 else "lower pitch value"
        lines.append(f"| {rank} | `{label}` | {row.coefficient:.4f} | {direction} |")

    lines.extend(["", "## Traits Most Associated with Higher Pitch Value", ""])
    if positive.empty:
        lines.append("No movement traits had positive coefficients in the interaction model.")
    else:
        for row in positive.head(6).itertuples(index=False):
            label = LABELS.get(row.variable, row.variable)
            lines.append(f"- `{label}`: coefficient {row.coefficient:.4f}, p-value {format_p(row.p_value)}.")

    lines.extend(
        [
            "",
            "## Baseball Summary",
            "",
            "The model is descriptive, not a pure pitch-design law. It asks which movement and release traits separate higher-scoring pitcher-pitch types after the Pitch Value Score has already summarized whiff, strike, and contact-quality outcomes.",
            "",
            "Positive standardized coefficients point toward traits linked with better pitch value. Negative coefficients point toward traits linked with lower pitch value. The interaction terms test whether movement plays differently at higher velocity, which matters because the same IVB or horizontal break can look very different to hitters when it arrives harder.",
            "",
            "Use the partial dependence plots as the cleanest visual read: they hold the rest of the movement profile near typical values and show how predicted pitch value changes as one trait moves.",
            "",
            "## Plots",
            "",
        ]
    )
    for variable in PREDICTORS:
        lines.append(f"- `{PLOTS_DIR / f'effect_{variable}.png'}`")
    for variable in PREDICTORS:
        lines.append(f"- `{PLOTS_DIR / f'partial_dependence_{variable}.png'}`")
    for interaction in INTERACTIONS:
        lines.append(f"- `{PLOTS_DIR / f'partial_dependence_{interaction}.png'}`")
    lines.append(f"- `{PLOTS_DIR / 'movement_correlation_heatmap.png'}`")

    REPORT_PATH.write_text("\n".join(lines), encoding="utf-8")


def main() -> None:
    model_df = make_model_frame()
    model_df.to_csv(OUTPUT_PATH, index=False)

    z, means, stds = standardize_features(model_df)
    y = model_df[DEPENDENT].astype(float)

    base_features = PREDICTORS
    interaction_features = [*PREDICTORS, *INTERACTIONS.keys()]
    base_table, _, base_r2 = fit_ols(z[base_features], y)
    interaction_table, _, interaction_r2 = fit_ols(z[interaction_features], y)
    vif = vif_statistics(z[interaction_features])
    correlations = movement_correlations(model_df)

    make_effect_plots(model_df)
    make_correlation_heatmap(correlations)
    make_partial_dependence_plots(model_df, means, stds, interaction_table, interaction_features)
    interaction_table.merge(vif, on="variable", how="left").to_csv(COEFFICIENTS_PATH, index=False)
    correlations.to_csv(CORRELATIONS_PATH, index=False)
    write_report(model_df, base_table, interaction_table, base_r2, interaction_r2, vif, correlations)

    importance = interaction_table.loc[interaction_table["variable"].ne("Intercept")].copy()
    importance["importance"] = importance["coefficient"].abs()
    importance = importance.sort_values("importance", ascending=False)

    print(f"Wrote model data: {OUTPUT_PATH}")
    print(f"Wrote report: {REPORT_PATH}")
    print(f"Wrote plots to: {PLOTS_DIR}")
    print(f"Groups modeled: {len(model_df):,}")
    print(f"Main-effects R-squared: {base_r2:.4f}")
    print(f"Interaction R-squared: {interaction_r2:.4f}")
    print("\nInteraction model coefficients:")
    print(interaction_table.to_string(index=False))
    print("\nVariable importance:")
    print(importance[["variable", "coefficient", "p_value"]].to_string(index=False))


if __name__ == "__main__":
    main()
