from __future__ import annotations

import numpy as np
import pandas as pd

from paper_utils import DATA_DIR, DEPENDENTS, REPORT_DIR, design_matrix, ensure_dirs, fit_ols_hc3, is_batted_ball_dependent, markdown_table, model_result_rows, regression_frame_for, safe_standardize


INPUT_PATH = DATA_DIR / "regression_dataset.csv"
OUTPUT_PATH = DATA_DIR / "robustness_results.csv"
REPORT_PATH = REPORT_DIR / "robustness_checks.md"
NUMERIC_FULL = ["movement_quality_20_80", "location_score_20_80", "pitch_count", "batted_ball_count"]
NUMERIC_SHORT = ["movement_quality_20_80", "location_score_20_80"]


def weighted_fit_rows(frame: pd.DataFrame, dependent: str, weights: pd.Series, check: str) -> list[dict[str, object]]:
    # WLS is implemented by premultiplying y and X by sqrt(weights).
    x, _ = design_matrix(frame, NUMERIC_FULL, ["pitch_type", "batter_side"])
    y = frame[dependent].astype(float)
    w = np.sqrt(pd.to_numeric(weights, errors="coerce").fillna(0).clip(lower=0).to_numpy())
    xw = x.mul(w, axis=0)
    yw = y * w
    fit = fit_ols_hc3(xw, yw)
    return model_result_rows(fit, dependent, check, f"{dependent} ~ weighted full model")


def fit_rows(frame: pd.DataFrame, dependent: str, check: str, sample: str, numeric: list[str], fixed: list[str]) -> list[dict[str, object]]:
    x, _ = design_matrix(frame, numeric, fixed)
    fit = fit_ols_hc3(x, frame[dependent])
    rows = model_result_rows(
        fit,
        dependent,
        check,
        f"{dependent} ~ {' + '.join([*numeric, *[f'C({f})' for f in fixed]])}",
    )
    for row in rows:
        row["sample"] = sample
    return rows


def cooks_trim(frame: pd.DataFrame, dependent: str) -> pd.DataFrame:
    x, _ = design_matrix(frame, NUMERIC_FULL, ["pitch_type", "batter_side"])
    fit = fit_ols_hc3(x, frame[dependent])
    resid = fit["resid"]
    h = fit["hat"]
    mse = max(np.sum(resid**2) / max(fit["n"] - fit["k"], 1), 1e-12)
    cooks = (resid**2 / mse) * h / ((1 - h) ** 2) / fit["k"]
    return frame.loc[cooks <= 4 / len(frame)].copy()


def robustness_for(df: pd.DataFrame, dependent: str) -> list[dict[str, object]]:
    frame = regression_frame_for(df, dependent).dropna(subset=NUMERIC_FULL + ["pitch_type", "batter_side"])
    if len(frame) < 20:
        return []
    rows = []
    rows.extend(weighted_fit_rows(frame, dependent, frame["pitch_count"], "WLS pitch_count"))
    if is_batted_ball_dependent(dependent):
        rows.extend(weighted_fit_rows(frame, dependent, frame["batted_ball_count"], "WLS batted_ball_count"))

    standardized = safe_standardize(frame, [dependent, *NUMERIC_FULL])
    rows.extend(fit_rows(standardized, dependent, "Standardized OLS", "All", NUMERIC_FULL, ["pitch_type", "batter_side"]))

    trimmed = cooks_trim(frame, dependent)
    if len(trimmed) >= 20:
        rows.extend(fit_rows(trimmed, dependent, "Cook's distance <= 4/n", "All", NUMERIC_FULL, ["pitch_type", "batter_side"]))

    for pitch_type, group in frame.groupby("pitch_type"):
        if len(group) >= 30:
            rows.extend(fit_rows(group, dependent, "Pitch-type-specific", str(pitch_type), NUMERIC_SHORT, ["batter_side"]))

    for batter_side, group in frame.groupby("batter_side"):
        if len(group) >= 30:
            rows.extend(fit_rows(group, dependent, "Batter-side-specific", str(batter_side), NUMERIC_SHORT, ["pitch_type"]))
    return rows


def main() -> None:
    ensure_dirs()
    df = pd.read_csv(INPUT_PATH)
    rows = []
    for dependent in DEPENDENTS:
        rows.extend(robustness_for(df, dependent))
    results = pd.DataFrame(rows)
    results.to_csv(OUTPUT_PATH, index=False)
    key = results.loc[
        results["term"].isin(["movement_quality_20_80", "location_score_20_80"])
    ].copy()
    lines = [
        "# Robustness Checks",
        "",
        f"- Input dataset: `{INPUT_PATH}`",
        f"- Output CSV: `{OUTPUT_PATH}`",
        "",
        "## Movement vs Location Coefficients",
        "",
        *markdown_table(key, max_rows=None),
    ]
    REPORT_PATH.write_text("\n".join(lines), encoding="utf-8")
    print(f"Wrote robustness results: {OUTPUT_PATH}")
    print(f"Wrote report: {REPORT_PATH}")
    print(f"Rows: {len(results):,}")


if __name__ == "__main__":
    main()
