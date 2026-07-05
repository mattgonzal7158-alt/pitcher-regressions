# Location Score Report

- Pitch input file: `data\processed\2026-data-with-woba-xwoba.parquet`
- Location grid input file: `data\processed\location_value_grid.csv`
- Output file: `data\processed\location_scores.csv`
- Assigned pitch rows: 129,986
- Qualified pitcher + pitch type + batter side rows: 1,558
- Qualification: at least 25 pitches with an assigned location grid value
- Score direction: higher is better; positive location advantage means the pitch was located in a lower-xwOBA grid cell than the pitch type + batter side league average.
- Pitch type normalization: `Fastball` is grouped with `Four-Seam`; `Two-Seam` is grouped with `Sinker`.

## Method

Each pitch is assigned to its 0.25 foot plate-location bin and joined to the matching pitch type + batter side Location Value grid.

`location_advantage = league_average_pitch_type_side_xwoba - grid_xwoba`

Here, `grid_xwoba` is the empirical-Bayes-smoothed xwOBA from the Location Value grid. Positive values mean the pitch was thrown to a better-than-average location for that exact pitch type and batter side.

Scores are aggregated by pitcher, normalized pitch type, and batter side:

- `location_score_raw`: average location advantage.
- `location_score_20_80`: scouting-style scale, mean 50 and 10 points per standard deviation, clipped from 20 to 80.
- `location_score_0_100`: percentile rank of `location_score_raw` among qualified rows.

## Top Location Scores

| Rank | Pitcher | Team | Pitch Type | Batter Side | Pitches | Avg Adv | Median Adv | Grid xwOBA | League xwOBA | LS 20-80 | LS 0-100 | Type/Side Rank |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | Gilleran, Jimmy | NEW_ENG23 | Slider | RHH | 54 | 0.0247 | 0.0236 | 0.2083 | 0.2330 | 80.0 | 100.0 | 1 |
| 2 | Wiltse, Ryan | EVA_OTT | Slider | RHH | 59 | 0.0246 | 0.0130 | 0.2084 | 0.2330 | 80.0 | 99.9 | 2 |
| 3 | Garcia, Hector | WAS_WIL3 | Slider | RHH | 36 | 0.0242 | 0.0138 | 0.2088 | 0.2330 | 80.0 | 99.9 | 3 |
| 4 | Thompson, Ross | SCH_BOO | Slider | RHH | 181 | 0.0240 | 0.0116 | 0.2091 | 0.2330 | 80.0 | 99.8 | 4 |
| 5 | Salata, Derek | SCH_BOO | Slider | RHH | 141 | 0.0227 | 0.0167 | 0.2103 | 0.2330 | 80.0 | 99.7 | 5 |
| 6 | Perez, Kelvin | WAS_WIL3 | Slider | RHH | 90 | 0.0227 | 0.0107 | 0.2103 | 0.2330 | 80.0 | 99.7 | 6 |
| 7 | Smith, Ethan | WIN_CIT29 | Slider | RHH | 30 | 0.0222 | 0.0024 | 0.2108 | 0.2330 | 80.0 | 99.6 | 7 |
| 8 | Vailes, Gage | GAT_GRI | Slider | RHH | 177 | 0.0216 | 0.0121 | 0.2114 | 0.2330 | 80.0 | 99.6 | 8 |
| 9 | Allemann, Braeden | QUE_CAP | Slider | RHH | 39 | 0.0214 | 0.0073 | 0.2116 | 0.2330 | 80.0 | 99.5 | 9 |
| 10 | Kirby, Zach | WAS_WIL3 | Slider | RHH | 126 | 0.0211 | 0.0083 | 0.2120 | 0.2330 | 80.0 | 99.4 | 10 |
| 11 | Blair, Davis | DOW_EAS1 | Slider | RHH | 61 | 0.0210 | 0.0130 | 0.2120 | 0.2330 | 80.0 | 99.4 | 11 |
| 12 | Belton, Hunter | MIS_MUD | Slider | RHH | 75 | 0.0210 | 0.0094 | 0.2121 | 0.2330 | 80.0 | 99.3 | 12 |
| 13 | Albert, Wes | TRI_VAL | Slider | RHH | 25 | 0.0209 | 0.0116 | 0.2121 | 0.2330 | 80.0 | 99.2 | 13 |
| 14 | Leak, Anthony | NEW_YOR13 | Slider | RHH | 131 | 0.0207 | 0.0110 | 0.2123 | 0.2330 | 79.8 | 99.2 | 14 |
| 15 | Helt, Robert | LAK_ERI24 | Slider | RHH | 137 | 0.0207 | 0.0042 | 0.2124 | 0.2330 | 79.6 | 99.1 | 15 |
| 16 | Finarelli, Nick | LON_ISL22 | Slider | RHH | 31 | 0.0207 | 0.0041 | 0.2124 | 0.2330 | 79.6 | 99.0 | 16 |
| 17 | Duncan, Tanner | DOW_EAS1 | Slider | RHH | 28 | 0.0206 | 0.0000 | 0.2125 | 0.2330 | 79.5 | 99.0 | 17 |
| 18 | Nova, Fraynel | LAK_ERI24 | Slider | RHH | 126 | 0.0205 | 0.0141 | 0.2125 | 0.2330 | 79.4 | 98.9 | 18 |
| 19 | Perdomo, Rafael | QUE_CAP | Slider | RHH | 46 | 0.0204 | 0.0105 | 0.2126 | 0.2330 | 79.3 | 98.8 | 19 |
| 20 | Gamelin, Shaun | JOL_SLA | Slider | RHH | 34 | 0.0199 | 0.0159 | 0.2131 | 0.2330 | 78.4 | 98.8 | 20 |
| 21 | Moore, Kyle | SCH_BOO | Slider | RHH | 31 | 0.0194 | 0.0094 | 0.2136 | 0.2330 | 77.5 | 98.7 | 21 |
| 22 | Estrella, Noah | TRI_VAL | Four-Seam | RHH | 48 | 0.0192 | 0.0161 | 0.2225 | 0.2416 | 77.0 | 98.7 | 1 |
| 23 | Smith, Donny | JOL_SLA | Slider | RHH | 29 | 0.0183 | 0.0037 | 0.2147 | 0.2330 | 75.4 | 98.6 | 22 |
| 24 | Cameron, Wyatt | SCH_BOO | Slider | RHH | 50 | 0.0183 | 0.0000 | 0.2148 | 0.2330 | 75.4 | 98.5 | 23 |
| 25 | Delaney, Carter | WIN_CIT29 | Slider | RHH | 40 | 0.0182 | 0.0087 | 0.2148 | 0.2330 | 75.4 | 98.5 | 24 |
| 26 | Hagan, Jack | DOW_EAS1 | Slider | RHH | 118 | 0.0182 | 0.0110 | 0.2149 | 0.2330 | 75.2 | 98.4 | 25 |
| 27 | Johnson, Preston | MIS_MUD | Four-Seam | RHH | 28 | 0.0180 | 0.0162 | 0.2236 | 0.2416 | 75.0 | 98.3 | 2 |
| 28 | Encarnacion, J.D. | EVA_OTT | Changeup | LHH | 28 | 0.0180 | 0.0126 | 0.2245 | 0.2425 | 74.9 | 98.3 | 1 |
| 29 | Maietta, Dante | WIN_CIT29 | Slider | RHH | 38 | 0.0179 | 0.0008 | 0.2152 | 0.2330 | 74.7 | 98.2 | 26 |
| 30 | McCartney, Seth | MIS_MUD | Slider | RHH | 36 | 0.0178 | 0.0021 | 0.2152 | 0.2330 | 74.6 | 98.1 | 27 |

## Top Location Scores by Pitch Type and Batter Side

### Changeup vs LHH

| Rank | Pitcher | Team | Pitch Type | Batter Side | Pitches | Avg Adv | Median Adv | Grid xwOBA | League xwOBA | LS 20-80 | LS 0-100 | Type/Side Rank |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 28 | Encarnacion, J.D. | EVA_OTT | Changeup | LHH | 28 | 0.0180 | 0.0126 | 0.2245 | 0.2425 | 74.9 | 98.3 | 1 |
| 37 | Smith, Jackson | MIS_MUD | Changeup | LHH | 51 | 0.0170 | 0.0113 | 0.2255 | 0.2425 | 73.1 | 97.7 | 2 |
| 67 | Dill, Austin | TRI_VAL | Changeup | LHH | 107 | 0.0150 | 0.0113 | 0.2275 | 0.2425 | 69.6 | 95.8 | 3 |
| 69 | Gregory, Ben | GAT_GRI | Changeup | LHH | 34 | 0.0150 | 0.0001 | 0.2275 | 0.2425 | 69.5 | 95.6 | 4 |
| 70 | Burcham, Jacob | GAT_GRI | Changeup | LHH | 49 | 0.0150 | 0.0113 | 0.2275 | 0.2425 | 69.5 | 95.6 | 5 |
| 79 | Hampton, Ky | OTT_TIT | Changeup | LHH | 116 | 0.0143 | 0.0142 | 0.2281 | 0.2425 | 68.4 | 95.0 | 6 |
| 86 | Hicks, Jackson | DOW_EAS1 | Changeup | LHH | 25 | 0.0141 | 0.0000 | 0.2284 | 0.2425 | 67.9 | 94.5 | 7 |
| 104 | Garcia, Jorge | SUS_COU1 | Changeup | LHH | 34 | 0.0131 | 0.0000 | 0.2294 | 0.2425 | 66.2 | 93.4 | 8 |
| 112 | Marynczak, Arlo | TRI_VAL | Changeup | LHH | 75 | 0.0126 | 0.0000 | 0.2298 | 0.2425 | 65.4 | 92.9 | 9 |
| 119 | Gartland, Chad | TRI_VAL | Changeup | LHH | 25 | 0.0124 | 0.0047 | 0.2301 | 0.2425 | 64.9 | 92.4 | 10 |
| 122 | Maietta, Dante | WIN_CIT29 | Changeup | LHH | 114 | 0.0123 | 0.0000 | 0.2301 | 0.2425 | 64.9 | 92.2 | 11 |
| 135 | Igami, Chikara | QUE_CAP | Changeup | LHH | 33 | 0.0119 | 0.0036 | 0.2305 | 0.2425 | 64.1 | 91.4 | 12 |
| 137 | O'Hanlon, Michael | WAS_WIL3 | Changeup | LHH | 31 | 0.0118 | 0.0002 | 0.2307 | 0.2425 | 63.9 | 91.3 | 13 |
| 139 | Albert, Wes | TRI_VAL | Changeup | LHH | 38 | 0.0118 | 0.0024 | 0.2307 | 0.2425 | 63.8 | 91.1 | 14 |
| 145 | Leak, Anthony | NEW_YOR13 | Changeup | LHH | 51 | 0.0116 | 0.0104 | 0.2309 | 0.2425 | 63.6 | 90.8 | 15 |

### Changeup vs RHH

| Rank | Pitcher | Team | Pitch Type | Batter Side | Pitches | Avg Adv | Median Adv | Grid xwOBA | League xwOBA | LS 20-80 | LS 0-100 | Type/Side Rank |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 101 | Culley, Wesley | NEW_YOR13 | Changeup | RHH | 36 | 0.0132 | 0.0081 | 0.2364 | 0.2496 | 66.4 | 93.6 | 1 |
| 170 | Alpern, Liam | FLO_Y'A | Changeup | RHH | 38 | 0.0110 | 0.0000 | 0.2386 | 0.2496 | 62.4 | 89.2 | 2 |
| 182 | Gollert, Harley | TRO_AIG | Changeup | RHH | 93 | 0.0107 | 0.0086 | 0.2389 | 0.2496 | 62.0 | 88.4 | 3 |
| 209 | Parra, Andres | LAK_ERI24 | Changeup | RHH | 41 | 0.0100 | 0.0021 | 0.2396 | 0.2496 | 60.7 | 86.6 | 4 |
| 221 | Gollert, Harley | QUE_CAP | Changeup | RHH | 38 | 0.0098 | 0.0016 | 0.2398 | 0.2496 | 60.4 | 85.9 | 5 |
| 230 | Campbell, Tyler | MIS_MUD | Changeup | RHH | 45 | 0.0096 | 0.0000 | 0.2400 | 0.2496 | 60.0 | 85.3 | 6 |
| 277 | Carroll, Jake | JOL_SLA | Changeup | RHH | 29 | 0.0090 | 0.0000 | 0.2406 | 0.2496 | 58.9 | 82.3 | 7 |
| 282 | Pindel, Buddie | SCH_BOO | Changeup | RHH | 25 | 0.0088 | 0.0085 | 0.2408 | 0.2496 | 58.6 | 82.0 | 8 |
| 293 | Galva, Claudio | GAT_GRI | Changeup | RHH | 64 | 0.0086 | 0.0019 | 0.2410 | 0.2496 | 58.3 | 81.3 | 9 |
| 308 | Thornton, Tyler | NEW_ENG23 | Changeup | RHH | 48 | 0.0084 | 0.0074 | 0.2412 | 0.2496 | 57.8 | 80.3 | 10 |
| 328 | Fry, Dale | LON_ISL22 | Changeup | RHH | 26 | 0.0082 | 0.0009 | 0.2414 | 0.2496 | 57.4 | 79.0 | 11 |
| 339 | Givens-Craig, Hayden | SUS_COU1 | Changeup | RHH | 35 | 0.0080 | 0.0000 | 0.2416 | 0.2496 | 57.2 | 78.3 | 12 |
| 343 | Barker, Alex | NEW_YOR13 | Changeup | RHH | 80 | 0.0080 | 0.0000 | 0.2416 | 0.2496 | 57.1 | 78.0 | 13 |
| 349 | Sanchez, Edwin | LAK_ERI24 | Changeup | RHH | 70 | 0.0080 | 0.0000 | 0.2417 | 0.2496 | 57.0 | 77.7 | 14 |
| 350 | Steinhauer, Ryan | NEW_JER6 | Changeup | RHH | 57 | 0.0079 | 0.0030 | 0.2417 | 0.2496 | 57.0 | 77.6 | 15 |

### Curveball vs LHH

| Rank | Pitcher | Team | Pitch Type | Batter Side | Pitches | Avg Adv | Median Adv | Grid xwOBA | League xwOBA | LS 20-80 | LS 0-100 | Type/Side Rank |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 160 | Carroll, Jake | JOL_SLA | Curveball | LHH | 29 | 0.0113 | 0.0033 | 0.2385 | 0.2498 | 63.0 | 89.8 | 1 |
| 331 | Shinn, Nathan | LAK_ERI24 | Curveball | LHH | 29 | 0.0081 | 0.0000 | 0.2417 | 0.2498 | 57.3 | 78.8 | 2 |
| 366 | Langrell, Connor | MIS_MUD | Curveball | LHH | 48 | 0.0077 | 0.0051 | 0.2420 | 0.2498 | 56.7 | 76.6 | 3 |
| 466 | Barker, Alex | NEW_YOR13 | Curveball | LHH | 28 | 0.0063 | 0.0000 | 0.2434 | 0.2498 | 54.2 | 70.2 | 4 |
| 518 | Morgan, Cooper | QUE_CAP | Curveball | LHH | 44 | 0.0059 | 0.0031 | 0.2439 | 0.2498 | 53.3 | 66.8 | 5 |
| 537 | Williams, Pierce | NEW_ENG23 | Curveball | LHH | 59 | 0.0057 | -0.0000 | 0.2441 | 0.2498 | 53.0 | 65.6 | 6 |
| 580 | Kassebaum, Torin | LON_ISL22 | Curveball | LHH | 25 | 0.0053 | 0.0048 | 0.2445 | 0.2498 | 52.3 | 62.8 | 7 |
| 621 | Fauci, Sonny | NEW_JER6 | Curveball | LHH | 30 | 0.0048 | 0.0000 | 0.2450 | 0.2498 | 51.5 | 60.2 | 8 |
| 630 | Peters, Garrett | NEW_YOR13 | Curveball | LHH | 87 | 0.0047 | -0.0000 | 0.2450 | 0.2498 | 51.3 | 59.6 | 9 |
| 639 | Foltz Jr., Michael | WAS_WIL3 | Curveball | LHH | 30 | 0.0047 | 0.0018 | 0.2451 | 0.2498 | 51.2 | 59.1 | 10 |
| 695 | Villalobos, Jonaiker | FLO_Y'A | Curveball | LHH | 49 | 0.0041 | 0.0000 | 0.2457 | 0.2498 | 50.2 | 55.5 | 11 |
| 703 | Rohde, Isaac | NEW_YOR13 | Curveball | LHH | 34 | 0.0041 | 0.0000 | 0.2457 | 0.2498 | 50.1 | 54.9 | 12 |
| 740 | Sanchez, Edwin | LAK_ERI24 | Curveball | LHH | 33 | 0.0037 | 0.0000 | 0.2461 | 0.2498 | 49.5 | 52.6 | 13 |
| 749 | Noriega, Branden | LAK_ERI24 | Curveball | LHH | 40 | 0.0036 | -0.0000 | 0.2461 | 0.2498 | 49.4 | 52.0 | 14 |
| 760 | Martzolf, Max | OTT_TIT | Curveball | LHH | 56 | 0.0035 | -0.0000 | 0.2462 | 0.2498 | 49.2 | 51.3 | 15 |

### Curveball vs RHH

| Rank | Pitcher | Team | Pitch Type | Batter Side | Pitches | Avg Adv | Median Adv | Grid xwOBA | League xwOBA | LS 20-80 | LS 0-100 | Type/Side Rank |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 54 | Hargrove, Dawson | LAK_ERI24 | Curveball | RHH | 26 | 0.0157 | 0.0145 | 0.2399 | 0.2555 | 70.8 | 96.6 | 1 |
| 90 | Garcia, Hector | WAS_WIL3 | Curveball | RHH | 27 | 0.0139 | 0.0105 | 0.2417 | 0.2555 | 67.6 | 94.3 | 2 |
| 113 | Simpson, Garret | EVA_OTT | Curveball | RHH | 37 | 0.0126 | 0.0009 | 0.2430 | 0.2555 | 65.2 | 92.8 | 3 |
| 141 | Maryniak, Connor | NEW_JER6 | Curveball | RHH | 59 | 0.0117 | 0.0048 | 0.2438 | 0.2555 | 63.7 | 91.0 | 4 |
| 237 | Lawson, Nathan | FLO_Y'A | Curveball | RHH | 30 | 0.0096 | 0.0004 | 0.2460 | 0.2555 | 59.9 | 84.9 | 5 |
| 243 | Allemann, Braeden | QUE_CAP | Curveball | RHH | 108 | 0.0095 | 0.0000 | 0.2460 | 0.2555 | 59.8 | 84.5 | 6 |
| 245 | Plumadore, Carson | WIN_CIT29 | Curveball | RHH | 30 | 0.0095 | 0.0076 | 0.2461 | 0.2555 | 59.8 | 84.3 | 7 |
| 249 | Majick, Eli | NEW_ENG23 | Curveball | RHH | 28 | 0.0094 | 0.0015 | 0.2461 | 0.2555 | 59.6 | 84.1 | 8 |
| 272 | Perdomo, Rafael | QUE_CAP | Curveball | RHH | 26 | 0.0090 | 0.0000 | 0.2465 | 0.2555 | 59.0 | 82.6 | 9 |
| 286 | Langrell, Connor | MIS_MUD | Curveball | RHH | 47 | 0.0087 | 0.0000 | 0.2468 | 0.2555 | 58.4 | 81.7 | 10 |
| 303 | Hohenstein, Liam | WIN_CIT29 | Curveball | RHH | 34 | 0.0085 | 0.0000 | 0.2471 | 0.2555 | 58.0 | 80.6 | 11 |
| 317 | Coles, Chad | WAS_WIL3 | Curveball | RHH | 43 | 0.0083 | 0.0008 | 0.2472 | 0.2555 | 57.7 | 79.7 | 12 |
| 354 | Moore, Kyle | SCH_BOO | Curveball | RHH | 73 | 0.0079 | 0.0000 | 0.2476 | 0.2555 | 56.9 | 77.3 | 13 |
| 370 | Hampton, Ky | OTT_TIT | Curveball | RHH | 33 | 0.0076 | 0.0000 | 0.2479 | 0.2555 | 56.4 | 76.3 | 14 |
| 375 | Henderson, Drew | DOW_EAS1 | Curveball | RHH | 149 | 0.0075 | 0.0000 | 0.2480 | 0.2555 | 56.3 | 76.0 | 15 |

### Cutter vs LHH

| Rank | Pitcher | Team | Pitch Type | Batter Side | Pitches | Avg Adv | Median Adv | Grid xwOBA | League xwOBA | LS 20-80 | LS 0-100 | Type/Side Rank |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 743 | McEvoy, Aidan | FLO_Y'A | Cutter | LHH | 36 | 0.0037 | 0.0000 | 0.2209 | 0.2247 | 49.5 | 52.4 | 1 |
| 808 | Cook, Cole | SCH_BOO | Cutter | LHH | 29 | 0.0031 | 0.0033 | 0.2216 | 0.2247 | 48.4 | 48.2 | 2 |
| 860 | Petschke, Ben | EVA_OTT | Cutter | LHH | 146 | 0.0027 | 0.0000 | 0.2220 | 0.2247 | 47.7 | 44.9 | 3 |
| 912 | Majick, Eli | NEW_ENG23 | Cutter | LHH | 26 | 0.0023 | 0.0025 | 0.2224 | 0.2247 | 46.9 | 41.5 | 4 |
| 932 | Parsons, Billy | SUS_COU1 | Cutter | LHH | 39 | 0.0021 | 0.0000 | 0.2226 | 0.2247 | 46.6 | 40.2 | 5 |
| 1004 | Sechrist, Zander | WAS_WIL3 | Cutter | LHH | 41 | 0.0015 | 0.0000 | 0.2232 | 0.2247 | 45.5 | 35.6 | 6 |
| 1054 | Salata, Derek | SCH_BOO | Cutter | LHH | 47 | 0.0011 | 0.0000 | 0.2235 | 0.2247 | 44.9 | 32.4 | 7 |
| 1070 | Binns, Malik | NEW_JER6 | Cutter | LHH | 34 | 0.0010 | 0.0000 | 0.2237 | 0.2247 | 44.7 | 31.4 | 8 |
| 1083 | Webster, Evan | FLO_Y'A | Cutter | LHH | 76 | 0.0009 | 0.0000 | 0.2237 | 0.2247 | 44.5 | 30.6 | 9 |
| 1084 | Langrell, Connor | MIS_MUD | Cutter | LHH | 100 | 0.0009 | 0.0009 | 0.2237 | 0.2247 | 44.5 | 30.5 | 10 |
| 1118 | Debban, Caleb | NEW_JER6 | Cutter | LHH | 58 | 0.0007 | 0.0000 | 0.2240 | 0.2247 | 44.1 | 28.3 | 11 |
| 1128 | Morgan, Marcus | JOL_SLA | Cutter | LHH | 38 | 0.0006 | 0.0000 | 0.2241 | 0.2247 | 43.9 | 27.7 | 12 |
| 1145 | Bell, Brendan | NEW_ENG23 | Cutter | LHH | 38 | 0.0004 | 0.0000 | 0.2243 | 0.2247 | 43.6 | 26.6 | 13 |
| 1165 | Smith, Jackson | MIS_MUD | Cutter | LHH | 39 | 0.0002 | 0.0000 | 0.2245 | 0.2247 | 43.2 | 25.3 | 14 |
| 1186 | Parks, Pavin | LAK_ERI24 | Cutter | LHH | 40 | 0.0000 | 0.0000 | 0.2246 | 0.2247 | 42.9 | 23.9 | 15 |

### Cutter vs RHH

| Rank | Pitcher | Team | Pitch Type | Batter Side | Pitches | Avg Adv | Median Adv | Grid xwOBA | League xwOBA | LS 20-80 | LS 0-100 | Type/Side Rank |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 385 | Good, Ty | GAT_GRI | Cutter | RHH | 31 | 0.0073 | 0.0035 | 0.2383 | 0.2457 | 55.9 | 75.4 | 1 |
| 408 | Wiltse, Ryan | EVA_OTT | Cutter | RHH | 34 | 0.0070 | 0.0000 | 0.2386 | 0.2457 | 55.4 | 73.9 | 2 |
| 415 | Ginn, Landon | WAS_WIL3 | Cutter | RHH | 56 | 0.0069 | 0.0000 | 0.2388 | 0.2457 | 55.2 | 73.4 | 3 |
| 472 | Baird, Dustin | MIS_MUD | Cutter | RHH | 30 | 0.0063 | 0.0003 | 0.2394 | 0.2457 | 54.0 | 69.8 | 4 |
| 494 | Lockhart, Gauge | LAK_ERI24 | Cutter | RHH | 30 | 0.0061 | 0.0109 | 0.2396 | 0.2457 | 53.7 | 68.4 | 5 |
| 498 | Jones, Breyln | NEW_JER6 | Cutter | RHH | 40 | 0.0060 | 0.0003 | 0.2396 | 0.2457 | 53.6 | 68.1 | 6 |
| 652 | Salata, Derek | SCH_BOO | Cutter | RHH | 64 | 0.0046 | 0.0000 | 0.2411 | 0.2457 | 51.0 | 58.2 | 7 |
| 667 | Bell, Brendan | NEW_ENG23 | Cutter | RHH | 25 | 0.0044 | 0.0000 | 0.2412 | 0.2457 | 50.8 | 57.3 | 8 |
| 668 | Majick, Eli | NEW_ENG23 | Cutter | RHH | 40 | 0.0044 | 0.0020 | 0.2412 | 0.2457 | 50.8 | 57.2 | 9 |
| 765 | Valdez, Alex | EVA_OTT | Cutter | RHH | 43 | 0.0035 | 0.0000 | 0.2422 | 0.2457 | 49.0 | 51.0 | 10 |
| 779 | Townes, Holland | SCH_BOO | Cutter | RHH | 26 | 0.0033 | 0.0002 | 0.2423 | 0.2457 | 48.8 | 50.1 | 11 |
| 803 | Petschke, Ben | EVA_OTT | Cutter | RHH | 103 | 0.0031 | 0.0004 | 0.2425 | 0.2457 | 48.5 | 48.5 | 12 |
| 813 | Smith, Jackson | MIS_MUD | Cutter | RHH | 53 | 0.0031 | 0.0000 | 0.2426 | 0.2457 | 48.3 | 47.9 | 13 |
| 829 | Parks, Pavin | LAK_ERI24 | Cutter | RHH | 94 | 0.0029 | 0.0000 | 0.2427 | 0.2457 | 48.1 | 46.9 | 14 |
| 850 | Thiels, Brenton | MIS_MUD | Cutter | RHH | 28 | 0.0028 | 0.0000 | 0.2429 | 0.2457 | 47.8 | 45.5 | 15 |

### Four-Seam vs LHH

| Rank | Pitcher | Team | Pitch Type | Batter Side | Pitches | Avg Adv | Median Adv | Grid xwOBA | League xwOBA | LS 20-80 | LS 0-100 | Type/Side Rank |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 50 | Davis, Tyler | WAS_WIL3 | Four-Seam | LHH | 48 | 0.0160 | 0.0177 | 0.2302 | 0.2462 | 71.4 | 96.9 | 1 |
| 52 | Wehrle, Tyler | WIN_CIT29 | Four-Seam | LHH | 80 | 0.0157 | 0.0178 | 0.2305 | 0.2462 | 70.9 | 96.7 | 2 |
| 65 | Brothers, Kellen | SUS_COU1 | Four-Seam | LHH | 134 | 0.0151 | 0.0163 | 0.2311 | 0.2462 | 69.8 | 95.9 | 3 |
| 80 | Parsons, Billy | SUS_COU1 | Four-Seam | LHH | 171 | 0.0143 | 0.0142 | 0.2319 | 0.2462 | 68.4 | 94.9 | 4 |
| 93 | Foster, Kobe | WAS_WIL3 | Four-Seam | LHH | 133 | 0.0138 | 0.0142 | 0.2324 | 0.2462 | 67.4 | 94.1 | 5 |
| 117 | Smith, Ben | NEW_ENG23 | Four-Seam | LHH | 40 | 0.0124 | 0.0122 | 0.2338 | 0.2462 | 65.0 | 92.6 | 6 |
| 128 | Herbert, Andrew | WAS_WIL3 | Four-Seam | LHH | 35 | 0.0122 | 0.0142 | 0.2341 | 0.2462 | 64.6 | 91.8 | 7 |
| 131 | Ferguson, Francis | QUE_CAP | Four-Seam | LHH | 51 | 0.0120 | 0.0142 | 0.2342 | 0.2462 | 64.3 | 91.7 | 8 |
| 144 | Fowler, Dalton | SUS_COU1 | Four-Seam | LHH | 43 | 0.0117 | 0.0131 | 0.2345 | 0.2462 | 63.7 | 90.8 | 9 |
| 164 | Zaffiro, Cole | SCH_BOO | Four-Seam | LHH | 85 | 0.0112 | 0.0131 | 0.2350 | 0.2462 | 62.9 | 89.5 | 10 |
| 180 | Alpern, Liam | FLO_Y'A | Four-Seam | LHH | 86 | 0.0107 | 0.0090 | 0.2355 | 0.2462 | 62.0 | 88.5 | 11 |
| 181 | Moore, Kyle | SCH_BOO | Four-Seam | LHH | 93 | 0.0107 | 0.0067 | 0.2355 | 0.2462 | 62.0 | 88.4 | 12 |
| 189 | O'Dell, Casey | JOL_SLA | Four-Seam | LHH | 35 | 0.0104 | 0.0078 | 0.2358 | 0.2462 | 61.5 | 87.9 | 13 |
| 197 | Lawson, Nathan | FLO_Y'A | Four-Seam | LHH | 38 | 0.0102 | 0.0117 | 0.2360 | 0.2462 | 61.1 | 87.4 | 14 |
| 202 | Kirby, Zach | WAS_WIL3 | Four-Seam | LHH | 163 | 0.0101 | 0.0109 | 0.2361 | 0.2462 | 60.9 | 87.1 | 15 |

### Four-Seam vs RHH

| Rank | Pitcher | Team | Pitch Type | Batter Side | Pitches | Avg Adv | Median Adv | Grid xwOBA | League xwOBA | LS 20-80 | LS 0-100 | Type/Side Rank |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 22 | Estrella, Noah | TRI_VAL | Four-Seam | RHH | 48 | 0.0192 | 0.0161 | 0.2225 | 0.2416 | 77.0 | 98.7 | 1 |
| 27 | Johnson, Preston | MIS_MUD | Four-Seam | RHH | 28 | 0.0180 | 0.0162 | 0.2236 | 0.2416 | 75.0 | 98.3 | 2 |
| 32 | Delvecchio, Dylan | LAK_ERI24 | Four-Seam | RHH | 25 | 0.0178 | 0.0209 | 0.2238 | 0.2416 | 74.5 | 98.0 | 3 |
| 33 | Mercado, Nelson | OTT_TIT | Four-Seam | RHH | 42 | 0.0175 | 0.0145 | 0.2241 | 0.2416 | 74.1 | 97.9 | 4 |
| 34 | Brothers, Kellen | SUS_COU1 | Four-Seam | RHH | 100 | 0.0174 | 0.0192 | 0.2242 | 0.2416 | 73.9 | 97.9 | 5 |
| 53 | Binns, Malik | NEW_JER6 | Four-Seam | RHH | 48 | 0.0157 | 0.0134 | 0.2259 | 0.2416 | 70.9 | 96.7 | 6 |
| 59 | Ginn, Landon | WAS_WIL3 | Four-Seam | RHH | 59 | 0.0154 | 0.0130 | 0.2262 | 0.2416 | 70.3 | 96.3 | 7 |
| 61 | Gardner, Sam | GAT_GRI | Four-Seam | RHH | 27 | 0.0152 | 0.0224 | 0.2264 | 0.2416 | 70.0 | 96.1 | 8 |
| 62 | Langhorne, Miles | SUS_COU1 | Four-Seam | RHH | 40 | 0.0152 | 0.0020 | 0.2264 | 0.2416 | 69.9 | 96.1 | 9 |
| 73 | Grounds, Jackson | DOW_EAS1 | Four-Seam | RHH | 48 | 0.0149 | 0.0126 | 0.2267 | 0.2416 | 69.3 | 95.4 | 10 |
| 74 | Chapple, Bronson | TRO_AIG | Four-Seam | RHH | 49 | 0.0147 | 0.0164 | 0.2269 | 0.2416 | 69.1 | 95.3 | 11 |
| 76 | Cohn, Cooper | NIU_HUS | Four-Seam | RHH | 38 | 0.0145 | 0.0070 | 0.2271 | 0.2416 | 68.7 | 95.2 | 12 |
| 77 | Kalisky, Jack | OTT_TIT | Four-Seam | RHH | 29 | 0.0144 | 0.0193 | 0.2272 | 0.2416 | 68.6 | 95.1 | 13 |
| 78 | O'Dell, Casey | JOL_SLA | Four-Seam | RHH | 37 | 0.0144 | 0.0224 | 0.2273 | 0.2416 | 68.4 | 95.1 | 14 |
| 82 | Albert, Wes | TRI_VAL | Four-Seam | RHH | 54 | 0.0141 | 0.0181 | 0.2275 | 0.2416 | 68.0 | 94.8 | 15 |

### Sinker vs LHH

| Rank | Pitcher | Team | Pitch Type | Batter Side | Pitches | Avg Adv | Median Adv | Grid xwOBA | League xwOBA | LS 20-80 | LS 0-100 | Type/Side Rank |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 103 | Sechrist, Zander | WAS_WIL3 | Sinker | LHH | 32 | 0.0132 | 0.0043 | 0.2511 | 0.2643 | 66.3 | 93.5 | 1 |
| 241 | Kelly, Aiden | TRI_VAL | Sinker | LHH | 51 | 0.0095 | 0.0000 | 0.2548 | 0.2643 | 59.8 | 84.6 | 2 |
| 268 | Mannering, Shawn | DOW_EAS1 | Sinker | LHH | 27 | 0.0091 | 0.0084 | 0.2552 | 0.2643 | 59.1 | 82.9 | 3 |
| 278 | Sabatine, Gino | TRI_VAL | Sinker | LHH | 36 | 0.0090 | 0.0004 | 0.2553 | 0.2643 | 58.8 | 82.2 | 4 |
| 289 | Aldeano, Austin | TRO_AIG | Sinker | LHH | 45 | 0.0087 | 0.0078 | 0.2556 | 0.2643 | 58.3 | 81.5 | 5 |
| 300 | Williams, Pierce | NEW_ENG23 | Sinker | LHH | 27 | 0.0085 | 0.0140 | 0.2558 | 0.2643 | 58.0 | 80.8 | 6 |
| 311 | Vecerka, Boris | QUE_CAP | Sinker | LHH | 113 | 0.0083 | 0.0075 | 0.2559 | 0.2643 | 57.7 | 80.1 | 7 |
| 315 | McCartney, Seth | MIS_MUD | Sinker | LHH | 67 | 0.0083 | 0.0007 | 0.2560 | 0.2643 | 57.7 | 79.8 | 8 |
| 332 | Gilleran, James | NEW_ENG23 | Sinker | LHH | 25 | 0.0081 | 0.0061 | 0.2562 | 0.2643 | 57.3 | 78.8 | 9 |
| 334 | Kines, Gunnar | JOL_SLA | Sinker | LHH | 73 | 0.0081 | 0.0144 | 0.2562 | 0.2643 | 57.3 | 78.6 | 10 |
| 360 | Allemann, Braeden | QUE_CAP | Sinker | LHH | 35 | 0.0078 | 0.0000 | 0.2565 | 0.2643 | 56.8 | 77.0 | 11 |
| 393 | Webster, Evan | FLO_Y'A | Sinker | LHH | 33 | 0.0072 | 0.0113 | 0.2571 | 0.2643 | 55.7 | 74.8 | 12 |
| 394 | Barreto, Brayhans | TRI_VAL | Sinker | LHH | 44 | 0.0072 | 0.0000 | 0.2571 | 0.2643 | 55.7 | 74.8 | 13 |
| 404 | Stuka, Ted | OTT_TIT | Sinker | LHH | 63 | 0.0072 | 0.0007 | 0.2571 | 0.2643 | 55.6 | 74.1 | 14 |
| 429 | Joven, Art | MIS_MUD | Sinker | LHH | 100 | 0.0067 | 0.0032 | 0.2576 | 0.2643 | 54.8 | 72.5 | 15 |

### Sinker vs RHH

| Rank | Pitcher | Team | Pitch Type | Batter Side | Pitches | Avg Adv | Median Adv | Grid xwOBA | League xwOBA | LS 20-80 | LS 0-100 | Type/Side Rank |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 108 | Leach, Landon | TRO_AIG | Sinker | RHH | 44 | 0.0127 | 0.0063 | 0.2416 | 0.2543 | 65.5 | 93.1 | 1 |
| 158 | Aldeano, Austin | TRO_AIG | Sinker | RHH | 25 | 0.0113 | 0.0177 | 0.2430 | 0.2543 | 63.0 | 89.9 | 2 |
| 165 | Donnan, Blake | FLO_Y'A | Sinker | RHH | 84 | 0.0112 | 0.0108 | 0.2431 | 0.2543 | 62.9 | 89.5 | 3 |
| 190 | Campbell, AJ | WIN_CIT29 | Sinker | RHH | 29 | 0.0104 | 0.0080 | 0.2439 | 0.2543 | 61.4 | 87.9 | 4 |
| 206 | Petschke, Ben | EVA_OTT | Sinker | RHH | 33 | 0.0101 | 0.0080 | 0.2443 | 0.2543 | 60.8 | 86.8 | 5 |
| 226 | Turner, Eric | JOL_SLA | Sinker | RHH | 45 | 0.0097 | 0.0067 | 0.2446 | 0.2543 | 60.1 | 85.6 | 6 |
| 234 | Glickstein, Aaron | SCH_BOO | Sinker | RHH | 60 | 0.0096 | 0.0148 | 0.2447 | 0.2543 | 59.9 | 85.0 | 7 |
| 238 | Vecerka, Boris | QUE_CAP | Sinker | RHH | 77 | 0.0096 | 0.0033 | 0.2448 | 0.2543 | 59.9 | 84.8 | 8 |
| 292 | De Jesus, Larry | DOW_EAS1 | Sinker | RHH | 30 | 0.0086 | 0.0076 | 0.2457 | 0.2543 | 58.3 | 81.3 | 9 |
| 306 | Ryan, Dillon | NEW_ENG23 | Sinker | RHH | 88 | 0.0084 | 0.0006 | 0.2459 | 0.2543 | 57.9 | 80.4 | 10 |
| 333 | Mannering, Shawn | DOW_EAS1 | Sinker | RHH | 32 | 0.0081 | 0.0001 | 0.2462 | 0.2543 | 57.3 | 78.7 | 11 |
| 341 | Hoeymans, Jack | GAT_GRI | Sinker | RHH | 35 | 0.0080 | 0.0016 | 0.2463 | 0.2543 | 57.1 | 78.2 | 12 |
| 357 | Cerda, Junior | EVA_OTT | Sinker | RHH | 39 | 0.0078 | 0.0014 | 0.2465 | 0.2543 | 56.8 | 77.2 | 13 |
| 363 | Primeaux, Parker | SUS_COU1 | Sinker | RHH | 28 | 0.0078 | 0.0181 | 0.2465 | 0.2543 | 56.7 | 76.8 | 14 |
| 371 | Colon, Jeffrey | TRO_AIG | Sinker | RHH | 26 | 0.0076 | 0.0000 | 0.2467 | 0.2543 | 56.4 | 76.3 | 15 |

### Slider vs LHH

| Rank | Pitcher | Team | Pitch Type | Batter Side | Pitches | Avg Adv | Median Adv | Grid xwOBA | League xwOBA | LS 20-80 | LS 0-100 | Type/Side Rank |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 98 | Smith, Ben | NEW_ENG23 | Slider | LHH | 33 | 0.0134 | 0.0000 | 0.2235 | 0.2369 | 66.7 | 93.8 | 1 |
| 129 | Potteiger, Jack | JOL_SLA | Slider | LHH | 30 | 0.0122 | 0.0054 | 0.2247 | 0.2369 | 64.5 | 91.8 | 2 |
| 167 | McEvoy, Aidan | FLO_Y'A | Slider | LHH | 65 | 0.0111 | 0.0000 | 0.2258 | 0.2369 | 62.6 | 89.3 | 3 |
| 174 | Barker, Alex | NEW_YOR13 | Slider | LHH | 59 | 0.0109 | 0.0000 | 0.2260 | 0.2369 | 62.2 | 88.9 | 4 |
| 179 | Campbell, Tyler | MIS_MUD | Slider | LHH | 80 | 0.0108 | 0.0088 | 0.2261 | 0.2369 | 62.0 | 88.6 | 5 |
| 184 | Alpern, Liam | FLO_Y'A | Slider | LHH | 38 | 0.0106 | 0.0000 | 0.2263 | 0.2369 | 61.8 | 88.3 | 6 |
| 188 | Harris, Everette | TRI_VAL | Slider | LHH | 29 | 0.0105 | 0.0047 | 0.2264 | 0.2369 | 61.5 | 88.0 | 7 |
| 192 | Maher, Adam | TRI_VAL | Slider | LHH | 47 | 0.0103 | 0.0000 | 0.2266 | 0.2369 | 61.3 | 87.7 | 8 |
| 193 | Armstrong, Andrew | NEW_YOR13 | Slider | LHH | 60 | 0.0103 | 0.0037 | 0.2266 | 0.2369 | 61.2 | 87.7 | 9 |
| 199 | Dima, Josh | GAT_GRI | Slider | LHH | 71 | 0.0102 | 0.0000 | 0.2267 | 0.2369 | 61.0 | 87.3 | 10 |
| 203 | Cook, Cole | SCH_BOO | Slider | LHH | 102 | 0.0101 | 0.0009 | 0.2268 | 0.2369 | 60.9 | 87.0 | 11 |
| 225 | Eckaus, David | EVA_OTT | Slider | LHH | 107 | 0.0097 | 0.0000 | 0.2272 | 0.2369 | 60.1 | 85.6 | 12 |
| 246 | Hensey, Rob | SUS_COU1 | Slider | LHH | 67 | 0.0095 | 0.0060 | 0.2274 | 0.2369 | 59.7 | 84.3 | 13 |
| 248 | Scott, Brandon | LAK_ERI24 | Slider | LHH | 64 | 0.0095 | 0.0000 | 0.2274 | 0.2369 | 59.7 | 84.1 | 14 |
| 257 | Milburn, Isaac | FLO_Y'A | Slider | LHH | 70 | 0.0093 | 0.0020 | 0.2276 | 0.2369 | 59.4 | 83.6 | 15 |

### Slider vs RHH

| Rank | Pitcher | Team | Pitch Type | Batter Side | Pitches | Avg Adv | Median Adv | Grid xwOBA | League xwOBA | LS 20-80 | LS 0-100 | Type/Side Rank |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | Gilleran, Jimmy | NEW_ENG23 | Slider | RHH | 54 | 0.0247 | 0.0236 | 0.2083 | 0.2330 | 80.0 | 100.0 | 1 |
| 2 | Wiltse, Ryan | EVA_OTT | Slider | RHH | 59 | 0.0246 | 0.0130 | 0.2084 | 0.2330 | 80.0 | 99.9 | 2 |
| 3 | Garcia, Hector | WAS_WIL3 | Slider | RHH | 36 | 0.0242 | 0.0138 | 0.2088 | 0.2330 | 80.0 | 99.9 | 3 |
| 4 | Thompson, Ross | SCH_BOO | Slider | RHH | 181 | 0.0240 | 0.0116 | 0.2091 | 0.2330 | 80.0 | 99.8 | 4 |
| 5 | Salata, Derek | SCH_BOO | Slider | RHH | 141 | 0.0227 | 0.0167 | 0.2103 | 0.2330 | 80.0 | 99.7 | 5 |
| 6 | Perez, Kelvin | WAS_WIL3 | Slider | RHH | 90 | 0.0227 | 0.0107 | 0.2103 | 0.2330 | 80.0 | 99.7 | 6 |
| 7 | Smith, Ethan | WIN_CIT29 | Slider | RHH | 30 | 0.0222 | 0.0024 | 0.2108 | 0.2330 | 80.0 | 99.6 | 7 |
| 8 | Vailes, Gage | GAT_GRI | Slider | RHH | 177 | 0.0216 | 0.0121 | 0.2114 | 0.2330 | 80.0 | 99.6 | 8 |
| 9 | Allemann, Braeden | QUE_CAP | Slider | RHH | 39 | 0.0214 | 0.0073 | 0.2116 | 0.2330 | 80.0 | 99.5 | 9 |
| 10 | Kirby, Zach | WAS_WIL3 | Slider | RHH | 126 | 0.0211 | 0.0083 | 0.2120 | 0.2330 | 80.0 | 99.4 | 10 |
| 11 | Blair, Davis | DOW_EAS1 | Slider | RHH | 61 | 0.0210 | 0.0130 | 0.2120 | 0.2330 | 80.0 | 99.4 | 11 |
| 12 | Belton, Hunter | MIS_MUD | Slider | RHH | 75 | 0.0210 | 0.0094 | 0.2121 | 0.2330 | 80.0 | 99.3 | 12 |
| 13 | Albert, Wes | TRI_VAL | Slider | RHH | 25 | 0.0209 | 0.0116 | 0.2121 | 0.2330 | 80.0 | 99.2 | 13 |
| 14 | Leak, Anthony | NEW_YOR13 | Slider | RHH | 131 | 0.0207 | 0.0110 | 0.2123 | 0.2330 | 79.8 | 99.2 | 14 |
| 15 | Helt, Robert | LAK_ERI24 | Slider | RHH | 137 | 0.0207 | 0.0042 | 0.2124 | 0.2330 | 79.6 | 99.1 | 15 |

### Splitter vs LHH

| Rank | Pitcher | Team | Pitch Type | Batter Side | Pitches | Avg Adv | Median Adv | Grid xwOBA | League xwOBA | LS 20-80 | LS 0-100 | Type/Side Rank |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 864 | Coles, Chad | WAS_WIL3 | Splitter | LHH | 31 | 0.0027 | 0.0000 | 0.2402 | 0.2429 | 47.6 | 44.6 | 1 |
| 920 | Thornton, Tyler | NEW_ENG23 | Splitter | LHH | 52 | 0.0022 | 0.0000 | 0.2407 | 0.2429 | 46.8 | 41.0 | 2 |
| 958 | Williams, Brian | MIS_MUD | Splitter | LHH | 49 | 0.0019 | 0.0000 | 0.2410 | 0.2429 | 46.2 | 38.6 | 3 |
| 964 | Perozzi, John | SUS_COU1 | Splitter | LHH | 32 | 0.0018 | 0.0000 | 0.2411 | 0.2429 | 46.2 | 38.2 | 4 |
| 979 | Eldred, Zach | NEW_ENG23 | Splitter | LHH | 34 | 0.0017 | 0.0000 | 0.2412 | 0.2429 | 45.8 | 37.2 | 5 |
| 995 | Salata, Derek | SCH_BOO | Splitter | LHH | 88 | 0.0016 | 0.0000 | 0.2414 | 0.2429 | 45.6 | 36.2 | 6 |
| 996 | Thompson, Ross | SCH_BOO | Splitter | LHH | 104 | 0.0016 | 0.0000 | 0.2414 | 0.2429 | 45.6 | 36.1 | 7 |
| 1012 | Andueza, Axel | DOW_EAS1 | Splitter | LHH | 44 | 0.0014 | 0.0000 | 0.2415 | 0.2429 | 45.4 | 35.1 | 8 |
| 1033 | Pindel, Buddie | SCH_BOO | Splitter | LHH | 52 | 0.0013 | 0.0000 | 0.2416 | 0.2429 | 45.1 | 33.8 | 9 |
| 1041 | Garcia, Hector | WAS_WIL3 | Splitter | LHH | 59 | 0.0012 | 0.0000 | 0.2417 | 0.2429 | 45.0 | 33.2 | 10 |
| 1087 | Orth, Harry | SCH_BOO | Splitter | LHH | 31 | 0.0009 | 0.0000 | 0.2420 | 0.2429 | 44.4 | 30.3 | 11 |
| 1130 | Parsons, Billy | SUS_COU1 | Splitter | LHH | 33 | 0.0006 | 0.0000 | 0.2424 | 0.2429 | 43.9 | 27.5 | 12 |
| 1139 | Vitas, Ben | JOL_SLA | Splitter | LHH | 68 | 0.0005 | 0.0000 | 0.2425 | 0.2429 | 43.7 | 27.0 | 13 |
| 1147 | Villers, Ian | QUE_CAP | Splitter | LHH | 39 | 0.0004 | 0.0000 | 0.2426 | 0.2429 | 43.5 | 26.4 | 14 |
| 1164 | Gilleran, Jimmy | NEW_ENG23 | Splitter | LHH | 26 | 0.0002 | 0.0000 | 0.2427 | 0.2429 | 43.2 | 25.4 | 15 |

### Splitter vs RHH

| Rank | Pitcher | Team | Pitch Type | Batter Side | Pitches | Avg Adv | Median Adv | Grid xwOBA | League xwOBA | LS 20-80 | LS 0-100 | Type/Side Rank |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 938 | Villers, Ian | QUE_CAP | Splitter | RHH | 25 | 0.0020 | 0.0000 | 0.2494 | 0.2514 | 46.5 | 39.9 | 1 |
| 1025 | Pindel, Buddie | SCH_BOO | Splitter | RHH | 30 | 0.0013 | 0.0000 | 0.2501 | 0.2514 | 45.2 | 34.3 | 2 |
| 1069 | Williams, Brian | MIS_MUD | Splitter | RHH | 37 | 0.0010 | 0.0000 | 0.2504 | 0.2514 | 44.7 | 31.5 | 3 |
| 1138 | Eldred, Zach | NEW_ENG23 | Splitter | RHH | 32 | 0.0005 | 0.0000 | 0.2510 | 0.2514 | 43.7 | 27.0 | 4 |
| 1153 | Shears, Tanner | SCH_BOO | Splitter | RHH | 30 | 0.0003 | 0.0000 | 0.2511 | 0.2514 | 43.4 | 26.1 | 5 |
| 1267 | Vitas, Ben | JOL_SLA | Splitter | RHH | 30 | -0.0008 | 0.0000 | 0.2522 | 0.2514 | 41.5 | 18.7 | 6 |
| 1348 | MacMillan, Blake | TRO_AIG | Splitter | RHH | 29 | -0.0016 | 0.0000 | 0.2530 | 0.2514 | 40.0 | 13.5 | 7 |
| 1386 | Thornton, Tyler | NEW_ENG23 | Splitter | RHH | 36 | -0.0021 | 0.0000 | 0.2535 | 0.2514 | 39.2 | 11.1 | 8 |
| 1415 | Nakata, Yuto | QUE_CAP | Splitter | RHH | 28 | -0.0025 | 0.0000 | 0.2539 | 0.2514 | 38.4 | 9.2 | 9 |
| 1419 | Thompson, Ross | SCH_BOO | Splitter | RHH | 28 | -0.0026 | 0.0000 | 0.2540 | 0.2514 | 38.3 | 9.0 | 10 |

### Sweeper vs RHH

| Rank | Pitcher | Team | Pitch Type | Batter Side | Pitches | Avg Adv | Median Adv | Grid xwOBA | League xwOBA | LS 20-80 | LS 0-100 | Type/Side Rank |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1179 | Simpson, Garret | EVA_OTT | Sweeper | RHH | 32 | 0.0001 | 0.0000 | 0.1946 | 0.1946 | 43.0 | 24.4 | 1 |
| 1195 | Cerda, Junior | EVA_OTT | Sweeper | RHH | 30 | -0.0000 | 0.0000 | 0.1947 | 0.1946 | 42.8 | 23.4 | 2 |
