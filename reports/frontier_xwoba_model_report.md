# Frontier League xwOBA Model Report

- Input file: `data\processed\2026-data-with-woba.parquet`
- Output file: `data\processed\2026-data-with-woba-xwoba.parquet`
- Rows in source dataframe: 92,670
- Batted balls modeled: 25,622
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
| `linear_ev_la_la2_batted_type` | 0.219275 | 0.424451 | 0.223731 | 0.434674 |
| `linear_ev_la_batted_type` | 0.216059 | 0.425324 | 0.220558 | 0.435561 |
| `linear_ev_la_spray_batted_type` | 0.216054 | 0.425325 | 0.220551 | 0.435563 |

## Why This Model Was Selected

`linear_ev_la_la2_batted_type` was selected because it had the lowest holdout RMSE (0.434674) and the highest/competitive holdout R-squared (0.223731) among the candidate models. RMSE was used as the primary criterion because the prediction task is to assign calibrated expected wOBA values to individual batted balls; lower prediction error is more directly useful than a slightly more complex specification with no error gain.

## Batted Ball Type Summary

| Batted Ball Type | Count | Average woba_value |
|---|---:|---:|
| `Line Drive` | 5,143 | 0.509976 |
| `Fly Ball` | 5,880 | 0.292780 |
| `Bunt` | 129 | 0.249209 |
| `Ground Ball` | 8,905 | 0.167130 |
| `Pop Up` | 2,228 | 0.024271 |
| `Unknown` | 3,337 | 0.000219 |

## Exploratory Plots

- `plots\frontier_xwoba\woba_by_exit_velocity.png`
- `plots\frontier_xwoba\woba_by_launch_angle.png`
- `plots\frontier_xwoba\woba_by_spray_angle.png`
- `plots\frontier_xwoba\woba_by_batted_ball_type.png`
- `plots\frontier_xwoba\woba_ev_launch_scatter.png`