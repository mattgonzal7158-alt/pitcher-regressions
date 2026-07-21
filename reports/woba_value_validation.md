# woba_value Validation Report

- Input file: `data\raw\2026-data.parquet`
- Output file: `data\processed\2026-data-with-woba.parquet`
- Rows saved: 165,724
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
| `OTHER_ZERO` | 124,584 |
| `OUT` | 25,491 |
| `1B` | 6,708 |
| `BB` | 4,867 |
| `2B` | 1,779 |
| `HR` | 1,102 |
| `HBP` | 1,036 |
| `3B` | 157 |

## Raw Event Column Counts

### `play_result`

| Value | Count |
|---|---:|
| `<NA>` | 137,815 |
| `Out` | 16,051 |
| `Single` | 6,708 |
| `Double` | 1,779 |
| `Home Run` | 1,102 |
| `Fielder's Choice` | 798 |
| `Error` | 593 |
| `Sacrifice` | 580 |
| `Triple` | 157 |
| `Stolen Base` | 126 |
| `Caught Stealing` | 15 |

### `kor_bb`

| Value | Count |
|---|---:|
| `Undefined` | 152,808 |
| `Strikeout` | 8,049 |
| `Walk` | 4,867 |

### `pitch_call`

| Value | Count |
|---|---:|
| `Ball Called` | 61,413 |
| `Strike Called` | 27,776 |
| `In Play` | 27,772 |
| `Foul Ball Not Fieldable` | 25,362 |
| `Strike Swinging` | 16,743 |
| `<NA>` | 3,146 |
| `Ball In Dirt` | 1,395 |
| `Hit By Pitch` | 1,036 |
| `Foul Ball Fieldable` | 951 |
| `Intentional Ball` | 127 |
| `Automatic Strike` | 2 |
| `Automatic Ball` | 1 |

## woba_value Summary Statistics

| Statistic | Value |
|---|---:|
| `count` | 165724.000000 |
| `mean` | 0.090077 |
| `std` | 0.299435 |
| `min` | 0.000000 |
| `25%` | 0.000000 |
| `50%` | 0.000000 |
| `75%` | 0.000000 |
| `max` | 2.056000 |

## Average woba_value by Pitch Type

| Pitch Type | Count | Average woba_value | Sum woba_value |
|---|---:|---:|---:|
| `One Seam Fast Ball` | 2 | 0.350500 | 0.701000 |
| `Knuckleball` | 16 | 0.184312 | 2.949000 |
| `Sinker` | 23,972 | 0.107266 | 2571.391000 |
| `<NA>` | 1,194 | 0.105047 | 125.426000 |
| `Fastball` | 29,620 | 0.101390 | 3003.167000 |
| `Four-Seam` | 29,328 | 0.097612 | 2862.775000 |
| `Two-Seam` | 421 | 0.094867 | 39.939000 |
| `Cutter` | 6,630 | 0.088509 | 586.817000 |
| `Changeup` | 25,396 | 0.085595 | 2173.766000 |
| `Splitter` | 2,326 | 0.082530 | 191.965000 |
| `Other` | 121 | 0.078488 | 9.497000 |
| `Sweeper` | 475 | 0.077861 | 36.984000 |
| `Slider` | 29,678 | 0.073340 | 2176.597000 |
| `Curveball` | 16,545 | 0.069259 | 1145.893000 |