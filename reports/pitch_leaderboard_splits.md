# Handedness-Specific Pitch Leaderboards

- Pitch Value input: `data\processed\pitch_value_scores_with_type_rank.csv` (889 rows)
- Location Score input: `data\processed\location_scores.csv` (1,811 rows)
- Split component input: `data\processed\2026-data-with-woba-xwoba.parquet`
- Output file: `data\processed\pitch_leaderboard_splits.csv`
- Joined leaderboard rows: 1,581
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
| 1 | Ryan, Dillon | NEW_ENG23 | Slider | RHH | 61 | 79.9 | 72.2 | 77.6 | 100.0 | 0.0183 | 1 | 1 |
| 2 | Vecerka, Boris | QUE_CAP | Slider | RHH | 62 | 80.0 | 60.9 | 74.3 | 99.9 | 0.0116 | 2 | 2 |
| 3 | Kirby, Zach | WAS_WIL3 | Slider | RHH | 126 | 71.6 | 80.0 | 74.2 | 99.9 | 0.0234 | 3 | 3 |
| 4 | Bargo, Casey | NEW_ENG23 | Slider | RHH | 29 | 73.5 | 75.0 | 73.9 | 99.8 | 0.0199 | 4 | 4 |
| 5 | Grounds, Jackson | DOW_EAS1 | Curveball | RHH | 43 | 80.0 | 57.6 | 73.3 | 99.7 | 0.0096 | 1 | 1 |
| 6 | Grounds, Jackson | DOW_EAS1 | Four-Seam | RHH | 48 | 74.3 | 67.0 | 72.1 | 99.7 | 0.0152 | 1 | 1 |
| 7 | Harper, Scott | NEW_YOR13 | Slider | RHH | 169 | 73.6 | 68.3 | 72.1 | 99.6 | 0.0160 | 5 | 5 |
| 8 | Zentko, Dylan | EVA_OTT | Changeup | RHH | 57 | 78.5 | 56.4 | 71.9 | 99.6 | 0.0089 | 1 | 1 |
| 9 | Ryan, Dillon | NEW_ENG23 | Slider | LHH | 64 | 79.9 | 51.6 | 71.4 | 99.5 | 0.0060 | 6 | 1 |
| 10 | Alpern, Liam | FLO_Y'A | Slider | LHH | 38 | 76.3 | 59.5 | 71.3 | 99.4 | 0.0107 | 7 | 2 |
| 11 | Davis, Tyler | WIN_CIT29 | Four-Seam | RHH | 33 | 74.3 | 63.9 | 71.2 | 99.4 | 0.0133 | 2 | 2 |
| 12 | Peyton, Blake | GAT_GRI | Changeup | RHH | 90 | 77.2 | 56.3 | 70.9 | 99.3 | 0.0088 | 2 | 2 |
| 13 | Bauer, Patrick | QUE_CAP | Slider | RHH | 45 | 74.4 | 62.8 | 70.9 | 99.2 | 0.0127 | 8 | 6 |
| 14 | Carroll, Jake | JOL_SLA | Slider | LHH | 55 | 80.0 | 48.1 | 70.4 | 99.2 | 0.0039 | 9 | 3 |
| 15 | Morgan, Cooper | QUE_CAP | Curveball | LHH | 66 | 78.0 | 50.0 | 69.6 | 99.1 | 0.0051 | 2 | 1 |
| 16 | Serrano, Elio | NEW_JER6 | Changeup | LHH | 56 | 75.9 | 54.7 | 69.5 | 99.1 | 0.0079 | 3 | 1 |
| 17 | McEvoy, Aidan | FLO_Y'A | Slider | LHH | 76 | 72.5 | 62.0 | 69.4 | 99.0 | 0.0122 | 10 | 4 |
| 18 | Duncan, Tanner | DOW_EAS1 | Slider | RHH | 38 | 68.9 | 69.9 | 69.2 | 98.9 | 0.0169 | 11 | 7 |
| 19 | Hickey, Matt | GAT_GRI | Slider | RHH | 72 | 70.5 | 65.7 | 69.1 | 98.9 | 0.0144 | 12 | 8 |
| 20 | Grounds, Jackson | DOW_EAS1 | Curveball | LHH | 39 | 80.0 | 43.3 | 69.0 | 98.8 | 0.0011 | 3 | 2 |
| 21 | Debban, Caleb | NEW_JER6 | Four-Seam | RHH | 37 | 73.7 | 57.3 | 68.8 | 98.7 | 0.0094 | 3 | 3 |
| 22 | Nakata, Yuto | QUE_CAP | Slider | RHH | 99 | 68.9 | 68.2 | 68.7 | 98.7 | 0.0159 | 13 | 9 |
| 23 | Cameron, Zach | WIN_CIT29 | Four-Seam | RHH | 65 | 71.9 | 60.7 | 68.6 | 98.6 | 0.0114 | 4 | 4 |
| 24 | Lawson, Nathan | FLO_Y'A | Changeup | LHH | 45 | 72.4 | 59.2 | 68.4 | 98.5 | 0.0105 | 4 | 2 |
| 25 | Morrissey, Joe | EVA_OTT | Slider | RHH | 47 | 62.8 | 80.0 | 67.9 | 98.5 | 0.0234 | 14 | 10 |
| 26 | Grounds, Jackson | DOW_EAS1 | Four-Seam | LHH | 59 | 74.3 | 52.8 | 67.9 | 98.4 | 0.0068 | 5 | 1 |
| 27 | Jones, Logan | TRI_VAL | Slider | LHH | 33 | 74.7 | 51.4 | 67.7 | 98.4 | 0.0059 | 15 | 5 |
| 28 | Donnan, Blake | FLO_Y'A | Slider | RHH | 52 | 70.0 | 62.2 | 67.6 | 98.3 | 0.0123 | 16 | 11 |
| 29 | Barraza, Chris | MIS_MUD | Slider | RHH | 36 | 63.2 | 76.9 | 67.4 | 98.2 | 0.0211 | 17 | 12 |
| 30 | Escobar, Anthony | TRO_AIG | Changeup | LHH | 157 | 69.2 | 61.6 | 66.9 | 98.2 | 0.0120 | 5 | 3 |
| 31 | Vega, Lucas | TRO_AIG | Slider | RHH | 94 | 66.6 | 67.2 | 66.8 | 98.1 | 0.0153 | 18 | 13 |
| 32 | Harper, Scott | NEW_YOR13 | Slider | LHH | 48 | 73.6 | 50.8 | 66.8 | 98.0 | 0.0056 | 19 | 6 |
| 33 | Smith, Ben | NEW_ENG23 | Changeup | RHH | 43 | 67.4 | 64.1 | 66.4 | 98.0 | 0.0135 | 6 | 3 |
| 34 | Davis, Tyler | WIN_CIT29 | Four-Seam | LHH | 43 | 74.3 | 48.1 | 66.4 | 97.9 | 0.0040 | 6 | 2 |
| 35 | O'Hanlon, Michael | WAS_WIL3 | Slider | RHH | 54 | 60.5 | 80.0 | 66.4 | 97.8 | 0.0232 | 20 | 14 |
| 36 | Mercado, Nelson | OTT_TIT | Four-Seam | RHH | 42 | 60.6 | 79.2 | 66.2 | 97.8 | 0.0224 | 7 | 5 |
| 37 | Leduc, Zachary | TRO_AIG | Slider | RHH | 49 | 71.7 | 53.0 | 66.1 | 97.7 | 0.0069 | 21 | 15 |
| 38 | Perozzi, John | SUS_COU1 | Slider | RHH | 64 | 64.7 | 68.8 | 65.9 | 97.7 | 0.0162 | 22 | 16 |
| 39 | Jones, Logan | TRI_VAL | Slider | RHH | 32 | 74.7 | 44.7 | 65.7 | 97.6 | 0.0019 | 23 | 17 |
| 40 | Moore, Kyle | SCH_BOO | Slider | RHH | 36 | 63.5 | 70.4 | 65.6 | 97.5 | 0.0172 | 24 | 18 |

## Pitch Type + Batter Side Leaderboards

### Changeup vs LHH

| Rank | Pitcher | Team | Pitch Type | Batter Side | Split Pitches | PVS | Loc | Final | Final % | Avg Loc Adv | Type Rank | Type/Side Rank |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 16 | Serrano, Elio | NEW_JER6 | Changeup | LHH | 56 | 75.9 | 54.7 | 69.5 | 99.1 | 0.0079 | 3 | 1 |
| 24 | Lawson, Nathan | FLO_Y'A | Changeup | LHH | 45 | 72.4 | 59.2 | 68.4 | 98.5 | 0.0105 | 4 | 2 |
| 30 | Escobar, Anthony | TRO_AIG | Changeup | LHH | 157 | 69.2 | 61.6 | 66.9 | 98.2 | 0.0120 | 5 | 3 |
| 48 | Rodriguez, Joe Joe | NEW_JER6 | Changeup | LHH | 111 | 68.2 | 55.6 | 64.4 | 97.0 | 0.0084 | 7 | 4 |
| 59 | Harris, Everette | TRI_VAL | Changeup | LHH | 56 | 69.6 | 49.8 | 63.7 | 96.3 | 0.0050 | 8 | 5 |
| 67 | Leak, Anthony | NEW_YOR13 | Changeup | LHH | 64 | 66.0 | 56.8 | 63.2 | 95.8 | 0.0091 | 9 | 6 |
| 76 | Parsons, Billy | SUS_COU1 | Changeup | LHH | 43 | 68.4 | 49.6 | 62.8 | 95.3 | 0.0049 | 12 | 7 |
| 81 | Maietta, Dante | WIN_CIT29 | Changeup | LHH | 158 | 62.1 | 63.9 | 62.6 | 94.9 | 0.0133 | 13 | 8 |
| 104 | Wiltse, Ryan | EVA_OTT | Changeup | LHH | 110 | 68.1 | 45.9 | 61.5 | 93.5 | 0.0026 | 15 | 9 |
| 106 | Sesar, Jorden | SUS_COU1 | Changeup | LHH | 60 | 63.2 | 57.2 | 61.4 | 93.4 | 0.0094 | 16 | 10 |
| 109 | Drakeford, Dosie | NEW_JER6 | Changeup | LHH | 66 | 64.7 | 53.5 | 61.3 | 93.2 | 0.0072 | 17 | 11 |
| 127 | Willeman, Landon | EVA_OTT | Changeup | LHH | 127 | 61.0 | 58.8 | 60.3 | 92.0 | 0.0103 | 19 | 12 |
| 139 | Pardinho, Eric | OTT_TIT | Changeup | LHH | 119 | 60.5 | 58.6 | 59.9 | 91.3 | 0.0102 | 22 | 13 |
| 141 | Dill, Austin | TRI_VAL | Changeup | LHH | 118 | 56.2 | 68.4 | 59.9 | 91.1 | 0.0160 | 23 | 14 |
| 182 | Hocom, Quinn | TRI_VAL | Changeup | LHH | 74 | 59.3 | 58.6 | 59.1 | 88.6 | 0.0102 | 24 | 15 |
| 190 | Plumadore, Carson | WIN_CIT29 | Changeup | LHH | 194 | 60.5 | 54.8 | 58.8 | 88.0 | 0.0080 | 25 | 16 |
| 225 | Hensey, Rob | SUS_COU1 | Changeup | LHH | 55 | 60.4 | 51.5 | 57.7 | 85.8 | 0.0060 | 27 | 17 |
| 229 | Albert, Wes | DOW_EAS1 | Changeup | LHH | 42 | 51.0 | 73.0 | 57.6 | 85.6 | 0.0188 | 28 | 18 |
| 237 | Tokar, Heitor | OTT_TIT | Changeup | LHH | 41 | 63.3 | 44.0 | 57.5 | 85.1 | 0.0015 | 30 | 19 |
| 279 | Campbell, Tyler | MIS_MUD | Changeup | LHH | 25 | 63.6 | 40.3 | 56.6 | 82.4 | -0.0007 | 32 | 20 |
| 291 | Barreto, Brayhans | TRI_VAL | Changeup | LHH | 29 | 60.8 | 46.0 | 56.3 | 81.7 | 0.0027 | 36 | 21 |
| 302 | Burcham, Jacob | GAT_GRI | Changeup | LHH | 64 | 55.1 | 58.8 | 56.2 | 81.0 | 0.0103 | 37 | 22 |
| 303 | Miner, Jace | DOW_EAS1 | Changeup | LHH | 67 | 63.2 | 40.0 | 56.2 | 80.9 | -0.0009 | 38 | 23 |
| 323 | Andueza, Axel | DOW_EAS1 | Changeup | LHH | 86 | 57.9 | 50.9 | 55.8 | 79.6 | 0.0056 | 41 | 24 |
| 336 | Cameron, Zach | WIN_CIT29 | Changeup | LHH | 139 | 53.9 | 59.4 | 55.6 | 78.8 | 0.0106 | 43 | 25 |

### Changeup vs RHH

| Rank | Pitcher | Team | Pitch Type | Batter Side | Split Pitches | PVS | Loc | Final | Final % | Avg Loc Adv | Type Rank | Type/Side Rank |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 8 | Zentko, Dylan | EVA_OTT | Changeup | RHH | 57 | 78.5 | 56.4 | 71.9 | 99.6 | 0.0089 | 1 | 1 |
| 12 | Peyton, Blake | GAT_GRI | Changeup | RHH | 90 | 77.2 | 56.3 | 70.9 | 99.3 | 0.0088 | 2 | 2 |
| 33 | Smith, Ben | NEW_ENG23 | Changeup | RHH | 43 | 67.4 | 64.1 | 66.4 | 98.0 | 0.0135 | 6 | 3 |
| 70 | Rodriguez, Joe Joe | NEW_JER6 | Changeup | RHH | 33 | 68.2 | 51.0 | 63.1 | 95.6 | 0.0057 | 10 | 4 |
| 73 | Wiltse, Ryan | EVA_OTT | Changeup | RHH | 55 | 68.1 | 50.8 | 62.9 | 95.4 | 0.0056 | 11 | 5 |
| 91 | Harris, Everette | TRI_VAL | Changeup | RHH | 40 | 69.6 | 44.7 | 62.1 | 94.3 | 0.0019 | 14 | 6 |
| 123 | Messina, Chris | FDU_KNI | Changeup | RHH | 52 | 66.3 | 47.4 | 60.6 | 92.3 | 0.0035 | 18 | 7 |
| 128 | Campbell, Tyler | MIS_MUD | Changeup | RHH | 90 | 63.6 | 52.7 | 60.3 | 92.0 | 0.0067 | 20 | 8 |
| 131 | Earwood, Micah | SUS_COU1 | Changeup | RHH | 197 | 63.7 | 52.3 | 60.3 | 91.8 | 0.0064 | 21 | 9 |
| 209 | Miner, Jace | DOW_EAS1 | Changeup | RHH | 89 | 63.2 | 46.9 | 58.3 | 86.8 | 0.0032 | 26 | 10 |
| 235 | Rohde, Isaac | NEW_YOR13 | Changeup | RHH | 551 | 58.2 | 55.8 | 57.5 | 85.2 | 0.0085 | 29 | 11 |
| 246 | Hocom, Quinn | TRI_VAL | Changeup | RHH | 27 | 59.3 | 52.9 | 57.3 | 84.5 | 0.0068 | 31 | 12 |
| 280 | Maietta, Dante | WIN_CIT29 | Changeup | RHH | 125 | 62.1 | 43.5 | 56.5 | 82.4 | 0.0012 | 33 | 13 |
| 282 | VanMarter, Luke | LEM_COL | Changeup | RHH | 29 | 59.1 | 50.3 | 56.5 | 82.2 | 0.0053 | 34 | 14 |
| 284 | Morgan, Cooper | QUE_CAP | Changeup | RHH | 69 | 62.8 | 41.6 | 56.4 | 82.1 | 0.0001 | 35 | 15 |
| 313 | Barreto, Brayhans | TRI_VAL | Changeup | RHH | 93 | 60.8 | 45.0 | 56.0 | 80.3 | 0.0021 | 39 | 16 |
| 322 | Brothers, Kellen | SUS_COU1 | Changeup | RHH | 47 | 58.7 | 49.1 | 55.8 | 79.7 | 0.0045 | 40 | 17 |
| 325 | Tokar, Heitor | OTT_TIT | Changeup | RHH | 33 | 63.3 | 38.3 | 55.8 | 79.5 | -0.0019 | 42 | 18 |
| 351 | Willeman, Landon | EVA_OTT | Changeup | RHH | 52 | 61.0 | 42.1 | 55.4 | 77.9 | 0.0004 | 45 | 19 |
| 361 | Hensey, Rob | SUS_COU1 | Changeup | RHH | 222 | 60.4 | 42.8 | 55.1 | 77.2 | 0.0008 | 47 | 20 |
| 370 | Plumadore, Carson | WIN_CIT29 | Changeup | RHH | 78 | 60.5 | 42.0 | 54.9 | 76.7 | 0.0003 | 50 | 21 |
| 381 | Gollert, Harley | TRO_AIG | Changeup | RHH | 117 | 53.7 | 57.4 | 54.8 | 76.0 | 0.0095 | 51 | 22 |
| 423 | Boies, Emiles | QUE_CAP | Changeup | RHH | 62 | 57.7 | 45.4 | 54.0 | 73.3 | 0.0023 | 56 | 23 |
| 473 | Foster, Kobe | WAS_WIL3 | Changeup | RHH | 181 | 57.6 | 42.9 | 53.2 | 70.1 | 0.0009 | 62 | 24 |
| 490 | McKillican, Adam | QUE_CAP | Changeup | RHH | 33 | 54.7 | 48.9 | 53.0 | 69.1 | 0.0044 | 66 | 25 |

### Curveball vs LHH

| Rank | Pitcher | Team | Pitch Type | Batter Side | Split Pitches | PVS | Loc | Final | Final % | Avg Loc Adv | Type Rank | Type/Side Rank |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 15 | Morgan, Cooper | QUE_CAP | Curveball | LHH | 66 | 78.0 | 50.0 | 69.6 | 99.1 | 0.0051 | 2 | 1 |
| 20 | Grounds, Jackson | DOW_EAS1 | Curveball | LHH | 39 | 80.0 | 43.3 | 69.0 | 98.8 | 0.0011 | 3 | 2 |
| 50 | Bohnert, Matthew | WIN_CIT29 | Curveball | LHH | 46 | 71.8 | 46.4 | 64.1 | 96.9 | 0.0029 | 5 | 3 |
| 130 | Binns, Malik | NEW_JER6 | Curveball | LHH | 27 | 66.2 | 46.3 | 60.3 | 91.8 | 0.0029 | 16 | 4 |
| 147 | Salata, Derek | SCH_BOO | Curveball | LHH | 50 | 66.3 | 44.4 | 59.8 | 90.8 | 0.0018 | 18 | 5 |
| 154 | Hohenstein, Liam | WIN_CIT29 | Curveball | LHH | 46 | 67.1 | 42.3 | 59.7 | 90.3 | 0.0005 | 19 | 6 |
| 157 | Garcia, Brett | OTT_TIT | Curveball | LHH | 51 | 67.2 | 41.8 | 59.6 | 90.1 | 0.0002 | 21 | 7 |
| 173 | Eisenbarger, Jack | QUE_CAP | Curveball | LHH | 66 | 64.7 | 46.6 | 59.3 | 89.1 | 0.0031 | 24 | 8 |
| 180 | Heredia-Bustos, Rolando | DOW_EAS1 | Curveball | LHH | 35 | 66.2 | 42.8 | 59.2 | 88.7 | 0.0008 | 25 | 9 |
| 196 | Hickey, Matt | GAT_GRI | Curveball | LHH | 29 | 68.1 | 36.5 | 58.6 | 87.7 | -0.0030 | 26 | 10 |
| 227 | Harris, Ben | GAT_GRI | Curveball | LHH | 115 | 64.1 | 42.7 | 57.7 | 85.7 | 0.0008 | 31 | 11 |
| 270 | Cook, Cole | SCH_BOO | Curveball | LHH | 50 | 63.6 | 40.5 | 56.7 | 83.0 | -0.0006 | 37 | 12 |
| 272 | Hill, Kaleb | OTT_TIT | Curveball | LHH | 127 | 62.6 | 42.8 | 56.7 | 82.9 | 0.0008 | 38 | 13 |
| 301 | Earwood, Micah | SUS_COU1 | Curveball | LHH | 58 | 60.5 | 46.2 | 56.2 | 81.0 | 0.0028 | 40 | 14 |
| 305 | Wiltse, Ryan | EVA_OTT | Curveball | LHH | 97 | 61.6 | 43.4 | 56.2 | 80.8 | 0.0012 | 41 | 15 |
| 326 | Townes, Holland | SCH_BOO | Curveball | LHH | 28 | 64.1 | 36.2 | 55.7 | 79.4 | -0.0031 | 43 | 16 |
| 328 | Long, Jalon | NEW_YOR13 | Curveball | LHH | 26 | 55.7 | 55.8 | 55.7 | 79.3 | 0.0085 | 44 | 17 |
| 346 | Gollert, Harley | TRO_AIG | Curveball | LHH | 28 | 58.0 | 49.4 | 55.4 | 78.2 | 0.0047 | 46 | 18 |
| 399 | Langrell, Connor | MIS_MUD | Curveball | LHH | 57 | 56.3 | 50.3 | 54.5 | 74.8 | 0.0053 | 50 | 19 |
| 449 | Maryniak, Connor | NEW_JER6 | Curveball | LHH | 106 | 56.8 | 45.9 | 53.5 | 71.7 | 0.0026 | 54 | 20 |
| 469 | Hocom, Quinn | TRI_VAL | Curveball | LHH | 41 | 55.3 | 48.5 | 53.2 | 70.4 | 0.0042 | 58 | 21 |
| 496 | Balzan, Jackson | SUS_COU1 | Curveball | LHH | 29 | 56.9 | 43.5 | 52.9 | 68.7 | 0.0012 | 60 | 22 |
| 505 | Carroll, Jake | JOL_SLA | Curveball | LHH | 36 | 50.3 | 58.7 | 52.8 | 68.1 | 0.0103 | 63 | 23 |
| 510 | Boies, Emiles | QUE_CAP | Curveball | LHH | 28 | 58.0 | 40.5 | 52.7 | 67.8 | -0.0006 | 65 | 24 |
| 523 | Lefebvre, Charles | TRO_AIG | Curveball | LHH | 47 | 58.6 | 38.4 | 52.6 | 67.0 | -0.0018 | 66 | 25 |

### Curveball vs RHH

| Rank | Pitcher | Team | Pitch Type | Batter Side | Split Pitches | PVS | Loc | Final | Final % | Avg Loc Adv | Type Rank | Type/Side Rank |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 5 | Grounds, Jackson | DOW_EAS1 | Curveball | RHH | 43 | 80.0 | 57.6 | 73.3 | 99.7 | 0.0096 | 1 | 1 |
| 46 | Hohenstein, Liam | WIN_CIT29 | Curveball | RHH | 60 | 67.1 | 58.2 | 64.5 | 97.2 | 0.0100 | 4 | 2 |
| 58 | Jones, Breyln | NEW_JER6 | Curveball | RHH | 37 | 68.4 | 52.7 | 63.7 | 96.4 | 0.0067 | 6 | 3 |
| 65 | Garcia, Brett | OTT_TIT | Curveball | RHH | 70 | 67.2 | 54.0 | 63.2 | 96.0 | 0.0074 | 7 | 4 |
| 68 | Heredia-Bustos, Rolando | DOW_EAS1 | Curveball | RHH | 40 | 66.2 | 56.3 | 63.2 | 95.8 | 0.0088 | 8 | 5 |
| 72 | Hickey, Matt | GAT_GRI | Curveball | RHH | 36 | 68.1 | 51.2 | 63.0 | 95.5 | 0.0058 | 9 | 6 |
| 80 | Binns, Malik | NEW_JER6 | Curveball | RHH | 28 | 66.2 | 54.2 | 62.6 | 95.0 | 0.0076 | 10 | 7 |
| 82 | Bohnert, Matthew | WIN_CIT29 | Curveball | RHH | 52 | 71.8 | 41.1 | 62.6 | 94.9 | -0.0002 | 11 | 8 |
| 94 | Gregory, Ben | GAT_GRI | Curveball | RHH | 29 | 66.5 | 50.8 | 61.8 | 94.1 | 0.0055 | 12 | 9 |
| 95 | Salata, Derek | SCH_BOO | Curveball | RHH | 72 | 66.3 | 51.0 | 61.7 | 94.1 | 0.0057 | 13 | 10 |
| 118 | Majick, Eli | NEW_ENG23 | Curveball | RHH | 34 | 63.0 | 56.0 | 60.9 | 92.6 | 0.0086 | 14 | 11 |
| 125 | Harris, Ben | GAT_GRI | Curveball | RHH | 163 | 64.1 | 52.0 | 60.5 | 92.2 | 0.0063 | 15 | 12 |
| 144 | Wiltse, Ryan | EVA_OTT | Curveball | RHH | 49 | 61.6 | 55.5 | 59.8 | 91.0 | 0.0084 | 17 | 13 |
| 155 | Hampton, Ky | OTT_TIT | Curveball | RHH | 39 | 61.1 | 56.2 | 59.7 | 90.3 | 0.0088 | 20 | 14 |
| 164 | Simpson, Garret | EVA_OTT | Curveball | RHH | 55 | 56.4 | 66.5 | 59.5 | 89.7 | 0.0149 | 22 | 15 |
| 167 | Townes, Holland | SCH_BOO | Curveball | RHH | 62 | 64.1 | 48.5 | 59.4 | 89.5 | 0.0042 | 23 | 16 |
| 199 | Eisenbarger, Jack | QUE_CAP | Curveball | RHH | 27 | 64.7 | 44.1 | 58.5 | 87.5 | 0.0015 | 27 | 17 |
| 201 | Lefebvre, Charles | TRO_AIG | Curveball | RHH | 52 | 58.6 | 58.0 | 58.4 | 87.3 | 0.0098 | 28 | 18 |
| 219 | Earwood, Micah | SUS_COU1 | Curveball | RHH | 160 | 60.5 | 51.6 | 57.9 | 86.2 | 0.0060 | 29 | 19 |
| 226 | Maryniak, Connor | NEW_JER6 | Curveball | RHH | 96 | 56.8 | 59.9 | 57.7 | 85.8 | 0.0110 | 30 | 20 |
| 232 | Cook, Cole | SCH_BOO | Curveball | RHH | 66 | 63.6 | 43.4 | 57.6 | 85.4 | 0.0012 | 32 | 21 |
| 238 | Allemann, Braeden | QUE_CAP | Curveball | RHH | 137 | 56.4 | 60.0 | 57.5 | 85.0 | 0.0110 | 33 | 22 |
| 243 | Hill, Kaleb | OTT_TIT | Curveball | RHH | 120 | 62.6 | 45.3 | 57.4 | 84.7 | 0.0023 | 34 | 23 |
| 256 | Long, Jalon | NEW_YOR13 | Curveball | RHH | 27 | 55.7 | 60.4 | 57.1 | 83.9 | 0.0113 | 35 | 24 |
| 263 | Scafidi, Christian | LAK_ERI24 | Curveball | RHH | 35 | 61.2 | 47.0 | 56.9 | 83.4 | 0.0033 | 36 | 25 |

### Cutter vs LHH

| Rank | Pitcher | Team | Pitch Type | Batter Side | Split Pitches | PVS | Loc | Final | Final % | Avg Loc Adv | Type Rank | Type/Side Rank |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 85 | Webster, Evan | FLO_Y'A | Cutter | LHH | 99 | 70.4 | 43.9 | 62.4 | 94.7 | 0.0014 | 1 | 1 |
| 126 | Majick, Eli | NEW_ENG23 | Cutter | LHH | 28 | 66.4 | 46.3 | 60.4 | 92.1 | 0.0029 | 5 | 2 |
| 137 | Correa, Nelvin | QUE_CAP | Cutter | LHH | 63 | 67.9 | 41.6 | 60.0 | 91.4 | 0.0001 | 6 | 3 |
| 214 | Parsons, Billy | SUS_COU1 | Cutter | LHH | 40 | 64.0 | 44.5 | 58.2 | 86.5 | 0.0018 | 8 | 4 |
| 297 | Lockhart, Gauge | LAK_ERI24 | Cutter | LHH | 68 | 62.7 | 41.3 | 56.3 | 81.3 | -0.0001 | 11 | 5 |
| 344 | Morgan, Marcus | JOL_SLA | Cutter | LHH | 40 | 61.0 | 42.5 | 55.5 | 78.3 | 0.0006 | 12 | 6 |
| 410 | McEvoy, Aidan | FLO_Y'A | Cutter | LHH | 36 | 56.4 | 49.2 | 54.2 | 74.1 | 0.0046 | 14 | 7 |
| 425 | Bell, Brendan | NEW_ENG23 | Cutter | LHH | 52 | 59.1 | 41.8 | 53.9 | 73.2 | 0.0002 | 15 | 8 |
| 465 | Flontek, Zac | DOW_EAS1 | Cutter | LHH | 27 | 57.7 | 43.0 | 53.3 | 70.7 | 0.0009 | 16 | 9 |
| 575 | Debban, Caleb | NEW_JER6 | Cutter | LHH | 60 | 56.5 | 41.4 | 51.9 | 63.7 | -0.0000 | 19 | 10 |
| 594 | Moore, Kyle | SCH_BOO | Cutter | LHH | 38 | 55.1 | 43.8 | 51.7 | 62.5 | 0.0014 | 21 | 11 |
| 609 | Valdez, Alex | EVA_OTT | Cutter | LHH | 27 | 57.3 | 38.0 | 51.6 | 61.5 | -0.0020 | 22 | 12 |
| 628 | Saturria, Michael | NEW_ENG23 | Cutter | LHH | 127 | 56.8 | 38.4 | 51.3 | 60.3 | -0.0018 | 25 | 13 |
| 630 | Campbell, AJ | WIN_CIT29 | Cutter | LHH | 41 | 54.7 | 43.2 | 51.2 | 60.2 | 0.0010 | 26 | 14 |
| 689 | Smith, Jackson | MIS_MUD | Cutter | LHH | 44 | 54.0 | 42.4 | 50.5 | 56.5 | 0.0006 | 29 | 15 |
| 718 | Campbell, Tyler | MIS_MUD | Cutter | LHH | 60 | 53.2 | 43.1 | 50.2 | 54.6 | 0.0010 | 31 | 16 |
| 743 | Gorgen, Grady | NEW_YOR13 | Cutter | LHH | 41 | 54.1 | 40.0 | 49.8 | 53.1 | -0.0009 | 33 | 17 |
| 754 | MacMillan, Blake | TRO_AIG | Cutter | LHH | 61 | 54.0 | 39.7 | 49.7 | 52.4 | -0.0010 | 34 | 18 |
| 785 | Morgan, Cooper | QUE_CAP | Cutter | LHH | 61 | 53.9 | 38.7 | 49.3 | 50.4 | -0.0016 | 35 | 19 |
| 919 | Langrell, Connor | MIS_MUD | Cutter | LHH | 117 | 49.9 | 43.0 | 47.8 | 41.9 | 0.0009 | 41 | 20 |
| 995 | Binns, Malik | NEW_JER6 | Cutter | LHH | 34 | 49.1 | 41.8 | 46.9 | 37.1 | 0.0002 | 45 | 21 |
| 1041 | Catrambone, Ben | JOL_SLA | Cutter | LHH | 28 | 46.5 | 45.9 | 46.3 | 34.2 | 0.0026 | 47 | 22 |
| 1054 | Gamelin, Shaun | JOL_SLA | Cutter | LHH | 56 | 48.5 | 40.8 | 46.2 | 33.4 | -0.0004 | 48 | 23 |
| 1088 | Petschke, Ben | EVA_OTT | Cutter | LHH | 150 | 45.3 | 47.1 | 45.9 | 31.2 | 0.0034 | 49 | 24 |
| 1118 | Parks, Pavin | LAK_ERI24 | Cutter | LHH | 40 | 48.1 | 39.3 | 45.4 | 29.3 | -0.0013 | 51 | 25 |

### Cutter vs RHH

| Rank | Pitcher | Team | Pitch Type | Batter Side | Split Pitches | PVS | Loc | Final | Final % | Avg Loc Adv | Type Rank | Type/Side Rank |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 101 | Correa, Nelvin | QUE_CAP | Cutter | RHH | 55 | 67.9 | 47.0 | 61.6 | 93.7 | 0.0033 | 2 | 1 |
| 114 | Majick, Eli | NEW_ENG23 | Cutter | RHH | 60 | 66.4 | 48.4 | 61.0 | 92.9 | 0.0041 | 3 | 2 |
| 122 | Webster, Evan | FLO_Y'A | Cutter | RHH | 39 | 70.4 | 38.1 | 60.7 | 92.3 | -0.0020 | 4 | 3 |
| 185 | Lockhart, Gauge | LAK_ERI24 | Cutter | RHH | 71 | 62.7 | 50.1 | 58.9 | 88.4 | 0.0051 | 7 | 4 |
| 234 | Bell, Brendan | NEW_ENG23 | Cutter | RHH | 41 | 59.1 | 53.8 | 57.5 | 85.3 | 0.0073 | 9 | 5 |
| 265 | Good, Ty | GAT_GRI | Cutter | RHH | 40 | 58.4 | 53.4 | 56.9 | 83.3 | 0.0071 | 10 | 6 |
| 402 | Valdez, Alex | EVA_OTT | Cutter | RHH | 65 | 57.3 | 47.8 | 54.5 | 74.6 | 0.0038 | 13 | 7 |
| 495 | Saturria, Michael | NEW_ENG23 | Cutter | RHH | 128 | 56.8 | 43.7 | 52.9 | 68.8 | 0.0014 | 17 | 8 |
| 501 | Campbell, AJ | WIN_CIT29 | Cutter | RHH | 50 | 54.7 | 48.5 | 52.8 | 68.4 | 0.0042 | 18 | 9 |
| 584 | Debban, Caleb | NEW_JER6 | Cutter | RHH | 81 | 56.5 | 41.1 | 51.8 | 63.1 | -0.0002 | 20 | 10 |
| 618 | McEvoy, Aidan | FLO_Y'A | Cutter | RHH | 47 | 56.4 | 40.0 | 51.5 | 61.0 | -0.0009 | 23 | 11 |
| 619 | Flontek, Zac | DOW_EAS1 | Cutter | RHH | 30 | 57.7 | 36.9 | 51.5 | 60.9 | -0.0027 | 24 | 12 |
| 656 | Smith, Jackson | MIS_MUD | Cutter | RHH | 55 | 54.0 | 44.0 | 51.0 | 58.6 | 0.0015 | 27 | 13 |
| 679 | Moore, Kyle | SCH_BOO | Cutter | RHH | 109 | 55.1 | 40.2 | 50.6 | 57.1 | -0.0008 | 28 | 14 |
| 690 | Gorgen, Grady | NEW_YOR13 | Cutter | RHH | 37 | 54.1 | 42.2 | 50.5 | 56.4 | 0.0004 | 30 | 15 |
| 727 | Morgan, Cooper | QUE_CAP | Cutter | RHH | 54 | 53.9 | 40.9 | 50.0 | 54.1 | -0.0003 | 32 | 16 |
| 832 | Whitesell, Max | FLO_Y'A | Cutter | RHH | 34 | 53.0 | 39.0 | 48.8 | 47.4 | -0.0014 | 36 | 17 |
| 865 | MacMillan, Blake | TRO_AIG | Cutter | RHH | 83 | 54.0 | 35.3 | 48.4 | 45.4 | -0.0036 | 37 | 18 |
| 874 | Binns, Malik | NEW_JER6 | Cutter | RHH | 54 | 49.1 | 46.3 | 48.3 | 44.8 | 0.0029 | 38 | 19 |
| 887 | Wiltse, Ryan | EVA_OTT | Cutter | RHH | 48 | 47.2 | 50.4 | 48.2 | 44.0 | 0.0053 | 39 | 20 |
| 896 | Campbell, Tyler | MIS_MUD | Cutter | RHH | 88 | 53.2 | 36.1 | 48.0 | 43.4 | -0.0032 | 40 | 21 |
| 931 | Langrell, Connor | MIS_MUD | Cutter | RHH | 158 | 49.9 | 42.5 | 47.7 | 41.2 | 0.0006 | 42 | 22 |
| 937 | Parks, Pavin | LAK_ERI24 | Cutter | RHH | 94 | 48.1 | 46.6 | 47.6 | 40.8 | 0.0031 | 43 | 23 |
| 950 | Ginn, Landon | WAS_WIL3 | Cutter | RHH | 62 | 45.7 | 51.7 | 47.5 | 40.0 | 0.0061 | 44 | 24 |
| 1004 | Gamelin, Shaun | JOL_SLA | Cutter | RHH | 82 | 48.5 | 42.7 | 46.8 | 36.6 | 0.0007 | 46 | 25 |

### Four-Seam vs LHH

| Rank | Pitcher | Team | Pitch Type | Batter Side | Split Pitches | PVS | Loc | Final | Final % | Avg Loc Adv | Type Rank | Type/Side Rank |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 26 | Grounds, Jackson | DOW_EAS1 | Four-Seam | LHH | 59 | 74.3 | 52.8 | 67.9 | 98.4 | 0.0068 | 5 | 1 |
| 34 | Davis, Tyler | WIN_CIT29 | Four-Seam | LHH | 43 | 74.3 | 48.1 | 66.4 | 97.9 | 0.0040 | 6 | 2 |
| 60 | Wehrle, Tyler | WIN_CIT29 | Four-Seam | LHH | 80 | 59.6 | 72.6 | 63.5 | 96.3 | 0.0185 | 8 | 3 |
| 78 | Cameron, Zach | WIN_CIT29 | Four-Seam | LHH | 55 | 71.9 | 41.3 | 62.8 | 95.1 | -0.0001 | 10 | 4 |
| 100 | Morgan, Cooper | QUE_CAP | Four-Seam | LHH | 43 | 61.6 | 61.8 | 61.6 | 93.7 | 0.0121 | 14 | 5 |
| 129 | Foster, Kobe | WAS_WIL3 | Four-Seam | LHH | 180 | 58.6 | 64.3 | 60.3 | 91.9 | 0.0136 | 19 | 6 |
| 138 | Cartwright, Eli | GAT_GRI | Four-Seam | LHH | 61 | 61.4 | 56.8 | 60.0 | 91.3 | 0.0091 | 22 | 7 |
| 140 | Shears, Tanner | SCH_BOO | Four-Seam | LHH | 97 | 62.8 | 53.2 | 59.9 | 91.2 | 0.0070 | 23 | 8 |
| 163 | Mercado, Nelson | OTT_TIT | Four-Seam | LHH | 39 | 60.6 | 56.7 | 59.5 | 89.8 | 0.0091 | 28 | 9 |
| 166 | Herbert, Andrew | WAS_WIL3 | Four-Seam | LHH | 35 | 57.4 | 64.3 | 59.4 | 89.6 | 0.0136 | 29 | 10 |
| 169 | Grounds, Jackson | TRO_AIG | Four-Seam | LHH | 34 | 66.9 | 41.9 | 59.4 | 89.4 | 0.0002 | 30 | 11 |
| 188 | Correa, Nelvin | QUE_CAP | Four-Seam | LHH | 43 | 67.3 | 39.1 | 58.8 | 88.2 | -0.0014 | 34 | 12 |
| 192 | Foy, Corbin | LAK_ERI24 | Four-Seam | LHH | 48 | 65.7 | 42.5 | 58.7 | 87.9 | 0.0006 | 35 | 13 |
| 211 | Brown, Ethan | WAS_WIL3 | Four-Seam | LHH | 25 | 62.0 | 49.3 | 58.2 | 86.7 | 0.0047 | 37 | 14 |
| 213 | Zaffiro, Cole | SCH_BOO | Four-Seam | LHH | 141 | 59.0 | 56.2 | 58.2 | 86.6 | 0.0088 | 38 | 15 |
| 239 | Glickstein, Aaron | SCH_BOO | Four-Seam | LHH | 109 | 56.3 | 60.1 | 57.4 | 84.9 | 0.0111 | 46 | 16 |
| 244 | Dima, Josh | GAT_GRI | Four-Seam | LHH | 92 | 59.2 | 53.2 | 57.4 | 84.6 | 0.0070 | 48 | 17 |
| 248 | Langhorne, Miles | SUS_COU1 | Four-Seam | LHH | 30 | 58.9 | 53.5 | 57.3 | 84.4 | 0.0072 | 49 | 18 |
| 258 | Alpern, Liam | FLO_Y'A | Four-Seam | LHH | 86 | 53.8 | 64.8 | 57.1 | 83.7 | 0.0139 | 56 | 19 |
| 260 | Anderson, Colt | WAS_WIL3 | Four-Seam | LHH | 117 | 60.3 | 49.7 | 57.1 | 83.6 | 0.0049 | 58 | 20 |
| 264 | Harley, Tristan | SUS_COU1 | Four-Seam | LHH | 31 | 60.0 | 49.6 | 56.9 | 83.4 | 0.0048 | 59 | 21 |
| 266 | Brothers, Kellen | SUS_COU1 | Four-Seam | LHH | 181 | 51.3 | 69.7 | 56.8 | 83.2 | 0.0168 | 60 | 22 |
| 269 | Moore, Kyle | SCH_BOO | Four-Seam | LHH | 101 | 56.4 | 57.5 | 56.7 | 83.0 | 0.0095 | 62 | 23 |
| 293 | Williams, Pierce | NEW_ENG23 | Four-Seam | LHH | 95 | 56.6 | 55.5 | 56.3 | 81.5 | 0.0084 | 67 | 24 |
| 307 | Hughes, Grif | EVA_OTT | Four-Seam | LHH | 30 | 52.5 | 64.5 | 56.1 | 80.6 | 0.0137 | 71 | 25 |

### Four-Seam vs RHH

| Rank | Pitcher | Team | Pitch Type | Batter Side | Split Pitches | PVS | Loc | Final | Final % | Avg Loc Adv | Type Rank | Type/Side Rank |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 6 | Grounds, Jackson | DOW_EAS1 | Four-Seam | RHH | 48 | 74.3 | 67.0 | 72.1 | 99.7 | 0.0152 | 1 | 1 |
| 11 | Davis, Tyler | WIN_CIT29 | Four-Seam | RHH | 33 | 74.3 | 63.9 | 71.2 | 99.4 | 0.0133 | 2 | 2 |
| 21 | Debban, Caleb | NEW_JER6 | Four-Seam | RHH | 37 | 73.7 | 57.3 | 68.8 | 98.7 | 0.0094 | 3 | 3 |
| 23 | Cameron, Zach | WIN_CIT29 | Four-Seam | RHH | 65 | 71.9 | 60.7 | 68.6 | 98.6 | 0.0114 | 4 | 4 |
| 36 | Mercado, Nelson | OTT_TIT | Four-Seam | RHH | 42 | 60.6 | 79.2 | 66.2 | 97.8 | 0.0224 | 7 | 5 |
| 62 | Gregory, Ben | GAT_GRI | Four-Seam | RHH | 74 | 64.0 | 61.7 | 63.3 | 96.1 | 0.0121 | 9 | 6 |
| 86 | Correa, Nelvin | QUE_CAP | Four-Seam | RHH | 53 | 67.3 | 50.9 | 62.4 | 94.6 | 0.0056 | 11 | 7 |
| 90 | Grounds, Jackson | TRO_AIG | Four-Seam | RHH | 45 | 66.9 | 51.0 | 62.1 | 94.4 | 0.0057 | 12 | 8 |
| 99 | Wehrle, Tyler | WIN_CIT29 | Four-Seam | RHH | 156 | 59.6 | 66.4 | 61.7 | 93.8 | 0.0148 | 13 | 9 |
| 107 | Langhorne, Miles | SUS_COU1 | Four-Seam | RHH | 40 | 58.9 | 67.2 | 61.4 | 93.3 | 0.0153 | 15 | 10 |
| 113 | Foy, Corbin | LAK_ERI24 | Four-Seam | RHH | 47 | 65.7 | 50.4 | 61.1 | 92.9 | 0.0053 | 16 | 11 |
| 115 | Earwood, Micah | SUS_COU1 | Four-Seam | RHH | 95 | 65.5 | 50.4 | 61.0 | 92.8 | 0.0053 | 17 | 12 |
| 116 | Shears, Tanner | SCH_BOO | Four-Seam | RHH | 143 | 62.8 | 56.7 | 61.0 | 92.7 | 0.0091 | 18 | 13 |
| 133 | Garbrick, Alex | LAK_ERI24 | Four-Seam | RHH | 43 | 63.2 | 53.2 | 60.2 | 91.7 | 0.0070 | 20 | 14 |
| 135 | O'Dell, Casey | JOL_SLA | Four-Seam | RHH | 66 | 54.1 | 74.2 | 60.1 | 91.5 | 0.0195 | 21 | 15 |
| 146 | Campbell, Tyler | MIS_MUD | Four-Seam | RHH | 37 | 68.7 | 39.1 | 59.8 | 90.8 | -0.0014 | 24 | 16 |
| 152 | Harley, Tristan | SUS_COU1 | Four-Seam | RHH | 37 | 60.0 | 58.9 | 59.7 | 90.4 | 0.0104 | 25 | 17 |
| 159 | Kelly, Colin | SUS_COU1 | Four-Seam | RHH | 49 | 58.2 | 62.5 | 59.5 | 90.0 | 0.0125 | 26 | 18 |
| 160 | Ginn, Landon | WAS_WIL3 | Four-Seam | RHH | 68 | 54.3 | 71.7 | 59.5 | 89.9 | 0.0180 | 27 | 19 |
| 174 | Foster, Kobe | WAS_WIL3 | Four-Seam | RHH | 261 | 58.6 | 60.9 | 59.3 | 89.1 | 0.0115 | 31 | 20 |
| 177 | Rodriguez, Joe Joe | NEW_JER6 | Four-Seam | RHH | 56 | 57.1 | 64.3 | 59.2 | 88.9 | 0.0136 | 32 | 21 |
| 179 | Brouwer, Adam | LAK_ERI24 | Four-Seam | RHH | 41 | 57.8 | 62.4 | 59.2 | 88.7 | 0.0124 | 33 | 22 |
| 194 | Zaffiro, Cole | SCH_BOO | Four-Seam | RHH | 194 | 59.0 | 57.8 | 58.7 | 87.8 | 0.0097 | 36 | 23 |
| 217 | Hughes, Grif | EVA_OTT | Four-Seam | RHH | 27 | 52.5 | 70.8 | 58.0 | 86.3 | 0.0174 | 39 | 24 |
| 221 | Albert, Wes | TRI_VAL | Four-Seam | RHH | 54 | 52.9 | 69.4 | 57.8 | 86.1 | 0.0166 | 40 | 25 |

### Sinker vs LHH

| Rank | Pitcher | Team | Pitch Type | Batter Side | Split Pitches | PVS | Loc | Final | Final % | Avg Loc Adv | Type Rank | Type/Side Rank |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 69 | Riedel, Caleb | SCH_BOO | Sinker | LHH | 33 | 70.0 | 47.0 | 63.1 | 95.7 | 0.0033 | 3 | 1 |
| 112 | Mannering, Shawn | DOW_EAS1 | Sinker | LHH | 27 | 63.1 | 56.7 | 61.2 | 93.0 | 0.0091 | 7 | 2 |
| 124 | Glickstein, Aaron | SCH_BOO | Sinker | LHH | 30 | 66.2 | 47.3 | 60.5 | 92.2 | 0.0035 | 9 | 3 |
| 148 | Colon, Jeffrey | TRO_AIG | Sinker | LHH | 30 | 64.7 | 48.3 | 59.8 | 90.7 | 0.0041 | 11 | 4 |
| 170 | Widener, Jacob | SUS_COU1 | Sinker | LHH | 58 | 63.6 | 49.4 | 59.4 | 89.3 | 0.0047 | 12 | 5 |
| 203 | Sabatine, Gino | TRI_VAL | Sinker | LHH | 36 | 59.5 | 55.9 | 58.4 | 87.2 | 0.0086 | 14 | 6 |
| 218 | Odonnell, Brendan | NEW_ENG23 | Sinker | LHH | 37 | 65.9 | 39.4 | 57.9 | 86.3 | -0.0012 | 15 | 7 |
| 262 | McCartney, Seth | MIS_MUD | Sinker | LHH | 67 | 56.5 | 58.0 | 57.0 | 83.5 | 0.0098 | 16 | 8 |
| 275 | Morgan, Marcus | JOL_SLA | Sinker | LHH | 60 | 57.9 | 53.8 | 56.7 | 82.7 | 0.0073 | 18 | 9 |
| 281 | Aldeano, Austin | TRO_AIG | Sinker | LHH | 45 | 54.1 | 61.9 | 56.5 | 82.3 | 0.0122 | 19 | 10 |
| 358 | Plumadore, Carson | WIN_CIT29 | Sinker | LHH | 79 | 58.4 | 47.6 | 55.2 | 77.4 | 0.0037 | 24 | 11 |
| 372 | Lovell, Justin | WIN_CIT29 | Sinker | LHH | 78 | 58.5 | 46.2 | 54.8 | 76.5 | 0.0029 | 25 | 12 |
| 388 | Lawson, Nathan | FLO_Y'A | Sinker | LHH | 121 | 56.1 | 51.4 | 54.7 | 75.5 | 0.0059 | 28 | 13 |
| 403 | Fritz, AJ | MIS_MUD | Sinker | LHH | 33 | 55.5 | 52.0 | 54.5 | 74.6 | 0.0063 | 29 | 14 |
| 413 | Harley, Tristan | SUS_COU1 | Sinker | LHH | 74 | 59.4 | 41.9 | 54.2 | 73.9 | 0.0003 | 30 | 15 |
| 416 | Allemann, Braeden | QUE_CAP | Sinker | LHH | 44 | 54.0 | 54.5 | 54.1 | 73.8 | 0.0078 | 32 | 16 |
| 430 | Hensey, Rob | SUS_COU1 | Sinker | LHH | 158 | 53.7 | 54.3 | 53.9 | 72.9 | 0.0076 | 33 | 17 |
| 459 | Kelly, Aiden | TRI_VAL | Sinker | LHH | 51 | 52.0 | 56.8 | 53.4 | 71.0 | 0.0091 | 38 | 18 |
| 477 | Vecerka, Boris | QUE_CAP | Sinker | LHH | 138 | 52.6 | 54.3 | 53.1 | 69.9 | 0.0076 | 40 | 19 |
| 516 | Castro, Alexander | TRO_AIG | Sinker | LHH | 38 | 50.8 | 56.9 | 52.6 | 67.4 | 0.0092 | 45 | 20 |
| 517 | Long, Maddox | WAS_WIL3 | Sinker | LHH | 168 | 55.8 | 45.3 | 52.6 | 67.4 | 0.0023 | 46 | 21 |
| 519 | Henderson, Drew | DOW_EAS1 | Sinker | LHH | 87 | 56.9 | 42.6 | 52.6 | 67.2 | 0.0007 | 47 | 22 |
| 526 | Grounds, Jackson | DOW_EAS1 | Sinker | LHH | 75 | 57.0 | 42.0 | 52.5 | 66.8 | 0.0003 | 48 | 23 |
| 527 | Gregory, Ben | GAT_GRI | Sinker | LHH | 91 | 53.6 | 50.0 | 52.5 | 66.7 | 0.0051 | 49 | 24 |
| 536 | Webster, Evan | FLO_Y'A | Sinker | LHH | 33 | 52.0 | 53.6 | 52.5 | 66.2 | 0.0072 | 50 | 25 |

### Sinker vs RHH

| Rank | Pitcher | Team | Pitch Type | Batter Side | Split Pitches | PVS | Loc | Final | Final % | Avg Loc Adv | Type Rank | Type/Side Rank |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 51 | Still, Stephen | TRI_VAL | Sinker | RHH | 50 | 69.4 | 51.7 | 64.1 | 96.8 | 0.0061 | 1 | 1 |
| 53 | Glickstein, Aaron | SCH_BOO | Sinker | RHH | 75 | 66.2 | 59.0 | 64.0 | 96.7 | 0.0104 | 2 | 2 |
| 74 | Riedel, Caleb | SCH_BOO | Sinker | RHH | 48 | 70.0 | 46.4 | 62.9 | 95.4 | 0.0029 | 4 | 3 |
| 89 | Colon, Jeffrey | TRO_AIG | Sinker | RHH | 26 | 64.7 | 56.5 | 62.2 | 94.4 | 0.0089 | 5 | 4 |
| 96 | Garcia, Andrew | EVA_OTT | Sinker | RHH | 29 | 62.7 | 59.3 | 61.7 | 94.0 | 0.0106 | 6 | 5 |
| 117 | Mannering, Shawn | DOW_EAS1 | Sinker | RHH | 32 | 63.1 | 55.8 | 60.9 | 92.7 | 0.0085 | 8 | 6 |
| 132 | Petschke, Ben | EVA_OTT | Sinker | RHH | 42 | 60.4 | 60.0 | 60.3 | 91.7 | 0.0110 | 10 | 7 |
| 183 | Odonnell, Brendan | NEW_ENG23 | Sinker | RHH | 72 | 65.9 | 43.1 | 59.1 | 88.5 | 0.0010 | 13 | 8 |
| 273 | Aldeano, Austin | TRO_AIG | Sinker | RHH | 25 | 54.1 | 62.6 | 56.7 | 82.8 | 0.0126 | 17 | 9 |
| 286 | Plumadore, Carson | WIN_CIT29 | Sinker | RHH | 59 | 58.4 | 51.6 | 56.4 | 82.0 | 0.0060 | 20 | 10 |
| 290 | Widener, Jacob | SUS_COU1 | Sinker | RHH | 81 | 63.6 | 39.4 | 56.3 | 81.7 | -0.0012 | 21 | 11 |
| 298 | Turner, Eric | JOL_SLA | Sinker | RHH | 53 | 55.5 | 58.1 | 56.3 | 81.2 | 0.0099 | 22 | 12 |
| 304 | Henderson, Drew | DOW_EAS1 | Sinker | RHH | 42 | 56.9 | 54.5 | 56.2 | 80.8 | 0.0078 | 23 | 13 |
| 373 | McCartney, Seth | MIS_MUD | Sinker | RHH | 53 | 56.5 | 50.9 | 54.8 | 76.5 | 0.0056 | 26 | 14 |
| 378 | Morgan, Marcus | JOL_SLA | Sinker | RHH | 35 | 57.9 | 47.6 | 54.8 | 76.2 | 0.0037 | 27 | 15 |
| 415 | Vecerka, Boris | QUE_CAP | Sinker | RHH | 94 | 52.6 | 57.6 | 54.1 | 73.8 | 0.0096 | 31 | 16 |
| 435 | Grounds, Jackson | DOW_EAS1 | Sinker | RHH | 41 | 57.0 | 46.2 | 53.8 | 72.5 | 0.0028 | 34 | 17 |
| 438 | Long, Maddox | WAS_WIL3 | Sinker | RHH | 117 | 55.8 | 48.9 | 53.7 | 72.4 | 0.0044 | 35 | 18 |
| 439 | Kelly, Colin | SUS_COU1 | Sinker | RHH | 53 | 54.3 | 52.2 | 53.7 | 72.3 | 0.0064 | 36 | 19 |
| 444 | Lawson, Nathan | FLO_Y'A | Sinker | RHH | 97 | 56.1 | 47.5 | 53.6 | 72.0 | 0.0036 | 37 | 20 |
| 476 | Gregory, Ben | GAT_GRI | Sinker | RHH | 136 | 53.6 | 52.0 | 53.1 | 70.0 | 0.0063 | 39 | 21 |
| 483 | Kelly, Aiden | TRI_VAL | Sinker | RHH | 27 | 52.0 | 55.7 | 53.1 | 69.5 | 0.0085 | 41 | 22 |
| 485 | Lovell, Justin | WIN_CIT29 | Sinker | RHH | 58 | 58.5 | 40.2 | 53.0 | 69.4 | -0.0008 | 42 | 23 |
| 503 | Fuenmayor, Liu | OTT_TIT | Sinker | RHH | 57 | 55.7 | 46.1 | 52.8 | 68.2 | 0.0028 | 43 | 24 |
| 512 | Hungate, Chase | NEW_JER6 | Sinker | RHH | 42 | 58.1 | 40.1 | 52.7 | 67.7 | -0.0008 | 44 | 25 |

### Slider vs LHH

| Rank | Pitcher | Team | Pitch Type | Batter Side | Split Pitches | PVS | Loc | Final | Final % | Avg Loc Adv | Type Rank | Type/Side Rank |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 9 | Ryan, Dillon | NEW_ENG23 | Slider | LHH | 64 | 79.9 | 51.6 | 71.4 | 99.5 | 0.0060 | 6 | 1 |
| 10 | Alpern, Liam | FLO_Y'A | Slider | LHH | 38 | 76.3 | 59.5 | 71.3 | 99.4 | 0.0107 | 7 | 2 |
| 14 | Carroll, Jake | JOL_SLA | Slider | LHH | 55 | 80.0 | 48.1 | 70.4 | 99.2 | 0.0039 | 9 | 3 |
| 17 | McEvoy, Aidan | FLO_Y'A | Slider | LHH | 76 | 72.5 | 62.0 | 69.4 | 99.0 | 0.0122 | 10 | 4 |
| 27 | Jones, Logan | TRI_VAL | Slider | LHH | 33 | 74.7 | 51.4 | 67.7 | 98.4 | 0.0059 | 15 | 5 |
| 32 | Harper, Scott | NEW_YOR13 | Slider | LHH | 48 | 73.6 | 50.8 | 66.8 | 98.0 | 0.0056 | 19 | 6 |
| 42 | Balzan, Jackson | SUS_COU1 | Slider | LHH | 77 | 67.3 | 60.0 | 65.1 | 97.4 | 0.0110 | 26 | 7 |
| 54 | Leduc, Zachary | TRO_AIG | Slider | LHH | 38 | 71.7 | 46.1 | 64.0 | 96.6 | 0.0027 | 32 | 8 |
| 75 | Bargo, Casey | NEW_ENG23 | Slider | LHH | 27 | 73.5 | 38.2 | 62.9 | 95.3 | -0.0019 | 40 | 9 |
| 87 | MacMillan, Blake | TRO_AIG | Slider | LHH | 63 | 63.9 | 58.7 | 62.3 | 94.6 | 0.0102 | 45 | 10 |
| 136 | Foster, Kobe | WAS_WIL3 | Slider | LHH | 122 | 63.4 | 52.2 | 60.1 | 91.5 | 0.0064 | 60 | 11 |
| 142 | Morgan, Cooper | QUE_CAP | Slider | LHH | 44 | 60.5 | 58.4 | 59.9 | 91.1 | 0.0101 | 61 | 12 |
| 145 | Sechrist, Zander | WAS_WIL3 | Slider | LHH | 48 | 60.5 | 58.1 | 59.8 | 90.9 | 0.0099 | 63 | 13 |
| 162 | Webster, Evan | FLO_Y'A | Slider | LHH | 76 | 59.2 | 60.2 | 59.5 | 89.8 | 0.0111 | 70 | 14 |
| 172 | Duncan, Tanner | DOW_EAS1 | Slider | LHH | 26 | 68.9 | 37.0 | 59.3 | 89.2 | -0.0027 | 74 | 15 |
| 176 | Scott, Brandon | LAK_ERI24 | Slider | LHH | 70 | 58.9 | 60.1 | 59.2 | 88.9 | 0.0111 | 75 | 16 |
| 191 | Kemlage, Joe | NEW_ENG23 | Slider | LHH | 38 | 61.6 | 52.1 | 58.8 | 88.0 | 0.0063 | 81 | 17 |
| 202 | Dima, Josh | GAT_GRI | Slider | LHH | 75 | 57.2 | 61.3 | 58.4 | 87.3 | 0.0118 | 84 | 18 |
| 206 | Widener, Jacob | SUS_COU1 | Slider | LHH | 56 | 60.7 | 52.9 | 58.4 | 87.0 | 0.0068 | 87 | 19 |
| 207 | Morin, Jacob | QUE_CAP | Slider | LHH | 25 | 65.7 | 41.0 | 58.3 | 87.0 | -0.0002 | 88 | 20 |
| 208 | Hensey, Rob | SUS_COU1 | Slider | LHH | 81 | 58.9 | 57.0 | 58.3 | 86.9 | 0.0092 | 89 | 21 |
| 212 | Vail, Tyler | NEW_YOR13 | Slider | LHH | 52 | 62.8 | 47.4 | 58.2 | 86.7 | 0.0035 | 90 | 22 |
| 215 | Eckaus, David | EVA_OTT | Slider | LHH | 119 | 56.8 | 61.1 | 58.1 | 86.5 | 0.0117 | 91 | 23 |
| 216 | Harris, Everette | TRI_VAL | Slider | LHH | 29 | 56.3 | 62.0 | 58.0 | 86.4 | 0.0122 | 92 | 24 |
| 228 | Odonnell, Brendan | NEW_ENG23 | Slider | LHH | 91 | 58.3 | 56.2 | 57.6 | 85.6 | 0.0088 | 93 | 25 |

### Slider vs RHH

| Rank | Pitcher | Team | Pitch Type | Batter Side | Split Pitches | PVS | Loc | Final | Final % | Avg Loc Adv | Type Rank | Type/Side Rank |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | Ryan, Dillon | NEW_ENG23 | Slider | RHH | 61 | 79.9 | 72.2 | 77.6 | 100.0 | 0.0183 | 1 | 1 |
| 2 | Vecerka, Boris | QUE_CAP | Slider | RHH | 62 | 80.0 | 60.9 | 74.3 | 99.9 | 0.0116 | 2 | 2 |
| 3 | Kirby, Zach | WAS_WIL3 | Slider | RHH | 126 | 71.6 | 80.0 | 74.2 | 99.9 | 0.0234 | 3 | 3 |
| 4 | Bargo, Casey | NEW_ENG23 | Slider | RHH | 29 | 73.5 | 75.0 | 73.9 | 99.8 | 0.0199 | 4 | 4 |
| 7 | Harper, Scott | NEW_YOR13 | Slider | RHH | 169 | 73.6 | 68.3 | 72.1 | 99.6 | 0.0160 | 5 | 5 |
| 13 | Bauer, Patrick | QUE_CAP | Slider | RHH | 45 | 74.4 | 62.8 | 70.9 | 99.2 | 0.0127 | 8 | 6 |
| 18 | Duncan, Tanner | DOW_EAS1 | Slider | RHH | 38 | 68.9 | 69.9 | 69.2 | 98.9 | 0.0169 | 11 | 7 |
| 19 | Hickey, Matt | GAT_GRI | Slider | RHH | 72 | 70.5 | 65.7 | 69.1 | 98.9 | 0.0144 | 12 | 8 |
| 22 | Nakata, Yuto | QUE_CAP | Slider | RHH | 99 | 68.9 | 68.2 | 68.7 | 98.7 | 0.0159 | 13 | 9 |
| 25 | Morrissey, Joe | EVA_OTT | Slider | RHH | 47 | 62.8 | 80.0 | 67.9 | 98.5 | 0.0234 | 14 | 10 |
| 28 | Donnan, Blake | FLO_Y'A | Slider | RHH | 52 | 70.0 | 62.2 | 67.6 | 98.3 | 0.0123 | 16 | 11 |
| 29 | Barraza, Chris | MIS_MUD | Slider | RHH | 36 | 63.2 | 76.9 | 67.4 | 98.2 | 0.0211 | 17 | 12 |
| 31 | Vega, Lucas | TRO_AIG | Slider | RHH | 94 | 66.6 | 67.2 | 66.8 | 98.1 | 0.0153 | 18 | 13 |
| 35 | O'Hanlon, Michael | WAS_WIL3 | Slider | RHH | 54 | 60.5 | 80.0 | 66.4 | 97.8 | 0.0232 | 20 | 14 |
| 37 | Leduc, Zachary | TRO_AIG | Slider | RHH | 49 | 71.7 | 53.0 | 66.1 | 97.7 | 0.0069 | 21 | 15 |
| 38 | Perozzi, John | SUS_COU1 | Slider | RHH | 64 | 64.7 | 68.8 | 65.9 | 97.7 | 0.0162 | 22 | 16 |
| 39 | Jones, Logan | TRI_VAL | Slider | RHH | 32 | 74.7 | 44.7 | 65.7 | 97.6 | 0.0019 | 23 | 17 |
| 40 | Moore, Kyle | SCH_BOO | Slider | RHH | 36 | 63.5 | 70.4 | 65.6 | 97.5 | 0.0172 | 24 | 18 |
| 41 | Petschke, Ben | EVA_OTT | Slider | RHH | 86 | 64.5 | 67.0 | 65.3 | 97.5 | 0.0152 | 25 | 19 |
| 43 | Morin, Jacob | QUE_CAP | Slider | RHH | 60 | 65.7 | 63.2 | 64.9 | 97.3 | 0.0129 | 27 | 20 |
| 44 | Alpern, Liam | FLO_Y'A | Slider | RHH | 40 | 76.3 | 37.7 | 64.7 | 97.3 | -0.0022 | 28 | 21 |
| 47 | Vail, Tyler | NEW_YOR13 | Slider | RHH | 148 | 62.8 | 68.2 | 64.4 | 97.1 | 0.0159 | 29 | 22 |
| 49 | Leak, Anthony | NEW_YOR13 | Slider | RHH | 177 | 59.1 | 76.3 | 64.2 | 97.0 | 0.0207 | 30 | 23 |
| 52 | Allemann, Braeden | QUE_CAP | Slider | RHH | 73 | 58.0 | 78.1 | 64.1 | 96.8 | 0.0218 | 31 | 24 |
| 55 | Garcia, Hector | WAS_WIL3 | Slider | RHH | 36 | 57.1 | 80.0 | 64.0 | 96.6 | 0.0307 | 33 | 25 |

### Splitter vs LHH

| Rank | Pitcher | Team | Pitch Type | Batter Side | Split Pitches | PVS | Loc | Final | Final % | Avg Loc Adv | Type Rank | Type/Side Rank |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 45 | Garcia, Hector | WAS_WIL3 | Splitter | LHH | 59 | 73.6 | 43.3 | 64.5 | 97.2 | 0.0011 | 1 | 1 |
| 66 | Soto, Carlos | JOL_SLA | Splitter | LHH | 31 | 71.0 | 45.2 | 63.2 | 95.9 | 0.0022 | 2 | 2 |
| 110 | Coles, Chad | WAS_WIL3 | Splitter | LHH | 38 | 67.5 | 46.6 | 61.3 | 93.1 | 0.0031 | 3 | 3 |
| 193 | Pindel, Buddie | SCH_BOO | Splitter | LHH | 58 | 65.1 | 43.8 | 58.7 | 87.9 | 0.0014 | 7 | 4 |
| 195 | Shears, Tanner | SCH_BOO | Splitter | LHH | 37 | 66.0 | 41.5 | 58.7 | 87.7 | 0.0000 | 8 | 5 |
| 210 | Villers, Ian | QUE_CAP | Splitter | LHH | 39 | 65.1 | 42.3 | 58.3 | 86.8 | 0.0005 | 10 | 6 |
| 220 | Vitas, Ben | JOL_SLA | Splitter | LHH | 91 | 63.7 | 44.1 | 57.8 | 86.1 | 0.0016 | 11 | 7 |
| 414 | Williams, Brian | MIS_MUD | Splitter | LHH | 57 | 58.2 | 44.6 | 54.1 | 73.9 | 0.0019 | 13 | 8 |
| 447 | Thornton, Tyler | NEW_ENG23 | Splitter | LHH | 69 | 57.0 | 45.3 | 53.5 | 71.8 | 0.0023 | 14 | 9 |
| 579 | Salata, Derek | SCH_BOO | Splitter | LHH | 90 | 55.3 | 44.1 | 51.9 | 63.4 | 0.0016 | 17 | 10 |
| 608 | Thompson, Ross | SCH_BOO | Splitter | LHH | 145 | 55.1 | 43.4 | 51.6 | 61.6 | 0.0011 | 18 | 11 |
| 1355 | Gilleran, Jimmy | NEW_ENG23 | Splitter | LHH | 36 | 42.1 | 41.3 | 41.9 | 14.4 | -0.0001 | 20 | 12 |
| 1400 | Nakata, Yuto | QUE_CAP | Splitter | LHH | 82 | 42.6 | 37.7 | 41.1 | 11.5 | -0.0022 | 22 | 13 |
| 1446 | Eldred, Zach | NEW_ENG23 | Splitter | LHH | 46 | 37.3 | 46.4 | 40.0 | 8.6 | 0.0029 | 23 | 14 |
| 1533 | Duby, Bill | NEW_JER6 | Splitter | LHH | 45 | 34.9 | 40.4 | 36.6 | 3.1 | -0.0006 | 25 | 15 |
| 1564 | Andueza, Axel | DOW_EAS1 | Splitter | LHH | 70 | 28.3 | 41.4 | 32.2 | 1.1 | -0.0000 | 27 | 16 |

### Splitter vs RHH

| Rank | Pitcher | Team | Pitch Type | Batter Side | Split Pitches | PVS | Loc | Final | Final % | Avg Loc Adv | Type Rank | Type/Side Rank |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 156 | Coles, Chad | WAS_WIL3 | Splitter | RHH | 25 | 67.5 | 41.2 | 59.6 | 90.2 | -0.0001 | 4 | 1 |
| 175 | Villers, Ian | QUE_CAP | Splitter | RHH | 25 | 65.1 | 45.6 | 59.3 | 89.0 | 0.0025 | 5 | 2 |
| 189 | Pindel, Buddie | SCH_BOO | Splitter | RHH | 32 | 65.1 | 44.2 | 58.8 | 88.1 | 0.0016 | 6 | 3 |
| 198 | Shears, Tanner | SCH_BOO | Splitter | RHH | 37 | 66.0 | 41.0 | 58.5 | 87.5 | -0.0002 | 9 | 4 |
| 285 | Vitas, Ben | JOL_SLA | Splitter | RHH | 36 | 63.7 | 39.3 | 56.4 | 82.0 | -0.0012 | 12 | 5 |
| 468 | Williams, Brian | MIS_MUD | Splitter | RHH | 44 | 58.2 | 41.7 | 53.2 | 70.5 | 0.0001 | 15 | 6 |
| 576 | Thornton, Tyler | NEW_ENG23 | Splitter | RHH | 50 | 57.0 | 40.0 | 51.9 | 63.6 | -0.0008 | 16 | 7 |
| 824 | Thompson, Ross | SCH_BOO | Splitter | RHH | 30 | 55.1 | 34.7 | 49.0 | 47.9 | -0.0040 | 19 | 8 |
| 1393 | Nakata, Yuto | QUE_CAP | Splitter | RHH | 32 | 42.6 | 38.1 | 41.2 | 12.0 | -0.0020 | 21 | 9 |
| 1500 | Eldred, Zach | NEW_ENG23 | Splitter | RHH | 35 | 37.3 | 41.1 | 38.4 | 5.2 | -0.0002 | 24 | 10 |
| 1561 | Andueza, Axel | DOW_EAS1 | Splitter | RHH | 26 | 28.3 | 41.9 | 32.4 | 1.3 | 0.0003 | 26 | 11 |

### Sweeper vs RHH

| Rank | Pitcher | Team | Pitch Type | Batter Side | Split Pitches | PVS | Loc | Final | Final % | Avg Loc Adv | Type Rank | Type/Side Rank |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 245 | Cerda, Junior | EVA_OTT | Sweeper | RHH | 41 | 64.2 | 41.4 | 57.4 | 84.6 | -0.0000 | 1 | 1 |
