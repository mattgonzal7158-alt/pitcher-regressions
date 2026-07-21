# Stuff+ Movement Model

- Input file: `data\processed\master_pitch_evaluation_table.csv`
- Output file: `data\processed\stuff_plus_scores.csv`
- Scored rows: 1,581
- Dependent variable: `final_pitch_score_20_80`
- Predictors: `IVB`, `HB`, `velocity`, `spin_rate`, `extension`, `release_height`, `release_side`
- Pitch-type-specific model minimum: 30 rows
- Low-sample pitch types use the fallback pooled model with pitch type fixed effects.

## Warnings

- None.

## Model Summaries

| Model | Type | Rows | R-squared | Intercept |
|---|---|---:|---:|---:|
| Changeup | pitch_type_specific | 196 | 0.0695 | 50.21 |
| Curveball | pitch_type_specific | 174 | 0.0260 | 49.45 |
| Cutter | pitch_type_specific | 71 | 0.2136 | 48.93 |
| Four-Seam | pitch_type_specific | 512 | 0.0277 | 49.06 |
| Sinker | pitch_type_specific | 270 | 0.1430 | 46.63 |
| Slider | pitch_type_specific | 330 | 0.0665 | 53.04 |
| Pooled | pooled_fixed_effects | 1,581 | 0.0908 | 51.34 |

## Variable Importance by Pitch Type

### Changeup

| Variable | Standardized Coefficient | Absolute Importance |
|---|---:|---:|
| `release_side` | 2.545 | 2.545 |
| `HB` | -1.763 | 1.763 |
| `velocity` | -1.542 | 1.542 |
| `extension` | 0.793 | 0.793 |
| `release_height` | -0.515 | 0.515 |
| `IVB` | 0.261 | 0.261 |
| `spin_rate` | -0.076 | 0.076 |

### Curveball

| Variable | Standardized Coefficient | Absolute Importance |
|---|---:|---:|
| `velocity` | 0.875 | 0.875 |
| `release_height` | 0.829 | 0.829 |
| `release_side` | -0.790 | 0.790 |
| `HB` | -0.789 | 0.789 |
| `extension` | -0.582 | 0.582 |
| `IVB` | 0.119 | 0.119 |
| `spin_rate` | 0.057 | 0.057 |

### Cutter

| Variable | Standardized Coefficient | Absolute Importance |
|---|---:|---:|
| `release_side` | -2.462 | 2.462 |
| `HB` | 1.488 | 1.488 |
| `extension` | 1.369 | 1.369 |
| `spin_rate` | 0.841 | 0.841 |
| `release_height` | 0.519 | 0.519 |
| `velocity` | 0.379 | 0.379 |
| `IVB` | 0.082 | 0.082 |

### Four-Seam

| Variable | Standardized Coefficient | Absolute Importance |
|---|---:|---:|
| `IVB` | 0.988 | 0.988 |
| `velocity` | 0.495 | 0.495 |
| `release_height` | -0.216 | 0.216 |
| `HB` | -0.095 | 0.095 |
| `release_side` | -0.080 | 0.080 |
| `spin_rate` | 0.064 | 0.064 |
| `extension` | -0.037 | 0.037 |

### Pooled

| Variable | Standardized Coefficient | Absolute Importance |
|---|---:|---:|
| `IVB` | 1.291 | 1.291 |
| `spin_rate` | 1.029 | 1.029 |
| `extension` | 0.503 | 0.503 |
| `HB` | -0.354 | 0.354 |
| `release_height` | -0.330 | 0.330 |
| `velocity` | -0.216 | 0.216 |
| `release_side` | 0.191 | 0.191 |

### Sinker

| Variable | Standardized Coefficient | Absolute Importance |
|---|---:|---:|
| `HB` | -2.443 | 2.443 |
| `spin_rate` | 1.794 | 1.794 |
| `release_side` | 1.394 | 1.394 |
| `release_height` | -1.196 | 1.196 |
| `IVB` | 0.839 | 0.839 |
| `extension` | 0.492 | 0.492 |
| `velocity` | -0.068 | 0.068 |

### Slider

| Variable | Standardized Coefficient | Absolute Importance |
|---|---:|---:|
| `extension` | 1.500 | 1.500 |
| `velocity` | -1.242 | 1.242 |
| `spin_rate` | 1.156 | 1.156 |
| `release_side` | 0.510 | 0.510 |
| `HB` | -0.498 | 0.498 |
| `IVB` | 0.413 | 0.413 |
| `release_height` | -0.407 | 0.407 |

## Top 25 Stuff+ Pitches

| Rank | Pitcher | Team | Pitch Type | Side | Stuff+ | Stuff % | Final | Velo | IVB | HB | Spin | Model |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | Harris, Everette | TRI_VAL | Slider | LHH | 80.0 | 100.0 | 58.0 | 80.5 | 1.2 | -8.7 | 2862 | pitch_type_specific |
| 2 | Vega, Lucas | TRO_AIG | Slider | RHH | 80.0 | 99.9 | 66.8 | 79.2 | 6.6 | -9.3 | 2697 | pitch_type_specific |
| 3 | Vega, Lucas | TRO_AIG | Slider | LHH | 80.0 | 99.9 | 57.3 | 79.2 | 6.6 | -9.3 | 2697 | pitch_type_specific |
| 4 | Harper, Scott | NEW_YOR13 | Slider | RHH | 80.0 | 99.8 | 72.1 | 79.8 | 3.3 | -16.7 | 2669 | pitch_type_specific |
| 5 | Harper, Scott | NEW_YOR13 | Slider | LHH | 80.0 | 99.8 | 66.8 | 79.8 | 3.3 | -16.7 | 2669 | pitch_type_specific |
| 6 | Plumadore, Carson | WIN_CIT29 | Slider | RHH | 79.2 | 99.7 | 61.5 | 76.0 | 2.6 | -4.8 | 2435 | pitch_type_specific |
| 7 | Plumadore, Carson | WIN_CIT29 | Slider | LHH | 79.2 | 99.7 | 56.0 | 76.0 | 2.6 | -4.8 | 2435 | pitch_type_specific |
| 8 | Saturria, Michael | NEW_ENG23 | Slider | RHH | 78.9 | 99.5 | 54.8 | 80.7 | 3.9 | -7.3 | 2705 | pitch_type_specific |
| 9 | Saturria, Michael | NEW_ENG23 | Slider | LHH | 78.9 | 99.5 | 53.7 | 80.7 | 3.9 | -7.3 | 2705 | pitch_type_specific |
| 10 | Petery, Dylan | WIN_CIT29 | Slider | RHH | 78.7 | 99.4 | 50.1 | 78.0 | -0.6 | -12.2 | 2611 | pitch_type_specific |
| 11 | Cerda, Junior | EVA_OTT | Sweeper | RHH | 77.7 | 99.4 | 57.4 | 81.2 | -3.2 | -11.9 | 2677 | pooled_fixed_effects |
| 12 | Conklin, MacCallan | TRO_AIG | Slider | RHH | 76.4 | 99.3 | 48.5 | 84.5 | 9.1 | 0.6 | 2512 | pitch_type_specific |
| 13 | Conklin, MacCallan | TRO_AIG | Slider | LHH | 76.4 | 99.3 | 46.1 | 84.5 | 9.1 | 0.6 | 2512 | pitch_type_specific |
| 14 | Voytko, Fawster | TRO_AIG | Slider | RHH | 75.9 | 99.2 | 41.6 | 78.6 | 0.9 | -11.4 | 2323 | pitch_type_specific |
| 15 | Morgan, Marcus | JOL_SLA | Slider | LHH | 75.6 | 99.1 | 50.4 | 84.9 | 7.0 | -9.2 | 2844 | pitch_type_specific |
| 16 | Morin, Jacob | QUE_CAP | Slider | RHH | 75.5 | 99.0 | 64.9 | 77.4 | 7.4 | -6.2 | 2495 | pitch_type_specific |
| 17 | Morin, Jacob | QUE_CAP | Slider | LHH | 75.5 | 99.0 | 58.3 | 77.4 | 7.4 | -6.2 | 2495 | pitch_type_specific |
| 18 | Good, Ty | GAT_GRI | Cutter | RHH | 75.4 | 98.9 | 56.9 | 88.4 | 17.0 | 7.6 | 2059 | pitch_type_specific |
| 19 | Godwin, Connor | NEW_YOR13 | Slider | RHH | 75.2 | 98.8 | 49.9 | 82.4 | 0.0 | -10.2 | 2535 | pitch_type_specific |
| 20 | Godwin, Connor | NEW_YOR13 | Slider | LHH | 75.2 | 98.8 | 41.5 | 82.4 | 0.0 | -10.2 | 2535 | pitch_type_specific |
| 21 | Duby, Bill | NEW_JER6 | Slider | RHH | 74.6 | 98.7 | 63.9 | 80.0 | 7.3 | -0.3 | 2066 | pitch_type_specific |
| 22 | Ronne, Andrew | GAT_GRI | Slider | RHH | 74.3 | 98.6 | 57.6 | 81.4 | 0.0 | -14.6 | 2593 | pitch_type_specific |
| 23 | Ronne, Andrew | GAT_GRI | Slider | LHH | 74.3 | 98.6 | 52.5 | 81.4 | 0.0 | -14.6 | 2593 | pitch_type_specific |
| 24 | Widener, Jacob | SUS_COU1 | Slider | RHH | 74.2 | 98.5 | 59.7 | 80.4 | 3.4 | 16.4 | 2855 | pitch_type_specific |
| 25 | Widener, Jacob | SUS_COU1 | Slider | LHH | 74.2 | 98.5 | 58.4 | 80.4 | 3.4 | 16.4 | 2855 | pitch_type_specific |

## Top 10 Stuff+ by Pitch Type

### Changeup

| Rank | Pitcher | Team | Pitch Type | Side | Stuff+ | Stuff % | Final | Velo | IVB | HB | Spin | Model |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 70 | Cooper, Garrett | NEW_YOR13 | Changeup | LHH | 67.5 | 95.6 | 51.7 | 77.8 | 9.2 | 8.0 | 1402 | pitch_type_specific |
| 71 | Cooper, Garrett | NEW_YOR13 | Changeup | RHH | 67.5 | 95.6 | 50.8 | 77.8 | 9.2 | 8.0 | 1402 | pitch_type_specific |
| 80 | Campbell, Tyler | MIS_MUD | Changeup | RHH | 67.0 | 95.0 | 60.3 | 74.6 | 11.6 | -7.9 | 1847 | pitch_type_specific |
| 81 | Campbell, Tyler | MIS_MUD | Changeup | LHH | 67.0 | 95.0 | 56.6 | 74.6 | 11.6 | -7.9 | 1847 | pitch_type_specific |
| 113 | Kines, Gunnar | JOL_SLA | Changeup | LHH | 65.6 | 92.9 | 49.3 | 75.4 | 12.1 | -12.5 | 1907 | pitch_type_specific |
| 114 | Kines, Gunnar | JOL_SLA | Changeup | RHH | 65.6 | 92.9 | 49.3 | 75.4 | 12.1 | -12.5 | 1907 | pitch_type_specific |
| 119 | Rohde, Isaac | NEW_YOR13 | Changeup | RHH | 64.9 | 92.5 | 57.5 | 76.3 | 4.0 | -20.4 | 1977 | pitch_type_specific |
| 120 | Rohde, Isaac | NEW_YOR13 | Changeup | LHH | 64.9 | 92.5 | 53.4 | 76.3 | 4.0 | -20.4 | 1977 | pitch_type_specific |
| 139 | Harris, Everette | TRI_VAL | Changeup | LHH | 63.9 | 91.2 | 63.7 | 82.6 | 2.1 | 16.6 | 2144 | pitch_type_specific |
| 140 | Harris, Everette | TRI_VAL | Changeup | RHH | 63.9 | 91.2 | 62.1 | 82.6 | 2.1 | 16.6 | 2144 | pitch_type_specific |

### Curveball

| Rank | Pitcher | Team | Pitch Type | Side | Stuff+ | Stuff % | Final | Velo | IVB | HB | Spin | Model |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 273 | Maryniak, Connor | NEW_JER6 | Curveball | RHH | 58.7 | 82.8 | 57.7 | 81.3 | -9.6 | -4.5 | 2514 | pitch_type_specific |
| 274 | Maryniak, Connor | NEW_JER6 | Curveball | LHH | 58.7 | 82.8 | 53.5 | 81.3 | -9.6 | -4.5 | 2514 | pitch_type_specific |
| 295 | Lovin, Xander | GAT_GRI | Curveball | RHH | 58.2 | 81.4 | 27.8 | 76.9 | -9.3 | -12.3 | 2634 | pitch_type_specific |
| 296 | Lovin, Xander | GAT_GRI | Curveball | LHH | 58.2 | 81.4 | 26.5 | 76.9 | -9.3 | -12.3 | 2634 | pitch_type_specific |
| 305 | Moore, Kyle | SCH_BOO | Curveball | RHH | 58.1 | 80.7 | 52.7 | 76.9 | -8.5 | -7.8 | 2531 | pitch_type_specific |
| 306 | Moore, Kyle | SCH_BOO | Curveball | LHH | 58.1 | 80.7 | 45.5 | 76.9 | -8.5 | -7.8 | 2531 | pitch_type_specific |
| 327 | Harris, Ben | GAT_GRI | Curveball | RHH | 57.3 | 79.3 | 60.5 | 77.6 | -14.1 | -7.0 | 2163 | pitch_type_specific |
| 328 | Harris, Ben | GAT_GRI | Curveball | LHH | 57.3 | 79.3 | 57.7 | 77.6 | -14.1 | -7.0 | 2163 | pitch_type_specific |
| 369 | Grounds, Jackson | DOW_EAS1 | Curveball | RHH | 56.2 | 76.7 | 73.3 | 81.4 | -10.5 | -12.0 | 1946 | pitch_type_specific |
| 370 | Grounds, Jackson | DOW_EAS1 | Curveball | LHH | 56.2 | 76.7 | 69.0 | 81.4 | -10.5 | -12.0 | 1946 | pitch_type_specific |

### Cutter

| Rank | Pitcher | Team | Pitch Type | Side | Stuff+ | Stuff % | Final | Velo | IVB | HB | Spin | Model |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 18 | Good, Ty | GAT_GRI | Cutter | RHH | 75.4 | 98.9 | 56.9 | 88.4 | 17.0 | 7.6 | 2059 | pitch_type_specific |
| 61 | Webster, Evan | FLO_Y'A | Cutter | LHH | 68.4 | 96.2 | 62.4 | 84.4 | 5.6 | -0.4 | 2039 | pitch_type_specific |
| 62 | Webster, Evan | FLO_Y'A | Cutter | RHH | 68.4 | 96.2 | 60.7 | 84.4 | 5.6 | -0.4 | 2039 | pitch_type_specific |
| 66 | Debban, Caleb | NEW_JER6 | Cutter | LHH | 68.1 | 95.9 | 51.9 | 85.9 | 10.7 | -0.4 | 2337 | pitch_type_specific |
| 67 | Debban, Caleb | NEW_JER6 | Cutter | RHH | 68.1 | 95.9 | 51.8 | 85.9 | 10.7 | -0.4 | 2337 | pitch_type_specific |
| 115 | Majick, Eli | NEW_ENG23 | Cutter | RHH | 65.4 | 92.8 | 61.0 | 82.8 | 5.8 | -1.1 | 2493 | pitch_type_specific |
| 116 | Majick, Eli | NEW_ENG23 | Cutter | LHH | 65.4 | 92.8 | 60.4 | 82.8 | 5.8 | -1.1 | 2493 | pitch_type_specific |
| 159 | Thiels, Brenton | MIS_MUD | Cutter | RHH | 63.2 | 90.0 | 42.3 | 86.3 | 9.4 | 4.5 | 2311 | pitch_type_specific |
| 189 | McEvoy, Aidan | FLO_Y'A | Cutter | LHH | 62.0 | 88.1 | 54.2 | 83.1 | 7.6 | 1.3 | 2151 | pitch_type_specific |
| 190 | McEvoy, Aidan | FLO_Y'A | Cutter | RHH | 62.0 | 88.1 | 51.5 | 83.1 | 7.6 | 1.3 | 2151 | pitch_type_specific |

### Four-Seam

| Rank | Pitcher | Team | Pitch Type | Side | Stuff+ | Stuff % | Final | Velo | IVB | HB | Spin | Model |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 334 | Rodriguez, Luis | TRO_AIG | Four-Seam | LHH | 57.1 | 78.9 | 50.9 | 95.1 | 20.6 | 7.0 | 2360 | pitch_type_specific |
| 335 | Rodriguez, Luis | TRO_AIG | Four-Seam | RHH | 57.1 | 78.9 | 49.3 | 95.1 | 20.6 | 7.0 | 2360 | pitch_type_specific |
| 383 | Perozzi, John | SUS_COU1 | Four-Seam | RHH | 55.7 | 75.8 | 51.1 | 91.5 | 21.6 | 9.0 | 2198 | pitch_type_specific |
| 384 | Perozzi, John | SUS_COU1 | Four-Seam | LHH | 55.7 | 75.8 | 47.4 | 91.5 | 21.6 | 9.0 | 2198 | pitch_type_specific |
| 398 | Floyd, Conner | QUE_CAP | Four-Seam | RHH | 55.5 | 74.9 | 49.5 | 92.7 | 20.5 | 10.5 | 2401 | pitch_type_specific |
| 399 | Floyd, Conner | QUE_CAP | Four-Seam | LHH | 55.5 | 74.9 | 48.0 | 92.7 | 20.5 | 10.5 | 2401 | pitch_type_specific |
| 413 | Barraza, Chris | MIS_MUD | Four-Seam | RHH | 55.0 | 73.9 | 53.5 | 93.2 | 19.9 | 10.3 | 2452 | pitch_type_specific |
| 414 | Barraza, Chris | MIS_MUD | Four-Seam | LHH | 55.0 | 73.9 | 52.4 | 93.2 | 19.9 | 10.3 | 2452 | pitch_type_specific |
| 424 | Johnson, Preston | MIS_MUD | Four-Seam | RHH | 54.5 | 73.2 | 57.4 | 92.2 | 20.3 | 6.9 | 2368 | pitch_type_specific |
| 425 | Johnson, Preston | MIS_MUD | Four-Seam | LHH | 54.5 | 73.2 | 51.0 | 92.2 | 20.3 | 6.9 | 2368 | pitch_type_specific |

### Sinker

| Rank | Pitcher | Team | Pitch Type | Side | Stuff+ | Stuff % | Final | Velo | IVB | HB | Spin | Model |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 182 | Riedel, Caleb | SCH_BOO | Sinker | LHH | 62.2 | 88.5 | 63.1 | 88.8 | 16.1 | -15.9 | 2309 | pitch_type_specific |
| 183 | Riedel, Caleb | SCH_BOO | Sinker | RHH | 62.2 | 88.5 | 62.9 | 88.8 | 16.1 | -15.9 | 2309 | pitch_type_specific |
| 239 | Widener, Jacob | SUS_COU1 | Sinker | LHH | 60.0 | 84.9 | 59.4 | 88.9 | 9.0 | -11.4 | 2364 | pitch_type_specific |
| 240 | Widener, Jacob | SUS_COU1 | Sinker | RHH | 60.0 | 84.9 | 56.3 | 88.9 | 9.0 | -11.4 | 2364 | pitch_type_specific |
| 285 | Plumadore, Carson | WIN_CIT29 | Sinker | RHH | 58.4 | 82.0 | 56.4 | 87.1 | 13.7 | 18.6 | 2378 | pitch_type_specific |
| 286 | Plumadore, Carson | WIN_CIT29 | Sinker | LHH | 58.4 | 82.0 | 55.2 | 87.1 | 13.7 | 18.6 | 2378 | pitch_type_specific |
| 349 | Kemlage, Joe | NEW_ENG23 | Sinker | LHH | 56.8 | 78.0 | 45.2 | 91.0 | 8.4 | -15.4 | 2429 | pitch_type_specific |
| 350 | Kemlage, Joe | NEW_ENG23 | Sinker | RHH | 56.8 | 78.0 | 45.1 | 91.0 | 8.4 | -15.4 | 2429 | pitch_type_specific |
| 376 | Morgan, Marcus | JOL_SLA | Sinker | LHH | 55.9 | 76.2 | 56.7 | 91.9 | 10.3 | 15.2 | 2455 | pitch_type_specific |
| 377 | Morgan, Marcus | JOL_SLA | Sinker | RHH | 55.9 | 76.2 | 54.8 | 91.9 | 10.3 | 15.2 | 2455 | pitch_type_specific |

### Slider

| Rank | Pitcher | Team | Pitch Type | Side | Stuff+ | Stuff % | Final | Velo | IVB | HB | Spin | Model |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | Harris, Everette | TRI_VAL | Slider | LHH | 80.0 | 100.0 | 58.0 | 80.5 | 1.2 | -8.7 | 2862 | pitch_type_specific |
| 2 | Vega, Lucas | TRO_AIG | Slider | RHH | 80.0 | 99.9 | 66.8 | 79.2 | 6.6 | -9.3 | 2697 | pitch_type_specific |
| 3 | Vega, Lucas | TRO_AIG | Slider | LHH | 80.0 | 99.9 | 57.3 | 79.2 | 6.6 | -9.3 | 2697 | pitch_type_specific |
| 4 | Harper, Scott | NEW_YOR13 | Slider | RHH | 80.0 | 99.8 | 72.1 | 79.8 | 3.3 | -16.7 | 2669 | pitch_type_specific |
| 5 | Harper, Scott | NEW_YOR13 | Slider | LHH | 80.0 | 99.8 | 66.8 | 79.8 | 3.3 | -16.7 | 2669 | pitch_type_specific |
| 6 | Plumadore, Carson | WIN_CIT29 | Slider | RHH | 79.2 | 99.7 | 61.5 | 76.0 | 2.6 | -4.8 | 2435 | pitch_type_specific |
| 7 | Plumadore, Carson | WIN_CIT29 | Slider | LHH | 79.2 | 99.7 | 56.0 | 76.0 | 2.6 | -4.8 | 2435 | pitch_type_specific |
| 8 | Saturria, Michael | NEW_ENG23 | Slider | RHH | 78.9 | 99.5 | 54.8 | 80.7 | 3.9 | -7.3 | 2705 | pitch_type_specific |
| 9 | Saturria, Michael | NEW_ENG23 | Slider | LHH | 78.9 | 99.5 | 53.7 | 80.7 | 3.9 | -7.3 | 2705 | pitch_type_specific |
| 10 | Petery, Dylan | WIN_CIT29 | Slider | RHH | 78.7 | 99.4 | 50.1 | 78.0 | -0.6 | -12.2 | 2611 | pitch_type_specific |

### Splitter

| Rank | Pitcher | Team | Pitch Type | Side | Stuff+ | Stuff % | Final | Velo | IVB | HB | Spin | Model |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 111 | Williams, Brian | MIS_MUD | Splitter | LHH | 65.8 | 93.0 | 54.1 | 78.6 | 2.5 | 5.0 | 1728 | pooled_fixed_effects |
| 112 | Williams, Brian | MIS_MUD | Splitter | RHH | 65.8 | 93.0 | 53.2 | 78.6 | 2.5 | 5.0 | 1728 | pooled_fixed_effects |
| 147 | Garcia, Hector | WAS_WIL3 | Splitter | LHH | 63.6 | 90.8 | 64.5 | 78.2 | 11.7 | 7.6 | 1216 | pooled_fixed_effects |
| 261 | Duby, Bill | NEW_JER6 | Splitter | LHH | 58.9 | 83.6 | 36.6 | 78.8 | 6.1 | 3.8 | 985 | pooled_fixed_effects |
| 300 | Gilleran, Jimmy | NEW_ENG23 | Splitter | LHH | 58.2 | 81.1 | 41.9 | 79.0 | -0.1 | 7.8 | 1500 | pooled_fixed_effects |
| 303 | Pindel, Buddie | SCH_BOO | Splitter | RHH | 58.1 | 80.9 | 58.8 | 80.3 | 5.0 | 7.1 | 1100 | pooled_fixed_effects |
| 304 | Pindel, Buddie | SCH_BOO | Splitter | LHH | 58.1 | 80.9 | 58.7 | 80.3 | 5.0 | 7.1 | 1100 | pooled_fixed_effects |
| 311 | Salata, Derek | SCH_BOO | Splitter | LHH | 57.9 | 80.4 | 51.9 | 83.2 | 7.1 | 9.2 | 1133 | pooled_fixed_effects |
| 332 | Villers, Ian | QUE_CAP | Splitter | RHH | 57.1 | 79.0 | 59.3 | 83.1 | 7.5 | 11.5 | 1086 | pooled_fixed_effects |
| 333 | Villers, Ian | QUE_CAP | Splitter | LHH | 57.1 | 79.0 | 58.3 | 83.1 | 7.5 | 11.5 | 1086 | pooled_fixed_effects |

### Sweeper

| Rank | Pitcher | Team | Pitch Type | Side | Stuff+ | Stuff % | Final | Velo | IVB | HB | Spin | Model |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 11 | Cerda, Junior | EVA_OTT | Sweeper | RHH | 77.7 | 99.4 | 57.4 | 81.2 | -3.2 | -11.9 | 2677 | pooled_fixed_effects |
