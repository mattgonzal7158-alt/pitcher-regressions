from __future__ import annotations

import pandas as pd

from paper_utils import DATA_DIR, DEPENDENTS, REPORT_DIR, design_matrix, ensure_dirs, fit_ols_hc3, markdown_table, model_result_rows, regression_frame_for


INPUT_PATH = DATA_DIR / "regression_dataset.csv"
OUTPUT_PATH = DATA_DIR / "main_regression_results.csv"
REPORT_PATH = REPORT_DIR / "main_regression_results.md"

MODELS = {
    "Model 1": (["movement_quality_20_80"], []),
    "Model 2": (["location_score_20_80"], []),
    "Model 3": (["movement_quality_20_80", "location_score_20_80"], []),
    "Model 4": (["movement_quality_20_80", "location_score_20_80"], ["pitch_type", "batter_side"]),
    "Model 5": (
        ["movement_quality_20_80", "location_score_20_80", "pitch_count", "batted_ball_count"],
        ["pitch_type", "batter_side"],
    ),
}


def formula_label(dependent: str, numeric: list[str], fixed: list[str]) -> str:
    terms = [*numeric, *[f"C({fe})" for fe in fixed]]
    return f"{dependent} ~ " + " + ".join(terms)


def run_model(df: pd.DataFrame, dependent: str, model_name: str, numeric: list[str], fixed: list[str]) -> list[dict[str, object]]:
    frame = regression_frame_for(df, dependent).dropna(subset=numeric + fixed)
    if len(frame) < 10:
        return []
    x, _ = design_matrix(frame, numeric, fixed)
    fit = fit_ols_hc3(x, frame[dependent])
    return model_result_rows(fit, dependent, model_name, formula_label(dependent, numeric, fixed))


def main() -> None:
    ensure_dirs()
    df = pd.read_csv(INPUT_PATH)
    rows = []
    for dependent in DEPENDENTS:
        for model_name, (numeric, fixed) in MODELS.items():
            rows.extend(run_model(df, dependent, model_name, numeric, fixed))
    results = pd.DataFrame(rows)
    results.to_csv(OUTPUT_PATH, index=False)

    report_cols = [
        "dependent",
        "model",
        "term",
        "coefficient",
        "robust_se",
        "t_stat",
        "p_value",
        "p_stars",
        "ci_lower",
        "ci_upper",
        "r_squared",
        "adj_r_squared",
        "sample_size",
    ]
    key_terms = results.loc[
        results["term"].isin(["movement_quality_20_80", "location_score_20_80", "pitch_count", "batted_ball_count"])
    ].copy()
    lines = [
        "# Main Regression Results",
        "",
        f"- Input dataset: `{INPUT_PATH}`",
        f"- Output CSV: `{OUTPUT_PATH}`",
        "- Estimator: OLS with HC3 robust standard errors.",
        "",
        "## Key Coefficients",
        "",
        *markdown_table(key_terms[report_cols], max_rows=None),
        "",
        "## Full Regression Output",
        "",
        *markdown_table(results[report_cols], max_rows=None),
    ]
    REPORT_PATH.write_text("\n".join(lines), encoding="utf-8")
    print(f"Wrote main regression results: {OUTPUT_PATH}")
    print(f"Wrote report: {REPORT_PATH}")
    print(f"Rows: {len(results):,}")


if __name__ == "__main__":
    main()
