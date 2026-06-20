from __future__ import annotations

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

from paper_utils import DATA_DIR, DEPENDENTS, MAIN_PREDICTORS, PLOT_DIR, REPORT_DIR, ensure_dirs, markdown_table


DATASET_PATH = DATA_DIR / "regression_dataset.csv"
MAIN_RESULTS_PATH = DATA_DIR / "main_regression_results.csv"
ROBUSTNESS_PATH = DATA_DIR / "robustness_results.csv"
REPORT_PATH = REPORT_DIR / "paper_tables_and_figures.md"


def scatter_with_fit(df: pd.DataFrame, x: str, y: str, output_name: str, title: str) -> None:
    valid = df[[x, y]].dropna()
    fig, ax = plt.subplots(figsize=(8, 5))
    ax.scatter(valid[x], valid[y], alpha=0.55)
    if len(valid) >= 2:
        coef = np.polyfit(valid[x], valid[y], 1)
        x_line = np.linspace(valid[x].min(), valid[x].max(), 100)
        ax.plot(x_line, coef[0] * x_line + coef[1], color="#b33f3f", linewidth=2)
    ax.set_xlabel(x)
    ax.set_ylabel(y)
    ax.set_title(title)
    fig.tight_layout()
    fig.savefig(PLOT_DIR / output_name, dpi=160)
    plt.close(fig)


def main() -> None:
    ensure_dirs()
    df = pd.read_csv(DATASET_PATH)
    main_results = pd.read_csv(MAIN_RESULTS_PATH)
    robustness = pd.read_csv(ROBUSTNESS_PATH)
    if "check" not in robustness.columns and "sample" in robustness.columns:
        robustness["check"] = robustness["sample"]

    table_vars = [
        "pitch_count",
        "batted_ball_count",
        *DEPENDENTS,
        "movement_quality_20_80",
        "location_score_20_80",
    ]
    desc = df[table_vars].describe().T.reset_index().rename(columns={"index": "variable"})
    corr = df[table_vars].corr().reset_index().rename(columns={"index": "variable"})
    main_key = main_results.loc[
        main_results["term"].isin(["movement_quality_20_80", "location_score_20_80"])
    ].copy()
    robust_key = robustness.loc[
        robustness["term"].isin(["movement_quality_20_80", "location_score_20_80"])
    ].copy()
    pitch_type_table = robust_key.loc[robust_key["check"].eq("Pitch-type-specific")].copy()
    side_table = robust_key.loc[robust_key["check"].eq("Batter-side-specific")].copy()

    r2 = main_results[["dependent", "model", "r_squared"]].drop_duplicates()
    fig, ax = plt.subplots(figsize=(9, 5))
    for dependent, group in r2.groupby("dependent"):
        ordered = group.sort_values("model")
        ax.plot(ordered["model"], ordered["r_squared"], marker="o", label=dependent)
    ax.set_ylabel("R-squared")
    ax.set_title("R-squared by Model")
    ax.legend()
    fig.tight_layout()
    fig.savefig(PLOT_DIR / "r_squared_comparison.png", dpi=160)
    plt.close(fig)

    scatter_with_fit(df, "movement_quality_20_80", "xwoba_frontier", "movement_vs_xwoba.png", "Movement Quality vs xwOBA")
    scatter_with_fit(df, "location_score_20_80", "xwoba_frontier", "location_vs_xwoba.png", "Location Score vs xwOBA")
    scatter_with_fit(df, "movement_quality_20_80", "whiff_pct", "movement_vs_whiff_pct.png", "Movement Quality vs Whiff%")
    scatter_with_fit(df, "location_score_20_80", "hardhit_pct", "location_vs_hardhit_pct.png", "Location Score vs HardHit%")

    coef = main_key.loc[main_key["model"].eq("Model 5")].copy()
    coef["label"] = coef["dependent"] + " / " + coef["term"].str.replace("_20_80", "", regex=False)
    fig, ax = plt.subplots(figsize=(10, 6))
    colors = coef["term"].map({"movement_quality_20_80": "#4c78a8", "location_score_20_80": "#f58518"})
    ax.barh(coef["label"], coef["coefficient"], color=colors)
    ax.axvline(0, color="black", linewidth=1)
    ax.set_title("Movement vs Location Coefficients, Full Model")
    ax.set_xlabel("Coefficient")
    fig.tight_layout()
    fig.savefig(PLOT_DIR / "movement_location_coefficient_comparison.png", dpi=160)
    plt.close(fig)

    lines = [
        "# Paper Tables and Figures",
        "",
        "## Table 1. Descriptive Statistics",
        "",
        *markdown_table(desc, max_rows=None),
        "",
        "## Table 2. Correlation Matrix",
        "",
        *markdown_table(corr, max_rows=None),
        "",
        "## Table 3. Main Regression Table",
        "",
        *markdown_table(main_key, max_rows=None),
        "",
        "## Table 4. Robustness Regression Table",
        "",
        *markdown_table(robust_key, max_rows=None),
        "",
        "## Table 5. Pitch-Type-Specific Results",
        "",
        *markdown_table(pitch_type_table, max_rows=None),
        "",
        "## Table 6. Batter-Side-Specific Results",
        "",
        *markdown_table(side_table, max_rows=None),
        "",
        "## Figures",
        "",
        "- `paper_research/paper_1_movement_vs_location/plots/r_squared_comparison.png`",
        "- `paper_research/paper_1_movement_vs_location/plots/movement_vs_xwoba.png`",
        "- `paper_research/paper_1_movement_vs_location/plots/location_vs_xwoba.png`",
        "- `paper_research/paper_1_movement_vs_location/plots/movement_vs_whiff_pct.png`",
        "- `paper_research/paper_1_movement_vs_location/plots/location_vs_hardhit_pct.png`",
        "- `paper_research/paper_1_movement_vs_location/plots/movement_location_coefficient_comparison.png`",
    ]
    REPORT_PATH.write_text("\n".join(lines), encoding="utf-8")

    print(f"Wrote paper tables and figures report: {REPORT_PATH}")
    print(f"Wrote figures to: {PLOT_DIR}")


if __name__ == "__main__":
    main()
