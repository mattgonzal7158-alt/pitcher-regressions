# Regression Dataset Summary

- Master input: `C:\Users\mattg\OneDrive\Desktop\pitcher regressions\data\processed\master_pitch_evaluation_table_v2.csv`
- Output dataset: `C:\Users\mattg\OneDrive\Desktop\pitcher regressions\paper_research\paper_1_movement_vs_location\data\regression_dataset.csv`
- Rows before filtering: 988
- Rows after filtering: 988
- Minimum pitch count: 25

## Outcome Column Mapping

| Canonical variable | Source column |
|---|---|
| `xwoba_frontier` | `pitch-level aggregate: xwoba_frontier` |
| `woba_value` | `pitch-level aggregate: woba_value` |
| `whiff_pct` | `pitch-level aggregate: whiff_pct` |
| `hardhit_pct` | `pitch-level aggregate: hardhit_pct` |

## Pitch Type Counts

| pitch_type | rows |
|---|---|
| Four-Seam | 386 |
| Slider | 187 |
| Sinker | 178 |
| Changeup | 118 |
| Curveball | 74 |
| Cutter | 36 |
| Splitter | 9 |

## Batter Side Counts

| batter_side | rows |
|---|---|
| R | 503 |
| L | 485 |

## Missing Value Table Before Filtering

| column | missing_rows |
|---|---|
| pitcher_name | 0 |
| pitcher_id | 1 |
| pitcher_team | 0 |
| pitch_type | 0 |
| batter_side | 0 |
| pitch_count | 0 |
| batted_ball_count | 0 |
| xwoba_frontier | 0 |
| woba_value | 0 |
| whiff_pct | 0 |
| hardhit_pct | 0 |
| movement_quality_20_80 | 0 |
| location_score_20_80 | 0 |

## Descriptive Statistics

| variable | count | mean | std | min | 25% | 50% | 75% | max |
|---|---|---|---|---|---|---|---|---|
| pitch_count | 988.0000 | 63.6174 | 37.0446 | 25.0000 | 38.0000 | 52.0000 | 79.0000 | 384.0000 |
| batted_ball_count | 988.0000 | 36.1518 | 23.9800 | 10.0000 | 19.0000 | 29.0000 | 45.0000 | 163.0000 |
| xwoba_frontier | 988.0000 | 0.2428 | 0.0590 | 0.0591 | 0.2049 | 0.2419 | 0.2814 | 0.4529 |
| woba_value | 988.0000 | 0.0933 | 0.0469 | 0.0000 | 0.0612 | 0.0891 | 0.1210 | 0.3029 |
| whiff_pct | 988.0000 | 0.2355 | 0.1292 | 0.0000 | 0.1364 | 0.2174 | 0.3182 | 0.6957 |
| hardhit_pct | 988.0000 | 0.1811 | 0.1163 | 0.0000 | 0.1000 | 0.1667 | 0.2500 | 0.6667 |
| movement_quality_20_80 | 988.0000 | 49.1423 | 17.3036 | 20.1056 | 34.1549 | 48.6796 | 64.0757 | 80.0000 |
| location_score_20_80 | 988.0000 | 49.6365 | 9.8722 | 20.0000 | 42.9358 | 48.8345 | 55.6801 | 80.0000 |

## Dependent-Specific Filters

- `xwoba_frontier` usable rows: 988
- `woba_value` usable rows: 988
- `whiff_pct` usable rows: 988
- `hardhit_pct` usable rows: 988