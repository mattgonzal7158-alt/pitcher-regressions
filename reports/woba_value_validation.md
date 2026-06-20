# woba_value Validation Report

- Input file: `2026-data.parquet`
- Output file: `2026-data-with-woba.parquet`
- Rows saved: 92,670
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
| `OTHER_ZERO` | 69,746 |
| `OUT` | 14,181 |
| `1B` | 3,689 |
| `BB` | 2,737 |
| `2B` | 1,009 |
| `HR` | 636 |
| `HBP` | 588 |
| `3B` | 84 |

## Raw Event Column Counts

### `play_result`

| Value | Count |
|---|---:|
| `<NA>` | 77,243 |
| `Out` | 8,833 |
| `Single` | 3,689 |
| `Double` | 1,009 |
| `Home Run` | 636 |
| `Fielder's Choice` | 446 |
| `Error` | 366 |
| `Sacrifice` | 285 |
| `Triple` | 84 |
| `Stolen Base` | 70 |
| `Caught Stealing` | 9 |

### `kor_bb`

| Value | Count |
|---|---:|
| `Undefined` | 85,325 |
| `Strikeout` | 4,608 |
| `Walk` | 2,737 |

### `pitch_call`

| Value | Count |
|---|---:|
| `Ball Called` | 34,491 |
| `Strike Called` | 15,669 |
| `In Play` | 15,352 |
| `Foul Ball Not Fieldable` | 13,960 |
| `Strike Swinging` | 9,503 |
| `<NA>` | 1,622 |
| `Ball In Dirt` | 760 |
| `Foul Ball Fieldable` | 652 |
| `Hit By Pitch` | 588 |
| `Intentional Ball` | 70 |
| `Automatic Strike` | 2 |
| `Automatic Ball` | 1 |

## woba_value Summary Statistics

| Statistic | Value |
|---|---:|
| `count` | 92670.000000 |
| `mean` | 0.090232 |
| `std` | 0.300458 |
| `min` | 0.000000 |
| `25%` | 0.000000 |
| `50%` | 0.000000 |
| `75%` | 0.000000 |
| `max` | 2.056000 |

## Average woba_value by Pitch Type

| Pitch Type | Count | Average woba_value | Sum woba_value |
|---|---:|---:|---:|
| `One Seam Fast Ball` | 1 | 0.701000 | 0.701000 |
| `Sinker` | 13,190 | 0.109075 | 1438.697000 |
| `<NA>` | 775 | 0.103206 | 79.985000 |
| `Fastball` | 16,163 | 0.099399 | 1606.581000 |
| `Four-Seam` | 16,555 | 0.098329 | 1627.832000 |
| `Other` | 74 | 0.097324 | 7.202000 |
| `Two-Seam` | 339 | 0.094086 | 31.895000 |
| `Sweeper` | 246 | 0.092443 | 22.741000 |
| `Cutter` | 3,719 | 0.091150 | 338.988000 |
| `Changeup` | 14,577 | 0.085947 | 1252.856000 |
| `Splitter` | 1,331 | 0.080601 | 107.280000 |
| `Curveball` | 9,343 | 0.071876 | 671.534000 |
| `Slider` | 16,343 | 0.071874 | 1174.630000 |
| `Knuckleball` | 14 | 0.063786 | 0.893000 |