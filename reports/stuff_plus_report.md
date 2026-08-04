# Stuff+ Movement Model

- Input file: `data\processed\master_pitch_evaluation_table.csv`
- Output file: `data\processed\stuff_plus_scores.csv`
- Scored rows: 1,783
- Dependent variable: `final_pitch_score_20_80`
- Predictors: `IVB`, `HB`, `velocity`, `spin_rate`, `extension`, `release_height`, `release_side`
- Pitch-type-specific model minimum: 30 rows
- Low-sample pitch types use the fallback pooled model with pitch type fixed effects.

## Warnings

- None.

## Model Summaries

| Model | Type | Rows | R-squared | Intercept |
|---|---|---:|---:|---:|
| Changeup | pitch_type_specific | 229 | 0.0988 | 50.03 |
| Curveball | pitch_type_specific | 207 | 0.0572 | 49.27 |
| Cutter | pitch_type_specific | 80 | 0.1635 | 49.90 |
| Four-Seam | pitch_type_specific | 558 | 0.0375 | 48.95 |
| Sinker | pitch_type_specific | 302 | 0.1012 | 46.46 |
| Slider | pitch_type_specific | 377 | 0.0367 | 53.45 |
| Pooled | pooled_fixed_effects | 1,783 | 0.1076 | 51.56 |

## Variable Importance by Pitch Type

### Changeup

| Variable | Standardized Coefficient | Absolute Importance |
|---|---:|---:|
| `velocity` | -1.869 | 1.869 |
| `release_side` | 1.483 | 1.483 |
| `HB` | -0.572 | 0.572 |
| `extension` | 0.525 | 0.525 |
| `spin_rate` | 0.440 | 0.440 |
| `IVB` | 0.360 | 0.360 |
| `release_height` | 0.319 | 0.319 |

### Curveball

| Variable | Standardized Coefficient | Absolute Importance |
|---|---:|---:|
| `release_height` | 1.150 | 1.150 |
| `extension` | -1.015 | 1.015 |
| `spin_rate` | 0.987 | 0.987 |
| `IVB` | 0.835 | 0.835 |
| `velocity` | 0.446 | 0.446 |
| `release_side` | 0.339 | 0.339 |
| `HB` | 0.226 | 0.226 |

### Cutter

| Variable | Standardized Coefficient | Absolute Importance |
|---|---:|---:|
| `release_side` | -1.910 | 1.910 |
| `release_height` | 1.837 | 1.837 |
| `extension` | 1.639 | 1.639 |
| `spin_rate` | 1.386 | 1.386 |
| `velocity` | -1.123 | 1.123 |
| `HB` | 0.652 | 0.652 |
| `IVB` | 0.106 | 0.106 |

### Four-Seam

| Variable | Standardized Coefficient | Absolute Importance |
|---|---:|---:|
| `IVB` | 1.146 | 1.146 |
| `HB` | -0.744 | 0.744 |
| `velocity` | 0.482 | 0.482 |
| `release_height` | -0.330 | 0.330 |
| `release_side` | 0.153 | 0.153 |
| `extension` | 0.086 | 0.086 |
| `spin_rate` | 0.044 | 0.044 |

### Pooled

| Variable | Standardized Coefficient | Absolute Importance |
|---|---:|---:|
| `spin_rate` | 1.324 | 1.324 |
| `IVB` | 1.216 | 1.216 |
| `velocity` | -0.450 | 0.450 |
| `HB` | -0.281 | 0.281 |
| `extension` | 0.279 | 0.279 |
| `release_side` | 0.090 | 0.090 |
| `release_height` | -0.006 | 0.006 |

### Sinker

| Variable | Standardized Coefficient | Absolute Importance |
|---|---:|---:|
| `HB` | -1.624 | 1.624 |
| `spin_rate` | 1.611 | 1.611 |
| `release_height` | -1.200 | 1.200 |
| `release_side` | 0.917 | 0.917 |
| `IVB` | 0.429 | 0.429 |
| `velocity` | 0.259 | 0.259 |
| `extension` | 0.065 | 0.065 |

### Slider

| Variable | Standardized Coefficient | Absolute Importance |
|---|---:|---:|
| `spin_rate` | 1.147 | 1.147 |
| `HB` | -0.917 | 0.917 |
| `extension` | 0.910 | 0.910 |
| `velocity` | -0.781 | 0.781 |
| `IVB` | 0.373 | 0.373 |
| `release_side` | -0.227 | 0.227 |
| `release_height` | 0.151 | 0.151 |

## Top 25 Stuff+ Pitches

| Rank | Pitcher | Team | Pitch Type | Side | Stuff+ | Stuff % | Final | Velo | IVB | HB | Spin | Model |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | Vega, Lucas | TRO_AIG | Slider | RHH | 78.9 | 100.0 | 67.2 | 79.2 | 6.6 | -9.3 | 2697 | pitch_type_specific |
| 2 | Vega, Lucas | TRO_AIG | Slider | LHH | 78.9 | 100.0 | 59.4 | 79.2 | 6.6 | -9.3 | 2697 | pitch_type_specific |
| 3 | Harris, Everette | TRI_VAL | Slider | LHH | 77.1 | 99.9 | 59.3 | 80.5 | 1.1 | -8.3 | 2845 | pitch_type_specific |
| 4 | Harris, Everette | TRI_VAL | Slider | RHH | 77.1 | 99.9 | 51.3 | 80.5 | 1.1 | -8.3 | 2845 | pitch_type_specific |
| 5 | Morrissey, Joe | EVA_OTT | Slider | RHH | 76.7 | 99.8 | 61.8 | 79.8 | 2.0 | -13.3 | 2768 | pitch_type_specific |
| 6 | Harper, Scott | NEW_YOR13 | Slider | RHH | 76.6 | 99.7 | 70.8 | 79.7 | 3.2 | -16.7 | 2664 | pitch_type_specific |
| 7 | Harper, Scott | NEW_YOR13 | Slider | LHH | 76.6 | 99.7 | 65.3 | 79.7 | 3.2 | -16.7 | 2664 | pitch_type_specific |
| 8 | Petery, Dylan | WIN_CIT29 | Slider | RHH | 75.6 | 99.6 | 54.5 | 78.0 | -0.4 | -12.4 | 2605 | pitch_type_specific |
| 9 | Petery, Dylan | WIN_CIT29 | Slider | LHH | 75.6 | 99.6 | 50.4 | 78.0 | -0.4 | -12.4 | 2605 | pitch_type_specific |
| 10 | Ronne, Andrew | GAT_GRI | Slider | RHH | 75.0 | 99.5 | 59.7 | 81.3 | -0.5 | -14.5 | 2602 | pitch_type_specific |
| 11 | Ronne, Andrew | GAT_GRI | Slider | LHH | 75.0 | 99.5 | 54.3 | 81.3 | -0.5 | -14.5 | 2602 | pitch_type_specific |
| 12 | Bauer, Patrick | QUE_CAP | Slider | RHH | 74.8 | 99.4 | 74.8 | 78.0 | 0.1 | -10.5 | 2416 | pitch_type_specific |
| 13 | Saturria, Michael | NEW_ENG23 | Slider | RHH | 74.8 | 99.3 | 55.3 | 80.8 | 4.0 | -7.0 | 2703 | pitch_type_specific |
| 14 | Saturria, Michael | NEW_ENG23 | Slider | LHH | 74.8 | 99.3 | 53.5 | 80.8 | 4.0 | -7.0 | 2703 | pitch_type_specific |
| 15 | Morgan, Marcus | JOL_SLA | Slider | LHH | 74.5 | 99.2 | 51.1 | 84.9 | 7.0 | -9.2 | 2844 | pitch_type_specific |
| 16 | Voytko, Fawster | TRO_AIG | Slider | RHH | 73.9 | 99.1 | 49.5 | 78.8 | 1.6 | -11.3 | 2320 | pitch_type_specific |
| 17 | Voytko, Fawster | TRO_AIG | Slider | LHH | 73.9 | 99.1 | 40.0 | 78.8 | 1.6 | -11.3 | 2320 | pitch_type_specific |
| 18 | Marklund, Brandon | OTT_TIT | Slider | RHH | 73.5 | 99.0 | 59.9 | 79.6 | 6.4 | -14.2 | 2707 | pitch_type_specific |
| 19 | Marklund, Brandon | OTT_TIT | Slider | LHH | 73.5 | 99.0 | 54.7 | 79.6 | 6.4 | -14.2 | 2707 | pitch_type_specific |
| 20 | Conklin, MacCallan | TRO_AIG | Slider | RHH | 73.2 | 98.9 | 53.3 | 83.8 | 6.1 | -3.8 | 2592 | pitch_type_specific |
| 21 | Conklin, MacCallan | TRO_AIG | Slider | LHH | 73.2 | 98.9 | 49.7 | 83.8 | 6.1 | -3.8 | 2592 | pitch_type_specific |
| 22 | Morin, Jacob | QUE_CAP | Slider | RHH | 73.0 | 98.8 | 64.9 | 77.4 | 7.4 | -6.2 | 2495 | pitch_type_specific |
| 23 | Morin, Jacob | QUE_CAP | Slider | LHH | 73.0 | 98.8 | 57.8 | 77.4 | 7.4 | -6.2 | 2495 | pitch_type_specific |
| 24 | Blence, Connor | WIN_CIT29 | Slider | RHH | 72.8 | 98.7 | 52.4 | 79.5 | 3.8 | -4.9 | 2552 | pitch_type_specific |
| 25 | Blence, Connor | WIN_CIT29 | Slider | LHH | 72.8 | 98.7 | 43.3 | 79.5 | 3.8 | -4.9 | 2552 | pitch_type_specific |

## Top 10 Stuff+ by Pitch Type

### Changeup

| Rank | Pitcher | Team | Pitch Type | Side | Stuff+ | Stuff % | Final | Velo | IVB | HB | Spin | Model |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 50 | Kines, Gunnar | JOL_SLA | Changeup | LHH | 69.3 | 97.2 | 51.0 | 75.2 | 12.1 | -12.6 | 1900 | pitch_type_specific |
| 51 | Kines, Gunnar | JOL_SLA | Changeup | RHH | 69.3 | 97.2 | 51.0 | 75.2 | 12.1 | -12.6 | 1900 | pitch_type_specific |
| 81 | Maietta, Dante | WIN_CIT29 | Changeup | LHH | 67.9 | 95.5 | 62.2 | 77.7 | 15.3 | 13.9 | 1871 | pitch_type_specific |
| 82 | Maietta, Dante | WIN_CIT29 | Changeup | RHH | 67.9 | 95.5 | 57.1 | 77.7 | 15.3 | 13.9 | 1871 | pitch_type_specific |
| 101 | VanMarter, Luke | LEM_COL | Changeup | RHH | 66.6 | 94.4 | 57.5 | 77.6 | 12.9 | 11.7 | 1756 | pitch_type_specific |
| 102 | Wiltse, Ryan | EVA_OTT | Changeup | RHH | 66.5 | 94.3 | 62.8 | 78.1 | 13.6 | 10.2 | 1834 | pitch_type_specific |
| 103 | Wiltse, Ryan | EVA_OTT | Changeup | LHH | 66.5 | 94.3 | 62.0 | 78.1 | 13.6 | 10.2 | 1834 | pitch_type_specific |
| 116 | Good, Ty | GAT_GRI | Changeup | LHH | 66.3 | 93.6 | 62.5 | 77.9 | 17.1 | 4.5 | 1773 | pitch_type_specific |
| 118 | Westcott, Zac | FLO_Y'A | Changeup | LHH | 66.2 | 93.4 | 46.6 | 76.5 | 6.5 | 16.7 | 1915 | pitch_type_specific |
| 119 | Westcott, Zac | FLO_Y'A | Changeup | RHH | 66.2 | 93.4 | 40.7 | 76.5 | 6.5 | 16.7 | 1915 | pitch_type_specific |

### Curveball

| Rank | Pitcher | Team | Pitch Type | Side | Stuff+ | Stuff % | Final | Velo | IVB | HB | Spin | Model |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 106 | Moore, Kyle | SCH_BOO | Curveball | RHH | 66.4 | 94.1 | 54.3 | 76.9 | -8.6 | -7.7 | 2521 | pitch_type_specific |
| 107 | Moore, Kyle | SCH_BOO | Curveball | LHH | 66.4 | 94.1 | 49.1 | 76.9 | -8.6 | -7.7 | 2521 | pitch_type_specific |
| 225 | Sparks, Alec | GAT_GRI | Curveball | LHH | 62.8 | 87.4 | 68.7 | 77.6 | -4.4 | -7.0 | 2566 | pitch_type_specific |
| 226 | Sparks, Alec | GAT_GRI | Curveball | RHH | 62.8 | 87.4 | 65.4 | 77.6 | -4.4 | -7.0 | 2566 | pitch_type_specific |
| 253 | Campbell, AJ | WIN_CIT29 | Curveball | LHH | 62.0 | 85.8 | 56.1 | 75.2 | -0.9 | -16.1 | 2587 | pitch_type_specific |
| 254 | Campbell, AJ | WIN_CIT29 | Curveball | RHH | 62.0 | 85.8 | 54.8 | 75.2 | -0.9 | -16.1 | 2587 | pitch_type_specific |
| 260 | Maryniak, Connor | NEW_JER6 | Curveball | RHH | 61.8 | 85.4 | 57.6 | 81.3 | -9.6 | -4.5 | 2514 | pitch_type_specific |
| 261 | Maryniak, Connor | NEW_JER6 | Curveball | LHH | 61.8 | 85.4 | 53.0 | 81.3 | -9.6 | -4.5 | 2514 | pitch_type_specific |
| 266 | Peyton, Blake | GAT_GRI | Curveball | RHH | 61.6 | 85.1 | 50.2 | 77.6 | -7.2 | 9.4 | 2714 | pitch_type_specific |
| 267 | Peyton, Blake | GAT_GRI | Curveball | LHH | 61.6 | 85.1 | 49.1 | 77.6 | -7.2 | 9.4 | 2714 | pitch_type_specific |

### Cutter

| Rank | Pitcher | Team | Pitch Type | Side | Stuff+ | Stuff % | Final | Velo | IVB | HB | Spin | Model |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 26 | Barreto, Brayhans | TRI_VAL | Cutter | LHH | 72.6 | 98.6 | 62.6 | 83.5 | 9.1 | 0.1 | 1919 | pitch_type_specific |
| 34 | Majick, Eli | NEW_ENG23 | Cutter | RHH | 71.0 | 98.1 | 64.2 | 83.1 | 5.8 | -1.1 | 2491 | pitch_type_specific |
| 35 | Majick, Eli | NEW_ENG23 | Cutter | LHH | 71.0 | 98.1 | 61.9 | 83.1 | 5.8 | -1.1 | 2491 | pitch_type_specific |
| 36 | Good, Ty | GAT_GRI | Cutter | RHH | 70.9 | 98.0 | 54.8 | 88.3 | 17.0 | 7.6 | 2054 | pitch_type_specific |
| 41 | Webster, Evan | FLO_Y'A | Cutter | LHH | 70.4 | 97.7 | 61.8 | 84.5 | 5.7 | -0.5 | 2031 | pitch_type_specific |
| 42 | Webster, Evan | FLO_Y'A | Cutter | RHH | 70.4 | 97.7 | 60.8 | 84.5 | 5.7 | -0.5 | 2031 | pitch_type_specific |
| 58 | Thiels, Brenton | MIS_MUD | Cutter | RHH | 68.7 | 96.8 | 42.5 | 86.3 | 9.4 | 4.5 | 2311 | pitch_type_specific |
| 133 | Debban, Caleb | NEW_JER6 | Cutter | LHH | 65.7 | 92.6 | 51.4 | 85.9 | 10.7 | -0.5 | 2336 | pitch_type_specific |
| 134 | Debban, Caleb | NEW_JER6 | Cutter | RHH | 65.7 | 92.6 | 51.3 | 85.9 | 10.7 | -0.5 | 2336 | pitch_type_specific |
| 235 | Ginn, Landon | WAS_WIL3 | Cutter | RHH | 62.5 | 86.8 | 48.9 | 86.4 | 3.3 | -2.0 | 2836 | pitch_type_specific |

### Four-Seam

| Rank | Pitcher | Team | Pitch Type | Side | Stuff+ | Stuff % | Final | Velo | IVB | HB | Spin | Model |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 414 | Rodriguez, Luis | TRO_AIG | Four-Seam | LHH | 57.2 | 76.8 | 50.5 | 95.1 | 20.6 | 7.0 | 2360 | pitch_type_specific |
| 415 | Rodriguez, Luis | TRO_AIG | Four-Seam | RHH | 57.2 | 76.8 | 49.1 | 95.1 | 20.6 | 7.0 | 2360 | pitch_type_specific |
| 438 | Davis, Tyler | WAS_WIL3 | Four-Seam | LHH | 56.6 | 75.5 | 53.2 | 92.6 | 18.5 | -11.2 | 2340 | pitch_type_specific |
| 439 | Davis, Tyler | WAS_WIL3 | Four-Seam | RHH | 56.6 | 75.5 | 46.6 | 92.6 | 18.5 | -11.2 | 2340 | pitch_type_specific |
| 453 | Eisenbarger, Jack | QUE_CAP | Four-Seam | LHH | 56.1 | 74.6 | 49.4 | 90.0 | 18.9 | -13.8 | 2545 | pitch_type_specific |
| 454 | Eisenbarger, Jack | QUE_CAP | Four-Seam | RHH | 56.1 | 74.6 | 48.4 | 90.0 | 18.9 | -13.8 | 2545 | pitch_type_specific |
| 457 | Maher, Adam | TRI_VAL | Four-Seam | LHH | 56.0 | 74.4 | 49.7 | 87.8 | 20.4 | -9.7 | 2076 | pitch_type_specific |
| 458 | Maher, Adam | TRI_VAL | Four-Seam | RHH | 56.0 | 74.4 | 49.5 | 87.8 | 20.4 | -9.7 | 2076 | pitch_type_specific |
| 462 | Cartwright, Eli | GAT_GRI | Four-Seam | LHH | 55.9 | 74.1 | 60.5 | 90.3 | 18.4 | -8.6 | 2100 | pitch_type_specific |
| 463 | Cartwright, Eli | GAT_GRI | Four-Seam | RHH | 55.9 | 74.1 | 56.6 | 90.3 | 18.4 | -8.6 | 2100 | pitch_type_specific |

### Sinker

| Rank | Pitcher | Team | Pitch Type | Side | Stuff+ | Stuff % | Final | Velo | IVB | HB | Spin | Model |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 493 | Widener, Jacob | SUS_COU1 | Sinker | LHH | 55.0 | 72.4 | 60.6 | 88.7 | 8.2 | -11.0 | 2348 | pitch_type_specific |
| 494 | Widener, Jacob | SUS_COU1 | Sinker | RHH | 55.0 | 72.4 | 57.5 | 88.7 | 8.2 | -11.0 | 2348 | pitch_type_specific |
| 495 | Kemlage, Joe | NEW_ENG23 | Sinker | LHH | 55.0 | 72.3 | 47.6 | 91.0 | 8.5 | -15.3 | 2433 | pitch_type_specific |
| 496 | Kemlage, Joe | NEW_ENG23 | Sinker | RHH | 55.0 | 72.3 | 46.6 | 91.0 | 8.5 | -15.3 | 2433 | pitch_type_specific |
| 519 | Plumadore, Carson | WIN_CIT29 | Sinker | RHH | 54.7 | 70.9 | 58.4 | 87.3 | 13.9 | 18.4 | 2381 | pitch_type_specific |
| 520 | Plumadore, Carson | WIN_CIT29 | Sinker | LHH | 54.7 | 70.9 | 56.8 | 87.3 | 13.9 | 18.4 | 2381 | pitch_type_specific |
| 524 | Riedel, Caleb | SCH_BOO | Sinker | RHH | 54.6 | 70.6 | 63.3 | 88.9 | 15.9 | -15.9 | 2306 | pitch_type_specific |
| 525 | Riedel, Caleb | SCH_BOO | Sinker | LHH | 54.6 | 70.6 | 62.6 | 88.9 | 15.9 | -15.9 | 2306 | pitch_type_specific |
| 537 | Morgan, Marcus | JOL_SLA | Sinker | LHH | 54.4 | 69.9 | 56.5 | 91.9 | 10.3 | 15.2 | 2455 | pitch_type_specific |
| 538 | Morgan, Marcus | JOL_SLA | Sinker | RHH | 54.4 | 69.9 | 54.4 | 91.9 | 10.3 | 15.2 | 2455 | pitch_type_specific |

### Slider

| Rank | Pitcher | Team | Pitch Type | Side | Stuff+ | Stuff % | Final | Velo | IVB | HB | Spin | Model |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | Vega, Lucas | TRO_AIG | Slider | RHH | 78.9 | 100.0 | 67.2 | 79.2 | 6.6 | -9.3 | 2697 | pitch_type_specific |
| 2 | Vega, Lucas | TRO_AIG | Slider | LHH | 78.9 | 100.0 | 59.4 | 79.2 | 6.6 | -9.3 | 2697 | pitch_type_specific |
| 3 | Harris, Everette | TRI_VAL | Slider | LHH | 77.1 | 99.9 | 59.3 | 80.5 | 1.1 | -8.3 | 2845 | pitch_type_specific |
| 4 | Harris, Everette | TRI_VAL | Slider | RHH | 77.1 | 99.9 | 51.3 | 80.5 | 1.1 | -8.3 | 2845 | pitch_type_specific |
| 5 | Morrissey, Joe | EVA_OTT | Slider | RHH | 76.7 | 99.8 | 61.8 | 79.8 | 2.0 | -13.3 | 2768 | pitch_type_specific |
| 6 | Harper, Scott | NEW_YOR13 | Slider | RHH | 76.6 | 99.7 | 70.8 | 79.7 | 3.2 | -16.7 | 2664 | pitch_type_specific |
| 7 | Harper, Scott | NEW_YOR13 | Slider | LHH | 76.6 | 99.7 | 65.3 | 79.7 | 3.2 | -16.7 | 2664 | pitch_type_specific |
| 8 | Petery, Dylan | WIN_CIT29 | Slider | RHH | 75.6 | 99.6 | 54.5 | 78.0 | -0.4 | -12.4 | 2605 | pitch_type_specific |
| 9 | Petery, Dylan | WIN_CIT29 | Slider | LHH | 75.6 | 99.6 | 50.4 | 78.0 | -0.4 | -12.4 | 2605 | pitch_type_specific |
| 10 | Ronne, Andrew | GAT_GRI | Slider | RHH | 75.0 | 99.5 | 59.7 | 81.3 | -0.5 | -14.5 | 2602 | pitch_type_specific |

### Splitter

| Rank | Pitcher | Team | Pitch Type | Side | Stuff+ | Stuff % | Final | Velo | IVB | HB | Spin | Model |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 124 | Williams, Brian | MIS_MUD | Splitter | LHH | 66.0 | 93.1 | 52.8 | 78.6 | 2.7 | 4.9 | 1775 | pooled_fixed_effects |
| 125 | Williams, Brian | MIS_MUD | Splitter | RHH | 66.0 | 93.1 | 51.8 | 78.6 | 2.7 | 4.9 | 1775 | pooled_fixed_effects |
| 293 | Garcia, Hector | WAS_WIL3 | Splitter | LHH | 61.1 | 83.6 | 64.4 | 78.2 | 11.7 | 7.6 | 1216 | pooled_fixed_effects |
| 382 | Gilleran, Jimmy | NEW_ENG23 | Splitter | LHH | 58.1 | 78.6 | 39.3 | 79.1 | 0.0 | 7.7 | 1520 | pooled_fixed_effects |
| 474 | Pindel, Buddie | SCH_BOO | Splitter | RHH | 55.5 | 73.4 | 57.5 | 80.4 | 5.3 | 7.2 | 1119 | pooled_fixed_effects |
| 475 | Pindel, Buddie | SCH_BOO | Splitter | LHH | 55.5 | 73.4 | 56.9 | 80.4 | 5.3 | 7.2 | 1119 | pooled_fixed_effects |
| 485 | Villers, Ian | QUE_CAP | Splitter | RHH | 55.2 | 72.8 | 59.0 | 83.1 | 7.5 | 11.5 | 1086 | pooled_fixed_effects |
| 486 | Villers, Ian | QUE_CAP | Splitter | LHH | 55.2 | 72.8 | 58.1 | 83.1 | 7.5 | 11.5 | 1086 | pooled_fixed_effects |
| 502 | Duby, Bill | NEW_JER6 | Splitter | LHH | 54.8 | 71.9 | 37.6 | 78.9 | 5.9 | 3.5 | 958 | pooled_fixed_effects |
| 530 | Salata, Derek | SCH_BOO | Splitter | LHH | 54.6 | 70.3 | 50.8 | 83.1 | 5.8 | 8.6 | 1116 | pooled_fixed_effects |

### Sweeper

| Rank | Pitcher | Team | Pitch Type | Side | Stuff+ | Stuff % | Final | Velo | IVB | HB | Spin | Model |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 92 | Petschke, Ben | EVA_OTT | Sweeper | LHH | 67.3 | 94.9 | 51.5 | 79.7 | -2.7 | -17.1 | 2741 | pooled_fixed_effects |
| 150 | Cerda, Junior | EVA_OTT | Sweeper | RHH | 65.3 | 91.6 | 57.3 | 81.2 | -3.2 | -11.9 | 2677 | pooled_fixed_effects |
