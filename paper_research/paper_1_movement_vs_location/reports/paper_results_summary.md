# Paper Results Summary

## Research Question

What better explains pitch success in the Frontier League: movement quality or location quality?

## Hypotheses

- H1: Better movement quality is associated with better pitch outcomes.
- H2: Better location quality is associated with better pitch outcomes.
- H3: Movement and location explain different parts of pitch success, so both retain signal when modeled together.

## Data Description

The analysis uses `C:\Users\mattg\OneDrive\Desktop\pitcher regressions\paper_research\paper_1_movement_vs_location\data\regression_dataset.csv` with 988 pitcher + pitch type + batter side rows after the base filters. Rows require at least 25 pitches and non-missing movement and location scores. Batted-ball outcomes also require at least 10 batted balls in the regression scripts.

## Regression Specification

The primary specification is an OLS model with HC3 robust standard errors:

`Y ~ movement_quality_20_80 + location_score_20_80 + C(pitch_type) + C(batter_side) + pitch_count + batted_ball_count`

Dependent variables are `xwoba_frontier`, `woba_value`, `whiff_pct`, and `hardhit_pct`.

## Key Findings

| outcome | movement_coef | movement_p | movement_direction | location_coef | location_p | location_direction | larger_explanatory_signal | model_5_r_squared |
|---|---|---|---|---|---|---|---|---|
| xwoba_frontier | -0.0003 | 0.1051 | better | -0.0012 | 0.0000 | better | location quality | 0.0962 |
| woba_value | -0.0001 | 0.6918 | better | -0.0006 | 0.0001 | better | location quality | 0.1153 |
| whiff_pct | -0.0004 | 0.3157 | worse | 0.0013 | 0.0005 | better | location quality | 0.2745 |
| hardhit_pct | -0.0001 | 0.7626 | better | -0.0017 | 0.0000 | better | location quality | 0.0647 |

## Interpretation Rules

- For `xwoba_frontier`, `woba_value`, and `hardhit_pct`, lower is better for pitchers.
- For `whiff_pct`, higher is better for pitchers.
- A negative coefficient on `xwoba_frontier`, `woba_value`, or `hardhit_pct` indicates better pitcher outcomes.
- A positive coefficient on `whiff_pct` indicates better pitcher outcomes.

## Movement Quality Interpretation

- `xwoba_frontier`: a one-point increase in movement quality is associated with a coefficient of `-0.0003` in the full model, which points toward `better` pitcher outcomes under the outcome-specific direction rule.
- `woba_value`: a one-point increase in movement quality is associated with a coefficient of `-0.0001` in the full model, which points toward `better` pitcher outcomes under the outcome-specific direction rule.
- `whiff_pct`: a one-point increase in movement quality is associated with a coefficient of `-0.0004` in the full model, which points toward `worse` pitcher outcomes under the outcome-specific direction rule.
- `hardhit_pct`: a one-point increase in movement quality is associated with a coefficient of `-0.0001` in the full model, which points toward `better` pitcher outcomes under the outcome-specific direction rule.

## Location Score Interpretation

- `xwoba_frontier`: a one-point increase in location score is associated with a coefficient of `-0.0012` in the full model, which points toward `better` pitcher outcomes under the outcome-specific direction rule.
- `woba_value`: a one-point increase in location score is associated with a coefficient of `-0.0006` in the full model, which points toward `better` pitcher outcomes under the outcome-specific direction rule.
- `whiff_pct`: a one-point increase in location score is associated with a coefficient of `0.0013` in the full model, which points toward `better` pitcher outcomes under the outcome-specific direction rule.
- `hardhit_pct`: a one-point increase in location score is associated with a coefficient of `-0.0017` in the full model, which points toward `better` pitcher outcomes under the outcome-specific direction rule.

## Movement vs Location by Outcome

- `xwoba_frontier`: `location quality` has the larger absolute robust t-statistic in Model 5.
- `woba_value`: `location quality` has the larger absolute robust t-statistic in Model 5.
- `whiff_pct`: `location quality` has the larger absolute robust t-statistic in Model 5.
- `hardhit_pct`: `location quality` has the larger absolute robust t-statistic in Model 5.

## Limitations

- The analysis is observational and should not be read as causal.
- Movement and location scores are themselves estimated summaries, so measurement error may attenuate relationships.
- Some outcomes are batted-ball dependent and have smaller effective samples.
- Pitcher usage, count, game context, opponent quality, and catcher/game-calling effects are not fully controlled.

## Next Steps

- Add count-state and handedness interaction controls at the pitch level.
- Estimate hierarchical models with pitcher and team random effects.
- Test whether movement quality changes the return to location quality by adding interaction terms.
- Validate findings out of sample on future Frontier League data.

## Robustness Output

Robustness checks are saved in `C:\Users\mattg\OneDrive\Desktop\pitcher regressions\paper_research\paper_1_movement_vs_location\data\robustness_results.csv`.