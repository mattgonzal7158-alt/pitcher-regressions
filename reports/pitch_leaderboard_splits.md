# Handedness-Specific Pitch Leaderboards

- Pitch Value input: `data\processed\pitch_value_scores_with_type_rank.csv` (568 rows)
- Location Score input: `data\processed\location_scores.csv` (1,187 rows)
- Output file: `data\processed\pitch_leaderboard_splits.csv`
- Joined leaderboard rows: 988
- Formula: `0.70 * pitch_value_20_80 + 0.30 * location_score_20_80`
- Pitch Value is pitcher + pitch type level; Location Score supplies the batter-side split.
- Higher scores are better.

## Method

The leaderboard joins Pitch Value to Location Score by pitcher, team, and normalized pitch type. Because the Pitch Value table is not handedness-specific, each pitcher-pitch Pitch Value is paired with its available LHH and/or RHH Location Score rows.

`final_pitch_score_raw` and `final_pitch_score` are the weighted 20-80 blend. `final_pitch_score_0_100` is the percentile rank of that blended score among all split rows.

## Overall Leaderboard

| Rank | Pitcher | Team | Pitch Type | Batter Side | Split Pitches | PVS | Loc | Final | Final % | Avg Loc Adv | Type Rank | Type/Side Rank |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | Perez, Kelvin | WAS_WIL3 | Slider | RHH | 45 | 72.4 | 80.0 | 74.6 | 100.0 | 0.0183 | 1 | 1 |
| 2 | Harper, Scott | NEW_YOR13 | Slider | RHH | 98 | 77.6 | 67.3 | 74.5 | 99.9 | 0.0108 | 2 | 2 |
| 3 | Bargo, Casey | NEW_ENG23 | Slider | RHH | 29 | 71.8 | 72.3 | 71.9 | 99.8 | 0.0131 | 3 | 3 |
| 4 | Davis, Tyler | WIN_CIT29 | Four-Seam | RHH | 33 | 72.5 | 70.3 | 71.9 | 99.7 | 0.0122 | 1 | 1 |
| 5 | Grounds, Jackson | DOW_EAS1 | Curveball | RHH | 43 | 80.0 | 52.1 | 71.6 | 99.6 | 0.0037 | 1 | 1 |
| 6 | Escobar, Anthony | TRO_AIG | Changeup | LHH | 79 | 77.2 | 57.5 | 71.3 | 99.5 | 0.0063 | 1 | 1 |
| 7 | Grounds, Jackson | DOW_EAS1 | Four-Seam | RHH | 48 | 72.4 | 67.2 | 70.8 | 99.4 | 0.0107 | 2 | 2 |
| 8 | Carroll, Jake | JOL_SLA | Slider | LHH | 40 | 80.0 | 46.1 | 69.8 | 99.3 | 0.0009 | 4 | 1 |
| 9 | Alpern, Liam | FLO_Y'A | Slider | LHH | 38 | 74.3 | 58.8 | 69.7 | 99.2 | 0.0068 | 5 | 2 |
| 10 | Ryan, Dillon | NEW_ENG23 | Slider | RHH | 39 | 76.3 | 53.4 | 69.4 | 99.1 | 0.0043 | 6 | 4 |
| 11 | Grounds, Jackson | DOW_EAS1 | Four-Seam | LHH | 59 | 72.4 | 60.9 | 69.0 | 99.0 | 0.0078 | 3 | 1 |
| 12 | Grounds, Jackson | DOW_EAS1 | Curveball | LHH | 39 | 80.0 | 42.4 | 68.7 | 98.9 | -0.0007 | 2 | 1 |
| 13 | Kirby, Zach | WAS_WIL3 | Slider | RHH | 102 | 67.9 | 69.0 | 68.2 | 98.8 | 0.0116 | 7 | 5 |
| 14 | McEvoy, Aidan | FLO_Y'A | Slider | LHH | 51 | 74.6 | 53.1 | 68.2 | 98.7 | 0.0042 | 8 | 3 |
| 15 | Smith, Jackson | MIS_MUD | Slider | RHH | 52 | 68.5 | 65.9 | 67.7 | 98.6 | 0.0101 | 9 | 6 |
| 16 | Correa, Nelvin | QUE_CAP | Cutter | RHH | 28 | 74.2 | 52.3 | 67.6 | 98.5 | 0.0038 | 1 | 1 |
| 17 | Davis, Tyler | WIN_CIT29 | Four-Seam | LHH | 43 | 72.5 | 56.0 | 67.6 | 98.4 | 0.0055 | 4 | 2 |
| 18 | Ryan, Dillon | NEW_ENG23 | Slider | LHH | 54 | 76.3 | 47.2 | 67.6 | 98.3 | 0.0015 | 10 | 4 |
| 19 | Jones, Logan | TRI_VAL | Slider | LHH | 33 | 72.7 | 54.3 | 67.2 | 98.2 | 0.0048 | 11 | 5 |
| 20 | Harajli, Ahmad | FLO_Y'A | Slider | RHH | 39 | 68.9 | 62.0 | 66.8 | 98.1 | 0.0083 | 12 | 7 |
| 21 | Donnan, Blake | FLO_Y'A | Slider | RHH | 52 | 68.5 | 62.7 | 66.8 | 98.0 | 0.0087 | 13 | 8 |
| 22 | Webster, Evan | FLO_Y'A | Cutter | LHH | 70 | 75.4 | 46.4 | 66.7 | 97.9 | 0.0011 | 2 | 1 |
| 23 | Vitas, Ben | JOL_SLA | Splitter | LHH | 38 | 75.0 | 45.9 | 66.3 | 97.8 | 0.0009 | 1 | 1 |
| 24 | Webster, Evan | FLO_Y'A | Slider | LHH | 36 | 71.9 | 53.3 | 66.3 | 97.7 | 0.0043 | 14 | 6 |
| 25 | Willeman, Landon | EVA_OTT | Changeup | LHH | 80 | 68.7 | 60.2 | 66.2 | 97.6 | 0.0075 | 2 | 2 |
| 26 | Maietta, Dante | WIN_CIT29 | Changeup | LHH | 68 | 67.3 | 63.5 | 66.1 | 97.5 | 0.0090 | 3 | 3 |
| 27 | Cameron, Zach | WIN_CIT29 | Four-Seam | RHH | 34 | 66.5 | 64.8 | 66.0 | 97.4 | 0.0096 | 5 | 3 |
| 28 | Foster, Kobe | WAS_WIL3 | Slider | LHH | 76 | 73.0 | 49.1 | 65.8 | 97.3 | 0.0023 | 15 | 7 |
| 29 | Peyton, Blake | GAT_GRI | Changeup | RHH | 59 | 71.7 | 51.8 | 65.8 | 97.2 | 0.0036 | 4 | 1 |
| 30 | Alpern, Liam | FLO_Y'A | Slider | RHH | 40 | 74.3 | 45.7 | 65.8 | 97.1 | 0.0008 | 16 | 9 |
| 31 | Nakata, Yuto | QUE_CAP | Slider | RHH | 50 | 67.1 | 62.7 | 65.7 | 97.0 | 0.0087 | 17 | 10 |
| 32 | Long, Maddox | WAS_WIL3 | Slider | RHH | 111 | 64.8 | 67.5 | 65.6 | 96.9 | 0.0109 | 18 | 11 |
| 33 | Jones, Logan | TRI_VAL | Slider | RHH | 32 | 72.7 | 48.5 | 65.5 | 96.8 | 0.0021 | 19 | 12 |
| 34 | Wehrle, Tyler | WIN_CIT29 | Four-Seam | LHH | 75 | 60.1 | 76.5 | 65.0 | 96.7 | 0.0151 | 6 | 3 |
| 35 | Lefebvre, Charles | TRO_AIG | Slider | RHH | 53 | 62.3 | 71.0 | 64.9 | 96.6 | 0.0125 | 20 | 13 |
| 36 | Foster, Kobe | WAS_WIL3 | Four-Seam | LHH | 88 | 62.2 | 71.2 | 64.9 | 96.5 | 0.0126 | 7 | 4 |
| 37 | Still, Stephen | TRI_VAL | Sinker | RHH | 50 | 68.1 | 57.3 | 64.9 | 96.4 | 0.0062 | 1 | 1 |
| 38 | Nova, Fraynel | LAK_ERI24 | Slider | RHH | 100 | 58.2 | 80.0 | 64.7 | 96.3 | 0.0171 | 21 | 14 |
| 39 | Perozzi, John | SUS_COU1 | Slider | RHH | 46 | 59.3 | 76.0 | 64.3 | 96.2 | 0.0148 | 22 | 15 |
| 40 | Bargo, Casey | NEW_ENG23 | Slider | LHH | 27 | 71.8 | 46.8 | 64.3 | 96.1 | 0.0013 | 23 | 8 |

## Pitch Type + Batter Side Leaderboards

### Changeup vs LHH

| Rank | Pitcher | Team | Pitch Type | Batter Side | Split Pitches | PVS | Loc | Final | Final % | Avg Loc Adv | Type Rank | Type/Side Rank |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 6 | Escobar, Anthony | TRO_AIG | Changeup | LHH | 79 | 77.2 | 57.5 | 71.3 | 99.5 | 0.0063 | 1 | 1 |
| 25 | Willeman, Landon | EVA_OTT | Changeup | LHH | 80 | 68.7 | 60.2 | 66.2 | 97.6 | 0.0075 | 2 | 2 |
| 26 | Maietta, Dante | WIN_CIT29 | Changeup | LHH | 68 | 67.3 | 63.5 | 66.1 | 97.5 | 0.0090 | 3 | 3 |
| 71 | Moreno, Jose | DOW_EAS1 | Changeup | LHH | 28 | 65.5 | 51.7 | 61.3 | 92.9 | 0.0036 | 7 | 4 |
| 76 | Cooper, Garrett | NEW_YOR13 | Changeup | LHH | 73 | 61.7 | 59.6 | 61.1 | 92.4 | 0.0073 | 8 | 5 |
| 78 | Rodriguez, Joe Joe | NEW_JER6 | Changeup | LHH | 41 | 68.3 | 44.2 | 61.1 | 92.2 | 0.0001 | 9 | 6 |
| 94 | Dill, Austin | TRI_VAL | Changeup | LHH | 107 | 55.4 | 71.2 | 60.1 | 90.6 | 0.0126 | 13 | 7 |
| 96 | Wiltse, Ryan | EVA_OTT | Changeup | LHH | 78 | 66.0 | 46.2 | 60.1 | 90.4 | 0.0010 | 14 | 8 |
| 144 | Cameron, Zach | WIN_CIT29 | Changeup | LHH | 74 | 56.9 | 59.6 | 57.7 | 85.5 | 0.0072 | 17 | 9 |
| 152 | Boies, Emiles | QUE_CAP | Changeup | LHH | 88 | 66.8 | 35.0 | 57.2 | 84.7 | -0.0042 | 18 | 10 |
| 168 | Pindel, Buddie | SCH_BOO | Changeup | LHH | 70 | 57.9 | 54.7 | 56.9 | 83.1 | 0.0049 | 19 | 11 |
| 194 | Plumadore, Carson | WIN_CIT29 | Changeup | LHH | 133 | 55.7 | 57.2 | 56.2 | 80.5 | 0.0061 | 21 | 12 |
| 199 | Kirby, Zach | WAS_WIL3 | Changeup | LHH | 114 | 52.2 | 64.7 | 55.9 | 80.0 | 0.0096 | 22 | 13 |
| 212 | Burcham, Jacob | GAT_GRI | Changeup | LHH | 42 | 49.3 | 69.8 | 55.5 | 78.6 | 0.0120 | 24 | 14 |
| 224 | Hampton, Ky | OTT_TIT | Changeup | LHH | 74 | 50.4 | 66.2 | 55.1 | 77.4 | 0.0103 | 26 | 15 |
| 242 | Vailes, Gage | GAT_GRI | Changeup | LHH | 79 | 51.1 | 62.8 | 54.6 | 75.6 | 0.0087 | 27 | 16 |
| 247 | Barreto, Brayhans | TRI_VAL | Changeup | LHH | 26 | 57.4 | 47.4 | 54.4 | 75.1 | 0.0016 | 29 | 17 |
| 292 | Rohde, Isaac | NEW_YOR13 | Changeup | LHH | 159 | 57.7 | 43.3 | 53.4 | 70.5 | -0.0003 | 32 | 18 |
| 293 | Toribio, Noe | TRO_AIG | Changeup | LHH | 120 | 51.6 | 57.7 | 53.4 | 70.4 | 0.0063 | 33 | 19 |
| 310 | Thompson, Ross | SCH_BOO | Changeup | LHH | 74 | 53.0 | 53.4 | 53.1 | 68.7 | 0.0043 | 36 | 20 |
| 322 | Henderson, Drew | DOW_EAS1 | Changeup | LHH | 57 | 50.9 | 57.7 | 52.9 | 67.5 | 0.0063 | 38 | 21 |
| 377 | Balzan, Jackson | SUS_COU1 | Changeup | LHH | 64 | 55.9 | 41.6 | 51.6 | 61.9 | -0.0011 | 43 | 22 |
| 410 | Turner, Eric | JOL_SLA | Changeup | LHH | 77 | 51.0 | 50.9 | 51.0 | 58.6 | 0.0032 | 45 | 23 |
| 426 | DeCastro, Justin | LON_ISL22 | Changeup | LHH | 40 | 53.8 | 43.6 | 50.7 | 57.0 | -0.0002 | 46 | 24 |
| 446 | Roland, Cole | QUE_CAP | Changeup | LHH | 38 | 54.0 | 41.9 | 50.4 | 55.0 | -0.0010 | 48 | 25 |

### Changeup vs RHH

| Rank | Pitcher | Team | Pitch Type | Batter Side | Split Pitches | PVS | Loc | Final | Final % | Avg Loc Adv | Type Rank | Type/Side Rank |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 29 | Peyton, Blake | GAT_GRI | Changeup | RHH | 59 | 71.7 | 51.8 | 65.8 | 97.2 | 0.0036 | 4 | 1 |
| 57 | Maietta, Dante | WIN_CIT29 | Changeup | RHH | 44 | 67.3 | 52.8 | 62.9 | 94.3 | 0.0041 | 5 | 2 |
| 67 | Wiltse, Ryan | EVA_OTT | Changeup | RHH | 29 | 66.0 | 51.2 | 61.6 | 93.3 | 0.0033 | 6 | 3 |
| 88 | Messina, Chris | FDU_KNI | Changeup | RHH | 52 | 65.3 | 49.2 | 60.4 | 91.2 | 0.0024 | 10 | 4 |
| 91 | Hensey, Rob | SUS_COU1 | Changeup | RHH | 119 | 69.6 | 38.5 | 60.3 | 90.9 | -0.0025 | 11 | 5 |
| 92 | Willeman, Landon | EVA_OTT | Changeup | RHH | 32 | 68.7 | 40.2 | 60.2 | 90.8 | -0.0018 | 12 | 6 |
| 99 | Boies, Emiles | QUE_CAP | Changeup | RHH | 34 | 66.8 | 43.7 | 59.9 | 90.1 | -0.0001 | 15 | 7 |
| 102 | Foster, Kobe | WAS_WIL3 | Changeup | RHH | 112 | 66.1 | 45.0 | 59.8 | 89.8 | 0.0004 | 16 | 8 |
| 187 | Toribio, Noe | TRO_AIG | Changeup | RHH | 27 | 51.6 | 67.6 | 56.4 | 81.2 | 0.0110 | 20 | 9 |
| 202 | Rohde, Isaac | NEW_YOR13 | Changeup | RHH | 384 | 57.7 | 51.1 | 55.7 | 79.7 | 0.0033 | 23 | 10 |
| 219 | VanMarter, Luke | LEM_COL | Changeup | RHH | 29 | 58.5 | 47.7 | 55.3 | 77.9 | 0.0017 | 25 | 11 |
| 243 | Cooper, Garrett | NEW_YOR13 | Changeup | RHH | 36 | 61.7 | 37.8 | 54.5 | 75.5 | -0.0029 | 28 | 12 |
| 254 | Sakurai, Masatoshi | QUE_CAP | Changeup | RHH | 91 | 54.2 | 54.5 | 54.3 | 74.4 | 0.0049 | 30 | 13 |
| 256 | Barreto, Brayhans | TRI_VAL | Changeup | RHH | 82 | 57.4 | 46.9 | 54.2 | 74.2 | 0.0013 | 31 | 14 |
| 295 | Cameron, Zach | WIN_CIT29 | Changeup | RHH | 37 | 56.9 | 45.1 | 53.4 | 70.2 | 0.0005 | 34 | 15 |
| 299 | Roland, Cole | QUE_CAP | Changeup | RHH | 33 | 54.0 | 51.8 | 53.3 | 69.8 | 0.0036 | 35 | 16 |
| 317 | DeCastro, Justin | LON_ISL22 | Changeup | RHH | 82 | 53.8 | 51.2 | 53.0 | 68.0 | 0.0034 | 37 | 17 |
| 330 | Pierson, Kenny | LAK_ERI24 | Changeup | RHH | 104 | 52.3 | 54.0 | 52.8 | 66.7 | 0.0046 | 39 | 18 |
| 360 | Balzan, Jackson | SUS_COU1 | Changeup | RHH | 134 | 55.9 | 43.3 | 52.1 | 63.7 | -0.0003 | 40 | 19 |
| 367 | Dill, Austin | TRI_VAL | Changeup | RHH | 77 | 55.4 | 43.4 | 51.8 | 63.0 | -0.0003 | 41 | 20 |
| 375 | Plumadore, Carson | WIN_CIT29 | Changeup | RHH | 47 | 55.7 | 42.2 | 51.7 | 62.1 | -0.0009 | 42 | 21 |
| 395 | Kines, Gunnar | JOL_SLA | Changeup | RHH | 116 | 56.1 | 40.2 | 51.4 | 60.1 | -0.0018 | 44 | 22 |
| 436 | Barker, Alex | NEW_YOR13 | Changeup | RHH | 61 | 48.5 | 55.4 | 50.6 | 56.0 | 0.0053 | 47 | 23 |
| 459 | Villalobos, Jonaiker | FLO_Y'A | Changeup | RHH | 104 | 46.8 | 57.8 | 50.1 | 53.6 | 0.0064 | 51 | 24 |
| 496 | Williams, Pierce | NEW_ENG23 | Changeup | RHH | 176 | 50.6 | 46.4 | 49.4 | 49.9 | 0.0011 | 54 | 25 |

### Curveball vs LHH

| Rank | Pitcher | Team | Pitch Type | Batter Side | Split Pitches | PVS | Loc | Final | Final % | Avg Loc Adv | Type Rank | Type/Side Rank |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 12 | Grounds, Jackson | DOW_EAS1 | Curveball | LHH | 39 | 80.0 | 42.4 | 68.7 | 98.9 | -0.0007 | 2 | 1 |
| 75 | Harris, Ben | GAT_GRI | Curveball | LHH | 52 | 68.7 | 43.5 | 61.2 | 92.5 | -0.0003 | 6 | 2 |
| 156 | Hill, Kaleb | OTT_TIT | Curveball | LHH | 100 | 64.2 | 40.8 | 57.2 | 84.3 | -0.0015 | 9 | 3 |
| 189 | Garcia, Brett | OTT_TIT | Curveball | LHH | 36 | 60.1 | 47.4 | 56.3 | 81.0 | 0.0016 | 11 | 4 |
| 255 | Simpson, Garret | EVA_OTT | Curveball | LHH | 46 | 60.7 | 39.2 | 54.3 | 74.3 | -0.0022 | 14 | 5 |
| 301 | Noriega, Branden | LAK_ERI24 | Curveball | LHH | 29 | 54.9 | 49.6 | 53.3 | 69.6 | 0.0026 | 15 | 6 |
| 334 | Puccetti, Dominic | OTT_TIT | Curveball | LHH | 104 | 53.9 | 49.9 | 52.7 | 66.3 | 0.0027 | 18 | 7 |
| 349 | Milburn, Isaac | FLO_Y'A | Curveball | LHH | 50 | 54.7 | 46.9 | 52.3 | 64.8 | 0.0013 | 21 | 8 |
| 350 | Petschke, Ben | EVA_OTT | Curveball | LHH | 79 | 56.4 | 42.8 | 52.3 | 64.7 | -0.0006 | 22 | 9 |
| 359 | Kirby, Zach | WAS_WIL3 | Curveball | LHH | 48 | 57.5 | 39.6 | 52.1 | 63.8 | -0.0021 | 23 | 10 |
| 365 | Anibal, Trevor | NEW_ENG23 | Curveball | LHH | 34 | 57.1 | 39.8 | 51.9 | 63.2 | -0.0019 | 24 | 11 |
| 384 | Langrell, Connor | MIS_MUD | Curveball | LHH | 35 | 50.7 | 53.5 | 51.5 | 61.2 | 0.0044 | 26 | 12 |
| 387 | Peters, Garrett | NEW_YOR13 | Curveball | LHH | 62 | 51.9 | 50.4 | 51.5 | 60.9 | 0.0030 | 28 | 13 |
| 467 | Wiltse, Ryan | EVA_OTT | Curveball | LHH | 61 | 51.1 | 47.4 | 50.0 | 52.8 | 0.0016 | 36 | 14 |
| 469 | Sanchez, Edwin | LAK_ERI24 | Curveball | LHH | 29 | 51.6 | 46.1 | 49.9 | 52.6 | 0.0010 | 37 | 15 |
| 498 | Cooper, Garrett | NEW_YOR13 | Curveball | LHH | 38 | 50.6 | 46.4 | 49.3 | 49.7 | 0.0011 | 39 | 16 |
| 540 | Baker, Luke | EVA_OTT | Curveball | LHH | 37 | 48.2 | 48.5 | 48.3 | 45.4 | 0.0021 | 41 | 17 |
| 564 | Helt, Robert | LAK_ERI24 | Curveball | LHH | 62 | 50.1 | 42.6 | 47.9 | 43.0 | -0.0006 | 42 | 18 |
| 576 | Henderson, Drew | DOW_EAS1 | Curveball | LHH | 66 | 51.0 | 40.1 | 47.7 | 41.8 | -0.0018 | 43 | 19 |
| 617 | Andueza, Axel | DOW_EAS1 | Curveball | LHH | 72 | 46.2 | 48.4 | 46.9 | 37.7 | 0.0020 | 44 | 20 |
| 632 | Foster, Kobe | WAS_WIL3 | Curveball | LHH | 35 | 47.0 | 45.6 | 46.5 | 36.1 | 0.0007 | 46 | 21 |
| 642 | Allemann, Braeden | QUE_CAP | Curveball | LHH | 72 | 47.8 | 42.9 | 46.4 | 35.1 | -0.0005 | 47 | 22 |
| 658 | Figueredo, Kevin | WIN_CIT29 | Curveball | LHH | 45 | 45.1 | 48.5 | 46.1 | 33.5 | 0.0021 | 48 | 23 |
| 679 | Martzolf, Max | OTT_TIT | Curveball | LHH | 56 | 44.2 | 49.2 | 45.7 | 31.4 | 0.0024 | 49 | 24 |
| 701 | Shinn, Nathan | LAK_ERI24 | Curveball | LHH | 29 | 41.8 | 53.2 | 45.2 | 29.1 | 0.0043 | 51 | 25 |

### Curveball vs RHH

| Rank | Pitcher | Team | Pitch Type | Batter Side | Split Pitches | PVS | Loc | Final | Final % | Avg Loc Adv | Type Rank | Type/Side Rank |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 5 | Grounds, Jackson | DOW_EAS1 | Curveball | RHH | 43 | 80.0 | 52.1 | 71.6 | 99.6 | 0.0037 | 1 | 1 |
| 41 | Sechrist, Zander | WAS_WIL3 | Curveball | RHH | 37 | 68.4 | 54.8 | 64.3 | 96.0 | 0.0050 | 3 | 2 |
| 44 | Sesar, Jorden | SUS_COU1 | Curveball | RHH | 53 | 66.8 | 57.9 | 64.2 | 95.6 | 0.0064 | 4 | 3 |
| 47 | Harris, Ben | GAT_GRI | Curveball | RHH | 86 | 68.7 | 53.2 | 64.1 | 95.3 | 0.0043 | 5 | 4 |
| 122 | Hill, Kaleb | OTT_TIT | Curveball | RHH | 79 | 64.2 | 45.7 | 58.6 | 87.8 | 0.0008 | 7 | 5 |
| 140 | Garcia, Brett | OTT_TIT | Curveball | RHH | 36 | 60.1 | 52.5 | 57.8 | 85.9 | 0.0039 | 8 | 6 |
| 159 | Salata, Derek | SCH_BOO | Curveball | RHH | 37 | 58.5 | 54.0 | 57.1 | 84.0 | 0.0046 | 10 | 7 |
| 207 | Anibal, Trevor | NEW_ENG23 | Curveball | RHH | 37 | 57.1 | 52.0 | 55.5 | 79.1 | 0.0037 | 12 | 8 |
| 238 | Kirby, Zach | WAS_WIL3 | Curveball | RHH | 50 | 57.5 | 48.0 | 54.7 | 76.0 | 0.0018 | 13 | 9 |
| 306 | Petschke, Ben | EVA_OTT | Curveball | RHH | 79 | 56.4 | 45.6 | 53.2 | 69.1 | 0.0008 | 16 | 10 |
| 308 | Henderson, Drew | DOW_EAS1 | Curveball | RHH | 105 | 51.0 | 58.3 | 53.2 | 68.9 | 0.0066 | 17 | 11 |
| 336 | Puccetti, Dominic | OTT_TIT | Curveball | RHH | 44 | 53.9 | 49.8 | 52.7 | 66.1 | 0.0027 | 19 | 12 |
| 342 | Langrell, Connor | MIS_MUD | Curveball | RHH | 38 | 50.7 | 56.8 | 52.5 | 65.5 | 0.0059 | 20 | 13 |
| 379 | Balzan, Jackson | SUS_COU1 | Curveball | RHH | 35 | 53.8 | 46.2 | 51.6 | 61.7 | 0.0010 | 25 | 14 |
| 385 | Peyton, Blake | GAT_GRI | Curveball | RHH | 43 | 52.6 | 48.9 | 51.5 | 61.1 | 0.0023 | 27 | 15 |
| 393 | Helt, Robert | LAK_ERI24 | Curveball | RHH | 44 | 50.1 | 54.4 | 51.4 | 60.3 | 0.0048 | 29 | 16 |
| 401 | Allemann, Braeden | QUE_CAP | Curveball | RHH | 74 | 47.8 | 59.0 | 51.2 | 59.5 | 0.0070 | 30 | 17 |
| 407 | Oe, Ryoya | OTT_TIT | Curveball | RHH | 35 | 53.5 | 45.4 | 51.1 | 58.9 | 0.0007 | 31 | 18 |
| 414 | Cooper, Garrett | NEW_YOR13 | Curveball | RHH | 54 | 50.6 | 51.5 | 50.9 | 58.2 | 0.0035 | 32 | 19 |
| 431 | Barker, Alex | NEW_YOR13 | Curveball | RHH | 43 | 51.0 | 50.1 | 50.7 | 56.5 | 0.0028 | 33 | 20 |
| 433 | Noriega, Branden | LAK_ERI24 | Curveball | RHH | 61 | 54.9 | 40.9 | 50.7 | 56.3 | -0.0014 | 34 | 21 |
| 447 | Milburn, Isaac | FLO_Y'A | Curveball | RHH | 84 | 54.7 | 40.3 | 50.3 | 54.9 | -0.0017 | 35 | 22 |
| 478 | Moore, Kyle | SCH_BOO | Curveball | RHH | 60 | 46.9 | 56.4 | 49.7 | 51.7 | 0.0057 | 38 | 23 |
| 527 | Willeman, Landon | EVA_OTT | Curveball | RHH | 37 | 46.1 | 54.6 | 48.6 | 46.8 | 0.0049 | 40 | 24 |
| 623 | Peters, Garrett | NEW_YOR13 | Curveball | RHH | 27 | 51.9 | 34.4 | 46.7 | 37.0 | -0.0044 | 45 | 25 |

### Cutter vs LHH

| Rank | Pitcher | Team | Pitch Type | Batter Side | Split Pitches | PVS | Loc | Final | Final % | Avg Loc Adv | Type Rank | Type/Side Rank |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 22 | Webster, Evan | FLO_Y'A | Cutter | LHH | 70 | 75.4 | 46.4 | 66.7 | 97.9 | 0.0011 | 2 | 1 |
| 45 | Correa, Nelvin | QUE_CAP | Cutter | LHH | 40 | 74.2 | 40.7 | 64.1 | 95.5 | -0.0015 | 4 | 2 |
| 178 | McEvoy, Aidan | FLO_Y'A | Cutter | LHH | 29 | 59.8 | 49.0 | 56.6 | 82.1 | 0.0023 | 5 | 3 |
| 276 | Morgan, Marcus | JOL_SLA | Cutter | LHH | 38 | 56.9 | 46.4 | 53.7 | 72.2 | 0.0011 | 7 | 4 |
| 280 | Gamelin, Shaun | JOL_SLA | Cutter | LHH | 51 | 55.8 | 48.4 | 53.6 | 71.8 | 0.0020 | 8 | 5 |
| 281 | Gorgen, Grady | NEW_YOR13 | Cutter | LHH | 30 | 57.1 | 45.3 | 53.6 | 71.7 | 0.0006 | 9 | 6 |
| 324 | Saturria, Michael | NEW_ENG23 | Cutter | LHH | 76 | 57.4 | 42.5 | 52.9 | 67.3 | -0.0007 | 11 | 7 |
| 371 | Langrell, Connor | MIS_MUD | Cutter | LHH | 50 | 53.6 | 47.5 | 51.7 | 62.6 | 0.0016 | 13 | 8 |
| 506 | Simpson, Garret | EVA_OTT | Cutter | LHH | 36 | 52.9 | 40.0 | 49.0 | 48.9 | -0.0019 | 17 | 9 |
| 543 | Salata, Derek | SCH_BOO | Cutter | LHH | 26 | 48.2 | 48.4 | 48.2 | 45.1 | 0.0020 | 20 | 10 |
| 551 | Cook, Cole | SCH_BOO | Cutter | LHH | 28 | 46.8 | 51.1 | 48.1 | 44.3 | 0.0033 | 21 | 11 |
| 595 | MacMillan, Blake | TRO_AIG | Cutter | LHH | 37 | 49.8 | 41.8 | 47.4 | 39.9 | -0.0010 | 22 | 12 |
| 596 | Petschke, Ben | EVA_OTT | Cutter | LHH | 128 | 46.5 | 49.4 | 47.4 | 39.8 | 0.0025 | 23 | 13 |
| 681 | Binns, Malik | NEW_JER6 | Cutter | LHH | 30 | 45.8 | 45.3 | 45.6 | 31.2 | 0.0006 | 29 | 14 |
| 771 | Williams, Brian | MIS_MUD | Cutter | LHH | 45 | 45.9 | 38.9 | 43.8 | 22.1 | -0.0024 | 31 | 15 |
| 877 | Morgan, Cooper | QUE_CAP | Cutter | LHH | 25 | 43.9 | 33.4 | 40.8 | 11.3 | -0.0049 | 34 | 16 |
| 909 | Parks, Pavin | LAK_ERI24 | Cutter | LHH | 39 | 38.1 | 44.0 | 39.9 | 8.1 | 0.0000 | 35 | 17 |

### Cutter vs RHH

| Rank | Pitcher | Team | Pitch Type | Batter Side | Split Pitches | PVS | Loc | Final | Final % | Avg Loc Adv | Type Rank | Type/Side Rank |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 16 | Correa, Nelvin | QUE_CAP | Cutter | RHH | 28 | 74.2 | 52.3 | 67.6 | 98.5 | 0.0038 | 1 | 1 |
| 43 | Webster, Evan | FLO_Y'A | Cutter | RHH | 29 | 75.4 | 38.2 | 64.2 | 95.7 | -0.0027 | 3 | 2 |
| 274 | Saturria, Michael | NEW_ENG23 | Cutter | RHH | 79 | 57.4 | 45.5 | 53.8 | 72.4 | 0.0007 | 6 | 3 |
| 304 | Gamelin, Shaun | JOL_SLA | Cutter | RHH | 62 | 55.8 | 47.2 | 53.2 | 69.3 | 0.0015 | 10 | 4 |
| 328 | Gorgen, Grady | NEW_YOR13 | Cutter | RHH | 28 | 57.1 | 42.9 | 52.9 | 66.9 | -0.0005 | 12 | 5 |
| 399 | Moore, Kyle | SCH_BOO | Cutter | RHH | 73 | 57.1 | 37.5 | 51.3 | 59.7 | -0.0030 | 14 | 6 |
| 445 | Langrell, Connor | MIS_MUD | Cutter | RHH | 101 | 53.6 | 42.9 | 50.4 | 55.1 | -0.0005 | 15 | 7 |
| 492 | Simpson, Garret | EVA_OTT | Cutter | RHH | 28 | 52.9 | 41.5 | 49.5 | 50.3 | -0.0012 | 16 | 8 |
| 523 | Salata, Derek | SCH_BOO | Cutter | RHH | 39 | 48.2 | 49.9 | 48.7 | 47.2 | 0.0027 | 18 | 9 |
| 532 | Debban, Caleb | NEW_JER6 | Cutter | RHH | 34 | 49.8 | 45.0 | 48.4 | 46.3 | 0.0005 | 19 | 10 |
| 608 | Petschke, Ben | EVA_OTT | Cutter | RHH | 82 | 46.5 | 48.2 | 47.0 | 38.6 | 0.0019 | 24 | 11 |
| 652 | MacMillan, Blake | TRO_AIG | Cutter | RHH | 51 | 49.8 | 37.8 | 46.2 | 34.1 | -0.0029 | 25 | 12 |
| 654 | Williams, Brian | MIS_MUD | Cutter | RHH | 62 | 45.9 | 46.8 | 46.2 | 33.9 | 0.0013 | 26 | 13 |
| 663 | Morgan, Cooper | QUE_CAP | Cutter | RHH | 27 | 43.9 | 50.8 | 46.0 | 33.0 | 0.0032 | 27 | 14 |
| 666 | Binns, Malik | NEW_JER6 | Cutter | RHH | 48 | 45.8 | 46.2 | 45.9 | 32.7 | 0.0010 | 28 | 15 |
| 727 | Cook, Cole | SCH_BOO | Cutter | RHH | 65 | 46.8 | 40.1 | 44.8 | 26.5 | -0.0018 | 30 | 16 |
| 831 | Parks, Pavin | LAK_ERI24 | Cutter | RHH | 73 | 38.1 | 52.2 | 42.4 | 16.0 | 0.0038 | 32 | 17 |
| 842 | Thiels, Brenton | MIS_MUD | Cutter | RHH | 28 | 41.4 | 43.7 | 42.1 | 14.9 | -0.0002 | 33 | 18 |
| 940 | Jones, Breyln | NEW_JER6 | Cutter | RHH | 33 | 32.3 | 51.5 | 38.0 | 5.0 | 0.0035 | 36 | 19 |

### Four-Seam vs LHH

| Rank | Pitcher | Team | Pitch Type | Batter Side | Split Pitches | PVS | Loc | Final | Final % | Avg Loc Adv | Type Rank | Type/Side Rank |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 11 | Grounds, Jackson | DOW_EAS1 | Four-Seam | LHH | 59 | 72.4 | 60.9 | 69.0 | 99.0 | 0.0078 | 3 | 1 |
| 17 | Davis, Tyler | WIN_CIT29 | Four-Seam | LHH | 43 | 72.5 | 56.0 | 67.6 | 98.4 | 0.0055 | 4 | 2 |
| 34 | Wehrle, Tyler | WIN_CIT29 | Four-Seam | LHH | 75 | 60.1 | 76.5 | 65.0 | 96.7 | 0.0151 | 6 | 3 |
| 36 | Foster, Kobe | WAS_WIL3 | Four-Seam | LHH | 88 | 62.2 | 71.2 | 64.9 | 96.5 | 0.0126 | 7 | 4 |
| 46 | Cartwright, Eli | GAT_GRI | Four-Seam | LHH | 42 | 63.1 | 66.5 | 64.1 | 95.4 | 0.0104 | 8 | 5 |
| 49 | Rodriguez, Joe Joe | NEW_JER6 | Four-Seam | LHH | 27 | 65.1 | 60.5 | 63.7 | 95.1 | 0.0077 | 9 | 6 |
| 65 | Zentko, Dylan | EVA_OTT | Four-Seam | LHH | 41 | 60.7 | 64.3 | 61.8 | 93.5 | 0.0094 | 14 | 7 |
| 73 | Zaffiro, Cole | SCH_BOO | Four-Seam | LHH | 44 | 61.5 | 60.8 | 61.3 | 92.7 | 0.0078 | 16 | 8 |
| 77 | Cameron, Zach | WIN_CIT29 | Four-Seam | LHH | 30 | 66.5 | 48.5 | 61.1 | 92.3 | 0.0021 | 18 | 9 |
| 81 | Herbert, Andrew | WAS_WIL3 | Four-Seam | LHH | 35 | 57.2 | 69.6 | 60.9 | 91.9 | 0.0119 | 20 | 10 |
| 100 | Widener, Jacob | SUS_COU1 | Four-Seam | LHH | 26 | 61.9 | 55.0 | 59.8 | 90.0 | 0.0051 | 22 | 11 |
| 104 | Anderson, Colt | WAS_WIL3 | Four-Seam | LHH | 37 | 60.7 | 57.4 | 59.7 | 89.6 | 0.0062 | 24 | 12 |
| 107 | Kines, Gunnar | JOL_SLA | Four-Seam | LHH | 121 | 56.9 | 66.1 | 59.6 | 89.3 | 0.0103 | 25 | 13 |
| 112 | Langhorne, Miles | SUS_COU1 | Four-Seam | LHH | 30 | 58.5 | 61.3 | 59.4 | 88.8 | 0.0080 | 27 | 14 |
| 116 | Eisenbarger, Jack | QUE_CAP | Four-Seam | LHH | 50 | 62.0 | 52.8 | 59.3 | 88.4 | 0.0041 | 28 | 15 |
| 121 | Shears, Tanner | SCH_BOO | Four-Seam | LHH | 61 | 61.5 | 52.3 | 58.8 | 87.9 | 0.0039 | 31 | 16 |
| 139 | Garcia, Brett | OTT_TIT | Four-Seam | LHH | 73 | 57.3 | 59.3 | 57.9 | 86.0 | 0.0071 | 38 | 17 |
| 149 | Marynczak, Arlo | TRI_VAL | Four-Seam | LHH | 52 | 53.4 | 67.4 | 57.6 | 85.0 | 0.0109 | 44 | 18 |
| 150 | Quigley, Michael | NEW_ENG23 | Four-Seam | LHH | 84 | 59.6 | 52.1 | 57.4 | 84.9 | 0.0037 | 45 | 19 |
| 158 | Fowler, Dalton | SUS_COU1 | Four-Seam | LHH | 43 | 52.9 | 67.1 | 57.1 | 84.1 | 0.0107 | 48 | 20 |
| 161 | Alpern, Liam | FLO_Y'A | Four-Seam | LHH | 86 | 53.9 | 64.7 | 57.1 | 83.8 | 0.0096 | 49 | 21 |
| 162 | Mercado, Nelson | OTT_TIT | Four-Seam | LHH | 39 | 60.1 | 50.1 | 57.1 | 83.7 | 0.0028 | 50 | 22 |
| 163 | Moore, Kyle | SCH_BOO | Four-Seam | LHH | 64 | 54.8 | 62.3 | 57.1 | 83.6 | 0.0085 | 51 | 23 |
| 164 | Foy, Corbin | LAK_ERI24 | Four-Seam | LHH | 48 | 64.6 | 39.4 | 57.0 | 83.5 | -0.0021 | 52 | 24 |
| 169 | Almanzar, Elian | DOW_EAS1 | Four-Seam | LHH | 82 | 54.0 | 63.7 | 56.9 | 83.0 | 0.0092 | 54 | 25 |

### Four-Seam vs RHH

| Rank | Pitcher | Team | Pitch Type | Batter Side | Split Pitches | PVS | Loc | Final | Final % | Avg Loc Adv | Type Rank | Type/Side Rank |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 4 | Davis, Tyler | WIN_CIT29 | Four-Seam | RHH | 33 | 72.5 | 70.3 | 71.9 | 99.7 | 0.0122 | 1 | 1 |
| 7 | Grounds, Jackson | DOW_EAS1 | Four-Seam | RHH | 48 | 72.4 | 67.2 | 70.8 | 99.4 | 0.0107 | 2 | 2 |
| 27 | Cameron, Zach | WIN_CIT29 | Four-Seam | RHH | 34 | 66.5 | 64.8 | 66.0 | 97.4 | 0.0096 | 5 | 3 |
| 50 | Shears, Tanner | SCH_BOO | Four-Seam | RHH | 67 | 61.5 | 68.9 | 63.7 | 95.0 | 0.0116 | 10 | 4 |
| 51 | Mercado, Nelson | OTT_TIT | Four-Seam | RHH | 42 | 60.1 | 71.5 | 63.5 | 94.9 | 0.0127 | 11 | 5 |
| 56 | Perez, Kelvin | WAS_WIL3 | Four-Seam | RHH | 27 | 67.7 | 52.1 | 63.0 | 94.4 | 0.0037 | 12 | 6 |
| 64 | Rodriguez, Joe Joe | NEW_JER6 | Four-Seam | RHH | 28 | 65.1 | 54.1 | 61.8 | 93.6 | 0.0047 | 13 | 7 |
| 70 | Foster, Kobe | WAS_WIL3 | Four-Seam | RHH | 164 | 62.2 | 59.6 | 61.4 | 93.0 | 0.0072 | 15 | 8 |
| 74 | MacMillan, Blake | TRO_AIG | Four-Seam | RHH | 54 | 61.2 | 61.2 | 61.2 | 92.6 | 0.0080 | 17 | 9 |
| 79 | Zaffiro, Cole | SCH_BOO | Four-Seam | RHH | 64 | 61.5 | 59.7 | 61.0 | 92.1 | 0.0073 | 19 | 10 |
| 87 | Wehrle, Tyler | WIN_CIT29 | Four-Seam | RHH | 152 | 60.1 | 61.7 | 60.6 | 91.3 | 0.0082 | 21 | 11 |
| 101 | Kines, Gunnar | JOL_SLA | Four-Seam | RHH | 131 | 56.9 | 66.7 | 59.8 | 89.9 | 0.0105 | 23 | 12 |
| 111 | Langhorne, Miles | SUS_COU1 | Four-Seam | RHH | 40 | 58.5 | 61.3 | 59.4 | 88.9 | 0.0080 | 26 | 13 |
| 117 | Quigley, Michael | NEW_ENG23 | Four-Seam | RHH | 61 | 59.6 | 57.7 | 59.0 | 88.3 | 0.0063 | 29 | 14 |
| 120 | Ginn, Landon | WAS_WIL3 | Four-Seam | RHH | 44 | 53.3 | 71.6 | 58.8 | 88.0 | 0.0128 | 30 | 15 |
| 129 | Widener, Jacob | SUS_COU1 | Four-Seam | RHH | 34 | 61.9 | 50.1 | 58.4 | 87.0 | 0.0028 | 32 | 16 |
| 131 | Binns, Malik | NEW_JER6 | Four-Seam | RHH | 25 | 48.8 | 80.0 | 58.2 | 86.8 | 0.0190 | 33 | 17 |
| 134 | Kelly, Colin | SUS_COU1 | Four-Seam | RHH | 49 | 58.0 | 58.2 | 58.0 | 86.5 | 0.0066 | 34 | 18 |
| 135 | Westcott, Zac | FLO_Y'A | Four-Seam | RHH | 124 | 55.5 | 63.9 | 58.0 | 86.4 | 0.0092 | 35 | 19 |
| 136 | Foy, Corbin | LAK_ERI24 | Four-Seam | RHH | 47 | 64.6 | 42.6 | 58.0 | 86.3 | -0.0007 | 36 | 20 |
| 137 | Cartwright, Eli | GAT_GRI | Four-Seam | RHH | 79 | 63.1 | 45.9 | 57.9 | 86.2 | 0.0009 | 37 | 21 |
| 141 | Hagan, Jack | DOW_EAS1 | Four-Seam | RHH | 31 | 62.8 | 46.2 | 57.8 | 85.8 | 0.0010 | 39 | 22 |
| 143 | Maher, Adam | TRI_VAL | Four-Seam | RHH | 46 | 61.5 | 48.8 | 57.7 | 85.6 | 0.0022 | 40 | 23 |
| 145 | Calderon, Jean | LAK_ERI24 | Four-Seam | RHH | 51 | 54.8 | 64.4 | 57.7 | 85.4 | 0.0095 | 41 | 24 |
| 147 | Thebiay, Nolan | EVA_OTT | Four-Seam | RHH | 164 | 57.6 | 57.9 | 57.7 | 85.2 | 0.0065 | 42 | 25 |

### Sinker vs LHH

| Rank | Pitcher | Team | Pitch Type | Batter Side | Split Pitches | PVS | Loc | Final | Final % | Avg Loc Adv | Type Rank | Type/Side Rank |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 54 | Lawson, Nathan | FLO_Y'A | Sinker | LHH | 28 | 62.6 | 64.5 | 63.2 | 94.6 | 0.0095 | 2 | 1 |
| 68 | Widener, Jacob | SUS_COU1 | Sinker | LHH | 28 | 66.4 | 50.1 | 61.5 | 93.2 | 0.0028 | 4 | 2 |
| 72 | Mannering, Shawn | DOW_EAS1 | Sinker | LHH | 27 | 62.3 | 58.9 | 61.3 | 92.8 | 0.0069 | 5 | 3 |
| 95 | Colon, Jeffrey | TRO_AIG | Sinker | LHH | 30 | 63.8 | 51.5 | 60.1 | 90.5 | 0.0035 | 9 | 4 |
| 123 | Plumadore, Carson | WIN_CIT29 | Sinker | LHH | 47 | 61.5 | 51.8 | 58.6 | 87.7 | 0.0036 | 10 | 5 |
| 124 | Gregory, Ben | GAT_GRI | Sinker | LHH | 31 | 56.8 | 62.8 | 58.6 | 87.6 | 0.0087 | 11 | 6 |
| 153 | Cerda, Junior | EVA_OTT | Sinker | LHH | 28 | 64.9 | 39.5 | 57.2 | 84.6 | -0.0021 | 14 | 7 |
| 165 | Daly, Ryan | JOL_SLA | Sinker | LHH | 47 | 58.0 | 54.6 | 57.0 | 83.4 | 0.0049 | 16 | 8 |
| 166 | McCartney, Seth | MIS_MUD | Sinker | LHH | 67 | 56.5 | 58.1 | 57.0 | 83.3 | 0.0065 | 17 | 9 |
| 197 | Cook, Cole | SCH_BOO | Sinker | LHH | 29 | 57.4 | 53.0 | 56.1 | 80.2 | 0.0042 | 20 | 10 |
| 205 | Kelly, Aiden | TRI_VAL | Sinker | LHH | 51 | 52.3 | 63.5 | 55.7 | 79.4 | 0.0091 | 21 | 11 |
| 216 | Kines, Gunnar | JOL_SLA | Sinker | LHH | 30 | 53.5 | 59.8 | 55.4 | 78.2 | 0.0073 | 22 | 12 |
| 218 | Morgan, Marcus | JOL_SLA | Sinker | LHH | 54 | 58.7 | 47.4 | 55.3 | 78.0 | 0.0016 | 23 | 13 |
| 220 | Stuka, Ted | OTT_TIT | Sinker | LHH | 45 | 55.0 | 55.8 | 55.2 | 77.8 | 0.0055 | 24 | 14 |
| 231 | Johnson, Caiden | OTT_TIT | Sinker | LHH | 31 | 57.2 | 49.6 | 54.9 | 76.7 | 0.0026 | 26 | 15 |
| 253 | Fritz, AJ | MIS_MUD | Sinker | LHH | 31 | 55.4 | 51.8 | 54.3 | 74.5 | 0.0036 | 28 | 16 |
| 257 | Harper, Scott | NEW_YOR13 | Sinker | LHH | 41 | 51.9 | 59.6 | 54.2 | 74.1 | 0.0072 | 29 | 17 |
| 259 | Aldeano, Austin | TRO_AIG | Sinker | LHH | 45 | 54.2 | 54.2 | 54.2 | 73.9 | 0.0047 | 30 | 18 |
| 262 | Hensey, Rob | SUS_COU1 | Sinker | LHH | 79 | 54.9 | 52.1 | 54.1 | 73.6 | 0.0038 | 32 | 19 |
| 268 | Vecerka, Boris | QUE_CAP | Sinker | LHH | 52 | 52.3 | 57.7 | 53.9 | 73.0 | 0.0063 | 33 | 20 |
| 275 | Henderson, Drew | DOW_EAS1 | Sinker | LHH | 43 | 55.6 | 49.4 | 53.7 | 72.3 | 0.0025 | 34 | 21 |
| 298 | Sechrist, Zander | WAS_WIL3 | Sinker | LHH | 28 | 43.7 | 75.7 | 53.3 | 69.9 | 0.0147 | 38 | 22 |
| 302 | Grounds, Jackson | DOW_EAS1 | Sinker | LHH | 75 | 56.8 | 45.0 | 53.3 | 69.5 | 0.0005 | 39 | 23 |
| 338 | Turner, Eric | JOL_SLA | Sinker | LHH | 33 | 54.8 | 47.6 | 52.6 | 65.9 | 0.0016 | 43 | 24 |
| 341 | Burcham, Jacob | GAT_GRI | Sinker | LHH | 57 | 54.7 | 47.6 | 52.5 | 65.6 | 0.0016 | 44 | 25 |

### Sinker vs RHH

| Rank | Pitcher | Team | Pitch Type | Batter Side | Split Pitches | PVS | Loc | Final | Final % | Avg Loc Adv | Type Rank | Type/Side Rank |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 37 | Still, Stephen | TRI_VAL | Sinker | RHH | 50 | 68.1 | 57.3 | 64.9 | 96.4 | 0.0062 | 1 | 1 |
| 60 | Mannering, Shawn | DOW_EAS1 | Sinker | RHH | 32 | 62.3 | 62.1 | 62.3 | 94.0 | 0.0084 | 3 | 2 |
| 80 | Cerda, Junior | EVA_OTT | Sinker | RHH | 26 | 64.9 | 51.8 | 60.9 | 92.0 | 0.0036 | 6 | 3 |
| 82 | Colon, Jeffrey | TRO_AIG | Sinker | RHH | 26 | 63.8 | 53.5 | 60.7 | 91.8 | 0.0044 | 7 | 4 |
| 83 | Plumadore, Carson | WIN_CIT29 | Sinker | RHH | 32 | 61.5 | 58.7 | 60.7 | 91.7 | 0.0068 | 8 | 5 |
| 127 | Pierson, Kenny | LAK_ERI24 | Sinker | RHH | 69 | 60.9 | 53.0 | 58.5 | 87.2 | 0.0042 | 12 | 6 |
| 128 | Widener, Jacob | SUS_COU1 | Sinker | RHH | 37 | 66.4 | 39.8 | 58.4 | 87.1 | -0.0019 | 13 | 7 |
| 155 | Gregory, Ben | GAT_GRI | Sinker | RHH | 45 | 56.8 | 58.0 | 57.2 | 84.4 | 0.0065 | 15 | 8 |
| 174 | Turner, Eric | JOL_SLA | Sinker | RHH | 42 | 54.8 | 61.0 | 56.7 | 82.5 | 0.0079 | 18 | 9 |
| 183 | Cook, Cole | SCH_BOO | Sinker | RHH | 36 | 57.4 | 54.2 | 56.4 | 81.6 | 0.0047 | 19 | 10 |
| 225 | McCartney, Seth | MIS_MUD | Sinker | RHH | 53 | 56.5 | 51.9 | 55.1 | 77.3 | 0.0037 | 25 | 11 |
| 232 | Morgan, Marcus | JOL_SLA | Sinker | RHH | 28 | 58.7 | 46.1 | 54.9 | 76.6 | 0.0010 | 27 | 12 |
| 260 | Kelly, Colin | SUS_COU1 | Sinker | RHH | 53 | 54.3 | 53.8 | 54.2 | 73.8 | 0.0045 | 31 | 13 |
| 278 | Lawson, Nathan | FLO_Y'A | Sinker | RHH | 27 | 62.6 | 32.9 | 53.7 | 72.0 | -0.0051 | 35 | 14 |
| 279 | Stuka, Ted | OTT_TIT | Sinker | RHH | 29 | 55.0 | 50.5 | 53.7 | 71.9 | 0.0030 | 36 | 15 |
| 286 | Daly, Ryan | JOL_SLA | Sinker | RHH | 55 | 58.0 | 43.1 | 53.5 | 71.2 | -0.0004 | 37 | 16 |
| 315 | Burcham, Jacob | GAT_GRI | Sinker | RHH | 95 | 54.7 | 49.2 | 53.0 | 68.2 | 0.0024 | 40 | 17 |
| 329 | Aldeano, Austin | TRO_AIG | Sinker | RHH | 25 | 54.2 | 49.6 | 52.8 | 66.8 | 0.0026 | 41 | 18 |
| 335 | Riedel, Caleb | SCH_BOO | Sinker | RHH | 28 | 58.6 | 38.9 | 52.7 | 66.2 | -0.0024 | 42 | 19 |
| 354 | Milburn, Isaac | FLO_Y'A | Sinker | RHH | 51 | 51.4 | 54.0 | 52.2 | 64.3 | 0.0046 | 47 | 20 |
| 355 | Hensey, Rob | SUS_COU1 | Sinker | RHH | 190 | 54.9 | 45.7 | 52.2 | 64.2 | 0.0008 | 48 | 21 |
| 363 | Armstrong, Andrew | NEW_YOR13 | Sinker | RHH | 42 | 52.3 | 50.9 | 51.9 | 63.4 | 0.0032 | 50 | 22 |
| 374 | Hoeymans, Jack | GAT_GRI | Sinker | RHH | 35 | 50.6 | 54.1 | 51.7 | 62.2 | 0.0047 | 52 | 23 |
| 380 | Kelly, Aiden | TRI_VAL | Sinker | RHH | 27 | 52.3 | 49.8 | 51.6 | 61.6 | 0.0027 | 53 | 24 |
| 391 | Grounds, Jackson | DOW_EAS1 | Sinker | RHH | 41 | 56.8 | 38.8 | 51.4 | 60.5 | -0.0024 | 56 | 25 |

### Slider vs LHH

| Rank | Pitcher | Team | Pitch Type | Batter Side | Split Pitches | PVS | Loc | Final | Final % | Avg Loc Adv | Type Rank | Type/Side Rank |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 8 | Carroll, Jake | JOL_SLA | Slider | LHH | 40 | 80.0 | 46.1 | 69.8 | 99.3 | 0.0009 | 4 | 1 |
| 9 | Alpern, Liam | FLO_Y'A | Slider | LHH | 38 | 74.3 | 58.8 | 69.7 | 99.2 | 0.0068 | 5 | 2 |
| 14 | McEvoy, Aidan | FLO_Y'A | Slider | LHH | 51 | 74.6 | 53.1 | 68.2 | 98.7 | 0.0042 | 8 | 3 |
| 18 | Ryan, Dillon | NEW_ENG23 | Slider | LHH | 54 | 76.3 | 47.2 | 67.6 | 98.3 | 0.0015 | 10 | 4 |
| 19 | Jones, Logan | TRI_VAL | Slider | LHH | 33 | 72.7 | 54.3 | 67.2 | 98.2 | 0.0048 | 11 | 5 |
| 24 | Webster, Evan | FLO_Y'A | Slider | LHH | 36 | 71.9 | 53.3 | 66.3 | 97.7 | 0.0043 | 14 | 6 |
| 28 | Foster, Kobe | WAS_WIL3 | Slider | LHH | 76 | 73.0 | 49.1 | 65.8 | 97.3 | 0.0023 | 15 | 7 |
| 40 | Bargo, Casey | NEW_ENG23 | Slider | LHH | 27 | 71.8 | 46.8 | 64.3 | 96.1 | 0.0013 | 23 | 8 |
| 98 | Armstrong, Andrew | NEW_YOR13 | Slider | LHH | 40 | 61.9 | 55.2 | 59.9 | 90.2 | 0.0052 | 42 | 9 |
| 106 | Cook, Cole | SCH_BOO | Slider | LHH | 87 | 60.0 | 58.8 | 59.7 | 89.4 | 0.0069 | 45 | 10 |
| 108 | Morin, Jacob | QUE_CAP | Slider | LHH | 25 | 64.6 | 47.6 | 59.5 | 89.2 | 0.0016 | 46 | 11 |
| 142 | Joven, Art | MIS_MUD | Slider | LHH | 93 | 58.4 | 56.3 | 57.7 | 85.7 | 0.0057 | 56 | 12 |
| 146 | Long, Maddox | WAS_WIL3 | Slider | LHH | 33 | 64.8 | 41.2 | 57.7 | 85.3 | -0.0013 | 57 | 13 |
| 154 | Tokar, Heitor | OTT_TIT | Slider | LHH | 29 | 61.6 | 47.1 | 57.2 | 84.5 | 0.0014 | 58 | 14 |
| 160 | Dima, Josh | GAT_GRI | Slider | LHH | 60 | 56.3 | 59.0 | 57.1 | 83.9 | 0.0070 | 59 | 15 |
| 173 | Hensey, Rob | SUS_COU1 | Slider | LHH | 45 | 57.6 | 54.8 | 56.7 | 82.6 | 0.0050 | 60 | 16 |
| 176 | Martinez, Mason | TRI_VAL | Slider | LHH | 32 | 58.5 | 52.3 | 56.6 | 82.3 | 0.0039 | 61 | 17 |
| 180 | Odonnell, Brendan | NEW_ENG23 | Slider | LHH | 47 | 57.7 | 53.8 | 56.5 | 81.9 | 0.0046 | 62 | 18 |
| 182 | Majick, Eli | NEW_ENG23 | Slider | LHH | 42 | 56.3 | 56.9 | 56.5 | 81.7 | 0.0060 | 64 | 19 |
| 195 | Whitesell, Max | FLO_Y'A | Slider | LHH | 35 | 58.8 | 50.0 | 56.2 | 80.4 | 0.0028 | 67 | 20 |
| 211 | Brito, Richard | NEW_ENG23 | Slider | LHH | 37 | 58.1 | 49.4 | 55.5 | 78.7 | 0.0025 | 72 | 21 |
| 221 | Nova, Fraynel | LAK_ERI24 | Slider | LHH | 98 | 58.2 | 48.4 | 55.2 | 77.7 | 0.0020 | 73 | 22 |
| 236 | Kaminer, Brandon | DOW_EAS1 | Slider | LHH | 33 | 54.7 | 54.9 | 54.8 | 76.2 | 0.0051 | 75 | 23 |
| 261 | Milburn, Isaac | FLO_Y'A | Slider | LHH | 69 | 54.6 | 53.0 | 54.1 | 73.7 | 0.0042 | 81 | 24 |
| 265 | Perozzi, John | SUS_COU1 | Slider | LHH | 37 | 59.3 | 41.7 | 54.0 | 73.3 | -0.0011 | 82 | 25 |

### Slider vs RHH

| Rank | Pitcher | Team | Pitch Type | Batter Side | Split Pitches | PVS | Loc | Final | Final % | Avg Loc Adv | Type Rank | Type/Side Rank |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | Perez, Kelvin | WAS_WIL3 | Slider | RHH | 45 | 72.4 | 80.0 | 74.6 | 100.0 | 0.0183 | 1 | 1 |
| 2 | Harper, Scott | NEW_YOR13 | Slider | RHH | 98 | 77.6 | 67.3 | 74.5 | 99.9 | 0.0108 | 2 | 2 |
| 3 | Bargo, Casey | NEW_ENG23 | Slider | RHH | 29 | 71.8 | 72.3 | 71.9 | 99.8 | 0.0131 | 3 | 3 |
| 10 | Ryan, Dillon | NEW_ENG23 | Slider | RHH | 39 | 76.3 | 53.4 | 69.4 | 99.1 | 0.0043 | 6 | 4 |
| 13 | Kirby, Zach | WAS_WIL3 | Slider | RHH | 102 | 67.9 | 69.0 | 68.2 | 98.8 | 0.0116 | 7 | 5 |
| 15 | Smith, Jackson | MIS_MUD | Slider | RHH | 52 | 68.5 | 65.9 | 67.7 | 98.6 | 0.0101 | 9 | 6 |
| 20 | Harajli, Ahmad | FLO_Y'A | Slider | RHH | 39 | 68.9 | 62.0 | 66.8 | 98.1 | 0.0083 | 12 | 7 |
| 21 | Donnan, Blake | FLO_Y'A | Slider | RHH | 52 | 68.5 | 62.7 | 66.8 | 98.0 | 0.0087 | 13 | 8 |
| 30 | Alpern, Liam | FLO_Y'A | Slider | RHH | 40 | 74.3 | 45.7 | 65.8 | 97.1 | 0.0008 | 16 | 9 |
| 31 | Nakata, Yuto | QUE_CAP | Slider | RHH | 50 | 67.1 | 62.7 | 65.7 | 97.0 | 0.0087 | 17 | 10 |
| 32 | Long, Maddox | WAS_WIL3 | Slider | RHH | 111 | 64.8 | 67.5 | 65.6 | 96.9 | 0.0109 | 18 | 11 |
| 33 | Jones, Logan | TRI_VAL | Slider | RHH | 32 | 72.7 | 48.5 | 65.5 | 96.8 | 0.0021 | 19 | 12 |
| 35 | Lefebvre, Charles | TRO_AIG | Slider | RHH | 53 | 62.3 | 71.0 | 64.9 | 96.6 | 0.0125 | 20 | 13 |
| 38 | Nova, Fraynel | LAK_ERI24 | Slider | RHH | 100 | 58.2 | 80.0 | 64.7 | 96.3 | 0.0171 | 21 | 14 |
| 39 | Perozzi, John | SUS_COU1 | Slider | RHH | 46 | 59.3 | 76.0 | 64.3 | 96.2 | 0.0148 | 22 | 15 |
| 48 | Whitesell, Max | FLO_Y'A | Slider | RHH | 77 | 58.8 | 75.3 | 63.7 | 95.2 | 0.0145 | 24 | 16 |
| 52 | Vailes, Gage | GAT_GRI | Slider | RHH | 125 | 60.6 | 69.8 | 63.4 | 94.8 | 0.0120 | 25 | 17 |
| 53 | Cohn, Cooper | NIU_HUS | Slider | RHH | 27 | 58.1 | 75.3 | 63.2 | 94.7 | 0.0145 | 26 | 18 |
| 55 | McEvoy, Aidan | FLO_Y'A | Slider | RHH | 27 | 74.6 | 36.2 | 63.1 | 94.5 | -0.0036 | 27 | 19 |
| 58 | Morin, Jacob | QUE_CAP | Slider | RHH | 60 | 64.6 | 58.3 | 62.7 | 94.2 | 0.0066 | 28 | 20 |
| 59 | Duby, Bill | NEW_JER6 | Slider | RHH | 38 | 58.3 | 71.6 | 62.3 | 94.1 | 0.0128 | 29 | 21 |
| 61 | Hagan, Jack | DOW_EAS1 | Slider | RHH | 73 | 57.2 | 73.7 | 62.2 | 93.9 | 0.0138 | 30 | 22 |
| 62 | Garcia, Hector | WAS_WIL3 | Slider | RHH | 36 | 56.9 | 74.1 | 62.0 | 93.8 | 0.0139 | 31 | 23 |
| 63 | Heredia-Bustos, Rolando | DOW_EAS1 | Slider | RHH | 181 | 59.0 | 68.6 | 61.9 | 93.7 | 0.0114 | 32 | 24 |
| 66 | Leak, Anthony | NEW_YOR13 | Slider | RHH | 94 | 57.2 | 72.0 | 61.7 | 93.4 | 0.0130 | 33 | 25 |

### Splitter vs LHH

| Rank | Pitcher | Team | Pitch Type | Batter Side | Split Pitches | PVS | Loc | Final | Final % | Avg Loc Adv | Type Rank | Type/Side Rank |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 23 | Vitas, Ben | JOL_SLA | Splitter | LHH | 38 | 75.0 | 45.9 | 66.3 | 97.8 | 0.0009 | 1 | 1 |
| 42 | Garcia, Hector | WAS_WIL3 | Splitter | LHH | 59 | 71.8 | 46.6 | 64.2 | 95.9 | 0.0012 | 2 | 2 |
| 126 | Pindel, Buddie | SCH_BOO | Splitter | LHH | 50 | 63.6 | 46.7 | 58.5 | 87.3 | 0.0012 | 5 | 3 |
| 130 | Villers, Ian | QUE_CAP | Splitter | LHH | 39 | 64.3 | 44.0 | 58.2 | 86.9 | -0.0000 | 6 | 4 |
| 196 | Thompson, Ross | SCH_BOO | Splitter | LHH | 69 | 59.8 | 47.6 | 56.1 | 80.3 | 0.0017 | 7 | 5 |
| 241 | Salata, Derek | SCH_BOO | Splitter | LHH | 64 | 57.6 | 47.5 | 54.6 | 75.7 | 0.0016 | 8 | 6 |
| 726 | Nakata, Yuto | QUE_CAP | Splitter | LHH | 47 | 46.3 | 41.1 | 44.8 | 26.6 | -0.0014 | 9 | 7 |

### Splitter vs RHH

| Rank | Pitcher | Team | Pitch Type | Batter Side | Split Pitches | PVS | Loc | Final | Final % | Avg Loc Adv | Type Rank | Type/Side Rank |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 118 | Villers, Ian | QUE_CAP | Splitter | RHH | 25 | 64.3 | 46.4 | 58.9 | 88.2 | 0.0011 | 3 | 1 |
| 125 | Pindel, Buddie | SCH_BOO | Splitter | RHH | 30 | 63.6 | 46.9 | 58.6 | 87.4 | 0.0013 | 4 | 2 |
