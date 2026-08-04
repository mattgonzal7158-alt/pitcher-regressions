# Location Score Report

- Pitch input file: `data\processed\2026-data-with-woba-xwoba.parquet`
- Location grid input file: `data\processed\location_value_grid.csv`
- Output file: `data\processed\location_scores.csv`
- Assigned pitch rows: 197,504
- Qualified pitcher + pitch type + batter side rows: 2,043
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
| 1 | Hohenstein, Liam | WIN_CIT29 | Slider | RHH | 27 | 0.0333 | 0.0255 | 0.1958 | 0.2291 | 80.0 | 100.0 | 1 |
| 2 | Garcia, Hector | WAS_WIL3 | Slider | RHH | 36 | 0.0303 | 0.0348 | 0.1987 | 0.2291 | 80.0 | 100.0 | 2 |
| 3 | Finarelli, Nick | LON_ISL22 | Slider | RHH | 31 | 0.0298 | 0.0200 | 0.1993 | 0.2291 | 80.0 | 99.9 | 3 |
| 4 | Wiltse, Ryan | EVA_OTT | Slider | RHH | 74 | 0.0296 | 0.0200 | 0.1995 | 0.2291 | 80.0 | 99.9 | 4 |
| 5 | Cameron, Wyatt | TRI_VAL | Slider | RHH | 25 | 0.0292 | 0.0395 | 0.1998 | 0.2291 | 80.0 | 99.8 | 5 |
| 6 | Stegura, Drew | WAS_WIL3 | Slider | RHH | 25 | 0.0282 | 0.0343 | 0.2009 | 0.2291 | 80.0 | 99.8 | 6 |
| 7 | Givens-Craig, Hayden | SUS_COU1 | Slider | RHH | 28 | 0.0279 | 0.0235 | 0.2012 | 0.2291 | 80.0 | 99.7 | 7 |
| 8 | Smith, Ethan | WIN_CIT29 | Slider | RHH | 30 | 0.0272 | 0.0182 | 0.2019 | 0.2291 | 80.0 | 99.7 | 8 |
| 9 | Perdomo, Rafael | QUE_CAP | Slider | RHH | 73 | 0.0267 | 0.0081 | 0.2024 | 0.2291 | 80.0 | 99.6 | 9 |
| 10 | Cameron, Wyatt | SCH_BOO | Slider | RHH | 50 | 0.0266 | 0.0038 | 0.2024 | 0.2291 | 80.0 | 99.6 | 10 |
| 11 | Cerda, Junior | EVA_OTT | Slider | RHH | 116 | 0.0260 | 0.0164 | 0.2030 | 0.2291 | 80.0 | 99.5 | 11 |
| 12 | Hagan, Jack | DOW_EAS1 | Slider | RHH | 191 | 0.0259 | 0.0209 | 0.2032 | 0.2291 | 80.0 | 99.5 | 12 |
| 13 | Martinez, Gregory | DOW_EAS1 | Slider | RHH | 26 | 0.0258 | 0.0273 | 0.2032 | 0.2291 | 80.0 | 99.4 | 13 |
| 14 | Albert, Wes | TRI_VAL | Slider | RHH | 25 | 0.0257 | 0.0200 | 0.2033 | 0.2291 | 80.0 | 99.4 | 14 |
| 15 | Gilleran, Jimmy | NEW_ENG23 | Slider | RHH | 109 | 0.0257 | 0.0220 | 0.2034 | 0.2291 | 80.0 | 99.3 | 15 |
| 16 | Kirby, Zach | WAS_WIL3 | Slider | RHH | 126 | 0.0251 | 0.0142 | 0.2039 | 0.2291 | 79.8 | 99.3 | 16 |
| 17 | Mercado, Nelson | OTT_TIT | Four-Seam | RHH | 42 | 0.0251 | 0.0260 | 0.2120 | 0.2371 | 79.8 | 99.2 | 1 |
| 18 | Rivas, Albert | GAT_GRI | Slider | RHH | 43 | 0.0248 | 0.0081 | 0.2042 | 0.2291 | 79.3 | 99.2 | 17 |
| 19 | Thompson, Ross | SCH_BOO | Slider | RHH | 243 | 0.0245 | 0.0142 | 0.2045 | 0.2291 | 78.9 | 99.1 | 18 |
| 20 | Bargo, Casey | NEW_ENG23 | Slider | RHH | 29 | 0.0245 | 0.0255 | 0.2045 | 0.2291 | 78.9 | 99.1 | 19 |
| 21 | Nova, Fraynel | LAK_ERI24 | Slider | RHH | 174 | 0.0245 | 0.0093 | 0.2045 | 0.2291 | 78.9 | 99.0 | 20 |
| 22 | O'Hanlon, Michael | WAS_WIL3 | Slider | RHH | 63 | 0.0245 | 0.0089 | 0.2046 | 0.2291 | 78.8 | 99.0 | 21 |
| 23 | King, Jacob | DOW_EAS1 | Slider | RHH | 36 | 0.0244 | 0.0247 | 0.2047 | 0.2291 | 78.7 | 98.9 | 22 |
| 24 | Helt, Robert | LAK_ERI24 | Slider | RHH | 147 | 0.0243 | 0.0081 | 0.2048 | 0.2291 | 78.5 | 98.9 | 23 |
| 25 | Belton, Hunter | MIS_MUD | Slider | RHH | 75 | 0.0241 | 0.0142 | 0.2049 | 0.2291 | 78.3 | 98.8 | 24 |
| 26 | Allemann, Braeden | QUE_CAP | Slider | RHH | 89 | 0.0241 | 0.0093 | 0.2050 | 0.2291 | 78.2 | 98.8 | 25 |
| 27 | Salata, Derek | SCH_BOO | Slider | RHH | 250 | 0.0240 | 0.0181 | 0.2051 | 0.2291 | 78.0 | 98.7 | 26 |
| 28 | Kemlage, Joe | NEW_ENG23 | Four-Seam | RHH | 28 | 0.0240 | 0.0200 | 0.2131 | 0.2371 | 78.0 | 98.7 | 2 |
| 29 | Binns, Malik | NEW_JER6 | Slider | RHH | 26 | 0.0237 | 0.0122 | 0.2054 | 0.2291 | 77.6 | 98.6 | 27 |
| 30 | Duby, Bill | NEW_JER6 | Slider | RHH | 70 | 0.0236 | 0.0206 | 0.2055 | 0.2291 | 77.4 | 98.6 | 28 |

## Top Location Scores by Pitch Type and Batter Side

### Changeup vs LHH

| Rank | Pitcher | Team | Pitch Type | Batter Side | Pitches | Avg Adv | Median Adv | Grid xwOBA | League xwOBA | LS 20-80 | LS 0-100 | Type/Side Rank |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 43 | Encarnacion, J.D. | EVA_OTT | Changeup | LHH | 28 | 0.0222 | 0.0124 | 0.2181 | 0.2403 | 75.3 | 97.9 | 1 |
| 51 | Allemann, Braeden | QUE_CAP | Changeup | LHH | 44 | 0.0209 | 0.0155 | 0.2194 | 0.2403 | 73.3 | 97.6 | 2 |
| 65 | Petschke, Ben | EVA_OTT | Changeup | LHH | 25 | 0.0201 | 0.0108 | 0.2202 | 0.2403 | 72.0 | 96.9 | 3 |
| 75 | Estrella, Noah | TRI_VAL | Changeup | LHH | 29 | 0.0194 | 0.0108 | 0.2208 | 0.2403 | 71.0 | 96.4 | 4 |
| 81 | Hicks, Jackson | DOW_EAS1 | Changeup | LHH | 25 | 0.0193 | 0.0098 | 0.2210 | 0.2403 | 70.7 | 96.1 | 5 |
| 84 | Dill, Austin | TRI_VAL | Changeup | LHH | 118 | 0.0191 | 0.0118 | 0.2212 | 0.2403 | 70.5 | 95.9 | 6 |
| 86 | Smith, Jackson | MIS_MUD | Changeup | LHH | 80 | 0.0190 | 0.0174 | 0.2213 | 0.2403 | 70.3 | 95.8 | 7 |
| 87 | Brodsky, Jack | WAS_WIL3 | Changeup | LHH | 26 | 0.0189 | 0.0024 | 0.2214 | 0.2403 | 70.1 | 95.8 | 8 |
| 90 | Kirby, Zach | WAS_WIL3 | Changeup | LHH | 119 | 0.0187 | 0.0143 | 0.2216 | 0.2403 | 69.7 | 95.6 | 9 |
| 126 | Catrambone, Ben | JOL_SLA | Changeup | LHH | 25 | 0.0169 | 0.0098 | 0.2234 | 0.2403 | 67.0 | 93.9 | 10 |
| 127 | Hampton, Ky | OTT_TIT | Changeup | LHH | 168 | 0.0169 | 0.0109 | 0.2234 | 0.2403 | 67.0 | 93.8 | 11 |
| 131 | Albert, Wes | DOW_EAS1 | Changeup | LHH | 67 | 0.0168 | 0.0108 | 0.2235 | 0.2403 | 66.9 | 93.6 | 12 |
| 132 | Soto, Noel | TRI_VAL | Changeup | LHH | 48 | 0.0167 | 0.0094 | 0.2236 | 0.2403 | 66.7 | 93.6 | 13 |
| 159 | Igami, Chikara | QUE_CAP | Changeup | LHH | 33 | 0.0159 | 0.0098 | 0.2244 | 0.2403 | 65.5 | 92.3 | 14 |
| 165 | Albert, Wes | TRI_VAL | Changeup | LHH | 38 | 0.0157 | 0.0000 | 0.2246 | 0.2403 | 65.2 | 92.0 | 15 |

### Changeup vs RHH

| Rank | Pitcher | Team | Pitch Type | Batter Side | Pitches | Avg Adv | Median Adv | Grid xwOBA | League xwOBA | LS 20-80 | LS 0-100 | Type/Side Rank |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 154 | Smith, Ben | NEW_ENG23 | Changeup | RHH | 60 | 0.0160 | 0.0122 | 0.2301 | 0.2461 | 65.7 | 92.5 | 1 |
| 181 | Culley, Wesley | NEW_YOR13 | Changeup | RHH | 36 | 0.0155 | 0.0211 | 0.2307 | 0.2461 | 64.7 | 91.2 | 2 |
| 243 | Walsh, John | MIS_MUD | Changeup | RHH | 66 | 0.0137 | 0.0062 | 0.2324 | 0.2461 | 62.0 | 88.2 | 3 |
| 275 | Benitez, Jorge | NEW_JER6 | Changeup | RHH | 45 | 0.0132 | 0.0025 | 0.2329 | 0.2461 | 61.3 | 86.6 | 4 |
| 290 | Steinhauer, Ryan | NEW_JER6 | Changeup | RHH | 57 | 0.0128 | 0.0012 | 0.2333 | 0.2461 | 60.6 | 85.9 | 5 |
| 308 | Alpern, Liam | FLO_Y'A | Changeup | RHH | 38 | 0.0125 | 0.0034 | 0.2336 | 0.2461 | 60.2 | 85.0 | 6 |
| 310 | Pindel, Buddie | SCH_BOO | Changeup | RHH | 30 | 0.0125 | 0.0010 | 0.2336 | 0.2461 | 60.1 | 84.9 | 7 |
| 317 | Kriebel, Chase | EVA_OTT | Changeup | RHH | 36 | 0.0124 | 0.0022 | 0.2337 | 0.2461 | 60.0 | 84.5 | 8 |
| 330 | Gollert, Harley | QUE_CAP | Changeup | RHH | 38 | 0.0122 | 0.0000 | 0.2339 | 0.2461 | 59.7 | 83.9 | 9 |
| 339 | Hocom, Quinn | TRI_VAL | Changeup | RHH | 37 | 0.0121 | 0.0065 | 0.2341 | 0.2461 | 59.4 | 83.5 | 10 |
| 377 | Henderson, Drew | DOW_EAS1 | Changeup | RHH | 75 | 0.0116 | 0.0026 | 0.2345 | 0.2461 | 58.7 | 81.6 | 11 |
| 399 | Zentko, Dylan | EVA_OTT | Changeup | RHH | 90 | 0.0112 | 0.0015 | 0.2349 | 0.2461 | 58.1 | 80.5 | 12 |
| 474 | Galva, Claudio | GAT_GRI | Changeup | RHH | 97 | 0.0102 | 0.0025 | 0.2360 | 0.2461 | 56.5 | 76.8 | 13 |
| 475 | Andueza, Axel | DOW_EAS1 | Changeup | RHH | 26 | 0.0102 | 0.0054 | 0.2360 | 0.2461 | 56.5 | 76.8 | 14 |
| 480 | Parra, Andres | LAK_ERI24 | Changeup | RHH | 41 | 0.0101 | 0.0000 | 0.2360 | 0.2461 | 56.4 | 76.6 | 15 |

### Curveball vs LHH

| Rank | Pitcher | Team | Pitch Type | Batter Side | Pitches | Avg Adv | Median Adv | Grid xwOBA | League xwOBA | LS 20-80 | LS 0-100 | Type/Side Rank |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 326 | Shinn, Nathan | LAK_ERI24 | Curveball | LHH | 29 | 0.0123 | 0.0026 | 0.2288 | 0.2411 | 59.8 | 84.1 | 1 |
| 464 | Carroll, Jake | JOL_SLA | Curveball | LHH | 47 | 0.0103 | 0.0002 | 0.2308 | 0.2411 | 56.6 | 77.3 | 2 |
| 512 | Long, Jalon | NEW_YOR13 | Curveball | LHH | 27 | 0.0097 | 0.0000 | 0.2314 | 0.2411 | 55.8 | 75.0 | 3 |
| 573 | Barker, Alex | NEW_YOR13 | Curveball | LHH | 36 | 0.0089 | 0.0014 | 0.2322 | 0.2411 | 54.6 | 72.0 | 4 |
| 684 | Sanchez, Edwin | LAK_ERI24 | Curveball | LHH | 66 | 0.0079 | 0.0000 | 0.2332 | 0.2411 | 53.0 | 66.6 | 5 |
| 716 | Martzolf, Max | OTT_TIT | Curveball | LHH | 56 | 0.0076 | 0.0000 | 0.2335 | 0.2411 | 52.4 | 65.0 | 6 |
| 744 | Foltz Jr., Michael | WAS_WIL3 | Curveball | LHH | 70 | 0.0072 | 0.0013 | 0.2339 | 0.2411 | 51.9 | 63.6 | 7 |
| 753 | Williams, Pierce | NEW_ENG23 | Curveball | LHH | 71 | 0.0072 | 0.0017 | 0.2339 | 0.2411 | 51.8 | 63.2 | 8 |
| 768 | Kalisky, Jack | OTT_TIT | Curveball | LHH | 33 | 0.0070 | 0.0000 | 0.2341 | 0.2411 | 51.6 | 62.5 | 9 |
| 771 | Sparks, Alec | GAT_GRI | Curveball | LHH | 51 | 0.0070 | 0.0000 | 0.2341 | 0.2411 | 51.6 | 62.3 | 10 |
| 805 | Hocom, Quinn | TRI_VAL | Curveball | LHH | 48 | 0.0068 | 0.0001 | 0.2343 | 0.2411 | 51.2 | 60.6 | 11 |
| 826 | Binns, Malik | NEW_JER6 | Curveball | LHH | 27 | 0.0066 | 0.0000 | 0.2344 | 0.2411 | 51.0 | 59.6 | 12 |
| 827 | Anderson, Colt | WAS_WIL3 | Curveball | LHH | 59 | 0.0066 | 0.0000 | 0.2345 | 0.2411 | 51.0 | 59.6 | 13 |
| 830 | Morgan, Cooper | QUE_CAP | Curveball | LHH | 77 | 0.0066 | 0.0005 | 0.2345 | 0.2411 | 51.0 | 59.4 | 14 |
| 835 | Cameron, Wyatt | SCH_BOO | Curveball | LHH | 47 | 0.0066 | -0.0000 | 0.2345 | 0.2411 | 50.9 | 59.2 | 15 |

### Curveball vs RHH

| Rank | Pitcher | Team | Pitch Type | Batter Side | Pitches | Avg Adv | Median Adv | Grid xwOBA | League xwOBA | LS 20-80 | LS 0-100 | Type/Side Rank |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 117 | Melendez, Omar | NEW_ENG23 | Curveball | RHH | 26 | 0.0172 | 0.0059 | 0.2314 | 0.2486 | 67.5 | 94.3 | 1 |
| 145 | Hargrove, Dawson | LAK_ERI24 | Curveball | RHH | 44 | 0.0162 | 0.0092 | 0.2324 | 0.2486 | 66.0 | 93.0 | 2 |
| 170 | Cirino, Miguel | DOW_EAS1 | Curveball | RHH | 29 | 0.0156 | 0.0087 | 0.2330 | 0.2486 | 65.0 | 91.7 | 3 |
| 219 | Kalisky, Jack | OTT_TIT | Curveball | RHH | 60 | 0.0143 | 0.0003 | 0.2343 | 0.2486 | 63.0 | 89.3 | 4 |
| 222 | Hampton, Ky | OTT_TIT | Curveball | RHH | 61 | 0.0142 | 0.0037 | 0.2344 | 0.2486 | 62.8 | 89.2 | 5 |
| 223 | Simpson, Garret | EVA_OTT | Curveball | RHH | 66 | 0.0142 | 0.0000 | 0.2345 | 0.2486 | 62.8 | 89.1 | 6 |
| 240 | Garcia, Hector | WAS_WIL3 | Curveball | RHH | 27 | 0.0138 | 0.0090 | 0.2349 | 0.2486 | 62.1 | 88.3 | 7 |
| 244 | Morse, Colby | EVA_OTT | Curveball | RHH | 25 | 0.0137 | 0.0000 | 0.2349 | 0.2486 | 62.0 | 88.1 | 8 |
| 254 | Allemann, Braeden | QUE_CAP | Curveball | RHH | 158 | 0.0135 | 0.0000 | 0.2351 | 0.2486 | 61.7 | 87.6 | 9 |
| 292 | Grounds, Jackson | DOW_EAS1 | Curveball | RHH | 43 | 0.0128 | 0.0000 | 0.2359 | 0.2486 | 60.6 | 85.8 | 10 |
| 304 | Coles, Chad | WAS_WIL3 | Curveball | RHH | 45 | 0.0126 | 0.0000 | 0.2361 | 0.2486 | 60.3 | 85.2 | 11 |
| 316 | Perdomo, Rafael | QUE_CAP | Curveball | RHH | 46 | 0.0124 | 0.0000 | 0.2362 | 0.2486 | 60.0 | 84.6 | 12 |
| 333 | Hohenstein, Liam | WIN_CIT29 | Curveball | RHH | 61 | 0.0122 | 0.0000 | 0.2365 | 0.2486 | 59.6 | 83.7 | 13 |
| 337 | Albert, Wes | DOW_EAS1 | Curveball | RHH | 25 | 0.0121 | 0.0000 | 0.2365 | 0.2486 | 59.5 | 83.6 | 14 |
| 347 | Maryniak, Connor | NEW_JER6 | Curveball | RHH | 96 | 0.0119 | 0.0000 | 0.2367 | 0.2486 | 59.2 | 83.1 | 15 |

### Cutter vs LHH

| Rank | Pitcher | Team | Pitch Type | Batter Side | Pitches | Avg Adv | Median Adv | Grid xwOBA | League xwOBA | LS 20-80 | LS 0-100 | Type/Side Rank |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1288 | Petschke, Ben | EVA_OTT | Cutter | LHH | 174 | 0.0031 | 0.0003 | 0.2231 | 0.2262 | 45.5 | 37.0 | 1 |
| 1389 | McEvoy, Aidan | FLO_Y'A | Cutter | LHH | 50 | 0.0025 | 0.0000 | 0.2237 | 0.2262 | 44.5 | 32.1 | 2 |
| 1449 | Cook, Cole | SCH_BOO | Cutter | LHH | 40 | 0.0021 | 0.0000 | 0.2241 | 0.2262 | 43.9 | 29.1 | 3 |
| 1495 | Salata, Derek | SCH_BOO | Cutter | LHH | 78 | 0.0018 | 0.0000 | 0.2244 | 0.2262 | 43.4 | 26.9 | 4 |
| 1548 | Langrell, Connor | MIS_MUD | Cutter | LHH | 144 | 0.0014 | 0.0000 | 0.2248 | 0.2262 | 42.9 | 24.3 | 5 |
| 1568 | Parsons, Billy | SUS_COU1 | Cutter | LHH | 45 | 0.0013 | 0.0009 | 0.2249 | 0.2262 | 42.6 | 23.3 | 6 |
| 1569 | Garcia, Jorge | SUS_COU1 | Cutter | LHH | 30 | 0.0013 | 0.0000 | 0.2249 | 0.2262 | 42.6 | 23.3 | 7 |
| 1572 | Morgan, Marcus | JOL_SLA | Cutter | LHH | 40 | 0.0012 | 0.0000 | 0.2250 | 0.2262 | 42.6 | 23.1 | 8 |
| 1606 | Catrambone, Ben | JOL_SLA | Cutter | LHH | 34 | 0.0009 | 0.0000 | 0.2253 | 0.2262 | 42.0 | 21.4 | 9 |
| 1611 | Webster, Evan | FLO_Y'A | Cutter | LHH | 104 | 0.0009 | 0.0000 | 0.2254 | 0.2262 | 42.0 | 21.2 | 10 |
| 1614 | MacMillan, Blake | TRO_AIG | Cutter | LHH | 62 | 0.0008 | 0.0000 | 0.2254 | 0.2262 | 41.9 | 21.0 | 11 |
| 1628 | Bell, Brendan | NEW_ENG23 | Cutter | LHH | 66 | 0.0007 | 0.0000 | 0.2255 | 0.2262 | 41.8 | 20.4 | 12 |
| 1635 | Campbell, AJ | WIN_CIT29 | Cutter | LHH | 44 | 0.0007 | 0.0000 | 0.2256 | 0.2262 | 41.7 | 20.0 | 13 |
| 1637 | Jones, Breyln | NEW_JER6 | Cutter | LHH | 26 | 0.0006 | 0.0000 | 0.2256 | 0.2262 | 41.6 | 19.9 | 14 |
| 1654 | Townes, Holland | SCH_BOO | Cutter | LHH | 27 | 0.0005 | 0.0000 | 0.2257 | 0.2262 | 41.4 | 19.1 | 15 |

### Cutter vs RHH

| Rank | Pitcher | Team | Pitch Type | Batter Side | Pitches | Avg Adv | Median Adv | Grid xwOBA | League xwOBA | LS 20-80 | LS 0-100 | Type/Side Rank |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 553 | Jones, Breyln | NEW_JER6 | Cutter | RHH | 46 | 0.0091 | 0.0000 | 0.2248 | 0.2340 | 54.9 | 73.0 | 1 |
| 791 | Maietta, Dante | WIN_CIT29 | Cutter | RHH | 33 | 0.0069 | 0.0000 | 0.2271 | 0.2340 | 51.4 | 61.3 | 2 |
| 821 | Good, Ty | GAT_GRI | Cutter | RHH | 44 | 0.0067 | 0.0000 | 0.2273 | 0.2340 | 51.1 | 59.9 | 3 |
| 890 | Scafidi, Christian | LAK_ERI24 | Cutter | RHH | 27 | 0.0060 | 0.0000 | 0.2279 | 0.2340 | 50.1 | 56.5 | 4 |
| 907 | Bell, Brendan | NEW_ENG23 | Cutter | RHH | 58 | 0.0059 | 0.0000 | 0.2281 | 0.2340 | 49.8 | 55.7 | 5 |
| 980 | Ginn, Landon | WAS_WIL3 | Cutter | RHH | 68 | 0.0054 | 0.0000 | 0.2286 | 0.2340 | 49.0 | 52.1 | 6 |
| 1003 | Thiels, Brenton | MIS_MUD | Cutter | RHH | 28 | 0.0052 | 0.0000 | 0.2287 | 0.2340 | 48.8 | 51.0 | 7 |
| 1007 | Majick, Eli | NEW_ENG23 | Cutter | RHH | 83 | 0.0052 | 0.0026 | 0.2288 | 0.2340 | 48.8 | 50.8 | 8 |
| 1031 | Baird, Dustin | MIS_MUD | Cutter | RHH | 30 | 0.0050 | 0.0000 | 0.2289 | 0.2340 | 48.5 | 49.6 | 9 |
| 1061 | Rivera, Matthew | NEW_ENG23 | Cutter | RHH | 29 | 0.0048 | 0.0000 | 0.2292 | 0.2340 | 48.1 | 48.1 | 10 |
| 1076 | Valdez, Alex | EVA_OTT | Cutter | RHH | 78 | 0.0047 | 0.0000 | 0.2293 | 0.2340 | 48.0 | 47.4 | 11 |
| 1112 | Forsyth, Braden | MIS_MUD | Cutter | RHH | 27 | 0.0044 | 0.0000 | 0.2295 | 0.2340 | 47.5 | 45.6 | 12 |
| 1132 | Salata, Derek | SCH_BOO | Cutter | RHH | 121 | 0.0042 | 0.0000 | 0.2297 | 0.2340 | 47.3 | 44.6 | 13 |
| 1155 | Morrissey, Joe | EVA_OTT | Cutter | RHH | 38 | 0.0041 | 0.0000 | 0.2299 | 0.2340 | 47.0 | 43.5 | 14 |
| 1162 | Lockhart, Gauge | LAK_ERI24 | Cutter | RHH | 74 | 0.0040 | 0.0000 | 0.2299 | 0.2340 | 46.9 | 43.2 | 15 |

### Four-Seam vs LHH

| Rank | Pitcher | Team | Pitch Type | Batter Side | Pitches | Avg Adv | Median Adv | Grid xwOBA | League xwOBA | LS 20-80 | LS 0-100 | Type/Side Rank |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 95 | Davis, Tyler | WAS_WIL3 | Four-Seam | LHH | 48 | 0.0184 | 0.0249 | 0.2239 | 0.2423 | 69.3 | 95.4 | 1 |
| 119 | Parsons, Billy | SUS_COU1 | Four-Seam | LHH | 199 | 0.0171 | 0.0135 | 0.2251 | 0.2423 | 67.4 | 94.2 | 2 |
| 121 | Toribio, Noe | TRO_AIG | Four-Seam | LHH | 25 | 0.0171 | 0.0191 | 0.2252 | 0.2423 | 67.3 | 94.1 | 3 |
| 155 | Hughes, Grif | EVA_OTT | Four-Seam | LHH | 30 | 0.0160 | 0.0091 | 0.2263 | 0.2423 | 65.6 | 92.5 | 4 |
| 162 | Foster, Kobe | WAS_WIL3 | Four-Seam | LHH | 186 | 0.0158 | 0.0191 | 0.2265 | 0.2423 | 65.2 | 92.1 | 5 |
| 164 | Fowler, Dalton | SUS_COU1 | Four-Seam | LHH | 43 | 0.0157 | 0.0228 | 0.2265 | 0.2423 | 65.2 | 92.0 | 6 |
| 168 | Brothers, Kellen | SUS_COU1 | Four-Seam | LHH | 237 | 0.0157 | 0.0143 | 0.2266 | 0.2423 | 65.1 | 91.8 | 7 |
| 172 | Ferguson, Francis | QUE_CAP | Four-Seam | LHH | 51 | 0.0156 | 0.0135 | 0.2267 | 0.2423 | 65.0 | 91.6 | 8 |
| 188 | Smith, Ben | NEW_ENG23 | Four-Seam | LHH | 45 | 0.0153 | 0.0135 | 0.2270 | 0.2423 | 64.4 | 90.8 | 9 |
| 189 | Alpern, Liam | FLO_Y'A | Four-Seam | LHH | 86 | 0.0152 | 0.0116 | 0.2271 | 0.2423 | 64.3 | 90.8 | 10 |
| 190 | Hard, Sean | NEW_JER6 | Four-Seam | LHH | 41 | 0.0152 | 0.0000 | 0.2271 | 0.2423 | 64.3 | 90.7 | 11 |
| 216 | Wehrle, Tyler | WIN_CIT29 | Four-Seam | LHH | 176 | 0.0144 | 0.0091 | 0.2279 | 0.2423 | 63.1 | 89.5 | 12 |
| 221 | Lyons, Kendall | QUE_CAP | Four-Seam | LHH | 25 | 0.0142 | 0.0084 | 0.2280 | 0.2423 | 62.8 | 89.2 | 13 |
| 229 | Barreto, Brayhans | TRI_VAL | Four-Seam | LHH | 66 | 0.0141 | 0.0218 | 0.2282 | 0.2423 | 62.6 | 88.8 | 14 |
| 236 | Herbert, Andrew | WAS_WIL3 | Four-Seam | LHH | 35 | 0.0139 | 0.0135 | 0.2284 | 0.2423 | 62.3 | 88.5 | 15 |

### Four-Seam vs RHH

| Rank | Pitcher | Team | Pitch Type | Batter Side | Pitches | Avg Adv | Median Adv | Grid xwOBA | League xwOBA | LS 20-80 | LS 0-100 | Type/Side Rank |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 17 | Mercado, Nelson | OTT_TIT | Four-Seam | RHH | 42 | 0.0251 | 0.0260 | 0.2120 | 0.2371 | 79.8 | 99.2 | 1 |
| 28 | Kemlage, Joe | NEW_ENG23 | Four-Seam | RHH | 28 | 0.0240 | 0.0200 | 0.2131 | 0.2371 | 78.0 | 98.7 | 2 |
| 32 | Johnson, Preston | MIS_MUD | Four-Seam | RHH | 28 | 0.0231 | 0.0223 | 0.2139 | 0.2371 | 76.7 | 98.5 | 3 |
| 63 | Delvecchio, Dylan | LAK_ERI24 | Four-Seam | RHH | 25 | 0.0202 | 0.0207 | 0.2169 | 0.2371 | 72.1 | 97.0 | 4 |
| 69 | Petraitis, AJ | LEM_COL | Four-Seam | RHH | 29 | 0.0198 | 0.0235 | 0.2173 | 0.2371 | 71.5 | 96.7 | 5 |
| 79 | Brothers, Kellen | SUS_COU1 | Four-Seam | RHH | 208 | 0.0193 | 0.0156 | 0.2177 | 0.2371 | 70.8 | 96.2 | 6 |
| 91 | Albert, Wes | TRI_VAL | Four-Seam | RHH | 54 | 0.0185 | 0.0183 | 0.2185 | 0.2371 | 69.6 | 95.6 | 7 |
| 92 | Hard, Sean | NEW_JER6 | Four-Seam | RHH | 29 | 0.0185 | 0.0070 | 0.2185 | 0.2371 | 69.5 | 95.5 | 8 |
| 93 | Morse, Colby | EVA_OTT | Four-Seam | RHH | 42 | 0.0185 | 0.0153 | 0.2186 | 0.2371 | 69.5 | 95.5 | 9 |
| 99 | Kalisky, Jack | OTT_TIT | Four-Seam | RHH | 68 | 0.0182 | 0.0198 | 0.2189 | 0.2371 | 69.0 | 95.2 | 10 |
| 108 | Chapple, Bronson | TRO_AIG | Four-Seam | RHH | 49 | 0.0178 | 0.0152 | 0.2193 | 0.2371 | 68.4 | 94.8 | 11 |
| 111 | Hughes, Grif | EVA_OTT | Four-Seam | RHH | 27 | 0.0176 | 0.0004 | 0.2194 | 0.2371 | 68.1 | 94.6 | 12 |
| 115 | Roitman, Justin | WAG_SEA | Four-Seam | RHH | 40 | 0.0173 | 0.0031 | 0.2197 | 0.2371 | 67.7 | 94.4 | 13 |
| 124 | O'Dell, Casey | JOL_SLA | Four-Seam | RHH | 79 | 0.0170 | 0.0149 | 0.2200 | 0.2371 | 67.2 | 94.0 | 14 |
| 125 | Hohenstein, Liam | WIN_CIT29 | Four-Seam | RHH | 26 | 0.0170 | 0.0113 | 0.2201 | 0.2371 | 67.1 | 93.9 | 15 |

### Sinker vs LHH

| Rank | Pitcher | Team | Pitch Type | Batter Side | Pitches | Avg Adv | Median Adv | Grid xwOBA | League xwOBA | LS 20-80 | LS 0-100 | Type/Side Rank |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 217 | Aldeano, Austin | TRO_AIG | Sinker | LHH | 45 | 0.0144 | 0.0137 | 0.2427 | 0.2570 | 63.1 | 89.4 | 1 |
| 281 | McCartney, Seth | MIS_MUD | Sinker | LHH | 67 | 0.0131 | 0.0137 | 0.2439 | 0.2570 | 61.1 | 86.3 | 2 |
| 378 | Williams, Pierce | NEW_ENG23 | Sinker | LHH | 29 | 0.0116 | 0.0157 | 0.2455 | 0.2570 | 58.7 | 81.5 | 3 |
| 402 | Gilleran, James | NEW_ENG23 | Sinker | LHH | 25 | 0.0112 | 0.0052 | 0.2459 | 0.2570 | 58.1 | 80.4 | 4 |
| 421 | Cook, Cole | SCH_BOO | Sinker | LHH | 57 | 0.0109 | 0.0157 | 0.2462 | 0.2570 | 57.6 | 79.4 | 5 |
| 424 | Delongchamp, Luke | TRI_VAL | Sinker | LHH | 75 | 0.0108 | 0.0052 | 0.2462 | 0.2570 | 57.5 | 79.3 | 6 |
| 427 | Kelly, Aiden | TRI_VAL | Sinker | LHH | 51 | 0.0108 | 0.0000 | 0.2462 | 0.2570 | 57.5 | 79.1 | 7 |
| 445 | Hicks, Jackson | DOW_EAS1 | Sinker | LHH | 31 | 0.0105 | 0.0000 | 0.2465 | 0.2570 | 57.1 | 78.3 | 8 |
| 462 | Sechrist, Zander | WAS_WIL3 | Sinker | LHH | 32 | 0.0103 | 0.0050 | 0.2468 | 0.2570 | 56.6 | 77.4 | 9 |
| 484 | Sabatine, Gino | TRI_VAL | Sinker | LHH | 36 | 0.0100 | 0.0035 | 0.2470 | 0.2570 | 56.3 | 76.4 | 10 |
| 486 | Kines, Gunnar | JOL_SLA | Sinker | LHH | 73 | 0.0100 | 0.0157 | 0.2470 | 0.2570 | 56.2 | 76.3 | 11 |
| 488 | Reeves, Cobe | NEW_YOR13 | Sinker | LHH | 56 | 0.0100 | 0.0056 | 0.2471 | 0.2570 | 56.2 | 76.2 | 12 |
| 508 | Schueller, Jase | MIS_MUD | Sinker | LHH | 38 | 0.0097 | 0.0071 | 0.2473 | 0.2570 | 55.8 | 75.2 | 13 |
| 538 | O'Brien, Keenan | SUS_COU1 | Sinker | LHH | 53 | 0.0094 | 0.0060 | 0.2477 | 0.2570 | 55.2 | 73.7 | 14 |
| 567 | Hensey, Rob | SUS_COU1 | Sinker | LHH | 173 | 0.0090 | 0.0114 | 0.2480 | 0.2570 | 54.7 | 72.3 | 15 |

### Sinker vs RHH

| Rank | Pitcher | Team | Pitch Type | Batter Side | Pitches | Avg Adv | Median Adv | Grid xwOBA | League xwOBA | LS 20-80 | LS 0-100 | Type/Side Rank |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 120 | Aldeano, Austin | TRO_AIG | Sinker | RHH | 25 | 0.0171 | 0.0273 | 0.2336 | 0.2507 | 67.3 | 94.2 | 1 |
| 204 | Leach, Landon | TRO_AIG | Sinker | RHH | 60 | 0.0148 | 0.0085 | 0.2359 | 0.2507 | 63.8 | 90.1 | 2 |
| 210 | Donnan, Blake | FLO_Y'A | Sinker | RHH | 84 | 0.0147 | 0.0129 | 0.2361 | 0.2507 | 63.5 | 89.8 | 3 |
| 260 | O'Brien, Keenan | SUS_COU1 | Sinker | RHH | 38 | 0.0134 | 0.0043 | 0.2373 | 0.2507 | 61.6 | 87.3 | 4 |
| 325 | Colon, Jeffrey | TRO_AIG | Sinker | RHH | 26 | 0.0123 | 0.0066 | 0.2385 | 0.2507 | 59.8 | 84.1 | 5 |
| 340 | Glickstein, Aaron | SCH_BOO | Sinker | RHH | 84 | 0.0120 | 0.0113 | 0.2387 | 0.2507 | 59.4 | 83.4 | 6 |
| 341 | Petschke, Ben | EVA_OTT | Sinker | RHH | 44 | 0.0120 | 0.0048 | 0.2387 | 0.2507 | 59.4 | 83.4 | 7 |
| 369 | Garcia, Andrew | EVA_OTT | Sinker | RHH | 29 | 0.0117 | 0.0043 | 0.2391 | 0.2507 | 58.8 | 82.0 | 8 |
| 385 | Shears, Tanner | SCH_BOO | Sinker | RHH | 50 | 0.0115 | 0.0021 | 0.2393 | 0.2507 | 58.5 | 81.2 | 9 |
| 398 | Delongchamp, Luke | TRI_VAL | Sinker | RHH | 74 | 0.0112 | 0.0062 | 0.2395 | 0.2507 | 58.2 | 80.6 | 10 |
| 406 | Lockhart, Gauge | LAK_ERI24 | Sinker | RHH | 34 | 0.0111 | 0.0000 | 0.2396 | 0.2507 | 58.0 | 80.2 | 11 |
| 417 | Hoeymans, Jack | GAT_GRI | Sinker | RHH | 35 | 0.0110 | 0.0000 | 0.2398 | 0.2507 | 57.7 | 79.6 | 12 |
| 483 | Ryan, Dillon | NEW_ENG23 | Sinker | RHH | 133 | 0.0100 | 0.0038 | 0.2407 | 0.2507 | 56.3 | 76.4 | 13 |
| 493 | Kelly, Aiden | TRI_VAL | Sinker | RHH | 27 | 0.0099 | 0.0043 | 0.2408 | 0.2507 | 56.1 | 75.9 | 14 |
| 500 | Turner, Eric | JOL_SLA | Sinker | RHH | 53 | 0.0099 | 0.0077 | 0.2409 | 0.2507 | 56.0 | 75.6 | 15 |

### Slider vs LHH

| Rank | Pitcher | Team | Pitch Type | Batter Side | Pitches | Avg Adv | Median Adv | Grid xwOBA | League xwOBA | LS 20-80 | LS 0-100 | Type/Side Rank |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 123 | Eckaus, David | EVA_OTT | Slider | LHH | 138 | 0.0170 | 0.0038 | 0.2193 | 0.2363 | 67.2 | 94.0 | 1 |
| 139 | Harris, Everette | TRI_VAL | Slider | LHH | 33 | 0.0165 | 0.0160 | 0.2199 | 0.2363 | 66.3 | 93.2 | 2 |
| 161 | Potteiger, Jack | JOL_SLA | Slider | LHH | 30 | 0.0159 | 0.0110 | 0.2205 | 0.2363 | 65.4 | 92.2 | 3 |
| 212 | Cook, Cole | SCH_BOO | Slider | LHH | 156 | 0.0145 | 0.0045 | 0.2218 | 0.2363 | 63.3 | 89.7 | 4 |
| 215 | Barker, Alex | NEW_YOR13 | Slider | LHH | 118 | 0.0144 | 0.0045 | 0.2219 | 0.2363 | 63.2 | 89.5 | 5 |
| 220 | Foltz Jr., Michael | WAS_WIL3 | Slider | LHH | 31 | 0.0143 | 0.0074 | 0.2220 | 0.2363 | 62.9 | 89.3 | 6 |
| 238 | McEvoy, Aidan | FLO_Y'A | Slider | LHH | 88 | 0.0138 | 0.0074 | 0.2226 | 0.2363 | 62.1 | 88.4 | 7 |
| 241 | Culley, Wesley | LAK_ERI24 | Slider | LHH | 26 | 0.0137 | 0.0038 | 0.2226 | 0.2363 | 62.1 | 88.3 | 8 |
| 251 | MacMillan, Blake | TRO_AIG | Slider | LHH | 64 | 0.0136 | 0.0022 | 0.2227 | 0.2363 | 61.9 | 87.8 | 9 |
| 263 | Scott, Brandon | LAK_ERI24 | Slider | LHH | 70 | 0.0134 | 0.0036 | 0.2230 | 0.2363 | 61.5 | 87.2 | 10 |
| 272 | Misla, Luis | TRI_VAL | Slider | LHH | 62 | 0.0133 | 0.0000 | 0.2231 | 0.2363 | 61.3 | 86.7 | 11 |
| 280 | Cox, Carter | NIU_HUS | Slider | LHH | 26 | 0.0132 | 0.0056 | 0.2232 | 0.2363 | 61.2 | 86.3 | 12 |
| 299 | Webster, Evan | FLO_Y'A | Slider | LHH | 81 | 0.0126 | 0.0080 | 0.2237 | 0.2363 | 60.4 | 85.4 | 13 |
| 301 | Campbell, Tyler | MIS_MUD | Slider | LHH | 133 | 0.0126 | 0.0074 | 0.2237 | 0.2363 | 60.3 | 85.3 | 14 |
| 306 | Soto, Carlos | JOL_SLA | Slider | LHH | 34 | 0.0126 | 0.0037 | 0.2237 | 0.2363 | 60.3 | 85.1 | 15 |

### Slider vs RHH

| Rank | Pitcher | Team | Pitch Type | Batter Side | Pitches | Avg Adv | Median Adv | Grid xwOBA | League xwOBA | LS 20-80 | LS 0-100 | Type/Side Rank |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | Hohenstein, Liam | WIN_CIT29 | Slider | RHH | 27 | 0.0333 | 0.0255 | 0.1958 | 0.2291 | 80.0 | 100.0 | 1 |
| 2 | Garcia, Hector | WAS_WIL3 | Slider | RHH | 36 | 0.0303 | 0.0348 | 0.1987 | 0.2291 | 80.0 | 100.0 | 2 |
| 3 | Finarelli, Nick | LON_ISL22 | Slider | RHH | 31 | 0.0298 | 0.0200 | 0.1993 | 0.2291 | 80.0 | 99.9 | 3 |
| 4 | Wiltse, Ryan | EVA_OTT | Slider | RHH | 74 | 0.0296 | 0.0200 | 0.1995 | 0.2291 | 80.0 | 99.9 | 4 |
| 5 | Cameron, Wyatt | TRI_VAL | Slider | RHH | 25 | 0.0292 | 0.0395 | 0.1998 | 0.2291 | 80.0 | 99.8 | 5 |
| 6 | Stegura, Drew | WAS_WIL3 | Slider | RHH | 25 | 0.0282 | 0.0343 | 0.2009 | 0.2291 | 80.0 | 99.8 | 6 |
| 7 | Givens-Craig, Hayden | SUS_COU1 | Slider | RHH | 28 | 0.0279 | 0.0235 | 0.2012 | 0.2291 | 80.0 | 99.7 | 7 |
| 8 | Smith, Ethan | WIN_CIT29 | Slider | RHH | 30 | 0.0272 | 0.0182 | 0.2019 | 0.2291 | 80.0 | 99.7 | 8 |
| 9 | Perdomo, Rafael | QUE_CAP | Slider | RHH | 73 | 0.0267 | 0.0081 | 0.2024 | 0.2291 | 80.0 | 99.6 | 9 |
| 10 | Cameron, Wyatt | SCH_BOO | Slider | RHH | 50 | 0.0266 | 0.0038 | 0.2024 | 0.2291 | 80.0 | 99.6 | 10 |
| 11 | Cerda, Junior | EVA_OTT | Slider | RHH | 116 | 0.0260 | 0.0164 | 0.2030 | 0.2291 | 80.0 | 99.5 | 11 |
| 12 | Hagan, Jack | DOW_EAS1 | Slider | RHH | 191 | 0.0259 | 0.0209 | 0.2032 | 0.2291 | 80.0 | 99.5 | 12 |
| 13 | Martinez, Gregory | DOW_EAS1 | Slider | RHH | 26 | 0.0258 | 0.0273 | 0.2032 | 0.2291 | 80.0 | 99.4 | 13 |
| 14 | Albert, Wes | TRI_VAL | Slider | RHH | 25 | 0.0257 | 0.0200 | 0.2033 | 0.2291 | 80.0 | 99.4 | 14 |
| 15 | Gilleran, Jimmy | NEW_ENG23 | Slider | RHH | 109 | 0.0257 | 0.0220 | 0.2034 | 0.2291 | 80.0 | 99.3 | 15 |

### Splitter vs LHH

| Rank | Pitcher | Team | Pitch Type | Batter Side | Pitches | Avg Adv | Median Adv | Grid xwOBA | League xwOBA | LS 20-80 | LS 0-100 | Type/Side Rank |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1090 | Bauer, Patrick | QUE_CAP | Splitter | LHH | 30 | 0.0046 | 0.0002 | 0.2384 | 0.2430 | 47.8 | 46.7 | 1 |
| 1348 | Eldred, Zach | NEW_ENG23 | Splitter | LHH | 51 | 0.0027 | 0.0000 | 0.2403 | 0.2430 | 44.9 | 34.1 | 2 |
| 1381 | Soto, Carlos | JOL_SLA | Splitter | LHH | 46 | 0.0025 | 0.0000 | 0.2405 | 0.2430 | 44.6 | 32.5 | 3 |
| 1407 | Thornton, Tyler | NEW_ENG23 | Splitter | LHH | 80 | 0.0024 | 0.0000 | 0.2406 | 0.2430 | 44.3 | 31.2 | 4 |
| 1419 | Vitas, Ben | JOL_SLA | Splitter | LHH | 116 | 0.0023 | 0.0000 | 0.2407 | 0.2430 | 44.2 | 30.6 | 5 |
| 1470 | Coles, Chad | WAS_WIL3 | Splitter | LHH | 38 | 0.0019 | 0.0000 | 0.2411 | 0.2430 | 43.7 | 28.1 | 6 |
| 1477 | Williams, Brian | MIS_MUD | Splitter | LHH | 72 | 0.0019 | 0.0000 | 0.2411 | 0.2430 | 43.6 | 27.8 | 7 |
| 1515 | Garcia, Hector | WAS_WIL3 | Splitter | LHH | 59 | 0.0017 | 0.0000 | 0.2413 | 0.2430 | 43.3 | 25.9 | 8 |
| 1571 | Salata, Derek | SCH_BOO | Splitter | LHH | 92 | 0.0012 | 0.0000 | 0.2418 | 0.2430 | 42.6 | 23.2 | 9 |
| 1604 | Thompson, Ross | SCH_BOO | Splitter | LHH | 183 | 0.0009 | 0.0000 | 0.2421 | 0.2430 | 42.0 | 21.5 | 10 |
| 1620 | Gilleran, Jimmy | NEW_ENG23 | Splitter | LHH | 39 | 0.0008 | 0.0000 | 0.2422 | 0.2430 | 41.8 | 20.8 | 11 |
| 1639 | Villers, Ian | QUE_CAP | Splitter | LHH | 39 | 0.0006 | 0.0000 | 0.2424 | 0.2430 | 41.6 | 19.8 | 12 |
| 1651 | Shears, Tanner | SCH_BOO | Splitter | LHH | 39 | 0.0005 | 0.0000 | 0.2425 | 0.2430 | 41.5 | 19.2 | 13 |
| 1653 | Parsons, Billy | SUS_COU1 | Splitter | LHH | 35 | 0.0005 | 0.0000 | 0.2425 | 0.2430 | 41.4 | 19.1 | 14 |
| 1663 | Perozzi, John | SUS_COU1 | Splitter | LHH | 44 | 0.0005 | 0.0000 | 0.2425 | 0.2430 | 41.4 | 18.6 | 15 |

### Splitter vs RHH

| Rank | Pitcher | Team | Pitch Type | Batter Side | Pitches | Avg Adv | Median Adv | Grid xwOBA | League xwOBA | LS 20-80 | LS 0-100 | Type/Side Rank |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1378 | Villers, Ian | QUE_CAP | Splitter | RHH | 25 | 0.0026 | 0.0022 | 0.2369 | 0.2394 | 44.6 | 32.6 | 1 |
| 1524 | Pindel, Buddie | SCH_BOO | Splitter | RHH | 35 | 0.0016 | 0.0000 | 0.2378 | 0.2394 | 43.2 | 25.5 | 2 |
| 1726 | Shears, Tanner | SCH_BOO | Splitter | RHH | 39 | -0.0000 | 0.0000 | 0.2394 | 0.2394 | 40.6 | 15.6 | 3 |
| 1752 | Williams, Brian | MIS_MUD | Splitter | RHH | 54 | -0.0003 | 0.0000 | 0.2397 | 0.2394 | 40.2 | 14.3 | 4 |
| 1794 | Eldred, Zach | NEW_ENG23 | Splitter | RHH | 41 | -0.0008 | 0.0000 | 0.2402 | 0.2394 | 39.4 | 12.2 | 5 |
| 1796 | Soto, Carlos | JOL_SLA | Splitter | RHH | 25 | -0.0008 | 0.0000 | 0.2402 | 0.2394 | 39.4 | 12.1 | 6 |
| 1818 | Coles, Chad | WAS_WIL3 | Splitter | RHH | 25 | -0.0011 | 0.0000 | 0.2405 | 0.2394 | 38.9 | 11.1 | 7 |
| 1833 | MacMillan, Blake | TRO_AIG | Splitter | RHH | 32 | -0.0012 | 0.0000 | 0.2407 | 0.2394 | 38.7 | 10.3 | 8 |
| 1835 | Thornton, Tyler | NEW_ENG23 | Splitter | RHH | 66 | -0.0012 | 0.0000 | 0.2407 | 0.2394 | 38.7 | 10.2 | 9 |
| 1842 | Andueza, Axel | DOW_EAS1 | Splitter | RHH | 61 | -0.0013 | 0.0000 | 0.2408 | 0.2394 | 38.5 | 9.9 | 10 |
| 1855 | Vitas, Ben | JOL_SLA | Splitter | RHH | 45 | -0.0014 | 0.0000 | 0.2408 | 0.2394 | 38.4 | 9.3 | 11 |
| 1864 | Martzolf, Max | JOL_SLA | Splitter | RHH | 31 | -0.0016 | 0.0000 | 0.2410 | 0.2394 | 38.2 | 8.8 | 12 |
| 1915 | Fuenmayor, Liu | OTT_TIT | Splitter | RHH | 27 | -0.0023 | 0.0000 | 0.2417 | 0.2394 | 37.1 | 6.3 | 13 |
| 1963 | Thompson, Ross | SCH_BOO | Splitter | RHH | 38 | -0.0031 | 0.0000 | 0.2426 | 0.2394 | 35.8 | 4.0 | 14 |
| 1975 | Nakata, Yuto | QUE_CAP | Splitter | RHH | 32 | -0.0036 | 0.0000 | 0.2430 | 0.2394 | 35.1 | 3.4 | 15 |

### Sweeper vs LHH

| Rank | Pitcher | Team | Pitch Type | Batter Side | Pitches | Avg Adv | Median Adv | Grid xwOBA | League xwOBA | LS 20-80 | LS 0-100 | Type/Side Rank |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1644 | Petschke, Ben | EVA_OTT | Sweeper | LHH | 40 | 0.0006 | 0.0000 | 0.2059 | 0.2065 | 41.5 | 19.6 | 1 |

### Sweeper vs RHH

| Rank | Pitcher | Team | Pitch Type | Batter Side | Pitches | Avg Adv | Median Adv | Grid xwOBA | League xwOBA | LS 20-80 | LS 0-100 | Type/Side Rank |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1701 | Cerda, Junior | EVA_OTT | Sweeper | RHH | 41 | 0.0002 | 0.0000 | 0.1928 | 0.1930 | 40.9 | 16.8 | 1 |
| 1849 | Simpson, Garret | EVA_OTT | Sweeper | RHH | 32 | -0.0014 | 0.0000 | 0.1944 | 0.1930 | 38.5 | 9.5 | 2 |
