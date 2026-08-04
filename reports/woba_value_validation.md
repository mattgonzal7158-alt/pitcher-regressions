# woba_value Validation Report

- Input file: `data\raw\2026-data.parquet`
- Output file: `data\processed\2026-data-with-woba.parquet`
- Rows saved: 199,368
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
| `OTHER_ZERO` | 149,733 |
| `OUT` | 30,835 |
| `1B` | 8,112 |
| `BB` | 5,828 |
| `2B` | 2,137 |
| `HR` | 1,323 |
| `HBP` | 1,215 |
| `3B` | 185 |

## Raw Event Column Counts

### `play_result`

| Value | Count |
|---|---:|
| `<NA>` | 165,636 |
| `Out` | 19,413 |
| `Single` | 8,112 |
| `Double` | 2,137 |
| `Home Run` | 1,323 |
| `Fielder's Choice` | 973 |
| `Sacrifice` | 716 |
| `Error` | 687 |
| `Triple` | 185 |
| `Stolen Base` | 157 |
| `Caught Stealing` | 29 |

### `kor_bb`

| Value | Count |
|---|---:|
| `Undefined` | 183,833 |
| `Strikeout` | 9,707 |
| `Walk` | 5,828 |

### `pitch_call`

| Value | Count |
|---|---:|
| `Ball Called` | 73,693 |
| `In Play` | 33,550 |
| `Strike Called` | 33,410 |
| `Foul Ball Not Fieldable` | 30,668 |
| `Strike Swinging` | 20,132 |
| `<NA>` | 3,608 |
| `Ball In Dirt` | 1,733 |
| `Hit By Pitch` | 1,215 |
| `Foul Ball Fieldable` | 1,160 |
| `Intentional Ball` | 196 |
| `Automatic Strike` | 2 |
| `Automatic Ball` | 1 |

## woba_value Summary Statistics

| Statistic | Value |
|---|---:|
| `count` | 199368.000000 |
| `mean` | 0.089976 |
| `std` | 0.299273 |
| `min` | 0.000000 |
| `25%` | 0.000000 |
| `50%` | 0.000000 |
| `75%` | 0.000000 |
| `max` | 2.056000 |

## Average woba_value by Pitch Type

| Pitch Type | Count | Average woba_value | Sum woba_value |
|---|---:|---:|---:|
| `One Seam Fast Ball` | 2 | 0.350500 | 0.701000 |
| `Knuckleball` | 20 | 0.147450 | 2.949000 |
| `<NA>` | 1,461 | 0.106498 | 155.593000 |
| `Sinker` | 29,180 | 0.106407 | 3104.961000 |
| `Fastball` | 34,920 | 0.101928 | 3559.343000 |
| `Four-Seam` | 35,808 | 0.097216 | 3481.116000 |
| `Two-Seam` | 436 | 0.096319 | 41.995000 |
| `Cutter` | 8,104 | 0.087175 | 706.463000 |
| `Changeup` | 30,295 | 0.085955 | 2604.017000 |
| `Splitter` | 2,760 | 0.079549 | 219.555000 |
| `Slider` | 35,649 | 0.073625 | 2624.646000 |
| `Sweeper` | 628 | 0.072293 | 45.400000 |
| `Other` | 152 | 0.071704 | 10.899000 |
| `Curveball` | 19,953 | 0.069201 | 1380.764000 |