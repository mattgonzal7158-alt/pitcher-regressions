# Handedness-Specific Pitch Leaderboards

- Pitch Value input: `data\processed\pitch_value_scores_with_type_rank.csv` (853 rows)
- Location Score input: `data\processed\location_scores.csv` (1,758 rows)
- Split component input: `data\processed\2026-data-with-woba-xwoba.parquet`
- Output file: `data\processed\pitch_leaderboard_splits.csv`
- Joined leaderboard rows: 1,527
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
| 1 | Ryan, Dillon | NEW_ENG23 | Slider | RHH | 61 | 79.9 | 69.2 | 76.7 | 100.0 | 0.0157 | 1 | 1 |
| 2 | Kirby, Zach | WAS_WIL3 | Slider | RHH | 126 | 71.7 | 80.0 | 74.2 | 99.9 | 0.0222 | 2 | 2 |
| 3 | Bargo, Casey | NEW_ENG23 | Slider | RHH | 29 | 73.6 | 75.5 | 74.1 | 99.9 | 0.0194 | 3 | 3 |
| 4 | Grounds, Jackson | DOW_EAS1 | Curveball | RHH | 43 | 80.0 | 57.6 | 73.3 | 99.8 | 0.0091 | 1 | 1 |
| 5 | Moore, Kyle | SCH_BOO | Slider | RHH | 31 | 71.2 | 76.5 | 72.8 | 99.7 | 0.0199 | 4 | 4 |
| 6 | Grounds, Jackson | DOW_EAS1 | Four-Seam | RHH | 48 | 74.4 | 68.5 | 72.6 | 99.7 | 0.0153 | 1 | 1 |
| 7 | Vecerka, Boris | QUE_CAP | Slider | RHH | 53 | 77.6 | 60.8 | 72.5 | 99.6 | 0.0109 | 5 | 5 |
| 8 | Lawson, Nathan | FLO_Y'A | Changeup | LHH | 40 | 78.2 | 59.1 | 72.5 | 99.5 | 0.0100 | 1 | 1 |
| 9 | Alpern, Liam | FLO_Y'A | Slider | LHH | 38 | 76.4 | 61.5 | 72.0 | 99.5 | 0.0114 | 6 | 1 |
| 10 | Zentko, Dylan | EVA_OTT | Changeup | RHH | 57 | 78.6 | 56.1 | 71.8 | 99.4 | 0.0082 | 2 | 1 |
| 11 | Hickey, Matt | GAT_GRI | Slider | RHH | 71 | 73.5 | 67.5 | 71.7 | 99.3 | 0.0148 | 7 | 6 |
| 12 | Harper, Scott | NEW_YOR13 | Slider | RHH | 166 | 72.6 | 69.1 | 71.5 | 99.3 | 0.0157 | 8 | 7 |
| 13 | Leduc, Zachary | TRO_AIG | Slider | RHH | 46 | 79.2 | 53.6 | 71.5 | 99.2 | 0.0068 | 9 | 8 |
| 14 | Davis, Tyler | WIN_CIT29 | Four-Seam | RHH | 33 | 74.4 | 64.7 | 71.5 | 99.1 | 0.0131 | 2 | 2 |
| 15 | Ryan, Dillon | NEW_ENG23 | Slider | LHH | 64 | 79.9 | 51.3 | 71.3 | 99.1 | 0.0055 | 10 | 2 |
| 16 | Morgan, Cooper | QUE_CAP | Curveball | LHH | 56 | 80.0 | 50.8 | 71.2 | 99.0 | 0.0052 | 2 | 1 |
| 17 | Leduc, Zachary | TRO_AIG | Slider | LHH | 32 | 79.2 | 52.0 | 71.0 | 99.0 | 0.0059 | 11 | 3 |
| 18 | Peyton, Blake | GAT_GRI | Changeup | RHH | 90 | 77.3 | 55.5 | 70.8 | 98.9 | 0.0079 | 3 | 2 |
| 19 | Escobar, Anthony | TRO_AIG | Changeup | LHH | 142 | 72.7 | 65.0 | 70.4 | 98.8 | 0.0133 | 4 | 2 |
| 20 | Carroll, Jake | JOL_SLA | Slider | LHH | 50 | 80.0 | 47.8 | 70.3 | 98.8 | 0.0035 | 12 | 4 |
| 21 | Nakata, Yuto | QUE_CAP | Slider | RHH | 89 | 70.5 | 68.3 | 69.8 | 98.7 | 0.0152 | 13 | 9 |
| 22 | Grounds, Jackson | DOW_EAS1 | Curveball | LHH | 39 | 80.0 | 45.2 | 69.6 | 98.6 | 0.0020 | 3 | 2 |
| 23 | Serrano, Elio | NEW_JER6 | Changeup | LHH | 56 | 75.9 | 54.2 | 69.4 | 98.6 | 0.0072 | 5 | 3 |
| 24 | Grounds, Jackson | DOW_EAS1 | Four-Seam | LHH | 59 | 74.4 | 56.2 | 68.9 | 98.5 | 0.0083 | 3 | 1 |
| 25 | Cameron, Zach | WIN_CIT29 | Four-Seam | RHH | 63 | 71.7 | 62.4 | 68.9 | 98.4 | 0.0119 | 4 | 3 |
| 26 | Debban, Caleb | NEW_JER6 | Four-Seam | RHH | 37 | 73.8 | 56.1 | 68.5 | 98.4 | 0.0082 | 5 | 4 |
| 27 | Donnan, Blake | FLO_Y'A | Slider | RHH | 52 | 70.1 | 63.8 | 68.2 | 98.3 | 0.0126 | 14 | 10 |
| 28 | McEvoy, Aidan | FLO_Y'A | Slider | LHH | 69 | 70.5 | 62.0 | 67.9 | 98.2 | 0.0116 | 15 | 5 |
| 29 | Jones, Logan | TRI_VAL | Slider | LHH | 33 | 74.7 | 51.2 | 67.7 | 98.2 | 0.0054 | 16 | 6 |
| 30 | Vega, Lucas | TRO_AIG | Slider | RHH | 94 | 66.7 | 68.1 | 67.1 | 98.1 | 0.0151 | 17 | 11 |
| 31 | Barraza, Chris | MIS_MUD | Slider | RHH | 34 | 63.4 | 75.8 | 67.1 | 98.0 | 0.0196 | 18 | 12 |
| 32 | Rodriguez, Joe Joe | NEW_JER6 | Changeup | LHH | 92 | 70.6 | 58.1 | 66.8 | 98.0 | 0.0094 | 6 | 4 |
| 33 | O'Hanlon, Michael | WAS_WIL3 | Slider | RHH | 51 | 61.9 | 78.2 | 66.8 | 97.9 | 0.0209 | 19 | 13 |
| 34 | Smith, Ben | NEW_ENG23 | Changeup | RHH | 43 | 67.6 | 64.6 | 66.7 | 97.8 | 0.0131 | 7 | 3 |
| 35 | Harper, Scott | NEW_YOR13 | Slider | LHH | 46 | 72.6 | 52.0 | 66.4 | 97.8 | 0.0059 | 20 | 7 |
| 36 | Davis, Tyler | WIN_CIT29 | Four-Seam | LHH | 43 | 74.4 | 47.4 | 66.3 | 97.7 | 0.0032 | 6 | 2 |
| 37 | Glickstein, Aaron | SCH_BOO | Sinker | RHH | 72 | 68.3 | 61.3 | 66.2 | 97.6 | 0.0112 | 1 | 1 |
| 38 | Lockhart, Gauge | LAK_ERI24 | Cutter | RHH | 59 | 72.5 | 51.2 | 66.1 | 97.6 | 0.0054 | 1 | 1 |
| 39 | Perozzi, John | SUS_COU1 | Slider | RHH | 63 | 64.1 | 70.1 | 65.9 | 97.5 | 0.0162 | 21 | 14 |
| 40 | Jones, Logan | FLO_Y'A | Slider | RHH | 33 | 68.5 | 59.1 | 65.7 | 97.4 | 0.0099 | 22 | 15 |

## Pitch Type + Batter Side Leaderboards

### Changeup vs LHH

| Rank | Pitcher | Team | Pitch Type | Batter Side | Split Pitches | PVS | Loc | Final | Final % | Avg Loc Adv | Type Rank | Type/Side Rank |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 8 | Lawson, Nathan | FLO_Y'A | Changeup | LHH | 40 | 78.2 | 59.1 | 72.5 | 99.5 | 0.0100 | 1 | 1 |
| 19 | Escobar, Anthony | TRO_AIG | Changeup | LHH | 142 | 72.7 | 65.0 | 70.4 | 98.8 | 0.0133 | 4 | 2 |
| 23 | Serrano, Elio | NEW_JER6 | Changeup | LHH | 56 | 75.9 | 54.2 | 69.4 | 98.6 | 0.0072 | 5 | 3 |
| 32 | Rodriguez, Joe Joe | NEW_JER6 | Changeup | LHH | 92 | 70.6 | 58.1 | 66.8 | 98.0 | 0.0094 | 6 | 4 |
| 56 | Harris, Everette | TRI_VAL | Changeup | LHH | 56 | 69.7 | 50.0 | 63.8 | 96.4 | 0.0047 | 9 | 5 |
| 61 | Parsons, Billy | SUS_COU1 | Changeup | LHH | 43 | 68.5 | 51.8 | 63.5 | 96.1 | 0.0058 | 10 | 6 |
| 67 | Maietta, Dante | WIN_CIT29 | Changeup | LHH | 150 | 63.3 | 63.7 | 63.4 | 95.7 | 0.0126 | 11 | 7 |
| 87 | Sesar, Jorden | SUS_COU1 | Changeup | LHH | 57 | 64.3 | 57.5 | 62.3 | 94.4 | 0.0090 | 13 | 8 |
| 90 | Leak, Anthony | NEW_YOR13 | Changeup | LHH | 63 | 64.0 | 57.9 | 62.1 | 94.2 | 0.0092 | 14 | 9 |
| 107 | Drakeford, Dosie | NEW_JER6 | Changeup | LHH | 66 | 64.7 | 53.3 | 61.3 | 93.1 | 0.0066 | 16 | 10 |
| 121 | Hocom, Quinn | TRI_VAL | Changeup | LHH | 74 | 59.4 | 63.2 | 60.6 | 92.1 | 0.0123 | 18 | 11 |
| 122 | Willeman, Landon | EVA_OTT | Changeup | LHH | 127 | 61.2 | 59.1 | 60.5 | 92.1 | 0.0099 | 19 | 12 |
| 139 | Dill, Austin | TRI_VAL | Changeup | LHH | 118 | 56.4 | 68.0 | 59.9 | 91.0 | 0.0151 | 20 | 13 |
| 157 | Wiltse, Ryan | EVA_OTT | Changeup | LHH | 99 | 65.8 | 45.1 | 59.6 | 89.8 | 0.0019 | 21 | 14 |
| 168 | Tokar, Heitor | OTT_TIT | Changeup | LHH | 38 | 64.6 | 46.7 | 59.2 | 89.1 | 0.0028 | 22 | 15 |
| 186 | Plumadore, Carson | WIN_CIT29 | Changeup | LHH | 192 | 60.5 | 55.0 | 58.9 | 87.9 | 0.0076 | 23 | 16 |
| 209 | Hensey, Rob | SUS_COU1 | Changeup | LHH | 55 | 60.5 | 52.7 | 58.2 | 86.4 | 0.0063 | 27 | 17 |
| 217 | Pardinho, Eric | OTT_TIT | Changeup | LHH | 102 | 57.5 | 58.9 | 57.9 | 85.9 | 0.0098 | 29 | 18 |
| 237 | Gartland, Chad | TRI_VAL | Changeup | LHH | 44 | 59.2 | 53.1 | 57.4 | 84.5 | 0.0065 | 31 | 19 |
| 266 | Miner, Jace | DOW_EAS1 | Changeup | LHH | 67 | 63.3 | 41.7 | 56.8 | 82.6 | -0.0000 | 33 | 20 |
| 273 | Cameron, Zach | WIN_CIT29 | Changeup | LHH | 135 | 54.9 | 61.0 | 56.7 | 82.2 | 0.0111 | 34 | 21 |
| 290 | Burcham, Jacob | GAT_GRI | Changeup | LHH | 62 | 54.4 | 60.6 | 56.3 | 81.1 | 0.0108 | 36 | 22 |
| 299 | Andueza, Axel | DOW_EAS1 | Changeup | LHH | 86 | 58.0 | 51.2 | 56.0 | 80.5 | 0.0054 | 37 | 23 |
| 308 | Daly, Ryan | JOL_SLA | Changeup | LHH | 162 | 54.4 | 59.1 | 55.8 | 79.9 | 0.0099 | 39 | 24 |
| 319 | Vega, Lucas | TRO_AIG | Changeup | LHH | 65 | 54.5 | 58.5 | 55.7 | 79.2 | 0.0096 | 41 | 25 |

### Changeup vs RHH

| Rank | Pitcher | Team | Pitch Type | Batter Side | Split Pitches | PVS | Loc | Final | Final % | Avg Loc Adv | Type Rank | Type/Side Rank |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 10 | Zentko, Dylan | EVA_OTT | Changeup | RHH | 57 | 78.6 | 56.1 | 71.8 | 99.4 | 0.0082 | 2 | 1 |
| 18 | Peyton, Blake | GAT_GRI | Changeup | RHH | 90 | 77.3 | 55.5 | 70.8 | 98.9 | 0.0079 | 3 | 2 |
| 34 | Smith, Ben | NEW_ENG23 | Changeup | RHH | 43 | 67.6 | 64.6 | 66.7 | 97.8 | 0.0131 | 7 | 3 |
| 50 | Rodriguez, Joe Joe | NEW_JER6 | Changeup | RHH | 33 | 70.6 | 50.0 | 64.4 | 96.8 | 0.0047 | 8 | 4 |
| 85 | Harris, Everette | TRI_VAL | Changeup | RHH | 40 | 69.7 | 45.3 | 62.4 | 94.5 | 0.0020 | 12 | 5 |
| 101 | Wiltse, Ryan | EVA_OTT | Changeup | RHH | 51 | 65.8 | 51.5 | 61.5 | 93.5 | 0.0056 | 15 | 6 |
| 114 | Messina, Chris | FDU_KNI | Changeup | RHH | 52 | 66.5 | 48.1 | 60.9 | 92.6 | 0.0036 | 17 | 7 |
| 187 | Campbell, Tyler | MIS_MUD | Changeup | RHH | 72 | 60.9 | 54.0 | 58.8 | 87.8 | 0.0070 | 24 | 8 |
| 205 | Miner, Jace | DOW_EAS1 | Changeup | RHH | 89 | 63.3 | 46.8 | 58.3 | 86.6 | 0.0029 | 25 | 9 |
| 207 | Maietta, Dante | WIN_CIT29 | Changeup | RHH | 109 | 63.3 | 46.5 | 58.3 | 86.5 | 0.0027 | 26 | 10 |
| 215 | Hocom, Quinn | TRI_VAL | Changeup | RHH | 27 | 59.4 | 54.7 | 58.0 | 86.0 | 0.0074 | 28 | 11 |
| 222 | Rohde, Isaac | NEW_YOR13 | Changeup | RHH | 551 | 58.4 | 55.9 | 57.6 | 85.5 | 0.0081 | 30 | 12 |
| 242 | Morgan, Cooper | QUE_CAP | Changeup | RHH | 59 | 65.6 | 37.6 | 57.2 | 84.2 | -0.0024 | 32 | 13 |
| 275 | VanMarter, Luke | LEM_COL | Changeup | RHH | 29 | 59.2 | 50.9 | 56.7 | 82.1 | 0.0052 | 35 | 14 |
| 300 | Brothers, Kellen | SUS_COU1 | Changeup | RHH | 47 | 58.8 | 49.2 | 55.9 | 80.4 | 0.0043 | 38 | 15 |
| 317 | Tokar, Heitor | OTT_TIT | Changeup | RHH | 32 | 64.6 | 35.0 | 55.7 | 79.3 | -0.0039 | 40 | 16 |
| 323 | Willeman, Landon | EVA_OTT | Changeup | RHH | 52 | 61.2 | 42.8 | 55.6 | 78.9 | 0.0006 | 42 | 17 |
| 343 | Hensey, Rob | SUS_COU1 | Changeup | RHH | 222 | 60.5 | 42.5 | 55.1 | 77.6 | 0.0004 | 45 | 18 |
| 347 | Plumadore, Carson | WIN_CIT29 | Changeup | RHH | 77 | 60.5 | 42.2 | 55.0 | 77.3 | 0.0002 | 46 | 19 |
| 357 | Gollert, Harley | TRO_AIG | Changeup | RHH | 117 | 53.8 | 57.2 | 54.8 | 76.7 | 0.0088 | 48 | 20 |
| 364 | Barreto, Brayhans | TRI_VAL | Changeup | RHH | 87 | 58.7 | 45.7 | 54.8 | 76.2 | 0.0023 | 50 | 21 |
| 421 | Boies, Emiles | QUE_CAP | Changeup | RHH | 60 | 57.4 | 45.3 | 53.8 | 72.5 | 0.0020 | 57 | 22 |
| 424 | Cooper, Garrett | NEW_YOR13 | Changeup | RHH | 112 | 55.0 | 50.8 | 53.7 | 72.3 | 0.0052 | 58 | 23 |
| 427 | Turner, Eric | JOL_SLA | Changeup | RHH | 40 | 53.9 | 53.3 | 53.7 | 72.1 | 0.0066 | 59 | 24 |
| 463 | McKillican, Adam | QUE_CAP | Changeup | RHH | 33 | 54.9 | 49.5 | 53.3 | 69.7 | 0.0044 | 64 | 25 |

### Curveball vs LHH

| Rank | Pitcher | Team | Pitch Type | Batter Side | Split Pitches | PVS | Loc | Final | Final % | Avg Loc Adv | Type Rank | Type/Side Rank |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 16 | Morgan, Cooper | QUE_CAP | Curveball | LHH | 56 | 80.0 | 50.8 | 71.2 | 99.0 | 0.0052 | 2 | 1 |
| 22 | Grounds, Jackson | DOW_EAS1 | Curveball | LHH | 39 | 80.0 | 45.2 | 69.6 | 98.6 | 0.0020 | 3 | 2 |
| 51 | Bohnert, Matthew | WIN_CIT29 | Curveball | LHH | 46 | 71.9 | 46.7 | 64.3 | 96.7 | 0.0028 | 4 | 3 |
| 138 | Salata, Derek | SCH_BOO | Curveball | LHH | 50 | 66.5 | 44.8 | 60.0 | 91.0 | 0.0017 | 19 | 4 |
| 141 | Garcia, Brett | OTT_TIT | Curveball | LHH | 48 | 67.4 | 42.4 | 59.9 | 90.8 | 0.0003 | 20 | 5 |
| 156 | Binns, Malik | NEW_JER6 | Curveball | LHH | 27 | 66.3 | 43.9 | 59.6 | 89.8 | 0.0012 | 24 | 6 |
| 161 | Eisenbarger, Jack | QUE_CAP | Curveball | LHH | 66 | 64.8 | 47.0 | 59.5 | 89.5 | 0.0030 | 25 | 7 |
| 191 | Hohenstein, Liam | WIN_CIT29 | Curveball | LHH | 45 | 65.2 | 43.6 | 58.7 | 87.6 | 0.0011 | 27 | 8 |
| 192 | Hill, Kaleb | OTT_TIT | Curveball | LHH | 111 | 66.1 | 41.5 | 58.7 | 87.5 | -0.0002 | 28 | 9 |
| 197 | Heredia-Bustos, Rolando | DOW_EAS1 | Curveball | LHH | 35 | 66.3 | 40.5 | 58.6 | 87.2 | -0.0007 | 29 | 10 |
| 208 | Townes, Holland | SCH_BOO | Curveball | LHH | 26 | 68.7 | 33.7 | 58.2 | 86.4 | -0.0047 | 31 | 11 |
| 228 | Cook, Cole | SCH_BOO | Curveball | LHH | 49 | 63.8 | 42.9 | 57.5 | 85.1 | 0.0006 | 34 | 12 |
| 245 | Hickey, Matt | GAT_GRI | Curveball | LHH | 26 | 65.5 | 37.9 | 57.2 | 84.0 | -0.0022 | 36 | 13 |
| 255 | Boies, Emiles | QUE_CAP | Curveball | LHH | 28 | 63.5 | 41.7 | 57.0 | 83.4 | -0.0000 | 39 | 14 |
| 278 | Maryniak, Connor | NEW_JER6 | Curveball | LHH | 97 | 61.1 | 45.7 | 56.5 | 81.9 | 0.0023 | 41 | 15 |
| 292 | Wiltse, Ryan | EVA_OTT | Curveball | LHH | 91 | 61.6 | 43.7 | 56.2 | 80.9 | 0.0011 | 42 | 16 |
| 303 | Harris, Ben | GAT_GRI | Curveball | LHH | 86 | 61.8 | 42.0 | 55.9 | 80.2 | 0.0002 | 44 | 17 |
| 324 | Gollert, Harley | TRO_AIG | Curveball | LHH | 28 | 58.1 | 49.9 | 55.6 | 78.8 | 0.0047 | 48 | 18 |
| 338 | Sechrist, Zander | WAS_WIL3 | Curveball | LHH | 38 | 59.1 | 46.2 | 55.2 | 77.9 | 0.0025 | 49 | 19 |
| 353 | Langrell, Connor | MIS_MUD | Curveball | LHH | 55 | 56.4 | 51.7 | 55.0 | 76.9 | 0.0057 | 50 | 20 |
| 409 | Earwood, Micah | SUS_COU1 | Curveball | LHH | 55 | 56.4 | 48.4 | 54.0 | 73.3 | 0.0038 | 54 | 21 |
| 423 | Peters, Garrett | NEW_YOR13 | Curveball | LHH | 121 | 56.0 | 48.5 | 53.7 | 72.4 | 0.0038 | 55 | 22 |
| 433 | Hocom, Quinn | TRI_VAL | Curveball | LHH | 41 | 55.5 | 49.2 | 53.6 | 71.7 | 0.0043 | 58 | 23 |
| 458 | Carroll, Jake | JOL_SLA | Curveball | LHH | 35 | 50.4 | 60.1 | 53.3 | 70.1 | 0.0105 | 59 | 24 |
| 475 | Lefebvre, Charles | TRO_AIG | Curveball | LHH | 47 | 58.7 | 39.9 | 53.1 | 69.0 | -0.0011 | 61 | 25 |

### Curveball vs RHH

| Rank | Pitcher | Team | Pitch Type | Batter Side | Split Pitches | PVS | Loc | Final | Final % | Avg Loc Adv | Type Rank | Type/Side Rank |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 4 | Grounds, Jackson | DOW_EAS1 | Curveball | RHH | 43 | 80.0 | 57.6 | 73.3 | 99.8 | 0.0091 | 1 | 1 |
| 63 | Garcia, Brett | OTT_TIT | Curveball | RHH | 67 | 67.4 | 54.4 | 63.5 | 95.9 | 0.0073 | 5 | 2 |
| 65 | Hohenstein, Liam | WIN_CIT29 | Curveball | RHH | 58 | 65.2 | 59.3 | 63.4 | 95.8 | 0.0100 | 6 | 3 |
| 68 | Heredia-Bustos, Rolando | DOW_EAS1 | Curveball | RHH | 40 | 66.3 | 56.3 | 63.3 | 95.6 | 0.0083 | 7 | 4 |
| 69 | Townes, Holland | SCH_BOO | Curveball | RHH | 56 | 68.7 | 50.7 | 63.3 | 95.5 | 0.0051 | 8 | 5 |
| 72 | Jones, Breyln | NEW_JER6 | Curveball | RHH | 33 | 68.0 | 52.2 | 63.2 | 95.4 | 0.0060 | 9 | 6 |
| 74 | Bohnert, Matthew | WIN_CIT29 | Curveball | RHH | 51 | 71.9 | 42.2 | 63.0 | 95.2 | 0.0003 | 10 | 7 |
| 81 | Binns, Malik | NEW_JER6 | Curveball | RHH | 28 | 66.3 | 54.2 | 62.7 | 94.8 | 0.0071 | 11 | 8 |
| 88 | Salata, Derek | SCH_BOO | Curveball | RHH | 72 | 66.5 | 52.2 | 62.2 | 94.3 | 0.0060 | 12 | 9 |
| 92 | Gregory, Ben | GAT_GRI | Curveball | RHH | 29 | 66.7 | 51.3 | 62.0 | 94.0 | 0.0055 | 13 | 10 |
| 97 | Majick, Eli | NEW_ENG23 | Curveball | RHH | 34 | 63.1 | 58.4 | 61.7 | 93.7 | 0.0095 | 14 | 11 |
| 112 | Hickey, Matt | GAT_GRI | Curveball | RHH | 36 | 65.5 | 50.4 | 60.9 | 92.7 | 0.0049 | 15 | 12 |
| 124 | Wiltse, Ryan | EVA_OTT | Curveball | RHH | 40 | 61.6 | 57.8 | 60.4 | 91.9 | 0.0092 | 16 | 13 |
| 125 | Hill, Kaleb | OTT_TIT | Curveball | RHH | 111 | 66.1 | 47.2 | 60.4 | 91.9 | 0.0031 | 17 | 14 |
| 132 | Maryniak, Connor | NEW_JER6 | Curveball | RHH | 83 | 61.1 | 58.0 | 60.2 | 91.4 | 0.0093 | 18 | 15 |
| 142 | Boies, Emiles | QUE_CAP | Curveball | RHH | 52 | 63.5 | 51.3 | 59.8 | 90.8 | 0.0055 | 21 | 16 |
| 144 | Hampton, Ky | OTT_TIT | Curveball | RHH | 39 | 61.3 | 56.4 | 59.8 | 90.6 | 0.0084 | 22 | 17 |
| 147 | Simpson, Garret | EVA_OTT | Curveball | RHH | 55 | 56.6 | 67.1 | 59.8 | 90.4 | 0.0146 | 23 | 18 |
| 178 | Harris, Ben | GAT_GRI | Curveball | RHH | 156 | 61.8 | 52.3 | 59.0 | 88.4 | 0.0061 | 26 | 19 |
| 198 | Lefebvre, Charles | TRO_AIG | Curveball | RHH | 52 | 58.7 | 58.1 | 58.6 | 87.1 | 0.0094 | 30 | 20 |
| 218 | Eisenbarger, Jack | QUE_CAP | Curveball | RHH | 27 | 64.8 | 41.6 | 57.8 | 85.8 | -0.0001 | 32 | 21 |
| 220 | Cook, Cole | SCH_BOO | Curveball | RHH | 65 | 63.8 | 43.6 | 57.7 | 85.7 | 0.0010 | 33 | 22 |
| 244 | Sechrist, Zander | WAS_WIL3 | Curveball | RHH | 54 | 59.1 | 52.7 | 57.2 | 84.1 | 0.0063 | 35 | 23 |
| 248 | Langrell, Connor | MIS_MUD | Curveball | RHH | 59 | 56.4 | 58.8 | 57.1 | 83.8 | 0.0098 | 37 | 24 |
| 254 | Scafidi, Christian | LAK_ERI24 | Curveball | RHH | 35 | 61.3 | 47.0 | 57.0 | 83.4 | 0.0030 | 38 | 25 |

### Cutter vs LHH

| Rank | Pitcher | Team | Pitch Type | Batter Side | Split Pitches | PVS | Loc | Final | Final % | Avg Loc Adv | Type Rank | Type/Side Rank |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 75 | Webster, Evan | FLO_Y'A | Cutter | LHH | 95 | 71.1 | 43.8 | 62.9 | 95.2 | 0.0012 | 2 | 1 |
| 79 | Lockhart, Gauge | LAK_ERI24 | Cutter | LHH | 36 | 72.5 | 40.1 | 62.8 | 94.9 | -0.0010 | 3 | 2 |
| 137 | Correa, Nelvin | QUE_CAP | Cutter | LHH | 59 | 67.6 | 42.2 | 60.0 | 91.1 | 0.0002 | 6 | 3 |
| 154 | Majick, Eli | NEW_ENG23 | Cutter | LHH | 26 | 64.6 | 48.1 | 59.6 | 90.0 | 0.0036 | 8 | 4 |
| 189 | Parsons, Billy | SUS_COU1 | Cutter | LHH | 39 | 64.6 | 45.1 | 58.8 | 87.7 | 0.0019 | 9 | 5 |
| 331 | Morgan, Marcus | JOL_SLA | Cutter | LHH | 40 | 61.1 | 42.3 | 55.5 | 78.4 | 0.0003 | 12 | 6 |
| 365 | Bell, Brendan | NEW_ENG23 | Cutter | LHH | 46 | 59.9 | 42.8 | 54.8 | 76.2 | 0.0006 | 13 | 7 |
| 408 | McEvoy, Aidan | FLO_Y'A | Cutter | LHH | 36 | 56.3 | 48.8 | 54.0 | 73.3 | 0.0041 | 14 | 8 |
| 474 | Moore, Kyle | SCH_BOO | Cutter | LHH | 35 | 56.9 | 44.3 | 53.1 | 69.0 | 0.0015 | 17 | 9 |
| 531 | Debban, Caleb | NEW_JER6 | Cutter | LHH | 60 | 56.6 | 42.2 | 52.3 | 65.3 | 0.0003 | 18 | 10 |
| 546 | Saturria, Michael | NEW_ENG23 | Cutter | LHH | 117 | 58.0 | 38.6 | 52.1 | 64.3 | -0.0018 | 19 | 11 |
| 641 | Valdez, Alex | EVA_OTT | Cutter | LHH | 26 | 56.3 | 38.0 | 50.8 | 58.1 | -0.0022 | 24 | 12 |
| 667 | Gorgen, Grady | NEW_YOR13 | Cutter | LHH | 37 | 55.2 | 39.8 | 50.6 | 56.4 | -0.0012 | 26 | 13 |
| 689 | Smith, Jackson | MIS_MUD | Cutter | LHH | 42 | 53.3 | 43.3 | 50.3 | 54.9 | 0.0009 | 28 | 14 |
| 719 | MacMillan, Blake | TRO_AIG | Cutter | LHH | 61 | 54.1 | 40.3 | 50.0 | 53.0 | -0.0008 | 29 | 15 |
| 828 | Campbell, Tyler | MIS_MUD | Cutter | LHH | 56 | 50.1 | 44.5 | 48.4 | 45.8 | 0.0015 | 31 | 16 |
| 895 | Langrell, Connor | MIS_MUD | Cutter | LHH | 111 | 49.4 | 43.4 | 47.6 | 41.5 | 0.0009 | 36 | 17 |
| 926 | Binns, Malik | NEW_JER6 | Cutter | LHH | 34 | 49.3 | 42.4 | 47.2 | 39.4 | 0.0004 | 38 | 18 |
| 955 | Morgan, Cooper | QUE_CAP | Cutter | LHH | 52 | 50.8 | 37.9 | 46.9 | 37.5 | -0.0022 | 40 | 19 |
| 1002 | Gamelin, Shaun | JOL_SLA | Cutter | LHH | 56 | 48.8 | 41.0 | 46.4 | 34.4 | -0.0005 | 43 | 20 |
| 1046 | Petschke, Ben | EVA_OTT | Cutter | LHH | 150 | 45.5 | 46.8 | 45.9 | 31.6 | 0.0029 | 44 | 21 |
| 1060 | Catrambone, Ben | JOL_SLA | Cutter | LHH | 25 | 45.9 | 45.5 | 45.8 | 30.6 | 0.0021 | 45 | 22 |
| 1062 | Parks, Pavin | LAK_ERI24 | Cutter | LHH | 40 | 48.3 | 39.8 | 45.7 | 30.5 | -0.0012 | 46 | 23 |
| 1073 | Campbell, AJ | WIN_CIT29 | Cutter | LHH | 31 | 46.4 | 43.6 | 45.6 | 29.8 | 0.0011 | 47 | 24 |
| 1175 | Cook, Cole | SCH_BOO | Cutter | LHH | 33 | 43.0 | 47.9 | 44.5 | 23.1 | 0.0035 | 52 | 25 |

### Cutter vs RHH

| Rank | Pitcher | Team | Pitch Type | Batter Side | Split Pitches | PVS | Loc | Final | Final % | Avg Loc Adv | Type Rank | Type/Side Rank |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 38 | Lockhart, Gauge | LAK_ERI24 | Cutter | RHH | 59 | 72.5 | 51.2 | 66.1 | 97.6 | 0.0054 | 1 | 1 |
| 105 | Correa, Nelvin | QUE_CAP | Cutter | RHH | 51 | 67.6 | 46.7 | 61.3 | 93.2 | 0.0028 | 4 | 2 |
| 116 | Webster, Evan | FLO_Y'A | Cutter | RHH | 38 | 71.1 | 36.9 | 60.8 | 92.5 | -0.0028 | 5 | 3 |
| 152 | Majick, Eli | NEW_ENG23 | Cutter | RHH | 42 | 64.6 | 48.4 | 59.7 | 90.1 | 0.0038 | 7 | 4 |
| 200 | Bell, Brendan | NEW_ENG23 | Cutter | RHH | 39 | 59.9 | 55.2 | 58.5 | 87.0 | 0.0077 | 10 | 5 |
| 251 | Good, Ty | GAT_GRI | Cutter | RHH | 40 | 58.6 | 53.5 | 57.1 | 83.6 | 0.0067 | 11 | 6 |
| 431 | Saturria, Michael | NEW_ENG23 | Cutter | RHH | 128 | 58.0 | 43.6 | 53.6 | 71.8 | 0.0010 | 15 | 7 |
| 460 | Valdez, Alex | EVA_OTT | Cutter | RHH | 52 | 56.3 | 46.2 | 53.3 | 69.9 | 0.0026 | 16 | 8 |
| 555 | Debban, Caleb | NEW_JER6 | Cutter | RHH | 81 | 56.6 | 41.1 | 52.0 | 63.7 | -0.0004 | 20 | 9 |
| 607 | Gorgen, Grady | NEW_YOR13 | Cutter | RHH | 37 | 55.2 | 42.0 | 51.2 | 60.3 | 0.0002 | 21 | 10 |
| 611 | Moore, Kyle | SCH_BOO | Cutter | RHH | 93 | 56.9 | 38.0 | 51.2 | 60.1 | -0.0021 | 22 | 11 |
| 613 | McEvoy, Aidan | FLO_Y'A | Cutter | RHH | 44 | 56.3 | 39.4 | 51.2 | 59.9 | -0.0014 | 23 | 12 |
| 644 | Smith, Jackson | MIS_MUD | Cutter | RHH | 55 | 53.3 | 45.0 | 50.8 | 57.9 | 0.0018 | 25 | 13 |
| 685 | Flontek, Zac | DOW_EAS1 | Cutter | RHH | 30 | 55.8 | 37.7 | 50.4 | 55.2 | -0.0023 | 27 | 14 |
| 817 | MacMillan, Blake | TRO_AIG | Cutter | RHH | 83 | 54.1 | 35.6 | 48.6 | 46.6 | -0.0035 | 30 | 15 |
| 831 | Binns, Malik | NEW_JER6 | Cutter | RHH | 54 | 49.3 | 46.2 | 48.4 | 45.6 | 0.0026 | 32 | 16 |
| 861 | Parks, Pavin | LAK_ERI24 | Cutter | RHH | 94 | 48.3 | 47.5 | 48.1 | 43.7 | 0.0033 | 33 | 17 |
| 867 | Ginn, Landon | WAS_WIL3 | Cutter | RHH | 61 | 45.9 | 52.9 | 48.0 | 43.3 | 0.0064 | 34 | 18 |
| 882 | Morgan, Cooper | QUE_CAP | Cutter | RHH | 45 | 50.8 | 40.9 | 47.8 | 42.3 | -0.0005 | 35 | 19 |
| 924 | Langrell, Connor | MIS_MUD | Cutter | RHH | 151 | 49.4 | 42.2 | 47.3 | 39.6 | 0.0002 | 37 | 20 |
| 939 | Gamelin, Shaun | JOL_SLA | Cutter | RHH | 81 | 48.8 | 43.5 | 47.2 | 38.6 | 0.0010 | 39 | 21 |
| 983 | Wiltse, Ryan | EVA_OTT | Cutter | RHH | 47 | 44.8 | 50.9 | 46.6 | 35.7 | 0.0052 | 41 | 22 |
| 1000 | Campbell, Tyler | MIS_MUD | Cutter | RHH | 76 | 50.1 | 37.8 | 46.4 | 34.6 | -0.0023 | 42 | 23 |
| 1076 | Catrambone, Ben | JOL_SLA | Cutter | RHH | 36 | 45.9 | 44.8 | 45.6 | 29.6 | 0.0017 | 48 | 24 |
| 1104 | Jones, Breyln | NEW_JER6 | Cutter | RHH | 44 | 41.0 | 55.3 | 45.3 | 27.8 | 0.0078 | 49 | 25 |

### Four-Seam vs LHH

| Rank | Pitcher | Team | Pitch Type | Batter Side | Split Pitches | PVS | Loc | Final | Final % | Avg Loc Adv | Type Rank | Type/Side Rank |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 24 | Grounds, Jackson | DOW_EAS1 | Four-Seam | LHH | 59 | 74.4 | 56.2 | 68.9 | 98.5 | 0.0083 | 3 | 1 |
| 36 | Davis, Tyler | WIN_CIT29 | Four-Seam | LHH | 43 | 74.4 | 47.4 | 66.3 | 97.7 | 0.0032 | 6 | 2 |
| 58 | Wehrle, Tyler | WIN_CIT29 | Four-Seam | LHH | 80 | 59.8 | 72.5 | 63.6 | 96.3 | 0.0177 | 9 | 3 |
| 83 | Cameron, Zach | WIN_CIT29 | Four-Seam | LHH | 52 | 71.7 | 40.8 | 62.4 | 94.6 | -0.0006 | 11 | 4 |
| 110 | Grounds, Jackson | TRO_AIG | Four-Seam | LHH | 27 | 67.9 | 44.9 | 61.0 | 92.9 | 0.0018 | 15 | 5 |
| 123 | Foster, Kobe | WAS_WIL3 | Four-Seam | LHH | 180 | 58.7 | 64.5 | 60.5 | 92.0 | 0.0131 | 16 | 6 |
| 143 | Zaffiro, Cole | SCH_BOO | Four-Seam | LHH | 130 | 60.1 | 59.2 | 59.8 | 90.7 | 0.0100 | 20 | 7 |
| 148 | Cartwright, Eli | GAT_GRI | Four-Seam | LHH | 61 | 61.5 | 55.8 | 59.8 | 90.4 | 0.0080 | 22 | 8 |
| 150 | Herbert, Andrew | WAS_WIL3 | Four-Seam | LHH | 35 | 57.5 | 65.1 | 59.8 | 90.2 | 0.0134 | 23 | 9 |
| 163 | Morgan, Cooper | QUE_CAP | Four-Seam | LHH | 34 | 61.9 | 53.5 | 59.4 | 89.4 | 0.0067 | 26 | 10 |
| 165 | Mercado, Nelson | OTT_TIT | Four-Seam | LHH | 39 | 60.8 | 55.9 | 59.3 | 89.3 | 0.0081 | 27 | 11 |
| 179 | Foy, Corbin | LAK_ERI24 | Four-Seam | LHH | 48 | 65.8 | 43.1 | 59.0 | 88.3 | 0.0008 | 31 | 12 |
| 194 | Anderson, Colt | WAS_WIL3 | Four-Seam | LHH | 112 | 61.0 | 53.3 | 58.7 | 87.4 | 0.0066 | 32 | 13 |
| 202 | Brown, Ethan | WAS_WIL3 | Four-Seam | LHH | 25 | 62.2 | 49.6 | 58.4 | 86.8 | 0.0045 | 35 | 14 |
| 204 | Shears, Tanner | SCH_BOO | Four-Seam | LHH | 93 | 60.6 | 53.3 | 58.4 | 86.7 | 0.0066 | 36 | 15 |
| 206 | Correa, Nelvin | QUE_CAP | Four-Seam | LHH | 41 | 67.2 | 37.6 | 58.3 | 86.6 | -0.0024 | 37 | 16 |
| 225 | Garcia, Brett | OTT_TIT | Four-Seam | LHH | 105 | 58.7 | 55.0 | 57.6 | 85.3 | 0.0076 | 39 | 17 |
| 232 | Brothers, Kellen | SUS_COU1 | Four-Seam | LHH | 181 | 51.5 | 71.4 | 57.5 | 84.9 | 0.0170 | 43 | 18 |
| 241 | Agosto, Justus | TRI_VAL | Four-Seam | LHH | 45 | 53.5 | 66.1 | 57.3 | 84.3 | 0.0140 | 47 | 19 |
| 249 | Dima, Josh | GAT_GRI | Four-Seam | LHH | 92 | 59.3 | 51.9 | 57.1 | 83.8 | 0.0058 | 48 | 20 |
| 253 | Glickstein, Aaron | SCH_BOO | Four-Seam | LHH | 108 | 56.1 | 59.0 | 57.0 | 83.5 | 0.0099 | 50 | 21 |
| 258 | Langhorne, Miles | SUS_COU1 | Four-Seam | LHH | 30 | 59.1 | 51.9 | 56.9 | 83.2 | 0.0058 | 51 | 22 |
| 261 | O'Dell, Casey | JOL_SLA | Four-Seam | LHH | 51 | 55.1 | 61.0 | 56.9 | 83.0 | 0.0111 | 52 | 23 |
| 264 | Jones, Breyln | NEW_JER6 | Four-Seam | LHH | 28 | 52.6 | 66.7 | 56.8 | 82.8 | 0.0143 | 53 | 24 |
| 269 | Alpern, Liam | FLO_Y'A | Four-Seam | LHH | 86 | 53.9 | 63.4 | 56.8 | 82.4 | 0.0124 | 57 | 25 |

### Four-Seam vs RHH

| Rank | Pitcher | Team | Pitch Type | Batter Side | Split Pitches | PVS | Loc | Final | Final % | Avg Loc Adv | Type Rank | Type/Side Rank |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 6 | Grounds, Jackson | DOW_EAS1 | Four-Seam | RHH | 48 | 74.4 | 68.5 | 72.6 | 99.7 | 0.0153 | 1 | 1 |
| 14 | Davis, Tyler | WIN_CIT29 | Four-Seam | RHH | 33 | 74.4 | 64.7 | 71.5 | 99.1 | 0.0131 | 2 | 2 |
| 25 | Cameron, Zach | WIN_CIT29 | Four-Seam | RHH | 63 | 71.7 | 62.4 | 68.9 | 98.4 | 0.0119 | 4 | 3 |
| 26 | Debban, Caleb | NEW_JER6 | Four-Seam | RHH | 37 | 73.8 | 56.1 | 68.5 | 98.4 | 0.0082 | 5 | 4 |
| 43 | Mercado, Nelson | OTT_TIT | Four-Seam | RHH | 42 | 60.8 | 76.4 | 65.5 | 97.2 | 0.0199 | 7 | 5 |
| 52 | Grounds, Jackson | TRO_AIG | Four-Seam | RHH | 35 | 67.9 | 55.4 | 64.2 | 96.7 | 0.0078 | 8 | 6 |
| 77 | Gregory, Ben | GAT_GRI | Four-Seam | RHH | 74 | 64.1 | 60.0 | 62.9 | 95.0 | 0.0105 | 10 | 7 |
| 93 | Langhorne, Miles | SUS_COU1 | Four-Seam | RHH | 40 | 59.1 | 68.8 | 62.0 | 94.0 | 0.0155 | 12 | 8 |
| 96 | Wehrle, Tyler | WIN_CIT29 | Four-Seam | RHH | 156 | 59.8 | 66.1 | 61.7 | 93.8 | 0.0140 | 13 | 9 |
| 109 | Correa, Nelvin | QUE_CAP | Four-Seam | RHH | 45 | 67.2 | 46.8 | 61.1 | 92.9 | 0.0029 | 14 | 10 |
| 127 | Garbrick, Alex | LAK_ERI24 | Four-Seam | RHH | 43 | 63.4 | 53.2 | 60.3 | 91.7 | 0.0066 | 17 | 11 |
| 131 | Foy, Corbin | LAK_ERI24 | Four-Seam | RHH | 47 | 65.8 | 47.4 | 60.3 | 91.5 | 0.0032 | 18 | 12 |
| 133 | Shears, Tanner | SCH_BOO | Four-Seam | RHH | 126 | 60.6 | 58.9 | 60.1 | 91.4 | 0.0098 | 19 | 13 |
| 146 | Ginn, Landon | WAS_WIL3 | Four-Seam | RHH | 67 | 54.4 | 72.3 | 59.8 | 90.5 | 0.0175 | 21 | 14 |
| 151 | O'Dell, Casey | JOL_SLA | Four-Seam | RHH | 63 | 55.1 | 70.5 | 59.7 | 90.2 | 0.0165 | 24 | 15 |
| 158 | Kelly, Colin | SUS_COU1 | Four-Seam | RHH | 49 | 58.4 | 62.1 | 59.5 | 89.7 | 0.0117 | 25 | 16 |
| 167 | Foster, Kobe | WAS_WIL3 | Four-Seam | RHH | 261 | 58.7 | 60.4 | 59.2 | 89.1 | 0.0107 | 28 | 17 |
| 169 | Garcia, Brett | OTT_TIT | Four-Seam | RHH | 153 | 58.7 | 60.4 | 59.2 | 89.0 | 0.0107 | 29 | 18 |
| 171 | Zaffiro, Cole | SCH_BOO | Four-Seam | RHH | 159 | 60.1 | 57.0 | 59.2 | 88.9 | 0.0088 | 30 | 19 |
| 195 | Brouwer, Adam | LAK_ERI24 | Four-Seam | RHH | 41 | 57.9 | 60.4 | 58.6 | 87.3 | 0.0107 | 33 | 20 |
| 196 | Rodriguez, Joe Joe | NEW_JER6 | Four-Seam | RHH | 48 | 58.4 | 59.1 | 58.6 | 87.2 | 0.0099 | 34 | 21 |
| 210 | Albert, Wes | TRI_VAL | Four-Seam | RHH | 54 | 53.0 | 70.0 | 58.1 | 86.3 | 0.0162 | 38 | 22 |
| 227 | Johnson, Preston | MIS_MUD | Four-Seam | RHH | 28 | 50.0 | 75.1 | 57.5 | 85.2 | 0.0191 | 40 | 23 |
| 230 | Calderon, Jean | LAK_ERI24 | Four-Seam | RHH | 51 | 55.0 | 63.3 | 57.5 | 85.0 | 0.0124 | 41 | 24 |
| 231 | Glickstein, Aaron | SCH_BOO | Four-Seam | RHH | 75 | 56.1 | 60.6 | 57.5 | 84.9 | 0.0108 | 42 | 25 |

### Sinker vs LHH

| Rank | Pitcher | Team | Pitch Type | Batter Side | Split Pitches | PVS | Loc | Final | Final % | Avg Loc Adv | Type Rank | Type/Side Rank |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 73 | Riedel, Caleb | SCH_BOO | Sinker | LHH | 33 | 70.0 | 46.6 | 63.0 | 95.3 | 0.0028 | 4 | 1 |
| 86 | Glickstein, Aaron | SCH_BOO | Sinker | LHH | 29 | 68.3 | 48.2 | 62.3 | 94.4 | 0.0037 | 6 | 2 |
| 98 | Mannering, Shawn | DOW_EAS1 | Sinker | LHH | 27 | 63.3 | 57.7 | 61.6 | 93.6 | 0.0091 | 7 | 3 |
| 129 | Colon, Jeffrey | TRO_AIG | Sinker | LHH | 30 | 64.9 | 49.7 | 60.3 | 91.6 | 0.0045 | 11 | 4 |
| 164 | Widener, Jacob | SUS_COU1 | Sinker | LHH | 58 | 63.7 | 49.0 | 59.3 | 89.3 | 0.0042 | 12 | 5 |
| 193 | Sabatine, Gino | TRI_VAL | Sinker | LHH | 36 | 59.6 | 56.6 | 58.7 | 87.4 | 0.0085 | 13 | 6 |
| 236 | McCartney, Seth | MIS_MUD | Sinker | LHH | 67 | 56.7 | 58.8 | 57.4 | 84.6 | 0.0098 | 15 | 7 |
| 257 | Morgan, Marcus | JOL_SLA | Sinker | LHH | 60 | 58.1 | 54.4 | 57.0 | 83.2 | 0.0072 | 17 | 8 |
| 279 | Lovell, Justin | WIN_CIT29 | Sinker | LHH | 77 | 60.5 | 47.3 | 56.5 | 81.8 | 0.0032 | 18 | 9 |
| 285 | Aldeano, Austin | TRO_AIG | Sinker | LHH | 45 | 54.3 | 61.2 | 56.4 | 81.4 | 0.0112 | 19 | 10 |
| 328 | Lawson, Nathan | FLO_Y'A | Sinker | LHH | 115 | 56.7 | 52.9 | 55.6 | 78.6 | 0.0064 | 23 | 11 |
| 362 | Fritz, AJ | MIS_MUD | Sinker | LHH | 33 | 55.6 | 52.9 | 54.8 | 76.4 | 0.0064 | 26 | 12 |
| 372 | Harley, Tristan | SUS_COU1 | Sinker | LHH | 74 | 59.6 | 42.7 | 54.5 | 75.7 | 0.0005 | 27 | 13 |
| 377 | Cerda, Junior | EVA_OTT | Sinker | LHH | 49 | 58.9 | 44.1 | 54.5 | 75.4 | 0.0013 | 29 | 14 |
| 393 | Hensey, Rob | SUS_COU1 | Sinker | LHH | 158 | 53.9 | 55.1 | 54.3 | 74.3 | 0.0077 | 32 | 15 |
| 401 | Kelly, Aiden | TRI_VAL | Sinker | LHH | 51 | 52.2 | 58.5 | 54.1 | 73.8 | 0.0096 | 33 | 16 |
| 404 | Turner, Eric | JOL_SLA | Sinker | LHH | 45 | 56.8 | 47.9 | 54.1 | 73.6 | 0.0035 | 34 | 17 |
| 440 | Henderson, Drew | DOW_EAS1 | Sinker | LHH | 76 | 56.7 | 46.3 | 53.6 | 71.3 | 0.0026 | 38 | 18 |
| 441 | Allemann, Braeden | QUE_CAP | Sinker | LHH | 40 | 53.9 | 52.8 | 53.6 | 71.2 | 0.0063 | 39 | 19 |
| 446 | Vecerka, Boris | QUE_CAP | Sinker | LHH | 138 | 52.8 | 55.2 | 53.5 | 70.9 | 0.0077 | 41 | 20 |
| 452 | Stuka, Ted | OTT_TIT | Sinker | LHH | 82 | 51.3 | 58.5 | 53.4 | 70.5 | 0.0096 | 43 | 21 |
| 464 | Hungate, Chase | NEW_JER6 | Sinker | LHH | 32 | 59.7 | 38.0 | 53.2 | 69.7 | -0.0022 | 45 | 22 |
| 469 | Cook, Cole | SCH_BOO | Sinker | LHH | 53 | 51.7 | 56.6 | 53.2 | 69.4 | 0.0085 | 46 | 23 |
| 479 | Webster, Evan | FLO_Y'A | Sinker | LHH | 33 | 52.2 | 55.1 | 53.0 | 68.7 | 0.0077 | 48 | 24 |
| 484 | Grounds, Jackson | DOW_EAS1 | Sinker | LHH | 75 | 57.2 | 43.1 | 53.0 | 68.4 | 0.0008 | 49 | 25 |

### Sinker vs RHH

| Rank | Pitcher | Team | Pitch Type | Batter Side | Split Pitches | PVS | Loc | Final | Final % | Avg Loc Adv | Type Rank | Type/Side Rank |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 37 | Glickstein, Aaron | SCH_BOO | Sinker | RHH | 72 | 68.3 | 61.3 | 66.2 | 97.6 | 0.0112 | 1 | 1 |
| 47 | Still, Stephen | TRI_VAL | Sinker | RHH | 50 | 69.5 | 53.8 | 64.8 | 97.0 | 0.0069 | 2 | 2 |
| 57 | Riedel, Caleb | SCH_BOO | Sinker | RHH | 44 | 70.0 | 48.7 | 63.6 | 96.3 | 0.0040 | 3 | 3 |
| 76 | Colon, Jeffrey | TRO_AIG | Sinker | RHH | 26 | 64.9 | 58.2 | 62.9 | 95.1 | 0.0094 | 5 | 4 |
| 102 | Garcia, Andrew | EVA_OTT | Sinker | RHH | 29 | 62.9 | 58.2 | 61.5 | 93.4 | 0.0094 | 8 | 5 |
| 103 | Mannering, Shawn | DOW_EAS1 | Sinker | RHH | 32 | 63.3 | 57.1 | 61.4 | 93.3 | 0.0088 | 9 | 6 |
| 117 | Petschke, Ben | EVA_OTT | Sinker | RHH | 42 | 60.6 | 61.3 | 60.8 | 92.4 | 0.0112 | 10 | 7 |
| 213 | Turner, Eric | JOL_SLA | Sinker | RHH | 46 | 56.8 | 61.1 | 58.1 | 86.1 | 0.0111 | 14 | 8 |
| 247 | Aldeano, Austin | TRO_AIG | Sinker | RHH | 25 | 54.3 | 63.6 | 57.1 | 83.9 | 0.0125 | 16 | 9 |
| 287 | Widener, Jacob | SUS_COU1 | Sinker | RHH | 81 | 63.7 | 39.1 | 56.3 | 81.3 | -0.0016 | 20 | 10 |
| 291 | Henderson, Drew | DOW_EAS1 | Sinker | RHH | 39 | 56.7 | 55.0 | 56.2 | 81.0 | 0.0076 | 21 | 11 |
| 304 | McCartney, Seth | MIS_MUD | Sinker | RHH | 53 | 56.7 | 53.9 | 55.9 | 80.2 | 0.0070 | 22 | 12 |
| 344 | Lovell, Justin | WIN_CIT29 | Sinker | RHH | 52 | 60.5 | 42.7 | 55.1 | 77.5 | 0.0005 | 24 | 13 |
| 354 | Morgan, Marcus | JOL_SLA | Sinker | RHH | 35 | 58.1 | 47.6 | 54.9 | 76.9 | 0.0034 | 25 | 14 |
| 375 | Vecerka, Boris | QUE_CAP | Sinker | RHH | 81 | 52.8 | 58.5 | 54.5 | 75.5 | 0.0096 | 28 | 15 |
| 386 | Hungate, Chase | NEW_JER6 | Sinker | RHH | 34 | 59.7 | 41.7 | 54.3 | 74.8 | -0.0000 | 30 | 16 |
| 391 | Cerda, Junior | EVA_OTT | Sinker | RHH | 65 | 58.9 | 43.6 | 54.3 | 74.5 | 0.0010 | 31 | 17 |
| 405 | Long, Maddox | WAS_WIL3 | Sinker | RHH | 117 | 56.0 | 49.7 | 54.1 | 73.5 | 0.0046 | 35 | 18 |
| 426 | Plumadore, Carson | WIN_CIT29 | Sinker | RHH | 49 | 54.8 | 51.2 | 53.7 | 72.2 | 0.0054 | 36 | 19 |
| 437 | Kelly, Aiden | TRI_VAL | Sinker | RHH | 27 | 52.2 | 56.8 | 53.6 | 71.4 | 0.0086 | 37 | 20 |
| 442 | Lawson, Nathan | FLO_Y'A | Sinker | RHH | 71 | 56.7 | 46.3 | 53.6 | 71.1 | 0.0026 | 40 | 21 |
| 451 | Kelly, Colin | SUS_COU1 | Sinker | RHH | 53 | 54.5 | 51.0 | 53.4 | 70.5 | 0.0053 | 42 | 22 |
| 462 | Grounds, Jackson | DOW_EAS1 | Sinker | RHH | 41 | 57.2 | 44.2 | 53.3 | 69.8 | 0.0014 | 44 | 23 |
| 470 | Gregory, Ben | GAT_GRI | Sinker | RHH | 136 | 53.8 | 51.7 | 53.1 | 69.3 | 0.0057 | 47 | 24 |
| 493 | Hoeymans, Jack | GAT_GRI | Sinker | RHH | 35 | 50.4 | 58.7 | 52.9 | 67.8 | 0.0097 | 50 | 25 |

### Slider vs LHH

| Rank | Pitcher | Team | Pitch Type | Batter Side | Split Pitches | PVS | Loc | Final | Final % | Avg Loc Adv | Type Rank | Type/Side Rank |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 9 | Alpern, Liam | FLO_Y'A | Slider | LHH | 38 | 76.4 | 61.5 | 72.0 | 99.5 | 0.0114 | 6 | 1 |
| 15 | Ryan, Dillon | NEW_ENG23 | Slider | LHH | 64 | 79.9 | 51.3 | 71.3 | 99.1 | 0.0055 | 10 | 2 |
| 17 | Leduc, Zachary | TRO_AIG | Slider | LHH | 32 | 79.2 | 52.0 | 71.0 | 99.0 | 0.0059 | 11 | 3 |
| 20 | Carroll, Jake | JOL_SLA | Slider | LHH | 50 | 80.0 | 47.8 | 70.3 | 98.8 | 0.0035 | 12 | 4 |
| 28 | McEvoy, Aidan | FLO_Y'A | Slider | LHH | 69 | 70.5 | 62.0 | 67.9 | 98.2 | 0.0116 | 15 | 5 |
| 29 | Jones, Logan | TRI_VAL | Slider | LHH | 33 | 74.7 | 51.2 | 67.7 | 98.2 | 0.0054 | 16 | 6 |
| 35 | Harper, Scott | NEW_YOR13 | Slider | LHH | 46 | 72.6 | 52.0 | 66.4 | 97.8 | 0.0059 | 20 | 7 |
| 46 | Balzan, Jackson | SUS_COU1 | Slider | LHH | 75 | 66.5 | 61.4 | 64.9 | 97.1 | 0.0113 | 27 | 8 |
| 71 | Bargo, Casey | NEW_ENG23 | Slider | LHH | 27 | 73.6 | 39.2 | 63.3 | 95.4 | -0.0015 | 38 | 9 |
| 84 | MacMillan, Blake | TRO_AIG | Slider | LHH | 63 | 64.1 | 58.4 | 62.4 | 94.6 | 0.0096 | 42 | 10 |
| 115 | Morgan, Cooper | QUE_CAP | Slider | LHH | 42 | 62.3 | 57.6 | 60.9 | 92.5 | 0.0091 | 53 | 11 |
| 119 | Foster, Kobe | WAS_WIL3 | Slider | LHH | 122 | 63.6 | 53.7 | 60.6 | 92.3 | 0.0069 | 55 | 12 |
| 149 | Eckaus, David | EVA_OTT | Slider | LHH | 115 | 59.1 | 61.3 | 59.8 | 90.3 | 0.0112 | 64 | 13 |
| 155 | Webster, Evan | FLO_Y'A | Slider | LHH | 76 | 59.3 | 60.4 | 59.6 | 89.9 | 0.0107 | 66 | 14 |
| 160 | Scott, Brandon | LAK_ERI24 | Slider | LHH | 67 | 59.0 | 60.5 | 59.5 | 89.6 | 0.0108 | 67 | 15 |
| 166 | Widener, Jacob | SUS_COU1 | Slider | LHH | 54 | 60.7 | 56.0 | 59.3 | 89.2 | 0.0082 | 69 | 16 |
| 174 | Hensey, Rob | SUS_COU1 | Slider | LHH | 81 | 59.0 | 59.2 | 59.0 | 88.7 | 0.0100 | 73 | 17 |
| 181 | Vail, Tyler | NEW_YOR13 | Slider | LHH | 50 | 62.9 | 49.7 | 59.0 | 88.2 | 0.0045 | 76 | 18 |
| 184 | Morin, Jacob | QUE_CAP | Slider | LHH | 25 | 65.8 | 42.8 | 58.9 | 88.0 | 0.0006 | 79 | 19 |
| 188 | Dima, Josh | GAT_GRI | Slider | LHH | 75 | 57.3 | 62.3 | 58.8 | 87.8 | 0.0118 | 81 | 20 |
| 190 | Kemlage, Joe | NEW_ENG23 | Slider | LHH | 38 | 61.7 | 51.9 | 58.8 | 87.6 | 0.0058 | 82 | 21 |
| 216 | Harris, Everette | TRI_VAL | Slider | LHH | 29 | 56.5 | 61.3 | 57.9 | 85.9 | 0.0112 | 85 | 22 |
| 221 | Sechrist, Zander | WAS_WIL3 | Slider | LHH | 48 | 58.3 | 56.1 | 57.6 | 85.6 | 0.0082 | 87 | 23 |
| 226 | Milburn, Isaac | FLO_Y'A | Slider | LHH | 79 | 54.9 | 63.7 | 57.5 | 85.3 | 0.0126 | 90 | 24 |
| 229 | Plumadore, Carson | WIN_CIT29 | Slider | LHH | 37 | 62.9 | 44.8 | 57.5 | 85.1 | 0.0018 | 91 | 25 |

### Slider vs RHH

| Rank | Pitcher | Team | Pitch Type | Batter Side | Split Pitches | PVS | Loc | Final | Final % | Avg Loc Adv | Type Rank | Type/Side Rank |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | Ryan, Dillon | NEW_ENG23 | Slider | RHH | 61 | 79.9 | 69.2 | 76.7 | 100.0 | 0.0157 | 1 | 1 |
| 2 | Kirby, Zach | WAS_WIL3 | Slider | RHH | 126 | 71.7 | 80.0 | 74.2 | 99.9 | 0.0222 | 2 | 2 |
| 3 | Bargo, Casey | NEW_ENG23 | Slider | RHH | 29 | 73.6 | 75.5 | 74.1 | 99.9 | 0.0194 | 3 | 3 |
| 5 | Moore, Kyle | SCH_BOO | Slider | RHH | 31 | 71.2 | 76.5 | 72.8 | 99.7 | 0.0199 | 4 | 4 |
| 7 | Vecerka, Boris | QUE_CAP | Slider | RHH | 53 | 77.6 | 60.8 | 72.5 | 99.6 | 0.0109 | 5 | 5 |
| 11 | Hickey, Matt | GAT_GRI | Slider | RHH | 71 | 73.5 | 67.5 | 71.7 | 99.3 | 0.0148 | 7 | 6 |
| 12 | Harper, Scott | NEW_YOR13 | Slider | RHH | 166 | 72.6 | 69.1 | 71.5 | 99.3 | 0.0157 | 8 | 7 |
| 13 | Leduc, Zachary | TRO_AIG | Slider | RHH | 46 | 79.2 | 53.6 | 71.5 | 99.2 | 0.0068 | 9 | 8 |
| 21 | Nakata, Yuto | QUE_CAP | Slider | RHH | 89 | 70.5 | 68.3 | 69.8 | 98.7 | 0.0152 | 13 | 9 |
| 27 | Donnan, Blake | FLO_Y'A | Slider | RHH | 52 | 70.1 | 63.8 | 68.2 | 98.3 | 0.0126 | 14 | 10 |
| 30 | Vega, Lucas | TRO_AIG | Slider | RHH | 94 | 66.7 | 68.1 | 67.1 | 98.1 | 0.0151 | 17 | 11 |
| 31 | Barraza, Chris | MIS_MUD | Slider | RHH | 34 | 63.4 | 75.8 | 67.1 | 98.0 | 0.0196 | 18 | 12 |
| 33 | O'Hanlon, Michael | WAS_WIL3 | Slider | RHH | 51 | 61.9 | 78.2 | 66.8 | 97.9 | 0.0209 | 19 | 13 |
| 39 | Perozzi, John | SUS_COU1 | Slider | RHH | 63 | 64.1 | 70.1 | 65.9 | 97.5 | 0.0162 | 21 | 14 |
| 40 | Jones, Logan | FLO_Y'A | Slider | RHH | 33 | 68.5 | 59.1 | 65.7 | 97.4 | 0.0099 | 22 | 15 |
| 41 | Jones, Logan | TRI_VAL | Slider | RHH | 32 | 74.7 | 44.5 | 65.7 | 97.4 | 0.0016 | 23 | 16 |
| 42 | Petschke, Ben | EVA_OTT | Slider | RHH | 86 | 64.6 | 67.7 | 65.6 | 97.3 | 0.0149 | 24 | 17 |
| 44 | Morin, Jacob | QUE_CAP | Slider | RHH | 60 | 65.8 | 64.3 | 65.3 | 97.2 | 0.0129 | 25 | 18 |
| 45 | Alpern, Liam | FLO_Y'A | Slider | RHH | 40 | 76.4 | 38.3 | 65.0 | 97.1 | -0.0020 | 26 | 19 |
| 49 | Vail, Tyler | NEW_YOR13 | Slider | RHH | 147 | 62.9 | 68.4 | 64.6 | 96.9 | 0.0153 | 28 | 20 |
| 53 | Vailes, Gage | GAT_GRI | Slider | RHH | 220 | 57.5 | 79.5 | 64.1 | 96.6 | 0.0217 | 29 | 21 |
| 54 | Garcia, Hector | WAS_WIL3 | Slider | RHH | 36 | 57.2 | 80.0 | 64.1 | 96.5 | 0.0270 | 30 | 22 |
| 55 | Allemann, Braeden | QUE_CAP | Slider | RHH | 65 | 58.3 | 76.9 | 63.9 | 96.5 | 0.0202 | 31 | 23 |
| 59 | Dill, Austin | TRI_VAL | Slider | RHH | 62 | 61.1 | 69.5 | 63.6 | 96.2 | 0.0159 | 32 | 24 |
| 60 | Hagan, Jack | DOW_EAS1 | Slider | RHH | 129 | 57.9 | 76.7 | 63.5 | 96.1 | 0.0200 | 33 | 25 |

### Splitter vs LHH

| Rank | Pitcher | Team | Pitch Type | Batter Side | Split Pitches | PVS | Loc | Final | Final % | Avg Loc Adv | Type Rank | Type/Side Rank |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 48 | Garcia, Hector | WAS_WIL3 | Splitter | LHH | 59 | 73.6 | 43.9 | 64.7 | 96.9 | 0.0012 | 1 | 1 |
| 100 | Coles, Chad | WAS_WIL3 | Splitter | LHH | 38 | 67.6 | 47.2 | 61.5 | 93.5 | 0.0031 | 2 | 2 |
| 177 | Pindel, Buddie | SCH_BOO | Splitter | LHH | 58 | 65.3 | 44.3 | 59.0 | 88.5 | 0.0014 | 6 | 3 |
| 199 | Villers, Ian | QUE_CAP | Splitter | LHH | 39 | 65.2 | 42.7 | 58.5 | 87.0 | 0.0005 | 7 | 4 |
| 203 | Shears, Tanner | SCH_BOO | Splitter | LHH | 36 | 65.5 | 41.8 | 58.4 | 86.8 | 0.0000 | 9 | 5 |
| 211 | Vitas, Ben | JOL_SLA | Splitter | LHH | 91 | 63.9 | 44.6 | 58.1 | 86.2 | 0.0016 | 10 | 6 |
| 383 | Williams, Brian | MIS_MUD | Splitter | LHH | 57 | 58.3 | 45.1 | 54.4 | 75.0 | 0.0019 | 12 | 7 |
| 422 | Thornton, Tyler | NEW_ENG23 | Splitter | LHH | 69 | 57.2 | 45.7 | 53.7 | 72.4 | 0.0023 | 13 | 8 |
| 545 | Salata, Derek | SCH_BOO | Splitter | LHH | 90 | 55.4 | 44.5 | 52.1 | 64.4 | 0.0015 | 15 | 9 |
| 565 | Thompson, Ross | SCH_BOO | Splitter | LHH | 145 | 55.2 | 44.0 | 51.8 | 63.1 | 0.0013 | 17 | 10 |
| 1345 | Nakata, Yuto | QUE_CAP | Splitter | LHH | 80 | 42.2 | 38.2 | 41.0 | 12.0 | -0.0020 | 19 | 11 |
| 1385 | Eldred, Zach | NEW_ENG23 | Splitter | LHH | 45 | 37.6 | 46.5 | 40.2 | 9.4 | 0.0027 | 21 | 12 |
| 1472 | Duby, Bill | NEW_JER6 | Splitter | LHH | 43 | 35.2 | 41.0 | 36.9 | 3.7 | -0.0005 | 23 | 13 |
| 1511 | Andueza, Axel | DOW_EAS1 | Splitter | LHH | 70 | 28.5 | 41.7 | 32.4 | 1.1 | -0.0000 | 25 | 14 |

### Splitter vs RHH

| Rank | Pitcher | Team | Pitch Type | Batter Side | Split Pitches | PVS | Loc | Final | Final % | Avg Loc Adv | Type Rank | Type/Side Rank |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 135 | Coles, Chad | WAS_WIL3 | Splitter | RHH | 25 | 67.6 | 42.3 | 60.0 | 91.2 | 0.0003 | 3 | 1 |
| 159 | Villers, Ian | QUE_CAP | Splitter | RHH | 25 | 65.2 | 46.1 | 59.5 | 89.7 | 0.0025 | 4 | 2 |
| 176 | Pindel, Buddie | SCH_BOO | Splitter | RHH | 31 | 65.3 | 44.3 | 59.0 | 88.5 | 0.0015 | 5 | 3 |
| 201 | Shears, Tanner | SCH_BOO | Splitter | RHH | 33 | 65.5 | 41.9 | 58.4 | 86.9 | 0.0001 | 8 | 4 |
| 270 | Vitas, Ben | JOL_SLA | Splitter | RHH | 36 | 63.9 | 40.1 | 56.8 | 82.4 | -0.0010 | 11 | 5 |
| 429 | Williams, Brian | MIS_MUD | Splitter | RHH | 44 | 58.3 | 42.7 | 53.7 | 72.0 | 0.0006 | 14 | 6 |
| 548 | Thornton, Tyler | NEW_ENG23 | Splitter | RHH | 50 | 57.2 | 40.3 | 52.1 | 64.2 | -0.0009 | 16 | 7 |
| 749 | Thompson, Ross | SCH_BOO | Splitter | RHH | 30 | 55.2 | 36.2 | 49.5 | 51.0 | -0.0032 | 18 | 8 |
| 1353 | Nakata, Yuto | QUE_CAP | Splitter | RHH | 30 | 42.2 | 37.8 | 40.9 | 11.5 | -0.0023 | 20 | 9 |
| 1426 | Eldred, Zach | NEW_ENG23 | Splitter | RHH | 35 | 37.6 | 41.7 | 38.8 | 6.7 | -0.0001 | 22 | 10 |
| 1510 | Andueza, Axel | DOW_EAS1 | Splitter | RHH | 26 | 28.5 | 42.0 | 32.5 | 1.2 | 0.0001 | 24 | 11 |
