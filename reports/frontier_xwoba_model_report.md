# Frontier League xwOBA Model Report

- Input file: `data\processed\2026-data-with-woba.parquet`
- Output file: `data\processed\2026-data-with-woba-xwoba.parquet`
- Rows in source dataframe: 199,368
- Batted balls modeled: 56,122
- Prediction column: `xwoba_frontier`
- Selected model: `linear_ev_la_la2_batted_type`

## Columns Identified

| Feature | Column Used | Note |
|---|---|---|
| Exit Velocity | `hit_launch_exit_speed_y` | Populated launch-tracking column; `_x` counterpart is empty in this file. |
| Launch Angle | `hit_launch_angle_y` | Populated launch-tracking column; `_x` counterpart is empty in this file. |
| Spray Angle | `hit_launch_direction_y` | Populated launch direction column. |
| Batted Ball Type | `hit_type` | Normalized tagged/auto hit type; missing values are modeled as `Unknown`. |
| Target | `woba_value` | Previously created Frontier League wOBA value. |

## Model Performance

| Model | Train R-squared | Train RMSE | Test R-squared | Test RMSE |
|---|---:|---:|---:|---:|
| `linear_ev_la_la2_batted_type` | 0.214830 | 0.421542 | 0.219150 | 0.430157 |
| `linear_ev_la_batted_type` | 0.211576 | 0.422415 | 0.215055 | 0.431284 |
| `linear_ev_la_spray_batted_type` | 0.211595 | 0.422409 | 0.215031 | 0.431290 |

## Why This Model Was Selected

`linear_ev_la_la2_batted_type` was selected because it had the lowest holdout RMSE (0.430157) and the highest/competitive holdout R-squared (0.219150) among the candidate models. RMSE was used as the primary criterion because the prediction task is to assign calibrated expected wOBA values to individual batted balls; lower prediction error is more directly useful than a slightly more complex specification with no error gain.

## Batted Ball Type Summary

| Batted Ball Type | Count | Average woba_value |
|---|---:|---:|
| `Line Drive` | 11,010 | 0.501728 |
| `Fly Ball` | 13,107 | 0.289062 |
| `Bunt` | 311 | 0.268235 |
| `Ground Ball` | 19,261 | 0.166591 |
| `Pop Up` | 5,042 | 0.031639 |
| `Unknown` | 7,391 | 0.000198 |

## Exploratory Plots

- `plots\frontier_xwoba\woba_by_exit_velocity.png`
- `plots\frontier_xwoba\woba_by_launch_angle.png`
- `plots\frontier_xwoba\woba_by_spray_angle.png`
- `plots\frontier_xwoba\woba_by_batted_ball_type.png`
- `plots\frontier_xwoba\woba_ev_launch_scatter.png`