# Stuff+ Movement Model

- Input file: `data\processed\master_pitch_evaluation_table.csv`
- Output file: `data\processed\stuff_plus_scores.csv`
- Scored rows: 988
- Dependent variable: `final_pitch_score_20_80`
- Predictors: `IVB`, `HB`, `velocity`, `spin_rate`, `extension`, `release_height`, `release_side`
- Pitch-type-specific model minimum: 30 rows
- Low-sample pitch types use the fallback pooled model with pitch type fixed effects.

## Warnings

- None.

## Model Summaries

| Model | Type | Rows | R-squared | Intercept |
|---|---|---:|---:|---:|
| Changeup | pitch_type_specific | 118 | 0.0918 | 49.15 |
| Curveball | pitch_type_specific | 74 | 0.2405 | 48.86 |
| Cutter | pitch_type_specific | 36 | 0.1223 | 50.05 |
| Four-Seam | pitch_type_specific | 386 | 0.0598 | 49.21 |
| Sinker | pitch_type_specific | 178 | 0.1662 | 47.33 |
| Slider | pitch_type_specific | 187 | 0.0962 | 53.20 |
| Pooled | pooled_fixed_effects | 988 | 0.0814 | 49.90 |

## Variable Importance by Pitch Type

### Changeup

| Variable | Standardized Coefficient | Absolute Importance |
|---|---:|---:|
| `release_side` | 2.349 | 2.349 |
| `velocity` | -1.861 | 1.861 |
| `HB` | -1.476 | 1.476 |
| `IVB` | 0.986 | 0.986 |
| `spin_rate` | -0.800 | 0.800 |
| `release_height` | -0.242 | 0.242 |
| `extension` | 0.192 | 0.192 |

### Curveball

| Variable | Standardized Coefficient | Absolute Importance |
|---|---:|---:|
| `IVB` | -3.785 | 3.785 |
| `release_side` | -2.936 | 2.936 |
| `velocity` | 2.928 | 2.928 |
| `spin_rate` | -1.546 | 1.546 |
| `extension` | -1.242 | 1.242 |
| `HB` | -1.167 | 1.167 |
| `release_height` | -0.143 | 0.143 |

### Cutter

| Variable | Standardized Coefficient | Absolute Importance |
|---|---:|---:|
| `release_side` | -2.144 | 2.144 |
| `HB` | 1.628 | 1.628 |
| `release_height` | 1.344 | 1.344 |
| `velocity` | -1.289 | 1.289 |
| `extension` | 1.063 | 1.063 |
| `spin_rate` | 0.943 | 0.943 |
| `IVB` | 0.696 | 0.696 |

### Four-Seam

| Variable | Standardized Coefficient | Absolute Importance |
|---|---:|---:|
| `IVB` | 1.568 | 1.568 |
| `velocity` | 0.721 | 0.721 |
| `HB` | -0.522 | 0.522 |
| `release_side` | 0.236 | 0.236 |
| `extension` | 0.197 | 0.197 |
| `spin_rate` | -0.044 | 0.044 |
| `release_height` | 0.025 | 0.025 |

### Pooled

| Variable | Standardized Coefficient | Absolute Importance |
|---|---:|---:|
| `IVB` | 1.392 | 1.392 |
| `spin_rate` | 0.650 | 0.650 |
| `extension` | 0.498 | 0.498 |
| `velocity` | -0.471 | 0.471 |
| `release_height` | -0.310 | 0.310 |
| `HB` | -0.294 | 0.294 |
| `release_side` | 0.243 | 0.243 |

### Sinker

| Variable | Standardized Coefficient | Absolute Importance |
|---|---:|---:|
| `spin_rate` | 2.308 | 2.308 |
| `HB` | -2.072 | 2.072 |
| `release_height` | -1.262 | 1.262 |
| `IVB` | 0.918 | 0.918 |
| `release_side` | 0.731 | 0.731 |
| `extension` | 0.385 | 0.385 |
| `velocity` | -0.124 | 0.124 |

### Slider

| Variable | Standardized Coefficient | Absolute Importance |
|---|---:|---:|
| `velocity` | -2.111 | 2.111 |
| `extension` | 1.616 | 1.616 |
| `release_height` | -1.012 | 1.012 |
| `release_side` | 0.720 | 0.720 |
| `spin_rate` | 0.547 | 0.547 |
| `HB` | -0.159 | 0.159 |
| `IVB` | -0.018 | 0.018 |

## Top 25 Stuff+ Pitches

| Rank | Pitcher | Team | Pitch Type | Side | Stuff+ | Stuff % | Final | Velo | IVB | HB | Spin | Model |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | Plumadore, Carson | WIN_CIT29 | Slider | RHH | 80.0 | 100.0 | 56.5 | 75.7 | 3.4 | -6.0 | 2452 | pitch_type_specific |
| 2 | Garcia, Brett | OTT_TIT | Curveball | RHH | 80.0 | 99.8 | 57.8 | 81.1 | -16.8 | -7.5 | 2116 | pitch_type_specific |
| 3 | Garcia, Brett | OTT_TIT | Curveball | LHH | 80.0 | 99.8 | 56.3 | 81.1 | -16.8 | -7.5 | 2116 | pitch_type_specific |
| 4 | Garcia, Hector | WAS_WIL3 | Splitter | LHH | 80.0 | 99.7 | 64.2 | 78.2 | 11.7 | 7.6 | 1216 | pooled_fixed_effects |
| 5 | Campbell, Tyler | MIS_MUD | Slider | RHH | 80.0 | 99.6 | 48.0 | 74.0 | 8.0 | 5.4 | 2236 | pitch_type_specific |
| 6 | Harper, Scott | NEW_YOR13 | Slider | RHH | 80.0 | 99.5 | 74.5 | 79.8 | 3.2 | -16.4 | 2650 | pitch_type_specific |
| 7 | Smith, Jackson | MIS_MUD | Slider | RHH | 79.3 | 99.4 | 67.7 | 78.1 | 2.1 | -10.2 | 2661 | pitch_type_specific |
| 8 | Vega, Lucas | TRO_AIG | Slider | RHH | 78.7 | 99.3 | 60.6 | 79.0 | 6.2 | -10.8 | 2705 | pitch_type_specific |
| 9 | Duby, Bill | NEW_JER6 | Slider | RHH | 78.5 | 99.2 | 62.3 | 79.7 | 8.1 | 0.4 | 2027 | pitch_type_specific |
| 10 | Whitesell, Max | FLO_Y'A | Slider | RHH | 77.2 | 99.0 | 63.7 | 80.1 | 6.4 | -4.2 | 2081 | pitch_type_specific |
| 11 | Whitesell, Max | FLO_Y'A | Slider | LHH | 77.2 | 99.0 | 56.2 | 80.1 | 6.4 | -4.2 | 2081 | pitch_type_specific |
| 12 | Pindel, Buddie | SCH_BOO | Splitter | RHH | 76.2 | 98.8 | 58.6 | 80.3 | 4.8 | 7.3 | 1095 | pooled_fixed_effects |
| 13 | Pindel, Buddie | SCH_BOO | Splitter | LHH | 76.2 | 98.8 | 58.5 | 80.3 | 4.8 | 7.3 | 1095 | pooled_fixed_effects |
| 14 | Salata, Derek | SCH_BOO | Splitter | LHH | 75.6 | 98.7 | 54.6 | 83.0 | 6.5 | 8.9 | 1104 | pooled_fixed_effects |
| 15 | Thompson, Ross | SCH_BOO | Splitter | LHH | 75.4 | 98.6 | 56.1 | 79.6 | 4.4 | 9.4 | 1066 | pooled_fixed_effects |
| 16 | Morin, Jacob | QUE_CAP | Slider | RHH | 75.2 | 98.4 | 62.7 | 77.4 | 7.4 | -6.2 | 2495 | pitch_type_specific |
| 17 | Morin, Jacob | QUE_CAP | Slider | LHH | 75.2 | 98.4 | 59.5 | 77.4 | 7.4 | -6.2 | 2495 | pitch_type_specific |
| 18 | Villers, Ian | QUE_CAP | Splitter | RHH | 75.2 | 98.2 | 58.9 | 83.1 | 7.5 | 11.5 | 1086 | pooled_fixed_effects |
| 19 | Villers, Ian | QUE_CAP | Splitter | LHH | 75.2 | 98.2 | 58.2 | 83.1 | 7.5 | 11.5 | 1086 | pooled_fixed_effects |
| 20 | Saturria, Michael | NEW_ENG23 | Slider | LHH | 73.9 | 98.0 | 49.9 | 80.3 | 4.1 | -7.8 | 2707 | pitch_type_specific |
| 21 | Saturria, Michael | NEW_ENG23 | Slider | RHH | 73.9 | 98.0 | 49.7 | 80.3 | 4.1 | -7.8 | 2707 | pitch_type_specific |
| 22 | Harris, Ben | GAT_GRI | Curveball | RHH | 73.7 | 97.8 | 64.1 | 78.0 | -14.0 | -7.2 | 2124 | pitch_type_specific |
| 23 | Harris, Ben | GAT_GRI | Curveball | LHH | 73.7 | 97.8 | 61.2 | 78.0 | -14.0 | -7.2 | 2124 | pitch_type_specific |
| 24 | Garcia, Hector | WAS_WIL3 | Slider | RHH | 72.9 | 97.7 | 62.0 | 77.3 | 2.0 | -7.1 | 2355 | pitch_type_specific |
| 25 | Carroll, Jake | JOL_SLA | Slider | LHH | 72.8 | 97.6 | 69.8 | 75.2 | -6.4 | 7.7 | 2019 | pitch_type_specific |

## Top 10 Stuff+ by Pitch Type

### Changeup

| Rank | Pitcher | Team | Pitch Type | Side | Stuff+ | Stuff % | Final | Velo | IVB | HB | Spin | Model |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 92 | Thompson, Ross | SCH_BOO | Changeup | LHH | 64.0 | 90.8 | 53.1 | 79.6 | 5.3 | 9.1 | 1084 | pitch_type_specific |
| 100 | Cooper, Garrett | NEW_YOR13 | Changeup | LHH | 63.5 | 89.9 | 61.1 | 78.1 | 8.5 | 6.7 | 1449 | pitch_type_specific |
| 101 | Cooper, Garrett | NEW_YOR13 | Changeup | RHH | 63.5 | 89.9 | 54.5 | 78.1 | 8.5 | 6.7 | 1449 | pitch_type_specific |
| 110 | Brothers, Kellen | SUS_COU1 | Changeup | LHH | 62.3 | 89.0 | 40.3 | 80.0 | 11.7 | 12.4 | 1559 | pitch_type_specific |
| 112 | Maietta, Dante | WIN_CIT29 | Changeup | LHH | 62.3 | 88.7 | 66.1 | 77.1 | 15.5 | 14.9 | 1846 | pitch_type_specific |
| 113 | Maietta, Dante | WIN_CIT29 | Changeup | RHH | 62.3 | 88.7 | 62.9 | 77.1 | 15.5 | 14.9 | 1846 | pitch_type_specific |
| 125 | Kines, Gunnar | JOL_SLA | Changeup | RHH | 61.6 | 87.4 | 51.4 | 75.8 | 12.7 | -12.7 | 1897 | pitch_type_specific |
| 126 | Kines, Gunnar | JOL_SLA | Changeup | LHH | 61.6 | 87.4 | 50.2 | 75.8 | 12.7 | -12.7 | 1897 | pitch_type_specific |
| 137 | VanMarter, Luke | LEM_COL | Changeup | RHH | 60.0 | 86.2 | 55.3 | 77.6 | 12.9 | 11.7 | 1756 | pitch_type_specific |
| 140 | Escobar, Anthony | TRO_AIG | Changeup | LHH | 59.6 | 85.9 | 71.3 | 79.5 | 10.0 | 11.5 | 1579 | pitch_type_specific |

### Curveball

| Rank | Pitcher | Team | Pitch Type | Side | Stuff+ | Stuff % | Final | Velo | IVB | HB | Spin | Model |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 2 | Garcia, Brett | OTT_TIT | Curveball | RHH | 80.0 | 99.8 | 57.8 | 81.1 | -16.8 | -7.5 | 2116 | pitch_type_specific |
| 3 | Garcia, Brett | OTT_TIT | Curveball | LHH | 80.0 | 99.8 | 56.3 | 81.1 | -16.8 | -7.5 | 2116 | pitch_type_specific |
| 22 | Harris, Ben | GAT_GRI | Curveball | RHH | 73.7 | 97.8 | 64.1 | 78.0 | -14.0 | -7.2 | 2124 | pitch_type_specific |
| 23 | Harris, Ben | GAT_GRI | Curveball | LHH | 73.7 | 97.8 | 61.2 | 78.0 | -14.0 | -7.2 | 2124 | pitch_type_specific |
| 43 | Grounds, Jackson | DOW_EAS1 | Curveball | RHH | 69.1 | 95.7 | 71.6 | 81.4 | -10.5 | -12.0 | 1946 | pitch_type_specific |
| 44 | Grounds, Jackson | DOW_EAS1 | Curveball | LHH | 69.1 | 95.7 | 68.7 | 81.4 | -10.5 | -12.0 | 1946 | pitch_type_specific |
| 55 | Shinn, Nathan | LAK_ERI24 | Curveball | LHH | 67.0 | 94.5 | 45.2 | 79.6 | -5.9 | 0.6 | 2113 | pitch_type_specific |
| 56 | Shinn, Nathan | LAK_ERI24 | Curveball | RHH | 67.0 | 94.5 | 43.4 | 79.6 | -5.9 | 0.6 | 2113 | pitch_type_specific |
| 134 | Anibal, Trevor | NEW_ENG23 | Curveball | RHH | 60.9 | 86.5 | 55.5 | 75.9 | -15.4 | -9.6 | 2476 | pitch_type_specific |
| 135 | Anibal, Trevor | NEW_ENG23 | Curveball | LHH | 60.9 | 86.5 | 51.9 | 75.9 | -15.4 | -9.6 | 2476 | pitch_type_specific |

### Cutter

| Rank | Pitcher | Team | Pitch Type | Side | Stuff+ | Stuff % | Final | Velo | IVB | HB | Spin | Model |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 51 | Thiels, Brenton | MIS_MUD | Cutter | RHH | 67.8 | 94.9 | 42.1 | 86.3 | 9.4 | 4.5 | 2311 | pitch_type_specific |
| 62 | Webster, Evan | FLO_Y'A | Cutter | LHH | 66.7 | 93.8 | 66.7 | 84.3 | 5.6 | -0.2 | 2064 | pitch_type_specific |
| 63 | Webster, Evan | FLO_Y'A | Cutter | RHH | 66.7 | 93.8 | 64.2 | 84.3 | 5.6 | -0.2 | 2064 | pitch_type_specific |
| 68 | Debban, Caleb | NEW_JER6 | Cutter | RHH | 65.8 | 93.2 | 48.4 | 86.1 | 8.9 | 1.3 | 2331 | pitch_type_specific |
| 93 | McEvoy, Aidan | FLO_Y'A | Cutter | LHH | 64.0 | 90.7 | 56.6 | 83.0 | 7.7 | 1.7 | 2145 | pitch_type_specific |
| 207 | Langrell, Connor | MIS_MUD | Cutter | LHH | 57.1 | 79.1 | 51.7 | 86.7 | 10.3 | -0.7 | 2329 | pitch_type_specific |
| 208 | Langrell, Connor | MIS_MUD | Cutter | RHH | 57.1 | 79.1 | 50.4 | 86.7 | 10.3 | -0.7 | 2329 | pitch_type_specific |
| 236 | Cook, Cole | SCH_BOO | Cutter | LHH | 56.0 | 76.2 | 48.1 | 82.3 | 9.0 | -3.2 | 2420 | pitch_type_specific |
| 237 | Cook, Cole | SCH_BOO | Cutter | RHH | 56.0 | 76.2 | 44.8 | 82.3 | 9.0 | -3.2 | 2420 | pitch_type_specific |
| 250 | Salata, Derek | SCH_BOO | Cutter | RHH | 55.3 | 74.7 | 48.7 | 87.4 | 11.0 | -0.1 | 2373 | pitch_type_specific |

### Four-Seam

| Rank | Pitcher | Team | Pitch Type | Side | Stuff+ | Stuff % | Final | Velo | IVB | HB | Spin | Model |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 121 | Rodriguez, Luis | TRO_AIG | Four-Seam | LHH | 61.8 | 87.8 | 50.7 | 95.1 | 20.6 | 6.4 | 2336 | pitch_type_specific |
| 122 | Rodriguez, Luis | TRO_AIG | Four-Seam | RHH | 61.8 | 87.8 | 49.2 | 95.1 | 20.6 | 6.4 | 2336 | pitch_type_specific |
| 148 | Perozzi, John | SUS_COU1 | Four-Seam | RHH | 58.9 | 85.1 | 55.1 | 91.2 | 21.7 | 9.2 | 2169 | pitch_type_specific |
| 149 | Perozzi, John | SUS_COU1 | Four-Seam | LHH | 58.9 | 85.1 | 45.2 | 91.2 | 21.7 | 9.2 | 2169 | pitch_type_specific |
| 155 | Johnson, Preston | MIS_MUD | Four-Seam | RHH | 58.7 | 84.4 | 56.6 | 92.2 | 20.3 | 6.9 | 2368 | pitch_type_specific |
| 156 | Johnson, Preston | MIS_MUD | Four-Seam | LHH | 58.7 | 84.4 | 53.4 | 92.2 | 20.3 | 6.9 | 2368 | pitch_type_specific |
| 168 | Barraza, Chris | MIS_MUD | Four-Seam | RHH | 58.4 | 83.0 | 51.5 | 93.2 | 20.4 | 10.2 | 2446 | pitch_type_specific |
| 169 | Barraza, Chris | MIS_MUD | Four-Seam | LHH | 58.4 | 83.0 | 49.5 | 93.2 | 20.4 | 10.2 | 2446 | pitch_type_specific |
| 184 | Long, Jalon | NEW_YOR13 | Four-Seam | RHH | 58.0 | 81.4 | 53.8 | 91.9 | 20.3 | 7.8 | 2131 | pitch_type_specific |
| 185 | Long, Jalon | NEW_YOR13 | Four-Seam | LHH | 58.0 | 81.4 | 51.6 | 91.9 | 20.3 | 7.8 | 2131 | pitch_type_specific |

### Sinker

| Rank | Pitcher | Team | Pitch Type | Side | Stuff+ | Stuff % | Final | Velo | IVB | HB | Spin | Model |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 66 | Riedel, Caleb | SCH_BOO | Sinker | RHH | 66.3 | 93.4 | 52.7 | 88.6 | 16.3 | -16.0 | 2332 | pitch_type_specific |
| 77 | Widener, Jacob | SUS_COU1 | Sinker | LHH | 65.1 | 92.3 | 61.5 | 88.5 | 10.0 | -12.0 | 2343 | pitch_type_specific |
| 78 | Widener, Jacob | SUS_COU1 | Sinker | RHH | 65.1 | 92.3 | 58.4 | 88.5 | 10.0 | -12.0 | 2343 | pitch_type_specific |
| 96 | Kemlage, Joe | NEW_ENG23 | Sinker | RHH | 63.6 | 90.3 | 43.1 | 91.0 | 9.8 | -15.1 | 2435 | pitch_type_specific |
| 97 | Kemlage, Joe | NEW_ENG23 | Sinker | LHH | 63.6 | 90.3 | 41.8 | 91.0 | 9.8 | -15.1 | 2435 | pitch_type_specific |
| 132 | Plumadore, Carson | WIN_CIT29 | Sinker | RHH | 61.4 | 86.7 | 60.7 | 87.7 | 14.0 | 18.5 | 2396 | pitch_type_specific |
| 133 | Plumadore, Carson | WIN_CIT29 | Sinker | LHH | 61.4 | 86.7 | 58.6 | 87.7 | 14.0 | 18.5 | 2396 | pitch_type_specific |
| 158 | Still, Stephen | TRI_VAL | Sinker | RHH | 58.7 | 84.1 | 64.9 | 90.6 | 14.1 | -18.1 | 2325 | pitch_type_specific |
| 172 | Morgan, Marcus | JOL_SLA | Sinker | LHH | 58.3 | 82.6 | 55.3 | 92.1 | 10.5 | 15.6 | 2454 | pitch_type_specific |
| 173 | Morgan, Marcus | JOL_SLA | Sinker | RHH | 58.3 | 82.6 | 54.9 | 92.1 | 10.5 | 15.6 | 2454 | pitch_type_specific |

### Slider

| Rank | Pitcher | Team | Pitch Type | Side | Stuff+ | Stuff % | Final | Velo | IVB | HB | Spin | Model |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | Plumadore, Carson | WIN_CIT29 | Slider | RHH | 80.0 | 100.0 | 56.5 | 75.7 | 3.4 | -6.0 | 2452 | pitch_type_specific |
| 5 | Campbell, Tyler | MIS_MUD | Slider | RHH | 80.0 | 99.6 | 48.0 | 74.0 | 8.0 | 5.4 | 2236 | pitch_type_specific |
| 6 | Harper, Scott | NEW_YOR13 | Slider | RHH | 80.0 | 99.5 | 74.5 | 79.8 | 3.2 | -16.4 | 2650 | pitch_type_specific |
| 7 | Smith, Jackson | MIS_MUD | Slider | RHH | 79.3 | 99.4 | 67.7 | 78.1 | 2.1 | -10.2 | 2661 | pitch_type_specific |
| 8 | Vega, Lucas | TRO_AIG | Slider | RHH | 78.7 | 99.3 | 60.6 | 79.0 | 6.2 | -10.8 | 2705 | pitch_type_specific |
| 9 | Duby, Bill | NEW_JER6 | Slider | RHH | 78.5 | 99.2 | 62.3 | 79.7 | 8.1 | 0.4 | 2027 | pitch_type_specific |
| 10 | Whitesell, Max | FLO_Y'A | Slider | RHH | 77.2 | 99.0 | 63.7 | 80.1 | 6.4 | -4.2 | 2081 | pitch_type_specific |
| 11 | Whitesell, Max | FLO_Y'A | Slider | LHH | 77.2 | 99.0 | 56.2 | 80.1 | 6.4 | -4.2 | 2081 | pitch_type_specific |
| 16 | Morin, Jacob | QUE_CAP | Slider | RHH | 75.2 | 98.4 | 62.7 | 77.4 | 7.4 | -6.2 | 2495 | pitch_type_specific |
| 17 | Morin, Jacob | QUE_CAP | Slider | LHH | 75.2 | 98.4 | 59.5 | 77.4 | 7.4 | -6.2 | 2495 | pitch_type_specific |

### Splitter

| Rank | Pitcher | Team | Pitch Type | Side | Stuff+ | Stuff % | Final | Velo | IVB | HB | Spin | Model |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 4 | Garcia, Hector | WAS_WIL3 | Splitter | LHH | 80.0 | 99.7 | 64.2 | 78.2 | 11.7 | 7.6 | 1216 | pooled_fixed_effects |
| 12 | Pindel, Buddie | SCH_BOO | Splitter | RHH | 76.2 | 98.8 | 58.6 | 80.3 | 4.8 | 7.3 | 1095 | pooled_fixed_effects |
| 13 | Pindel, Buddie | SCH_BOO | Splitter | LHH | 76.2 | 98.8 | 58.5 | 80.3 | 4.8 | 7.3 | 1095 | pooled_fixed_effects |
| 14 | Salata, Derek | SCH_BOO | Splitter | LHH | 75.6 | 98.7 | 54.6 | 83.0 | 6.5 | 8.9 | 1104 | pooled_fixed_effects |
| 15 | Thompson, Ross | SCH_BOO | Splitter | LHH | 75.4 | 98.6 | 56.1 | 79.6 | 4.4 | 9.4 | 1066 | pooled_fixed_effects |
| 18 | Villers, Ian | QUE_CAP | Splitter | RHH | 75.2 | 98.2 | 58.9 | 83.1 | 7.5 | 11.5 | 1086 | pooled_fixed_effects |
| 19 | Villers, Ian | QUE_CAP | Splitter | LHH | 75.2 | 98.2 | 58.2 | 83.1 | 7.5 | 11.5 | 1086 | pooled_fixed_effects |
| 33 | Vitas, Ben | JOL_SLA | Splitter | LHH | 71.9 | 96.8 | 66.3 | 81.6 | 2.2 | 7.9 | 1048 | pooled_fixed_effects |
| 35 | Nakata, Yuto | QUE_CAP | Splitter | LHH | 71.5 | 96.6 | 44.8 | 83.6 | 3.0 | 6.7 | 989 | pooled_fixed_effects |
