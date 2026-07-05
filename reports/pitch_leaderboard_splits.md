# Handedness-Specific Pitch Leaderboards

- Pitch Value input: `data\processed\pitch_value_scores_with_type_rank.csv` (744 rows)
- Location Score input: `data\processed\location_scores.csv` (1,558 rows)
- Split component input: `data\processed\2026-data-with-woba-xwoba.parquet`
- Output file: `data\processed\pitch_leaderboard_splits.csv`
- Joined leaderboard rows: 1,323
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
| 1 | Vecerka, Boris | QUE_CAP | Slider | RHH | 48 | 80.0 | 63.7 | 75.1 | 100.0 | 0.0117 | 1 | 1 |
| 2 | Ryan, Dillon | NEW_ENG23 | Slider | RHH | 54 | 79.2 | 63.0 | 74.4 | 99.9 | 0.0113 | 2 | 2 |
| 3 | Harper, Scott | NEW_YOR13 | Slider | RHH | 143 | 76.7 | 67.5 | 74.0 | 99.8 | 0.0138 | 3 | 3 |
| 4 | Kirby, Zach | WAS_WIL3 | Slider | RHH | 126 | 70.9 | 80.0 | 73.6 | 99.8 | 0.0211 | 4 | 4 |
| 5 | Bargo, Casey | NEW_ENG23 | Slider | RHH | 29 | 72.8 | 73.7 | 73.0 | 99.7 | 0.0173 | 5 | 5 |
| 6 | Moore, Kyle | SCH_BOO | Slider | RHH | 31 | 70.4 | 77.5 | 72.5 | 99.6 | 0.0194 | 6 | 6 |
| 7 | Grounds, Jackson | DOW_EAS1 | Curveball | RHH | 43 | 80.0 | 54.8 | 72.5 | 99.5 | 0.0067 | 1 | 1 |
| 8 | Grounds, Jackson | DOW_EAS1 | Four-Seam | RHH | 48 | 73.5 | 69.3 | 72.2 | 99.5 | 0.0149 | 1 | 1 |
| 9 | Lawson, Nathan | FLO_Y'A | Changeup | LHH | 33 | 77.0 | 60.6 | 72.0 | 99.4 | 0.0099 | 1 | 1 |
| 10 | Morgan, Cooper | QUE_CAP | Curveball | LHH | 44 | 80.0 | 53.3 | 72.0 | 99.3 | 0.0059 | 2 | 1 |
| 11 | Alpern, Liam | FLO_Y'A | Slider | LHH | 38 | 75.5 | 61.8 | 71.4 | 99.2 | 0.0106 | 7 | 1 |
| 12 | Carroll, Jake | JOL_SLA | Slider | LHH | 46 | 80.0 | 49.8 | 70.9 | 99.2 | 0.0039 | 8 | 2 |
| 13 | Davis, Tyler | WIN_CIT29 | Four-Seam | RHH | 33 | 73.6 | 64.2 | 70.8 | 99.1 | 0.0120 | 2 | 2 |
| 14 | Ryan, Dillon | NEW_ENG23 | Slider | LHH | 59 | 79.2 | 48.5 | 70.0 | 99.0 | 0.0032 | 9 | 3 |
| 15 | Cameron, Zach | WIN_CIT29 | Four-Seam | RHH | 50 | 70.9 | 67.1 | 69.8 | 98.9 | 0.0136 | 3 | 3 |
| 16 | Rodriguez, Joe Joe | NEW_JER6 | Changeup | LHH | 59 | 74.8 | 58.1 | 69.8 | 98.9 | 0.0085 | 2 | 2 |
| 17 | Grounds, Jackson | DOW_EAS1 | Curveball | LHH | 39 | 80.0 | 45.0 | 69.5 | 98.8 | 0.0012 | 3 | 2 |
| 18 | Peyton, Blake | GAT_GRI | Changeup | RHH | 84 | 76.4 | 52.7 | 69.2 | 98.7 | 0.0055 | 3 | 1 |
| 19 | Escobar, Anthony | TRO_AIG | Changeup | LHH | 100 | 72.0 | 61.9 | 69.0 | 98.6 | 0.0107 | 4 | 3 |
| 20 | Harper, Scott | NEW_YOR13 | Slider | LHH | 31 | 76.7 | 50.9 | 69.0 | 98.6 | 0.0045 | 10 | 4 |
| 21 | McEvoy, Aidan | FLO_Y'A | Slider | LHH | 65 | 71.7 | 62.6 | 68.9 | 98.5 | 0.0111 | 11 | 5 |
| 22 | Grounds, Jackson | DOW_EAS1 | Four-Seam | LHH | 59 | 73.5 | 58.0 | 68.8 | 98.4 | 0.0085 | 4 | 1 |
| 23 | Hickey, Matt | GAT_GRI | Slider | RHH | 63 | 67.6 | 70.5 | 68.5 | 98.3 | 0.0155 | 12 | 7 |
| 24 | Serrano, Elio | NEW_JER6 | Changeup | LHH | 49 | 74.3 | 54.1 | 68.2 | 98.3 | 0.0063 | 5 | 4 |
| 25 | Jones, Logan | TRI_VAL | Slider | LHH | 33 | 73.7 | 53.0 | 67.5 | 98.2 | 0.0057 | 13 | 6 |
| 26 | Donnan, Blake | FLO_Y'A | Slider | RHH | 52 | 69.2 | 63.4 | 67.5 | 98.1 | 0.0115 | 14 | 8 |
| 27 | Toribio, Noe | TRO_AIG | Slider | RHH | 89 | 69.7 | 60.7 | 67.0 | 98.0 | 0.0100 | 15 | 9 |
| 28 | Nakata, Yuto | QUE_CAP | Slider | RHH | 83 | 69.8 | 59.8 | 66.8 | 98.0 | 0.0095 | 16 | 10 |
| 29 | Vega, Lucas | TRO_AIG | Slider | RHH | 84 | 66.0 | 67.4 | 66.4 | 97.9 | 0.0138 | 17 | 11 |
| 30 | Hagan, Jack | DOW_EAS1 | Slider | RHH | 118 | 62.2 | 75.2 | 66.1 | 97.8 | 0.0182 | 18 | 12 |
| 31 | Davis, Tyler | WIN_CIT29 | Four-Seam | LHH | 43 | 73.6 | 47.9 | 65.9 | 97.7 | 0.0028 | 5 | 2 |
| 32 | Perozzi, John | SUS_COU1 | Slider | RHH | 62 | 64.1 | 69.4 | 65.7 | 97.7 | 0.0149 | 19 | 13 |
| 33 | O'Hanlon, Michael | WAS_WIL3 | Slider | RHH | 45 | 61.8 | 74.6 | 65.6 | 97.6 | 0.0178 | 20 | 14 |
| 34 | Sesar, Jorden | SUS_COU1 | Changeup | LHH | 47 | 69.1 | 55.9 | 65.2 | 97.5 | 0.0073 | 6 | 5 |
| 35 | Jones, Logan | TRI_VAL | Slider | RHH | 32 | 73.7 | 45.1 | 65.1 | 97.4 | 0.0013 | 21 | 15 |
| 36 | Petschke, Ben | EVA_OTT | Slider | RHH | 84 | 63.9 | 68.0 | 65.1 | 97.4 | 0.0141 | 22 | 16 |
| 37 | Morin, Jacob | QUE_CAP | Slider | RHH | 60 | 65.1 | 65.0 | 65.1 | 97.3 | 0.0124 | 23 | 17 |
| 38 | Harajli, Ahmad | FLO_Y'A | Slider | RHH | 49 | 65.0 | 64.8 | 64.9 | 97.2 | 0.0123 | 24 | 18 |
| 39 | Leak, Anthony | NEW_YOR13 | Slider | RHH | 131 | 58.5 | 79.8 | 64.9 | 97.1 | 0.0207 | 25 | 19 |
| 40 | Vailes, Gage | GAT_GRI | Slider | RHH | 177 | 58.3 | 80.0 | 64.8 | 97.1 | 0.0216 | 26 | 20 |

## Pitch Type + Batter Side Leaderboards

### Changeup vs LHH

| Rank | Pitcher | Team | Pitch Type | Batter Side | Split Pitches | PVS | Loc | Final | Final % | Avg Loc Adv | Type Rank | Type/Side Rank |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 9 | Lawson, Nathan | FLO_Y'A | Changeup | LHH | 33 | 77.0 | 60.6 | 72.0 | 99.4 | 0.0099 | 1 | 1 |
| 16 | Rodriguez, Joe Joe | NEW_JER6 | Changeup | LHH | 59 | 74.8 | 58.1 | 69.8 | 98.9 | 0.0085 | 2 | 2 |
| 19 | Escobar, Anthony | TRO_AIG | Changeup | LHH | 100 | 72.0 | 61.9 | 69.0 | 98.6 | 0.0107 | 4 | 3 |
| 24 | Serrano, Elio | NEW_JER6 | Changeup | LHH | 49 | 74.3 | 54.1 | 68.2 | 98.3 | 0.0063 | 5 | 4 |
| 34 | Sesar, Jorden | SUS_COU1 | Changeup | LHH | 47 | 69.1 | 55.9 | 65.2 | 97.5 | 0.0073 | 6 | 5 |
| 48 | Hocom, Quinn | TRI_VAL | Changeup | LHH | 52 | 66.0 | 60.0 | 64.2 | 96.4 | 0.0096 | 7 | 6 |
| 49 | Maietta, Dante | WIN_CIT29 | Changeup | LHH | 114 | 63.8 | 64.9 | 64.1 | 96.4 | 0.0123 | 8 | 7 |
| 51 | Harris, Everette | TRI_VAL | Changeup | LHH | 56 | 69.0 | 51.6 | 63.8 | 96.2 | 0.0049 | 9 | 8 |
| 62 | Leak, Anthony | NEW_YOR13 | Changeup | LHH | 51 | 62.9 | 63.6 | 63.1 | 95.4 | 0.0116 | 10 | 9 |
| 77 | Parsons, Billy | SUS_COU1 | Changeup | LHH | 43 | 67.8 | 48.7 | 62.1 | 94.3 | 0.0033 | 12 | 10 |
| 80 | Drakeford, Dosie | NEW_JER6 | Changeup | LHH | 54 | 66.0 | 52.6 | 62.0 | 94.0 | 0.0055 | 13 | 11 |
| 81 | Cooper, Garrett | NEW_YOR13 | Changeup | LHH | 114 | 63.8 | 57.5 | 61.9 | 94.0 | 0.0082 | 14 | 12 |
| 100 | Smith, Jackson | MIS_MUD | Changeup | LHH | 51 | 56.3 | 73.1 | 61.4 | 92.5 | 0.0170 | 15 | 13 |
| 112 | Tokar, Heitor | OTT_TIT | Changeup | LHH | 33 | 66.7 | 45.8 | 60.4 | 91.6 | 0.0017 | 17 | 14 |
| 119 | Willeman, Landon | EVA_OTT | Changeup | LHH | 108 | 61.0 | 58.1 | 60.1 | 91.1 | 0.0085 | 19 | 15 |
| 123 | Henderson, Drew | DOW_EAS1 | Changeup | LHH | 83 | 59.1 | 62.1 | 60.0 | 90.8 | 0.0108 | 21 | 16 |
| 128 | Hensey, Rob | SUS_COU1 | Changeup | LHH | 38 | 59.1 | 61.6 | 59.9 | 90.4 | 0.0105 | 23 | 17 |
| 140 | Dill, Austin | TRI_VAL | Changeup | LHH | 107 | 55.2 | 69.6 | 59.5 | 89.5 | 0.0150 | 24 | 18 |
| 173 | Wiltse, Ryan | EVA_OTT | Changeup | LHH | 88 | 63.7 | 46.4 | 58.5 | 87.0 | 0.0020 | 26 | 19 |
| 184 | Miner, Jace | DOW_EAS1 | Changeup | LHH | 25 | 65.7 | 40.4 | 58.1 | 86.2 | -0.0014 | 27 | 20 |
| 201 | Whitesell, Max | FLO_Y'A | Changeup | LHH | 38 | 55.6 | 62.0 | 57.5 | 84.9 | 0.0108 | 32 | 21 |
| 215 | Plumadore, Carson | WIN_CIT29 | Changeup | LHH | 152 | 57.8 | 56.0 | 57.3 | 83.8 | 0.0074 | 34 | 22 |
| 252 | Cameron, Zach | WIN_CIT29 | Changeup | LHH | 118 | 56.0 | 56.8 | 56.2 | 81.0 | 0.0078 | 37 | 23 |
| 255 | Morel, Yohanse | OTT_TIT | Changeup | LHH | 50 | 54.4 | 60.1 | 56.1 | 80.8 | 0.0097 | 38 | 24 |
| 281 | Pardinho, Eric | OTT_TIT | Changeup | LHH | 85 | 54.9 | 56.8 | 55.5 | 78.8 | 0.0078 | 40 | 25 |

### Changeup vs RHH

| Rank | Pitcher | Team | Pitch Type | Batter Side | Split Pitches | PVS | Loc | Final | Final % | Avg Loc Adv | Type Rank | Type/Side Rank |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 18 | Peyton, Blake | GAT_GRI | Changeup | RHH | 84 | 76.4 | 52.7 | 69.2 | 98.7 | 0.0055 | 3 | 1 |
| 69 | Harris, Everette | TRI_VAL | Changeup | RHH | 40 | 69.0 | 47.5 | 62.5 | 94.9 | 0.0026 | 11 | 2 |
| 111 | Miner, Jace | DOW_EAS1 | Changeup | RHH | 53 | 65.7 | 48.2 | 60.5 | 91.7 | 0.0030 | 16 | 3 |
| 113 | Wiltse, Ryan | EVA_OTT | Changeup | RHH | 32 | 63.7 | 52.7 | 60.4 | 91.5 | 0.0055 | 18 | 4 |
| 121 | Messina, Chris | FDU_KNI | Changeup | RHH | 52 | 65.8 | 46.6 | 60.1 | 90.9 | 0.0021 | 20 | 5 |
| 126 | Maietta, Dante | WIN_CIT29 | Changeup | RHH | 77 | 63.8 | 51.1 | 60.0 | 90.6 | 0.0046 | 22 | 6 |
| 153 | Cooper, Garrett | NEW_YOR13 | Changeup | RHH | 84 | 63.8 | 48.2 | 59.1 | 88.5 | 0.0030 | 25 | 7 |
| 190 | Campbell, Tyler | MIS_MUD | Changeup | RHH | 45 | 57.1 | 60.0 | 58.0 | 85.7 | 0.0096 | 28 | 8 |
| 191 | Morgan, Cooper | QUE_CAP | Changeup | RHH | 52 | 65.9 | 39.4 | 57.9 | 85.6 | -0.0019 | 29 | 9 |
| 193 | Gollert, Harley | TRO_AIG | Changeup | RHH | 93 | 56.1 | 62.0 | 57.8 | 85.5 | 0.0107 | 30 | 10 |
| 196 | Rohde, Isaac | NEW_YOR13 | Changeup | RHH | 505 | 59.0 | 54.5 | 57.7 | 85.3 | 0.0066 | 31 | 11 |
| 213 | Tokar, Heitor | OTT_TIT | Changeup | RHH | 30 | 66.7 | 35.4 | 57.3 | 84.0 | -0.0042 | 33 | 12 |
| 224 | Henderson, Drew | DOW_EAS1 | Changeup | RHH | 43 | 59.1 | 52.4 | 57.1 | 83.1 | 0.0054 | 35 | 13 |
| 243 | Willeman, Landon | EVA_OTT | Changeup | RHH | 46 | 61.0 | 46.3 | 56.6 | 81.7 | 0.0019 | 36 | 14 |
| 280 | Foster, Kobe | WAS_WIL3 | Changeup | RHH | 146 | 59.1 | 47.1 | 55.5 | 78.9 | 0.0024 | 39 | 15 |
| 300 | Brothers, Kellen | SUS_COU1 | Changeup | RHH | 29 | 55.5 | 54.3 | 55.2 | 77.4 | 0.0064 | 42 | 16 |
| 319 | Galva, Claudio | GAT_GRI | Changeup | RHH | 64 | 53.4 | 58.3 | 54.9 | 76.0 | 0.0086 | 46 | 17 |
| 321 | Hensey, Rob | SUS_COU1 | Changeup | RHH | 188 | 59.1 | 44.8 | 54.8 | 75.8 | 0.0011 | 47 | 18 |
| 324 | Barreto, Brayhans | TRI_VAL | Changeup | RHH | 85 | 57.4 | 48.7 | 54.8 | 75.6 | 0.0033 | 49 | 19 |
| 365 | Boies, Emiles | QUE_CAP | Changeup | RHH | 45 | 57.7 | 45.1 | 53.9 | 72.5 | 0.0013 | 52 | 20 |
| 373 | VanMarter, Luke | LEM_COL | Changeup | RHH | 29 | 58.6 | 42.5 | 53.8 | 71.9 | -0.0002 | 53 | 21 |
| 398 | Plumadore, Carson | WIN_CIT29 | Changeup | RHH | 57 | 57.8 | 42.6 | 53.3 | 70.0 | -0.0001 | 55 | 22 |
| 407 | Vail, Tyler | NEW_YOR13 | Changeup | RHH | 153 | 55.4 | 48.0 | 53.2 | 69.3 | 0.0029 | 56 | 23 |
| 430 | Roland, Cole | QUE_CAP | Changeup | RHH | 33 | 53.7 | 49.9 | 52.6 | 67.6 | 0.0040 | 58 | 24 |
| 454 | Toribio, Noe | TRO_AIG | Changeup | RHH | 43 | 52.1 | 52.5 | 52.3 | 65.8 | 0.0054 | 61 | 25 |

### Curveball vs LHH

| Rank | Pitcher | Team | Pitch Type | Batter Side | Split Pitches | PVS | Loc | Final | Final % | Avg Loc Adv | Type Rank | Type/Side Rank |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 10 | Morgan, Cooper | QUE_CAP | Curveball | LHH | 44 | 80.0 | 53.3 | 72.0 | 99.3 | 0.0059 | 2 | 1 |
| 17 | Grounds, Jackson | DOW_EAS1 | Curveball | LHH | 39 | 80.0 | 45.0 | 69.5 | 98.8 | 0.0012 | 3 | 2 |
| 110 | Eisenbarger, Jack | QUE_CAP | Curveball | LHH | 46 | 66.4 | 47.0 | 60.5 | 91.8 | 0.0023 | 11 | 3 |
| 133 | Garcia, Brett | OTT_TIT | Curveball | LHH | 44 | 66.1 | 44.4 | 59.6 | 90.0 | 0.0009 | 12 | 4 |
| 138 | Salata, Derek | SCH_BOO | Curveball | LHH | 27 | 66.0 | 44.5 | 59.6 | 89.6 | 0.0009 | 13 | 5 |
| 152 | Binns, Malik | NEW_JER6 | Curveball | LHH | 27 | 65.6 | 44.0 | 59.1 | 88.6 | 0.0006 | 14 | 6 |
| 170 | Harris, Ben | GAT_GRI | Curveball | LHH | 72 | 65.7 | 42.4 | 58.7 | 87.2 | -0.0003 | 16 | 7 |
| 192 | Bohnert, Matthew | WIN_CIT29 | Curveball | LHH | 40 | 64.0 | 43.6 | 57.9 | 85.6 | 0.0004 | 18 | 8 |
| 206 | Heredia-Bustos, Rolando | DOW_EAS1 | Curveball | LHH | 29 | 62.7 | 45.1 | 57.4 | 84.5 | 0.0013 | 19 | 9 |
| 209 | Maryniak, Connor | NEW_JER6 | Curveball | LHH | 62 | 61.8 | 46.9 | 57.4 | 84.3 | 0.0023 | 20 | 10 |
| 242 | Hill, Kaleb | OTT_TIT | Curveball | LHH | 106 | 63.4 | 40.6 | 56.6 | 81.8 | -0.0013 | 24 | 11 |
| 266 | Simpson, Garret | EVA_OTT | Curveball | LHH | 57 | 62.3 | 40.9 | 55.9 | 80.0 | -0.0011 | 29 | 12 |
| 271 | Earwood, Micah | SUS_COU1 | Curveball | LHH | 44 | 60.1 | 45.7 | 55.8 | 79.6 | 0.0016 | 30 | 13 |
| 307 | Wiltse, Ryan | EVA_OTT | Curveball | LHH | 89 | 59.4 | 44.8 | 55.0 | 76.9 | 0.0011 | 35 | 14 |
| 315 | Peters, Garrett | NEW_YOR13 | Curveball | LHH | 87 | 56.5 | 51.3 | 54.9 | 76.3 | 0.0047 | 37 | 15 |
| 372 | De Los Santos, Enmanuel | NEW_ENG23 | Curveball | LHH | 45 | 57.8 | 44.5 | 53.8 | 72.0 | 0.0009 | 39 | 16 |
| 375 | Sesar, Jorden | SUS_COU1 | Curveball | LHH | 30 | 56.0 | 48.6 | 53.8 | 71.7 | 0.0032 | 40 | 17 |
| 426 | Lefebvre, Charles | TRO_AIG | Curveball | LHH | 45 | 56.9 | 42.8 | 52.6 | 67.9 | -0.0000 | 46 | 18 |
| 445 | Langrell, Connor | MIS_MUD | Curveball | LHH | 48 | 50.5 | 56.7 | 52.4 | 66.4 | 0.0077 | 47 | 19 |
| 448 | Petschke, Ben | EVA_OTT | Curveball | LHH | 85 | 56.3 | 43.1 | 52.3 | 66.2 | 0.0001 | 48 | 20 |
| 462 | Noriega, Branden | LAK_ERI24 | Curveball | LHH | 40 | 53.4 | 49.4 | 52.2 | 65.2 | 0.0036 | 49 | 21 |
| 497 | Sanchez, Edwin | LAK_ERI24 | Curveball | LHH | 33 | 52.6 | 49.5 | 51.7 | 62.5 | 0.0037 | 53 | 22 |
| 512 | Anibal, Trevor | NEW_ENG23 | Curveball | LHH | 45 | 58.6 | 34.9 | 51.4 | 61.4 | -0.0045 | 56 | 23 |
| 534 | Kirby, Zach | WAS_WIL3 | Curveball | LHH | 53 | 56.1 | 39.5 | 51.1 | 59.7 | -0.0019 | 58 | 24 |
| 541 | Cook, Cole | SCH_BOO | Curveball | LHH | 38 | 55.7 | 39.6 | 50.9 | 59.2 | -0.0018 | 59 | 25 |

### Curveball vs RHH

| Rank | Pitcher | Team | Pitch Type | Batter Side | Split Pitches | PVS | Loc | Final | Final % | Avg Loc Adv | Type Rank | Type/Side Rank |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 7 | Grounds, Jackson | DOW_EAS1 | Curveball | RHH | 43 | 80.0 | 54.8 | 72.5 | 99.5 | 0.0067 | 1 | 1 |
| 57 | Sechrist, Zander | WAS_WIL3 | Curveball | RHH | 46 | 67.7 | 53.0 | 63.3 | 95.8 | 0.0057 | 4 | 2 |
| 60 | Simpson, Garret | EVA_OTT | Curveball | RHH | 37 | 62.3 | 65.2 | 63.1 | 95.5 | 0.0126 | 5 | 3 |
| 66 | Salata, Derek | SCH_BOO | Curveball | RHH | 56 | 66.0 | 54.8 | 62.7 | 95.1 | 0.0067 | 6 | 4 |
| 71 | Maryniak, Connor | NEW_JER6 | Curveball | RHH | 59 | 61.8 | 63.7 | 62.4 | 94.7 | 0.0117 | 7 | 5 |
| 75 | Binns, Malik | NEW_JER6 | Curveball | RHH | 28 | 65.6 | 54.1 | 62.1 | 94.4 | 0.0063 | 8 | 6 |
| 91 | Garcia, Brett | OTT_TIT | Curveball | RHH | 60 | 66.1 | 51.1 | 61.6 | 93.2 | 0.0046 | 9 | 7 |
| 97 | Harris, Ben | GAT_GRI | Curveball | RHH | 133 | 65.7 | 51.8 | 61.5 | 92.7 | 0.0050 | 10 | 8 |
| 154 | Eisenbarger, Jack | QUE_CAP | Curveball | RHH | 25 | 66.4 | 42.0 | 59.0 | 88.4 | -0.0005 | 15 | 9 |
| 182 | Hill, Kaleb | OTT_TIT | Curveball | RHH | 95 | 63.4 | 46.1 | 58.2 | 86.3 | 0.0018 | 17 | 10 |
| 219 | Wiltse, Ryan | EVA_OTT | Curveball | RHH | 27 | 59.4 | 52.1 | 57.2 | 83.5 | 0.0052 | 21 | 11 |
| 221 | Anibal, Trevor | NEW_ENG23 | Curveball | RHH | 54 | 58.6 | 53.9 | 57.1 | 83.4 | 0.0062 | 22 | 12 |
| 231 | Gollert, Harley | TRO_AIG | Curveball | RHH | 35 | 59.8 | 50.0 | 56.9 | 82.6 | 0.0040 | 23 | 13 |
| 253 | Earwood, Micah | SUS_COU1 | Curveball | RHH | 38 | 60.1 | 47.0 | 56.2 | 81.0 | 0.0023 | 25 | 14 |
| 254 | Bohnert, Matthew | WIN_CIT29 | Curveball | RHH | 43 | 64.0 | 37.8 | 56.2 | 80.9 | -0.0028 | 26 | 15 |
| 259 | Scafidi, Christian | LAK_ERI24 | Curveball | RHH | 34 | 60.5 | 45.4 | 56.0 | 80.5 | 0.0014 | 27 | 16 |
| 261 | Lefebvre, Charles | TRO_AIG | Curveball | RHH | 44 | 56.9 | 53.8 | 55.9 | 80.3 | 0.0061 | 28 | 17 |
| 272 | Petery, Dylan | WIN_CIT29 | Curveball | RHH | 44 | 60.5 | 44.6 | 55.8 | 79.5 | 0.0010 | 31 | 18 |
| 277 | Allemann, Braeden | QUE_CAP | Curveball | RHH | 108 | 53.8 | 59.8 | 55.6 | 79.1 | 0.0095 | 32 | 19 |
| 286 | Vail, Tyler | NEW_YOR13 | Curveball | RHH | 165 | 58.1 | 48.9 | 55.3 | 78.5 | 0.0034 | 33 | 20 |
| 288 | Boies, Emiles | QUE_CAP | Curveball | RHH | 41 | 55.7 | 54.4 | 55.3 | 78.3 | 0.0065 | 34 | 21 |
| 313 | Sesar, Jorden | SUS_COU1 | Curveball | RHH | 68 | 56.0 | 52.6 | 54.9 | 76.4 | 0.0054 | 36 | 22 |
| 352 | De Los Santos, Enmanuel | NEW_ENG23 | Curveball | RHH | 42 | 57.8 | 46.3 | 54.3 | 73.5 | 0.0019 | 38 | 23 |
| 384 | Petschke, Ben | EVA_OTT | Curveball | RHH | 79 | 56.3 | 47.1 | 53.5 | 71.1 | 0.0024 | 41 | 24 |
| 396 | Henderson, Drew | DOW_EAS1 | Curveball | RHH | 149 | 52.0 | 56.3 | 53.3 | 70.1 | 0.0075 | 42 | 25 |

### Cutter vs LHH

| Rank | Pitcher | Team | Pitch Type | Batter Side | Split Pitches | PVS | Loc | Final | Final % | Avg Loc Adv | Type Rank | Type/Side Rank |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 42 | Webster, Evan | FLO_Y'A | Cutter | LHH | 76 | 73.5 | 44.5 | 64.8 | 96.9 | 0.0009 | 1 | 1 |
| 76 | Correa, Nelvin | QUE_CAP | Cutter | LHH | 47 | 71.5 | 40.3 | 62.1 | 94.3 | -0.0014 | 5 | 2 |
| 166 | Parsons, Billy | SUS_COU1 | Cutter | LHH | 39 | 64.0 | 46.6 | 58.8 | 87.5 | 0.0021 | 6 | 3 |
| 263 | Majick, Eli | NEW_ENG23 | Cutter | LHH | 26 | 59.8 | 46.9 | 55.9 | 80.2 | 0.0023 | 9 | 4 |
| 317 | Bell, Brendan | NEW_ENG23 | Cutter | LHH | 38 | 59.8 | 43.6 | 54.9 | 76.1 | 0.0004 | 10 | 5 |
| 417 | Morgan, Marcus | JOL_SLA | Cutter | LHH | 38 | 56.8 | 43.9 | 52.9 | 68.6 | 0.0006 | 11 | 6 |
| 435 | Debban, Caleb | NEW_JER6 | Cutter | LHH | 58 | 56.1 | 44.1 | 52.5 | 67.2 | 0.0007 | 12 | 7 |
| 520 | Gorgen, Grady | NEW_YOR13 | Cutter | LHH | 33 | 55.0 | 42.8 | 51.3 | 60.8 | -0.0001 | 16 | 8 |
| 532 | McEvoy, Aidan | FLO_Y'A | Cutter | LHH | 36 | 51.9 | 49.5 | 51.2 | 59.9 | 0.0037 | 17 | 9 |
| 565 | Moore, Kyle | SCH_BOO | Cutter | LHH | 25 | 54.2 | 42.1 | 50.6 | 57.4 | -0.0004 | 19 | 10 |
| 567 | Smith, Jackson | MIS_MUD | Cutter | LHH | 39 | 53.7 | 43.2 | 50.6 | 57.2 | 0.0002 | 20 | 11 |
| 596 | Saturria, Michael | NEW_ENG23 | Cutter | LHH | 102 | 54.3 | 40.7 | 50.2 | 55.0 | -0.0012 | 21 | 12 |
| 639 | Campbell, Tyler | MIS_MUD | Cutter | LHH | 53 | 52.5 | 42.9 | 49.6 | 51.8 | 0.0000 | 23 | 13 |
| 750 | Langrell, Connor | MIS_MUD | Cutter | LHH | 100 | 49.3 | 44.5 | 47.8 | 43.4 | 0.0009 | 29 | 14 |
| 752 | Binns, Malik | NEW_JER6 | Cutter | LHH | 34 | 49.2 | 44.7 | 47.8 | 43.2 | 0.0010 | 30 | 15 |
| 840 | MacMillan, Blake | TRO_AIG | Cutter | LHH | 47 | 49.6 | 39.9 | 46.7 | 36.6 | -0.0017 | 35 | 16 |
| 854 | Gamelin, Shaun | JOL_SLA | Cutter | LHH | 56 | 48.5 | 42.0 | 46.5 | 35.5 | -0.0005 | 36 | 17 |
| 855 | Parks, Pavin | LAK_ERI24 | Cutter | LHH | 40 | 48.0 | 42.9 | 46.5 | 35.4 | 0.0000 | 37 | 18 |
| 907 | Petschke, Ben | EVA_OTT | Cutter | LHH | 146 | 44.9 | 47.7 | 45.8 | 31.5 | 0.0027 | 40 | 19 |
| 918 | Simpson, Garret | EVA_OTT | Cutter | LHH | 42 | 47.9 | 40.2 | 45.6 | 30.7 | -0.0015 | 41 | 20 |
| 994 | Ginn, Landon | WAS_WIL3 | Cutter | LHH | 42 | 45.6 | 42.3 | 44.6 | 24.9 | -0.0003 | 44 | 21 |
| 1020 | Cook, Cole | SCH_BOO | Cutter | LHH | 29 | 42.4 | 48.4 | 44.2 | 23.0 | 0.0031 | 45 | 22 |
| 1048 | Salata, Derek | SCH_BOO | Cutter | LHH | 47 | 43.1 | 44.9 | 43.6 | 20.9 | 0.0011 | 46 | 23 |
| 1145 | Morgan, Cooper | QUE_CAP | Cutter | LHH | 42 | 43.2 | 38.0 | 41.6 | 13.5 | -0.0027 | 50 | 24 |
| 1199 | Williams, Brian | MIS_MUD | Cutter | LHH | 47 | 40.1 | 41.3 | 40.4 | 9.4 | -0.0009 | 53 | 25 |

### Cutter vs RHH

| Rank | Pitcher | Team | Pitch Type | Batter Side | Split Pitches | PVS | Loc | Final | Final % | Avg Loc Adv | Type Rank | Type/Side Rank |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 47 | Correa, Nelvin | QUE_CAP | Cutter | RHH | 41 | 71.5 | 47.7 | 64.4 | 96.5 | 0.0027 | 2 | 1 |
| 72 | Valdez, Alex | EVA_OTT | Cutter | RHH | 43 | 67.9 | 49.0 | 62.3 | 94.6 | 0.0035 | 3 | 2 |
| 74 | Webster, Evan | FLO_Y'A | Cutter | RHH | 32 | 73.5 | 35.9 | 62.2 | 94.5 | -0.0039 | 4 | 3 |
| 225 | Majick, Eli | NEW_ENG23 | Cutter | RHH | 40 | 59.8 | 50.8 | 57.1 | 83.1 | 0.0044 | 7 | 4 |
| 226 | Bell, Brendan | NEW_ENG23 | Cutter | RHH | 25 | 59.8 | 50.8 | 57.1 | 83.0 | 0.0044 | 8 | 5 |
| 467 | Smith, Jackson | MIS_MUD | Cutter | RHH | 53 | 53.7 | 48.3 | 52.1 | 64.8 | 0.0031 | 13 | 6 |
| 473 | Debban, Caleb | NEW_JER6 | Cutter | RHH | 77 | 56.1 | 42.5 | 52.0 | 64.3 | -0.0002 | 14 | 7 |
| 492 | Gorgen, Grady | NEW_YOR13 | Cutter | RHH | 35 | 55.0 | 44.0 | 51.7 | 62.9 | 0.0007 | 15 | 8 |
| 546 | Saturria, Michael | NEW_ENG23 | Cutter | RHH | 107 | 54.3 | 42.6 | 50.8 | 58.8 | -0.0002 | 18 | 9 |
| 602 | McEvoy, Aidan | FLO_Y'A | Cutter | RHH | 37 | 51.9 | 45.9 | 50.1 | 54.6 | 0.0017 | 22 | 10 |
| 654 | Moore, Kyle | SCH_BOO | Cutter | RHH | 81 | 54.2 | 38.3 | 49.4 | 50.6 | -0.0026 | 24 | 11 |
| 700 | Binns, Malik | NEW_JER6 | Cutter | RHH | 54 | 49.2 | 47.6 | 48.7 | 47.2 | 0.0027 | 25 | 12 |
| 712 | Ginn, Landon | WAS_WIL3 | Cutter | RHH | 56 | 45.6 | 55.2 | 48.5 | 46.3 | 0.0069 | 26 | 13 |
| 729 | Campbell, Tyler | MIS_MUD | Cutter | RHH | 75 | 52.5 | 38.1 | 48.2 | 45.0 | -0.0027 | 27 | 14 |
| 737 | Parks, Pavin | LAK_ERI24 | Cutter | RHH | 94 | 48.0 | 48.1 | 48.1 | 44.4 | 0.0029 | 28 | 15 |
| 758 | Catrambone, Ben | JOL_SLA | Cutter | RHH | 34 | 49.0 | 45.0 | 47.8 | 42.8 | 0.0012 | 31 | 16 |
| 772 | Gamelin, Shaun | JOL_SLA | Cutter | RHH | 81 | 48.5 | 45.6 | 47.6 | 41.7 | 0.0015 | 32 | 17 |
| 778 | Langrell, Connor | MIS_MUD | Cutter | RHH | 132 | 49.3 | 43.3 | 47.5 | 41.3 | 0.0003 | 33 | 18 |
| 786 | Lovell, Justin | WIN_CIT29 | Cutter | RHH | 38 | 51.3 | 38.1 | 47.4 | 40.7 | -0.0027 | 34 | 19 |
| 894 | Petschke, Ben | EVA_OTT | Cutter | RHH | 103 | 44.9 | 48.5 | 46.0 | 32.5 | 0.0031 | 38 | 20 |
| 899 | MacMillan, Blake | TRO_AIG | Cutter | RHH | 72 | 49.6 | 37.3 | 45.9 | 32.1 | -0.0031 | 39 | 21 |
| 925 | Simpson, Garret | EVA_OTT | Cutter | RHH | 33 | 47.9 | 40.1 | 45.6 | 30.2 | -0.0015 | 42 | 22 |
| 933 | Salata, Derek | SCH_BOO | Cutter | RHH | 64 | 43.1 | 51.0 | 45.5 | 29.6 | 0.0046 | 43 | 23 |
| 1077 | Morgan, Cooper | QUE_CAP | Cutter | RHH | 38 | 43.2 | 43.1 | 43.2 | 18.7 | 0.0001 | 47 | 24 |
| 1119 | Thiels, Brenton | MIS_MUD | Cutter | RHH | 28 | 40.1 | 47.8 | 42.4 | 15.5 | 0.0028 | 48 | 25 |

### Four-Seam vs LHH

| Rank | Pitcher | Team | Pitch Type | Batter Side | Split Pitches | PVS | Loc | Final | Final % | Avg Loc Adv | Type Rank | Type/Side Rank |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 22 | Grounds, Jackson | DOW_EAS1 | Four-Seam | LHH | 59 | 73.5 | 58.0 | 68.8 | 98.4 | 0.0085 | 4 | 1 |
| 31 | Davis, Tyler | WIN_CIT29 | Four-Seam | LHH | 43 | 73.6 | 47.9 | 65.9 | 97.7 | 0.0028 | 5 | 2 |
| 61 | Foster, Kobe | WAS_WIL3 | Four-Seam | LHH | 133 | 61.3 | 67.4 | 63.1 | 95.5 | 0.0138 | 9 | 3 |
| 65 | Wehrle, Tyler | WIN_CIT29 | Four-Seam | LHH | 80 | 59.2 | 70.9 | 62.7 | 95.2 | 0.0157 | 10 | 4 |
| 85 | Cameron, Zach | WIN_CIT29 | Four-Seam | LHH | 48 | 70.9 | 40.6 | 61.8 | 93.7 | -0.0013 | 13 | 5 |
| 87 | Rodriguez, Joe Joe | NEW_JER6 | Four-Seam | LHH | 31 | 63.2 | 58.3 | 61.8 | 93.5 | 0.0087 | 14 | 6 |
| 131 | Zaffiro, Cole | SCH_BOO | Four-Seam | LHH | 85 | 58.4 | 62.9 | 59.8 | 90.2 | 0.0112 | 18 | 7 |
| 134 | Cartwright, Eli | GAT_GRI | Four-Seam | LHH | 49 | 60.2 | 58.3 | 59.6 | 89.9 | 0.0087 | 19 | 8 |
| 147 | Herbert, Andrew | WAS_WIL3 | Four-Seam | LHH | 35 | 57.1 | 64.6 | 59.3 | 89.0 | 0.0122 | 22 | 9 |
| 148 | Anderson, Colt | WAS_WIL3 | Four-Seam | LHH | 92 | 61.4 | 54.2 | 59.2 | 88.9 | 0.0064 | 23 | 10 |
| 155 | Shears, Tanner | SCH_BOO | Four-Seam | LHH | 87 | 62.4 | 51.1 | 59.0 | 88.4 | 0.0046 | 25 | 11 |
| 163 | Mercado, Nelson | OTT_TIT | Four-Seam | LHH | 39 | 60.3 | 55.4 | 58.8 | 87.8 | 0.0070 | 28 | 12 |
| 179 | Brothers, Kellen | SUS_COU1 | Four-Seam | LHH | 134 | 53.4 | 69.8 | 58.3 | 86.5 | 0.0151 | 33 | 13 |
| 188 | Garcia, Brett | OTT_TIT | Four-Seam | LHH | 95 | 58.9 | 56.0 | 58.1 | 85.9 | 0.0074 | 35 | 14 |
| 199 | Foy, Corbin | LAK_ERI24 | Four-Seam | LHH | 48 | 65.0 | 40.2 | 57.6 | 85.0 | -0.0015 | 36 | 15 |
| 207 | Correa, Nelvin | QUE_CAP | Four-Seam | LHH | 38 | 66.5 | 36.2 | 57.4 | 84.4 | -0.0038 | 38 | 16 |
| 218 | Langhorne, Miles | SUS_COU1 | Four-Seam | LHH | 30 | 58.6 | 53.9 | 57.2 | 83.6 | 0.0062 | 42 | 17 |
| 223 | Glickstein, Aaron | SCH_BOO | Four-Seam | LHH | 77 | 55.6 | 60.6 | 57.1 | 83.2 | 0.0099 | 43 | 18 |
| 239 | Ortiz, Julio | GAT_GRI | Four-Seam | LHH | 142 | 59.6 | 49.6 | 56.6 | 82.0 | 0.0038 | 47 | 19 |
| 244 | Riedel, Caleb | SCH_BOO | Four-Seam | LHH | 47 | 61.5 | 44.9 | 56.5 | 81.6 | 0.0012 | 48 | 20 |
| 247 | Moore, Kyle | SCH_BOO | Four-Seam | LHH | 93 | 54.0 | 62.0 | 56.4 | 81.4 | 0.0107 | 50 | 21 |
| 256 | Alpern, Liam | FLO_Y'A | Four-Seam | LHH | 86 | 53.6 | 62.0 | 56.1 | 80.7 | 0.0107 | 52 | 22 |
| 262 | Shinn, Nathan | LAK_ERI24 | Four-Seam | LHH | 101 | 54.8 | 58.5 | 55.9 | 80.3 | 0.0088 | 54 | 23 |
| 265 | Fowler, Dalton | SUS_COU1 | Four-Seam | LHH | 43 | 52.5 | 63.7 | 55.9 | 80.0 | 0.0117 | 55 | 24 |
| 279 | Brown, Ethan | WAS_WIL3 | Four-Seam | LHH | 25 | 61.6 | 41.3 | 55.5 | 79.0 | -0.0009 | 62 | 25 |

### Four-Seam vs RHH

| Rank | Pitcher | Team | Pitch Type | Batter Side | Split Pitches | PVS | Loc | Final | Final % | Avg Loc Adv | Type Rank | Type/Side Rank |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 8 | Grounds, Jackson | DOW_EAS1 | Four-Seam | RHH | 48 | 73.5 | 69.3 | 72.2 | 99.5 | 0.0149 | 1 | 1 |
| 13 | Davis, Tyler | WIN_CIT29 | Four-Seam | RHH | 33 | 73.6 | 64.2 | 70.8 | 99.1 | 0.0120 | 2 | 2 |
| 15 | Cameron, Zach | WIN_CIT29 | Four-Seam | RHH | 50 | 70.9 | 67.1 | 69.8 | 98.9 | 0.0136 | 3 | 3 |
| 45 | Mercado, Nelson | OTT_TIT | Four-Seam | RHH | 42 | 60.3 | 74.1 | 64.4 | 96.7 | 0.0175 | 6 | 4 |
| 53 | Rodriguez, Joe Joe | NEW_JER6 | Four-Seam | RHH | 36 | 63.2 | 65.0 | 63.7 | 96.1 | 0.0124 | 7 | 5 |
| 59 | Gregory, Ben | GAT_GRI | Four-Seam | RHH | 73 | 63.6 | 62.3 | 63.2 | 95.6 | 0.0109 | 8 | 6 |
| 79 | Langhorne, Miles | SUS_COU1 | Four-Seam | RHH | 40 | 58.6 | 69.9 | 62.0 | 94.1 | 0.0152 | 11 | 7 |
| 82 | Foster, Kobe | WAS_WIL3 | Four-Seam | RHH | 220 | 61.3 | 63.4 | 61.9 | 93.9 | 0.0115 | 12 | 8 |
| 99 | Shears, Tanner | SCH_BOO | Four-Seam | RHH | 118 | 62.4 | 59.0 | 61.4 | 92.6 | 0.0091 | 15 | 9 |
| 107 | Wehrle, Tyler | WIN_CIT29 | Four-Seam | RHH | 156 | 59.2 | 64.8 | 60.9 | 92.0 | 0.0123 | 16 | 10 |
| 115 | Brouwer, Adam | LAK_ERI24 | Four-Seam | RHH | 64 | 60.6 | 59.5 | 60.3 | 91.4 | 0.0094 | 17 | 11 |
| 137 | Brothers, Kellen | SUS_COU1 | Four-Seam | RHH | 100 | 53.4 | 73.9 | 59.6 | 89.7 | 0.0174 | 20 | 12 |
| 146 | Foy, Corbin | LAK_ERI24 | Four-Seam | RHH | 47 | 65.0 | 46.0 | 59.3 | 89.0 | 0.0018 | 21 | 13 |
| 149 | MacMillan, Blake | TRO_AIG | Four-Seam | RHH | 80 | 62.6 | 51.3 | 59.2 | 88.8 | 0.0047 | 24 | 14 |
| 158 | Zaffiro, Cole | SCH_BOO | Four-Seam | RHH | 125 | 58.4 | 60.0 | 58.9 | 88.1 | 0.0096 | 26 | 15 |
| 161 | Ginn, Landon | WAS_WIL3 | Four-Seam | RHH | 59 | 54.0 | 70.3 | 58.8 | 87.9 | 0.0154 | 27 | 16 |
| 165 | Correa, Nelvin | QUE_CAP | Four-Seam | RHH | 37 | 66.5 | 40.8 | 58.8 | 87.6 | -0.0012 | 29 | 17 |
| 168 | Anderson, Colt | WAS_WIL3 | Four-Seam | RHH | 135 | 61.4 | 52.6 | 58.7 | 87.4 | 0.0055 | 30 | 18 |
| 171 | Garcia, Brett | OTT_TIT | Four-Seam | RHH | 134 | 58.9 | 57.7 | 58.6 | 87.2 | 0.0083 | 31 | 19 |
| 172 | Kelly, Colin | SUS_COU1 | Four-Seam | RHH | 49 | 58.0 | 59.9 | 58.6 | 87.1 | 0.0096 | 32 | 20 |
| 181 | Perez, Kelvin | WAS_WIL3 | Four-Seam | RHH | 46 | 54.7 | 66.6 | 58.3 | 86.4 | 0.0133 | 34 | 21 |
| 204 | Brouwer, Adam | LAK_ERI24 | Four-Seam | RHH | 41 | 57.4 | 57.6 | 57.5 | 84.7 | 0.0083 | 37 | 22 |
| 208 | Johnson, Preston | MIS_MUD | Four-Seam | RHH | 28 | 49.8 | 75.0 | 57.4 | 84.4 | 0.0180 | 39 | 23 |
| 212 | Albert, Wes | TRI_VAL | Four-Seam | RHH | 54 | 52.8 | 68.0 | 57.3 | 84.1 | 0.0141 | 40 | 24 |
| 216 | Delaney, Carter | WIN_CIT29 | Four-Seam | RHH | 67 | 55.8 | 60.7 | 57.3 | 83.7 | 0.0100 | 41 | 25 |

### Sinker vs LHH

| Rank | Pitcher | Team | Pitch Type | Batter Side | Split Pitches | PVS | Loc | Final | Final % | Avg Loc Adv | Type Rank | Type/Side Rank |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 58 | Lovell, Justin | WIN_CIT29 | Sinker | LHH | 59 | 72.2 | 42.2 | 63.2 | 95.7 | -0.0004 | 2 | 1 |
| 92 | Mannering, Shawn | DOW_EAS1 | Sinker | LHH | 27 | 62.7 | 59.1 | 61.6 | 93.1 | 0.0091 | 5 | 2 |
| 109 | Colon, Jeffrey | TRO_AIG | Sinker | LHH | 30 | 64.3 | 52.0 | 60.6 | 91.8 | 0.0051 | 8 | 3 |
| 142 | Lawson, Nathan | FLO_Y'A | Sinker | LHH | 87 | 62.4 | 52.6 | 59.4 | 89.3 | 0.0055 | 10 | 4 |
| 156 | Sabatine, Gino | TRI_VAL | Sinker | LHH | 36 | 59.1 | 58.8 | 59.0 | 88.3 | 0.0090 | 11 | 5 |
| 169 | Riedel, Caleb | SCH_BOO | Sinker | LHH | 26 | 64.9 | 44.2 | 58.7 | 87.3 | 0.0007 | 12 | 6 |
| 194 | Glickstein, Aaron | SCH_BOO | Sinker | LHH | 25 | 63.5 | 44.4 | 57.8 | 85.4 | 0.0008 | 14 | 7 |
| 222 | Widener, Jacob | SUS_COU1 | Sinker | LHH | 46 | 61.3 | 47.4 | 57.1 | 83.3 | 0.0025 | 18 | 8 |
| 234 | McCartney, Seth | MIS_MUD | Sinker | LHH | 67 | 56.4 | 57.7 | 56.8 | 82.4 | 0.0083 | 19 | 9 |
| 241 | Morgan, Marcus | JOL_SLA | Sinker | LHH | 54 | 58.7 | 51.7 | 56.6 | 81.9 | 0.0050 | 21 | 10 |
| 287 | Cook, Cole | SCH_BOO | Sinker | LHH | 39 | 55.8 | 54.2 | 55.3 | 78.4 | 0.0063 | 23 | 11 |
| 293 | Aldeano, Austin | TRO_AIG | Sinker | LHH | 45 | 53.9 | 58.3 | 55.2 | 77.9 | 0.0087 | 25 | 12 |
| 299 | Hensey, Rob | SUS_COU1 | Sinker | LHH | 117 | 55.6 | 54.2 | 55.2 | 77.5 | 0.0063 | 27 | 13 |
| 335 | Joven, Art | MIS_MUD | Sinker | LHH | 100 | 54.6 | 54.8 | 54.6 | 74.8 | 0.0067 | 29 | 14 |
| 343 | Pierson, Kenny | LAK_ERI24 | Sinker | LHH | 56 | 54.3 | 54.7 | 54.5 | 74.1 | 0.0067 | 30 | 15 |
| 346 | Turner, Eric | JOL_SLA | Sinker | LHH | 44 | 56.4 | 49.9 | 54.4 | 73.9 | 0.0039 | 31 | 16 |
| 351 | Kelly, Aiden | TRI_VAL | Sinker | LHH | 51 | 51.9 | 59.8 | 54.3 | 73.5 | 0.0095 | 32 | 17 |
| 356 | Fritz, AJ | MIS_MUD | Sinker | LHH | 33 | 55.2 | 51.8 | 54.2 | 73.2 | 0.0050 | 34 | 18 |
| 359 | Cerda, Junior | EVA_OTT | Sinker | LHH | 39 | 60.8 | 38.4 | 54.1 | 72.9 | -0.0025 | 36 | 19 |
| 368 | Plumadore, Carson | WIN_CIT29 | Sinker | LHH | 68 | 55.6 | 49.9 | 53.9 | 72.3 | 0.0040 | 38 | 20 |
| 393 | Vecerka, Boris | QUE_CAP | Sinker | LHH | 113 | 51.6 | 57.7 | 53.4 | 70.4 | 0.0083 | 41 | 21 |
| 397 | Stuka, Ted | OTT_TIT | Sinker | LHH | 63 | 52.3 | 55.6 | 53.3 | 70.1 | 0.0072 | 42 | 22 |
| 411 | Grounds, Jackson | DOW_EAS1 | Sinker | LHH | 75 | 56.7 | 44.4 | 53.0 | 69.0 | 0.0008 | 44 | 23 |
| 413 | Webster, Evan | FLO_Y'A | Sinker | LHH | 33 | 51.8 | 55.7 | 53.0 | 68.9 | 0.0072 | 45 | 24 |
| 414 | Martzolf, Max | JOL_SLA | Sinker | LHH | 70 | 54.8 | 48.8 | 53.0 | 68.8 | 0.0034 | 46 | 25 |

### Sinker vs RHH

| Rank | Pitcher | Team | Pitch Type | Batter Side | Split Pitches | PVS | Loc | Final | Final % | Avg Loc Adv | Type Rank | Type/Side Rank |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 43 | Still, Stephen | TRI_VAL | Sinker | RHH | 50 | 68.8 | 54.4 | 64.5 | 96.8 | 0.0065 | 1 | 1 |
| 70 | Glickstein, Aaron | SCH_BOO | Sinker | RHH | 60 | 63.5 | 59.9 | 62.4 | 94.8 | 0.0096 | 3 | 2 |
| 83 | Colon, Jeffrey | TRO_AIG | Sinker | RHH | 26 | 64.3 | 56.4 | 61.9 | 93.8 | 0.0076 | 4 | 3 |
| 101 | Lovell, Justin | WIN_CIT29 | Sinker | RHH | 30 | 72.2 | 35.9 | 61.3 | 92.4 | -0.0039 | 6 | 4 |
| 105 | Mannering, Shawn | DOW_EAS1 | Sinker | RHH | 32 | 62.7 | 57.3 | 61.0 | 92.1 | 0.0081 | 7 | 5 |
| 135 | Cerda, Junior | EVA_OTT | Sinker | RHH | 39 | 60.8 | 56.8 | 59.6 | 89.9 | 0.0078 | 9 | 6 |
| 187 | Riedel, Caleb | SCH_BOO | Sinker | RHH | 38 | 64.9 | 42.0 | 58.1 | 85.9 | -0.0005 | 13 | 7 |
| 200 | Morgan, Marcus | JOL_SLA | Sinker | RHH | 28 | 58.7 | 54.9 | 57.5 | 85.0 | 0.0067 | 15 | 8 |
| 203 | Turner, Eric | JOL_SLA | Sinker | RHH | 45 | 56.4 | 60.1 | 57.5 | 84.7 | 0.0097 | 16 | 9 |
| 217 | Lawson, Nathan | FLO_Y'A | Sinker | RHH | 58 | 62.4 | 45.3 | 57.2 | 83.7 | 0.0014 | 17 | 10 |
| 238 | Aldeano, Austin | TRO_AIG | Sinker | RHH | 25 | 53.9 | 63.0 | 56.7 | 82.1 | 0.0113 | 20 | 11 |
| 268 | Widener, Jacob | SUS_COU1 | Sinker | RHH | 68 | 61.3 | 43.0 | 55.8 | 79.8 | 0.0001 | 22 | 12 |
| 291 | McCartney, Seth | MIS_MUD | Sinker | RHH | 53 | 56.4 | 52.6 | 55.2 | 78.1 | 0.0054 | 24 | 13 |
| 296 | Plumadore, Carson | WIN_CIT29 | Sinker | RHH | 45 | 55.6 | 54.4 | 55.2 | 77.7 | 0.0065 | 26 | 14 |
| 305 | Cook, Cole | SCH_BOO | Sinker | RHH | 45 | 55.8 | 53.4 | 55.1 | 77.0 | 0.0059 | 28 | 15 |
| 353 | Henderson, Drew | DOW_EAS1 | Sinker | RHH | 36 | 56.2 | 49.5 | 54.2 | 73.4 | 0.0037 | 33 | 16 |
| 358 | Kelly, Colin | SUS_COU1 | Sinker | RHH | 53 | 54.1 | 54.2 | 54.1 | 73.0 | 0.0064 | 35 | 17 |
| 361 | Vecerka, Boris | QUE_CAP | Sinker | RHH | 77 | 51.6 | 59.9 | 54.1 | 72.8 | 0.0096 | 37 | 18 |
| 370 | Long, Maddox | WAS_WIL3 | Sinker | RHH | 117 | 55.6 | 49.7 | 53.8 | 72.1 | 0.0038 | 39 | 19 |
| 389 | Pierson, Kenny | LAK_ERI24 | Sinker | RHH | 136 | 54.3 | 51.4 | 53.5 | 70.7 | 0.0048 | 40 | 20 |
| 409 | Kelly, Aiden | TRI_VAL | Sinker | RHH | 27 | 51.9 | 55.9 | 53.1 | 69.2 | 0.0073 | 43 | 21 |
| 449 | Hensey, Rob | SUS_COU1 | Sinker | RHH | 256 | 55.6 | 44.7 | 52.3 | 66.1 | 0.0010 | 49 | 22 |
| 452 | Benitez, Jorge | NEW_JER6 | Sinker | RHH | 51 | 53.4 | 49.7 | 52.3 | 65.9 | 0.0038 | 50 | 23 |
| 455 | Grounds, Jackson | DOW_EAS1 | Sinker | RHH | 41 | 56.7 | 41.8 | 52.2 | 65.7 | -0.0006 | 51 | 24 |
| 459 | Hoeymans, Jack | GAT_GRI | Sinker | RHH | 35 | 50.1 | 57.1 | 52.2 | 65.4 | 0.0080 | 52 | 25 |

### Slider vs LHH

| Rank | Pitcher | Team | Pitch Type | Batter Side | Split Pitches | PVS | Loc | Final | Final % | Avg Loc Adv | Type Rank | Type/Side Rank |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 11 | Alpern, Liam | FLO_Y'A | Slider | LHH | 38 | 75.5 | 61.8 | 71.4 | 99.2 | 0.0106 | 7 | 1 |
| 12 | Carroll, Jake | JOL_SLA | Slider | LHH | 46 | 80.0 | 49.8 | 70.9 | 99.2 | 0.0039 | 8 | 2 |
| 14 | Ryan, Dillon | NEW_ENG23 | Slider | LHH | 59 | 79.2 | 48.5 | 70.0 | 99.0 | 0.0032 | 9 | 3 |
| 20 | Harper, Scott | NEW_YOR13 | Slider | LHH | 31 | 76.7 | 50.9 | 69.0 | 98.6 | 0.0045 | 10 | 4 |
| 21 | McEvoy, Aidan | FLO_Y'A | Slider | LHH | 65 | 71.7 | 62.6 | 68.9 | 98.5 | 0.0111 | 11 | 5 |
| 25 | Jones, Logan | TRI_VAL | Slider | LHH | 33 | 73.7 | 53.0 | 67.5 | 98.2 | 0.0057 | 13 | 6 |
| 50 | Bargo, Casey | NEW_ENG23 | Slider | LHH | 27 | 72.8 | 43.3 | 63.9 | 96.3 | 0.0002 | 29 | 7 |
| 54 | Sechrist, Zander | WAS_WIL3 | Slider | LHH | 34 | 68.5 | 52.3 | 63.7 | 96.0 | 0.0053 | 31 | 8 |
| 89 | Balzan, Jackson | SUS_COU1 | Slider | LHH | 51 | 66.6 | 50.2 | 61.7 | 93.3 | 0.0041 | 43 | 9 |
| 106 | MacMillan, Blake | TRO_AIG | Slider | LHH | 57 | 61.7 | 59.2 | 61.0 | 92.1 | 0.0092 | 53 | 10 |
| 125 | Foster, Kobe | WAS_WIL3 | Slider | LHH | 99 | 62.6 | 53.9 | 60.0 | 90.6 | 0.0062 | 60 | 11 |
| 129 | Smith, Jackson | MIS_MUD | Slider | LHH | 41 | 65.9 | 45.8 | 59.9 | 90.3 | 0.0016 | 62 | 12 |
| 141 | Armstrong, Andrew | NEW_YOR13 | Slider | LHH | 60 | 58.7 | 61.2 | 59.5 | 89.4 | 0.0103 | 65 | 13 |
| 150 | Morgan, Cooper | QUE_CAP | Slider | LHH | 38 | 60.4 | 56.5 | 59.2 | 88.7 | 0.0076 | 69 | 14 |
| 167 | Webster, Evan | FLO_Y'A | Slider | LHH | 75 | 58.8 | 58.6 | 58.8 | 87.5 | 0.0088 | 75 | 15 |
| 174 | Widener, Jacob | SUS_COU1 | Slider | LHH | 50 | 60.1 | 54.7 | 58.5 | 86.9 | 0.0067 | 76 | 16 |
| 177 | Morin, Jacob | QUE_CAP | Slider | LHH | 25 | 65.1 | 42.7 | 58.4 | 86.7 | -0.0001 | 78 | 17 |
| 183 | Dima, Josh | GAT_GRI | Slider | LHH | 71 | 56.9 | 61.0 | 58.1 | 86.2 | 0.0102 | 79 | 18 |
| 185 | Scott, Brandon | LAK_ERI24 | Slider | LHH | 64 | 57.4 | 59.7 | 58.1 | 86.1 | 0.0095 | 80 | 19 |
| 189 | Perozzi, John | SUS_COU1 | Slider | LHH | 61 | 64.1 | 43.8 | 58.0 | 85.8 | 0.0005 | 82 | 20 |
| 195 | Harris, Everette | TRI_VAL | Slider | LHH | 29 | 56.1 | 61.5 | 57.7 | 85.3 | 0.0105 | 83 | 21 |
| 197 | Kemlage, Joe | NEW_ENG23 | Slider | LHH | 32 | 59.3 | 53.6 | 57.6 | 85.2 | 0.0061 | 84 | 22 |
| 198 | Cook, Cole | SCH_BOO | Slider | LHH | 102 | 56.2 | 60.9 | 57.6 | 85.1 | 0.0101 | 85 | 23 |
| 202 | Eckaus, David | EVA_OTT | Slider | LHH | 107 | 56.4 | 60.1 | 57.5 | 84.8 | 0.0097 | 86 | 24 |
| 220 | Brito, Richard | NEW_ENG23 | Slider | LHH | 37 | 58.1 | 54.9 | 57.1 | 83.4 | 0.0067 | 91 | 25 |

### Slider vs RHH

| Rank | Pitcher | Team | Pitch Type | Batter Side | Split Pitches | PVS | Loc | Final | Final % | Avg Loc Adv | Type Rank | Type/Side Rank |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | Vecerka, Boris | QUE_CAP | Slider | RHH | 48 | 80.0 | 63.7 | 75.1 | 100.0 | 0.0117 | 1 | 1 |
| 2 | Ryan, Dillon | NEW_ENG23 | Slider | RHH | 54 | 79.2 | 63.0 | 74.4 | 99.9 | 0.0113 | 2 | 2 |
| 3 | Harper, Scott | NEW_YOR13 | Slider | RHH | 143 | 76.7 | 67.5 | 74.0 | 99.8 | 0.0138 | 3 | 3 |
| 4 | Kirby, Zach | WAS_WIL3 | Slider | RHH | 126 | 70.9 | 80.0 | 73.6 | 99.8 | 0.0211 | 4 | 4 |
| 5 | Bargo, Casey | NEW_ENG23 | Slider | RHH | 29 | 72.8 | 73.7 | 73.0 | 99.7 | 0.0173 | 5 | 5 |
| 6 | Moore, Kyle | SCH_BOO | Slider | RHH | 31 | 70.4 | 77.5 | 72.5 | 99.6 | 0.0194 | 6 | 6 |
| 23 | Hickey, Matt | GAT_GRI | Slider | RHH | 63 | 67.6 | 70.5 | 68.5 | 98.3 | 0.0155 | 12 | 7 |
| 26 | Donnan, Blake | FLO_Y'A | Slider | RHH | 52 | 69.2 | 63.4 | 67.5 | 98.1 | 0.0115 | 14 | 8 |
| 27 | Toribio, Noe | TRO_AIG | Slider | RHH | 89 | 69.7 | 60.7 | 67.0 | 98.0 | 0.0100 | 15 | 9 |
| 28 | Nakata, Yuto | QUE_CAP | Slider | RHH | 83 | 69.8 | 59.8 | 66.8 | 98.0 | 0.0095 | 16 | 10 |
| 29 | Vega, Lucas | TRO_AIG | Slider | RHH | 84 | 66.0 | 67.4 | 66.4 | 97.9 | 0.0138 | 17 | 11 |
| 30 | Hagan, Jack | DOW_EAS1 | Slider | RHH | 118 | 62.2 | 75.2 | 66.1 | 97.8 | 0.0182 | 18 | 12 |
| 32 | Perozzi, John | SUS_COU1 | Slider | RHH | 62 | 64.1 | 69.4 | 65.7 | 97.7 | 0.0149 | 19 | 13 |
| 33 | O'Hanlon, Michael | WAS_WIL3 | Slider | RHH | 45 | 61.8 | 74.6 | 65.6 | 97.6 | 0.0178 | 20 | 14 |
| 35 | Jones, Logan | TRI_VAL | Slider | RHH | 32 | 73.7 | 45.1 | 65.1 | 97.4 | 0.0013 | 21 | 15 |
| 36 | Petschke, Ben | EVA_OTT | Slider | RHH | 84 | 63.9 | 68.0 | 65.1 | 97.4 | 0.0141 | 22 | 16 |
| 37 | Morin, Jacob | QUE_CAP | Slider | RHH | 60 | 65.1 | 65.0 | 65.1 | 97.3 | 0.0124 | 23 | 17 |
| 38 | Harajli, Ahmad | FLO_Y'A | Slider | RHH | 49 | 65.0 | 64.8 | 64.9 | 97.2 | 0.0123 | 24 | 18 |
| 39 | Leak, Anthony | NEW_YOR13 | Slider | RHH | 131 | 58.5 | 79.8 | 64.9 | 97.1 | 0.0207 | 25 | 19 |
| 40 | Vailes, Gage | GAT_GRI | Slider | RHH | 177 | 58.3 | 80.0 | 64.8 | 97.1 | 0.0216 | 26 | 20 |
| 41 | Alpern, Liam | FLO_Y'A | Slider | RHH | 40 | 75.5 | 39.9 | 64.8 | 97.0 | -0.0017 | 27 | 21 |
| 44 | Gilleran, Jimmy | NEW_ENG23 | Slider | RHH | 54 | 57.8 | 80.0 | 64.4 | 96.7 | 0.0247 | 28 | 22 |
| 52 | Garcia, Hector | WAS_WIL3 | Slider | RHH | 36 | 56.8 | 80.0 | 63.7 | 96.1 | 0.0242 | 30 | 23 |
| 55 | Helt, Robert | LAK_ERI24 | Slider | RHH | 137 | 56.8 | 79.6 | 63.6 | 95.9 | 0.0207 | 32 | 24 |
| 56 | Smith, Jackson | MIS_MUD | Slider | RHH | 65 | 65.9 | 57.6 | 63.4 | 95.8 | 0.0083 | 33 | 25 |

### Splitter vs LHH

| Rank | Pitcher | Team | Pitch Type | Batter Side | Split Pitches | PVS | Loc | Final | Final % | Avg Loc Adv | Type Rank | Type/Side Rank |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 46 | Garcia, Hector | WAS_WIL3 | Splitter | LHH | 59 | 72.7 | 45.0 | 64.4 | 96.6 | 0.0012 | 1 | 1 |
| 117 | Vitas, Ben | JOL_SLA | Splitter | LHH | 68 | 67.3 | 43.7 | 60.2 | 91.2 | 0.0005 | 2 | 2 |
| 130 | Shears, Tanner | SCH_BOO | Splitter | LHH | 35 | 67.2 | 42.8 | 59.9 | 90.2 | -0.0001 | 4 | 3 |
| 178 | Pindel, Buddie | SCH_BOO | Splitter | LHH | 52 | 64.0 | 45.1 | 58.4 | 86.6 | 0.0013 | 8 | 4 |
| 180 | Villers, Ian | QUE_CAP | Splitter | LHH | 39 | 64.6 | 43.5 | 58.3 | 86.5 | 0.0004 | 9 | 5 |
| 228 | Thornton, Tyler | NEW_ENG23 | Splitter | LHH | 52 | 61.4 | 46.8 | 57.0 | 82.8 | 0.0022 | 10 | 6 |
| 276 | Thompson, Ross | SCH_BOO | Splitter | LHH | 104 | 59.9 | 45.6 | 55.6 | 79.2 | 0.0016 | 11 | 7 |
| 420 | Williams, Brian | MIS_MUD | Splitter | LHH | 49 | 55.7 | 46.2 | 52.9 | 68.3 | 0.0019 | 14 | 8 |
| 536 | Salata, Derek | SCH_BOO | Splitter | LHH | 88 | 53.4 | 45.6 | 51.1 | 59.6 | 0.0016 | 16 | 9 |
| 984 | Eldred, Zach | NEW_ENG23 | Splitter | LHH | 34 | 44.2 | 45.8 | 44.7 | 25.7 | 0.0017 | 17 | 10 |
| 1072 | Nakata, Yuto | QUE_CAP | Splitter | LHH | 66 | 43.8 | 42.1 | 43.3 | 19.0 | -0.0004 | 19 | 11 |
| 1300 | Duby, Bill | NEW_JER6 | Splitter | LHH | 36 | 32.0 | 41.7 | 34.9 | 1.8 | -0.0006 | 21 | 12 |

### Splitter vs RHH

| Rank | Pitcher | Team | Pitch Type | Batter Side | Split Pitches | PVS | Loc | Final | Final % | Avg Loc Adv | Type Rank | Type/Side Rank |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 122 | Shears, Tanner | SCH_BOO | Splitter | RHH | 30 | 67.2 | 43.4 | 60.1 | 90.9 | 0.0003 | 3 | 1 |
| 139 | Vitas, Ben | JOL_SLA | Splitter | RHH | 30 | 67.3 | 41.5 | 59.5 | 89.6 | -0.0008 | 5 | 2 |
| 151 | Villers, Ian | QUE_CAP | Splitter | RHH | 25 | 64.6 | 46.5 | 59.2 | 88.7 | 0.0020 | 6 | 3 |
| 175 | Pindel, Buddie | SCH_BOO | Splitter | RHH | 30 | 64.0 | 45.2 | 58.4 | 86.8 | 0.0013 | 7 | 4 |
| 327 | Thornton, Tyler | NEW_ENG23 | Splitter | RHH | 36 | 61.4 | 39.2 | 54.7 | 75.4 | -0.0021 | 12 | 5 |
| 391 | Thompson, Ross | SCH_BOO | Splitter | RHH | 28 | 59.9 | 38.3 | 53.4 | 70.5 | -0.0026 | 13 | 6 |
| 442 | Williams, Brian | MIS_MUD | Splitter | RHH | 37 | 55.7 | 44.7 | 52.4 | 66.7 | 0.0010 | 15 | 7 |
| 1030 | Eldred, Zach | NEW_ENG23 | Splitter | RHH | 32 | 44.2 | 43.7 | 44.0 | 22.2 | 0.0005 | 18 | 8 |
| 1131 | Nakata, Yuto | QUE_CAP | Splitter | RHH | 28 | 43.8 | 38.4 | 42.2 | 14.6 | -0.0025 | 20 | 9 |
