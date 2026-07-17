# woba_value Validation Report

- Input file: `data\raw\2026-data.parquet`
- Output file: `data\processed\2026-data-with-woba.parquet`
- Rows saved: 155,981
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
| `OTHER_ZERO` | 117,113 |
| `OUT` | 24,064 |
| `1B` | 6,326 |
| `BB` | 4,611 |
| `2B` | 1,693 |
| `HR` | 1,049 |
| `HBP` | 981 |
| `3B` | 144 |

## Raw Event Column Counts

### `play_result`

| Value | Count |
|---|---:|
| `<NA>` | 129,622 |
| `Out` | 15,156 |
| `Single` | 6,326 |
| `Double` | 1,693 |
| `Home Run` | 1,049 |
| `Fielder's Choice` | 750 |
| `Error` | 561 |
| `Sacrifice` | 539 |
| `Triple` | 144 |
| `Stolen Base` | 126 |
| `Caught Stealing` | 15 |

### `kor_bb`

| Value | Count |
|---|---:|
| `Undefined` | 143,764 |
| `Strikeout` | 7,606 |
| `Walk` | 4,611 |

### `pitch_call`

| Value | Count |
|---|---:|
| `Ball Called` | 58,022 |
| `Strike Called` | 26,282 |
| `In Play` | 26,222 |
| `Foul Ball Not Fieldable` | 23,829 |
| `Strike Swinging` | 15,796 |
| `<NA>` | 2,501 |
| `Ball In Dirt` | 1,294 |
| `Hit By Pitch` | 981 |
| `Foul Ball Fieldable` | 928 |
| `Intentional Ball` | 123 |
| `Automatic Strike` | 2 |
| `Automatic Ball` | 1 |

## woba_value Summary Statistics

| Statistic | Value |
|---|---:|
| `count` | 155981.000000 |
| `mean` | 0.090578 |
| `std` | 0.300329 |
| `min` | 0.000000 |
| `25%` | 0.000000 |
| `50%` | 0.000000 |
| `75%` | 0.000000 |
| `max` | 2.056000 |

## Average woba_value by Pitch Type

| Pitch Type | Count | Average woba_value | Sum woba_value |
|---|---:|---:|---:|
| `One Seam Fast Ball` | 2 | 0.350500 | 0.701000 |
| `Sinker` | 22,343 | 0.107875 | 2410.250000 |
| `<NA>` | 1,118 | 0.104355 | 116.669000 |
| `Fastball` | 28,507 | 0.101029 | 2880.037000 |
| `Four-Seam` | 27,240 | 0.098610 | 2686.123000 |
| `Two-Seam` | 420 | 0.095093 | 39.939000 |
| `Cutter` | 6,120 | 0.090381 | 553.133000 |
| `Changeup` | 23,914 | 0.086180 | 2060.916000 |
| `Splitter` | 2,258 | 0.081915 | 184.963000 |
| `Other` | 119 | 0.079807 | 9.497000 |
| `Slider` | 28,093 | 0.073957 | 2077.683000 |
| `Sweeper` | 426 | 0.073561 | 31.337000 |
| `Curveball` | 15,406 | 0.069863 | 1076.313000 |
| `Knuckleball` | 15 | 0.059533 | 0.893000 |