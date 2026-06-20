from __future__ import annotations

from pathlib import Path

import numpy as np
import pandas as pd
from scipy import stats


PROJECT_ROOT = Path(__file__).resolve().parents[3]
PAPER_ROOT = Path(__file__).resolve().parents[1]
DATA_DIR = PAPER_ROOT / "data"
REPORT_DIR = PAPER_ROOT / "reports"
PLOT_DIR = PAPER_ROOT / "plots"
DIAGNOSTIC_PLOT_DIR = PLOT_DIR / "diagnostics"

MASTER_CANDIDATES = [
    PROJECT_ROOT / "data" / "processed" / "master_pitch_evaluation_table_v2.csv",
    PROJECT_ROOT / "data" / "processed" / "master_pitch_evaluation_table.csv",
]
ENRICHED_PITCH_PATH = PROJECT_ROOT / "data" / "processed" / "2026-data-with-woba-xwoba.parquet"

DEPENDENTS = ["xwoba_frontier", "woba_value", "whiff_pct", "hardhit_pct"]
MAIN_PREDICTORS = ["movement_quality_20_80", "location_score_20_80"]
CONTROLS = ["pitch_count", "batted_ball_count"]
REGRESSION_COLUMNS = [
    "pitcher_name",
    "pitcher_id",
    "pitcher_team",
    "pitch_type",
    "batter_side",
    "pitch_count",
    "batted_ball_count",
    "xwoba_frontier",
    "woba_value",
    "whiff_pct",
    "hardhit_pct",
    "movement_quality_20_80",
    "location_score_20_80",
]

PITCH_TYPE_NORMALIZATION = {
    "Fastball": "Four-Seam",
    "Two-Seam": "Sinker",
}


def ensure_dirs() -> None:
    DATA_DIR.mkdir(parents=True, exist_ok=True)
    REPORT_DIR.mkdir(parents=True, exist_ok=True)
    PLOT_DIR.mkdir(parents=True, exist_ok=True)
    DIAGNOSTIC_PLOT_DIR.mkdir(parents=True, exist_ok=True)


def find_master_table() -> Path:
    for path in MASTER_CANDIDATES:
        if path.exists():
            return path
    candidates = sorted(
        (PROJECT_ROOT / "data" / "processed").glob("*master*pitch*evaluation*.csv"),
        key=lambda p: p.stat().st_mtime,
        reverse=True,
    )
    if candidates:
        return candidates[0]
    raise FileNotFoundError("No master pitch evaluation table found in data/processed.")


def normalize_pitch_type(series: pd.Series) -> pd.Series:
    return series.astype("string").replace(PITCH_TYPE_NORMALIZATION)


def normalize_batter_side(series: pd.Series) -> pd.Series:
    side = series.astype("string").str.upper().str.strip()
    return side.replace({"RIGHT": "R", "LEFT": "L", "RHH": "R", "LHH": "L"})


def normalize_pitcher_id(series: pd.Series) -> pd.Series:
    numeric = pd.to_numeric(series, errors="coerce")
    return numeric.astype("Int64").astype("string")


def add_join_keys(df: pd.DataFrame) -> pd.DataFrame:
    work = df.copy()
    if "pitch_type" in work.columns:
        work["pitch_type"] = normalize_pitch_type(work["pitch_type"])
    if "batter_side" in work.columns:
        work["batter_side"] = normalize_batter_side(work["batter_side"])
    elif "batter_side_canonical" in work.columns:
        work["batter_side"] = normalize_batter_side(work["batter_side_canonical"])
    if "pitcher_id" in work.columns:
        work["pitcher_id_key"] = normalize_pitcher_id(work["pitcher_id"])
    return work


def is_batted_ball_dependent(dependent: str) -> bool:
    return dependent in {"xwoba_frontier", "woba_value", "hardhit_pct"}


def regression_frame_for(df: pd.DataFrame, dependent: str) -> pd.DataFrame:
    columns = [
        dependent,
        "movement_quality_20_80",
        "location_score_20_80",
        "pitch_type",
        "batter_side",
        "pitch_count",
        "batted_ball_count",
    ]
    required = [dependent, "movement_quality_20_80", "location_score_20_80"]
    if is_batted_ball_dependent(dependent):
        required.append("batted_ball_count")
    out = df[columns].copy()
    out = out.dropna(subset=required)
    if is_batted_ball_dependent(dependent):
        out = out.loc[pd.to_numeric(out["batted_ball_count"], errors="coerce").ge(10)]
    return out


def stars(p_value: float) -> str:
    if pd.isna(p_value):
        return ""
    if p_value < 0.001:
        return "***"
    if p_value < 0.01:
        return "**"
    if p_value < 0.05:
        return "*"
    if p_value < 0.1:
        return "+"
    return ""


def markdown_table(df: pd.DataFrame, max_rows: int | None = None) -> list[str]:
    if df.empty:
        return ["No rows."]
    show = df if max_rows is None else df.head(max_rows)
    cols = list(show.columns)
    lines = [
        "| " + " | ".join(cols) + " |",
        "|" + "|".join(["---"] * len(cols)) + "|",
    ]
    for row in show.itertuples(index=False):
        values = []
        for value in row:
            if pd.isna(value):
                values.append("")
            elif isinstance(value, float):
                values.append(f"{value:.4f}")
            else:
                values.append(str(value))
        lines.append("| " + " | ".join(values) + " |")
    return lines


def safe_standardize(frame: pd.DataFrame, columns: list[str]) -> pd.DataFrame:
    out = frame.copy()
    for column in columns:
        values = pd.to_numeric(out[column], errors="coerce")
        std = values.std(ddof=0)
        out[column] = 0.0 if pd.isna(std) or np.isclose(std, 0) else (values - values.mean()) / std
    return out


def design_matrix(
    df: pd.DataFrame,
    numeric_terms: list[str],
    fixed_effects: list[str] | None = None,
) -> tuple[pd.DataFrame, list[str]]:
    fixed_effects = fixed_effects or []
    pieces = []
    names = []
    for term in numeric_terms:
        pieces.append(pd.to_numeric(df[term], errors="coerce").rename(term))
        names.append(term)
    for fe in fixed_effects:
        dummies = pd.get_dummies(df[fe].astype("string"), prefix=fe, drop_first=True)
        dummies = dummies.astype(float)
        pieces.append(dummies)
        names.extend(list(dummies.columns))
    x = pd.concat(pieces, axis=1) if pieces else pd.DataFrame(index=df.index)
    return x.astype(float), names


def fit_ols_hc3(x: pd.DataFrame, y: pd.Series) -> dict[str, object]:
    x_values = x.to_numpy(dtype=float)
    y_values = y.to_numpy(dtype=float)
    x_matrix = np.column_stack([np.ones(len(x_values)), x_values])
    names = ["Intercept", *list(x.columns)]
    xtx_inv = np.linalg.pinv(x_matrix.T @ x_matrix)
    beta = xtx_inv @ x_matrix.T @ y_values
    fitted = x_matrix @ beta
    resid = y_values - fitted
    n = len(y_values)
    k = x_matrix.shape[1]
    hat = np.einsum("ij,jk,ik->i", x_matrix, xtx_inv, x_matrix)
    scale = (resid / np.clip(1 - hat, 1e-9, None)) ** 2
    meat = x_matrix.T @ (x_matrix * scale[:, None])
    cov = xtx_inv @ meat @ xtx_inv
    se = np.sqrt(np.clip(np.diag(cov), 0, None))
    t_stat = np.divide(beta, se, out=np.full_like(beta, np.nan), where=se != 0)
    df_resid = max(n - k, 1)
    p_values = 2 * stats.t.sf(np.abs(t_stat), df_resid)
    ci_low = beta - stats.t.ppf(0.975, df_resid) * se
    ci_high = beta + stats.t.ppf(0.975, df_resid) * se
    total_ss = np.sum((y_values - y_values.mean()) ** 2)
    resid_ss = np.sum(resid**2)
    r2 = np.nan if np.isclose(total_ss, 0) else 1 - resid_ss / total_ss
    adj_r2 = np.nan if n <= k or pd.isna(r2) else 1 - (1 - r2) * (n - 1) / (n - k)
    sigma2 = max(resid_ss / n, 1e-12)
    aic = n * np.log(sigma2) + 2 * k
    bic = n * np.log(sigma2) + np.log(n) * k
    return {
        "names": names,
        "beta": beta,
        "se": se,
        "t_stat": t_stat,
        "p_values": p_values,
        "ci_low": ci_low,
        "ci_high": ci_high,
        "fitted": fitted,
        "resid": resid,
        "hat": hat,
        "r_squared": r2,
        "adj_r_squared": adj_r2,
        "aic": aic,
        "bic": bic,
        "n": n,
        "k": k,
        "x_matrix": x_matrix,
    }


def model_result_rows(
    fit: dict[str, object],
    dependent: str,
    model: str,
    formula: str,
) -> list[dict[str, object]]:
    rows = []
    for i, term in enumerate(fit["names"]):
        rows.append(
            {
                "dependent": dependent,
                "model": model,
                "formula": formula,
                "term": term,
                "coefficient": fit["beta"][i],
                "robust_se": fit["se"][i],
                "t_stat": fit["t_stat"][i],
                "p_value": fit["p_values"][i],
                "p_stars": stars(fit["p_values"][i]),
                "ci_lower": fit["ci_low"][i],
                "ci_upper": fit["ci_high"][i],
                "r_squared": fit["r_squared"],
                "adj_r_squared": fit["adj_r_squared"],
                "aic": fit["aic"],
                "bic": fit["bic"],
                "sample_size": fit["n"],
            }
        )
    return rows
