# Frontier League xwOBA Model Report

- Input file: `data\processed\2026-data-with-woba.parquet`
- Output file: `data\processed\2026-data-with-woba-xwoba.parquet`
- Rows in source dataframe: 155,981
- Batted balls modeled: 43,662
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
| `linear_ev_la_la2_batted_type` | 0.220024 | 0.423824 | 0.217793 | 0.425916 |
| `linear_ev_la_spray_batted_type` | 0.216559 | 0.424765 | 0.214836 | 0.426721 |
| `linear_ev_la_batted_type` | 0.216555 | 0.424766 | 0.214825 | 0.426724 |

## Why This Model Was Selected

`linear_ev_la_la2_batted_type` was selected because it had the lowest holdout RMSE (0.425916) and the highest/competitive holdout R-squared (0.217793) among the candidate models. RMSE was used as the primary criterion because the prediction task is to assign calibrated expected wOBA values to individual batted balls; lower prediction error is more directly useful than a slightly more complex specification with no error gain.

## Batted Ball Type Summary

| Batted Ball Type | Count | Average woba_value |
|---|---:|---:|
| `Line Drive` | 8,673 | 0.509840 |
| `Fly Ball` | 10,100 | 0.290415 |
| `Bunt` | 229 | 0.249572 |
| `Ground Ball` | 15,097 | 0.165290 |
| `Pop Up` | 3,861 | 0.029316 |
| `Unknown` | 5,702 | 0.000128 |

## Exploratory Plots

- `plots\frontier_xwoba\woba_by_exit_velocity.png`
- `plots\frontier_xwoba\woba_by_launch_angle.png`
- `plots\frontier_xwoba\woba_by_spray_angle.png`
- `plots\frontier_xwoba\woba_by_batted_ball_type.png`
- `plots\frontier_xwoba\woba_ev_launch_scatter.png`