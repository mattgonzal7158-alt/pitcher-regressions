# woba_value Validation Report

- Input file: `data\raw\2026-data.parquet`
- Output file: `data\processed\2026-data-with-woba.parquet`
- Rows saved: 131,151
- Columns saved: 243

## Event/Result Columns Identified

| Role | Actual Column Name | Why Used |
|---|---|---|
| Plate appearance / batted-ball result | `play_result` | Contains `Single`, `Double`, `Triple`, `Home Run`, and in-play zero-value results. |
| Walk / strikeout result | `kor_bb` | Contains `Walk` and `Strikeout`. |
| Pitch result | `pitch_call` | Contains `Hit By Pitch`. |
| Pitch type | `pitch_type` | Clean pitch-type column used for the pitch-type average. |

## Assumptions

- `play_result` is used for hit events because it contains the actual canonical hit result names.
- `kor_bb == Walk` is mapped to `BB`.
- `pitch_call == Hit By Pitch` is mapped to `HBP`.
- `kor_bb == Strikeout` plus `play_result` values `Out`, `Fielder's Choice`, `Sacrifice`, and `Caught Stealing` are treated as outs and assigned `0.0`.
- Rows that do not match a provided positive weight or the listed out labels are assigned `0.0` and counted as `OTHER_ZERO`; this includes non-terminal pitches and events outside the provided weights, such as `Error` or `Stolen Base`.
- If a row has overlapping labels, positive weighted outcomes are applied after zero-value out labels.

## Weights Applied

| Event | Weight |
|---|---:|
| `BB` | 0.701 |
| `HBP` | 0.732 |
| `1B` | 0.893 |
| `2B` | 1.265 |
| `3B` | 1.601 |
| `HR` | 2.056 |

## Derived Event Counts

| Event | Count |
|---|---:|
| `OTHER_ZERO` | 98,593 |
| `OUT` | 20,107 |
| `1B` | 5,310 |
| `BB` | 3,881 |
| `2B` | 1,417 |
| `HR` | 895 |
| `HBP` | 824 |
| `3B` | 124 |

## Raw Event Column Counts

### `play_result`

| Value | Count |
|---|---:|
| `<NA>` | 109,183 |
| `Out` | 12,564 |
| `Single` | 5,310 |
| `Double` | 1,417 |
| `Home Run` | 895 |
| `Fielder's Choice` | 636 |
| `Error` | 479 |
| `Sacrifice` | 441 |
| `Triple` | 124 |
| `Stolen Base` | 91 |
| `Caught Stealing` | 11 |

### `kor_bb`

| Value | Count |
|---|---:|
| `Undefined` | 120,814 |
| `Strikeout` | 6,456 |
| `Walk` | 3,881 |

### `pitch_call`

| Value | Count |
|---|---:|
| `Ball Called` | 48,650 |
| `Strike Called` | 22,151 |
| `In Play` | 21,870 |
| `Foul Ball Not Fieldable` | 19,867 |
| `Strike Swinging` | 13,343 |
| `<NA>` | 2,473 |
| `Ball In Dirt` | 1,102 |
| `Hit By Pitch` | 824 |
| `Foul Ball Fieldable` | 768 |
| `Intentional Ball` | 100 |
| `Automatic Strike` | 2 |
| `Automatic Ball` | 1 |

## woba_value Summary Statistics

| Statistic | Value |
|---|---:|
| `count` | 131151.000000 |
| `mean` | 0.090710 |
| `std` | 0.300877 |
| `min` | 0.000000 |
| `25%` | 0.000000 |
| `50%` | 0.000000 |
| `75%` | 0.000000 |
| `max` | 2.056000 |

## Average woba_value by Pitch Type

| Pitch Type | Count | Average woba_value | Sum woba_value |
|---|---:|---:|---:|
| `One Seam Fast Ball` | 2 | 0.350500 | 0.701000 |
| `Sinker` | 18,890 | 0.109191 | 2062.626000 |
| `<NA>` | 971 | 0.108138 | 105.002000 |
| `Fastball` | 24,345 | 0.101648 | 2474.622000 |
| `Four-Seam` | 22,214 | 0.097901 | 2174.783000 |
| `Cutter` | 5,275 | 0.091286 | 481.532000 |
| `Two-Seam` | 368 | 0.090565 | 33.328000 |
| `Other` | 98 | 0.089755 | 8.796000 |
| `Changeup` | 19,974 | 0.085361 | 1705.000000 |
| `Splitter` | 1,888 | 0.082551 | 155.857000 |
| `Slider` | 23,672 | 0.073885 | 1749.007000 |
| `Sweeper` | 381 | 0.072320 | 27.554000 |
| `Curveball` | 13,059 | 0.070222 | 917.027000 |
| `Knuckleball` | 14 | 0.063786 | 0.893000 |