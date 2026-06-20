from __future__ import annotations

import pandas as pd

from paper_utils import DATA_DIR, DEPENDENTS, REPORT_DIR, ensure_dirs, is_batted_ball_dependent, markdown_table


DATASET_PATH = DATA_DIR / "regression_dataset.csv"
MAIN_RESULTS_PATH = DATA_DIR / "main_regression_results.csv"
ROBUSTNESS_PATH = DATA_DIR / "robustness_results.csv"
OUTPUT_PATH = REPORT_DIR / "paper_results_summary.md"


def pitcher_direction(dependent: str, coefficient: float) -> str:
    if dependent in {"xwoba_frontier", "woba_value", "hardhit_pct"}:
        return "better" if coefficient < 0 else "worse"
    if dependent == "whiff_pct":
        return "better" if coefficient > 0 else "worse"
    return "higher" if coefficient > 0 else "lower"


def main() -> None:
    ensure_dirs()
    df = pd.read_csv(DATASET_PATH)
    main_results = pd.read_csv(MAIN_RESULTS_PATH)
    robustness = pd.read_csv(ROBUSTNESS_PATH)

    model5 = main_results.loc[
        main_results["model"].eq("Model 5")
        & main_results["term"].isin(["movement_quality_20_80", "location_score_20_80"])
    ].copy()
    findings = []
    for dep in DEPENDENTS:
        rows = model5.loc[model5["dependent"].eq(dep)].set_index("term")
        if rows.empty:
            continue
        move = rows.loc["movement_quality_20_80"]
        loc = rows.loc["location_score_20_80"]
        winner = (
            "movement quality"
            if abs(move["t_stat"]) > abs(loc["t_stat"])
            else "location quality"
        )
        findings.append(
            {
                "outcome": dep,
                "movement_coef": move["coefficient"],
                "movement_p": move["p_value"],
                "movement_direction": pitcher_direction(dep, move["coefficient"]),
                "location_coef": loc["coefficient"],
                "location_p": loc["p_value"],
                "location_direction": pitcher_direction(dep, loc["coefficient"]),
                "larger_explanatory_signal": winner,
                "model_5_r_squared": move["r_squared"],
            }
        )
    findings_df = pd.DataFrame(findings)

    lines = [
        "# Paper Results Summary",
        "",
        "## Research Question",
        "",
        "What better explains pitch success in the Frontier League: movement quality or location quality?",
        "",
        "## Hypotheses",
        "",
        "- H1: Better movement quality is associated with better pitch outcomes.",
        "- H2: Better location quality is associated with better pitch outcomes.",
        "- H3: Movement and location explain different parts of pitch success, so both retain signal when modeled together.",
        "",
        "## Data Description",
        "",
        f"The analysis uses `{DATASET_PATH}` with {len(df):,} pitcher + pitch type + batter side rows after the base filters. Rows require at least 25 pitches and non-missing movement and location scores. Batted-ball outcomes also require at least 10 batted balls in the regression scripts.",
        "",
        "## Regression Specification",
        "",
        "The primary specification is an OLS model with HC3 robust standard errors:",
        "",
        "`Y ~ movement_quality_20_80 + location_score_20_80 + C(pitch_type) + C(batter_side) + pitch_count + batted_ball_count`",
        "",
        "Dependent variables are `xwoba_frontier`, `woba_value`, `whiff_pct`, and `hardhit_pct`.",
        "",
        "## Key Findings",
        "",
        *markdown_table(findings_df, max_rows=None),
        "",
        "## Interpretation Rules",
        "",
        "- For `xwoba_frontier`, `woba_value`, and `hardhit_pct`, lower is better for pitchers.",
        "- For `whiff_pct`, higher is better for pitchers.",
        "- A negative coefficient on `xwoba_frontier`, `woba_value`, or `hardhit_pct` indicates better pitcher outcomes.",
        "- A positive coefficient on `whiff_pct` indicates better pitcher outcomes.",
        "",
        "## Movement Quality Interpretation",
        "",
    ]
    for row in findings_df.itertuples(index=False):
        lines.append(
            f"- `{row.outcome}`: a one-point increase in movement quality is associated with a coefficient of `{row.movement_coef:.4f}` in the full model, which points toward `{row.movement_direction}` pitcher outcomes under the outcome-specific direction rule."
        )
    lines.extend(["", "## Location Score Interpretation", ""])
    for row in findings_df.itertuples(index=False):
        lines.append(
            f"- `{row.outcome}`: a one-point increase in location score is associated with a coefficient of `{row.location_coef:.4f}` in the full model, which points toward `{row.location_direction}` pitcher outcomes under the outcome-specific direction rule."
        )
    lines.extend(
        [
            "",
            "## Movement vs Location by Outcome",
            "",
        ]
    )
    for row in findings_df.itertuples(index=False):
        lines.append(
            f"- `{row.outcome}`: `{row.larger_explanatory_signal}` has the larger absolute robust t-statistic in Model 5."
        )
    lines.extend(
        [
            "",
            "## Limitations",
            "",
            "- The analysis is observational and should not be read as causal.",
            "- Movement and location scores are themselves estimated summaries, so measurement error may attenuate relationships.",
            "- Some outcomes are batted-ball dependent and have smaller effective samples.",
            "- Pitcher usage, count, game context, opponent quality, and catcher/game-calling effects are not fully controlled.",
            "",
            "## Next Steps",
            "",
            "- Add count-state and handedness interaction controls at the pitch level.",
            "- Estimate hierarchical models with pitcher and team random effects.",
            "- Test whether movement quality changes the return to location quality by adding interaction terms.",
            "- Validate findings out of sample on future Frontier League data.",
            "",
            "## Robustness Output",
            "",
            f"Robustness checks are saved in `{ROBUSTNESS_PATH}`.",
        ]
    )
    OUTPUT_PATH.write_text("\n".join(lines), encoding="utf-8")
    print(f"Wrote paper results summary: {OUTPUT_PATH}")


if __name__ == "__main__":
    main()
