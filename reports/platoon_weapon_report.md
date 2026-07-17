# Platoon Weapon Report

- Input file: `data\processed\pitch_leaderboard_splits.csv`
- Output file: `data\processed\platoon_weapon_scores.csv`
- Input split rows: 1,527
- Pitcher + pitch type rows with both RHH and LHH scores: 674
- Platoon gap: `score_vs_rhh - score_vs_lhh`
- Positive gap means the pitch grades better versus RHH. Negative gap means it grades better versus LHH.
- Reverse Split Weapon is defined from this file only: the pitch's gap is at least 5 points and opposite the typical median gap for that pitch type.

## Category Counts

| Category | Count |
|---|---:|
| Balanced Weapon | 519 |
| Right-Handed Killer | 108 |
| Left-Handed Killer | 36 |
| Reverse Split Weapon | 11 |

## Top 20 Right-Handed Killing Pitches

| Pitcher | Team | Pitch Type | RHH | LHH | Gap | Avg | R Pitches | L Pitches | Category |
|---|---|---|---|---|---|---|---|---|---|
| Thompson, Ross | SCH_BOO | Slider | 60.9 | 44.2 | 16.8 | 52.6 | 196 | 27 | Right-Handed Killer |
| Vailes, Gage | GAT_GRI | Slider | 64.1 | 49.5 | 14.6 | 56.8 | 220 | 95 | Right-Handed Killer |
| Hagan, Jack | DOW_EAS1 | Slider | 63.5 | 50.0 | 13.5 | 56.8 | 129 | 81 | Right-Handed Killer |
| Pardinho, Eric | OTT_TIT | Slider | 57.6 | 45.7 | 11.9 | 51.6 | 121 | 30 | Right-Handed Killer |
| Nova, Fraynel | LAK_ERI24 | Slider | 63.5 | 51.7 | 11.8 | 57.6 | 145 | 159 | Right-Handed Killer |
| Gamelin, Shaun | JOL_SLA | Slider | 58.9 | 47.1 | 11.7 | 53.0 | 43 | 32 | Right-Handed Killer |
| Perdomo, Rafael | QUE_CAP | Slider | 57.2 | 45.9 | 11.4 | 51.5 | 46 | 38 | Right-Handed Killer |
| Blair, Davis | DOW_EAS1 | Slider | 59.8 | 48.6 | 11.2 | 54.2 | 61 | 38 | Right-Handed Killer |
| Leak, Anthony | NEW_YOR13 | Slider | 63.5 | 52.4 | 11.1 | 57.9 | 166 | 94 | Right-Handed Killer |
| Bargo, Casey | NEW_ENG23 | Slider | 74.1 | 63.3 | 10.9 | 68.7 | 29 | 27 | Right-Handed Killer |
| Cerda, Junior | EVA_OTT | Slider | 57.3 | 46.5 | 10.8 | 51.9 | 54 | 30 | Right-Handed Killer |
| Heredia-Bustos, Rolando | DOW_EAS1 | Slider | 60.1 | 49.3 | 10.8 | 54.7 | 267 | 182 | Right-Handed Killer |
| Helt, Robert | LAK_ERI24 | Slider | 62.2 | 51.5 | 10.7 | 56.8 | 144 | 85 | Right-Handed Killer |
| Smith, Ethan | WIN_CIT29 | Slider | 57.6 | 47.1 | 10.5 | 52.3 | 30 | 28 | Right-Handed Killer |
| Turner, Eric | JOL_SLA | Slider | 55.0 | 44.5 | 10.5 | 49.7 | 124 | 79 | Right-Handed Killer |
| Ginn, Landon | WAS_WIL3 | Four-Seam | 59.8 | 49.5 | 10.3 | 54.6 | 67 | 75 | Right-Handed Killer |
| Cohn, Cooper | NIU_HUS | Slider | 62.1 | 51.8 | 10.2 | 57.0 | 27 | 36 | Right-Handed Killer |
| Vega, Lucas | TRO_AIG | Slider | 67.1 | 57.0 | 10.2 | 62.1 | 94 | 40 | Right-Handed Killer |
| Bice, Emmett | NEW_YOR13 | Slider | 61.1 | 51.8 | 9.2 | 56.5 | 133 | 140 | Right-Handed Killer |
| Petschke, Ben | EVA_OTT | Slider | 65.6 | 56.3 | 9.2 | 61.0 | 86 | 58 | Right-Handed Killer |

## Top 20 Left-Handed Killing Pitches

| Pitcher | Team | Pitch Type | RHH | LHH | Gap | Avg | R Pitches | L Pitches | Category |
|---|---|---|---|---|---|---|---|---|---|
| Fowler, Dalton | SUS_COU1 | Four-Seam | 46.1 | 56.5 | -10.3 | 51.3 | 46 | 43 | Left-Handed Killer |
| Cook, Cole | SCH_BOO | Slider | 47.6 | 55.7 | -8.0 | 51.6 | 71 | 124 | Reverse Split Weapon |
| Dill, Austin | TRI_VAL | Changeup | 52.3 | 59.9 | -7.6 | 56.1 | 86 | 118 | Left-Handed Killer |
| McEvoy, Aidan | FLO_Y'A | Slider | 60.3 | 67.9 | -7.6 | 64.1 | 38 | 69 | Reverse Split Weapon |
| Alpern, Liam | FLO_Y'A | Slider | 65.0 | 72.0 | -7.0 | 68.5 | 40 | 38 | Reverse Split Weapon |
| Walsh, John | MIS_MUD | Slider | 49.9 | 56.7 | -6.7 | 53.3 | 25 | 42 | Reverse Split Weapon |
| Odonnell, Brendan | NEW_ENG23 | Slider | 50.5 | 57.2 | -6.7 | 53.8 | 125 | 85 | Reverse Split Weapon |
| Dima, Josh | GAT_GRI | Slider | 52.2 | 58.8 | -6.6 | 55.5 | 44 | 75 | Reverse Split Weapon |
| Hensey, Rob | SUS_COU1 | Slider | 52.4 | 59.0 | -6.6 | 55.7 | 27 | 81 | Reverse Split Weapon |
| Alpern, Liam | FLO_Y'A | Four-Seam | 50.3 | 56.8 | -6.5 | 53.5 | 178 | 86 | Left-Handed Killer |
| Agosto, Justus | TRI_VAL | Four-Seam | 51.2 | 57.3 | -6.0 | 54.2 | 33 | 45 | Left-Handed Killer |
| Sechrist, Zander | WAS_WIL3 | Slider | 52.2 | 57.6 | -5.4 | 54.9 | 32 | 48 | Reverse Split Weapon |
| Cameron, Zach | WIN_CIT29 | Changeup | 51.4 | 56.7 | -5.3 | 54.1 | 70 | 135 | Left-Handed Killer |
| Ferguson, Francis | QUE_CAP | Four-Seam | 49.8 | 55.1 | -5.3 | 52.5 | 78 | 51 | Left-Handed Killer |
| Jones, Breyln | NEW_JER6 | Four-Seam | 51.6 | 56.8 | -5.3 | 54.2 | 25 | 28 | Left-Handed Killer |
| Webster, Evan | FLO_Y'A | Slider | 54.4 | 59.6 | -5.2 | 57.0 | 35 | 76 | Reverse Split Weapon |
| Milburn, Isaac | FLO_Y'A | Slider | 52.4 | 57.5 | -5.2 | 54.9 | 101 | 79 | Reverse Split Weapon |
| Maietta, Dante | WIN_CIT29 | Changeup | 58.3 | 63.4 | -5.1 | 60.8 | 109 | 150 | Left-Handed Killer |
| Eckaus, David | EVA_OTT | Slider | 54.6 | 59.8 | -5.1 | 57.2 | 60 | 115 | Reverse Split Weapon |
| Morgan, Cooper | QUE_CAP | Four-Seam | 54.4 | 59.4 | -5.0 | 56.9 | 31 | 34 | Left-Handed Killer |

## Top 20 Balanced Pitches

| Pitcher | Team | Pitch Type | RHH | LHH | Gap | Avg | R Pitches | L Pitches | Category |
|---|---|---|---|---|---|---|---|---|---|
| Leduc, Zachary | TRO_AIG | Slider | 71.5 | 71.0 | 0.5 | 71.3 | 46 | 32 | Balanced Weapon |
| Jones, Logan | TRI_VAL | Slider | 65.7 | 67.7 | -2.0 | 66.7 | 32 | 33 | Balanced Weapon |
| Rodriguez, Joe Joe | NEW_JER6 | Changeup | 64.4 | 66.8 | -2.4 | 65.6 | 33 | 92 | Balanced Weapon |
| Bohnert, Matthew | WIN_CIT29 | Curveball | 63.0 | 64.3 | -1.3 | 63.6 | 51 | 46 | Balanced Weapon |
| Riedel, Caleb | SCH_BOO | Sinker | 63.6 | 63.0 | 0.6 | 63.3 | 44 | 33 | Balanced Weapon |
| Harris, Everette | TRI_VAL | Changeup | 62.4 | 63.8 | -1.4 | 63.1 | 40 | 56 | Balanced Weapon |
| Wehrle, Tyler | WIN_CIT29 | Four-Seam | 61.7 | 63.6 | -1.9 | 62.6 | 156 | 80 | Balanced Weapon |
| Webster, Evan | FLO_Y'A | Cutter | 60.8 | 62.9 | -2.1 | 61.9 | 38 | 95 | Balanced Weapon |
| MacMillan, Blake | TRO_AIG | Slider | 61.3 | 62.4 | -1.1 | 61.8 | 43 | 63 | Balanced Weapon |
| Colon, Jeffrey | TRO_AIG | Sinker | 62.9 | 60.3 | 2.6 | 61.6 | 26 | 30 | Balanced Weapon |
| Mannering, Shawn | DOW_EAS1 | Sinker | 61.4 | 61.6 | -0.2 | 61.5 | 32 | 27 | Balanced Weapon |
| Salata, Derek | SCH_BOO | Curveball | 62.2 | 60.0 | 2.2 | 61.1 | 72 | 50 | Balanced Weapon |
| Coles, Chad | WAS_WIL3 | Splitter | 60.0 | 61.5 | -1.5 | 60.8 | 25 | 38 | Balanced Weapon |
| Correa, Nelvin | QUE_CAP | Cutter | 61.3 | 60.0 | 1.3 | 60.7 | 51 | 59 | Balanced Weapon |
| Wiltse, Ryan | EVA_OTT | Changeup | 61.5 | 59.6 | 1.9 | 60.5 | 51 | 99 | Balanced Weapon |
| Widener, Jacob | SUS_COU1 | Slider | 61.0 | 59.3 | 1.7 | 60.2 | 37 | 54 | Balanced Weapon |
| Foster, Kobe | WAS_WIL3 | Four-Seam | 59.2 | 60.5 | -1.2 | 59.8 | 261 | 180 | Balanced Weapon |
| Majick, Eli | NEW_ENG23 | Cutter | 59.7 | 59.6 | 0.1 | 59.7 | 42 | 26 | Balanced Weapon |
| Correa, Nelvin | QUE_CAP | Four-Seam | 61.1 | 58.3 | 2.7 | 59.7 | 45 | 41 | Balanced Weapon |
| Foy, Corbin | LAK_ERI24 | Four-Seam | 60.3 | 59.0 | 1.3 | 59.6 | 47 | 48 | Balanced Weapon |

## Pitch Type Typical Gaps

| Pitch Type | Median Gap | Rows |
|---|---:|---:|
| Slider | 5.1 | 138 |
| Curveball | 1.8 | 72 |
| Four-Seam | 1.4 | 236 |
| Cutter | 0.6 | 30 |
| Sinker | 0.3 | 119 |
| Changeup | -0.4 | 68 |
| Splitter | -0.7 | 11 |