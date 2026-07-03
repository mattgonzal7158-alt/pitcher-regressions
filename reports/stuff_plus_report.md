# Stuff+ Movement Model

- Input file: `data\processed\master_pitch_evaluation_table.csv`
- Output file: `data\processed\stuff_plus_scores.csv`
- Scored rows: 1,323
- Dependent variable: `final_pitch_score_20_80`
- Predictors: `IVB`, `HB`, `velocity`, `spin_rate`, `extension`, `release_height`, `release_side`
- Pitch-type-specific model minimum: 30 rows
- Low-sample pitch types use the fallback pooled model with pitch type fixed effects.

## Warnings

- None.

## Model Summaries

| Model | Type | Rows | R-squared | Intercept |
|---|---|---:|---:|---:|
| Changeup | pitch_type_specific | 169 | 0.0856 | 50.45 |
| Curveball | pitch_type_specific | 127 | 0.0346 | 49.88 |
| Cutter | pitch_type_specific | 55 | 0.0943 | 49.26 |
| Four-Seam | pitch_type_specific | 456 | 0.0572 | 48.62 |
| Sinker | pitch_type_specific | 226 | 0.1684 | 46.92 |
| Slider | pitch_type_specific | 269 | 0.0922 | 53.30 |
| Pooled | pooled_fixed_effects | 1,323 | 0.1014 | 51.42 |

## Variable Importance by Pitch Type

### Changeup

| Variable | Standardized Coefficient | Absolute Importance |
|---|---:|---:|
| `release_side` | 2.238 | 2.238 |
| `velocity` | -1.656 | 1.656 |
| `HB` | -1.013 | 1.013 |
| `extension` | 0.865 | 0.865 |
| `release_height` | -0.540 | 0.540 |
| `spin_rate` | -0.167 | 0.167 |
| `IVB` | 0.125 | 0.125 |

### Curveball

| Variable | Standardized Coefficient | Absolute Importance |
|---|---:|---:|
| `HB` | -1.602 | 1.602 |
| `release_side` | -0.846 | 0.846 |
| `spin_rate` | 0.643 | 0.643 |
| `extension` | -0.631 | 0.631 |
| `velocity` | 0.601 | 0.601 |
| `IVB` | -0.148 | 0.148 |
| `release_height` | -0.126 | 0.126 |

### Cutter

| Variable | Standardized Coefficient | Absolute Importance |
|---|---:|---:|
| `release_side` | -1.631 | 1.631 |
| `HB` | 0.964 | 0.964 |
| `IVB` | -0.962 | 0.962 |
| `velocity` | 0.821 | 0.821 |
| `release_height` | 0.739 | 0.739 |
| `extension` | 0.596 | 0.596 |
| `spin_rate` | 0.145 | 0.145 |

### Four-Seam

| Variable | Standardized Coefficient | Absolute Importance |
|---|---:|---:|
| `IVB` | 1.454 | 1.454 |
| `HB` | -0.810 | 0.810 |
| `release_side` | 0.756 | 0.756 |
| `velocity` | 0.585 | 0.585 |
| `extension` | -0.155 | 0.155 |
| `release_height` | -0.129 | 0.129 |
| `spin_rate` | -0.024 | 0.024 |

### Pooled

| Variable | Standardized Coefficient | Absolute Importance |
|---|---:|---:|
| `IVB` | 1.715 | 1.715 |
| `spin_rate` | 1.026 | 1.026 |
| `velocity` | -0.624 | 0.624 |
| `release_height` | -0.479 | 0.479 |
| `HB` | -0.404 | 0.404 |
| `release_side` | 0.389 | 0.389 |
| `extension` | 0.352 | 0.352 |

### Sinker

| Variable | Standardized Coefficient | Absolute Importance |
|---|---:|---:|
| `HB` | -2.439 | 2.439 |
| `spin_rate` | 1.784 | 1.784 |
| `release_height` | -1.625 | 1.625 |
| `IVB` | 1.382 | 1.382 |
| `release_side` | 1.029 | 1.029 |
| `velocity` | 0.154 | 0.154 |
| `extension` | 0.135 | 0.135 |

### Slider

| Variable | Standardized Coefficient | Absolute Importance |
|---|---:|---:|
| `velocity` | -2.020 | 2.020 |
| `extension` | 1.746 | 1.746 |
| `spin_rate` | 1.103 | 1.103 |
| `HB` | -0.628 | 0.628 |
| `release_height` | -0.587 | 0.587 |
| `release_side` | 0.368 | 0.368 |
| `IVB` | 0.261 | 0.261 |

## Top 25 Stuff+ Pitches

| Rank | Pitcher | Team | Pitch Type | Side | Stuff+ | Stuff % | Final | Velo | IVB | HB | Spin | Model |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | Harris, Everette | TRI_VAL | Slider | LHH | 80.0 | 100.0 | 57.7 | 80.5 | 1.2 | -8.7 | 2862 | pitch_type_specific |
| 2 | Vega, Lucas | TRO_AIG | Slider | RHH | 80.0 | 99.9 | 66.4 | 79.0 | 6.5 | -10.3 | 2707 | pitch_type_specific |
| 3 | Vega, Lucas | TRO_AIG | Slider | LHH | 80.0 | 99.9 | 55.6 | 79.0 | 6.5 | -10.3 | 2707 | pitch_type_specific |
| 4 | Plumadore, Carson | WIN_CIT29 | Slider | RHH | 80.0 | 99.7 | 58.9 | 75.9 | 2.7 | -5.3 | 2445 | pitch_type_specific |
| 5 | Plumadore, Carson | WIN_CIT29 | Slider | LHH | 80.0 | 99.7 | 54.7 | 75.9 | 2.7 | -5.3 | 2445 | pitch_type_specific |
| 6 | Harper, Scott | NEW_YOR13 | Slider | RHH | 80.0 | 99.6 | 74.0 | 79.8 | 3.5 | -16.7 | 2675 | pitch_type_specific |
| 7 | Harper, Scott | NEW_YOR13 | Slider | LHH | 80.0 | 99.6 | 69.0 | 79.8 | 3.5 | -16.7 | 2675 | pitch_type_specific |
| 8 | Campbell, Tyler | MIS_MUD | Slider | LHH | 79.2 | 99.4 | 53.4 | 74.5 | 8.6 | 3.8 | 2220 | pitch_type_specific |
| 9 | Campbell, Tyler | MIS_MUD | Slider | RHH | 79.2 | 99.4 | 47.4 | 74.5 | 8.6 | 3.8 | 2220 | pitch_type_specific |
| 10 | Saturria, Michael | NEW_ENG23 | Slider | RHH | 77.2 | 99.3 | 55.2 | 80.4 | 3.9 | -7.5 | 2712 | pitch_type_specific |
| 11 | Saturria, Michael | NEW_ENG23 | Slider | LHH | 77.2 | 99.3 | 53.4 | 80.4 | 3.9 | -7.5 | 2712 | pitch_type_specific |
| 12 | Morin, Jacob | QUE_CAP | Slider | RHH | 76.9 | 99.1 | 65.1 | 77.4 | 7.4 | -6.2 | 2495 | pitch_type_specific |
| 13 | Morin, Jacob | QUE_CAP | Slider | LHH | 76.9 | 99.1 | 58.4 | 77.4 | 7.4 | -6.2 | 2495 | pitch_type_specific |
| 14 | Duby, Bill | NEW_JER6 | Slider | RHH | 76.8 | 99.0 | 62.6 | 79.6 | 7.7 | 0.3 | 2053 | pitch_type_specific |
| 15 | Gregory, Ben | GAT_GRI | Slider | RHH | 75.7 | 98.9 | 62.8 | 79.6 | 1.3 | -4.9 | 2362 | pitch_type_specific |
| 16 | Smith, Jackson | MIS_MUD | Slider | RHH | 75.4 | 98.8 | 63.4 | 77.9 | 1.7 | -10.3 | 2663 | pitch_type_specific |
| 17 | Smith, Jackson | MIS_MUD | Slider | LHH | 75.4 | 98.8 | 59.9 | 77.9 | 1.7 | -10.3 | 2663 | pitch_type_specific |
| 18 | Widener, Jacob | SUS_COU1 | Slider | RHH | 75.3 | 98.7 | 59.7 | 80.6 | 3.3 | 16.1 | 2857 | pitch_type_specific |
| 19 | Widener, Jacob | SUS_COU1 | Slider | LHH | 75.3 | 98.7 | 58.5 | 80.6 | 3.3 | 16.1 | 2857 | pitch_type_specific |
| 20 | Whitesell, Max | FLO_Y'A | Slider | RHH | 74.5 | 98.5 | 59.3 | 80.2 | 6.3 | -4.3 | 2085 | pitch_type_specific |
| 21 | Whitesell, Max | FLO_Y'A | Slider | LHH | 74.5 | 98.5 | 51.7 | 80.2 | 6.3 | -4.3 | 2085 | pitch_type_specific |
| 22 | Sechrist, Zander | WAS_WIL3 | Slider | LHH | 74.5 | 98.4 | 63.7 | 68.3 | 1.3 | 9.7 | 1831 | pitch_type_specific |
| 23 | Sechrist, Zander | WAS_WIL3 | Slider | RHH | 74.5 | 98.4 | 58.9 | 68.3 | 1.3 | 9.7 | 1831 | pitch_type_specific |
| 24 | Garcia, Hector | WAS_WIL3 | Slider | RHH | 74.0 | 98.3 | 63.7 | 77.3 | 2.0 | -7.1 | 2355 | pitch_type_specific |
| 25 | Godwin, Connor | NEW_YOR13 | Slider | RHH | 74.0 | 98.1 | 50.7 | 82.4 | 0.0 | -10.2 | 2535 | pitch_type_specific |

## Top 10 Stuff+ by Pitch Type

### Changeup

| Rank | Pitcher | Team | Pitch Type | Side | Stuff+ | Stuff % | Final | Velo | IVB | HB | Spin | Model |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 53 | Cooper, Garrett | NEW_YOR13 | Changeup | LHH | 68.6 | 96.0 | 61.9 | 77.5 | 8.4 | 7.4 | 1395 | pitch_type_specific |
| 54 | Cooper, Garrett | NEW_YOR13 | Changeup | RHH | 68.6 | 96.0 | 59.1 | 77.5 | 8.4 | 7.4 | 1395 | pitch_type_specific |
| 90 | Daly, Ryan | JOL_SLA | Changeup | LHH | 65.6 | 93.2 | 55.1 | 78.9 | 5.2 | 16.1 | 2080 | pitch_type_specific |
| 91 | Daly, Ryan | JOL_SLA | Changeup | RHH | 65.6 | 93.2 | 49.7 | 78.9 | 5.2 | 16.1 | 2080 | pitch_type_specific |
| 99 | Campbell, Tyler | MIS_MUD | Changeup | RHH | 64.9 | 92.6 | 58.0 | 74.9 | 11.9 | -8.2 | 1872 | pitch_type_specific |
| 109 | Harris, Everette | TRI_VAL | Changeup | LHH | 64.3 | 91.8 | 63.8 | 82.6 | 2.1 | 16.6 | 2144 | pitch_type_specific |
| 110 | Harris, Everette | TRI_VAL | Changeup | RHH | 64.3 | 91.8 | 62.5 | 82.6 | 2.1 | 16.6 | 2144 | pitch_type_specific |
| 130 | Westcott, Zac | FLO_Y'A | Changeup | LHH | 63.3 | 90.2 | 45.4 | 76.5 | 6.5 | 16.7 | 1915 | pitch_type_specific |
| 131 | Westcott, Zac | FLO_Y'A | Changeup | RHH | 63.3 | 90.2 | 41.2 | 76.5 | 6.5 | 16.7 | 1915 | pitch_type_specific |
| 132 | Rohde, Isaac | NEW_YOR13 | Changeup | RHH | 63.3 | 90.1 | 57.7 | 76.1 | 4.2 | -20.4 | 1971 | pitch_type_specific |

### Curveball

| Rank | Pitcher | Team | Pitch Type | Side | Stuff+ | Stuff % | Final | Velo | IVB | HB | Spin | Model |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 184 | Petschke, Ben | EVA_OTT | Curveball | RHH | 61.6 | 86.1 | 53.5 | 77.2 | -9.7 | -15.7 | 2771 | pitch_type_specific |
| 185 | Petschke, Ben | EVA_OTT | Curveball | LHH | 61.6 | 86.1 | 52.3 | 77.2 | -9.7 | -15.7 | 2771 | pitch_type_specific |
| 188 | Lovin, Xander | GAT_GRI | Curveball | LHH | 61.4 | 85.9 | 32.0 | 77.0 | -9.6 | -12.6 | 2634 | pitch_type_specific |
| 198 | Bice, Emmett | NEW_YOR13 | Curveball | RHH | 60.8 | 85.1 | 45.8 | 79.0 | -10.3 | -13.4 | 2985 | pitch_type_specific |
| 199 | Bice, Emmett | NEW_YOR13 | Curveball | LHH | 60.8 | 85.1 | 42.3 | 79.0 | -10.3 | -13.4 | 2985 | pitch_type_specific |
| 247 | Moore, Kyle | SCH_BOO | Curveball | RHH | 58.8 | 81.4 | 53.2 | 76.8 | -8.8 | -8.3 | 2536 | pitch_type_specific |
| 248 | Moore, Kyle | SCH_BOO | Curveball | LHH | 58.8 | 81.4 | 47.8 | 76.8 | -8.8 | -8.3 | 2536 | pitch_type_specific |
| 251 | Simpson, Garret | EVA_OTT | Curveball | RHH | 58.7 | 81.1 | 63.1 | 76.8 | -12.2 | -13.3 | 2693 | pitch_type_specific |
| 252 | Simpson, Garret | EVA_OTT | Curveball | LHH | 58.7 | 81.1 | 55.9 | 76.8 | -12.2 | -13.3 | 2693 | pitch_type_specific |
| 290 | Cameron, Wyatt | SCH_BOO | Curveball | RHH | 57.0 | 78.1 | 35.0 | 81.1 | -13.5 | -9.7 | 2296 | pitch_type_specific |

### Cutter

| Rank | Pitcher | Team | Pitch Type | Side | Stuff+ | Stuff % | Final | Velo | IVB | HB | Spin | Model |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 186 | Webster, Evan | FLO_Y'A | Cutter | LHH | 61.5 | 86.0 | 64.8 | 84.2 | 5.8 | -0.1 | 2054 | pitch_type_specific |
| 187 | Webster, Evan | FLO_Y'A | Cutter | RHH | 61.5 | 86.0 | 62.2 | 84.2 | 5.8 | -0.1 | 2054 | pitch_type_specific |
| 282 | Majick, Eli | NEW_ENG23 | Cutter | RHH | 57.3 | 78.7 | 57.1 | 82.8 | 5.5 | -0.9 | 2502 | pitch_type_specific |
| 283 | Majick, Eli | NEW_ENG23 | Cutter | LHH | 57.3 | 78.7 | 55.9 | 82.8 | 5.5 | -0.9 | 2502 | pitch_type_specific |
| 296 | Thiels, Brenton | MIS_MUD | Cutter | RHH | 56.6 | 77.7 | 42.4 | 86.3 | 9.4 | 4.5 | 2311 | pitch_type_specific |
| 311 | Bell, Brendan | NEW_ENG23 | Cutter | RHH | 56.3 | 76.5 | 57.1 | 92.2 | 9.3 | -0.4 | 2391 | pitch_type_specific |
| 312 | Bell, Brendan | NEW_ENG23 | Cutter | LHH | 56.3 | 76.5 | 54.9 | 92.2 | 9.3 | -0.4 | 2391 | pitch_type_specific |
| 337 | Debban, Caleb | NEW_JER6 | Cutter | LHH | 55.6 | 74.6 | 52.5 | 86.0 | 10.6 | -0.3 | 2337 | pitch_type_specific |
| 338 | Debban, Caleb | NEW_JER6 | Cutter | RHH | 55.6 | 74.6 | 52.0 | 86.0 | 10.6 | -0.3 | 2337 | pitch_type_specific |
| 397 | Morgan, Cooper | QUE_CAP | Cutter | RHH | 53.8 | 70.0 | 43.2 | 86.1 | 8.7 | -2.8 | 2122 | pitch_type_specific |

### Four-Seam

| Rank | Pitcher | Team | Pitch Type | Side | Stuff+ | Stuff % | Final | Velo | IVB | HB | Spin | Model |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 234 | Rodriguez, Luis | TRO_AIG | Four-Seam | LHH | 59.1 | 82.4 | 51.3 | 95.2 | 20.6 | 6.8 | 2356 | pitch_type_specific |
| 235 | Rodriguez, Luis | TRO_AIG | Four-Seam | RHH | 59.1 | 82.4 | 50.1 | 95.2 | 20.6 | 6.8 | 2356 | pitch_type_specific |
| 269 | Floyd, Conner | QUE_CAP | Four-Seam | RHH | 57.9 | 79.7 | 48.2 | 92.5 | 20.7 | 10.8 | 2389 | pitch_type_specific |
| 270 | Floyd, Conner | QUE_CAP | Four-Seam | LHH | 57.9 | 79.7 | 46.6 | 92.5 | 20.7 | 10.8 | 2389 | pitch_type_specific |
| 301 | MacMillan, Blake | TRO_AIG | Four-Seam | RHH | 56.4 | 77.3 | 59.2 | 88.3 | 21.7 | -6.0 | 2199 | pitch_type_specific |
| 302 | MacMillan, Blake | TRO_AIG | Four-Seam | LHH | 56.4 | 77.3 | 54.2 | 88.3 | 21.7 | -6.0 | 2199 | pitch_type_specific |
| 307 | Johnson, Preston | MIS_MUD | Four-Seam | RHH | 56.4 | 76.8 | 57.4 | 92.2 | 20.3 | 6.9 | 2368 | pitch_type_specific |
| 308 | Johnson, Preston | MIS_MUD | Four-Seam | LHH | 56.4 | 76.8 | 51.2 | 92.2 | 20.3 | 6.9 | 2368 | pitch_type_specific |
| 323 | Barraza, Chris | MIS_MUD | Four-Seam | RHH | 56.0 | 75.6 | 52.3 | 93.2 | 20.0 | 10.3 | 2450 | pitch_type_specific |
| 324 | Barraza, Chris | MIS_MUD | Four-Seam | LHH | 56.0 | 75.6 | 50.4 | 93.2 | 20.0 | 10.3 | 2450 | pitch_type_specific |

### Sinker

| Rank | Pitcher | Team | Pitch Type | Side | Stuff+ | Stuff % | Final | Velo | IVB | HB | Spin | Model |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 79 | Riedel, Caleb | SCH_BOO | Sinker | LHH | 66.4 | 94.1 | 58.7 | 88.7 | 16.2 | -16.1 | 2330 | pitch_type_specific |
| 80 | Riedel, Caleb | SCH_BOO | Sinker | RHH | 66.4 | 94.1 | 58.1 | 88.7 | 16.2 | -16.1 | 2330 | pitch_type_specific |
| 173 | Widener, Jacob | SUS_COU1 | Sinker | LHH | 62.1 | 87.0 | 57.1 | 89.0 | 9.2 | -11.7 | 2376 | pitch_type_specific |
| 174 | Widener, Jacob | SUS_COU1 | Sinker | RHH | 62.1 | 87.0 | 55.8 | 89.0 | 9.2 | -11.7 | 2376 | pitch_type_specific |
| 213 | Balzan, Jackson | SUS_COU1 | Sinker | LHH | 60.0 | 83.9 | 49.8 | 86.1 | 17.4 | -14.5 | 2218 | pitch_type_specific |
| 214 | Balzan, Jackson | SUS_COU1 | Sinker | RHH | 60.0 | 83.9 | 48.9 | 86.1 | 17.4 | -14.5 | 2218 | pitch_type_specific |
| 229 | Plumadore, Carson | WIN_CIT29 | Sinker | RHH | 59.3 | 82.7 | 55.2 | 87.1 | 13.6 | 18.6 | 2383 | pitch_type_specific |
| 230 | Plumadore, Carson | WIN_CIT29 | Sinker | LHH | 59.3 | 82.7 | 53.9 | 87.1 | 13.6 | 18.6 | 2383 | pitch_type_specific |
| 240 | Kemlage, Joe | NEW_ENG23 | Sinker | LHH | 58.9 | 81.9 | 44.8 | 90.8 | 8.7 | -15.5 | 2430 | pitch_type_specific |
| 241 | Kemlage, Joe | NEW_ENG23 | Sinker | RHH | 58.9 | 81.9 | 44.2 | 90.8 | 8.7 | -15.5 | 2430 | pitch_type_specific |

### Slider

| Rank | Pitcher | Team | Pitch Type | Side | Stuff+ | Stuff % | Final | Velo | IVB | HB | Spin | Model |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | Harris, Everette | TRI_VAL | Slider | LHH | 80.0 | 100.0 | 57.7 | 80.5 | 1.2 | -8.7 | 2862 | pitch_type_specific |
| 2 | Vega, Lucas | TRO_AIG | Slider | RHH | 80.0 | 99.9 | 66.4 | 79.0 | 6.5 | -10.3 | 2707 | pitch_type_specific |
| 3 | Vega, Lucas | TRO_AIG | Slider | LHH | 80.0 | 99.9 | 55.6 | 79.0 | 6.5 | -10.3 | 2707 | pitch_type_specific |
| 4 | Plumadore, Carson | WIN_CIT29 | Slider | RHH | 80.0 | 99.7 | 58.9 | 75.9 | 2.7 | -5.3 | 2445 | pitch_type_specific |
| 5 | Plumadore, Carson | WIN_CIT29 | Slider | LHH | 80.0 | 99.7 | 54.7 | 75.9 | 2.7 | -5.3 | 2445 | pitch_type_specific |
| 6 | Harper, Scott | NEW_YOR13 | Slider | RHH | 80.0 | 99.6 | 74.0 | 79.8 | 3.5 | -16.7 | 2675 | pitch_type_specific |
| 7 | Harper, Scott | NEW_YOR13 | Slider | LHH | 80.0 | 99.6 | 69.0 | 79.8 | 3.5 | -16.7 | 2675 | pitch_type_specific |
| 8 | Campbell, Tyler | MIS_MUD | Slider | LHH | 79.2 | 99.4 | 53.4 | 74.5 | 8.6 | 3.8 | 2220 | pitch_type_specific |
| 9 | Campbell, Tyler | MIS_MUD | Slider | RHH | 79.2 | 99.4 | 47.4 | 74.5 | 8.6 | 3.8 | 2220 | pitch_type_specific |
| 10 | Saturria, Michael | NEW_ENG23 | Slider | RHH | 77.2 | 99.3 | 55.2 | 80.4 | 3.9 | -7.5 | 2712 | pitch_type_specific |

### Splitter

| Rank | Pitcher | Team | Pitch Type | Side | Stuff+ | Stuff % | Final | Velo | IVB | HB | Spin | Model |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 35 | Garcia, Hector | WAS_WIL3 | Splitter | LHH | 70.7 | 97.4 | 64.4 | 78.2 | 11.7 | 7.6 | 1216 | pooled_fixed_effects |
| 40 | Williams, Brian | MIS_MUD | Splitter | LHH | 70.5 | 97.0 | 52.9 | 78.8 | 2.3 | 5.3 | 1674 | pooled_fixed_effects |
| 41 | Williams, Brian | MIS_MUD | Splitter | RHH | 70.5 | 97.0 | 52.4 | 78.8 | 2.3 | 5.3 | 1674 | pooled_fixed_effects |
| 72 | Duby, Bill | NEW_JER6 | Splitter | LHH | 66.6 | 94.6 | 34.9 | 78.8 | 7.0 | 4.0 | 997 | pooled_fixed_effects |
| 102 | Pindel, Buddie | SCH_BOO | Splitter | RHH | 64.6 | 92.3 | 58.4 | 80.3 | 4.7 | 7.3 | 1101 | pooled_fixed_effects |
| 103 | Pindel, Buddie | SCH_BOO | Splitter | LHH | 64.6 | 92.3 | 58.4 | 80.3 | 4.7 | 7.3 | 1101 | pooled_fixed_effects |
| 115 | Thompson, Ross | SCH_BOO | Splitter | LHH | 64.2 | 91.3 | 55.6 | 79.4 | 4.1 | 9.4 | 1052 | pooled_fixed_effects |
| 116 | Thompson, Ross | SCH_BOO | Splitter | RHH | 64.2 | 91.3 | 53.4 | 79.4 | 4.1 | 9.4 | 1052 | pooled_fixed_effects |
| 125 | Salata, Derek | SCH_BOO | Splitter | LHH | 63.5 | 90.6 | 51.1 | 83.2 | 7.2 | 9.3 | 1137 | pooled_fixed_effects |
| 163 | Villers, Ian | QUE_CAP | Splitter | RHH | 62.2 | 87.7 | 59.2 | 83.1 | 7.5 | 11.5 | 1086 | pooled_fixed_effects |
