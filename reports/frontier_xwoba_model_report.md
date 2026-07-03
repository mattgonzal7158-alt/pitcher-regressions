# Frontier League xwOBA Model Report

- Input file: `data\processed\2026-data-with-woba.parquet`
- Output file: `data\processed\2026-data-with-woba-xwoba.parquet`
- Rows in source dataframe: 131,151
- Batted balls modeled: 36,428
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
| `linear_ev_la_la2_batted_type` | 0.219948 | 0.425684 | 0.219858 | 0.428099 |
| `linear_ev_la_spray_batted_type` | 0.216678 | 0.426576 | 0.216163 | 0.429112 |
| `linear_ev_la_batted_type` | 0.216674 | 0.426577 | 0.216143 | 0.429117 |

## Why This Model Was Selected

`linear_ev_la_la2_batted_type` was selected because it had the lowest holdout RMSE (0.428099) and the highest/competitive holdout R-squared (0.219858) among the candidate models. RMSE was used as the primary criterion because the prediction task is to assign calibrated expected wOBA values to individual batted balls; lower prediction error is more directly useful than a slightly more complex specification with no error gain.

## Batted Ball Type Summary

| Batted Ball Type | Count | Average woba_value |
|---|---:|---:|
| `Line Drive` | 7,273 | 0.509645 |
| `Fly Ball` | 8,360 | 0.297280 |
| `Bunt` | 182 | 0.264956 |
| `Ground Ball` | 12,626 | 0.166675 |
| `Pop Up` | 3,258 | 0.028095 |
| `Unknown` | 4,729 | 0.000155 |

## Exploratory Plots

- `plots\frontier_xwoba\woba_by_exit_velocity.png`
- `plots\frontier_xwoba\woba_by_launch_angle.png`
- `plots\frontier_xwoba\woba_by_spray_angle.png`
- `plots\frontier_xwoba\woba_by_batted_ball_type.png`
- `plots\frontier_xwoba\woba_ev_launch_scatter.png`