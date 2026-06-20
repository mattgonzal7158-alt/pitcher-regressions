from __future__ import annotations

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from scipy import stats
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score
from sklearn.preprocessing import StandardScaler


INPUT_PATH = Path("data/processed/2026-data-with-woba-xwoba.parquet")
AGG_OUTPUT_PATH = Path("data/processed/pitcher_pitch_type_xwoba_metrics.csv")
REPORT_PATH = Path("reports/xwoba_pitch_metric_regression_report.md")
PLOTS_DIR = Path("plots/xwoba_pitch_metrics")

MIN_PITCHES = 50
MIN_BATTED_BALLS = 10

DEPENDENT = "xwoba_frontier"
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

    swing = clean_bool(pitch_call.isin(
        [
            "Strike Swinging",
            "Foul Ball Not Fieldable",
            "Foul Ball Fieldable",
            "In Play",
        ]
    ))
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
    batted_ball = df["xwoba_frontier"].notna()
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
    grouped["avg_exit_velocity"] = safe_rate(
        grouped["exit_velocity_sum"], grouped["batted_ball_count"]
    )
    grouped["hardhit_pct"] = safe_rate(grouped["hardhit_count"], grouped["batted_ball_count"])
    grouped["barrel_pct"] = safe_rate(grouped["barrel_count"], grouped["batted_ball_count"])
    grouped["sweetspot_pct"] = safe_rate(grouped["sweetspot_count"], grouped["batted_ball_count"])

    return grouped


def fit_ols(x: pd.DataFrame, y: pd.Series) -> pd.DataFrame:
    x_matrix = np.column_stack([np.ones(len(x)), x.to_numpy(dtype=float)])
    y_values = y.to_numpy(dtype=float)
    coefficients, _, _, _ = np.linalg.lstsq(x_matrix, y_values, rcond=None)
    predictions = x_matrix @ coefficients
    residuals = y_values - predictions
    dof = len(y_values) - x_matrix.shape[1]
    mse = np.sum(residuals**2) / dof
    covariance = mse * np.linalg.inv(x_matrix.T @ x_matrix)
    standard_errors = np.sqrt(np.diag(covariance))
    t_values = coefficients / standard_errors
    p_values = 2 * stats.t.sf(np.abs(t_values), dof)

    return pd.DataFrame(
        {
            "variable": ["Intercept", *x.columns],
            "coefficient": coefficients,
            "std_error": standard_errors,
            "t_stat": t_values,
            "p_value": p_values,
        }
    )


def standardized_coefficients(x: pd.DataFrame, y: pd.Series) -> pd.DataFrame:
    scaler_x = StandardScaler()
    scaler_y = StandardScaler()
    x_scaled = scaler_x.fit_transform(x)
    y_scaled = scaler_y.fit_transform(y.to_numpy().reshape(-1, 1)).ravel()
    model = LinearRegression().fit(x_scaled, y_scaled)
    return pd.DataFrame(
        {"variable": x.columns, "standardized_coefficient": model.coef_}
    )


def vif_statistics(x: pd.DataFrame) -> pd.DataFrame:
    rows = []
    for column in x.columns:
        other_columns = [candidate for candidate in x.columns if candidate != column]
        model = LinearRegression().fit(x[other_columns], x[column])
        r_squared = r2_score(x[column], model.predict(x[other_columns]))
        vif = np.inf if np.isclose(1 - r_squared, 0) else 1 / (1 - r_squared)
        rows.append({"variable": column, "vif": vif})
    return pd.DataFrame(rows)


def make_plots(model_df: pd.DataFrame, coefficient_table: pd.DataFrame) -> None:
    PLOTS_DIR.mkdir(exist_ok=True)

    pretty_names = {
        "whiff_pct": "Whiff%",
        "csw_pct": "CSW%",
        "putaway_pct": "PutAway%",
        "k_pct": "K%",
        "avg_exit_velocity": "Average Exit Velocity",
        "hardhit_pct": "HardHit%",
        "barrel_pct": "Barrel%",
        "sweetspot_pct": "SweetSpot%",
    }

    for variable in PREDICTORS:
        fig, ax = plt.subplots(figsize=(8, 6))
        ax.scatter(model_df[variable], model_df[DEPENDENT], s=18, alpha=0.55, color="#356a8a")
        fit = np.polyfit(model_df[variable], model_df[DEPENDENT], deg=1)
        x_line = np.linspace(model_df[variable].min(), model_df[variable].max(), 100)
        ax.plot(x_line, fit[0] * x_line + fit[1], color="#b33f3f", linewidth=2)
        ax.set_title(f"{pretty_names[variable]} vs xwOBA")
        ax.set_xlabel(pretty_names[variable])
        ax.set_ylabel("xwoba_frontier")
        fig.tight_layout()
        fig.savefig(PLOTS_DIR / f"{variable}_vs_xwoba.png", dpi=160)
        plt.close(fig)

    coef_plot = coefficient_table.loc[coefficient_table["variable"].ne("Intercept")].copy()
    coef_plot = coef_plot.sort_values("standardized_coefficient")
    fig, ax = plt.subplots(figsize=(9, 6))
    colors = np.where(coef_plot["standardized_coefficient"].lt(0), "#2d6a4f", "#9d3d3d")
    ax.barh(coef_plot["variable"].map(pretty_names), coef_plot["standardized_coefficient"], color=colors)
    ax.axvline(0, color="#333333", linewidth=1)
    ax.set_title("Standardized Relationship with xwOBA")
    ax.set_xlabel("Standardized Coefficient")
    fig.tight_layout()
    fig.savefig(PLOTS_DIR / "standardized_coefficients.png", dpi=160)
    plt.close(fig)

    corr = model_df[[DEPENDENT, *PREDICTORS]].corr()
    fig, ax = plt.subplots(figsize=(9, 7))
    image = ax.imshow(corr, vmin=-1, vmax=1, cmap="coolwarm")
    labels = ["xwOBA", *[pretty_names[p] for p in PREDICTORS]]
    ax.set_xticks(range(len(labels)), labels=labels, rotation=45, ha="right")
    ax.set_yticks(range(len(labels)), labels=labels)
    for i in range(corr.shape[0]):
        for j in range(corr.shape[1]):
            ax.text(j, i, f"{corr.iloc[i, j]:.2f}", ha="center", va="center", fontsize=8)
    ax.set_title("Metric Correlations")
    fig.colorbar(image, ax=ax, label="Correlation")
    fig.tight_layout()
    fig.savefig(PLOTS_DIR / "metric_correlation_heatmap.png", dpi=160)
    plt.close(fig)


def format_p(value: float) -> str:
    return "<0.0001" if value < 0.0001 else f"{value:.4f}"


def write_report(
    aggregate_df: pd.DataFrame,
    model_df: pd.DataFrame,
    coefficient_table: pd.DataFrame,
    overall_r2: float,
) -> None:
    ranked = coefficient_table.loc[coefficient_table["variable"].ne("Intercept")].copy()
    ranked["importance"] = ranked["standardized_coefficient"].abs()
    ranked = ranked.sort_values("importance", ascending=False)
    lower_xwoba = ranked.loc[ranked["standardized_coefficient"].lt(0)].sort_values(
        "standardized_coefficient"
    )

    lines = [
        "# Pitch Metrics Predicting Frontier xwOBA",
        "",
        f"- Input file: `{INPUT_PATH}`",
        f"- Aggregate output: `{AGG_OUTPUT_PATH}`",
        f"- Aggregation level: pitcher + pitch type",
        f"- Total pitcher-pitch type groups: {len(aggregate_df):,}",
        f"- Regression groups after filters: {len(model_df):,}",
        f"- Filters: at least {MIN_PITCHES} pitches and {MIN_BATTED_BALLS} tracked batted balls",
        "- Pitch type normalization: `Fastball` is grouped with `Four-Seam`; `Two-Seam` is grouped with `Sinker`.",
        f"- Dependent variable: average `{DEPENDENT}`",
        f"- Model R-squared: {overall_r2:.4f}",
        "",
        "## Metric Definitions",
        "",
        "| Metric | Definition Used |",
        "|---|---|",
        "| Whiff% | `Strike Swinging / swings`; swings are swinging strikes, fouls, and balls in play. |",
        "| CSW% | `(Called Strike + Automatic Strike + Strike Swinging) / total pitches`. |",
        "| PutAway% | `Strikeout / two-strike pitches`. |",
        "| K% | `Strikeout / terminal PA-ending pitches` for that pitch type. |",
        "| Average Exit Velocity | Mean `hit_launch_exit_speed_y` on tracked batted balls. |",
        "| HardHit% | Batted balls with exit velocity at least 95 mph / tracked batted balls. |",
        "| Barrel% | Approximate Statcast barrel zone using EV at least 98 mph with launch-angle window expanding from 26-30 degrees. |",
        "| SweetSpot% | Batted balls with launch angle from 8 to 32 degrees / tracked batted balls. |",
        "",
        "## Regression Output",
        "",
        "| Variable | Coefficient | P-value | Standardized Coef | VIF |",
        "|---|---:|---:|---:|---:|",
    ]

    for row in coefficient_table.itertuples(index=False):
        vif = "" if row.variable == "Intercept" else f"{row.vif:.2f}"
        std = "" if pd.isna(row.standardized_coefficient) else f"{row.standardized_coefficient:.4f}"
        lines.append(
            f"| `{row.variable}` | {row.coefficient:.6f} | {format_p(row.p_value)} | {std} | {vif} |"
        )

    lines.extend(
        [
            "",
            "## Variable Importance",
            "",
            "| Rank | Variable | Standardized Coef | Direction |",
            "|---:|---|---:|---|",
        ]
    )
    for rank, row in enumerate(ranked.itertuples(index=False), start=1):
        direction = "lower xwOBA" if row.standardized_coefficient < 0 else "higher xwOBA"
        lines.append(
            f"| {rank} | `{row.variable}` | {row.standardized_coefficient:.4f} | {direction} |"
        )

    lines.extend(["", "## Most Associated with Lower xwOBA", ""])
    if lower_xwoba.empty:
        lines.append("No variables had negative standardized coefficients in this multivariate model.")
    else:
        for row in lower_xwoba.head(5).itertuples(index=False):
            lines.append(
                f"- `{row.variable}`: standardized coefficient {row.standardized_coefficient:.4f}, "
                f"p-value {format_p(row.p_value)}."
            )

    lines.extend(
        [
            "",
            "## Baseball Interpretation",
            "",
            "Negative coefficients indicate traits associated with suppressing expected damage on contact for a pitcher-pitch type. Positive coefficients indicate traits associated with allowing more expected damage.",
            "",
            "Miss metrics and contact metrics should be read together. A pitch can lower xwOBA either by missing bats and stealing strikes before contact happens, or by shaping contact into weaker, less optimal launch conditions. VIF values are included because these pitch traits overlap: for example, HardHit%, Barrel%, SweetSpot%, and average exit velocity often move together.",
            "",
            "In this model, the strongest lower-xwOBA indicators are the variables with the most negative standardized coefficients. Those are the best all-else-equal signals for pitcher-pitch types that prevent dangerous batted balls. The strongest positive coefficients identify risk traits: when those rise, average xwOBA tends to rise after controlling for the other metrics.",
            "",
            "## Visualizations",
            "",
            f"- `{PLOTS_DIR / 'standardized_coefficients.png'}`",
            f"- `{PLOTS_DIR / 'metric_correlation_heatmap.png'}`",
        ]
    )
    for variable in PREDICTORS:
        lines.append(f"- `{PLOTS_DIR / f'{variable}_vs_xwoba.png'}`")

    REPORT_PATH.write_text("\n".join(lines), encoding="utf-8")


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
    aggregate_df.to_csv(AGG_OUTPUT_PATH, index=False)

    model_df = aggregate_df.loc[
        aggregate_df["pitch_count"].ge(MIN_PITCHES)
        & aggregate_df["batted_ball_count"].ge(MIN_BATTED_BALLS)
    ].copy()
    model_df = model_df.dropna(subset=[DEPENDENT, *PREDICTORS])

    x = model_df[PREDICTORS].astype(float)
    y = model_df[DEPENDENT].astype(float)
    ols = fit_ols(x, y)
    std = standardized_coefficients(x, y)
    vif = vif_statistics(x)
    coefficient_table = (
        ols.merge(std, on="variable", how="left")
        .merge(vif, on="variable", how="left")
        .sort_values("variable", key=lambda s: s.eq("Intercept"), ascending=False)
    )

    x_matrix = np.column_stack([np.ones(len(x)), x.to_numpy(dtype=float)])
    coef = ols["coefficient"].to_numpy()
    predictions = x_matrix @ coef
    overall_r2 = r2_score(y, predictions)

    make_plots(model_df, coefficient_table)
    write_report(aggregate_df, model_df, coefficient_table, overall_r2)

    ranked = coefficient_table.loc[coefficient_table["variable"].ne("Intercept")].copy()
    ranked["importance"] = ranked["standardized_coefficient"].abs()
    ranked = ranked.sort_values("importance", ascending=False)

    print(f"Wrote aggregate metrics: {AGG_OUTPUT_PATH}")
    print(f"Wrote report: {REPORT_PATH}")
    print(f"Wrote plots to: {PLOTS_DIR}")
    print(f"Regression groups: {len(model_df):,}")
    print(f"Model R-squared: {overall_r2:.4f}")
    print("\nRegression coefficients:")
    print(coefficient_table.to_string(index=False))
    print("\nVariable importance:")
    print(ranked[["variable", "standardized_coefficient", "p_value", "vif"]].to_string(index=False))


if __name__ == "__main__":
    main()
