# Location Score Report

- Pitch input file: `data\processed\2026-data-with-woba-xwoba.parquet`
- Location grid input file: `data\processed\location_value_grid.csv`
- Output file: `data\processed\location_scores.csv`
- Assigned pitch rows: 154,654
- Qualified pitcher + pitch type + batter side rows: 1,758
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
| 1 | Garcia, Hector | WAS_WIL3 | Slider | RHH | 36 | 0.0270 | 0.0212 | 0.2044 | 0.2314 | 80.0 | 100.0 | 1 |
| 2 | Perez, Kelvin | WAS_WIL3 | Slider | RHH | 103 | 0.0251 | 0.0265 | 0.2063 | 0.2314 | 80.0 | 99.9 | 2 |
| 3 | Wiltse, Ryan | EVA_OTT | Slider | RHH | 60 | 0.0248 | 0.0186 | 0.2066 | 0.2314 | 80.0 | 99.9 | 3 |
| 4 | Gilleran, Jimmy | NEW_ENG23 | Slider | RHH | 90 | 0.0244 | 0.0244 | 0.2070 | 0.2314 | 80.0 | 99.8 | 4 |
| 5 | Salata, Derek | SCH_BOO | Slider | RHH | 163 | 0.0236 | 0.0196 | 0.2078 | 0.2314 | 80.0 | 99.8 | 5 |
| 6 | Smith, Ethan | WIN_CIT29 | Slider | RHH | 30 | 0.0235 | 0.0101 | 0.2079 | 0.2314 | 80.0 | 99.7 | 6 |
| 7 | Perdomo, Rafael | QUE_CAP | Slider | RHH | 46 | 0.0232 | 0.0145 | 0.2082 | 0.2314 | 80.0 | 99.7 | 7 |
| 8 | Albert, Wes | TRI_VAL | Slider | RHH | 25 | 0.0230 | 0.0152 | 0.2084 | 0.2314 | 80.0 | 99.6 | 8 |
| 9 | Blair, Davis | DOW_EAS1 | Slider | RHH | 61 | 0.0224 | 0.0089 | 0.2090 | 0.2314 | 80.0 | 99.5 | 9 |
| 10 | Thompson, Ross | SCH_BOO | Slider | RHH | 196 | 0.0223 | 0.0089 | 0.2091 | 0.2314 | 80.0 | 99.5 | 10 |
| 11 | Kirby, Zach | WAS_WIL3 | Slider | RHH | 126 | 0.0222 | 0.0115 | 0.2092 | 0.2314 | 80.0 | 99.4 | 11 |
| 12 | Belton, Hunter | MIS_MUD | Slider | RHH | 75 | 0.0220 | 0.0138 | 0.2094 | 0.2314 | 80.0 | 99.4 | 12 |
| 13 | Morrissey, Joe | EVA_OTT | Slider | RHH | 45 | 0.0219 | 0.0186 | 0.2095 | 0.2314 | 79.9 | 99.3 | 13 |
| 14 | Vailes, Gage | GAT_GRI | Slider | RHH | 220 | 0.0217 | 0.0152 | 0.2097 | 0.2314 | 79.5 | 99.3 | 14 |
| 15 | Cameron, Wyatt | SCH_BOO | Slider | RHH | 50 | 0.0215 | 0.0000 | 0.2099 | 0.2314 | 79.1 | 99.2 | 15 |
| 16 | Nova, Fraynel | LAK_ERI24 | Slider | RHH | 145 | 0.0215 | 0.0186 | 0.2099 | 0.2314 | 79.1 | 99.1 | 16 |
| 17 | Finarelli, Nick | LON_ISL22 | Slider | RHH | 31 | 0.0210 | 0.0016 | 0.2104 | 0.2314 | 78.4 | 99.1 | 17 |
| 18 | O'Hanlon, Michael | WAS_WIL3 | Slider | RHH | 51 | 0.0209 | 0.0016 | 0.2105 | 0.2314 | 78.2 | 99.0 | 18 |
| 19 | Encarnacion, J.D. | EVA_OTT | Changeup | LHH | 28 | 0.0205 | 0.0169 | 0.2213 | 0.2418 | 77.4 | 99.0 | 1 |
| 20 | Allemann, Braeden | QUE_CAP | Slider | RHH | 65 | 0.0202 | 0.0077 | 0.2112 | 0.2314 | 76.9 | 98.9 | 19 |
| 21 | Hagan, Jack | DOW_EAS1 | Slider | RHH | 129 | 0.0200 | 0.0138 | 0.2114 | 0.2314 | 76.7 | 98.9 | 20 |
| 22 | Helt, Robert | LAK_ERI24 | Slider | RHH | 144 | 0.0200 | 0.0008 | 0.2114 | 0.2314 | 76.6 | 98.8 | 21 |
| 23 | Moore, Kyle | SCH_BOO | Slider | RHH | 31 | 0.0199 | 0.0138 | 0.2115 | 0.2314 | 76.5 | 98.7 | 22 |
| 24 | Leak, Anthony | NEW_YOR13 | Slider | RHH | 166 | 0.0199 | 0.0143 | 0.2115 | 0.2314 | 76.5 | 98.7 | 23 |
| 25 | Mercado, Nelson | OTT_TIT | Four-Seam | RHH | 42 | 0.0199 | 0.0177 | 0.2189 | 0.2388 | 76.4 | 98.6 | 1 |
| 26 | Willeman, Landon | EVA_OTT | Slider | RHH | 70 | 0.0199 | 0.0060 | 0.2115 | 0.2314 | 76.3 | 98.6 | 24 |
| 27 | McCartney, Seth | MIS_MUD | Slider | RHH | 36 | 0.0197 | 0.0008 | 0.2117 | 0.2314 | 76.1 | 98.5 | 25 |
| 28 | Vilchez, Michael | OTT_TIT | Slider | RHH | 81 | 0.0197 | 0.0159 | 0.2117 | 0.2314 | 76.1 | 98.5 | 26 |
| 29 | Allemann, Braeden | QUE_CAP | Changeup | LHH | 32 | 0.0196 | 0.0121 | 0.2222 | 0.2418 | 75.9 | 98.4 | 2 |
| 30 | Hargrove, Dawson | LAK_ERI24 | Curveball | RHH | 29 | 0.0196 | 0.0132 | 0.2330 | 0.2526 | 75.9 | 98.4 | 1 |

## Top Location Scores by Pitch Type and Batter Side

### Changeup vs LHH

| Rank | Pitcher | Team | Pitch Type | Batter Side | Pitches | Avg Adv | Median Adv | Grid xwOBA | League xwOBA | LS 20-80 | LS 0-100 | Type/Side Rank |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 19 | Encarnacion, J.D. | EVA_OTT | Changeup | LHH | 28 | 0.0205 | 0.0169 | 0.2213 | 0.2418 | 77.4 | 99.0 | 1 |
| 29 | Allemann, Braeden | QUE_CAP | Changeup | LHH | 32 | 0.0196 | 0.0121 | 0.2222 | 0.2418 | 75.9 | 98.4 | 2 |
| 68 | Smith, Jackson | MIS_MUD | Changeup | LHH | 73 | 0.0164 | 0.0110 | 0.2254 | 0.2418 | 70.3 | 96.2 | 3 |
| 75 | Voytko, Fawster | TRO_AIG | Changeup | LHH | 41 | 0.0160 | 0.0118 | 0.2258 | 0.2418 | 69.5 | 95.8 | 4 |
| 83 | Hicks, Jackson | DOW_EAS1 | Changeup | LHH | 25 | 0.0156 | 0.0081 | 0.2261 | 0.2418 | 68.9 | 95.3 | 5 |
| 100 | Dill, Austin | TRI_VAL | Changeup | LHH | 118 | 0.0151 | 0.0104 | 0.2267 | 0.2418 | 68.0 | 94.4 | 6 |
| 120 | Hampton, Ky | OTT_TIT | Changeup | LHH | 138 | 0.0140 | 0.0111 | 0.2277 | 0.2418 | 66.2 | 93.2 | 7 |
| 126 | Albert, Wes | TRI_VAL | Changeup | LHH | 38 | 0.0138 | 0.0053 | 0.2279 | 0.2418 | 65.8 | 92.9 | 8 |
| 129 | Garcia, Jorge | SUS_COU1 | Changeup | LHH | 35 | 0.0136 | 0.0026 | 0.2281 | 0.2418 | 65.5 | 92.7 | 9 |
| 138 | Escobar, Anthony | TRO_AIG | Changeup | LHH | 142 | 0.0133 | 0.0052 | 0.2284 | 0.2418 | 65.0 | 92.2 | 10 |
| 150 | Noble, Nick | FDU_KNI | Changeup | LHH | 46 | 0.0131 | 0.0095 | 0.2286 | 0.2418 | 64.6 | 91.5 | 11 |
| 152 | O'Hanlon, Michael | WAS_WIL3 | Changeup | LHH | 35 | 0.0130 | 0.0040 | 0.2287 | 0.2418 | 64.4 | 91.4 | 12 |
| 164 | Maietta, Dante | WIN_CIT29 | Changeup | LHH | 150 | 0.0126 | 0.0042 | 0.2292 | 0.2418 | 63.7 | 90.7 | 13 |
| 167 | Igami, Chikara | QUE_CAP | Changeup | LHH | 33 | 0.0126 | 0.0083 | 0.2292 | 0.2418 | 63.6 | 90.6 | 14 |
| 175 | Hocom, Quinn | TRI_VAL | Changeup | LHH | 74 | 0.0123 | 0.0004 | 0.2294 | 0.2418 | 63.2 | 90.1 | 15 |

### Changeup vs RHH

| Rank | Pitcher | Team | Pitch Type | Batter Side | Pitches | Avg Adv | Median Adv | Grid xwOBA | League xwOBA | LS 20-80 | LS 0-100 | Type/Side Rank |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 98 | Walsh, John | MIS_MUD | Changeup | RHH | 35 | 0.0152 | 0.0129 | 0.2326 | 0.2478 | 68.1 | 94.5 | 1 |
| 119 | Culley, Wesley | NEW_YOR13 | Changeup | RHH | 36 | 0.0140 | 0.0106 | 0.2337 | 0.2478 | 66.2 | 93.3 | 2 |
| 149 | Smith, Ben | NEW_ENG23 | Changeup | RHH | 43 | 0.0131 | 0.0082 | 0.2346 | 0.2478 | 64.6 | 91.6 | 3 |
| 159 | Carroll, Jake | JOL_SLA | Changeup | RHH | 31 | 0.0128 | 0.0025 | 0.2350 | 0.2478 | 64.0 | 91.0 | 4 |
| 258 | Steinhauer, Ryan | NEW_JER6 | Changeup | RHH | 57 | 0.0108 | 0.0068 | 0.2370 | 0.2478 | 60.6 | 85.4 | 5 |
| 261 | Alpern, Liam | FLO_Y'A | Changeup | RHH | 38 | 0.0108 | 0.0041 | 0.2370 | 0.2478 | 60.5 | 85.2 | 6 |
| 290 | Parra, Andres | LAK_ERI24 | Changeup | RHH | 41 | 0.0102 | 0.0001 | 0.2376 | 0.2478 | 59.5 | 83.6 | 7 |
| 332 | Galva, Claudio | GAT_GRI | Changeup | RHH | 86 | 0.0097 | 0.0049 | 0.2381 | 0.2478 | 58.6 | 81.2 | 8 |
| 358 | Pindel, Buddie | SCH_BOO | Changeup | RHH | 27 | 0.0093 | 0.0020 | 0.2385 | 0.2478 | 57.9 | 79.7 | 9 |
| 365 | Gollert, Harley | QUE_CAP | Changeup | RHH | 38 | 0.0092 | 0.0000 | 0.2386 | 0.2478 | 57.8 | 79.3 | 10 |
| 393 | Gollert, Harley | TRO_AIG | Changeup | RHH | 117 | 0.0088 | 0.0025 | 0.2389 | 0.2478 | 57.2 | 77.7 | 11 |
| 399 | Fry, Dale | LON_ISL22 | Changeup | RHH | 26 | 0.0088 | 0.0010 | 0.2389 | 0.2478 | 57.1 | 77.4 | 12 |
| 432 | Givens-Craig, Hayden | SUS_COU1 | Changeup | RHH | 35 | 0.0084 | 0.0000 | 0.2393 | 0.2478 | 56.4 | 75.5 | 13 |
| 445 | Barker, Alex | NEW_YOR13 | Changeup | RHH | 117 | 0.0083 | 0.0001 | 0.2395 | 0.2478 | 56.2 | 74.7 | 14 |
| 450 | Zentko, Dylan | EVA_OTT | Changeup | RHH | 57 | 0.0082 | 0.0000 | 0.2395 | 0.2478 | 56.1 | 74.5 | 15 |

### Curveball vs LHH

| Rank | Pitcher | Team | Pitch Type | Batter Side | Pitches | Avg Adv | Median Adv | Grid xwOBA | League xwOBA | LS 20-80 | LS 0-100 | Type/Side Rank |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 274 | Carroll, Jake | JOL_SLA | Curveball | LHH | 35 | 0.0105 | 0.0000 | 0.2336 | 0.2441 | 60.1 | 84.5 | 1 |
| 366 | Shinn, Nathan | LAK_ERI24 | Curveball | LHH | 29 | 0.0092 | 0.0000 | 0.2349 | 0.2441 | 57.8 | 79.2 | 2 |
| 603 | Martzolf, Max | OTT_TIT | Curveball | LHH | 56 | 0.0064 | 0.0000 | 0.2377 | 0.2441 | 52.8 | 65.8 | 3 |
| 647 | Williams, Pierce | NEW_ENG23 | Curveball | LHH | 65 | 0.0059 | 0.0000 | 0.2382 | 0.2441 | 52.1 | 63.3 | 4 |
| 669 | Barker, Alex | NEW_YOR13 | Curveball | LHH | 33 | 0.0057 | 0.0000 | 0.2384 | 0.2441 | 51.8 | 62.0 | 5 |
| 673 | Langrell, Connor | MIS_MUD | Curveball | LHH | 55 | 0.0057 | 0.0000 | 0.2384 | 0.2441 | 51.7 | 61.8 | 6 |
| 730 | Morgan, Cooper | QUE_CAP | Curveball | LHH | 56 | 0.0052 | 0.0000 | 0.2389 | 0.2441 | 50.8 | 58.5 | 7 |
| 751 | Cameron, Wyatt | SCH_BOO | Curveball | LHH | 47 | 0.0050 | 0.0000 | 0.2391 | 0.2441 | 50.5 | 57.3 | 8 |
| 789 | Gollert, Harley | TRO_AIG | Curveball | LHH | 28 | 0.0047 | 0.0000 | 0.2394 | 0.2441 | 49.9 | 55.2 | 9 |
| 800 | Baker, Luke | EVA_OTT | Curveball | LHH | 37 | 0.0046 | 0.0000 | 0.2395 | 0.2441 | 49.7 | 54.6 | 10 |
| 817 | Foltz Jr., Michael | WAS_WIL3 | Curveball | LHH | 47 | 0.0044 | 0.0000 | 0.2397 | 0.2441 | 49.5 | 53.6 | 11 |
| 828 | Kalisky, Jack | OTT_TIT | Curveball | LHH | 25 | 0.0043 | 0.0000 | 0.2398 | 0.2441 | 49.3 | 53.0 | 12 |
| 833 | Nova, Fraynel | LAK_ERI24 | Curveball | LHH | 25 | 0.0043 | 0.0000 | 0.2398 | 0.2441 | 49.2 | 52.7 | 13 |
| 838 | Hocom, Quinn | TRI_VAL | Curveball | LHH | 41 | 0.0043 | 0.0000 | 0.2398 | 0.2441 | 49.2 | 52.4 | 14 |
| 843 | Figueredo, Kevin | WIN_CIT29 | Curveball | LHH | 45 | 0.0042 | 0.0000 | 0.2399 | 0.2441 | 49.1 | 52.1 | 15 |

### Curveball vs RHH

| Rank | Pitcher | Team | Pitch Type | Batter Side | Pitches | Avg Adv | Median Adv | Grid xwOBA | League xwOBA | LS 20-80 | LS 0-100 | Type/Side Rank |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 30 | Hargrove, Dawson | LAK_ERI24 | Curveball | RHH | 29 | 0.0196 | 0.0132 | 0.2330 | 0.2526 | 75.9 | 98.4 | 1 |
| 108 | Simpson, Garret | EVA_OTT | Curveball | RHH | 55 | 0.0146 | 0.0000 | 0.2380 | 0.2526 | 67.1 | 93.9 | 2 |
| 140 | Kalisky, Jack | OTT_TIT | Curveball | RHH | 41 | 0.0133 | 0.0034 | 0.2393 | 0.2526 | 64.9 | 92.1 | 3 |
| 156 | Garcia, Hector | WAS_WIL3 | Curveball | RHH | 27 | 0.0129 | 0.0099 | 0.2397 | 0.2526 | 64.3 | 91.2 | 4 |
| 195 | Perdomo, Rafael | QUE_CAP | Curveball | RHH | 26 | 0.0118 | 0.0004 | 0.2408 | 0.2526 | 62.4 | 89.0 | 5 |
| 202 | Long, Jalon | NEW_YOR13 | Curveball | RHH | 26 | 0.0117 | 0.0011 | 0.2409 | 0.2526 | 62.1 | 88.6 | 6 |
| 236 | Allemann, Braeden | QUE_CAP | Curveball | RHH | 122 | 0.0112 | 0.0004 | 0.2414 | 0.2526 | 61.3 | 86.6 | 7 |
| 245 | Coles, Chad | WAS_WIL3 | Curveball | RHH | 45 | 0.0111 | 0.0024 | 0.2415 | 0.2526 | 61.1 | 86.1 | 8 |
| 247 | Brothers, Kellen | SUS_COU1 | Curveball | RHH | 25 | 0.0111 | 0.0000 | 0.2415 | 0.2526 | 61.0 | 86.0 | 9 |
| 295 | Ginn, Landon | WAS_WIL3 | Curveball | RHH | 26 | 0.0102 | 0.0000 | 0.2424 | 0.2526 | 59.5 | 83.3 | 10 |
| 299 | Hohenstein, Liam | WIN_CIT29 | Curveball | RHH | 58 | 0.0100 | 0.0007 | 0.2426 | 0.2526 | 59.3 | 83.0 | 11 |
| 326 | Langrell, Connor | MIS_MUD | Curveball | RHH | 59 | 0.0098 | 0.0000 | 0.2428 | 0.2526 | 58.8 | 81.5 | 12 |
| 328 | House, Tristan | MIS_MUD | Curveball | RHH | 28 | 0.0098 | 0.0000 | 0.2428 | 0.2526 | 58.8 | 81.4 | 13 |
| 343 | Majick, Eli | NEW_ENG23 | Curveball | RHH | 34 | 0.0095 | 0.0000 | 0.2431 | 0.2526 | 58.4 | 80.5 | 14 |
| 345 | Lawson, Nathan | FLO_Y'A | Curveball | RHH | 31 | 0.0095 | 0.0000 | 0.2431 | 0.2526 | 58.3 | 80.4 | 15 |

### Cutter vs LHH

| Rank | Pitcher | Team | Pitch Type | Batter Side | Pitches | Avg Adv | Median Adv | Grid xwOBA | League xwOBA | LS 20-80 | LS 0-100 | Type/Side Rank |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 856 | McEvoy, Aidan | FLO_Y'A | Cutter | LHH | 36 | 0.0041 | 0.0000 | 0.2224 | 0.2264 | 48.8 | 51.4 | 1 |
| 912 | Majick, Eli | NEW_ENG23 | Cutter | LHH | 26 | 0.0036 | 0.0026 | 0.2228 | 0.2264 | 48.1 | 48.2 | 2 |
| 928 | Cook, Cole | SCH_BOO | Cutter | LHH | 33 | 0.0035 | 0.0012 | 0.2229 | 0.2264 | 47.9 | 47.3 | 3 |
| 1014 | Petschke, Ben | EVA_OTT | Cutter | LHH | 150 | 0.0029 | 0.0000 | 0.2236 | 0.2264 | 46.8 | 42.4 | 4 |
| 1100 | Jones, Breyln | NEW_JER6 | Cutter | LHH | 25 | 0.0023 | 0.0000 | 0.2242 | 0.2264 | 45.7 | 37.5 | 5 |
| 1126 | Catrambone, Ben | JOL_SLA | Cutter | LHH | 25 | 0.0021 | 0.0000 | 0.2243 | 0.2264 | 45.5 | 36.0 | 6 |
| 1153 | Parsons, Billy | SUS_COU1 | Cutter | LHH | 39 | 0.0019 | 0.0000 | 0.2246 | 0.2264 | 45.1 | 34.5 | 7 |
| 1196 | Sechrist, Zander | WAS_WIL3 | Cutter | LHH | 41 | 0.0016 | 0.0000 | 0.2249 | 0.2264 | 44.5 | 32.0 | 8 |
| 1203 | Campbell, Tyler | MIS_MUD | Cutter | LHH | 56 | 0.0015 | 0.0000 | 0.2249 | 0.2264 | 44.5 | 31.6 | 9 |
| 1216 | Moore, Kyle | SCH_BOO | Cutter | LHH | 35 | 0.0015 | 0.0000 | 0.2250 | 0.2264 | 44.3 | 30.9 | 10 |
| 1260 | Webster, Evan | FLO_Y'A | Cutter | LHH | 95 | 0.0012 | 0.0000 | 0.2253 | 0.2264 | 43.8 | 28.4 | 11 |
| 1279 | Campbell, AJ | WIN_CIT29 | Cutter | LHH | 31 | 0.0011 | 0.0000 | 0.2254 | 0.2264 | 43.6 | 27.3 | 12 |
| 1305 | Langrell, Connor | MIS_MUD | Cutter | LHH | 111 | 0.0009 | 0.0000 | 0.2255 | 0.2264 | 43.4 | 25.8 | 13 |
| 1308 | Smith, Jackson | MIS_MUD | Cutter | LHH | 42 | 0.0009 | 0.0006 | 0.2256 | 0.2264 | 43.3 | 25.7 | 14 |
| 1336 | Bell, Brendan | NEW_ENG23 | Cutter | LHH | 46 | 0.0006 | 0.0000 | 0.2259 | 0.2264 | 42.8 | 24.1 | 15 |

### Cutter vs RHH

| Rank | Pitcher | Team | Pitch Type | Batter Side | Pitches | Avg Adv | Median Adv | Grid xwOBA | League xwOBA | LS 20-80 | LS 0-100 | Type/Side Rank |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 469 | Jones, Breyln | NEW_JER6 | Cutter | RHH | 44 | 0.0078 | 0.0009 | 0.2306 | 0.2384 | 55.3 | 73.4 | 1 |
| 477 | Bell, Brendan | NEW_ENG23 | Cutter | RHH | 39 | 0.0077 | 0.0070 | 0.2307 | 0.2384 | 55.2 | 72.9 | 2 |
| 571 | Good, Ty | GAT_GRI | Cutter | RHH | 40 | 0.0067 | 0.0000 | 0.2316 | 0.2384 | 53.5 | 67.6 | 3 |
| 600 | Ginn, Landon | WAS_WIL3 | Cutter | RHH | 61 | 0.0064 | 0.0000 | 0.2320 | 0.2384 | 52.9 | 65.9 | 4 |
| 706 | Lockhart, Gauge | LAK_ERI24 | Cutter | RHH | 59 | 0.0054 | 0.0050 | 0.2330 | 0.2384 | 51.2 | 59.9 | 5 |
| 725 | Wiltse, Ryan | EVA_OTT | Cutter | RHH | 47 | 0.0052 | 0.0000 | 0.2332 | 0.2384 | 50.9 | 58.8 | 6 |
| 729 | Baird, Dustin | MIS_MUD | Cutter | RHH | 30 | 0.0052 | 0.0000 | 0.2332 | 0.2384 | 50.8 | 58.6 | 7 |
| 771 | Salata, Derek | SCH_BOO | Cutter | RHH | 72 | 0.0047 | 0.0000 | 0.2336 | 0.2384 | 50.0 | 56.2 | 8 |
| 888 | Majick, Eli | NEW_ENG23 | Cutter | RHH | 42 | 0.0038 | 0.0013 | 0.2346 | 0.2384 | 48.4 | 49.5 | 9 |
| 955 | Parks, Pavin | LAK_ERI24 | Cutter | RHH | 94 | 0.0033 | 0.0000 | 0.2351 | 0.2384 | 47.5 | 45.7 | 10 |
| 997 | Townes, Holland | SCH_BOO | Cutter | RHH | 35 | 0.0030 | 0.0019 | 0.2354 | 0.2384 | 46.9 | 43.3 | 11 |
| 1009 | Thiels, Brenton | MIS_MUD | Cutter | RHH | 28 | 0.0029 | 0.0000 | 0.2355 | 0.2384 | 46.8 | 42.7 | 12 |
| 1025 | Correa, Nelvin | QUE_CAP | Cutter | RHH | 51 | 0.0028 | 0.0000 | 0.2356 | 0.2384 | 46.7 | 41.8 | 13 |
| 1059 | Binns, Malik | NEW_JER6 | Cutter | RHH | 54 | 0.0026 | 0.0000 | 0.2358 | 0.2384 | 46.2 | 39.8 | 14 |
| 1060 | Valdez, Alex | EVA_OTT | Cutter | RHH | 52 | 0.0026 | 0.0000 | 0.2358 | 0.2384 | 46.2 | 39.8 | 15 |

### Four-Seam vs LHH

| Rank | Pitcher | Team | Pitch Type | Batter Side | Pitches | Avg Adv | Median Adv | Grid xwOBA | League xwOBA | LS 20-80 | LS 0-100 | Type/Side Rank |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 36 | Masick, Jason | NEW_YOR13 | Four-Seam | LHH | 34 | 0.0189 | 0.0119 | 0.2256 | 0.2445 | 74.6 | 98.0 | 1 |
| 46 | Wehrle, Tyler | WIN_CIT29 | Four-Seam | LHH | 80 | 0.0177 | 0.0229 | 0.2268 | 0.2445 | 72.5 | 97.4 | 2 |
| 57 | Brothers, Kellen | SUS_COU1 | Four-Seam | LHH | 181 | 0.0170 | 0.0196 | 0.2275 | 0.2445 | 71.4 | 96.8 | 3 |
| 62 | Davis, Tyler | WAS_WIL3 | Four-Seam | LHH | 48 | 0.0165 | 0.0200 | 0.2280 | 0.2445 | 70.5 | 96.5 | 4 |
| 73 | Parsons, Billy | SUS_COU1 | Four-Seam | LHH | 171 | 0.0161 | 0.0167 | 0.2284 | 0.2445 | 69.8 | 95.9 | 5 |
| 115 | Jones, Breyln | NEW_JER6 | Four-Seam | LHH | 28 | 0.0143 | 0.0000 | 0.2302 | 0.2445 | 66.7 | 93.5 | 6 |
| 122 | Agosto, Justus | TRI_VAL | Four-Seam | LHH | 45 | 0.0140 | 0.0084 | 0.2305 | 0.2445 | 66.1 | 93.1 | 7 |
| 131 | Ferguson, Francis | QUE_CAP | Four-Seam | LHH | 51 | 0.0136 | 0.0139 | 0.2309 | 0.2445 | 65.4 | 92.6 | 8 |
| 136 | Smith, Ben | NEW_ENG23 | Four-Seam | LHH | 45 | 0.0134 | 0.0109 | 0.2311 | 0.2445 | 65.1 | 92.3 | 9 |
| 137 | Herbert, Andrew | WAS_WIL3 | Four-Seam | LHH | 35 | 0.0134 | 0.0165 | 0.2311 | 0.2445 | 65.1 | 92.3 | 10 |
| 139 | Fowler, Dalton | SUS_COU1 | Four-Seam | LHH | 43 | 0.0133 | 0.0152 | 0.2312 | 0.2445 | 65.0 | 92.2 | 11 |
| 151 | Foster, Kobe | WAS_WIL3 | Four-Seam | LHH | 180 | 0.0131 | 0.0158 | 0.2314 | 0.2445 | 64.5 | 91.5 | 12 |
| 155 | Toribio, Noe | TRO_AIG | Four-Seam | LHH | 25 | 0.0129 | 0.0070 | 0.2316 | 0.2445 | 64.3 | 91.2 | 13 |
| 171 | Alpern, Liam | FLO_Y'A | Four-Seam | LHH | 86 | 0.0124 | 0.0046 | 0.2321 | 0.2445 | 63.4 | 90.3 | 14 |
| 185 | Hughes, Grif | EVA_OTT | Four-Seam | LHH | 30 | 0.0121 | 0.0038 | 0.2324 | 0.2445 | 62.9 | 89.5 | 15 |

### Four-Seam vs RHH

| Rank | Pitcher | Team | Pitch Type | Batter Side | Pitches | Avg Adv | Median Adv | Grid xwOBA | League xwOBA | LS 20-80 | LS 0-100 | Type/Side Rank |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 25 | Mercado, Nelson | OTT_TIT | Four-Seam | RHH | 42 | 0.0199 | 0.0177 | 0.2189 | 0.2388 | 76.4 | 98.6 | 1 |
| 34 | Kalisky, Jack | OTT_TIT | Four-Seam | RHH | 45 | 0.0193 | 0.0292 | 0.2195 | 0.2388 | 75.4 | 98.1 | 2 |
| 35 | Johnson, Preston | MIS_MUD | Four-Seam | RHH | 28 | 0.0191 | 0.0206 | 0.2196 | 0.2388 | 75.1 | 98.1 | 3 |
| 43 | Petraitis, AJ | LEM_COL | Four-Seam | RHH | 29 | 0.0178 | 0.0258 | 0.2210 | 0.2388 | 72.7 | 97.6 | 4 |
| 48 | Ginn, Landon | WAS_WIL3 | Four-Seam | RHH | 67 | 0.0175 | 0.0162 | 0.2213 | 0.2388 | 72.3 | 97.3 | 5 |
| 49 | Delvecchio, Dylan | LAK_ERI24 | Four-Seam | RHH | 25 | 0.0174 | 0.0214 | 0.2214 | 0.2388 | 72.1 | 97.3 | 6 |
| 58 | Brothers, Kellen | SUS_COU1 | Four-Seam | RHH | 170 | 0.0170 | 0.0147 | 0.2218 | 0.2388 | 71.3 | 96.8 | 7 |
| 63 | O'Dell, Casey | JOL_SLA | Four-Seam | RHH | 63 | 0.0165 | 0.0138 | 0.2223 | 0.2388 | 70.5 | 96.5 | 8 |
| 72 | Albert, Wes | TRI_VAL | Four-Seam | RHH | 54 | 0.0162 | 0.0203 | 0.2226 | 0.2388 | 70.0 | 96.0 | 9 |
| 76 | Roitman, Justin | WAG_SEA | Four-Seam | RHH | 40 | 0.0159 | 0.0000 | 0.2228 | 0.2388 | 69.5 | 95.7 | 10 |
| 82 | Binns, Malik | NEW_JER6 | Four-Seam | RHH | 48 | 0.0156 | 0.0089 | 0.2232 | 0.2388 | 69.0 | 95.4 | 11 |
| 84 | Langhorne, Miles | SUS_COU1 | Four-Seam | RHH | 40 | 0.0155 | 0.0043 | 0.2232 | 0.2388 | 68.8 | 95.3 | 12 |
| 88 | Langrell, Connor | MIS_MUD | Four-Seam | RHH | 25 | 0.0154 | 0.0136 | 0.2234 | 0.2388 | 68.6 | 95.1 | 13 |
| 90 | Grounds, Jackson | DOW_EAS1 | Four-Seam | RHH | 48 | 0.0153 | 0.0149 | 0.2234 | 0.2388 | 68.5 | 94.9 | 14 |
| 91 | De Los Santos, Enmanuel | NEW_ENG23 | Four-Seam | RHH | 119 | 0.0153 | 0.0084 | 0.2235 | 0.2388 | 68.5 | 94.9 | 15 |

### Sinker vs LHH

| Rank | Pitcher | Team | Pitch Type | Batter Side | Pitches | Avg Adv | Median Adv | Grid xwOBA | League xwOBA | LS 20-80 | LS 0-100 | Type/Side Rank |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 144 | Sechrist, Zander | WAS_WIL3 | Sinker | LHH | 32 | 0.0132 | 0.0041 | 0.2476 | 0.2608 | 64.7 | 91.9 | 1 |
| 242 | Aldeano, Austin | TRO_AIG | Sinker | LHH | 45 | 0.0112 | 0.0137 | 0.2496 | 0.2608 | 61.2 | 86.3 | 2 |
| 244 | Williams, Pierce | NEW_ENG23 | Sinker | LHH | 29 | 0.0111 | 0.0172 | 0.2497 | 0.2608 | 61.1 | 86.2 | 3 |
| 300 | Shoemaker, Adam | QUE_CAP | Sinker | LHH | 25 | 0.0100 | 0.0060 | 0.2508 | 0.2608 | 59.2 | 83.0 | 4 |
| 325 | McCartney, Seth | MIS_MUD | Sinker | LHH | 67 | 0.0098 | 0.0043 | 0.2510 | 0.2608 | 58.8 | 81.6 | 5 |
| 334 | Kelly, Aiden | TRI_VAL | Sinker | LHH | 51 | 0.0096 | 0.0000 | 0.2512 | 0.2608 | 58.5 | 81.1 | 6 |
| 336 | Stuka, Ted | OTT_TIT | Sinker | LHH | 82 | 0.0096 | 0.0012 | 0.2512 | 0.2608 | 58.5 | 80.9 | 7 |
| 370 | Mannering, Shawn | DOW_EAS1 | Sinker | LHH | 27 | 0.0091 | 0.0112 | 0.2517 | 0.2608 | 57.7 | 79.0 | 8 |
| 389 | Reeves, Cobe | NEW_YOR13 | Sinker | LHH | 52 | 0.0089 | 0.0082 | 0.2519 | 0.2608 | 57.3 | 77.9 | 9 |
| 409 | Kines, Gunnar | JOL_SLA | Sinker | LHH | 73 | 0.0087 | 0.0112 | 0.2521 | 0.2608 | 56.9 | 76.8 | 10 |
| 414 | Gilleran, James | NEW_ENG23 | Sinker | LHH | 25 | 0.0086 | 0.0060 | 0.2522 | 0.2608 | 56.8 | 76.5 | 11 |
| 420 | Delongchamp, Luke | TRI_VAL | Sinker | LHH | 47 | 0.0086 | 0.0000 | 0.2522 | 0.2608 | 56.7 | 76.2 | 12 |
| 422 | Cook, Cole | SCH_BOO | Sinker | LHH | 53 | 0.0085 | 0.0110 | 0.2523 | 0.2608 | 56.6 | 76.1 | 13 |
| 423 | Sabatine, Gino | TRI_VAL | Sinker | LHH | 36 | 0.0085 | 0.0021 | 0.2523 | 0.2608 | 56.6 | 76.0 | 14 |
| 478 | Vecerka, Boris | QUE_CAP | Sinker | LHH | 138 | 0.0077 | 0.0074 | 0.2531 | 0.2608 | 55.2 | 72.9 | 15 |

### Sinker vs RHH

| Rank | Pitcher | Team | Pitch Type | Batter Side | Pitches | Avg Adv | Median Adv | Grid xwOBA | League xwOBA | LS 20-80 | LS 0-100 | Type/Side Rank |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 168 | Aldeano, Austin | TRO_AIG | Sinker | RHH | 25 | 0.0125 | 0.0207 | 0.2401 | 0.2527 | 63.6 | 90.5 | 1 |
| 181 | Donnan, Blake | FLO_Y'A | Sinker | RHH | 84 | 0.0122 | 0.0158 | 0.2405 | 0.2527 | 63.0 | 89.8 | 2 |
| 192 | Leach, Landon | TRO_AIG | Sinker | RHH | 47 | 0.0119 | 0.0000 | 0.2408 | 0.2527 | 62.5 | 89.1 | 3 |
| 233 | Petschke, Ben | EVA_OTT | Sinker | RHH | 42 | 0.0112 | 0.0061 | 0.2415 | 0.2527 | 61.3 | 86.8 | 4 |
| 237 | Glickstein, Aaron | SCH_BOO | Sinker | RHH | 72 | 0.0112 | 0.0173 | 0.2415 | 0.2527 | 61.3 | 86.6 | 5 |
| 246 | Turner, Eric | JOL_SLA | Sinker | RHH | 46 | 0.0111 | 0.0113 | 0.2416 | 0.2527 | 61.1 | 86.1 | 6 |
| 317 | Campbell, AJ | WIN_CIT29 | Sinker | RHH | 31 | 0.0099 | 0.0166 | 0.2428 | 0.2527 | 59.0 | 82.0 | 7 |
| 330 | Hoeymans, Jack | GAT_GRI | Sinker | RHH | 35 | 0.0097 | 0.0012 | 0.2430 | 0.2527 | 58.7 | 81.3 | 8 |
| 338 | Vecerka, Boris | QUE_CAP | Sinker | RHH | 81 | 0.0096 | 0.0054 | 0.2431 | 0.2527 | 58.5 | 80.8 | 9 |
| 341 | O'Brien, Keenan | SUS_COU1 | Sinker | RHH | 28 | 0.0096 | 0.0054 | 0.2431 | 0.2527 | 58.4 | 80.7 | 10 |
| 349 | Colon, Jeffrey | TRO_AIG | Sinker | RHH | 26 | 0.0094 | 0.0024 | 0.2433 | 0.2527 | 58.2 | 80.2 | 11 |
| 350 | Garcia, Andrew | EVA_OTT | Sinker | RHH | 29 | 0.0094 | 0.0042 | 0.2433 | 0.2527 | 58.2 | 80.1 | 12 |
| 396 | Mannering, Shawn | DOW_EAS1 | Sinker | RHH | 32 | 0.0088 | 0.0000 | 0.2439 | 0.2527 | 57.1 | 77.5 | 13 |
| 412 | Kelly, Aiden | TRI_VAL | Sinker | RHH | 27 | 0.0086 | 0.0050 | 0.2440 | 0.2527 | 56.8 | 76.6 | 14 |
| 426 | Delongchamp, Luke | TRI_VAL | Sinker | RHH | 53 | 0.0084 | 0.0023 | 0.2442 | 0.2527 | 56.5 | 75.8 | 15 |

### Slider vs LHH

| Rank | Pitcher | Team | Pitch Type | Batter Side | Pitches | Avg Adv | Median Adv | Grid xwOBA | League xwOBA | LS 20-80 | LS 0-100 | Type/Side Rank |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 113 | Potteiger, Jack | JOL_SLA | Slider | LHH | 30 | 0.0144 | 0.0095 | 0.2229 | 0.2373 | 66.8 | 93.6 | 1 |
| 118 | Foltz Jr., Michael | WAS_WIL3 | Slider | LHH | 25 | 0.0140 | 0.0054 | 0.2232 | 0.2373 | 66.2 | 93.3 | 2 |
| 162 | Campbell, Tyler | MIS_MUD | Slider | LHH | 88 | 0.0126 | 0.0108 | 0.2247 | 0.2373 | 63.7 | 90.8 | 3 |
| 165 | Milburn, Isaac | FLO_Y'A | Slider | LHH | 79 | 0.0126 | 0.0114 | 0.2247 | 0.2373 | 63.7 | 90.7 | 4 |
| 169 | Barker, Alex | NEW_YOR13 | Slider | LHH | 95 | 0.0125 | 0.0024 | 0.2248 | 0.2373 | 63.6 | 90.4 | 5 |
| 197 | Dima, Josh | GAT_GRI | Slider | LHH | 75 | 0.0118 | 0.0000 | 0.2255 | 0.2373 | 62.3 | 88.9 | 6 |
| 204 | Smith, Ben | NEW_ENG23 | Slider | LHH | 40 | 0.0117 | 0.0000 | 0.2256 | 0.2373 | 62.1 | 88.5 | 7 |
| 207 | McEvoy, Aidan | FLO_Y'A | Slider | LHH | 69 | 0.0116 | 0.0024 | 0.2257 | 0.2373 | 62.0 | 88.3 | 8 |
| 222 | Alpern, Liam | FLO_Y'A | Slider | LHH | 38 | 0.0114 | 0.0000 | 0.2259 | 0.2373 | 61.5 | 87.4 | 9 |
| 227 | Balzan, Jackson | SUS_COU1 | Slider | LHH | 75 | 0.0113 | 0.0061 | 0.2260 | 0.2373 | 61.4 | 87.1 | 10 |
| 229 | Eckaus, David | EVA_OTT | Slider | LHH | 115 | 0.0112 | 0.0010 | 0.2260 | 0.2373 | 61.3 | 87.0 | 11 |
| 232 | Harris, Everette | TRI_VAL | Slider | LHH | 29 | 0.0112 | 0.0043 | 0.2260 | 0.2373 | 61.3 | 86.9 | 12 |
| 243 | Maher, Adam | TRI_VAL | Slider | LHH | 48 | 0.0111 | 0.0010 | 0.2262 | 0.2373 | 61.1 | 86.2 | 13 |
| 262 | Scott, Brandon | LAK_ERI24 | Slider | LHH | 67 | 0.0108 | 0.0002 | 0.2265 | 0.2373 | 60.5 | 85.2 | 14 |
| 266 | Webster, Evan | FLO_Y'A | Slider | LHH | 76 | 0.0107 | 0.0043 | 0.2266 | 0.2373 | 60.4 | 84.9 | 15 |

### Slider vs RHH

| Rank | Pitcher | Team | Pitch Type | Batter Side | Pitches | Avg Adv | Median Adv | Grid xwOBA | League xwOBA | LS 20-80 | LS 0-100 | Type/Side Rank |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | Garcia, Hector | WAS_WIL3 | Slider | RHH | 36 | 0.0270 | 0.0212 | 0.2044 | 0.2314 | 80.0 | 100.0 | 1 |
| 2 | Perez, Kelvin | WAS_WIL3 | Slider | RHH | 103 | 0.0251 | 0.0265 | 0.2063 | 0.2314 | 80.0 | 99.9 | 2 |
| 3 | Wiltse, Ryan | EVA_OTT | Slider | RHH | 60 | 0.0248 | 0.0186 | 0.2066 | 0.2314 | 80.0 | 99.9 | 3 |
| 4 | Gilleran, Jimmy | NEW_ENG23 | Slider | RHH | 90 | 0.0244 | 0.0244 | 0.2070 | 0.2314 | 80.0 | 99.8 | 4 |
| 5 | Salata, Derek | SCH_BOO | Slider | RHH | 163 | 0.0236 | 0.0196 | 0.2078 | 0.2314 | 80.0 | 99.8 | 5 |
| 6 | Smith, Ethan | WIN_CIT29 | Slider | RHH | 30 | 0.0235 | 0.0101 | 0.2079 | 0.2314 | 80.0 | 99.7 | 6 |
| 7 | Perdomo, Rafael | QUE_CAP | Slider | RHH | 46 | 0.0232 | 0.0145 | 0.2082 | 0.2314 | 80.0 | 99.7 | 7 |
| 8 | Albert, Wes | TRI_VAL | Slider | RHH | 25 | 0.0230 | 0.0152 | 0.2084 | 0.2314 | 80.0 | 99.6 | 8 |
| 9 | Blair, Davis | DOW_EAS1 | Slider | RHH | 61 | 0.0224 | 0.0089 | 0.2090 | 0.2314 | 80.0 | 99.5 | 9 |
| 10 | Thompson, Ross | SCH_BOO | Slider | RHH | 196 | 0.0223 | 0.0089 | 0.2091 | 0.2314 | 80.0 | 99.5 | 10 |
| 11 | Kirby, Zach | WAS_WIL3 | Slider | RHH | 126 | 0.0222 | 0.0115 | 0.2092 | 0.2314 | 80.0 | 99.4 | 11 |
| 12 | Belton, Hunter | MIS_MUD | Slider | RHH | 75 | 0.0220 | 0.0138 | 0.2094 | 0.2314 | 80.0 | 99.4 | 12 |
| 13 | Morrissey, Joe | EVA_OTT | Slider | RHH | 45 | 0.0219 | 0.0186 | 0.2095 | 0.2314 | 79.9 | 99.3 | 13 |
| 14 | Vailes, Gage | GAT_GRI | Slider | RHH | 220 | 0.0217 | 0.0152 | 0.2097 | 0.2314 | 79.5 | 99.3 | 14 |
| 15 | Cameron, Wyatt | SCH_BOO | Slider | RHH | 50 | 0.0215 | 0.0000 | 0.2099 | 0.2314 | 79.1 | 99.2 | 15 |

### Splitter vs LHH

| Rank | Pitcher | Team | Pitch Type | Batter Side | Pitches | Avg Adv | Median Adv | Grid xwOBA | League xwOBA | LS 20-80 | LS 0-100 | Type/Side Rank |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 973 | Coles, Chad | WAS_WIL3 | Splitter | LHH | 38 | 0.0031 | 0.0000 | 0.2391 | 0.2422 | 47.2 | 44.7 | 1 |
| 1032 | Eldred, Zach | NEW_ENG23 | Splitter | LHH | 45 | 0.0027 | 0.0000 | 0.2395 | 0.2422 | 46.5 | 41.4 | 2 |
| 1104 | Thornton, Tyler | NEW_ENG23 | Splitter | LHH | 69 | 0.0023 | 0.0000 | 0.2399 | 0.2422 | 45.7 | 37.3 | 3 |
| 1129 | Soto, Carlos | JOL_SLA | Splitter | LHH | 26 | 0.0021 | 0.0000 | 0.2401 | 0.2422 | 45.4 | 35.8 | 4 |
| 1154 | Williams, Brian | MIS_MUD | Splitter | LHH | 57 | 0.0019 | 0.0000 | 0.2403 | 0.2422 | 45.1 | 34.4 | 5 |
| 1159 | Perozzi, John | SUS_COU1 | Splitter | LHH | 33 | 0.0019 | 0.0000 | 0.2403 | 0.2422 | 45.0 | 34.1 | 6 |
| 1191 | Vitas, Ben | JOL_SLA | Splitter | LHH | 91 | 0.0016 | 0.0000 | 0.2405 | 0.2422 | 44.6 | 32.3 | 7 |
| 1204 | Salata, Derek | SCH_BOO | Splitter | LHH | 90 | 0.0015 | 0.0000 | 0.2406 | 0.2422 | 44.5 | 31.6 | 8 |
| 1218 | Pindel, Buddie | SCH_BOO | Splitter | LHH | 58 | 0.0014 | 0.0000 | 0.2407 | 0.2422 | 44.3 | 30.8 | 9 |
| 1249 | Thompson, Ross | SCH_BOO | Splitter | LHH | 145 | 0.0013 | 0.0000 | 0.2409 | 0.2422 | 44.0 | 29.0 | 10 |
| 1252 | Garcia, Hector | WAS_WIL3 | Splitter | LHH | 59 | 0.0012 | 0.0000 | 0.2410 | 0.2422 | 43.9 | 28.8 | 11 |
| 1315 | Parsons, Billy | SUS_COU1 | Splitter | LHH | 33 | 0.0008 | 0.0000 | 0.2414 | 0.2422 | 43.2 | 25.3 | 12 |
| 1346 | Villers, Ian | QUE_CAP | Splitter | LHH | 39 | 0.0005 | 0.0000 | 0.2417 | 0.2422 | 42.7 | 23.5 | 13 |
| 1362 | Orth, Harry | SCH_BOO | Splitter | LHH | 31 | 0.0004 | 0.0000 | 0.2418 | 0.2422 | 42.5 | 22.6 | 14 |
| 1419 | Shears, Tanner | SCH_BOO | Splitter | LHH | 36 | 0.0000 | 0.0000 | 0.2422 | 0.2422 | 41.8 | 19.3 | 15 |

### Splitter vs RHH

| Rank | Pitcher | Team | Pitch Type | Batter Side | Pitches | Avg Adv | Median Adv | Grid xwOBA | League xwOBA | LS 20-80 | LS 0-100 | Type/Side Rank |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1076 | Villers, Ian | QUE_CAP | Splitter | RHH | 25 | 0.0025 | 0.0024 | 0.2431 | 0.2456 | 46.1 | 38.9 | 1 |
| 1217 | Pindel, Buddie | SCH_BOO | Splitter | RHH | 31 | 0.0015 | 0.0000 | 0.2441 | 0.2456 | 44.3 | 30.8 | 2 |
| 1341 | Williams, Brian | MIS_MUD | Splitter | RHH | 44 | 0.0006 | 0.0000 | 0.2450 | 0.2456 | 42.7 | 23.8 | 3 |
| 1383 | Coles, Chad | WAS_WIL3 | Splitter | RHH | 25 | 0.0003 | 0.0000 | 0.2453 | 0.2456 | 42.3 | 21.4 | 4 |
| 1413 | Andueza, Axel | DOW_EAS1 | Splitter | RHH | 26 | 0.0001 | 0.0000 | 0.2455 | 0.2456 | 42.0 | 19.7 | 5 |
| 1415 | Shears, Tanner | SCH_BOO | Splitter | RHH | 33 | 0.0001 | 0.0000 | 0.2455 | 0.2456 | 41.9 | 19.6 | 6 |
| 1435 | Eldred, Zach | NEW_ENG23 | Splitter | RHH | 35 | -0.0001 | 0.0000 | 0.2457 | 0.2456 | 41.7 | 18.4 | 7 |
| 1510 | Thornton, Tyler | NEW_ENG23 | Splitter | RHH | 50 | -0.0009 | 0.0000 | 0.2465 | 0.2456 | 40.3 | 14.2 | 8 |
| 1521 | Vitas, Ben | JOL_SLA | Splitter | RHH | 36 | -0.0010 | 0.0000 | 0.2466 | 0.2456 | 40.1 | 13.5 | 9 |
| 1575 | MacMillan, Blake | TRO_AIG | Splitter | RHH | 31 | -0.0016 | 0.0000 | 0.2472 | 0.2456 | 39.1 | 10.5 | 10 |
| 1627 | Nakata, Yuto | QUE_CAP | Splitter | RHH | 30 | -0.0023 | 0.0000 | 0.2479 | 0.2456 | 37.8 | 7.5 | 11 |
| 1664 | Thompson, Ross | SCH_BOO | Splitter | RHH | 30 | -0.0032 | 0.0000 | 0.2488 | 0.2456 | 36.2 | 5.4 | 12 |

### Sweeper vs RHH

| Rank | Pitcher | Team | Pitch Type | Batter Side | Pitches | Avg Adv | Median Adv | Grid xwOBA | League xwOBA | LS 20-80 | LS 0-100 | Type/Side Rank |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1440 | Cerda, Junior | EVA_OTT | Sweeper | RHH | 35 | -0.0001 | 0.0000 | 0.1939 | 0.1938 | 41.6 | 18.1 | 1 |
| 1448 | Simpson, Garret | EVA_OTT | Sweeper | RHH | 32 | -0.0002 | 0.0000 | 0.1939 | 0.1938 | 41.4 | 17.7 | 2 |
