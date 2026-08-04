# Handedness-Specific Pitch Leaderboards

- Pitch Value input: `data\processed\pitch_value_scores_with_type_rank.csv` (1,002 rows)
- Location Score input: `data\processed\location_scores.csv` (2,043 rows)
- Split component input: `data\processed\2026-data-with-woba-xwoba.parquet`
- Output file: `data\processed\pitch_leaderboard_splits.csv`
- Joined leaderboard rows: 1,783
- Formula: `0.70 * pitch_value_20_80 + 0.30 * location_score_20_80`
- Pitch Value is pitcher + pitch type level; Location Score supplies the batter-side split.
- Higher scores are better.

## Method

The leaderboard joins Pitch Value to Location Score by pitcher, team, and normalized pitch type. Because the Pitch Value table is not handedness-specific, each pitcher-pitch Pitch Value is paired with its available LHH and/or RHH Location Score rows.

Ground-ball, strikeout, line-drive, and fly-ball component scores are calculated separately for each pitcher + pitch type + batter side row, then ranked within the split leaderboard. Higher strikeout and ground-ball rates score better; lower line-drive and fly-ball rates score better.

`final_pitch_score_raw` and `final_pitch_score` are the weighted 20-80 blend. `final_pitch_score_0_100` is the percentile rank of that blended score among all split rows.

## Overall Leaderboard

| Rank | Pitcher | Team | Pitch Type | Batter Side | Split Pitches | PVS | Loc | Final | Final % | Avg Loc Adv | Type Rank | Type/Side Rank |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | Sanders, Brayden | MIS_MUD | Slider | RHH | 44 | 76.6 | 72.2 | 75.3 | 100.0 | 0.0202 | 1 | 1 |
| 2 | Bargo, Casey | NEW_ENG23 | Slider | RHH | 29 | 73.6 | 78.9 | 75.2 | 99.9 | 0.0245 | 2 | 2 |
| 3 | Harley, Tristan | SUS_COU1 | Slider | RHH | 44 | 77.0 | 70.0 | 74.9 | 99.9 | 0.0188 | 3 | 3 |
| 4 | Ryan, Dillon | NEW_ENG23 | Slider | RHH | 76 | 79.6 | 64.0 | 74.9 | 99.8 | 0.0150 | 4 | 4 |
| 5 | Bauer, Patrick | QUE_CAP | Slider | RHH | 65 | 76.5 | 70.9 | 74.8 | 99.8 | 0.0194 | 5 | 5 |
| 6 | Vecerka, Boris | QUE_CAP | Slider | RHH | 62 | 80.0 | 62.6 | 74.8 | 99.7 | 0.0141 | 6 | 6 |
| 7 | Grounds, Jackson | DOW_EAS1 | Curveball | RHH | 43 | 80.0 | 60.6 | 74.2 | 99.7 | 0.0128 | 1 | 1 |
| 8 | Kirby, Zach | WAS_WIL3 | Slider | RHH | 126 | 71.6 | 79.8 | 74.1 | 99.6 | 0.0251 | 7 | 7 |
| 9 | Carroll, Jake | JOL_SLA | Slider | LHH | 55 | 80.0 | 52.7 | 71.8 | 99.6 | 0.0077 | 8 | 1 |
| 10 | Grounds, Jackson | DOW_EAS1 | Four-Seam | RHH | 48 | 74.1 | 64.6 | 71.2 | 99.5 | 0.0153 | 1 | 1 |
| 11 | Harper, Scott | NEW_YOR13 | Slider | RHH | 193 | 72.8 | 66.3 | 70.8 | 99.4 | 0.0164 | 9 | 8 |
| 12 | Ryan, Dillon | NEW_ENG23 | Slider | LHH | 73 | 79.6 | 50.3 | 70.8 | 99.4 | 0.0062 | 10 | 2 |
| 13 | Morgan, Cooper | QUE_CAP | Curveball | LHH | 77 | 78.8 | 51.0 | 70.4 | 99.3 | 0.0066 | 2 | 1 |
| 14 | Flontek, Zac | DOW_EAS1 | Slider | RHH | 35 | 80.0 | 47.9 | 70.4 | 99.3 | 0.0046 | 11 | 9 |
| 15 | Duncan, Tanner | DOW_EAS1 | Slider | RHH | 58 | 67.9 | 76.1 | 70.3 | 99.2 | 0.0228 | 12 | 10 |
| 16 | Flontek, Zac | DOW_EAS1 | Slider | LHH | 41 | 80.0 | 47.1 | 70.1 | 99.2 | 0.0041 | 13 | 3 |
| 17 | Morrissey, Joe | EVA_OTT | Cutter | RHH | 38 | 80.0 | 47.0 | 70.1 | 99.1 | 0.0041 | 1 | 1 |
| 18 | Davis, Tyler | WIN_CIT29 | Four-Seam | RHH | 33 | 74.4 | 59.9 | 70.1 | 99.0 | 0.0123 | 2 | 2 |
| 19 | Alpern, Liam | FLO_Y'A | Slider | LHH | 38 | 76.1 | 55.8 | 70.0 | 99.0 | 0.0097 | 14 | 4 |
| 20 | Heintz, Danny | FLO_Y'A | Four-Seam | RHH | 36 | 75.8 | 54.9 | 69.6 | 98.9 | 0.0092 | 3 | 3 |
| 21 | Grounds, Jackson | DOW_EAS1 | Curveball | LHH | 39 | 80.0 | 45.2 | 69.6 | 98.9 | 0.0029 | 3 | 2 |
| 22 | McEvoy, Aidan | FLO_Y'A | Slider | LHH | 88 | 71.9 | 62.1 | 69.0 | 98.8 | 0.0138 | 15 | 5 |
| 23 | Nakata, Yuto | QUE_CAP | Slider | RHH | 99 | 69.0 | 68.6 | 68.9 | 98.8 | 0.0179 | 16 | 11 |
| 24 | O'Dell, Casey | JOL_SLA | Slider | RHH | 41 | 66.1 | 74.7 | 68.7 | 98.7 | 0.0219 | 17 | 12 |
| 25 | Sparks, Alec | GAT_GRI | Curveball | LHH | 51 | 76.0 | 51.6 | 68.7 | 98.7 | 0.0070 | 4 | 3 |
| 26 | Donnan, Blake | FLO_Y'A | Slider | RHH | 52 | 69.7 | 65.1 | 68.4 | 98.6 | 0.0157 | 18 | 13 |
| 27 | Jones, Logan | TRI_VAL | Slider | LHH | 33 | 74.3 | 54.3 | 68.3 | 98.5 | 0.0088 | 19 | 6 |
| 28 | Debban, Caleb | NEW_JER6 | Four-Seam | RHH | 37 | 73.5 | 55.8 | 68.2 | 98.5 | 0.0097 | 4 | 4 |
| 29 | Marynczak, Arlo | TRI_VAL | Slider | RHH | 49 | 66.7 | 70.8 | 67.9 | 98.4 | 0.0194 | 20 | 14 |
| 30 | Barraza, Chris | MIS_MUD | Slider | RHH | 57 | 64.2 | 74.7 | 67.4 | 98.4 | 0.0219 | 21 | 15 |
| 31 | Grounds, Jackson | DOW_EAS1 | Four-Seam | LHH | 59 | 74.1 | 51.1 | 67.2 | 98.3 | 0.0067 | 5 | 1 |
| 32 | Vega, Lucas | TRO_AIG | Slider | RHH | 94 | 66.7 | 68.4 | 67.2 | 98.3 | 0.0178 | 22 | 16 |
| 33 | Scafidi, Christian | LAK_ERI24 | Cutter | RHH | 27 | 74.4 | 50.1 | 67.1 | 98.2 | 0.0060 | 2 | 2 |
| 34 | Tomczak, Anthony | EVA_OTT | Slider | RHH | 55 | 66.4 | 67.2 | 66.7 | 98.1 | 0.0170 | 23 | 17 |
| 35 | Peyton, Blake | GAT_GRI | Changeup | RHH | 104 | 70.8 | 56.1 | 66.4 | 98.1 | 0.0099 | 1 | 1 |
| 36 | Mercado, Nelson | OTT_TIT | Four-Seam | RHH | 42 | 60.6 | 79.8 | 66.4 | 98.0 | 0.0251 | 6 | 5 |
| 37 | Davis, Tyler | WIN_CIT29 | Four-Seam | LHH | 43 | 74.4 | 47.5 | 66.3 | 98.0 | 0.0044 | 7 | 2 |
| 38 | MacMillan, Blake | TRO_AIG | Slider | LHH | 64 | 68.1 | 61.9 | 66.2 | 97.9 | 0.0136 | 24 | 7 |
| 39 | Earwood, Micah | SUS_COU1 | Four-Seam | RHH | 96 | 73.3 | 49.6 | 66.2 | 97.9 | 0.0057 | 8 | 6 |
| 40 | Jones, Logan | TRI_VAL | Slider | RHH | 32 | 74.3 | 46.6 | 66.0 | 97.8 | 0.0038 | 25 | 18 |

## Pitch Type + Batter Side Leaderboards

### Changeup vs LHH

| Rank | Pitcher | Team | Pitch Type | Batter Side | Split Pitches | PVS | Loc | Final | Final % | Avg Loc Adv | Type Rank | Type/Side Rank |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 42 | Lawson, Nathan | FLO_Y'A | Changeup | LHH | 74 | 68.9 | 58.5 | 65.8 | 97.7 | 0.0114 | 2 | 1 |
| 45 | Rodriguez, Joe Joe | NEW_JER6 | Changeup | LHH | 140 | 69.1 | 56.8 | 65.4 | 97.5 | 0.0104 | 3 | 2 |
| 47 | Escobar, Anthony | TRO_AIG | Changeup | LHH | 187 | 67.6 | 60.1 | 65.4 | 97.4 | 0.0125 | 4 | 3 |
| 65 | Perdomo, Rafael | QUE_CAP | Changeup | LHH | 52 | 69.1 | 52.0 | 64.0 | 96.4 | 0.0073 | 5 | 4 |
| 73 | O'Hanlon, Michael | WAS_WIL3 | Changeup | LHH | 60 | 66.4 | 56.7 | 63.5 | 96.0 | 0.0103 | 8 | 5 |
| 77 | Parsons, Billy | SUS_COU1 | Changeup | LHH | 43 | 68.4 | 51.1 | 63.2 | 95.7 | 0.0067 | 9 | 6 |
| 86 | Harris, Everette | TRI_VAL | Changeup | LHH | 71 | 66.3 | 54.7 | 62.8 | 95.2 | 0.0090 | 11 | 7 |
| 96 | Good, Ty | GAT_GRI | Changeup | LHH | 59 | 70.7 | 43.4 | 62.5 | 94.7 | 0.0018 | 12 | 8 |
| 100 | Maietta, Dante | WIN_CIT29 | Changeup | LHH | 193 | 61.5 | 63.9 | 62.2 | 94.4 | 0.0149 | 13 | 9 |
| 106 | Leak, Anthony | NEW_YOR13 | Changeup | LHH | 77 | 64.3 | 56.6 | 62.0 | 94.1 | 0.0102 | 14 | 10 |
| 107 | Wiltse, Ryan | EVA_OTT | Changeup | LHH | 137 | 67.4 | 49.6 | 62.0 | 94.1 | 0.0057 | 15 | 11 |
| 115 | Drakeford, Dosie | NEW_JER6 | Changeup | LHH | 66 | 64.5 | 54.9 | 61.6 | 93.6 | 0.0091 | 16 | 12 |
| 119 | Sesar, Jorden | SUS_COU1 | Changeup | LHH | 75 | 62.5 | 59.3 | 61.5 | 93.4 | 0.0119 | 17 | 13 |
| 134 | Eisenbarger, Jack | QUE_CAP | Changeup | LHH | 45 | 60.5 | 61.4 | 60.8 | 92.5 | 0.0133 | 20 | 14 |
| 141 | Dill, Austin | TRI_VAL | Changeup | LHH | 118 | 56.2 | 70.5 | 60.5 | 92.1 | 0.0191 | 21 | 15 |
| 163 | Serrano, Elio | NEW_JER6 | Changeup | LHH | 91 | 61.8 | 55.7 | 60.0 | 90.9 | 0.0096 | 25 | 16 |
| 194 | Soto, Noel | TRI_VAL | Changeup | LHH | 48 | 55.5 | 66.7 | 58.9 | 89.2 | 0.0167 | 27 | 17 |
| 209 | Campbell, Tyler | MIS_MUD | Changeup | LHH | 25 | 65.6 | 41.1 | 58.3 | 88.3 | 0.0003 | 28 | 18 |
| 210 | Tokar, Heitor | OTT_TIT | Changeup | LHH | 47 | 63.9 | 45.1 | 58.2 | 88.3 | 0.0029 | 29 | 19 |
| 225 | Marynczak, Arlo | TRI_VAL | Changeup | LHH | 159 | 56.9 | 60.1 | 57.9 | 87.4 | 0.0125 | 30 | 20 |
| 236 | Willeman, Landon | EVA_OTT | Changeup | LHH | 163 | 58.6 | 55.5 | 57.6 | 86.8 | 0.0095 | 31 | 21 |
| 238 | Kowalski, Benjamin | WAS_WIL3 | Changeup | LHH | 41 | 56.0 | 61.3 | 57.6 | 86.7 | 0.0132 | 32 | 22 |
| 246 | Barreto, Brayhans | TRI_VAL | Changeup | LHH | 31 | 60.9 | 49.5 | 57.5 | 86.3 | 0.0057 | 34 | 23 |
| 267 | Daly, Ryan | JOL_SLA | Changeup | LHH | 192 | 56.6 | 58.3 | 57.1 | 85.1 | 0.0114 | 36 | 24 |
| 278 | Cameron, Zach | WIN_CIT29 | Changeup | LHH | 163 | 57.0 | 57.1 | 57.0 | 84.5 | 0.0105 | 38 | 25 |

### Changeup vs RHH

| Rank | Pitcher | Team | Pitch Type | Batter Side | Split Pitches | PVS | Loc | Final | Final % | Avg Loc Adv | Type Rank | Type/Side Rank |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 35 | Peyton, Blake | GAT_GRI | Changeup | RHH | 104 | 70.8 | 56.1 | 66.4 | 98.1 | 0.0099 | 1 | 1 |
| 68 | Smith, Ben | NEW_ENG23 | Changeup | RHH | 60 | 62.9 | 65.7 | 63.8 | 96.2 | 0.0160 | 6 | 2 |
| 69 | Rodriguez, Joe Joe | NEW_JER6 | Changeup | RHH | 47 | 69.1 | 51.3 | 63.7 | 96.2 | 0.0068 | 7 | 3 |
| 84 | Wiltse, Ryan | EVA_OTT | Changeup | RHH | 65 | 67.4 | 52.3 | 62.8 | 95.3 | 0.0075 | 10 | 4 |
| 120 | Lawson, Nathan | FLO_Y'A | Changeup | RHH | 33 | 68.9 | 44.1 | 61.5 | 93.3 | 0.0022 | 18 | 5 |
| 127 | Campbell, Tyler | MIS_MUD | Changeup | RHH | 113 | 65.6 | 51.1 | 61.3 | 92.9 | 0.0067 | 19 | 6 |
| 142 | Zentko, Dylan | EVA_OTT | Changeup | RHH | 90 | 61.6 | 58.1 | 60.5 | 92.1 | 0.0112 | 22 | 7 |
| 144 | Messina, Chris | FDU_KNI | Changeup | RHH | 52 | 66.4 | 46.7 | 60.5 | 92.0 | 0.0039 | 23 | 8 |
| 162 | Harris, Everette | TRI_VAL | Changeup | RHH | 47 | 66.3 | 45.3 | 60.0 | 91.0 | 0.0030 | 24 | 9 |
| 168 | Earwood, Micah | SUS_COU1 | Changeup | RHH | 199 | 63.3 | 51.9 | 59.8 | 90.6 | 0.0072 | 26 | 10 |
| 243 | Andueza, Axel | DOW_EAS1 | Changeup | RHH | 26 | 58.0 | 56.5 | 57.5 | 86.4 | 0.0102 | 33 | 11 |
| 247 | VanMarter, Luke | LEM_COL | Changeup | RHH | 29 | 59.0 | 53.8 | 57.5 | 86.2 | 0.0084 | 35 | 12 |
| 276 | Maietta, Dante | WIN_CIT29 | Changeup | RHH | 137 | 61.5 | 46.8 | 57.1 | 84.6 | 0.0039 | 37 | 13 |
| 284 | Eisenbarger, Jack | QUE_CAP | Changeup | RHH | 182 | 60.5 | 48.5 | 56.9 | 84.1 | 0.0050 | 40 | 14 |
| 296 | Barreto, Brayhans | TRI_VAL | Changeup | RHH | 99 | 60.9 | 46.7 | 56.7 | 83.5 | 0.0039 | 42 | 15 |
| 311 | Hocom, Quinn | TRI_VAL | Changeup | RHH | 37 | 55.1 | 59.4 | 56.4 | 82.6 | 0.0121 | 44 | 16 |
| 332 | Morgan, Cooper | QUE_CAP | Changeup | RHH | 75 | 61.9 | 42.4 | 56.0 | 81.4 | 0.0011 | 46 | 17 |
| 339 | Brothers, Kellen | SUS_COU1 | Changeup | RHH | 61 | 58.7 | 49.4 | 55.9 | 81.0 | 0.0056 | 47 | 18 |
| 343 | Rohde, Isaac | NEW_YOR13 | Changeup | RHH | 680 | 56.6 | 54.1 | 55.9 | 80.8 | 0.0086 | 48 | 19 |
| 350 | Tokar, Heitor | OTT_TIT | Changeup | RHH | 33 | 63.9 | 36.6 | 55.7 | 80.4 | -0.0026 | 50 | 20 |
| 362 | Foster, Kobe | WAS_WIL3 | Changeup | RHH | 208 | 59.9 | 45.5 | 55.5 | 79.8 | 0.0031 | 51 | 21 |
| 401 | Salata, Derek | SCH_BOO | Changeup | RHH | 70 | 58.1 | 47.6 | 55.0 | 77.6 | 0.0045 | 53 | 22 |
| 431 | Cameron, Zach | WIN_CIT29 | Changeup | RHH | 86 | 57.0 | 48.8 | 54.5 | 75.9 | 0.0053 | 57 | 23 |
| 462 | Willeman, Landon | EVA_OTT | Changeup | RHH | 54 | 58.6 | 43.9 | 54.2 | 74.1 | 0.0021 | 59 | 24 |
| 474 | Barker, Alex | NEW_YOR13 | Changeup | RHH | 185 | 54.2 | 53.5 | 54.0 | 73.5 | 0.0082 | 63 | 25 |

### Curveball vs LHH

| Rank | Pitcher | Team | Pitch Type | Batter Side | Split Pitches | PVS | Loc | Final | Final % | Avg Loc Adv | Type Rank | Type/Side Rank |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 13 | Morgan, Cooper | QUE_CAP | Curveball | LHH | 77 | 78.8 | 51.0 | 70.4 | 99.3 | 0.0066 | 2 | 1 |
| 21 | Grounds, Jackson | DOW_EAS1 | Curveball | LHH | 39 | 80.0 | 45.2 | 69.6 | 98.9 | 0.0029 | 3 | 2 |
| 25 | Sparks, Alec | GAT_GRI | Curveball | LHH | 51 | 76.0 | 51.6 | 68.7 | 98.7 | 0.0070 | 4 | 3 |
| 87 | Bohnert, Matthew | WIN_CIT29 | Curveball | LHH | 62 | 69.9 | 46.3 | 62.8 | 95.2 | 0.0036 | 9 | 4 |
| 104 | Pierson, Kenny | LAK_ERI24 | Curveball | LHH | 67 | 69.3 | 45.1 | 62.1 | 94.2 | 0.0029 | 11 | 5 |
| 116 | Binns, Malik | NEW_JER6 | Curveball | LHH | 27 | 66.2 | 51.0 | 61.6 | 93.6 | 0.0066 | 15 | 6 |
| 129 | Rodriguez, Ramon | WIN_CIT29 | Curveball | LHH | 55 | 69.9 | 40.6 | 61.1 | 92.8 | -0.0000 | 16 | 7 |
| 169 | Heredia-Bustos, Rolando | DOW_EAS1 | Curveball | LHH | 35 | 66.0 | 45.2 | 59.8 | 90.6 | 0.0029 | 20 | 8 |
| 185 | Hohenstein, Liam | WIN_CIT29 | Curveball | LHH | 48 | 67.0 | 40.8 | 59.2 | 89.7 | 0.0001 | 22 | 9 |
| 203 | Eisenbarger, Jack | QUE_CAP | Curveball | LHH | 68 | 63.9 | 45.6 | 58.4 | 88.7 | 0.0032 | 24 | 10 |
| 264 | Hocom, Quinn | TRI_VAL | Curveball | LHH | 48 | 59.8 | 51.2 | 57.2 | 85.2 | 0.0068 | 33 | 11 |
| 272 | Hickey, Matt | GAT_GRI | Curveball | LHH | 36 | 65.0 | 38.7 | 57.1 | 84.8 | -0.0013 | 34 | 12 |
| 287 | Salata, Derek | SCH_BOO | Curveball | LHH | 56 | 63.1 | 42.4 | 56.9 | 84.0 | 0.0011 | 36 | 13 |
| 299 | Harris, Ben | GAT_GRI | Curveball | LHH | 143 | 63.1 | 41.6 | 56.6 | 83.3 | 0.0006 | 37 | 14 |
| 329 | Campbell, AJ | WIN_CIT29 | Curveball | LHH | 32 | 59.8 | 47.5 | 56.1 | 81.6 | 0.0044 | 41 | 15 |
| 356 | Hill, Kaleb | OTT_TIT | Curveball | LHH | 137 | 61.2 | 42.5 | 55.6 | 80.1 | 0.0012 | 45 | 16 |
| 364 | Kostura, Brit | WAS_WIL3 | Curveball | LHH | 54 | 60.8 | 43.3 | 55.5 | 79.6 | 0.0017 | 46 | 17 |
| 367 | Langrell, Connor | MIS_MUD | Curveball | LHH | 77 | 59.1 | 47.2 | 55.5 | 79.5 | 0.0042 | 47 | 18 |
| 405 | Garcia, Brett | OTT_TIT | Curveball | LHH | 69 | 62.1 | 38.0 | 54.9 | 77.3 | -0.0017 | 51 | 19 |
| 445 | Long, Jalon | NEW_YOR13 | Curveball | LHH | 27 | 53.8 | 55.8 | 54.4 | 75.1 | 0.0097 | 54 | 20 |
| 458 | Scafidi, Christian | LAK_ERI24 | Curveball | LHH | 25 | 61.2 | 38.0 | 54.2 | 74.4 | -0.0017 | 57 | 21 |
| 482 | Lefebvre, Charles | TRO_AIG | Curveball | LHH | 64 | 58.5 | 42.7 | 53.7 | 73.0 | 0.0013 | 59 | 22 |
| 488 | Boies, Emiles | QUE_CAP | Curveball | LHH | 43 | 61.2 | 36.0 | 53.7 | 72.7 | -0.0030 | 60 | 23 |
| 495 | Cook, Cole | SCH_BOO | Curveball | LHH | 56 | 60.1 | 38.2 | 53.5 | 72.3 | -0.0016 | 61 | 24 |
| 504 | Earwood, Micah | SUS_COU1 | Curveball | LHH | 72 | 58.2 | 42.4 | 53.4 | 71.8 | 0.0012 | 63 | 25 |

### Curveball vs RHH

| Rank | Pitcher | Team | Pitch Type | Batter Side | Split Pitches | PVS | Loc | Final | Final % | Avg Loc Adv | Type Rank | Type/Side Rank |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 7 | Grounds, Jackson | DOW_EAS1 | Curveball | RHH | 43 | 80.0 | 60.6 | 74.2 | 99.7 | 0.0128 | 1 | 1 |
| 46 | Sparks, Alec | GAT_GRI | Curveball | RHH | 38 | 76.0 | 40.6 | 65.4 | 97.5 | -0.0000 | 5 | 2 |
| 55 | Hohenstein, Liam | WIN_CIT29 | Curveball | RHH | 61 | 67.0 | 59.6 | 64.8 | 97.0 | 0.0122 | 6 | 3 |
| 72 | Jones, Breyln | NEW_JER6 | Curveball | RHH | 37 | 68.5 | 52.3 | 63.6 | 96.0 | 0.0075 | 7 | 4 |
| 85 | Heredia-Bustos, Rolando | DOW_EAS1 | Curveball | RHH | 40 | 66.0 | 55.3 | 62.8 | 95.3 | 0.0094 | 8 | 5 |
| 97 | Binns, Malik | NEW_JER6 | Curveball | RHH | 28 | 66.2 | 53.6 | 62.4 | 94.6 | 0.0083 | 10 | 6 |
| 109 | Rodriguez, Ramon | WIN_CIT29 | Curveball | RHH | 64 | 69.9 | 43.0 | 61.9 | 93.9 | 0.0015 | 12 | 7 |
| 112 | Hampton, Ky | OTT_TIT | Curveball | RHH | 61 | 61.3 | 62.8 | 61.8 | 93.8 | 0.0142 | 13 | 8 |
| 113 | Salata, Derek | SCH_BOO | Curveball | RHH | 131 | 63.1 | 58.5 | 61.7 | 93.7 | 0.0115 | 14 | 9 |
| 148 | Bohnert, Matthew | WIN_CIT29 | Curveball | RHH | 62 | 69.9 | 38.4 | 60.4 | 91.8 | -0.0014 | 17 | 10 |
| 156 | Hickey, Matt | GAT_GRI | Curveball | RHH | 48 | 65.0 | 49.0 | 60.2 | 91.3 | 0.0054 | 18 | 11 |
| 164 | Harris, Ben | GAT_GRI | Curveball | RHH | 181 | 63.1 | 52.6 | 60.0 | 90.9 | 0.0077 | 19 | 12 |
| 182 | Conklin, MacCallan | TRO_AIG | Curveball | RHH | 36 | 64.2 | 47.8 | 59.3 | 89.8 | 0.0046 | 21 | 13 |
| 201 | Boies, Emiles | QUE_CAP | Curveball | RHH | 75 | 61.2 | 52.3 | 58.5 | 88.8 | 0.0075 | 23 | 14 |
| 227 | Garcia, Brett | OTT_TIT | Curveball | RHH | 84 | 62.1 | 47.9 | 57.8 | 87.3 | 0.0046 | 25 | 15 |
| 229 | Allemann, Braeden | QUE_CAP | Curveball | RHH | 158 | 56.1 | 61.7 | 57.8 | 87.2 | 0.0135 | 26 | 16 |
| 240 | Langrell, Connor | MIS_MUD | Curveball | RHH | 79 | 59.1 | 54.1 | 57.6 | 86.6 | 0.0086 | 27 | 17 |
| 241 | Maryniak, Connor | NEW_JER6 | Curveball | RHH | 96 | 56.8 | 59.2 | 57.6 | 86.5 | 0.0119 | 28 | 18 |
| 250 | Wiltse, Ryan | EVA_OTT | Curveball | RHH | 62 | 58.6 | 54.8 | 57.4 | 86.0 | 0.0091 | 29 | 19 |
| 255 | Scafidi, Christian | LAK_ERI24 | Curveball | RHH | 36 | 61.2 | 48.3 | 57.3 | 85.8 | 0.0049 | 30 | 20 |
| 258 | Eisenbarger, Jack | QUE_CAP | Curveball | RHH | 30 | 63.9 | 41.8 | 57.3 | 85.6 | 0.0008 | 31 | 21 |
| 259 | Lefebvre, Charles | TRO_AIG | Curveball | RHH | 60 | 58.5 | 54.5 | 57.3 | 85.5 | 0.0089 | 32 | 22 |
| 286 | Kostura, Brit | WAS_WIL3 | Curveball | RHH | 33 | 60.8 | 47.9 | 56.9 | 84.0 | 0.0046 | 35 | 23 |
| 305 | Hocom, Quinn | TRI_VAL | Curveball | RHH | 72 | 59.8 | 48.9 | 56.5 | 83.0 | 0.0053 | 38 | 24 |
| 326 | Zaffiro, Cole | SCH_BOO | Curveball | RHH | 61 | 59.5 | 48.3 | 56.1 | 81.8 | 0.0049 | 39 | 25 |

### Cutter vs LHH

| Rank | Pitcher | Team | Pitch Type | Batter Side | Split Pitches | PVS | Loc | Final | Final % | Avg Loc Adv | Type Rank | Type/Side Rank |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 57 | Scafidi, Christian | LAK_ERI24 | Cutter | LHH | 25 | 74.4 | 41.3 | 64.5 | 96.9 | 0.0004 | 3 | 1 |
| 90 | Barreto, Brayhans | TRI_VAL | Cutter | LHH | 33 | 72.4 | 39.8 | 62.6 | 95.0 | -0.0006 | 5 | 2 |
| 108 | Majick, Eli | NEW_ENG23 | Cutter | LHH | 34 | 70.8 | 41.2 | 61.9 | 94.0 | 0.0004 | 6 | 3 |
| 111 | Webster, Evan | FLO_Y'A | Cutter | LHH | 104 | 70.3 | 42.0 | 61.8 | 93.8 | 0.0009 | 7 | 4 |
| 176 | Correa, Nelvin | QUE_CAP | Cutter | LHH | 73 | 67.8 | 40.2 | 59.5 | 90.2 | -0.0003 | 11 | 5 |
| 235 | Parsons, Billy | SUS_COU1 | Cutter | LHH | 45 | 64.1 | 42.6 | 57.7 | 86.9 | 0.0013 | 13 | 6 |
| 366 | Morgan, Marcus | JOL_SLA | Cutter | LHH | 40 | 61.0 | 42.6 | 55.5 | 79.5 | 0.0012 | 15 | 7 |
| 371 | Lockhart, Gauge | LAK_ERI24 | Cutter | LHH | 74 | 62.6 | 38.7 | 55.4 | 79.2 | -0.0013 | 16 | 8 |
| 388 | Garcia, Jorge | SUS_COU1 | Cutter | LHH | 30 | 60.5 | 42.6 | 55.1 | 78.3 | 0.0013 | 17 | 9 |
| 580 | Flontek, Zac | DOW_EAS1 | Cutter | LHH | 31 | 57.9 | 40.5 | 52.7 | 67.5 | -0.0001 | 22 | 10 |
| 650 | Saturria, Michael | NEW_ENG23 | Cutter | LHH | 133 | 58.5 | 36.8 | 52.0 | 63.6 | -0.0025 | 23 | 11 |
| 678 | Valdez, Alex | EVA_OTT | Cutter | LHH | 27 | 57.6 | 37.9 | 51.7 | 62.0 | -0.0018 | 25 | 12 |
| 699 | Debban, Caleb | NEW_JER6 | Cutter | LHH | 62 | 56.3 | 39.8 | 51.4 | 60.9 | -0.0005 | 27 | 13 |
| 721 | McEvoy, Aidan | FLO_Y'A | Cutter | LHH | 50 | 54.1 | 44.5 | 51.2 | 59.6 | 0.0025 | 29 | 14 |
| 748 | MacMillan, Blake | TRO_AIG | Cutter | LHH | 62 | 54.8 | 41.9 | 50.9 | 58.1 | 0.0008 | 31 | 15 |
| 766 | Campbell, Tyler | MIS_MUD | Cutter | LHH | 105 | 54.8 | 41.3 | 50.7 | 57.1 | 0.0004 | 32 | 16 |
| 767 | Gorgen, Grady | NEW_YOR13 | Cutter | LHH | 41 | 55.4 | 39.8 | 50.7 | 57.0 | -0.0005 | 33 | 17 |
| 776 | Moore, Kyle | SCH_BOO | Cutter | LHH | 39 | 54.8 | 40.9 | 50.6 | 56.5 | 0.0002 | 34 | 18 |
| 948 | Gamelin, Shaun | JOL_SLA | Cutter | LHH | 58 | 53.9 | 36.9 | 48.8 | 46.9 | -0.0024 | 44 | 19 |
| 953 | Bell, Brendan | NEW_ENG23 | Cutter | LHH | 66 | 51.7 | 41.8 | 48.7 | 46.6 | 0.0007 | 45 | 20 |
| 1000 | Campbell, AJ | WIN_CIT29 | Cutter | LHH | 44 | 51.1 | 41.7 | 48.3 | 44.0 | 0.0007 | 49 | 21 |
| 1023 | Langrell, Connor | MIS_MUD | Cutter | LHH | 144 | 50.3 | 42.9 | 48.1 | 42.7 | 0.0014 | 50 | 22 |
| 1110 | Petschke, Ben | EVA_OTT | Cutter | LHH | 174 | 48.0 | 45.5 | 47.3 | 37.8 | 0.0031 | 53 | 23 |
| 1113 | Smith, Jackson | MIS_MUD | Cutter | LHH | 60 | 51.0 | 38.4 | 47.2 | 37.6 | -0.0014 | 54 | 24 |
| 1119 | Parks, Pavin | LAK_ERI24 | Cutter | LHH | 41 | 49.7 | 41.2 | 47.2 | 37.3 | 0.0004 | 55 | 25 |

### Cutter vs RHH

| Rank | Pitcher | Team | Pitch Type | Batter Side | Split Pitches | PVS | Loc | Final | Final % | Avg Loc Adv | Type Rank | Type/Side Rank |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 17 | Morrissey, Joe | EVA_OTT | Cutter | RHH | 38 | 80.0 | 47.0 | 70.1 | 99.1 | 0.0041 | 1 | 1 |
| 33 | Scafidi, Christian | LAK_ERI24 | Cutter | RHH | 27 | 74.4 | 50.1 | 67.1 | 98.2 | 0.0060 | 2 | 2 |
| 63 | Majick, Eli | NEW_ENG23 | Cutter | RHH | 83 | 70.8 | 48.8 | 64.2 | 96.5 | 0.0052 | 4 | 3 |
| 135 | Webster, Evan | FLO_Y'A | Cutter | RHH | 47 | 70.3 | 38.5 | 60.8 | 92.5 | -0.0013 | 8 | 4 |
| 145 | Correa, Nelvin | QUE_CAP | Cutter | RHH | 66 | 67.8 | 43.4 | 60.5 | 91.9 | 0.0018 | 9 | 5 |
| 171 | Leak, Anthony | NEW_YOR13 | Cutter | RHH | 44 | 68.6 | 39.2 | 59.8 | 90.5 | -0.0009 | 10 | 6 |
| 224 | Lockhart, Gauge | LAK_ERI24 | Cutter | RHH | 74 | 62.6 | 46.9 | 57.9 | 87.5 | 0.0040 | 12 | 7 |
| 348 | Garcia, Jorge | SUS_COU1 | Cutter | RHH | 28 | 60.5 | 44.5 | 55.7 | 80.5 | 0.0025 | 14 | 8 |
| 412 | Good, Ty | GAT_GRI | Cutter | RHH | 44 | 56.4 | 51.1 | 54.8 | 76.9 | 0.0067 | 18 | 9 |
| 420 | Valdez, Alex | EVA_OTT | Cutter | RHH | 78 | 57.6 | 48.0 | 54.7 | 76.5 | 0.0047 | 19 | 10 |
| 438 | Saturria, Michael | NEW_ENG23 | Cutter | RHH | 131 | 58.5 | 44.9 | 54.4 | 75.5 | 0.0027 | 20 | 11 |
| 549 | Wiltse, Ryan | EVA_OTT | Cutter | RHH | 59 | 55.8 | 46.2 | 52.9 | 69.3 | 0.0036 | 21 | 12 |
| 657 | Flontek, Zac | DOW_EAS1 | Cutter | RHH | 33 | 57.9 | 38.0 | 51.9 | 63.2 | -0.0017 | 24 | 13 |
| 695 | Gorgen, Grady | NEW_YOR13 | Cutter | RHH | 42 | 55.4 | 42.1 | 51.4 | 61.1 | 0.0009 | 26 | 14 |
| 703 | Debban, Caleb | NEW_JER6 | Cutter | RHH | 82 | 56.3 | 39.8 | 51.3 | 60.6 | -0.0006 | 28 | 15 |
| 727 | Bell, Brendan | NEW_ENG23 | Cutter | RHH | 58 | 51.7 | 49.8 | 51.2 | 59.3 | 0.0059 | 30 | 16 |
| 787 | Moore, Kyle | SCH_BOO | Cutter | RHH | 125 | 54.8 | 40.5 | 50.5 | 55.9 | -0.0001 | 35 | 17 |
| 803 | Gamelin, Shaun | JOL_SLA | Cutter | RHH | 90 | 53.9 | 41.8 | 50.3 | 55.0 | 0.0007 | 36 | 18 |
| 833 | McEvoy, Aidan | FLO_Y'A | Cutter | RHH | 58 | 54.1 | 40.2 | 49.9 | 53.3 | -0.0003 | 37 | 19 |
| 844 | Campbell, AJ | WIN_CIT29 | Cutter | RHH | 54 | 51.1 | 46.9 | 49.8 | 52.7 | 0.0040 | 38 | 20 |
| 887 | Savinon, Jordan | NEW_YOR13 | Cutter | RHH | 41 | 56.5 | 33.0 | 49.4 | 50.3 | -0.0049 | 39 | 21 |
| 911 | Smith, Jackson | MIS_MUD | Cutter | RHH | 83 | 51.0 | 44.9 | 49.2 | 49.0 | 0.0027 | 40 | 22 |
| 925 | Campbell, Tyler | MIS_MUD | Cutter | RHH | 151 | 54.8 | 35.8 | 49.1 | 48.2 | -0.0031 | 41 | 23 |
| 934 | MacMillan, Blake | TRO_AIG | Cutter | RHH | 88 | 54.8 | 35.4 | 49.0 | 47.7 | -0.0033 | 42 | 24 |
| 944 | Ginn, Landon | WAS_WIL3 | Cutter | RHH | 68 | 48.8 | 49.0 | 48.9 | 47.1 | 0.0054 | 43 | 25 |

### Four-Seam vs LHH

| Rank | Pitcher | Team | Pitch Type | Batter Side | Split Pitches | PVS | Loc | Final | Final % | Avg Loc Adv | Type Rank | Type/Side Rank |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 31 | Grounds, Jackson | DOW_EAS1 | Four-Seam | LHH | 59 | 74.1 | 51.1 | 67.2 | 98.3 | 0.0067 | 5 | 1 |
| 37 | Davis, Tyler | WIN_CIT29 | Four-Seam | LHH | 43 | 74.4 | 47.5 | 66.3 | 98.0 | 0.0044 | 7 | 2 |
| 124 | Morgan, Cooper | QUE_CAP | Four-Seam | LHH | 45 | 61.9 | 60.1 | 61.3 | 93.1 | 0.0125 | 13 | 3 |
| 143 | Cameron, Zach | WIN_CIT29 | Four-Seam | LHH | 69 | 68.7 | 41.3 | 60.5 | 92.0 | 0.0004 | 16 | 4 |
| 146 | Cartwright, Eli | GAT_GRI | Four-Seam | LHH | 61 | 61.4 | 58.4 | 60.5 | 91.9 | 0.0114 | 17 | 5 |
| 147 | Foster, Kobe | WAS_WIL3 | Four-Seam | LHH | 186 | 58.4 | 65.2 | 60.4 | 91.8 | 0.0158 | 18 | 6 |
| 151 | Mercado, Nelson | OTT_TIT | Four-Seam | LHH | 39 | 60.6 | 59.8 | 60.4 | 91.6 | 0.0123 | 19 | 7 |
| 192 | Herbert, Andrew | WAS_WIL3 | Four-Seam | LHH | 35 | 57.5 | 62.3 | 58.9 | 89.3 | 0.0139 | 24 | 8 |
| 195 | Correa, Nelvin | QUE_CAP | Four-Seam | LHH | 47 | 67.7 | 37.9 | 58.8 | 89.1 | -0.0017 | 25 | 9 |
| 212 | Foy, Corbin | LAK_ERI24 | Four-Seam | LHH | 48 | 65.5 | 40.8 | 58.1 | 88.2 | 0.0001 | 30 | 10 |
| 234 | Culley, Wesley | LAK_ERI24 | Four-Seam | LHH | 28 | 57.2 | 58.8 | 57.7 | 86.9 | 0.0116 | 36 | 11 |
| 237 | Blowers, CJ | FLO_Y'A | Four-Seam | LHH | 78 | 58.2 | 56.1 | 57.6 | 86.8 | 0.0099 | 37 | 12 |
| 242 | Langhorne, Miles | SUS_COU1 | Four-Seam | LHH | 30 | 58.9 | 54.3 | 57.5 | 86.5 | 0.0088 | 38 | 13 |
| 252 | Zaffiro, Cole | SCH_BOO | Four-Seam | LHH | 194 | 58.0 | 55.9 | 57.4 | 85.9 | 0.0098 | 39 | 14 |
| 256 | Anderson, Colt | WAS_WIL3 | Four-Seam | LHH | 140 | 59.8 | 51.4 | 57.3 | 85.7 | 0.0069 | 40 | 15 |
| 269 | Hensey, Rob | SUS_COU1 | Four-Seam | LHH | 85 | 63.0 | 43.3 | 57.1 | 85.0 | 0.0017 | 44 | 16 |
| 275 | Brown, Ethan | WAS_WIL3 | Four-Seam | LHH | 25 | 61.9 | 45.7 | 57.1 | 84.6 | 0.0032 | 45 | 17 |
| 279 | Alpern, Liam | FLO_Y'A | Four-Seam | LHH | 86 | 53.8 | 64.3 | 57.0 | 84.4 | 0.0152 | 47 | 18 |
| 306 | Hughes, Grif | EVA_OTT | Four-Seam | LHH | 30 | 52.6 | 65.6 | 56.5 | 82.9 | 0.0160 | 54 | 19 |
| 312 | Kemlage, Joe | NEW_ENG23 | Four-Seam | LHH | 25 | 57.8 | 53.3 | 56.4 | 82.6 | 0.0081 | 55 | 20 |
| 313 | Fowler, Dalton | SUS_COU1 | Four-Seam | LHH | 43 | 52.7 | 65.2 | 56.4 | 82.5 | 0.0157 | 56 | 21 |
| 314 | Gregory, Ben | GAT_GRI | Four-Seam | LHH | 49 | 60.9 | 45.9 | 56.4 | 82.4 | 0.0034 | 57 | 22 |
| 316 | Wehrle, Tyler | WIN_CIT29 | Four-Seam | LHH | 176 | 53.5 | 63.1 | 56.4 | 82.3 | 0.0144 | 58 | 23 |
| 317 | Shears, Tanner | SCH_BOO | Four-Seam | LHH | 114 | 59.4 | 49.2 | 56.4 | 82.3 | 0.0055 | 59 | 24 |
| 328 | Almanzar, Elian | DOW_EAS1 | Four-Seam | LHH | 82 | 53.9 | 61.2 | 56.1 | 81.7 | 0.0132 | 63 | 25 |

### Four-Seam vs RHH

| Rank | Pitcher | Team | Pitch Type | Batter Side | Split Pitches | PVS | Loc | Final | Final % | Avg Loc Adv | Type Rank | Type/Side Rank |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 10 | Grounds, Jackson | DOW_EAS1 | Four-Seam | RHH | 48 | 74.1 | 64.6 | 71.2 | 99.5 | 0.0153 | 1 | 1 |
| 18 | Davis, Tyler | WIN_CIT29 | Four-Seam | RHH | 33 | 74.4 | 59.9 | 70.1 | 99.0 | 0.0123 | 2 | 2 |
| 20 | Heintz, Danny | FLO_Y'A | Four-Seam | RHH | 36 | 75.8 | 54.9 | 69.6 | 98.9 | 0.0092 | 3 | 3 |
| 28 | Debban, Caleb | NEW_JER6 | Four-Seam | RHH | 37 | 73.5 | 55.8 | 68.2 | 98.5 | 0.0097 | 4 | 4 |
| 36 | Mercado, Nelson | OTT_TIT | Four-Seam | RHH | 42 | 60.6 | 79.8 | 66.4 | 98.0 | 0.0251 | 6 | 5 |
| 39 | Earwood, Micah | SUS_COU1 | Four-Seam | RHH | 96 | 73.3 | 49.6 | 66.2 | 97.9 | 0.0057 | 8 | 6 |
| 44 | Cameron, Zach | WIN_CIT29 | Four-Seam | RHH | 75 | 68.7 | 57.8 | 65.5 | 97.6 | 0.0110 | 9 | 7 |
| 66 | Kemlage, Joe | NEW_ENG23 | Four-Seam | RHH | 28 | 57.8 | 78.0 | 63.8 | 96.4 | 0.0240 | 10 | 8 |
| 92 | Correa, Nelvin | QUE_CAP | Four-Seam | RHH | 61 | 67.7 | 50.5 | 62.6 | 94.9 | 0.0063 | 11 | 9 |
| 93 | Foy, Corbin | LAK_ERI24 | Four-Seam | RHH | 47 | 65.5 | 55.5 | 62.5 | 94.8 | 0.0096 | 12 | 10 |
| 126 | Gregory, Ben | GAT_GRI | Four-Seam | RHH | 100 | 60.9 | 62.4 | 61.3 | 93.0 | 0.0140 | 14 | 11 |
| 132 | Langhorne, Miles | SUS_COU1 | Four-Seam | RHH | 40 | 58.9 | 65.8 | 61.0 | 92.7 | 0.0162 | 15 | 12 |
| 178 | Kelly, Colin | SUS_COU1 | Four-Seam | RHH | 49 | 58.4 | 62.0 | 59.5 | 90.1 | 0.0137 | 20 | 13 |
| 183 | Foster, Kobe | WAS_WIL3 | Four-Seam | RHH | 291 | 58.4 | 61.3 | 59.3 | 89.8 | 0.0133 | 21 | 14 |
| 184 | Campbell, Tyler | MIS_MUD | Four-Seam | RHH | 37 | 68.6 | 37.5 | 59.2 | 89.7 | -0.0020 | 22 | 15 |
| 187 | Flontek, Zac | DOW_EAS1 | Four-Seam | RHH | 239 | 56.7 | 64.5 | 59.0 | 89.6 | 0.0153 | 23 | 16 |
| 197 | Zaffiro, Cole | SCH_BOO | Four-Seam | RHH | 246 | 58.0 | 60.3 | 58.7 | 89.0 | 0.0126 | 26 | 17 |
| 198 | Shears, Tanner | SCH_BOO | Four-Seam | RHH | 171 | 59.4 | 57.0 | 58.7 | 89.0 | 0.0105 | 27 | 18 |
| 207 | Brouwer, Adam | LAK_ERI24 | Four-Seam | RHH | 41 | 57.7 | 59.8 | 58.3 | 88.4 | 0.0123 | 28 | 19 |
| 208 | Rodriguez, Joe Joe | NEW_JER6 | Four-Seam | RHH | 85 | 54.6 | 66.9 | 58.3 | 88.4 | 0.0168 | 29 | 20 |
| 216 | Johnson, Preston | MIS_MUD | Four-Seam | RHH | 28 | 50.0 | 76.7 | 58.0 | 87.9 | 0.0231 | 31 | 21 |
| 220 | Albert, Wes | TRI_VAL | Four-Seam | RHH | 54 | 53.0 | 69.6 | 58.0 | 87.7 | 0.0185 | 32 | 22 |
| 223 | Garcia, Brett | OTT_TIT | Four-Seam | RHH | 191 | 57.4 | 59.2 | 57.9 | 87.5 | 0.0119 | 33 | 23 |
| 226 | Blowers, CJ | FLO_Y'A | Four-Seam | RHH | 87 | 58.2 | 57.0 | 57.9 | 87.4 | 0.0105 | 34 | 24 |
| 233 | Hensey, Rob | SUS_COU1 | Four-Seam | RHH | 158 | 63.0 | 45.2 | 57.7 | 87.0 | 0.0029 | 35 | 25 |

### Sinker vs LHH

| Rank | Pitcher | Team | Pitch Type | Batter Side | Split Pitches | PVS | Loc | Final | Final % | Avg Loc Adv | Type Rank | Type/Side Rank |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 89 | Riedel, Caleb | SCH_BOO | Sinker | LHH | 33 | 70.6 | 43.8 | 62.6 | 95.1 | 0.0020 | 5 | 1 |
| 136 | Glickstein, Aaron | SCH_BOO | Sinker | LHH | 41 | 66.6 | 47.3 | 60.8 | 92.4 | 0.0042 | 7 | 2 |
| 139 | Widener, Jacob | SUS_COU1 | Sinker | LHH | 87 | 64.0 | 52.6 | 60.6 | 92.3 | 0.0077 | 9 | 3 |
| 149 | Mannering, Shawn | DOW_EAS1 | Sinker | LHH | 27 | 63.1 | 54.2 | 60.4 | 91.7 | 0.0087 | 10 | 4 |
| 172 | Colon, Jeffrey | TRO_AIG | Sinker | LHH | 30 | 64.6 | 48.3 | 59.7 | 90.4 | 0.0049 | 12 | 5 |
| 202 | Sabatine, Gino | TRI_VAL | Sinker | LHH | 36 | 59.4 | 56.3 | 58.5 | 88.7 | 0.0100 | 13 | 6 |
| 211 | Grills, Evan | OTT_TIT | Sinker | LHH | 26 | 61.4 | 50.7 | 58.2 | 88.2 | 0.0064 | 15 | 7 |
| 221 | McCartney, Seth | MIS_MUD | Sinker | LHH | 67 | 56.6 | 61.1 | 58.0 | 87.7 | 0.0131 | 17 | 8 |
| 260 | Lovell, Justin | WIN_CIT29 | Sinker | LHH | 106 | 61.8 | 46.7 | 57.3 | 85.5 | 0.0039 | 19 | 9 |
| 289 | Plumadore, Carson | WIN_CIT29 | Sinker | LHH | 96 | 61.4 | 46.2 | 56.8 | 83.8 | 0.0036 | 21 | 10 |
| 292 | Aldeano, Austin | TRO_AIG | Sinker | LHH | 45 | 54.1 | 63.1 | 56.8 | 83.7 | 0.0144 | 22 | 11 |
| 309 | Morgan, Marcus | JOL_SLA | Sinker | LHH | 60 | 57.9 | 53.1 | 56.5 | 82.7 | 0.0080 | 23 | 12 |
| 378 | Odonnell, Brendan | NEW_ENG23 | Sinker | LHH | 43 | 63.1 | 37.1 | 55.3 | 78.9 | -0.0023 | 26 | 13 |
| 393 | Fritz, AJ | MIS_MUD | Sinker | LHH | 33 | 55.6 | 54.0 | 55.1 | 78.0 | 0.0085 | 28 | 14 |
| 396 | Lawson, Nathan | FLO_Y'A | Sinker | LHH | 153 | 57.3 | 49.7 | 55.0 | 77.8 | 0.0058 | 29 | 15 |
| 419 | Leak, Anthony | NEW_YOR13 | Sinker | LHH | 41 | 55.3 | 53.3 | 54.7 | 76.6 | 0.0081 | 31 | 16 |
| 430 | Hensey, Rob | SUS_COU1 | Sinker | LHH | 173 | 54.5 | 54.7 | 54.5 | 75.9 | 0.0090 | 32 | 17 |
| 448 | Lodes, Jett | FLO_Y'A | Sinker | LHH | 38 | 55.9 | 50.7 | 54.3 | 74.9 | 0.0065 | 36 | 18 |
| 478 | Fauci, Sonny | NEW_JER6 | Sinker | LHH | 86 | 55.8 | 49.1 | 53.8 | 73.2 | 0.0054 | 38 | 19 |
| 491 | Kelly, Aiden | TRI_VAL | Sinker | LHH | 51 | 52.0 | 57.5 | 53.6 | 72.5 | 0.0108 | 41 | 20 |
| 531 | Grounds, Jackson | DOW_EAS1 | Sinker | LHH | 75 | 57.0 | 43.9 | 53.1 | 70.3 | 0.0021 | 45 | 21 |
| 543 | Gregory, Ben | GAT_GRI | Sinker | LHH | 91 | 53.6 | 51.5 | 53.0 | 69.6 | 0.0070 | 48 | 22 |
| 555 | Long, Maddox | WAS_WIL3 | Sinker | LHH | 168 | 55.9 | 46.0 | 52.9 | 68.9 | 0.0035 | 49 | 23 |
| 558 | Vecerka, Boris | QUE_CAP | Sinker | LHH | 138 | 52.6 | 53.7 | 52.9 | 68.8 | 0.0083 | 50 | 24 |
| 595 | Turner, Eric | JOL_SLA | Sinker | LHH | 60 | 55.5 | 45.6 | 52.5 | 66.7 | 0.0032 | 52 | 25 |

### Sinker vs RHH

| Rank | Pitcher | Team | Pitch Type | Batter Side | Split Pitches | PVS | Loc | Final | Final % | Avg Loc Adv | Type Rank | Type/Side Rank |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 58 | Glickstein, Aaron | SCH_BOO | Sinker | RHH | 84 | 66.6 | 59.4 | 64.4 | 96.8 | 0.0120 | 1 | 1 |
| 76 | Riedel, Caleb | SCH_BOO | Sinker | RHH | 58 | 70.6 | 46.0 | 63.3 | 95.8 | 0.0035 | 2 | 2 |
| 78 | Colon, Jeffrey | TRO_AIG | Sinker | RHH | 26 | 64.6 | 59.8 | 63.1 | 95.7 | 0.0123 | 3 | 3 |
| 83 | Still, Stephen | TRI_VAL | Sinker | RHH | 50 | 69.4 | 47.7 | 62.8 | 95.4 | 0.0045 | 4 | 4 |
| 118 | Garcia, Andrew | EVA_OTT | Sinker | RHH | 29 | 62.7 | 58.8 | 61.6 | 93.4 | 0.0117 | 6 | 5 |
| 138 | Mannering, Shawn | DOW_EAS1 | Sinker | RHH | 32 | 63.1 | 54.8 | 60.6 | 92.3 | 0.0091 | 8 | 6 |
| 154 | Petschke, Ben | EVA_OTT | Sinker | RHH | 44 | 60.6 | 59.4 | 60.3 | 91.4 | 0.0120 | 11 | 7 |
| 206 | Plumadore, Carson | WIN_CIT29 | Sinker | RHH | 66 | 61.4 | 51.4 | 58.4 | 88.5 | 0.0069 | 14 | 8 |
| 215 | Aldeano, Austin | TRO_AIG | Sinker | RHH | 25 | 54.1 | 67.3 | 58.1 | 88.0 | 0.0171 | 16 | 9 |
| 249 | Widener, Jacob | SUS_COU1 | Sinker | RHH | 105 | 64.0 | 42.1 | 57.5 | 86.1 | 0.0009 | 18 | 10 |
| 266 | Odonnell, Brendan | NEW_ENG23 | Sinker | RHH | 92 | 63.1 | 43.3 | 57.2 | 85.1 | 0.0017 | 20 | 11 |
| 354 | Turner, Eric | JOL_SLA | Sinker | RHH | 53 | 55.5 | 56.0 | 55.6 | 80.2 | 0.0099 | 24 | 12 |
| 360 | Lovell, Justin | WIN_CIT29 | Sinker | RHH | 77 | 61.8 | 41.0 | 55.6 | 79.9 | 0.0002 | 25 | 13 |
| 384 | Lodes, Jett | FLO_Y'A | Sinker | RHH | 58 | 55.9 | 53.6 | 55.2 | 78.5 | 0.0083 | 27 | 14 |
| 414 | McCartney, Seth | MIS_MUD | Sinker | RHH | 53 | 56.6 | 50.3 | 54.7 | 76.8 | 0.0062 | 30 | 15 |
| 434 | Long, Maddox | WAS_WIL3 | Sinker | RHH | 117 | 55.9 | 51.3 | 54.5 | 75.7 | 0.0068 | 33 | 16 |
| 437 | Lawson, Nathan | FLO_Y'A | Sinker | RHH | 123 | 57.3 | 47.9 | 54.5 | 75.5 | 0.0046 | 34 | 17 |
| 443 | Morgan, Marcus | JOL_SLA | Sinker | RHH | 35 | 57.9 | 46.1 | 54.4 | 75.2 | 0.0035 | 35 | 18 |
| 476 | Grounds, Jackson | DOW_EAS1 | Sinker | RHH | 41 | 57.0 | 46.6 | 53.9 | 73.4 | 0.0038 | 37 | 19 |
| 481 | Kelly, Colin | SUS_COU1 | Sinker | RHH | 53 | 54.3 | 52.5 | 53.8 | 73.1 | 0.0076 | 39 | 20 |
| 489 | Barrett, Gabriel | NEW_YOR13 | Sinker | RHH | 37 | 55.3 | 49.9 | 53.6 | 72.6 | 0.0059 | 40 | 21 |
| 509 | Ryan, Dillon | NEW_ENG23 | Sinker | RHH | 133 | 52.1 | 56.3 | 53.4 | 71.5 | 0.0100 | 42 | 22 |
| 520 | Gregory, Ben | GAT_GRI | Sinker | RHH | 136 | 53.6 | 52.3 | 53.2 | 70.9 | 0.0075 | 43 | 23 |
| 523 | Kelly, Aiden | TRI_VAL | Sinker | RHH | 27 | 52.0 | 56.1 | 53.2 | 70.7 | 0.0099 | 44 | 24 |
| 533 | Henderson, Drew | DOW_EAS1 | Sinker | RHH | 50 | 55.2 | 48.0 | 53.1 | 70.2 | 0.0047 | 46 | 25 |

### Slider vs LHH

| Rank | Pitcher | Team | Pitch Type | Batter Side | Split Pitches | PVS | Loc | Final | Final % | Avg Loc Adv | Type Rank | Type/Side Rank |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 9 | Carroll, Jake | JOL_SLA | Slider | LHH | 55 | 80.0 | 52.7 | 71.8 | 99.6 | 0.0077 | 8 | 1 |
| 12 | Ryan, Dillon | NEW_ENG23 | Slider | LHH | 73 | 79.6 | 50.3 | 70.8 | 99.4 | 0.0062 | 10 | 2 |
| 16 | Flontek, Zac | DOW_EAS1 | Slider | LHH | 41 | 80.0 | 47.1 | 70.1 | 99.2 | 0.0041 | 13 | 3 |
| 19 | Alpern, Liam | FLO_Y'A | Slider | LHH | 38 | 76.1 | 55.8 | 70.0 | 99.0 | 0.0097 | 14 | 4 |
| 22 | McEvoy, Aidan | FLO_Y'A | Slider | LHH | 88 | 71.9 | 62.1 | 69.0 | 98.8 | 0.0138 | 15 | 5 |
| 27 | Jones, Logan | TRI_VAL | Slider | LHH | 33 | 74.3 | 54.3 | 68.3 | 98.5 | 0.0088 | 19 | 6 |
| 38 | MacMillan, Blake | TRO_AIG | Slider | LHH | 64 | 68.1 | 61.9 | 66.2 | 97.9 | 0.0136 | 24 | 7 |
| 48 | Harper, Scott | NEW_YOR13 | Slider | LHH | 50 | 72.8 | 48.0 | 65.3 | 97.4 | 0.0047 | 28 | 8 |
| 49 | Harley, Tristan | SUS_COU1 | Slider | LHH | 30 | 77.0 | 37.8 | 65.3 | 97.3 | -0.0018 | 29 | 9 |
| 52 | Balzan, Jackson | SUS_COU1 | Slider | LHH | 77 | 67.3 | 59.9 | 65.1 | 97.1 | 0.0123 | 32 | 10 |
| 79 | Kramer, Cameron | TRO_AIG | Slider | LHH | 32 | 75.7 | 33.7 | 63.1 | 95.6 | -0.0044 | 45 | 11 |
| 99 | Bargo, Casey | NEW_ENG23 | Slider | LHH | 27 | 73.6 | 36.1 | 62.3 | 94.5 | -0.0029 | 54 | 12 |
| 117 | Benitez, Jorge | NEW_JER6 | Slider | LHH | 85 | 64.5 | 54.6 | 61.6 | 93.5 | 0.0090 | 61 | 13 |
| 125 | Widener, Jacob | SUS_COU1 | Slider | LHH | 61 | 63.4 | 56.6 | 61.3 | 93.0 | 0.0102 | 65 | 14 |
| 128 | Eckaus, David | EVA_OTT | Slider | LHH | 138 | 58.7 | 67.2 | 61.3 | 92.9 | 0.0170 | 66 | 15 |
| 131 | Cook, Cole | SCH_BOO | Slider | LHH | 156 | 60.0 | 63.3 | 61.0 | 92.7 | 0.0145 | 68 | 16 |
| 140 | Duncan, Tanner | DOW_EAS1 | Slider | LHH | 30 | 67.9 | 43.5 | 60.6 | 92.2 | 0.0018 | 71 | 17 |
| 153 | Hensey, Rob | SUS_COU1 | Slider | LHH | 84 | 61.9 | 56.6 | 60.3 | 91.5 | 0.0102 | 73 | 18 |
| 157 | Morgan, Cooper | QUE_CAP | Slider | LHH | 49 | 61.1 | 58.0 | 60.2 | 91.3 | 0.0111 | 75 | 19 |
| 174 | Scott, Brandon | LAK_ERI24 | Slider | LHH | 70 | 58.9 | 61.5 | 59.7 | 90.3 | 0.0134 | 85 | 20 |
| 177 | Foster, Kobe | WAS_WIL3 | Slider | LHH | 124 | 61.7 | 54.2 | 59.5 | 90.1 | 0.0087 | 87 | 21 |
| 179 | Vega, Lucas | TRO_AIG | Slider | LHH | 40 | 66.7 | 42.5 | 59.4 | 90.0 | 0.0012 | 88 | 22 |
| 181 | Harris, Everette | TRI_VAL | Slider | LHH | 33 | 56.3 | 66.3 | 59.3 | 89.9 | 0.0165 | 90 | 23 |
| 186 | Webster, Evan | FLO_Y'A | Slider | LHH | 81 | 58.5 | 60.4 | 59.0 | 89.6 | 0.0126 | 91 | 24 |
| 189 | Barraza, Chris | MIS_MUD | Slider | LHH | 25 | 64.2 | 46.6 | 59.0 | 89.5 | 0.0038 | 92 | 25 |

### Slider vs RHH

| Rank | Pitcher | Team | Pitch Type | Batter Side | Split Pitches | PVS | Loc | Final | Final % | Avg Loc Adv | Type Rank | Type/Side Rank |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | Sanders, Brayden | MIS_MUD | Slider | RHH | 44 | 76.6 | 72.2 | 75.3 | 100.0 | 0.0202 | 1 | 1 |
| 2 | Bargo, Casey | NEW_ENG23 | Slider | RHH | 29 | 73.6 | 78.9 | 75.2 | 99.9 | 0.0245 | 2 | 2 |
| 3 | Harley, Tristan | SUS_COU1 | Slider | RHH | 44 | 77.0 | 70.0 | 74.9 | 99.9 | 0.0188 | 3 | 3 |
| 4 | Ryan, Dillon | NEW_ENG23 | Slider | RHH | 76 | 79.6 | 64.0 | 74.9 | 99.8 | 0.0150 | 4 | 4 |
| 5 | Bauer, Patrick | QUE_CAP | Slider | RHH | 65 | 76.5 | 70.9 | 74.8 | 99.8 | 0.0194 | 5 | 5 |
| 6 | Vecerka, Boris | QUE_CAP | Slider | RHH | 62 | 80.0 | 62.6 | 74.8 | 99.7 | 0.0141 | 6 | 6 |
| 8 | Kirby, Zach | WAS_WIL3 | Slider | RHH | 126 | 71.6 | 79.8 | 74.1 | 99.6 | 0.0251 | 7 | 7 |
| 11 | Harper, Scott | NEW_YOR13 | Slider | RHH | 193 | 72.8 | 66.3 | 70.8 | 99.4 | 0.0164 | 9 | 8 |
| 14 | Flontek, Zac | DOW_EAS1 | Slider | RHH | 35 | 80.0 | 47.9 | 70.4 | 99.3 | 0.0046 | 11 | 9 |
| 15 | Duncan, Tanner | DOW_EAS1 | Slider | RHH | 58 | 67.9 | 76.1 | 70.3 | 99.2 | 0.0228 | 12 | 10 |
| 23 | Nakata, Yuto | QUE_CAP | Slider | RHH | 99 | 69.0 | 68.6 | 68.9 | 98.8 | 0.0179 | 16 | 11 |
| 24 | O'Dell, Casey | JOL_SLA | Slider | RHH | 41 | 66.1 | 74.7 | 68.7 | 98.7 | 0.0219 | 17 | 12 |
| 26 | Donnan, Blake | FLO_Y'A | Slider | RHH | 52 | 69.7 | 65.1 | 68.4 | 98.6 | 0.0157 | 18 | 13 |
| 29 | Marynczak, Arlo | TRI_VAL | Slider | RHH | 49 | 66.7 | 70.8 | 67.9 | 98.4 | 0.0194 | 20 | 14 |
| 30 | Barraza, Chris | MIS_MUD | Slider | RHH | 57 | 64.2 | 74.7 | 67.4 | 98.4 | 0.0219 | 21 | 15 |
| 32 | Vega, Lucas | TRO_AIG | Slider | RHH | 94 | 66.7 | 68.4 | 67.2 | 98.3 | 0.0178 | 22 | 16 |
| 34 | Tomczak, Anthony | EVA_OTT | Slider | RHH | 55 | 66.4 | 67.2 | 66.7 | 98.1 | 0.0170 | 23 | 17 |
| 40 | Jones, Logan | TRI_VAL | Slider | RHH | 32 | 74.3 | 46.6 | 66.0 | 97.8 | 0.0038 | 25 | 18 |
| 41 | Townes, Holland | SCH_BOO | Slider | RHH | 36 | 68.4 | 60.3 | 66.0 | 97.8 | 0.0126 | 26 | 19 |
| 43 | Hickey, Matt | GAT_GRI | Slider | RHH | 91 | 67.9 | 59.8 | 65.5 | 97.6 | 0.0123 | 27 | 20 |
| 50 | Alpern, Liam | FLO_Y'A | Slider | RHH | 40 | 76.1 | 39.9 | 65.3 | 97.3 | -0.0005 | 30 | 21 |
| 51 | MacMillan, Blake | TRO_AIG | Slider | RHH | 44 | 68.1 | 58.1 | 65.1 | 97.2 | 0.0112 | 31 | 22 |
| 53 | Allemann, Braeden | QUE_CAP | Slider | RHH | 89 | 59.4 | 78.2 | 65.0 | 97.1 | 0.0241 | 33 | 23 |
| 54 | Morin, Jacob | QUE_CAP | Slider | RHH | 60 | 65.6 | 63.4 | 64.9 | 97.0 | 0.0146 | 34 | 24 |
| 56 | Petschke, Ben | EVA_OTT | Slider | RHH | 86 | 64.5 | 64.9 | 64.6 | 96.9 | 0.0156 | 35 | 25 |

### Splitter vs LHH

| Rank | Pitcher | Team | Pitch Type | Batter Side | Split Pitches | PVS | Loc | Final | Final % | Avg Loc Adv | Type Rank | Type/Side Rank |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 61 | Garcia, Hector | WAS_WIL3 | Splitter | LHH | 59 | 73.4 | 43.3 | 64.4 | 96.6 | 0.0017 | 1 | 1 |
| 152 | Coles, Chad | WAS_WIL3 | Splitter | LHH | 38 | 67.5 | 43.7 | 60.4 | 91.5 | 0.0019 | 2 | 2 |
| 213 | Villers, Ian | QUE_CAP | Splitter | LHH | 39 | 65.2 | 41.6 | 58.1 | 88.1 | 0.0006 | 5 | 3 |
| 217 | Shears, Tanner | SCH_BOO | Splitter | LHH | 39 | 65.2 | 41.5 | 58.0 | 87.9 | 0.0005 | 6 | 4 |
| 288 | Pindel, Buddie | SCH_BOO | Splitter | LHH | 61 | 63.6 | 41.2 | 56.9 | 83.9 | 0.0003 | 9 | 5 |
| 295 | Soto, Carlos | JOL_SLA | Splitter | LHH | 46 | 61.9 | 44.6 | 56.7 | 83.5 | 0.0025 | 10 | 6 |
| 571 | Williams, Brian | MIS_MUD | Splitter | LHH | 72 | 56.8 | 43.6 | 52.8 | 68.0 | 0.0019 | 12 | 7 |
| 659 | Vitas, Ben | JOL_SLA | Splitter | LHH | 116 | 55.2 | 44.2 | 51.9 | 63.1 | 0.0023 | 13 | 8 |
| 675 | Thornton, Tyler | NEW_ENG23 | Splitter | LHH | 80 | 54.9 | 44.3 | 51.7 | 62.2 | 0.0024 | 15 | 9 |
| 685 | Thompson, Ross | SCH_BOO | Splitter | LHH | 183 | 55.6 | 42.0 | 51.5 | 61.6 | 0.0009 | 16 | 10 |
| 763 | Salata, Derek | SCH_BOO | Splitter | LHH | 92 | 54.3 | 42.6 | 50.8 | 57.3 | 0.0012 | 17 | 11 |
| 1495 | Eldred, Zach | NEW_ENG23 | Splitter | LHH | 51 | 41.6 | 44.9 | 42.6 | 16.2 | 0.0027 | 21 | 12 |
| 1601 | Nakata, Yuto | QUE_CAP | Splitter | LHH | 84 | 42.7 | 35.8 | 40.6 | 10.3 | -0.0031 | 23 | 13 |
| 1657 | Gilleran, Jimmy | NEW_ENG23 | Splitter | LHH | 39 | 38.2 | 41.8 | 39.3 | 7.1 | 0.0008 | 25 | 14 |
| 1714 | Duby, Bill | NEW_JER6 | Splitter | LHH | 60 | 36.5 | 40.2 | 37.6 | 3.9 | -0.0003 | 26 | 15 |
| 1722 | Andueza, Axel | DOW_EAS1 | Splitter | LHH | 83 | 36.4 | 39.4 | 37.3 | 3.5 | -0.0008 | 27 | 16 |

### Splitter vs RHH

| Rank | Pitcher | Team | Pitch Type | Batter Side | Split Pitches | PVS | Loc | Final | Final % | Avg Loc Adv | Type Rank | Type/Side Rank |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 188 | Villers, Ian | QUE_CAP | Splitter | RHH | 25 | 65.2 | 44.6 | 59.0 | 89.5 | 0.0026 | 3 | 1 |
| 191 | Coles, Chad | WAS_WIL3 | Splitter | RHH | 25 | 67.5 | 38.9 | 58.9 | 89.3 | -0.0011 | 4 | 2 |
| 230 | Shears, Tanner | SCH_BOO | Splitter | RHH | 39 | 65.2 | 40.6 | 57.8 | 87.2 | -0.0000 | 7 | 3 |
| 248 | Pindel, Buddie | SCH_BOO | Splitter | RHH | 35 | 63.6 | 43.2 | 57.5 | 86.1 | 0.0016 | 8 | 4 |
| 389 | Soto, Carlos | JOL_SLA | Splitter | RHH | 25 | 61.9 | 39.4 | 55.1 | 78.2 | -0.0008 | 11 | 5 |
| 664 | Williams, Brian | MIS_MUD | Splitter | RHH | 54 | 56.8 | 40.2 | 51.8 | 62.8 | -0.0003 | 14 | 6 |
| 815 | Vitas, Ben | JOL_SLA | Splitter | RHH | 45 | 55.2 | 38.4 | 50.2 | 54.3 | -0.0014 | 18 | 7 |
| 826 | Thornton, Tyler | NEW_ENG23 | Splitter | RHH | 66 | 54.9 | 38.7 | 50.0 | 53.7 | -0.0012 | 19 | 8 |
| 859 | Thompson, Ross | SCH_BOO | Splitter | RHH | 38 | 55.6 | 35.8 | 49.7 | 51.9 | -0.0031 | 20 | 9 |
| 1581 | Eldred, Zach | NEW_ENG23 | Splitter | RHH | 41 | 41.6 | 39.4 | 41.0 | 11.4 | -0.0008 | 22 | 10 |
| 1611 | Nakata, Yuto | QUE_CAP | Splitter | RHH | 32 | 42.7 | 35.1 | 40.4 | 9.7 | -0.0036 | 24 | 11 |
| 1728 | Andueza, Axel | DOW_EAS1 | Splitter | RHH | 61 | 36.4 | 38.5 | 37.0 | 3.1 | -0.0013 | 28 | 12 |

### Sweeper vs LHH

| Rank | Pitcher | Team | Pitch Type | Batter Side | Split Pitches | PVS | Loc | Final | Final % | Avg Loc Adv | Type Rank | Type/Side Rank |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 686 | Petschke, Ben | EVA_OTT | Sweeper | LHH | 40 | 55.8 | 41.5 | 51.5 | 61.6 | 0.0006 | 2 | 1 |

### Sweeper vs RHH

| Rank | Pitcher | Team | Pitch Type | Batter Side | Split Pitches | PVS | Loc | Final | Final % | Avg Loc Adv | Type Rank | Type/Side Rank |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 261 | Cerda, Junior | EVA_OTT | Sweeper | RHH | 41 | 64.2 | 40.9 | 57.3 | 85.4 | 0.0002 | 1 | 1 |
