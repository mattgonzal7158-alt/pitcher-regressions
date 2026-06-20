# Location Score Report

- Pitch input file: `data\processed\2026-data-with-woba-xwoba.parquet`
- Location grid input file: `data\processed\location_value_grid.csv`
- Output file: `data\processed\location_scores.csv`
- Assigned pitch rows: 91,744
- Qualified pitcher + pitch type + batter side rows: 1,187
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
| 1 | Binns, Malik | NEW_JER6 | Four-Seam | RHH | 25 | 0.0190 | 0.0151 | 0.2210 | 0.2400 | 80.0 | 100.0 | 1 |
| 2 | Perez, Kelvin | WAS_WIL3 | Slider | RHH | 45 | 0.0183 | 0.0152 | 0.2117 | 0.2301 | 80.0 | 99.9 | 1 |
| 3 | McCartney, Seth | MIS_MUD | Slider | RHH | 36 | 0.0171 | 0.0034 | 0.2130 | 0.2301 | 80.0 | 99.8 | 2 |
| 4 | Nova, Fraynel | LAK_ERI24 | Slider | RHH | 100 | 0.0171 | 0.0118 | 0.2130 | 0.2301 | 80.0 | 99.7 | 3 |
| 5 | Smith, Ethan | WIN_CIT29 | Slider | RHH | 30 | 0.0167 | 0.0007 | 0.2133 | 0.2301 | 80.0 | 99.7 | 4 |
| 6 | Reeves, Cobe | NEW_YOR13 | Four-Seam | RHH | 27 | 0.0167 | 0.0204 | 0.2233 | 0.2400 | 80.0 | 99.6 | 2 |
| 7 | Blair, Davis | DOW_EAS1 | Slider | RHH | 61 | 0.0163 | 0.0095 | 0.2137 | 0.2301 | 79.2 | 99.5 | 5 |
| 8 | Long, Maddox | WAS_WIL3 | Changeup | LHH | 31 | 0.0162 | 0.0167 | 0.2273 | 0.2436 | 79.0 | 99.4 | 1 |
| 9 | Willeman, Landon | EVA_OTT | Slider | RHH | 33 | 0.0157 | 0.0000 | 0.2143 | 0.2301 | 77.9 | 99.3 | 6 |
| 10 | Petraitis, AJ | LEM_COL | Four-Seam | RHH | 29 | 0.0151 | 0.0078 | 0.2249 | 0.2400 | 76.6 | 99.2 | 3 |
| 11 | Wehrle, Tyler | WIN_CIT29 | Four-Seam | LHH | 75 | 0.0151 | 0.0141 | 0.2315 | 0.2466 | 76.5 | 99.2 | 1 |
| 12 | Belton, Hunter | MIS_MUD | Slider | RHH | 75 | 0.0150 | 0.0058 | 0.2151 | 0.2301 | 76.3 | 99.1 | 7 |
| 13 | Perdomo, Rafael | QUE_CAP | Slider | RHH | 46 | 0.0149 | 0.0007 | 0.2152 | 0.2301 | 76.0 | 99.0 | 8 |
| 14 | Perozzi, John | SUS_COU1 | Slider | RHH | 46 | 0.0148 | 0.0152 | 0.2152 | 0.2301 | 76.0 | 98.9 | 9 |
| 15 | Gamelin, Shaun | JOL_SLA | Slider | RHH | 31 | 0.0148 | 0.0102 | 0.2153 | 0.2301 | 75.8 | 98.8 | 10 |
| 16 | Sechrist, Zander | WAS_WIL3 | Sinker | LHH | 28 | 0.0147 | 0.0045 | 0.2485 | 0.2632 | 75.7 | 98.7 | 1 |
| 17 | Whitesell, Max | FLO_Y'A | Slider | RHH | 77 | 0.0145 | 0.0050 | 0.2155 | 0.2301 | 75.3 | 98.7 | 11 |
| 18 | Cohn, Cooper | NIU_HUS | Slider | RHH | 27 | 0.0145 | 0.0000 | 0.2155 | 0.2301 | 75.3 | 98.6 | 12 |
| 19 | Davis, Tyler | WAS_WIL3 | Four-Seam | LHH | 48 | 0.0144 | 0.0141 | 0.2323 | 0.2466 | 75.0 | 98.5 | 2 |
| 20 | Salata, Derek | SCH_BOO | Slider | RHH | 100 | 0.0142 | 0.0082 | 0.2158 | 0.2301 | 74.7 | 98.4 | 13 |
| 21 | Smith, Jackson | MIS_MUD | Changeup | LHH | 26 | 0.0142 | 0.0086 | 0.2294 | 0.2436 | 74.5 | 98.3 | 2 |
| 22 | Wiltse, Ryan | EVA_OTT | Slider | RHH | 35 | 0.0140 | 0.0082 | 0.2160 | 0.2301 | 74.3 | 98.2 | 14 |
| 23 | Garcia, Hector | WAS_WIL3 | Slider | RHH | 36 | 0.0139 | 0.0075 | 0.2161 | 0.2301 | 74.1 | 98.1 | 15 |
| 24 | Hagan, Jack | DOW_EAS1 | Slider | RHH | 73 | 0.0138 | 0.0082 | 0.2163 | 0.2301 | 73.7 | 98.1 | 16 |
| 25 | Pindel, Buddie | SCH_BOO | Slider | RHH | 66 | 0.0136 | 0.0000 | 0.2165 | 0.2301 | 73.3 | 98.0 | 17 |
| 26 | Bargo, Casey | NEW_ENG23 | Slider | RHH | 29 | 0.0131 | 0.0095 | 0.2169 | 0.2301 | 72.3 | 97.9 | 18 |
| 27 | Leak, Anthony | NEW_YOR13 | Slider | RHH | 94 | 0.0130 | 0.0045 | 0.2170 | 0.2301 | 72.0 | 97.8 | 19 |
| 28 | Duby, Bill | NEW_JER6 | Slider | RHH | 38 | 0.0128 | 0.0073 | 0.2173 | 0.2301 | 71.6 | 97.7 | 20 |
| 29 | Ginn, Landon | WAS_WIL3 | Four-Seam | RHH | 44 | 0.0128 | 0.0080 | 0.2272 | 0.2400 | 71.6 | 97.6 | 4 |
| 30 | Mercado, Nelson | OTT_TIT | Four-Seam | RHH | 42 | 0.0127 | 0.0074 | 0.2273 | 0.2400 | 71.5 | 97.6 | 5 |

## Top Location Scores by Pitch Type and Batter Side

### Changeup vs LHH

| Rank | Pitcher | Team | Pitch Type | Batter Side | Pitches | Avg Adv | Median Adv | Grid xwOBA | League xwOBA | LS 20-80 | LS 0-100 | Type/Side Rank |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 8 | Long, Maddox | WAS_WIL3 | Changeup | LHH | 31 | 0.0162 | 0.0167 | 0.2273 | 0.2436 | 79.0 | 99.4 | 1 |
| 21 | Smith, Jackson | MIS_MUD | Changeup | LHH | 26 | 0.0142 | 0.0086 | 0.2294 | 0.2436 | 74.5 | 98.3 | 2 |
| 34 | Dill, Austin | TRI_VAL | Changeup | LHH | 107 | 0.0126 | 0.0133 | 0.2310 | 0.2436 | 71.2 | 97.2 | 3 |
| 37 | Hicks, Jackson | DOW_EAS1 | Changeup | LHH | 25 | 0.0125 | 0.0000 | 0.2311 | 0.2436 | 70.9 | 97.0 | 4 |
| 45 | Burcham, Jacob | GAT_GRI | Changeup | LHH | 42 | 0.0120 | 0.0066 | 0.2316 | 0.2436 | 69.8 | 96.3 | 5 |
| 76 | Hampton, Ky | OTT_TIT | Changeup | LHH | 74 | 0.0103 | 0.0135 | 0.2333 | 0.2436 | 66.2 | 93.7 | 6 |
| 96 | Kirby, Zach | WAS_WIL3 | Changeup | LHH | 114 | 0.0096 | 0.0022 | 0.2340 | 0.2436 | 64.7 | 92.0 | 7 |
| 111 | Albert, Wes | TRI_VAL | Changeup | LHH | 38 | 0.0091 | 0.0000 | 0.2345 | 0.2436 | 63.6 | 90.7 | 8 |
| 113 | Maietta, Dante | WIN_CIT29 | Changeup | LHH | 68 | 0.0090 | 0.0022 | 0.2345 | 0.2436 | 63.5 | 90.6 | 9 |
| 120 | Huter, Blayne | SUS_COU1 | Changeup | LHH | 30 | 0.0088 | 0.0043 | 0.2348 | 0.2436 | 63.0 | 90.0 | 10 |
| 126 | Vailes, Gage | GAT_GRI | Changeup | LHH | 79 | 0.0087 | 0.0010 | 0.2349 | 0.2436 | 62.8 | 89.5 | 11 |
| 130 | Martinez, Mason | TRI_VAL | Changeup | LHH | 51 | 0.0087 | 0.0053 | 0.2349 | 0.2436 | 62.7 | 89.1 | 12 |
| 132 | Drakeford, Dosie | NEW_JER6 | Changeup | LHH | 26 | 0.0085 | 0.0022 | 0.2351 | 0.2436 | 62.3 | 89.0 | 13 |
| 142 | Whitesell, Max | FLO_Y'A | Changeup | LHH | 33 | 0.0083 | 0.0000 | 0.2353 | 0.2436 | 61.8 | 88.1 | 14 |
| 157 | Long, Jalon | NEW_YOR13 | Changeup | LHH | 45 | 0.0079 | 0.0000 | 0.2357 | 0.2436 | 61.1 | 86.9 | 15 |

### Changeup vs RHH

| Rank | Pitcher | Team | Pitch Type | Batter Side | Pitches | Avg Adv | Median Adv | Grid xwOBA | League xwOBA | LS 20-80 | LS 0-100 | Type/Side Rank |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 60 | Toribio, Noe | TRO_AIG | Changeup | RHH | 27 | 0.0110 | 0.0098 | 0.2389 | 0.2498 | 67.6 | 95.0 | 1 |
| 77 | Alpern, Liam | FLO_Y'A | Changeup | RHH | 38 | 0.0103 | 0.0009 | 0.2396 | 0.2498 | 66.2 | 93.6 | 2 |
| 216 | Sanchez, Edwin | LAK_ERI24 | Changeup | RHH | 43 | 0.0067 | 0.0000 | 0.2431 | 0.2498 | 58.6 | 81.9 | 3 |
| 220 | Thornton, Tyler | NEW_ENG23 | Changeup | RHH | 25 | 0.0067 | 0.0060 | 0.2432 | 0.2498 | 58.4 | 81.6 | 4 |
| 237 | Reeves, Cobe | NEW_YOR13 | Changeup | RHH | 33 | 0.0065 | 0.0000 | 0.2433 | 0.2498 | 58.0 | 80.1 | 5 |
| 246 | Villalobos, Jonaiker | FLO_Y'A | Changeup | RHH | 104 | 0.0064 | 0.0011 | 0.2434 | 0.2498 | 57.8 | 79.4 | 6 |
| 249 | Fry, Dale | LON_ISL22 | Changeup | RHH | 26 | 0.0064 | 0.0005 | 0.2435 | 0.2498 | 57.7 | 79.1 | 7 |
| 269 | Parra, Andres | LAK_ERI24 | Changeup | RHH | 41 | 0.0061 | 0.0000 | 0.2437 | 0.2498 | 57.1 | 77.4 | 8 |
| 300 | Gollert, Harley | QUE_CAP | Changeup | RHH | 38 | 0.0055 | 0.0000 | 0.2443 | 0.2498 | 55.9 | 74.8 | 9 |
| 323 | Barker, Alex | NEW_YOR13 | Changeup | RHH | 61 | 0.0053 | 0.0000 | 0.2445 | 0.2498 | 55.4 | 72.9 | 10 |
| 354 | Sakurai, Masatoshi | QUE_CAP | Changeup | RHH | 91 | 0.0049 | 0.0000 | 0.2450 | 0.2498 | 54.5 | 70.3 | 11 |
| 359 | Heredia-Bustos, Rolando | DOW_EAS1 | Changeup | RHH | 42 | 0.0048 | -0.0006 | 0.2450 | 0.2498 | 54.4 | 69.8 | 12 |
| 361 | Galva, Claudio | GAT_GRI | Changeup | RHH | 45 | 0.0048 | 0.0019 | 0.2451 | 0.2498 | 54.3 | 69.7 | 13 |
| 377 | Pierson, Kenny | LAK_ERI24 | Changeup | RHH | 104 | 0.0046 | 0.0014 | 0.2452 | 0.2498 | 54.0 | 68.3 | 14 |
| 425 | Maietta, Dante | WIN_CIT29 | Changeup | RHH | 44 | 0.0041 | 0.0000 | 0.2457 | 0.2498 | 52.8 | 64.3 | 15 |

### Curveball vs LHH

| Rank | Pitcher | Team | Pitch Type | Batter Side | Pitches | Avg Adv | Median Adv | Grid xwOBA | League xwOBA | LS 20-80 | LS 0-100 | Type/Side Rank |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 309 | Good, Ty | GAT_GRI | Curveball | LHH | 33 | 0.0054 | 0.0000 | 0.2420 | 0.2475 | 55.7 | 74.1 | 1 |
| 393 | Langrell, Connor | MIS_MUD | Curveball | LHH | 35 | 0.0044 | 0.0000 | 0.2430 | 0.2475 | 53.5 | 67.0 | 2 |
| 406 | Shinn, Nathan | LAK_ERI24 | Curveball | LHH | 29 | 0.0043 | 0.0000 | 0.2432 | 0.2475 | 53.2 | 65.9 | 3 |
| 459 | Williams, Pierce | NEW_ENG23 | Curveball | LHH | 52 | 0.0037 | 0.0000 | 0.2437 | 0.2475 | 52.0 | 61.4 | 4 |
| 542 | Peters, Garrett | NEW_YOR13 | Curveball | LHH | 62 | 0.0030 | 0.0000 | 0.2445 | 0.2475 | 50.4 | 54.4 | 5 |
| 561 | Puccetti, Dominic | OTT_TIT | Curveball | LHH | 104 | 0.0027 | 0.0000 | 0.2447 | 0.2475 | 49.9 | 52.8 | 6 |
| 573 | Noriega, Branden | LAK_ERI24 | Curveball | LHH | 29 | 0.0026 | 0.0000 | 0.2449 | 0.2475 | 49.6 | 51.8 | 7 |
| 578 | Kassebaum, Torin | LON_ISL22 | Curveball | LHH | 25 | 0.0026 | 0.0000 | 0.2449 | 0.2475 | 49.5 | 51.4 | 8 |
| 595 | Martzolf, Max | OTT_TIT | Curveball | LHH | 56 | 0.0024 | 0.0000 | 0.2451 | 0.2475 | 49.2 | 50.0 | 9 |
| 599 | Pierson, Kenny | LAK_ERI24 | Curveball | LHH | 37 | 0.0024 | 0.0000 | 0.2451 | 0.2475 | 49.1 | 49.6 | 10 |
| 623 | Baker, Luke | EVA_OTT | Curveball | LHH | 37 | 0.0021 | 0.0000 | 0.2454 | 0.2475 | 48.5 | 47.6 | 11 |
| 628 | Figueredo, Kevin | WIN_CIT29 | Curveball | LHH | 45 | 0.0021 | 0.0000 | 0.2454 | 0.2475 | 48.5 | 47.2 | 12 |
| 630 | Andueza, Axel | DOW_EAS1 | Curveball | LHH | 72 | 0.0020 | 0.0000 | 0.2454 | 0.2475 | 48.4 | 47.0 | 13 |
| 669 | Rohde, Isaac | NEW_YOR13 | Curveball | LHH | 30 | 0.0017 | 0.0000 | 0.2458 | 0.2475 | 47.7 | 43.7 | 14 |
| 686 | Garcia, Brett | OTT_TIT | Curveball | LHH | 36 | 0.0016 | 0.0000 | 0.2459 | 0.2475 | 47.4 | 42.3 | 15 |

### Curveball vs RHH

| Rank | Pitcher | Team | Pitch Type | Batter Side | Pitches | Avg Adv | Median Adv | Grid xwOBA | League xwOBA | LS 20-80 | LS 0-100 | Type/Side Rank |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 80 | Coles, Chad | WAS_WIL3 | Curveball | RHH | 31 | 0.0102 | 0.0000 | 0.2464 | 0.2566 | 66.0 | 93.3 | 1 |
| 116 | Garcia, Hector | WAS_WIL3 | Curveball | RHH | 27 | 0.0089 | 0.0092 | 0.2478 | 0.2566 | 63.1 | 90.3 | 2 |
| 162 | Plumadore, Carson | WIN_CIT29 | Curveball | RHH | 25 | 0.0078 | 0.0042 | 0.2488 | 0.2566 | 60.9 | 86.4 | 3 |
| 205 | Allemann, Braeden | QUE_CAP | Curveball | RHH | 74 | 0.0070 | 0.0000 | 0.2497 | 0.2566 | 59.0 | 82.8 | 4 |
| 224 | Perdomo, Rafael | QUE_CAP | Curveball | RHH | 26 | 0.0066 | 0.0000 | 0.2500 | 0.2566 | 58.3 | 81.2 | 5 |
| 227 | Henderson, Drew | DOW_EAS1 | Curveball | RHH | 105 | 0.0066 | 0.0000 | 0.2500 | 0.2566 | 58.3 | 81.0 | 6 |
| 242 | Sesar, Jorden | SUS_COU1 | Curveball | RHH | 53 | 0.0064 | 0.0000 | 0.2502 | 0.2566 | 57.9 | 79.7 | 7 |
| 243 | Cameron, Wyatt | SCH_BOO | Curveball | RHH | 33 | 0.0064 | 0.0000 | 0.2502 | 0.2566 | 57.9 | 79.6 | 8 |
| 278 | Langrell, Connor | MIS_MUD | Curveball | RHH | 38 | 0.0059 | 0.0000 | 0.2507 | 0.2566 | 56.8 | 76.7 | 9 |
| 289 | Moore, Kyle | SCH_BOO | Curveball | RHH | 60 | 0.0057 | 0.0003 | 0.2509 | 0.2566 | 56.4 | 75.7 | 10 |
| 308 | Townes, Holland | SCH_BOO | Curveball | RHH | 41 | 0.0055 | 0.0000 | 0.2512 | 0.2566 | 55.8 | 74.1 | 11 |
| 327 | Barron, Oscar | TES_BLA1 | Curveball | RHH | 153 | 0.0052 | 0.0000 | 0.2514 | 0.2566 | 55.3 | 72.5 | 12 |
| 346 | Sechrist, Zander | WAS_WIL3 | Curveball | RHH | 37 | 0.0050 | 0.0000 | 0.2517 | 0.2566 | 54.8 | 70.9 | 13 |
| 350 | Willeman, Landon | EVA_OTT | Curveball | RHH | 37 | 0.0049 | 0.0000 | 0.2517 | 0.2566 | 54.6 | 70.6 | 14 |
| 358 | Helt, Robert | LAK_ERI24 | Curveball | RHH | 44 | 0.0048 | 0.0000 | 0.2518 | 0.2566 | 54.4 | 69.9 | 15 |

### Cutter vs LHH

| Rank | Pitcher | Team | Pitch Type | Batter Side | Pitches | Avg Adv | Median Adv | Grid xwOBA | League xwOBA | LS 20-80 | LS 0-100 | Type/Side Rank |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 506 | Cook, Cole | SCH_BOO | Cutter | LHH | 28 | 0.0033 | 0.0015 | 0.2178 | 0.2211 | 51.1 | 57.5 | 1 |
| 586 | Petschke, Ben | EVA_OTT | Cutter | LHH | 128 | 0.0025 | 0.0000 | 0.2186 | 0.2211 | 49.4 | 50.7 | 2 |
| 590 | Parsons, Billy | SUS_COU1 | Cutter | LHH | 29 | 0.0025 | 0.0000 | 0.2186 | 0.2211 | 49.3 | 50.4 | 3 |
| 605 | McEvoy, Aidan | FLO_Y'A | Cutter | LHH | 29 | 0.0023 | 0.0000 | 0.2187 | 0.2211 | 49.0 | 49.1 | 4 |
| 606 | Sechrist, Zander | WAS_WIL3 | Cutter | LHH | 27 | 0.0023 | 0.0000 | 0.2187 | 0.2211 | 49.0 | 49.0 | 5 |
| 629 | Gamelin, Shaun | JOL_SLA | Cutter | LHH | 51 | 0.0020 | 0.0000 | 0.2190 | 0.2211 | 48.4 | 47.1 | 6 |
| 633 | Salata, Derek | SCH_BOO | Cutter | LHH | 26 | 0.0020 | 0.0000 | 0.2191 | 0.2211 | 48.4 | 46.8 | 7 |
| 683 | Langrell, Connor | MIS_MUD | Cutter | LHH | 50 | 0.0016 | 0.0014 | 0.2195 | 0.2211 | 47.5 | 42.5 | 8 |
| 747 | Webster, Evan | FLO_Y'A | Cutter | LHH | 70 | 0.0011 | 0.0000 | 0.2200 | 0.2211 | 46.4 | 37.2 | 9 |
| 749 | Morgan, Marcus | JOL_SLA | Cutter | LHH | 38 | 0.0011 | 0.0000 | 0.2200 | 0.2211 | 46.4 | 37.0 | 10 |
| 797 | Gorgen, Grady | NEW_YOR13 | Cutter | LHH | 30 | 0.0006 | 0.0000 | 0.2205 | 0.2211 | 45.3 | 32.9 | 11 |
| 798 | Binns, Malik | NEW_JER6 | Cutter | LHH | 30 | 0.0006 | 0.0000 | 0.2205 | 0.2211 | 45.3 | 32.9 | 12 |
| 849 | Parks, Pavin | LAK_ERI24 | Cutter | LHH | 39 | 0.0000 | 0.0000 | 0.2211 | 0.2211 | 44.0 | 28.6 | 13 |
| 926 | Saturria, Michael | NEW_ENG23 | Cutter | LHH | 76 | -0.0007 | 0.0000 | 0.2218 | 0.2211 | 42.5 | 22.1 | 14 |
| 951 | MacMillan, Blake | TRO_AIG | Cutter | LHH | 37 | -0.0010 | 0.0000 | 0.2221 | 0.2211 | 41.8 | 20.0 | 15 |

### Cutter vs RHH

| Rank | Pitcher | Team | Pitch Type | Batter Side | Pitches | Avg Adv | Median Adv | Grid xwOBA | League xwOBA | LS 20-80 | LS 0-100 | Type/Side Rank |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 279 | Wiltse, Ryan | EVA_OTT | Cutter | RHH | 29 | 0.0059 | 0.0000 | 0.2342 | 0.2400 | 56.7 | 76.6 | 1 |
| 441 | Baird, Dustin | MIS_MUD | Cutter | RHH | 30 | 0.0039 | 0.0015 | 0.2362 | 0.2400 | 52.3 | 62.9 | 2 |
| 446 | Correa, Nelvin | QUE_CAP | Cutter | RHH | 28 | 0.0038 | 0.0043 | 0.2362 | 0.2400 | 52.3 | 62.5 | 3 |
| 448 | Parks, Pavin | LAK_ERI24 | Cutter | RHH | 73 | 0.0038 | 0.0000 | 0.2362 | 0.2400 | 52.2 | 62.3 | 4 |
| 476 | Glickstein, Aaron | SCH_BOO | Cutter | RHH | 26 | 0.0036 | 0.0028 | 0.2364 | 0.2400 | 51.8 | 60.0 | 5 |
| 491 | Jones, Breyln | NEW_JER6 | Cutter | RHH | 33 | 0.0035 | 0.0000 | 0.2366 | 0.2400 | 51.5 | 58.7 | 6 |
| 526 | Morgan, Cooper | QUE_CAP | Cutter | RHH | 27 | 0.0032 | 0.0029 | 0.2369 | 0.2400 | 50.8 | 55.8 | 7 |
| 551 | Smith, Jackson | MIS_MUD | Cutter | RHH | 32 | 0.0029 | 0.0000 | 0.2371 | 0.2400 | 50.3 | 53.7 | 8 |
| 563 | Salata, Derek | SCH_BOO | Cutter | RHH | 39 | 0.0027 | 0.0000 | 0.2373 | 0.2400 | 49.9 | 52.7 | 9 |
| 646 | Petschke, Ben | EVA_OTT | Cutter | RHH | 82 | 0.0019 | 0.0000 | 0.2381 | 0.2400 | 48.2 | 45.7 | 10 |
| 700 | Gamelin, Shaun | JOL_SLA | Cutter | RHH | 62 | 0.0015 | 0.0000 | 0.2386 | 0.2400 | 47.2 | 41.1 | 11 |
| 719 | Williams, Brian | MIS_MUD | Cutter | RHH | 62 | 0.0013 | 0.0000 | 0.2387 | 0.2400 | 46.8 | 39.5 | 12 |
| 755 | Binns, Malik | NEW_JER6 | Cutter | RHH | 48 | 0.0010 | 0.0000 | 0.2390 | 0.2400 | 46.2 | 36.5 | 13 |
| 765 | Bohnert, Matthew | WIN_CIT29 | Cutter | RHH | 32 | 0.0009 | 0.0000 | 0.2392 | 0.2400 | 45.9 | 35.6 | 14 |
| 788 | Saturria, Michael | NEW_ENG23 | Cutter | RHH | 79 | 0.0007 | 0.0000 | 0.2393 | 0.2400 | 45.5 | 33.7 | 15 |

### Four-Seam vs LHH

| Rank | Pitcher | Team | Pitch Type | Batter Side | Pitches | Avg Adv | Median Adv | Grid xwOBA | League xwOBA | LS 20-80 | LS 0-100 | Type/Side Rank |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 11 | Wehrle, Tyler | WIN_CIT29 | Four-Seam | LHH | 75 | 0.0151 | 0.0141 | 0.2315 | 0.2466 | 76.5 | 99.2 | 1 |
| 19 | Davis, Tyler | WAS_WIL3 | Four-Seam | LHH | 48 | 0.0144 | 0.0141 | 0.2323 | 0.2466 | 75.0 | 98.5 | 2 |
| 31 | Bauer, Patrick | QUE_CAP | Four-Seam | LHH | 26 | 0.0127 | 0.0118 | 0.2340 | 0.2466 | 71.3 | 97.5 | 3 |
| 33 | Foster, Kobe | WAS_WIL3 | Four-Seam | LHH | 88 | 0.0126 | 0.0141 | 0.2340 | 0.2466 | 71.2 | 97.3 | 4 |
| 35 | Parsons, Billy | SUS_COU1 | Four-Seam | LHH | 128 | 0.0126 | 0.0117 | 0.2340 | 0.2466 | 71.1 | 97.1 | 5 |
| 40 | Barreto, Brayhans | TRI_VAL | Four-Seam | LHH | 38 | 0.0122 | 0.0005 | 0.2344 | 0.2466 | 70.4 | 96.7 | 6 |
| 49 | Herbert, Andrew | WAS_WIL3 | Four-Seam | LHH | 35 | 0.0119 | 0.0116 | 0.2348 | 0.2466 | 69.6 | 96.0 | 7 |
| 56 | Peters, Andrew | NEW_JER6 | Four-Seam | LHH | 71 | 0.0111 | 0.0071 | 0.2355 | 0.2466 | 68.0 | 95.4 | 8 |
| 57 | Leak, Anthony | NEW_YOR13 | Four-Seam | LHH | 31 | 0.0111 | 0.0109 | 0.2355 | 0.2466 | 67.9 | 95.3 | 9 |
| 63 | Marynczak, Arlo | TRI_VAL | Four-Seam | LHH | 52 | 0.0109 | 0.0128 | 0.2357 | 0.2466 | 67.4 | 94.8 | 10 |
| 69 | Fowler, Dalton | SUS_COU1 | Four-Seam | LHH | 43 | 0.0107 | 0.0078 | 0.2359 | 0.2466 | 67.1 | 94.3 | 11 |
| 72 | De Los Santos, Enmanuel | NEW_ENG23 | Four-Seam | LHH | 46 | 0.0105 | 0.0089 | 0.2361 | 0.2466 | 66.7 | 94.0 | 12 |
| 75 | Cartwright, Eli | GAT_GRI | Four-Seam | LHH | 42 | 0.0104 | 0.0069 | 0.2362 | 0.2466 | 66.5 | 93.8 | 13 |
| 78 | Kines, Gunnar | JOL_SLA | Four-Seam | LHH | 121 | 0.0103 | 0.0064 | 0.2364 | 0.2466 | 66.1 | 93.5 | 14 |
| 93 | Ferguson, Francis | QUE_CAP | Four-Seam | LHH | 51 | 0.0097 | 0.0078 | 0.2369 | 0.2466 | 65.0 | 92.2 | 15 |

### Four-Seam vs RHH

| Rank | Pitcher | Team | Pitch Type | Batter Side | Pitches | Avg Adv | Median Adv | Grid xwOBA | League xwOBA | LS 20-80 | LS 0-100 | Type/Side Rank |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | Binns, Malik | NEW_JER6 | Four-Seam | RHH | 25 | 0.0190 | 0.0151 | 0.2210 | 0.2400 | 80.0 | 100.0 | 1 |
| 6 | Reeves, Cobe | NEW_YOR13 | Four-Seam | RHH | 27 | 0.0167 | 0.0204 | 0.2233 | 0.2400 | 80.0 | 99.6 | 2 |
| 10 | Petraitis, AJ | LEM_COL | Four-Seam | RHH | 29 | 0.0151 | 0.0078 | 0.2249 | 0.2400 | 76.6 | 99.2 | 3 |
| 29 | Ginn, Landon | WAS_WIL3 | Four-Seam | RHH | 44 | 0.0128 | 0.0080 | 0.2272 | 0.2400 | 71.6 | 97.6 | 4 |
| 30 | Mercado, Nelson | OTT_TIT | Four-Seam | RHH | 42 | 0.0127 | 0.0074 | 0.2273 | 0.2400 | 71.5 | 97.6 | 5 |
| 32 | Johnson, Preston | MIS_MUD | Four-Seam | RHH | 28 | 0.0126 | 0.0090 | 0.2274 | 0.2400 | 71.2 | 97.4 | 6 |
| 39 | Perozzi, John | SUS_COU1 | Four-Seam | RHH | 51 | 0.0123 | 0.0034 | 0.2277 | 0.2400 | 70.5 | 96.8 | 7 |
| 41 | Davis, Tyler | WIN_CIT29 | Four-Seam | RHH | 33 | 0.0122 | 0.0021 | 0.2278 | 0.2400 | 70.3 | 96.6 | 8 |
| 52 | Shears, Tanner | SCH_BOO | Four-Seam | RHH | 67 | 0.0116 | 0.0037 | 0.2284 | 0.2400 | 68.9 | 95.7 | 9 |
| 64 | Brothers, Kellen | SUS_COU1 | Four-Seam | RHH | 60 | 0.0108 | 0.0023 | 0.2292 | 0.2400 | 67.4 | 94.7 | 10 |
| 68 | Grounds, Jackson | DOW_EAS1 | Four-Seam | RHH | 48 | 0.0107 | 0.0091 | 0.2293 | 0.2400 | 67.2 | 94.4 | 11 |
| 71 | Kines, Gunnar | JOL_SLA | Four-Seam | RHH | 131 | 0.0105 | 0.0053 | 0.2295 | 0.2400 | 66.7 | 94.1 | 12 |
| 73 | Gardner, Sam | GAT_GRI | Four-Seam | RHH | 27 | 0.0105 | 0.0000 | 0.2295 | 0.2400 | 66.6 | 93.9 | 13 |
| 74 | Nakata, Yuto | QUE_CAP | Four-Seam | RHH | 58 | 0.0105 | 0.0090 | 0.2295 | 0.2400 | 66.5 | 93.9 | 14 |
| 83 | Albert, Wes | TRI_VAL | Four-Seam | RHH | 52 | 0.0101 | 0.0085 | 0.2299 | 0.2400 | 65.8 | 93.1 | 15 |

### Sinker vs LHH

| Rank | Pitcher | Team | Pitch Type | Batter Side | Pitches | Avg Adv | Median Adv | Grid xwOBA | League xwOBA | LS 20-80 | LS 0-100 | Type/Side Rank |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 16 | Sechrist, Zander | WAS_WIL3 | Sinker | LHH | 28 | 0.0147 | 0.0045 | 0.2485 | 0.2632 | 75.7 | 98.7 | 1 |
| 99 | Lawson, Nathan | FLO_Y'A | Sinker | LHH | 28 | 0.0095 | 0.0078 | 0.2537 | 0.2632 | 64.5 | 91.7 | 2 |
| 112 | Kelly, Aiden | TRI_VAL | Sinker | LHH | 51 | 0.0091 | 0.0000 | 0.2542 | 0.2632 | 63.5 | 90.6 | 3 |
| 114 | Sabatine, Gino | TRI_VAL | Sinker | LHH | 28 | 0.0090 | 0.0019 | 0.2542 | 0.2632 | 63.5 | 90.5 | 4 |
| 127 | Gregory, Ben | GAT_GRI | Sinker | LHH | 31 | 0.0087 | 0.0036 | 0.2545 | 0.2632 | 62.8 | 89.4 | 5 |
| 184 | Kines, Gunnar | JOL_SLA | Sinker | LHH | 30 | 0.0073 | 0.0066 | 0.2559 | 0.2632 | 59.8 | 84.6 | 6 |
| 190 | Harper, Scott | NEW_YOR13 | Sinker | LHH | 41 | 0.0072 | 0.0000 | 0.2560 | 0.2632 | 59.6 | 84.1 | 7 |
| 208 | Mannering, Shawn | DOW_EAS1 | Sinker | LHH | 27 | 0.0069 | 0.0000 | 0.2563 | 0.2632 | 58.9 | 82.6 | 8 |
| 219 | Shoemaker, Adam | QUE_CAP | Sinker | LHH | 25 | 0.0067 | 0.0045 | 0.2565 | 0.2632 | 58.5 | 81.6 | 9 |
| 228 | Gilleran, James | NEW_ENG23 | Sinker | LHH | 25 | 0.0066 | 0.0039 | 0.2566 | 0.2632 | 58.3 | 80.9 | 10 |
| 235 | McCartney, Seth | MIS_MUD | Sinker | LHH | 67 | 0.0065 | 0.0000 | 0.2567 | 0.2632 | 58.1 | 80.3 | 11 |
| 251 | Vecerka, Boris | QUE_CAP | Sinker | LHH | 52 | 0.0063 | 0.0018 | 0.2569 | 0.2632 | 57.7 | 78.9 | 12 |
| 277 | Bradford, Ethan | NEW_YOR13 | Sinker | LHH | 44 | 0.0059 | 0.0072 | 0.2573 | 0.2632 | 56.8 | 76.7 | 13 |
| 306 | Stuka, Ted | OTT_TIT | Sinker | LHH | 45 | 0.0055 | 0.0000 | 0.2578 | 0.2632 | 55.8 | 74.3 | 14 |
| 324 | Hicks, Jackson | DOW_EAS1 | Sinker | LHH | 31 | 0.0053 | 0.0000 | 0.2579 | 0.2632 | 55.4 | 72.8 | 15 |

### Sinker vs RHH

| Rank | Pitcher | Team | Pitch Type | Batter Side | Pitches | Avg Adv | Median Adv | Grid xwOBA | League xwOBA | LS 20-80 | LS 0-100 | Type/Side Rank |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 44 | Leach, Landon | TRO_AIG | Sinker | RHH | 44 | 0.0120 | 0.0106 | 0.2436 | 0.2556 | 69.9 | 96.4 | 1 |
| 137 | Mannering, Shawn | DOW_EAS1 | Sinker | RHH | 32 | 0.0084 | 0.0067 | 0.2472 | 0.2556 | 62.1 | 88.5 | 2 |
| 145 | Campbell, AJ | WIN_CIT29 | Sinker | RHH | 25 | 0.0081 | 0.0075 | 0.2475 | 0.2556 | 61.5 | 87.9 | 3 |
| 159 | Turner, Eric | JOL_SLA | Sinker | RHH | 42 | 0.0079 | 0.0077 | 0.2477 | 0.2556 | 61.0 | 86.7 | 4 |
| 203 | Delongchamp, Luke | TRI_VAL | Sinker | RHH | 37 | 0.0070 | 0.0000 | 0.2486 | 0.2556 | 59.1 | 83.0 | 5 |
| 211 | Ryan, Dillon | NEW_ENG23 | Sinker | RHH | 66 | 0.0069 | 0.0072 | 0.2488 | 0.2556 | 58.8 | 82.3 | 6 |
| 213 | Plumadore, Carson | WIN_CIT29 | Sinker | RHH | 32 | 0.0068 | 0.0106 | 0.2488 | 0.2556 | 58.7 | 82.1 | 7 |
| 215 | Donnan, Blake | FLO_Y'A | Sinker | RHH | 84 | 0.0068 | 0.0071 | 0.2488 | 0.2556 | 58.6 | 82.0 | 8 |
| 217 | Glickstein, Aaron | SCH_BOO | Sinker | RHH | 33 | 0.0067 | 0.0069 | 0.2489 | 0.2556 | 58.5 | 81.8 | 9 |
| 236 | Rodriguez, Joe Joe | NEW_JER6 | Sinker | RHH | 47 | 0.0065 | 0.0018 | 0.2491 | 0.2556 | 58.1 | 80.2 | 10 |
| 238 | Gregory, Ben | GAT_GRI | Sinker | RHH | 45 | 0.0065 | 0.0071 | 0.2491 | 0.2556 | 58.0 | 80.0 | 11 |
| 263 | Still, Stephen | TRI_VAL | Sinker | RHH | 50 | 0.0062 | 0.0047 | 0.2494 | 0.2556 | 57.3 | 77.9 | 12 |
| 362 | Cook, Cole | SCH_BOO | Sinker | RHH | 36 | 0.0047 | 0.0017 | 0.2509 | 0.2556 | 54.2 | 69.6 | 13 |
| 368 | Hoeymans, Jack | GAT_GRI | Sinker | RHH | 35 | 0.0047 | 0.0000 | 0.2509 | 0.2556 | 54.1 | 69.1 | 14 |
| 378 | Milburn, Isaac | FLO_Y'A | Sinker | RHH | 51 | 0.0046 | 0.0000 | 0.2510 | 0.2556 | 54.0 | 68.2 | 15 |

### Slider vs LHH

| Rank | Pitcher | Team | Pitch Type | Batter Side | Pitches | Avg Adv | Median Adv | Grid xwOBA | League xwOBA | LS 20-80 | LS 0-100 | Type/Side Rank |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 117 | Bradford, Ethan | NEW_YOR13 | Slider | LHH | 30 | 0.0088 | 0.0052 | 0.2267 | 0.2355 | 63.1 | 90.2 | 1 |
| 125 | Potteiger, Jack | JOL_SLA | Slider | LHH | 30 | 0.0087 | 0.0034 | 0.2268 | 0.2355 | 62.8 | 89.6 | 2 |
| 201 | Cosentino, Nick | JOL_SLA | Slider | LHH | 30 | 0.0070 | 0.0026 | 0.2285 | 0.2355 | 59.1 | 83.2 | 3 |
| 204 | Dima, Josh | GAT_GRI | Slider | LHH | 60 | 0.0070 | 0.0000 | 0.2285 | 0.2355 | 59.0 | 82.9 | 4 |
| 209 | Cook, Cole | SCH_BOO | Slider | LHH | 87 | 0.0069 | 0.0000 | 0.2286 | 0.2355 | 58.8 | 82.5 | 5 |
| 212 | Alpern, Liam | FLO_Y'A | Slider | LHH | 38 | 0.0068 | 0.0000 | 0.2286 | 0.2355 | 58.8 | 82.2 | 6 |
| 239 | MacMillan, Blake | TRO_AIG | Slider | LHH | 37 | 0.0065 | 0.0019 | 0.2290 | 0.2355 | 58.0 | 79.9 | 7 |
| 248 | Parsons, Billy | SUS_COU1 | Slider | LHH | 86 | 0.0064 | 0.0034 | 0.2291 | 0.2355 | 57.8 | 79.2 | 8 |
| 274 | Majick, Eli | NEW_ENG23 | Slider | LHH | 42 | 0.0060 | 0.0039 | 0.2295 | 0.2355 | 56.9 | 77.0 | 9 |
| 284 | Linderman, Greyson | JOL_SLA | Slider | LHH | 27 | 0.0058 | 0.0000 | 0.2297 | 0.2355 | 56.5 | 76.2 | 10 |
| 292 | Joven, Art | MIS_MUD | Slider | LHH | 93 | 0.0057 | 0.0000 | 0.2298 | 0.2355 | 56.3 | 75.5 | 11 |
| 314 | Eckaus, David | EVA_OTT | Slider | LHH | 45 | 0.0054 | 0.0000 | 0.2301 | 0.2355 | 55.7 | 73.6 | 12 |
| 329 | Armstrong, Andrew | NEW_YOR13 | Slider | LHH | 40 | 0.0052 | 0.0000 | 0.2303 | 0.2355 | 55.2 | 72.4 | 13 |
| 338 | Kaminer, Brandon | DOW_EAS1 | Slider | LHH | 33 | 0.0051 | 0.0029 | 0.2304 | 0.2355 | 54.9 | 71.6 | 14 |
| 344 | Hensey, Rob | SUS_COU1 | Slider | LHH | 45 | 0.0050 | 0.0000 | 0.2305 | 0.2355 | 54.8 | 71.1 | 15 |

### Slider vs RHH

| Rank | Pitcher | Team | Pitch Type | Batter Side | Pitches | Avg Adv | Median Adv | Grid xwOBA | League xwOBA | LS 20-80 | LS 0-100 | Type/Side Rank |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 2 | Perez, Kelvin | WAS_WIL3 | Slider | RHH | 45 | 0.0183 | 0.0152 | 0.2117 | 0.2301 | 80.0 | 99.9 | 1 |
| 3 | McCartney, Seth | MIS_MUD | Slider | RHH | 36 | 0.0171 | 0.0034 | 0.2130 | 0.2301 | 80.0 | 99.8 | 2 |
| 4 | Nova, Fraynel | LAK_ERI24 | Slider | RHH | 100 | 0.0171 | 0.0118 | 0.2130 | 0.2301 | 80.0 | 99.7 | 3 |
| 5 | Smith, Ethan | WIN_CIT29 | Slider | RHH | 30 | 0.0167 | 0.0007 | 0.2133 | 0.2301 | 80.0 | 99.7 | 4 |
| 7 | Blair, Davis | DOW_EAS1 | Slider | RHH | 61 | 0.0163 | 0.0095 | 0.2137 | 0.2301 | 79.2 | 99.5 | 5 |
| 9 | Willeman, Landon | EVA_OTT | Slider | RHH | 33 | 0.0157 | 0.0000 | 0.2143 | 0.2301 | 77.9 | 99.3 | 6 |
| 12 | Belton, Hunter | MIS_MUD | Slider | RHH | 75 | 0.0150 | 0.0058 | 0.2151 | 0.2301 | 76.3 | 99.1 | 7 |
| 13 | Perdomo, Rafael | QUE_CAP | Slider | RHH | 46 | 0.0149 | 0.0007 | 0.2152 | 0.2301 | 76.0 | 99.0 | 8 |
| 14 | Perozzi, John | SUS_COU1 | Slider | RHH | 46 | 0.0148 | 0.0152 | 0.2152 | 0.2301 | 76.0 | 98.9 | 9 |
| 15 | Gamelin, Shaun | JOL_SLA | Slider | RHH | 31 | 0.0148 | 0.0102 | 0.2153 | 0.2301 | 75.8 | 98.8 | 10 |
| 17 | Whitesell, Max | FLO_Y'A | Slider | RHH | 77 | 0.0145 | 0.0050 | 0.2155 | 0.2301 | 75.3 | 98.7 | 11 |
| 18 | Cohn, Cooper | NIU_HUS | Slider | RHH | 27 | 0.0145 | 0.0000 | 0.2155 | 0.2301 | 75.3 | 98.6 | 12 |
| 20 | Salata, Derek | SCH_BOO | Slider | RHH | 100 | 0.0142 | 0.0082 | 0.2158 | 0.2301 | 74.7 | 98.4 | 13 |
| 22 | Wiltse, Ryan | EVA_OTT | Slider | RHH | 35 | 0.0140 | 0.0082 | 0.2160 | 0.2301 | 74.3 | 98.2 | 14 |
| 23 | Garcia, Hector | WAS_WIL3 | Slider | RHH | 36 | 0.0139 | 0.0075 | 0.2161 | 0.2301 | 74.1 | 98.1 | 15 |

### Splitter vs LHH

| Rank | Pitcher | Team | Pitch Type | Batter Side | Pitches | Avg Adv | Median Adv | Grid xwOBA | League xwOBA | LS 20-80 | LS 0-100 | Type/Side Rank |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 676 | Thompson, Ross | SCH_BOO | Splitter | LHH | 69 | 0.0017 | 0.0000 | 0.2357 | 0.2374 | 47.6 | 43.1 | 1 |
| 682 | Salata, Derek | SCH_BOO | Splitter | LHH | 64 | 0.0016 | -0.0000 | 0.2358 | 0.2374 | 47.5 | 42.6 | 2 |
| 724 | Williams, Brian | MIS_MUD | Splitter | LHH | 40 | 0.0013 | 0.0000 | 0.2361 | 0.2374 | 46.7 | 39.1 | 3 |
| 730 | Pindel, Buddie | SCH_BOO | Splitter | LHH | 50 | 0.0012 | -0.0000 | 0.2362 | 0.2374 | 46.7 | 38.6 | 4 |
| 734 | Garcia, Hector | WAS_WIL3 | Splitter | LHH | 59 | 0.0012 | 0.0000 | 0.2362 | 0.2374 | 46.6 | 38.2 | 5 |
| 746 | Andueza, Axel | DOW_EAS1 | Splitter | LHH | 25 | 0.0011 | 0.0000 | 0.2363 | 0.2374 | 46.4 | 37.2 | 6 |
| 764 | Vitas, Ben | JOL_SLA | Splitter | LHH | 38 | 0.0009 | -0.0000 | 0.2365 | 0.2374 | 45.9 | 35.7 | 7 |
| 810 | Thornton, Tyler | NEW_ENG23 | Splitter | LHH | 28 | 0.0005 | -0.0000 | 0.2369 | 0.2374 | 45.0 | 31.8 | 8 |
| 840 | Orth, Harry | SCH_BOO | Splitter | LHH | 31 | 0.0001 | 0.0000 | 0.2372 | 0.2374 | 44.3 | 29.3 | 9 |
| 850 | Villers, Ian | QUE_CAP | Splitter | LHH | 39 | -0.0000 | 0.0000 | 0.2374 | 0.2374 | 44.0 | 28.5 | 10 |
| 887 | Parsons, Billy | SUS_COU1 | Splitter | LHH | 26 | -0.0003 | -0.0000 | 0.2377 | 0.2374 | 43.4 | 25.4 | 11 |
| 971 | Duby, Bill | NEW_JER6 | Splitter | LHH | 30 | -0.0013 | -0.0000 | 0.2387 | 0.2374 | 41.3 | 18.3 | 12 |
| 978 | Nakata, Yuto | QUE_CAP | Splitter | LHH | 47 | -0.0014 | -0.0000 | 0.2388 | 0.2374 | 41.1 | 17.7 | 13 |

### Splitter vs RHH

| Rank | Pitcher | Team | Pitch Type | Batter Side | Pitches | Avg Adv | Median Adv | Grid xwOBA | League xwOBA | LS 20-80 | LS 0-100 | Type/Side Rank |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 711 | Pindel, Buddie | SCH_BOO | Splitter | RHH | 30 | 0.0013 | 0.0000 | 0.2512 | 0.2525 | 46.9 | 40.2 | 1 |
| 745 | Villers, Ian | QUE_CAP | Splitter | RHH | 25 | 0.0011 | 0.0000 | 0.2514 | 0.2525 | 46.4 | 37.3 | 2 |
| 861 | Williams, Brian | MIS_MUD | Splitter | RHH | 29 | -0.0001 | 0.0000 | 0.2526 | 0.2525 | 43.8 | 27.5 | 3 |

### Sweeper vs RHH

| Rank | Pitcher | Team | Pitch Type | Batter Side | Pitches | Avg Adv | Median Adv | Grid xwOBA | League xwOBA | LS 20-80 | LS 0-100 | Type/Side Rank |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 808 | Simpson, Garret | EVA_OTT | Sweeper | RHH | 26 | 0.0005 | 0.0000 | 0.2063 | 0.2068 | 45.1 | 32.0 | 1 |
| 843 | Cerda, Junior | EVA_OTT | Sweeper | RHH | 28 | 0.0001 | 0.0000 | 0.2067 | 0.2068 | 44.2 | 29.1 | 2 |
