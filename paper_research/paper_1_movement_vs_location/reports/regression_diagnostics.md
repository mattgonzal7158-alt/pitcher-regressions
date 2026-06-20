# Regression Diagnostics

- Input dataset: `C:\Users\mattg\OneDrive\Desktop\pitcher regressions\paper_research\paper_1_movement_vs_location\data\regression_dataset.csv`
- Output CSV: `C:\Users\mattg\OneDrive\Desktop\pitcher regressions\paper_research\paper_1_movement_vs_location\data\diagnostic_tests.csv`
- Diagnostic plots: `C:\Users\mattg\OneDrive\Desktop\pitcher regressions\paper_research\paper_1_movement_vs_location\plots\diagnostics`

## Diagnostic Tests

| dependent | diagnostic | variable | value | p_value |
|---|---|---|---|---|
| xwoba_frontier | VIF | movement_quality_20_80 | 1.0873 |  |
| xwoba_frontier | VIF | location_score_20_80 | 1.0246 |  |
| xwoba_frontier | VIF | pitch_count | 3.3550 |  |
| xwoba_frontier | VIF | batted_ball_count | 3.5000 |  |
| xwoba_frontier | Breusch-Pagan LM |  | 53.5584 | 0.0000 |
| xwoba_frontier | White LM |  | 67.3076 | 0.0000 |
| xwoba_frontier | Jarque-Bera |  | 7.8333 | 0.0199 |
| xwoba_frontier | Shapiro-Wilk |  | 0.9965 | 0.0260 |
| xwoba_frontier | Durbin-Watson |  | 1.4789 |  |
| xwoba_frontier | Residual mean |  | -0.0000 |  |
| xwoba_frontier | Residual std |  | 0.0560 |  |
| woba_value | VIF | movement_quality_20_80 | 1.0873 |  |
| woba_value | VIF | location_score_20_80 | 1.0246 |  |
| woba_value | VIF | pitch_count | 3.3550 |  |
| woba_value | VIF | batted_ball_count | 3.5000 |  |
| woba_value | Breusch-Pagan LM |  | 59.5068 | 0.0000 |
| woba_value | White LM |  | 86.2894 | 0.0000 |
| woba_value | Jarque-Bera |  | 69.2939 | 0.0000 |
| woba_value | Shapiro-Wilk |  | 0.9832 | 0.0000 |
| woba_value | Durbin-Watson |  | 1.8021 |  |
| woba_value | Residual mean |  | -0.0000 |  |
| woba_value | Residual std |  | 0.0441 |  |
| whiff_pct | VIF | movement_quality_20_80 | 1.0873 |  |
| whiff_pct | VIF | location_score_20_80 | 1.0246 |  |
| whiff_pct | VIF | pitch_count | 3.3550 |  |
| whiff_pct | VIF | batted_ball_count | 3.5000 |  |
| whiff_pct | Breusch-Pagan LM |  | 40.7300 | 0.0000 |
| whiff_pct | White LM |  | 81.9972 | 0.0000 |
| whiff_pct | Jarque-Bera |  | 18.4055 | 0.0001 |
| whiff_pct | Shapiro-Wilk |  | 0.9930 | 0.0001 |
| whiff_pct | Durbin-Watson |  | 1.9351 |  |
| whiff_pct | Residual mean |  | -0.0000 |  |
| whiff_pct | Residual std |  | 0.1100 |  |
| hardhit_pct | VIF | movement_quality_20_80 | 1.0873 |  |
| hardhit_pct | VIF | location_score_20_80 | 1.0246 |  |
| hardhit_pct | VIF | pitch_count | 3.3550 |  |
| hardhit_pct | VIF | batted_ball_count | 3.5000 |  |
| hardhit_pct | Breusch-Pagan LM |  | 47.1678 | 0.0000 |
| hardhit_pct | White LM |  | 64.6721 | 0.0000 |
| hardhit_pct | Jarque-Bera |  | 114.6392 | 0.0000 |
| hardhit_pct | Shapiro-Wilk |  | 0.9728 | 0.0000 |
| hardhit_pct | Durbin-Watson |  | 1.6348 |  |
| hardhit_pct | Residual mean |  | -0.0000 |  |
| hardhit_pct | Residual std |  | 0.1125 |  |