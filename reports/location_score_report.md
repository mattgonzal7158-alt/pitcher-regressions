# Location Score Report

- Pitch input file: `data\processed\2026-data-with-woba-xwoba.parquet`
- Location grid input file: `data\processed\location_value_grid.csv`
- Output file: `data\processed\location_scores.csv`
- Assigned pitch rows: 164,166
- Qualified pitcher + pitch type + batter side rows: 1,811
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
| 1 | Garcia, Hector | WAS_WIL3 | Slider | RHH | 36 | 0.0307 | 0.0283 | 0.1999 | 0.2306 | 80.0 | 100.0 | 1 |
| 2 | Perez, Kelvin | WAS_WIL3 | Slider | RHH | 103 | 0.0268 | 0.0267 | 0.2038 | 0.2306 | 80.0 | 99.9 | 2 |
| 3 | Perdomo, Rafael | QUE_CAP | Slider | RHH | 48 | 0.0265 | 0.0140 | 0.2042 | 0.2306 | 80.0 | 99.9 | 3 |
| 4 | Wiltse, Ryan | EVA_OTT | Slider | RHH | 63 | 0.0262 | 0.0227 | 0.2045 | 0.2306 | 80.0 | 99.8 | 4 |
| 5 | Finarelli, Nick | LON_ISL22 | Slider | RHH | 31 | 0.0252 | 0.0118 | 0.2055 | 0.2306 | 80.0 | 99.8 | 5 |
| 6 | Albert, Wes | DOW_EAS1 | Slider | RHH | 29 | 0.0248 | 0.0025 | 0.2058 | 0.2306 | 80.0 | 99.7 | 6 |
| 7 | Salata, Derek | SCH_BOO | Slider | RHH | 163 | 0.0244 | 0.0201 | 0.2062 | 0.2306 | 80.0 | 99.7 | 7 |
| 8 | Smith, Ethan | WIN_CIT29 | Slider | RHH | 30 | 0.0244 | 0.0113 | 0.2062 | 0.2306 | 80.0 | 99.6 | 8 |
| 9 | Thompson, Ross | SCH_BOO | Slider | RHH | 196 | 0.0241 | 0.0118 | 0.2065 | 0.2306 | 80.0 | 99.6 | 9 |
| 10 | Sanchez, Sergio | MIS_MUD | Slider | RHH | 28 | 0.0241 | 0.0025 | 0.2065 | 0.2306 | 80.0 | 99.5 | 10 |
| 11 | Cameron, Wyatt | SCH_BOO | Slider | RHH | 50 | 0.0239 | 0.0019 | 0.2067 | 0.2306 | 80.0 | 99.4 | 11 |
| 12 | Blair, Davis | DOW_EAS1 | Slider | RHH | 61 | 0.0238 | 0.0110 | 0.2069 | 0.2306 | 80.0 | 99.4 | 12 |
| 13 | Gilleran, Jimmy | NEW_ENG23 | Slider | RHH | 97 | 0.0237 | 0.0170 | 0.2069 | 0.2306 | 80.0 | 99.3 | 13 |
| 14 | Kirby, Zach | WAS_WIL3 | Slider | RHH | 126 | 0.0234 | 0.0116 | 0.2072 | 0.2306 | 80.0 | 99.3 | 14 |
| 15 | Morrissey, Joe | EVA_OTT | Slider | RHH | 47 | 0.0234 | 0.0273 | 0.2072 | 0.2306 | 80.0 | 99.2 | 15 |
| 16 | O'Hanlon, Michael | WAS_WIL3 | Slider | RHH | 54 | 0.0232 | 0.0054 | 0.2074 | 0.2306 | 80.0 | 99.2 | 16 |
| 17 | Albert, Wes | TRI_VAL | Slider | RHH | 25 | 0.0232 | 0.0118 | 0.2074 | 0.2306 | 80.0 | 99.1 | 17 |
| 18 | Voytko, Fawster | TRO_AIG | Slider | RHH | 39 | 0.0228 | 0.0025 | 0.2078 | 0.2306 | 79.9 | 99.1 | 18 |
| 19 | Nova, Fraynel | LAK_ERI24 | Slider | RHH | 153 | 0.0228 | 0.0170 | 0.2078 | 0.2306 | 79.9 | 99.0 | 19 |
| 20 | Duby, Bill | NEW_JER6 | Slider | RHH | 64 | 0.0225 | 0.0100 | 0.2082 | 0.2306 | 79.2 | 99.0 | 20 |
| 21 | Mercado, Nelson | OTT_TIT | Four-Seam | RHH | 42 | 0.0224 | 0.0239 | 0.2144 | 0.2368 | 79.2 | 98.9 | 1 |
| 22 | Belton, Hunter | MIS_MUD | Slider | RHH | 75 | 0.0222 | 0.0116 | 0.2084 | 0.2306 | 78.9 | 98.8 | 21 |
| 23 | Vailes, Gage | GAT_GRI | Slider | RHH | 220 | 0.0221 | 0.0140 | 0.2085 | 0.2306 | 78.6 | 98.8 | 22 |
| 24 | Tomczak, Anthony | EVA_OTT | Slider | RHH | 27 | 0.0221 | 0.0187 | 0.2085 | 0.2306 | 78.6 | 98.7 | 23 |
| 25 | Cerda, Junior | EVA_OTT | Slider | RHH | 79 | 0.0221 | 0.0056 | 0.2086 | 0.2306 | 78.6 | 98.7 | 24 |
| 26 | Helt, Robert | LAK_ERI24 | Slider | RHH | 147 | 0.0219 | 0.0050 | 0.2087 | 0.2306 | 78.4 | 98.6 | 25 |
| 27 | Allemann, Braeden | QUE_CAP | Slider | RHH | 73 | 0.0218 | 0.0056 | 0.2089 | 0.2306 | 78.1 | 98.6 | 26 |
| 28 | McMahon, Chris | LAK_ERI24 | Slider | RHH | 32 | 0.0213 | 0.0043 | 0.2094 | 0.2306 | 77.2 | 98.5 | 27 |
| 29 | Encarnacion, J.D. | EVA_OTT | Changeup | LHH | 28 | 0.0212 | 0.0178 | 0.2195 | 0.2407 | 77.1 | 98.5 | 1 |
| 30 | Barraza, Chris | MIS_MUD | Slider | RHH | 36 | 0.0211 | 0.0181 | 0.2095 | 0.2306 | 76.9 | 98.4 | 28 |

## Top Location Scores by Pitch Type and Batter Side

### Changeup vs LHH

| Rank | Pitcher | Team | Pitch Type | Batter Side | Pitches | Avg Adv | Median Adv | Grid xwOBA | League xwOBA | LS 20-80 | LS 0-100 | Type/Side Rank |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 29 | Encarnacion, J.D. | EVA_OTT | Changeup | LHH | 28 | 0.0212 | 0.0178 | 0.2195 | 0.2407 | 77.1 | 98.5 | 1 |
| 47 | Albert, Wes | DOW_EAS1 | Changeup | LHH | 42 | 0.0188 | 0.0224 | 0.2219 | 0.2407 | 73.0 | 97.5 | 2 |
| 51 | Hicks, Jackson | DOW_EAS1 | Changeup | LHH | 25 | 0.0184 | 0.0095 | 0.2223 | 0.2407 | 72.4 | 97.2 | 3 |
| 66 | Smith, Jackson | MIS_MUD | Changeup | LHH | 73 | 0.0174 | 0.0160 | 0.2232 | 0.2407 | 70.8 | 96.4 | 4 |
| 70 | Allemann, Braeden | QUE_CAP | Changeup | LHH | 34 | 0.0172 | 0.0103 | 0.2234 | 0.2407 | 70.5 | 96.2 | 5 |
| 91 | Dill, Austin | TRI_VAL | Changeup | LHH | 118 | 0.0160 | 0.0129 | 0.2247 | 0.2407 | 68.4 | 95.0 | 6 |
| 119 | Hampton, Ky | OTT_TIT | Changeup | LHH | 138 | 0.0149 | 0.0120 | 0.2258 | 0.2407 | 66.5 | 93.5 | 7 |
| 128 | Voytko, Fawster | TRO_AIG | Changeup | LHH | 57 | 0.0146 | 0.0120 | 0.2260 | 0.2407 | 66.1 | 93.0 | 8 |
| 130 | Albert, Wes | TRI_VAL | Changeup | LHH | 38 | 0.0145 | 0.0053 | 0.2262 | 0.2407 | 65.9 | 92.9 | 9 |
| 153 | Noble, Nick | FDU_KNI | Changeup | LHH | 46 | 0.0136 | 0.0103 | 0.2271 | 0.2407 | 64.3 | 91.6 | 10 |
| 161 | Kirby, Zach | WAS_WIL3 | Changeup | LHH | 119 | 0.0134 | 0.0095 | 0.2272 | 0.2407 | 64.1 | 91.2 | 11 |
| 167 | Maietta, Dante | WIN_CIT29 | Changeup | LHH | 158 | 0.0133 | 0.0040 | 0.2273 | 0.2407 | 63.9 | 90.8 | 12 |
| 172 | Garcia, Jorge | SUS_COU1 | Changeup | LHH | 36 | 0.0131 | 0.0049 | 0.2275 | 0.2407 | 63.6 | 90.6 | 13 |
| 176 | Smith, Ethan | WIN_CIT29 | Changeup | LHH | 45 | 0.0130 | 0.0057 | 0.2277 | 0.2407 | 63.3 | 90.3 | 14 |
| 187 | Marynczak, Arlo | TRI_VAL | Changeup | LHH | 117 | 0.0127 | 0.0072 | 0.2280 | 0.2407 | 62.8 | 89.7 | 15 |

### Changeup vs RHH

| Rank | Pitcher | Team | Pitch Type | Batter Side | Pitches | Avg Adv | Median Adv | Grid xwOBA | League xwOBA | LS 20-80 | LS 0-100 | Type/Side Rank |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 116 | Culley, Wesley | NEW_YOR13 | Changeup | RHH | 36 | 0.0149 | 0.0154 | 0.2305 | 0.2454 | 66.6 | 93.6 | 1 |
| 132 | Walsh, John | MIS_MUD | Changeup | RHH | 43 | 0.0143 | 0.0121 | 0.2311 | 0.2454 | 65.6 | 92.8 | 2 |
| 159 | Smith, Ben | NEW_ENG23 | Changeup | RHH | 43 | 0.0135 | 0.0091 | 0.2319 | 0.2454 | 64.1 | 91.3 | 3 |
| 258 | Alpern, Liam | FLO_Y'A | Changeup | RHH | 38 | 0.0115 | 0.0086 | 0.2339 | 0.2454 | 60.7 | 85.8 | 4 |
| 265 | Steinhauer, Ryan | NEW_JER6 | Changeup | RHH | 57 | 0.0114 | 0.0071 | 0.2340 | 0.2454 | 60.6 | 85.4 | 5 |
| 297 | Parra, Andres | LAK_ERI24 | Changeup | RHH | 41 | 0.0109 | 0.0000 | 0.2345 | 0.2454 | 59.8 | 83.7 | 6 |
| 318 | Kemlage, Joe | NEW_ENG23 | Changeup | RHH | 25 | 0.0104 | 0.0181 | 0.2350 | 0.2454 | 58.9 | 82.5 | 7 |
| 323 | Carroll, Jake | JOL_SLA | Changeup | RHH | 38 | 0.0103 | 0.0000 | 0.2351 | 0.2454 | 58.8 | 82.2 | 8 |
| 352 | Pindel, Buddie | SCH_BOO | Changeup | RHH | 27 | 0.0099 | 0.0000 | 0.2355 | 0.2454 | 58.1 | 80.6 | 9 |
| 355 | Barker, Alex | NEW_YOR13 | Changeup | RHH | 132 | 0.0099 | 0.0019 | 0.2355 | 0.2454 | 58.1 | 80.5 | 10 |
| 359 | Galva, Claudio | GAT_GRI | Changeup | RHH | 91 | 0.0099 | 0.0038 | 0.2356 | 0.2454 | 58.0 | 80.2 | 11 |
| 364 | Gollert, Harley | QUE_CAP | Changeup | RHH | 38 | 0.0097 | 0.0000 | 0.2357 | 0.2454 | 57.9 | 80.0 | 12 |
| 380 | Gollert, Harley | TRO_AIG | Changeup | RHH | 117 | 0.0095 | 0.0022 | 0.2359 | 0.2454 | 57.4 | 79.1 | 13 |
| 414 | Givens-Craig, Hayden | SUS_COU1 | Changeup | RHH | 35 | 0.0091 | 0.0000 | 0.2363 | 0.2454 | 56.8 | 77.2 | 14 |
| 421 | Fry, Dale | LON_ISL22 | Changeup | RHH | 26 | 0.0090 | 0.0000 | 0.2364 | 0.2454 | 56.7 | 76.8 | 15 |

### Curveball vs LHH

| Rank | Pitcher | Team | Pitch Type | Batter Side | Pitches | Avg Adv | Median Adv | Grid xwOBA | League xwOBA | LS 20-80 | LS 0-100 | Type/Side Rank |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 328 | Carroll, Jake | JOL_SLA | Curveball | LHH | 36 | 0.0103 | 0.0000 | 0.2308 | 0.2411 | 58.7 | 81.9 | 1 |
| 367 | Shinn, Nathan | LAK_ERI24 | Curveball | LHH | 29 | 0.0097 | 0.0020 | 0.2314 | 0.2411 | 57.8 | 79.8 | 2 |
| 463 | Long, Jalon | NEW_YOR13 | Curveball | LHH | 26 | 0.0085 | 0.0001 | 0.2326 | 0.2411 | 55.8 | 74.5 | 3 |
| 642 | Martzolf, Max | OTT_TIT | Curveball | LHH | 56 | 0.0064 | 0.0000 | 0.2347 | 0.2411 | 52.2 | 64.6 | 4 |
| 668 | Barker, Alex | NEW_YOR13 | Curveball | LHH | 36 | 0.0062 | 0.0000 | 0.2349 | 0.2411 | 51.8 | 63.2 | 5 |
| 680 | Baker, Luke | EVA_OTT | Curveball | LHH | 37 | 0.0061 | 0.0014 | 0.2350 | 0.2411 | 51.6 | 62.5 | 6 |
| 711 | Williams, Pierce | NEW_ENG23 | Curveball | LHH | 67 | 0.0058 | 0.0002 | 0.2353 | 0.2411 | 51.2 | 60.8 | 7 |
| 762 | Foltz Jr., Michael | WAS_WIL3 | Curveball | LHH | 49 | 0.0054 | 0.0014 | 0.2357 | 0.2411 | 50.5 | 58.0 | 8 |
| 764 | Sanchez, Edwin | LAK_ERI24 | Curveball | LHH | 54 | 0.0054 | 0.0000 | 0.2357 | 0.2411 | 50.5 | 57.9 | 9 |
| 778 | Kalisky, Jack | OTT_TIT | Curveball | LHH | 27 | 0.0053 | 0.0000 | 0.2358 | 0.2411 | 50.4 | 57.1 | 10 |
| 780 | Cameron, Wyatt | SCH_BOO | Curveball | LHH | 47 | 0.0053 | 0.0000 | 0.2358 | 0.2411 | 50.3 | 57.0 | 11 |
| 782 | Langrell, Connor | MIS_MUD | Curveball | LHH | 57 | 0.0053 | 0.0000 | 0.2358 | 0.2411 | 50.3 | 56.9 | 12 |
| 799 | Anderson, Colt | WAS_WIL3 | Curveball | LHH | 40 | 0.0051 | 0.0000 | 0.2360 | 0.2411 | 50.0 | 55.9 | 13 |
| 804 | Morgan, Cooper | QUE_CAP | Curveball | LHH | 66 | 0.0051 | 0.0001 | 0.2360 | 0.2411 | 50.0 | 55.7 | 14 |
| 828 | Johnston, Spencer | DOW_EAS1 | Curveball | LHH | 32 | 0.0048 | 0.0000 | 0.2363 | 0.2411 | 49.6 | 54.3 | 15 |

### Curveball vs RHH

| Rank | Pitcher | Team | Pitch Type | Batter Side | Pitches | Avg Adv | Median Adv | Grid xwOBA | League xwOBA | LS 20-80 | LS 0-100 | Type/Side Rank |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 35 | Hargrove, Dawson | LAK_ERI24 | Curveball | RHH | 30 | 0.0200 | 0.0154 | 0.2303 | 0.2503 | 75.2 | 98.1 | 1 |
| 120 | Simpson, Garret | EVA_OTT | Curveball | RHH | 55 | 0.0149 | 0.0000 | 0.2355 | 0.2503 | 66.5 | 93.4 | 2 |
| 145 | Perdomo, Rafael | QUE_CAP | Curveball | RHH | 30 | 0.0138 | 0.0000 | 0.2365 | 0.2503 | 64.7 | 92.0 | 3 |
| 165 | Morse, Colby | EVA_OTT | Curveball | RHH | 25 | 0.0133 | 0.0028 | 0.2370 | 0.2503 | 63.9 | 90.9 | 4 |
| 213 | Kalisky, Jack | OTT_TIT | Curveball | RHH | 46 | 0.0123 | 0.0001 | 0.2380 | 0.2503 | 62.2 | 88.3 | 5 |
| 216 | Garcia, Hector | WAS_WIL3 | Curveball | RHH | 27 | 0.0123 | 0.0099 | 0.2381 | 0.2503 | 62.1 | 88.1 | 6 |
| 271 | Long, Jalon | NEW_YOR13 | Curveball | RHH | 27 | 0.0113 | 0.0000 | 0.2391 | 0.2503 | 60.4 | 85.1 | 7 |
| 290 | Allemann, Braeden | QUE_CAP | Curveball | RHH | 137 | 0.0110 | 0.0000 | 0.2393 | 0.2503 | 60.0 | 84.0 | 8 |
| 292 | Maryniak, Connor | NEW_JER6 | Curveball | RHH | 96 | 0.0110 | 0.0000 | 0.2394 | 0.2503 | 59.9 | 83.9 | 9 |
| 301 | Coles, Chad | WAS_WIL3 | Curveball | RHH | 45 | 0.0107 | 0.0003 | 0.2396 | 0.2503 | 59.5 | 83.4 | 10 |
| 322 | Ginn, Landon | WAS_WIL3 | Curveball | RHH | 26 | 0.0103 | 0.0000 | 0.2400 | 0.2503 | 58.8 | 82.3 | 11 |
| 327 | Brothers, Kellen | SUS_COU1 | Curveball | RHH | 25 | 0.0103 | 0.0000 | 0.2401 | 0.2503 | 58.7 | 82.0 | 12 |
| 349 | Hohenstein, Liam | WIN_CIT29 | Curveball | RHH | 60 | 0.0100 | 0.0000 | 0.2404 | 0.2503 | 58.2 | 80.8 | 13 |
| 361 | Lefebvre, Charles | TRO_AIG | Curveball | RHH | 52 | 0.0098 | 0.0000 | 0.2405 | 0.2503 | 58.0 | 80.1 | 14 |
| 365 | House, Tristan | MIS_MUD | Curveball | RHH | 28 | 0.0097 | 0.0000 | 0.2406 | 0.2503 | 57.8 | 79.9 | 15 |

### Cutter vs LHH

| Rank | Pitcher | Team | Pitch Type | Batter Side | Pitches | Avg Adv | Median Adv | Grid xwOBA | League xwOBA | LS 20-80 | LS 0-100 | Type/Side Rank |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 856 | McEvoy, Aidan | FLO_Y'A | Cutter | LHH | 36 | 0.0046 | 0.0000 | 0.2230 | 0.2276 | 49.2 | 52.8 | 1 |
| 1001 | Cook, Cole | SCH_BOO | Cutter | LHH | 33 | 0.0035 | 0.0000 | 0.2241 | 0.2276 | 47.3 | 44.8 | 2 |
| 1020 | Petschke, Ben | EVA_OTT | Cutter | LHH | 150 | 0.0034 | 0.0000 | 0.2242 | 0.2276 | 47.1 | 43.7 | 3 |
| 1084 | Majick, Eli | NEW_ENG23 | Cutter | LHH | 28 | 0.0029 | 0.0000 | 0.2247 | 0.2276 | 46.3 | 40.2 | 4 |
| 1123 | Catrambone, Ben | JOL_SLA | Cutter | LHH | 28 | 0.0026 | 0.0000 | 0.2249 | 0.2276 | 45.9 | 38.0 | 5 |
| 1165 | Jones, Breyln | NEW_JER6 | Cutter | LHH | 26 | 0.0023 | 0.0000 | 0.2253 | 0.2276 | 45.3 | 35.7 | 6 |
| 1231 | Parsons, Billy | SUS_COU1 | Cutter | LHH | 40 | 0.0018 | 0.0000 | 0.2257 | 0.2276 | 44.5 | 32.1 | 7 |
| 1252 | Sechrist, Zander | WAS_WIL3 | Cutter | LHH | 41 | 0.0017 | 0.0000 | 0.2259 | 0.2276 | 44.3 | 30.9 | 8 |
| 1286 | Webster, Evan | FLO_Y'A | Cutter | LHH | 99 | 0.0014 | 0.0000 | 0.2261 | 0.2276 | 43.9 | 29.0 | 9 |
| 1292 | Moore, Kyle | SCH_BOO | Cutter | LHH | 38 | 0.0014 | 0.0000 | 0.2261 | 0.2276 | 43.8 | 28.7 | 10 |
| 1356 | Campbell, AJ | WIN_CIT29 | Cutter | LHH | 41 | 0.0010 | 0.0000 | 0.2265 | 0.2276 | 43.2 | 25.2 | 11 |
| 1361 | Campbell, Tyler | MIS_MUD | Cutter | LHH | 60 | 0.0010 | 0.0000 | 0.2266 | 0.2276 | 43.1 | 24.9 | 12 |
| 1365 | Langrell, Connor | MIS_MUD | Cutter | LHH | 117 | 0.0009 | 0.0000 | 0.2267 | 0.2276 | 43.0 | 24.7 | 13 |
| 1366 | Flontek, Zac | DOW_EAS1 | Cutter | LHH | 27 | 0.0009 | 0.0000 | 0.2267 | 0.2276 | 43.0 | 24.6 | 14 |
| 1399 | Morgan, Marcus | JOL_SLA | Cutter | LHH | 40 | 0.0006 | 0.0000 | 0.2269 | 0.2276 | 42.5 | 22.8 | 15 |

### Cutter vs RHH

| Rank | Pitcher | Team | Pitch Type | Batter Side | Pitches | Avg Adv | Median Adv | Grid xwOBA | League xwOBA | LS 20-80 | LS 0-100 | Type/Side Rank |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 467 | Jones, Breyln | NEW_JER6 | Cutter | RHH | 46 | 0.0085 | 0.0000 | 0.2276 | 0.2361 | 55.7 | 74.3 | 1 |
| 554 | Bell, Brendan | NEW_ENG23 | Cutter | RHH | 41 | 0.0073 | 0.0075 | 0.2287 | 0.2361 | 53.8 | 69.5 | 2 |
| 565 | Maietta, Dante | WIN_CIT29 | Cutter | RHH | 33 | 0.0072 | 0.0000 | 0.2289 | 0.2361 | 53.6 | 68.9 | 3 |
| 579 | Good, Ty | GAT_GRI | Cutter | RHH | 40 | 0.0071 | 0.0010 | 0.2290 | 0.2361 | 53.4 | 68.1 | 4 |
| 677 | Ginn, Landon | WAS_WIL3 | Cutter | RHH | 62 | 0.0061 | 0.0000 | 0.2300 | 0.2361 | 51.7 | 62.7 | 5 |
| 738 | Baird, Dustin | MIS_MUD | Cutter | RHH | 30 | 0.0056 | 0.0000 | 0.2305 | 0.2361 | 50.8 | 59.3 | 6 |
| 775 | Wiltse, Ryan | EVA_OTT | Cutter | RHH | 48 | 0.0053 | 0.0000 | 0.2308 | 0.2361 | 50.4 | 57.3 | 7 |
| 798 | Lockhart, Gauge | LAK_ERI24 | Cutter | RHH | 71 | 0.0051 | 0.0000 | 0.2310 | 0.2361 | 50.1 | 56.0 | 8 |
| 910 | Campbell, AJ | WIN_CIT29 | Cutter | RHH | 50 | 0.0042 | 0.0000 | 0.2319 | 0.2361 | 48.5 | 49.8 | 9 |
| 917 | Majick, Eli | NEW_ENG23 | Cutter | RHH | 60 | 0.0041 | 0.0062 | 0.2320 | 0.2361 | 48.4 | 49.4 | 10 |
| 922 | Thiels, Brenton | MIS_MUD | Cutter | RHH | 28 | 0.0041 | 0.0000 | 0.2320 | 0.2361 | 48.4 | 49.1 | 11 |
| 931 | Salata, Derek | SCH_BOO | Cutter | RHH | 72 | 0.0040 | 0.0000 | 0.2321 | 0.2361 | 48.2 | 48.6 | 12 |
| 963 | Valdez, Alex | EVA_OTT | Cutter | RHH | 65 | 0.0038 | 0.0000 | 0.2323 | 0.2361 | 47.8 | 46.9 | 13 |
| 1029 | Correa, Nelvin | QUE_CAP | Cutter | RHH | 55 | 0.0033 | 0.0000 | 0.2328 | 0.2361 | 47.0 | 43.2 | 14 |
| 1042 | Simone, Andrew | TRO_AIG | Cutter | RHH | 25 | 0.0032 | 0.0000 | 0.2329 | 0.2361 | 46.8 | 42.5 | 15 |

### Four-Seam vs LHH

| Rank | Pitcher | Team | Pitch Type | Batter Side | Pitches | Avg Adv | Median Adv | Grid xwOBA | League xwOBA | LS 20-80 | LS 0-100 | Type/Side Rank |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 49 | Wehrle, Tyler | WIN_CIT29 | Four-Seam | LHH | 80 | 0.0185 | 0.0227 | 0.2250 | 0.2435 | 72.6 | 97.3 | 1 |
| 79 | Parsons, Billy | SUS_COU1 | Four-Seam | LHH | 173 | 0.0169 | 0.0174 | 0.2266 | 0.2435 | 69.9 | 95.7 | 2 |
| 81 | Brothers, Kellen | SUS_COU1 | Four-Seam | LHH | 181 | 0.0168 | 0.0174 | 0.2267 | 0.2435 | 69.7 | 95.6 | 3 |
| 96 | Masick, Jason | NEW_YOR13 | Four-Seam | LHH | 42 | 0.0157 | 0.0078 | 0.2278 | 0.2435 | 67.9 | 94.8 | 4 |
| 100 | Davis, Tyler | WAS_WIL3 | Four-Seam | LHH | 48 | 0.0155 | 0.0175 | 0.2280 | 0.2435 | 67.5 | 94.5 | 5 |
| 140 | Alpern, Liam | FLO_Y'A | Four-Seam | LHH | 86 | 0.0139 | 0.0103 | 0.2296 | 0.2435 | 64.8 | 92.3 | 6 |
| 144 | Ferguson, Francis | QUE_CAP | Four-Seam | LHH | 51 | 0.0138 | 0.0139 | 0.2297 | 0.2435 | 64.7 | 92.1 | 7 |
| 149 | Hughes, Grif | EVA_OTT | Four-Seam | LHH | 30 | 0.0137 | 0.0080 | 0.2298 | 0.2435 | 64.5 | 91.8 | 8 |
| 154 | Herbert, Andrew | WAS_WIL3 | Four-Seam | LHH | 35 | 0.0136 | 0.0161 | 0.2299 | 0.2435 | 64.3 | 91.6 | 9 |
| 155 | Foster, Kobe | WAS_WIL3 | Four-Seam | LHH | 180 | 0.0136 | 0.0162 | 0.2300 | 0.2435 | 64.3 | 91.5 | 10 |
| 158 | Fowler, Dalton | SUS_COU1 | Four-Seam | LHH | 43 | 0.0135 | 0.0184 | 0.2300 | 0.2435 | 64.2 | 91.3 | 11 |
| 163 | Toribio, Noe | TRO_AIG | Four-Seam | LHH | 25 | 0.0134 | 0.0091 | 0.2301 | 0.2435 | 64.0 | 91.1 | 12 |
| 197 | Smith, Ben | NEW_ENG23 | Four-Seam | LHH | 45 | 0.0126 | 0.0123 | 0.2309 | 0.2435 | 62.6 | 89.2 | 13 |
| 217 | Agosto, Justus | TRI_VAL | Four-Seam | LHH | 45 | 0.0122 | 0.0091 | 0.2313 | 0.2435 | 62.0 | 88.1 | 14 |
| 226 | Morgan, Cooper | QUE_CAP | Four-Seam | LHH | 43 | 0.0121 | 0.0161 | 0.2314 | 0.2435 | 61.8 | 87.6 | 15 |

### Four-Seam vs RHH

| Rank | Pitcher | Team | Pitch Type | Batter Side | Pitches | Avg Adv | Median Adv | Grid xwOBA | League xwOBA | LS 20-80 | LS 0-100 | Type/Side Rank |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 21 | Mercado, Nelson | OTT_TIT | Four-Seam | RHH | 42 | 0.0224 | 0.0239 | 0.2144 | 0.2368 | 79.2 | 98.9 | 1 |
| 33 | Kemlage, Joe | NEW_ENG23 | Four-Seam | RHH | 26 | 0.0205 | 0.0190 | 0.2163 | 0.2368 | 76.0 | 98.2 | 2 |
| 34 | Johnson, Preston | MIS_MUD | Four-Seam | RHH | 28 | 0.0201 | 0.0214 | 0.2168 | 0.2368 | 75.2 | 98.2 | 3 |
| 41 | O'Dell, Casey | JOL_SLA | Four-Seam | RHH | 66 | 0.0195 | 0.0220 | 0.2174 | 0.2368 | 74.2 | 97.8 | 4 |
| 50 | Delvecchio, Dylan | LAK_ERI24 | Four-Seam | RHH | 25 | 0.0185 | 0.0244 | 0.2184 | 0.2368 | 72.6 | 97.3 | 5 |
| 55 | Brothers, Kellen | SUS_COU1 | Four-Seam | RHH | 170 | 0.0182 | 0.0163 | 0.2186 | 0.2368 | 72.1 | 97.0 | 6 |
| 63 | Ginn, Landon | WAS_WIL3 | Four-Seam | RHH | 68 | 0.0180 | 0.0154 | 0.2189 | 0.2368 | 71.7 | 96.6 | 7 |
| 67 | Hughes, Grif | EVA_OTT | Four-Seam | RHH | 27 | 0.0174 | 0.0000 | 0.2194 | 0.2368 | 70.8 | 96.4 | 8 |
| 68 | Albert, Wes | DOW_EAS1 | Four-Seam | RHH | 28 | 0.0174 | 0.0085 | 0.2195 | 0.2368 | 70.7 | 96.3 | 9 |
| 71 | Petraitis, AJ | LEM_COL | Four-Seam | RHH | 29 | 0.0172 | 0.0223 | 0.2196 | 0.2368 | 70.4 | 96.1 | 10 |
| 83 | Albert, Wes | TRI_VAL | Four-Seam | RHH | 54 | 0.0166 | 0.0207 | 0.2203 | 0.2368 | 69.4 | 95.5 | 11 |
| 84 | De Los Santos, Enmanuel | NEW_ENG23 | Four-Seam | RHH | 119 | 0.0164 | 0.0106 | 0.2204 | 0.2368 | 69.1 | 95.4 | 12 |
| 87 | Roitman, Justin | WAG_SEA | Four-Seam | RHH | 40 | 0.0161 | 0.0000 | 0.2207 | 0.2368 | 68.6 | 95.3 | 13 |
| 88 | Kalisky, Jack | OTT_TIT | Four-Seam | RHH | 52 | 0.0161 | 0.0234 | 0.2207 | 0.2368 | 68.6 | 95.2 | 14 |
| 93 | Gardner, Sam | GAT_GRI | Four-Seam | RHH | 27 | 0.0159 | 0.0219 | 0.2209 | 0.2368 | 68.3 | 94.9 | 15 |

### Sinker vs LHH

| Rank | Pitcher | Team | Pitch Type | Batter Side | Pitches | Avg Adv | Median Adv | Grid xwOBA | League xwOBA | LS 20-80 | LS 0-100 | Type/Side Rank |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 223 | Aldeano, Austin | TRO_AIG | Sinker | LHH | 45 | 0.0122 | 0.0143 | 0.2473 | 0.2595 | 61.9 | 87.7 | 1 |
| 237 | Sechrist, Zander | WAS_WIL3 | Sinker | LHH | 32 | 0.0118 | 0.0048 | 0.2476 | 0.2595 | 61.4 | 87.0 | 2 |
| 289 | Williams, Pierce | NEW_ENG23 | Sinker | LHH | 29 | 0.0110 | 0.0143 | 0.2485 | 0.2595 | 60.0 | 84.1 | 3 |
| 360 | McCartney, Seth | MIS_MUD | Sinker | LHH | 67 | 0.0098 | 0.0056 | 0.2497 | 0.2595 | 58.0 | 80.2 | 4 |
| 371 | Cook, Cole | SCH_BOO | Sinker | LHH | 55 | 0.0096 | 0.0143 | 0.2499 | 0.2595 | 57.6 | 79.6 | 5 |
| 402 | Castro, Alexander | TRO_AIG | Sinker | LHH | 38 | 0.0092 | 0.0085 | 0.2503 | 0.2595 | 56.9 | 77.9 | 6 |
| 407 | Kelly, Aiden | TRI_VAL | Sinker | LHH | 51 | 0.0091 | 0.0000 | 0.2503 | 0.2595 | 56.8 | 77.6 | 7 |
| 418 | Mannering, Shawn | DOW_EAS1 | Sinker | LHH | 27 | 0.0091 | 0.0075 | 0.2504 | 0.2595 | 56.7 | 77.0 | 8 |
| 427 | Delongchamp, Luke | TRI_VAL | Sinker | LHH | 54 | 0.0089 | 0.0073 | 0.2505 | 0.2595 | 56.5 | 76.5 | 9 |
| 451 | Stuka, Ted | OTT_TIT | Sinker | LHH | 85 | 0.0087 | 0.0009 | 0.2508 | 0.2595 | 56.1 | 75.2 | 10 |
| 456 | Reeves, Cobe | NEW_YOR13 | Sinker | LHH | 56 | 0.0086 | 0.0064 | 0.2508 | 0.2595 | 56.0 | 74.9 | 11 |
| 458 | Sabatine, Gino | TRI_VAL | Sinker | LHH | 36 | 0.0086 | 0.0028 | 0.2509 | 0.2595 | 55.9 | 74.8 | 12 |
| 459 | Kines, Gunnar | JOL_SLA | Sinker | LHH | 73 | 0.0086 | 0.0143 | 0.2509 | 0.2595 | 55.9 | 74.7 | 13 |
| 508 | Fauci, Sonny | NEW_JER6 | Sinker | LHH | 57 | 0.0079 | 0.0000 | 0.2515 | 0.2595 | 54.8 | 72.0 | 14 |
| 517 | Allemann, Braeden | QUE_CAP | Sinker | LHH | 44 | 0.0078 | 0.0000 | 0.2517 | 0.2595 | 54.5 | 71.5 | 15 |

### Sinker vs RHH

| Rank | Pitcher | Team | Pitch Type | Batter Side | Pitches | Avg Adv | Median Adv | Grid xwOBA | League xwOBA | LS 20-80 | LS 0-100 | Type/Side Rank |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 173 | Carsten, Will | FLO_Y'A | Sinker | RHH | 30 | 0.0131 | 0.0127 | 0.2381 | 0.2512 | 63.5 | 90.5 | 1 |
| 174 | Leach, Landon | TRO_AIG | Sinker | RHH | 54 | 0.0130 | 0.0083 | 0.2381 | 0.2512 | 63.4 | 90.4 | 2 |
| 198 | Aldeano, Austin | TRO_AIG | Sinker | RHH | 25 | 0.0126 | 0.0189 | 0.2386 | 0.2512 | 62.6 | 89.1 | 3 |
| 205 | Donnan, Blake | FLO_Y'A | Sinker | RHH | 84 | 0.0124 | 0.0147 | 0.2387 | 0.2512 | 62.4 | 88.7 | 4 |
| 287 | Petschke, Ben | EVA_OTT | Sinker | RHH | 42 | 0.0110 | 0.0101 | 0.2402 | 0.2512 | 60.0 | 84.2 | 5 |
| 303 | Garcia, Andrew | EVA_OTT | Sinker | RHH | 29 | 0.0106 | 0.0091 | 0.2406 | 0.2512 | 59.3 | 83.3 | 6 |
| 315 | Glickstein, Aaron | SCH_BOO | Sinker | RHH | 75 | 0.0104 | 0.0143 | 0.2408 | 0.2512 | 59.0 | 82.7 | 7 |
| 335 | Delongchamp, Luke | TRI_VAL | Sinker | RHH | 59 | 0.0102 | 0.0033 | 0.2410 | 0.2512 | 58.6 | 81.6 | 8 |
| 342 | Campbell, AJ | WIN_CIT29 | Sinker | RHH | 31 | 0.0100 | 0.0180 | 0.2411 | 0.2512 | 58.4 | 81.2 | 9 |
| 356 | Turner, Eric | JOL_SLA | Sinker | RHH | 53 | 0.0099 | 0.0083 | 0.2413 | 0.2512 | 58.1 | 80.4 | 10 |
| 370 | Vecerka, Boris | QUE_CAP | Sinker | RHH | 94 | 0.0096 | 0.0059 | 0.2416 | 0.2512 | 57.6 | 79.6 | 11 |
| 410 | Hoeymans, Jack | GAT_GRI | Sinker | RHH | 35 | 0.0091 | 0.0000 | 0.2421 | 0.2512 | 56.8 | 77.4 | 12 |
| 412 | O'Brien, Keenan | SUS_COU1 | Sinker | RHH | 28 | 0.0091 | 0.0041 | 0.2421 | 0.2512 | 56.8 | 77.3 | 13 |
| 425 | Colon, Jeffrey | TRO_AIG | Sinker | RHH | 26 | 0.0089 | 0.0017 | 0.2422 | 0.2512 | 56.5 | 76.6 | 14 |
| 466 | Mannering, Shawn | DOW_EAS1 | Sinker | RHH | 32 | 0.0085 | 0.0000 | 0.2427 | 0.2512 | 55.8 | 74.3 | 15 |

### Slider vs LHH

| Rank | Pitcher | Team | Pitch Type | Batter Side | Pitches | Avg Adv | Median Adv | Grid xwOBA | League xwOBA | LS 20-80 | LS 0-100 | Type/Side Rank |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 127 | Potteiger, Jack | JOL_SLA | Slider | LHH | 30 | 0.0147 | 0.0098 | 0.2224 | 0.2371 | 66.2 | 93.0 | 1 |
| 168 | Foltz Jr., Michael | WAS_WIL3 | Slider | LHH | 26 | 0.0133 | 0.0033 | 0.2238 | 0.2371 | 63.9 | 90.8 | 2 |
| 180 | Barker, Alex | NEW_YOR13 | Slider | LHH | 104 | 0.0129 | 0.0077 | 0.2243 | 0.2371 | 63.1 | 90.1 | 3 |
| 220 | Harris, Everette | TRI_VAL | Slider | LHH | 29 | 0.0122 | 0.0069 | 0.2249 | 0.2371 | 62.0 | 87.9 | 4 |
| 221 | McEvoy, Aidan | FLO_Y'A | Slider | LHH | 76 | 0.0122 | 0.0012 | 0.2249 | 0.2371 | 62.0 | 87.9 | 5 |
| 241 | Dima, Josh | GAT_GRI | Slider | LHH | 75 | 0.0118 | 0.0000 | 0.2254 | 0.2371 | 61.3 | 86.7 | 6 |
| 249 | Eckaus, David | EVA_OTT | Slider | LHH | 119 | 0.0117 | 0.0000 | 0.2255 | 0.2371 | 61.1 | 86.3 | 7 |
| 250 | Campbell, Tyler | MIS_MUD | Slider | LHH | 106 | 0.0116 | 0.0030 | 0.2255 | 0.2371 | 61.0 | 86.3 | 8 |
| 253 | Smith, Ben | NEW_ENG23 | Slider | LHH | 40 | 0.0116 | 0.0000 | 0.2255 | 0.2371 | 60.9 | 86.1 | 9 |
| 261 | Cook, Cole | SCH_BOO | Slider | LHH | 129 | 0.0114 | 0.0036 | 0.2257 | 0.2371 | 60.7 | 85.6 | 10 |
| 277 | Milburn, Isaac | FLO_Y'A | Slider | LHH | 85 | 0.0112 | 0.0044 | 0.2260 | 0.2371 | 60.2 | 84.8 | 11 |
| 278 | Webster, Evan | FLO_Y'A | Slider | LHH | 76 | 0.0111 | 0.0042 | 0.2260 | 0.2371 | 60.2 | 84.7 | 12 |
| 284 | Scott, Brandon | LAK_ERI24 | Slider | LHH | 70 | 0.0111 | 0.0000 | 0.2261 | 0.2371 | 60.1 | 84.4 | 13 |
| 286 | Balzan, Jackson | SUS_COU1 | Slider | LHH | 77 | 0.0110 | 0.0044 | 0.2261 | 0.2371 | 60.0 | 84.3 | 14 |
| 300 | Alpern, Liam | FLO_Y'A | Slider | LHH | 38 | 0.0107 | 0.0000 | 0.2264 | 0.2371 | 59.5 | 83.5 | 15 |

### Slider vs RHH

| Rank | Pitcher | Team | Pitch Type | Batter Side | Pitches | Avg Adv | Median Adv | Grid xwOBA | League xwOBA | LS 20-80 | LS 0-100 | Type/Side Rank |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | Garcia, Hector | WAS_WIL3 | Slider | RHH | 36 | 0.0307 | 0.0283 | 0.1999 | 0.2306 | 80.0 | 100.0 | 1 |
| 2 | Perez, Kelvin | WAS_WIL3 | Slider | RHH | 103 | 0.0268 | 0.0267 | 0.2038 | 0.2306 | 80.0 | 99.9 | 2 |
| 3 | Perdomo, Rafael | QUE_CAP | Slider | RHH | 48 | 0.0265 | 0.0140 | 0.2042 | 0.2306 | 80.0 | 99.9 | 3 |
| 4 | Wiltse, Ryan | EVA_OTT | Slider | RHH | 63 | 0.0262 | 0.0227 | 0.2045 | 0.2306 | 80.0 | 99.8 | 4 |
| 5 | Finarelli, Nick | LON_ISL22 | Slider | RHH | 31 | 0.0252 | 0.0118 | 0.2055 | 0.2306 | 80.0 | 99.8 | 5 |
| 6 | Albert, Wes | DOW_EAS1 | Slider | RHH | 29 | 0.0248 | 0.0025 | 0.2058 | 0.2306 | 80.0 | 99.7 | 6 |
| 7 | Salata, Derek | SCH_BOO | Slider | RHH | 163 | 0.0244 | 0.0201 | 0.2062 | 0.2306 | 80.0 | 99.7 | 7 |
| 8 | Smith, Ethan | WIN_CIT29 | Slider | RHH | 30 | 0.0244 | 0.0113 | 0.2062 | 0.2306 | 80.0 | 99.6 | 8 |
| 9 | Thompson, Ross | SCH_BOO | Slider | RHH | 196 | 0.0241 | 0.0118 | 0.2065 | 0.2306 | 80.0 | 99.6 | 9 |
| 10 | Sanchez, Sergio | MIS_MUD | Slider | RHH | 28 | 0.0241 | 0.0025 | 0.2065 | 0.2306 | 80.0 | 99.5 | 10 |
| 11 | Cameron, Wyatt | SCH_BOO | Slider | RHH | 50 | 0.0239 | 0.0019 | 0.2067 | 0.2306 | 80.0 | 99.4 | 11 |
| 12 | Blair, Davis | DOW_EAS1 | Slider | RHH | 61 | 0.0238 | 0.0110 | 0.2069 | 0.2306 | 80.0 | 99.4 | 12 |
| 13 | Gilleran, Jimmy | NEW_ENG23 | Slider | RHH | 97 | 0.0237 | 0.0170 | 0.2069 | 0.2306 | 80.0 | 99.3 | 13 |
| 14 | Kirby, Zach | WAS_WIL3 | Slider | RHH | 126 | 0.0234 | 0.0116 | 0.2072 | 0.2306 | 80.0 | 99.3 | 14 |
| 15 | Morrissey, Joe | EVA_OTT | Slider | RHH | 47 | 0.0234 | 0.0273 | 0.2072 | 0.2306 | 80.0 | 99.2 | 15 |

### Splitter vs LHH

| Rank | Pitcher | Team | Pitch Type | Batter Side | Pitches | Avg Adv | Median Adv | Grid xwOBA | League xwOBA | LS 20-80 | LS 0-100 | Type/Side Rank |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1057 | Coles, Chad | WAS_WIL3 | Splitter | LHH | 38 | 0.0031 | 0.0000 | 0.2375 | 0.2405 | 46.6 | 41.7 | 1 |
| 1077 | Eldred, Zach | NEW_ENG23 | Splitter | LHH | 46 | 0.0029 | 0.0000 | 0.2376 | 0.2405 | 46.4 | 40.6 | 2 |
| 1168 | Thornton, Tyler | NEW_ENG23 | Splitter | LHH | 69 | 0.0023 | 0.0000 | 0.2383 | 0.2405 | 45.3 | 35.6 | 3 |
| 1177 | Soto, Carlos | JOL_SLA | Splitter | LHH | 31 | 0.0022 | 0.0000 | 0.2383 | 0.2405 | 45.2 | 35.1 | 4 |
| 1216 | Perozzi, John | SUS_COU1 | Splitter | LHH | 34 | 0.0019 | 0.0000 | 0.2386 | 0.2405 | 44.7 | 32.9 | 5 |
| 1222 | Williams, Brian | MIS_MUD | Splitter | LHH | 57 | 0.0019 | 0.0000 | 0.2387 | 0.2405 | 44.6 | 32.6 | 6 |
| 1261 | Vitas, Ben | JOL_SLA | Splitter | LHH | 91 | 0.0016 | 0.0000 | 0.2390 | 0.2405 | 44.1 | 30.4 | 7 |
| 1267 | Salata, Derek | SCH_BOO | Splitter | LHH | 90 | 0.0016 | 0.0000 | 0.2390 | 0.2405 | 44.1 | 30.1 | 8 |
| 1294 | Pindel, Buddie | SCH_BOO | Splitter | LHH | 58 | 0.0014 | 0.0000 | 0.2391 | 0.2405 | 43.8 | 28.6 | 9 |
| 1341 | Thompson, Ross | SCH_BOO | Splitter | LHH | 145 | 0.0011 | 0.0000 | 0.2394 | 0.2405 | 43.4 | 26.0 | 10 |
| 1346 | Garcia, Hector | WAS_WIL3 | Splitter | LHH | 59 | 0.0011 | 0.0000 | 0.2395 | 0.2405 | 43.3 | 25.7 | 11 |
| 1384 | Parsons, Billy | SUS_COU1 | Splitter | LHH | 33 | 0.0008 | 0.0000 | 0.2398 | 0.2405 | 42.7 | 23.6 | 12 |
| 1420 | Villers, Ian | QUE_CAP | Splitter | LHH | 39 | 0.0005 | 0.0000 | 0.2400 | 0.2405 | 42.3 | 21.6 | 13 |
| 1440 | Orth, Harry | SCH_BOO | Splitter | LHH | 31 | 0.0003 | 0.0000 | 0.2402 | 0.2405 | 42.0 | 20.5 | 14 |
| 1477 | Shears, Tanner | SCH_BOO | Splitter | LHH | 37 | 0.0000 | 0.0000 | 0.2405 | 0.2405 | 41.5 | 18.5 | 15 |

### Splitter vs RHH

| Rank | Pitcher | Team | Pitch Type | Batter Side | Pitches | Avg Adv | Median Adv | Grid xwOBA | League xwOBA | LS 20-80 | LS 0-100 | Type/Side Rank |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1142 | Villers, Ian | QUE_CAP | Splitter | RHH | 25 | 0.0025 | 0.0024 | 0.2427 | 0.2452 | 45.6 | 37.0 | 1 |
| 1259 | Pindel, Buddie | SCH_BOO | Splitter | RHH | 32 | 0.0016 | 0.0000 | 0.2436 | 0.2452 | 44.2 | 30.5 | 2 |
| 1454 | Andueza, Axel | DOW_EAS1 | Splitter | RHH | 26 | 0.0003 | 0.0000 | 0.2449 | 0.2452 | 41.9 | 19.8 | 3 |
| 1467 | Williams, Brian | MIS_MUD | Splitter | RHH | 44 | 0.0001 | 0.0000 | 0.2450 | 0.2452 | 41.7 | 19.1 | 4 |
| 1498 | Coles, Chad | WAS_WIL3 | Splitter | RHH | 25 | -0.0001 | 0.0000 | 0.2453 | 0.2452 | 41.2 | 17.3 | 5 |
| 1508 | Eldred, Zach | NEW_ENG23 | Splitter | RHH | 35 | -0.0002 | 0.0000 | 0.2454 | 0.2452 | 41.1 | 16.8 | 6 |
| 1511 | Shears, Tanner | SCH_BOO | Splitter | RHH | 37 | -0.0002 | 0.0000 | 0.2454 | 0.2452 | 41.0 | 16.6 | 7 |
| 1562 | Thornton, Tyler | NEW_ENG23 | Splitter | RHH | 50 | -0.0008 | 0.0000 | 0.2460 | 0.2452 | 40.0 | 13.8 | 8 |
| 1601 | Vitas, Ben | JOL_SLA | Splitter | RHH | 36 | -0.0012 | 0.0000 | 0.2464 | 0.2452 | 39.3 | 11.7 | 9 |
| 1620 | MacMillan, Blake | TRO_AIG | Splitter | RHH | 31 | -0.0015 | 0.0000 | 0.2467 | 0.2452 | 38.9 | 10.6 | 10 |
| 1659 | Nakata, Yuto | QUE_CAP | Splitter | RHH | 32 | -0.0020 | 0.0000 | 0.2471 | 0.2452 | 38.1 | 8.4 | 11 |
| 1755 | Thompson, Ross | SCH_BOO | Splitter | RHH | 30 | -0.0040 | 0.0000 | 0.2492 | 0.2452 | 34.7 | 3.1 | 12 |

### Sweeper vs RHH

| Rank | Pitcher | Team | Pitch Type | Batter Side | Pitches | Avg Adv | Median Adv | Grid xwOBA | League xwOBA | LS 20-80 | LS 0-100 | Type/Side Rank |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1484 | Cerda, Junior | EVA_OTT | Sweeper | RHH | 41 | -0.0000 | 0.0000 | 0.1884 | 0.1884 | 41.4 | 18.1 | 1 |
| 1489 | Simpson, Garret | EVA_OTT | Sweeper | RHH | 32 | -0.0001 | 0.0000 | 0.1885 | 0.1884 | 41.3 | 17.8 | 2 |
