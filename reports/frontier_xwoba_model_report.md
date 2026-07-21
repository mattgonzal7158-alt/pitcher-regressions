# Frontier League xwOBA Model Report

- Input file: `data\processed\2026-data-with-woba.parquet`
- Output file: `data\processed\2026-data-with-woba-xwoba.parquet`
- Rows in source dataframe: 165,724
- Batted balls modeled: 46,396
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
| `linear_ev_la_la2_batted_type` | 0.219392 | 0.422276 | 0.213267 | 0.428062 |
| `linear_ev_la_spray_batted_type` | 0.216219 | 0.423133 | 0.209640 | 0.429048 |
| `linear_ev_la_batted_type` | 0.216221 | 0.423133 | 0.209602 | 0.429058 |

## Why This Model Was Selected

`linear_ev_la_la2_batted_type` was selected because it had the lowest holdout RMSE (0.428062) and the highest/competitive holdout R-squared (0.213267) among the candidate models. RMSE was used as the primary criterion because the prediction task is to assign calibrated expected wOBA values to individual batted balls; lower prediction error is more directly useful than a slightly more complex specification with no error gain.

## Batted Ball Type Summary

| Batted Ball Type | Count | Average woba_value |
|---|---:|---:|
| `Line Drive` | 9,202 | 0.507253 |
| `Fly Ball` | 10,725 | 0.288062 |
| `Bunt` | 246 | 0.246846 |
| `Ground Ball` | 16,034 | 0.165444 |
| `Pop Up` | 4,113 | 0.028388 |
| `Unknown` | 6,076 | 0.000120 |

## Exploratory Plots

- `plots\frontier_xwoba\woba_by_exit_velocity.png`
- `plots\frontier_xwoba\woba_by_launch_angle.png`
- `plots\frontier_xwoba\woba_by_spray_angle.png`
- `plots\frontier_xwoba\woba_by_batted_ball_type.png`
- `plots\frontier_xwoba\woba_ev_launch_scatter.png`