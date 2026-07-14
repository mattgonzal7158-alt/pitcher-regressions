# Stuff+ Movement Model

- Input file: `data\processed\master_pitch_evaluation_table.csv`
- Output file: `data\processed\stuff_plus_scores.csv`
- Scored rows: 1,527
- Dependent variable: `final_pitch_score_20_80`
- Predictors: `IVB`, `HB`, `velocity`, `spin_rate`, `extension`, `release_height`, `release_side`
- Pitch-type-specific model minimum: 30 rows
- Low-sample pitch types use the fallback pooled model with pitch type fixed effects.

## Warnings

- None.

## Model Summaries

| Model | Type | Rows | R-squared | Intercept |
|---|---|---:|---:|---:|
| Changeup | pitch_type_specific | 191 | 0.0710 | 50.31 |
| Curveball | pitch_type_specific | 162 | 0.0235 | 49.95 |
| Cutter | pitch_type_specific | 68 | 0.1873 | 48.76 |
| Four-Seam | pitch_type_specific | 498 | 0.0405 | 49.02 |
| Sinker | pitch_type_specific | 260 | 0.1217 | 46.73 |
| Slider | pitch_type_specific | 323 | 0.0620 | 52.92 |
| Pooled | pooled_fixed_effects | 1,527 | 0.0823 | 51.24 |

## Variable Importance by Pitch Type

### Changeup

| Variable | Standardized Coefficient | Absolute Importance |
|---|---:|---:|
| `release_side` | 2.904 | 2.904 |
| `HB` | -1.883 | 1.883 |
| `velocity` | -1.537 | 1.537 |
| `extension` | 0.703 | 0.703 |
| `release_height` | -0.503 | 0.503 |
| `IVB` | 0.247 | 0.247 |
| `spin_rate` | -0.107 | 0.107 |

### Curveball

| Variable | Standardized Coefficient | Absolute Importance |
|---|---:|---:|
| `release_side` | -1.004 | 1.004 |
| `velocity` | 0.851 | 0.851 |
| `HB` | -0.821 | 0.821 |
| `extension` | -0.629 | 0.629 |
| `release_height` | 0.482 | 0.482 |
| `IVB` | -0.476 | 0.476 |
| `spin_rate` | -0.329 | 0.329 |

### Cutter

| Variable | Standardized Coefficient | Absolute Importance |
|---|---:|---:|
| `release_side` | -2.253 | 2.253 |
| `HB` | 1.514 | 1.514 |
| `extension` | 1.412 | 1.412 |
| `velocity` | 1.020 | 1.020 |
| `release_height` | 0.665 | 0.665 |
| `IVB` | -0.495 | 0.495 |
| `spin_rate` | 0.340 | 0.340 |

### Four-Seam

| Variable | Standardized Coefficient | Absolute Importance |
|---|---:|---:|
| `IVB` | 1.138 | 1.138 |
| `HB` | -0.642 | 0.642 |
| `velocity` | 0.639 | 0.639 |
| `release_side` | 0.461 | 0.461 |
| `release_height` | -0.115 | 0.115 |
| `extension` | -0.043 | 0.043 |
| `spin_rate` | 0.039 | 0.039 |

### Pooled

| Variable | Standardized Coefficient | Absolute Importance |
|---|---:|---:|
| `IVB` | 1.316 | 1.316 |
| `spin_rate` | 0.847 | 0.847 |
| `extension` | 0.480 | 0.480 |
| `release_height` | -0.328 | 0.328 |
| `HB` | -0.220 | 0.220 |
| `release_side` | 0.195 | 0.195 |
| `velocity` | -0.171 | 0.171 |

### Sinker

| Variable | Standardized Coefficient | Absolute Importance |
|---|---:|---:|
| `HB` | -2.307 | 2.307 |
| `spin_rate` | 1.624 | 1.624 |
| `release_side` | 1.481 | 1.481 |
| `release_height` | -1.343 | 1.343 |
| `IVB` | 1.110 | 1.110 |
| `extension` | 0.299 | 0.299 |
| `velocity` | -0.089 | 0.089 |

### Slider

| Variable | Standardized Coefficient | Absolute Importance |
|---|---:|---:|
| `extension` | 1.514 | 1.514 |
| `velocity` | -1.196 | 1.196 |
| `spin_rate` | 0.890 | 0.890 |
| `release_height` | -0.611 | 0.611 |
| `HB` | -0.594 | 0.594 |
| `IVB` | 0.444 | 0.444 |
| `release_side` | 0.234 | 0.234 |

## Top 25 Stuff+ Pitches

| Rank | Pitcher | Team | Pitch Type | Side | Stuff+ | Stuff % | Final | Velo | IVB | HB | Spin | Model |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | Harris, Everette | TRI_VAL | Slider | LHH | 80.0 | 100.0 | 57.9 | 80.5 | 1.2 | -8.7 | 2862 | pitch_type_specific |
| 2 | Vega, Lucas | TRO_AIG | Slider | RHH | 80.0 | 99.9 | 67.1 | 79.2 | 6.6 | -9.3 | 2697 | pitch_type_specific |
| 3 | Vega, Lucas | TRO_AIG | Slider | LHH | 80.0 | 99.9 | 57.0 | 79.2 | 6.6 | -9.3 | 2697 | pitch_type_specific |
| 4 | Harper, Scott | NEW_YOR13 | Slider | RHH | 80.0 | 99.8 | 71.5 | 79.8 | 3.3 | -16.6 | 2665 | pitch_type_specific |
| 5 | Harper, Scott | NEW_YOR13 | Slider | LHH | 80.0 | 99.8 | 66.4 | 79.8 | 3.3 | -16.6 | 2665 | pitch_type_specific |
| 6 | Plumadore, Carson | WIN_CIT29 | Slider | RHH | 78.9 | 99.6 | 62.8 | 76.0 | 2.7 | -4.9 | 2439 | pitch_type_specific |
| 7 | Plumadore, Carson | WIN_CIT29 | Slider | LHH | 78.9 | 99.6 | 57.5 | 76.0 | 2.7 | -4.9 | 2439 | pitch_type_specific |
| 8 | Petery, Dylan | WIN_CIT29 | Slider | RHH | 77.4 | 99.5 | 49.8 | 78.1 | -0.6 | -12.0 | 2606 | pitch_type_specific |
| 9 | Saturria, Michael | NEW_ENG23 | Slider | RHH | 76.1 | 99.4 | 54.6 | 80.7 | 3.9 | -7.3 | 2706 | pitch_type_specific |
| 10 | Saturria, Michael | NEW_ENG23 | Slider | LHH | 76.1 | 99.4 | 53.6 | 80.7 | 3.9 | -7.3 | 2706 | pitch_type_specific |
| 11 | Conklin, MacCallan | TRO_AIG | Slider | RHH | 76.1 | 99.3 | 49.4 | 84.1 | 9.3 | 0.5 | 2526 | pitch_type_specific |
| 12 | Conklin, MacCallan | TRO_AIG | Slider | LHH | 76.1 | 99.3 | 47.9 | 84.1 | 9.3 | 0.5 | 2526 | pitch_type_specific |
| 13 | Campbell, Tyler | MIS_MUD | Slider | LHH | 76.1 | 99.2 | 54.1 | 74.3 | 8.1 | 3.9 | 2211 | pitch_type_specific |
| 14 | Campbell, Tyler | MIS_MUD | Slider | RHH | 76.1 | 99.2 | 48.8 | 74.3 | 8.1 | 3.9 | 2211 | pitch_type_specific |
| 15 | Duby, Bill | NEW_JER6 | Slider | RHH | 75.7 | 99.1 | 61.9 | 79.7 | 7.8 | 0.3 | 2041 | pitch_type_specific |
| 16 | Good, Ty | GAT_GRI | Cutter | RHH | 75.6 | 99.0 | 57.1 | 88.4 | 17.0 | 7.6 | 2059 | pitch_type_specific |
| 17 | Widener, Jacob | SUS_COU1 | Slider | RHH | 75.4 | 98.9 | 61.0 | 80.5 | 3.3 | 16.2 | 2854 | pitch_type_specific |
| 18 | Widener, Jacob | SUS_COU1 | Slider | LHH | 75.4 | 98.9 | 59.3 | 80.5 | 3.3 | 16.2 | 2854 | pitch_type_specific |
| 19 | Voytko, Fawster | TRO_AIG | Slider | RHH | 75.3 | 98.8 | 43.8 | 78.5 | 0.7 | -11.9 | 2334 | pitch_type_specific |
| 20 | Morin, Jacob | QUE_CAP | Slider | RHH | 75.3 | 98.7 | 65.3 | 77.4 | 7.4 | -6.2 | 2495 | pitch_type_specific |
| 21 | Morin, Jacob | QUE_CAP | Slider | LHH | 75.3 | 98.7 | 58.9 | 77.4 | 7.4 | -6.2 | 2495 | pitch_type_specific |
| 22 | Whitesell, Max | FLO_Y'A | Slider | RHH | 74.7 | 98.6 | 60.6 | 80.3 | 6.2 | -4.5 | 2081 | pitch_type_specific |
| 23 | Whitesell, Max | FLO_Y'A | Slider | LHH | 74.7 | 98.6 | 52.6 | 80.3 | 6.2 | -4.5 | 2081 | pitch_type_specific |
| 24 | Godwin, Connor | NEW_YOR13 | Slider | RHH | 74.2 | 98.5 | 50.5 | 82.4 | 0.0 | -10.2 | 2535 | pitch_type_specific |
| 25 | Godwin, Connor | NEW_YOR13 | Slider | LHH | 74.2 | 98.5 | 41.9 | 82.4 | 0.0 | -10.2 | 2535 | pitch_type_specific |

## Top 10 Stuff+ by Pitch Type

### Changeup

| Rank | Pitcher | Team | Pitch Type | Side | Stuff+ | Stuff % | Final | Velo | IVB | HB | Spin | Model |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 52 | Cooper, Garrett | NEW_YOR13 | Changeup | LHH | 68.5 | 96.6 | 54.8 | 77.7 | 8.7 | 8.0 | 1400 | pitch_type_specific |
| 53 | Cooper, Garrett | NEW_YOR13 | Changeup | RHH | 68.5 | 96.6 | 53.7 | 77.7 | 8.7 | 8.0 | 1400 | pitch_type_specific |
| 99 | Harris, Everette | TRI_VAL | Changeup | LHH | 65.2 | 93.5 | 63.8 | 82.6 | 2.1 | 16.6 | 2144 | pitch_type_specific |
| 100 | Harris, Everette | TRI_VAL | Changeup | RHH | 65.2 | 93.5 | 62.4 | 82.6 | 2.1 | 16.6 | 2144 | pitch_type_specific |
| 103 | Kines, Gunnar | JOL_SLA | Changeup | LHH | 65.1 | 93.3 | 48.7 | 75.4 | 12.2 | -12.5 | 1909 | pitch_type_specific |
| 104 | Kines, Gunnar | JOL_SLA | Changeup | RHH | 65.1 | 93.3 | 48.5 | 75.4 | 12.2 | -12.5 | 1909 | pitch_type_specific |
| 109 | Campbell, Tyler | MIS_MUD | Changeup | RHH | 64.7 | 92.9 | 58.8 | 74.8 | 11.9 | -7.9 | 1851 | pitch_type_specific |
| 110 | Campbell, Tyler | MIS_MUD | Changeup | LHH | 64.7 | 92.9 | 54.3 | 74.8 | 11.9 | -7.9 | 1851 | pitch_type_specific |
| 115 | Brothers, Kellen | SUS_COU1 | Changeup | RHH | 64.6 | 92.5 | 55.9 | 79.9 | 10.5 | 12.0 | 1497 | pitch_type_specific |
| 116 | Brothers, Kellen | SUS_COU1 | Changeup | LHH | 64.6 | 92.5 | 55.4 | 79.9 | 10.5 | 12.0 | 1497 | pitch_type_specific |

### Curveball

| Rank | Pitcher | Team | Pitch Type | Side | Stuff+ | Stuff % | Final | Velo | IVB | HB | Spin | Model |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 182 | Garcia, Brett | OTT_TIT | Curveball | RHH | 61.8 | 88.1 | 63.5 | 81.3 | -17.1 | -8.2 | 2144 | pitch_type_specific |
| 183 | Garcia, Brett | OTT_TIT | Curveball | LHH | 61.8 | 88.1 | 59.9 | 81.3 | -17.1 | -8.2 | 2144 | pitch_type_specific |
| 187 | Harris, Ben | GAT_GRI | Curveball | RHH | 61.5 | 87.8 | 59.0 | 77.9 | -14.1 | -7.2 | 2131 | pitch_type_specific |
| 188 | Harris, Ben | GAT_GRI | Curveball | LHH | 61.5 | 87.8 | 55.9 | 77.9 | -14.1 | -7.2 | 2131 | pitch_type_specific |
| 239 | Grounds, Jackson | DOW_EAS1 | Curveball | RHH | 59.8 | 84.4 | 73.3 | 81.4 | -10.5 | -12.0 | 1946 | pitch_type_specific |
| 240 | Grounds, Jackson | DOW_EAS1 | Curveball | LHH | 59.8 | 84.4 | 69.6 | 81.4 | -10.5 | -12.0 | 1946 | pitch_type_specific |
| 256 | Maryniak, Connor | NEW_JER6 | Curveball | RHH | 59.2 | 83.3 | 60.2 | 81.5 | -9.8 | -4.6 | 2515 | pitch_type_specific |
| 257 | Maryniak, Connor | NEW_JER6 | Curveball | LHH | 59.2 | 83.3 | 56.5 | 81.5 | -9.8 | -4.6 | 2515 | pitch_type_specific |
| 268 | Shinn, Nathan | LAK_ERI24 | Curveball | LHH | 58.9 | 82.5 | 45.7 | 79.6 | -5.9 | 0.6 | 2113 | pitch_type_specific |
| 269 | Shinn, Nathan | LAK_ERI24 | Curveball | RHH | 58.9 | 82.5 | 43.3 | 79.6 | -5.9 | 0.6 | 2113 | pitch_type_specific |

### Cutter

| Rank | Pitcher | Team | Pitch Type | Side | Stuff+ | Stuff % | Final | Velo | IVB | HB | Spin | Model |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 16 | Good, Ty | GAT_GRI | Cutter | RHH | 75.6 | 99.0 | 57.1 | 88.4 | 17.0 | 7.6 | 2059 | pitch_type_specific |
| 44 | Webster, Evan | FLO_Y'A | Cutter | LHH | 69.9 | 97.2 | 62.9 | 84.4 | 5.5 | -0.3 | 2041 | pitch_type_specific |
| 45 | Webster, Evan | FLO_Y'A | Cutter | RHH | 69.9 | 97.2 | 60.8 | 84.4 | 5.5 | -0.3 | 2041 | pitch_type_specific |
| 121 | Debban, Caleb | NEW_JER6 | Cutter | LHH | 64.5 | 92.1 | 52.3 | 85.9 | 10.7 | -0.4 | 2337 | pitch_type_specific |
| 122 | Debban, Caleb | NEW_JER6 | Cutter | RHH | 64.5 | 92.1 | 52.0 | 85.9 | 10.7 | -0.4 | 2337 | pitch_type_specific |
| 126 | Thiels, Brenton | MIS_MUD | Cutter | RHH | 64.1 | 91.8 | 42.1 | 86.3 | 9.4 | 4.5 | 2311 | pitch_type_specific |
| 237 | Majick, Eli | NEW_ENG23 | Cutter | RHH | 59.9 | 84.5 | 59.7 | 82.8 | 5.6 | -0.9 | 2500 | pitch_type_specific |
| 238 | Majick, Eli | NEW_ENG23 | Cutter | LHH | 59.9 | 84.5 | 59.6 | 82.8 | 5.6 | -0.9 | 2500 | pitch_type_specific |
| 272 | McEvoy, Aidan | FLO_Y'A | Cutter | LHH | 58.8 | 82.2 | 54.0 | 83.0 | 7.6 | 1.4 | 2151 | pitch_type_specific |
| 273 | McEvoy, Aidan | FLO_Y'A | Cutter | RHH | 58.8 | 82.2 | 51.2 | 83.0 | 7.6 | 1.4 | 2151 | pitch_type_specific |

### Four-Seam

| Rank | Pitcher | Team | Pitch Type | Side | Stuff+ | Stuff % | Final | Velo | IVB | HB | Spin | Model |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 232 | Rodriguez, Luis | TRO_AIG | Four-Seam | LHH | 60.1 | 84.8 | 51.1 | 95.1 | 20.6 | 7.0 | 2360 | pitch_type_specific |
| 233 | Rodriguez, Luis | TRO_AIG | Four-Seam | RHH | 60.1 | 84.8 | 49.8 | 95.1 | 20.6 | 7.0 | 2360 | pitch_type_specific |
| 310 | Floyd, Conner | QUE_CAP | Four-Seam | RHH | 57.9 | 79.7 | 48.8 | 92.6 | 20.7 | 10.7 | 2394 | pitch_type_specific |
| 311 | Floyd, Conner | QUE_CAP | Four-Seam | LHH | 57.9 | 79.7 | 46.9 | 92.6 | 20.7 | 10.7 | 2394 | pitch_type_specific |
| 349 | Johnson, Preston | MIS_MUD | Four-Seam | RHH | 57.0 | 77.2 | 57.5 | 92.2 | 20.3 | 6.9 | 2368 | pitch_type_specific |
| 350 | Johnson, Preston | MIS_MUD | Four-Seam | LHH | 57.0 | 77.2 | 51.1 | 92.2 | 20.3 | 6.9 | 2368 | pitch_type_specific |
| 359 | Barraza, Chris | MIS_MUD | Four-Seam | RHH | 56.7 | 76.5 | 53.4 | 93.2 | 19.9 | 10.3 | 2453 | pitch_type_specific |
| 360 | Barraza, Chris | MIS_MUD | Four-Seam | LHH | 56.7 | 76.5 | 52.3 | 93.2 | 19.9 | 10.3 | 2453 | pitch_type_specific |
| 374 | MacMillan, Blake | TRO_AIG | Four-Seam | RHH | 56.2 | 75.5 | 56.0 | 88.3 | 21.9 | -5.8 | 2200 | pitch_type_specific |
| 375 | MacMillan, Blake | TRO_AIG | Four-Seam | LHH | 56.2 | 75.5 | 53.4 | 88.3 | 21.9 | -5.8 | 2200 | pitch_type_specific |

### Sinker

| Rank | Pitcher | Team | Pitch Type | Side | Stuff+ | Stuff % | Final | Velo | IVB | HB | Spin | Model |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 166 | Riedel, Caleb | SCH_BOO | Sinker | RHH | 62.1 | 89.2 | 63.6 | 88.8 | 16.3 | -15.9 | 2308 | pitch_type_specific |
| 167 | Riedel, Caleb | SCH_BOO | Sinker | LHH | 62.1 | 89.2 | 63.0 | 88.8 | 16.3 | -15.9 | 2308 | pitch_type_specific |
| 225 | Plumadore, Carson | WIN_CIT29 | Sinker | RHH | 60.4 | 85.3 | 53.7 | 87.3 | 13.7 | 18.5 | 2384 | pitch_type_specific |
| 226 | Plumadore, Carson | WIN_CIT29 | Sinker | LHH | 60.4 | 85.3 | 52.6 | 87.3 | 13.7 | 18.5 | 2384 | pitch_type_specific |
| 347 | Balzan, Jackson | SUS_COU1 | Sinker | LHH | 57.0 | 77.3 | 49.1 | 86.1 | 17.3 | -14.6 | 2224 | pitch_type_specific |
| 348 | Balzan, Jackson | SUS_COU1 | Sinker | RHH | 57.0 | 77.3 | 48.8 | 86.1 | 17.3 | -14.6 | 2224 | pitch_type_specific |
| 353 | Widener, Jacob | SUS_COU1 | Sinker | LHH | 56.8 | 76.9 | 59.3 | 88.9 | 9.0 | -11.4 | 2364 | pitch_type_specific |
| 354 | Widener, Jacob | SUS_COU1 | Sinker | RHH | 56.8 | 76.9 | 56.3 | 88.9 | 9.0 | -11.4 | 2364 | pitch_type_specific |
| 423 | Morgan, Marcus | JOL_SLA | Sinker | LHH | 54.9 | 72.3 | 57.0 | 91.9 | 10.3 | 15.2 | 2455 | pitch_type_specific |
| 424 | Morgan, Marcus | JOL_SLA | Sinker | RHH | 54.9 | 72.3 | 54.9 | 91.9 | 10.3 | 15.2 | 2455 | pitch_type_specific |

### Slider

| Rank | Pitcher | Team | Pitch Type | Side | Stuff+ | Stuff % | Final | Velo | IVB | HB | Spin | Model |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | Harris, Everette | TRI_VAL | Slider | LHH | 80.0 | 100.0 | 57.9 | 80.5 | 1.2 | -8.7 | 2862 | pitch_type_specific |
| 2 | Vega, Lucas | TRO_AIG | Slider | RHH | 80.0 | 99.9 | 67.1 | 79.2 | 6.6 | -9.3 | 2697 | pitch_type_specific |
| 3 | Vega, Lucas | TRO_AIG | Slider | LHH | 80.0 | 99.9 | 57.0 | 79.2 | 6.6 | -9.3 | 2697 | pitch_type_specific |
| 4 | Harper, Scott | NEW_YOR13 | Slider | RHH | 80.0 | 99.8 | 71.5 | 79.8 | 3.3 | -16.6 | 2665 | pitch_type_specific |
| 5 | Harper, Scott | NEW_YOR13 | Slider | LHH | 80.0 | 99.8 | 66.4 | 79.8 | 3.3 | -16.6 | 2665 | pitch_type_specific |
| 6 | Plumadore, Carson | WIN_CIT29 | Slider | RHH | 78.9 | 99.6 | 62.8 | 76.0 | 2.7 | -4.9 | 2439 | pitch_type_specific |
| 7 | Plumadore, Carson | WIN_CIT29 | Slider | LHH | 78.9 | 99.6 | 57.5 | 76.0 | 2.7 | -4.9 | 2439 | pitch_type_specific |
| 8 | Petery, Dylan | WIN_CIT29 | Slider | RHH | 77.4 | 99.5 | 49.8 | 78.1 | -0.6 | -12.0 | 2606 | pitch_type_specific |
| 9 | Saturria, Michael | NEW_ENG23 | Slider | RHH | 76.1 | 99.4 | 54.6 | 80.7 | 3.9 | -7.3 | 2706 | pitch_type_specific |
| 10 | Saturria, Michael | NEW_ENG23 | Slider | LHH | 76.1 | 99.4 | 53.6 | 80.7 | 3.9 | -7.3 | 2706 | pitch_type_specific |

### Splitter

| Rank | Pitcher | Team | Pitch Type | Side | Stuff+ | Stuff % | Final | Velo | IVB | HB | Spin | Model |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 123 | Williams, Brian | MIS_MUD | Splitter | LHH | 64.4 | 92.0 | 54.4 | 78.6 | 2.5 | 5.0 | 1728 | pooled_fixed_effects |
| 124 | Williams, Brian | MIS_MUD | Splitter | RHH | 64.4 | 92.0 | 53.7 | 78.6 | 2.5 | 5.0 | 1728 | pooled_fixed_effects |
| 135 | Garcia, Hector | WAS_WIL3 | Splitter | LHH | 63.7 | 91.2 | 64.7 | 78.2 | 11.7 | 7.6 | 1216 | pooled_fixed_effects |
| 248 | Duby, Bill | NEW_JER6 | Splitter | LHH | 59.6 | 83.8 | 36.9 | 78.8 | 6.7 | 4.1 | 985 | pooled_fixed_effects |
| 289 | Pindel, Buddie | SCH_BOO | Splitter | RHH | 58.3 | 81.1 | 59.0 | 80.3 | 4.9 | 7.2 | 1105 | pooled_fixed_effects |
| 290 | Pindel, Buddie | SCH_BOO | Splitter | LHH | 58.3 | 81.1 | 59.0 | 80.3 | 4.9 | 7.2 | 1105 | pooled_fixed_effects |
| 293 | Salata, Derek | SCH_BOO | Splitter | LHH | 58.3 | 80.9 | 52.1 | 83.2 | 7.1 | 9.2 | 1133 | pooled_fixed_effects |
| 317 | Villers, Ian | QUE_CAP | Splitter | RHH | 57.7 | 79.3 | 59.5 | 83.1 | 7.5 | 11.5 | 1086 | pooled_fixed_effects |
| 318 | Villers, Ian | QUE_CAP | Splitter | LHH | 57.7 | 79.3 | 58.5 | 83.1 | 7.5 | 11.5 | 1086 | pooled_fixed_effects |
| 331 | Eldred, Zach | NEW_ENG23 | Splitter | LHH | 57.4 | 78.4 | 40.2 | 84.2 | 5.0 | 4.2 | 968 | pooled_fixed_effects |
