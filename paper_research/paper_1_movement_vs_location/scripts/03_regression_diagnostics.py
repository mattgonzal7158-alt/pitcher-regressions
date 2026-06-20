from __future__ import annotations

import itertools

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from scipy import stats

from paper_utils import DATA_DIR, DEPENDENTS, DIAGNOSTIC_PLOT_DIR, REPORT_DIR, design_matrix, ensure_dirs, fit_ols_hc3, markdown_table, regression_frame_for


INPUT_PATH = DATA_DIR / "regression_dataset.csv"
OUTPUT_PATH = DATA_DIR / "diagnostic_tests.csv"
REPORT_PATH = REPORT_DIR / "regression_diagnostics.md"
NUMERIC = ["movement_quality_20_80", "location_score_20_80", "pitch_count", "batted_ball_count"]


def r_squared(x: np.ndarray, y: np.ndarray) -> float:
    x_matrix = np.column_stack([np.ones(len(x)), x])
    beta = np.linalg.pinv(x_matrix.T @ x_matrix) @ x_matrix.T @ y
    pred = x_matrix @ beta
    total = np.sum((y - y.mean()) ** 2)
    return np.nan if np.isclose(total, 0) else 1 - np.sum((y - pred) ** 2) / total


def vif_rows(frame: pd.DataFrame, dependent: str) -> list[dict[str, object]]:
    rows = []
    for variable in NUMERIC:
        others = [col for col in NUMERIC if col != variable]
        valid = frame[[variable, *others]].dropna()
        if len(valid) < 5:
            vif = np.nan
        else:
            r2 = r_squared(valid[others].to_numpy(float), valid[variable].to_numpy(float))
            vif = np.inf if np.isclose(1 - r2, 0) else 1 / (1 - r2)
        rows.append({"dependent": dependent, "diagnostic": "VIF", "variable": variable, "value": vif, "p_value": np.nan})
    return rows


def lm_test(resid: np.ndarray, aux_x: pd.DataFrame, name: str, dependent: str) -> dict[str, object]:
    y = resid**2
    r2 = r_squared(aux_x.to_numpy(float), y)
    df = aux_x.shape[1]
    lm = len(y) * r2
    p = stats.chi2.sf(lm, df)
    return {"dependent": dependent, "diagnostic": name, "variable": "", "value": lm, "p_value": p}


def make_plots(dependent: str, fit: dict[str, object]) -> None:
    fitted = fit["fitted"]
    resid = fit["resid"]
    safe = dependent.replace("_", "-")

    fig, ax = plt.subplots(figsize=(8, 5))
    ax.scatter(fitted, resid, alpha=0.65)
    ax.axhline(0, color="black", linewidth=1)
    ax.set_xlabel("Fitted values")
    ax.set_ylabel("Residuals")
    ax.set_title(f"{dependent}: Residuals vs Fitted")
    fig.tight_layout()
    fig.savefig(DIAGNOSTIC_PLOT_DIR / f"{safe}_residuals_vs_fitted.png", dpi=160)
    plt.close(fig)

    fig, ax = plt.subplots(figsize=(6, 6))
    stats.probplot(resid, dist="norm", plot=ax)
    ax.set_title(f"{dependent}: QQ Plot")
    fig.tight_layout()
    fig.savefig(DIAGNOSTIC_PLOT_DIR / f"{safe}_qq_plot.png", dpi=160)
    plt.close(fig)

    fig, ax = plt.subplots(figsize=(8, 5))
    ax.hist(resid, bins=25, color="#4c78a8", edgecolor="white")
    ax.set_title(f"{dependent}: Residual Histogram")
    fig.tight_layout()
    fig.savefig(DIAGNOSTIC_PLOT_DIR / f"{safe}_residual_histogram.png", dpi=160)
    plt.close(fig)

    leverage = fit["hat"]
    cooks = (resid**2 / max(np.sum(resid**2) / max(fit["n"] - fit["k"], 1), 1e-12)) * leverage / ((1 - leverage) ** 2) / fit["k"]
    fig, ax = plt.subplots(figsize=(8, 5))
    ax.scatter(leverage, cooks, alpha=0.65)
    ax.set_xlabel("Leverage")
    ax.set_ylabel("Cook's distance")
    ax.set_title(f"{dependent}: Leverage / Influence")
    fig.tight_layout()
    fig.savefig(DIAGNOSTIC_PLOT_DIR / f"{safe}_influence_plot.png", dpi=160)
    plt.close(fig)


def diagnostics_for(df: pd.DataFrame, dependent: str) -> list[dict[str, object]]:
    frame = regression_frame_for(df, dependent).dropna(subset=NUMERIC + ["pitch_type", "batter_side"])
    if len(frame) < 20:
        return []
    x, _ = design_matrix(frame, NUMERIC, ["pitch_type", "batter_side"])
    fit = fit_ols_hc3(x, frame[dependent])
    resid = fit["resid"]
    rows = vif_rows(frame, dependent)

    aux = frame[NUMERIC].astype(float)
    rows.append(lm_test(resid, aux, "Breusch-Pagan LM", dependent))
    white = aux.copy()
    for col in NUMERIC:
        white[f"{col}_sq"] = white[col] ** 2
    for left, right in itertools.combinations(NUMERIC, 2):
        white[f"{left}_x_{right}"] = white[left] * white[right]
    rows.append(lm_test(resid, white, "White LM", dependent))

    jb = stats.jarque_bera(resid)
    shapiro_stat, shapiro_p = (np.nan, np.nan)
    if 3 <= len(resid) <= 5000:
        shapiro_stat, shapiro_p = stats.shapiro(resid)
    dw = np.sum(np.diff(resid) ** 2) / np.sum(resid**2)
    rows.extend(
        [
            {"dependent": dependent, "diagnostic": "Jarque-Bera", "variable": "", "value": jb.statistic, "p_value": jb.pvalue},
            {"dependent": dependent, "diagnostic": "Shapiro-Wilk", "variable": "", "value": shapiro_stat, "p_value": shapiro_p},
            {"dependent": dependent, "diagnostic": "Durbin-Watson", "variable": "", "value": dw, "p_value": np.nan},
            {"dependent": dependent, "diagnostic": "Residual mean", "variable": "", "value": resid.mean(), "p_value": np.nan},
            {"dependent": dependent, "diagnostic": "Residual std", "variable": "", "value": resid.std(ddof=1), "p_value": np.nan},
        ]
    )
    make_plots(dependent, fit)
    return rows


def main() -> None:
    ensure_dirs()
    df = pd.read_csv(INPUT_PATH)
    rows = []
    for dependent in DEPENDENTS:
        rows.extend(diagnostics_for(df, dependent))
    diagnostics = pd.DataFrame(rows)
    diagnostics.to_csv(OUTPUT_PATH, index=False)
    lines = [
        "# Regression Diagnostics",
        "",
        f"- Input dataset: `{INPUT_PATH}`",
        f"- Output CSV: `{OUTPUT_PATH}`",
        f"- Diagnostic plots: `{DIAGNOSTIC_PLOT_DIR}`",
        "",
        "## Diagnostic Tests",
        "",
        *markdown_table(diagnostics, max_rows=None),
    ]
    REPORT_PATH.write_text("\n".join(lines), encoding="utf-8")
    print(f"Wrote diagnostics: {OUTPUT_PATH}")
    print(f"Wrote report: {REPORT_PATH}")
    print(f"Wrote plots to: {DIAGNOSTIC_PLOT_DIR}")


if __name__ == "__main__":
    main()
