# Platoon Weapon Report

- Input file: `data\processed\pitch_leaderboard_splits.csv`
- Output file: `data\processed\platoon_weapon_scores.csv`
- Input split rows: 1,783
- Pitcher + pitch type rows with both RHH and LHH scores: 781
- Platoon gap: `score_vs_rhh - score_vs_lhh`
- Positive gap means the pitch grades better versus RHH. Negative gap means it grades better versus LHH.
- Reverse Split Weapon is defined from this file only: the pitch's gap is at least 5 points and opposite the typical median gap for that pitch type.

## Category Counts

| Category | Count |
|---|---:|
| Balanced Weapon | 614 |
| Right-Handed Killer | 124 |
| Left-Handed Killer | 34 |
| Reverse Split Weapon | 9 |

## Top 20 Right-Handed Killing Pitches

| Pitcher | Team | Pitch Type | RHH | LHH | Gap | Avg | R Pitches | L Pitches | Category |
|---|---|---|---|---|---|---|---|---|---|
| Thompson, Ross | SCH_BOO | Slider | 61.1 | 45.1 | 16.0 | 53.1 | 243 | 40 | Right-Handed Killer |
| Hagan, Jack | DOW_EAS1 | Slider | 64.3 | 50.5 | 13.8 | 57.4 | 191 | 106 | Right-Handed Killer |
| Perdomo, Rafael | QUE_CAP | Slider | 58.7 | 45.5 | 13.1 | 52.1 | 73 | 43 | Right-Handed Killer |
| Bargo, Casey | NEW_ENG23 | Slider | 75.2 | 62.3 | 12.8 | 68.7 | 29 | 27 | Right-Handed Killer |
| Nova, Fraynel | LAK_ERI24 | Slider | 60.4 | 48.0 | 12.4 | 54.2 | 174 | 200 | Right-Handed Killer |
| Cerda, Junior | EVA_OTT | Slider | 61.4 | 49.1 | 12.3 | 55.2 | 116 | 55 | Right-Handed Killer |
| Leak, Anthony | NEW_YOR13 | Slider | 63.7 | 52.2 | 11.5 | 57.9 | 220 | 105 | Right-Handed Killer |
| Helt, Robert | LAK_ERI24 | Slider | 62.5 | 51.2 | 11.3 | 56.9 | 147 | 86 | Right-Handed Killer |
| Vilchez, Michael | OTT_TIT | Slider | 56.0 | 44.8 | 11.2 | 50.4 | 94 | 26 | Right-Handed Killer |
| Leach, Landon | TRO_AIG | Slider | 57.1 | 46.2 | 10.9 | 51.7 | 36 | 36 | Right-Handed Killer |
| Blair, Davis | DOW_EAS1 | Slider | 58.8 | 48.1 | 10.7 | 53.4 | 61 | 38 | Right-Handed Killer |
| Cohn, Cooper | NIU_HUS | Slider | 62.6 | 51.9 | 10.7 | 57.2 | 27 | 36 | Right-Handed Killer |
| Woolfolk, Dallas | MIS_MUD | Slider | 56.5 | 45.8 | 10.6 | 51.2 | 72 | 37 | Right-Handed Killer |
| Smith, Ethan | WIN_CIT29 | Slider | 57.4 | 46.8 | 10.6 | 52.1 | 30 | 28 | Right-Handed Killer |
| Scafidi, Christian | LAK_ERI24 | Slider | 58.0 | 47.4 | 10.5 | 52.7 | 128 | 78 | Right-Handed Killer |
| Perez, Kelvin | WAS_WIL3 | Slider | 59.9 | 49.4 | 10.5 | 54.6 | 168 | 42 | Right-Handed Killer |
| Valdez, Alex | EVA_OTT | Slider | 60.1 | 49.6 | 10.5 | 54.8 | 99 | 91 | Right-Handed Killer |
| Heredia-Bustos, Rolando | DOW_EAS1 | Slider | 60.1 | 49.6 | 10.5 | 54.8 | 267 | 182 | Right-Handed Killer |
| Gilleran, Jimmy | NEW_ENG23 | Slider | 58.9 | 48.5 | 10.5 | 53.7 | 109 | 50 | Right-Handed Killer |
| Vailes, Gage | GAT_GRI | Slider | 62.1 | 51.7 | 10.4 | 56.9 | 254 | 112 | Right-Handed Killer |

## Top 20 Left-Handed Killing Pitches

| Pitcher | Team | Pitch Type | RHH | LHH | Gap | Avg | R Pitches | L Pitches | Category |
|---|---|---|---|---|---|---|---|---|---|
| Fowler, Dalton | SUS_COU1 | Four-Seam | 45.8 | 56.4 | -10.6 | 51.1 | 46 | 43 | Left-Handed Killer |
| Misla, Luis | TRI_VAL | Slider | 46.7 | 55.1 | -8.4 | 50.9 | 34 | 62 | Reverse Split Weapon |
| Harris, Everette | TRI_VAL | Slider | 51.3 | 59.3 | -8.0 | 55.3 | 26 | 33 | Reverse Split Weapon |
| Dill, Austin | TRI_VAL | Changeup | 52.6 | 60.5 | -7.9 | 56.6 | 86 | 118 | Left-Handed Killer |
| McEvoy, Aidan | FLO_Y'A | Slider | 61.4 | 69.0 | -7.6 | 65.2 | 44 | 88 | Reverse Split Weapon |
| Eckaus, David | EVA_OTT | Slider | 53.7 | 61.3 | -7.6 | 57.5 | 78 | 138 | Reverse Split Weapon |
| Cook, Cole | SCH_BOO | Slider | 53.4 | 61.0 | -7.6 | 57.2 | 122 | 156 | Reverse Split Weapon |
| Foster, Kobe | WAS_WIL3 | Slider | 52.5 | 59.5 | -7.0 | 56.0 | 25 | 124 | Reverse Split Weapon |
| Webster, Evan | FLO_Y'A | Slider | 52.1 | 59.0 | -7.0 | 55.6 | 38 | 81 | Reverse Split Weapon |
| Morgan, Cooper | QUE_CAP | Four-Seam | 54.4 | 61.3 | -7.0 | 57.9 | 36 | 45 | Left-Handed Killer |
| Grills, Evan | OTT_TIT | Sinker | 51.7 | 58.2 | -6.5 | 55.0 | 29 | 26 | Left-Handed Killer |
| Alpern, Liam | FLO_Y'A | Four-Seam | 50.6 | 57.0 | -6.4 | 53.8 | 178 | 86 | Left-Handed Killer |
| Dima, Josh | GAT_GRI | Slider | 52.5 | 58.0 | -5.5 | 55.2 | 49 | 94 | Reverse Split Weapon |
| Odonnell, Brendan | NEW_ENG23 | Slider | 52.2 | 57.6 | -5.4 | 54.9 | 155 | 109 | Reverse Split Weapon |
| Culley, Wesley | LAK_ERI24 | Four-Seam | 52.3 | 57.7 | -5.4 | 55.0 | 58 | 28 | Left-Handed Killer |
| Marynczak, Arlo | TRI_VAL | Changeup | 52.7 | 57.9 | -5.2 | 55.3 | 41 | 159 | Left-Handed Killer |
| Maietta, Dante | WIN_CIT29 | Changeup | 57.1 | 62.2 | -5.1 | 59.6 | 137 | 193 | Left-Handed Killer |

## Top 20 Balanced Pitches

| Pitcher | Team | Pitch Type | RHH | LHH | Gap | Avg | R Pitches | L Pitches | Category |
|---|---|---|---|---|---|---|---|---|---|
| Flontek, Zac | DOW_EAS1 | Slider | 70.4 | 70.1 | 0.2 | 70.2 | 35 | 41 | Balanced Weapon |
| Jones, Logan | TRI_VAL | Slider | 66.0 | 68.3 | -2.3 | 67.2 | 32 | 33 | Balanced Weapon |
| Scafidi, Christian | LAK_ERI24 | Cutter | 67.1 | 64.5 | 2.6 | 65.8 | 27 | 25 | Balanced Weapon |
| MacMillan, Blake | TRO_AIG | Slider | 65.1 | 66.2 | -1.1 | 65.7 | 44 | 64 | Balanced Weapon |
| Rodriguez, Joe Joe | NEW_JER6 | Changeup | 63.7 | 65.4 | -1.7 | 64.6 | 47 | 140 | Balanced Weapon |
| Kramer, Cameron | TRO_AIG | Slider | 63.3 | 63.1 | 0.2 | 63.2 | 31 | 32 | Balanced Weapon |
| Majick, Eli | NEW_ENG23 | Cutter | 64.2 | 61.9 | 2.3 | 63.0 | 83 | 34 | Balanced Weapon |
| Riedel, Caleb | SCH_BOO | Sinker | 63.3 | 62.6 | 0.7 | 62.9 | 58 | 33 | Balanced Weapon |
| Wiltse, Ryan | EVA_OTT | Changeup | 62.8 | 62.0 | 0.8 | 62.4 | 65 | 137 | Balanced Weapon |
| Binns, Malik | NEW_JER6 | Curveball | 62.4 | 61.6 | 0.8 | 62.0 | 28 | 27 | Balanced Weapon |
| Bohnert, Matthew | WIN_CIT29 | Curveball | 60.4 | 62.8 | -2.4 | 61.6 | 62 | 62 | Balanced Weapon |
| Rodriguez, Ramon | WIN_CIT29 | Curveball | 61.9 | 61.1 | 0.7 | 61.5 | 64 | 55 | Balanced Weapon |
| Harris, Everette | TRI_VAL | Changeup | 60.0 | 62.8 | -2.8 | 61.4 | 47 | 71 | Balanced Weapon |
| Webster, Evan | FLO_Y'A | Cutter | 60.8 | 61.8 | -1.0 | 61.3 | 47 | 104 | Balanced Weapon |
| Widener, Jacob | SUS_COU1 | Slider | 60.2 | 61.3 | -1.1 | 60.8 | 40 | 61 | Balanced Weapon |
| Mannering, Shawn | DOW_EAS1 | Sinker | 60.6 | 60.4 | 0.2 | 60.5 | 32 | 27 | Balanced Weapon |
| Correa, Nelvin | QUE_CAP | Cutter | 60.5 | 59.5 | 1.0 | 60.0 | 66 | 73 | Balanced Weapon |
| Foster, Kobe | WAS_WIL3 | Four-Seam | 59.3 | 60.4 | -1.2 | 59.8 | 291 | 186 | Balanced Weapon |
| Coles, Chad | WAS_WIL3 | Splitter | 58.9 | 60.4 | -1.4 | 59.6 | 25 | 38 | Balanced Weapon |
| Villers, Ian | QUE_CAP | Splitter | 59.0 | 58.1 | 0.9 | 58.5 | 25 | 39 | Balanced Weapon |

## Pitch Type Typical Gaps

| Pitch Type | Median Gap | Rows |
|---|---:|---:|
| Slider | 5.7 | 161 |
| Curveball | 1.9 | 94 |
| Four-Seam | 1.5 | 263 |
| Cutter | 1.1 | 34 |
| Sinker | 0.2 | 138 |
| Changeup | -0.9 | 79 |
| Splitter | -1.2 | 12 |