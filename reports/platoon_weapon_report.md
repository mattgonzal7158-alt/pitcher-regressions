# Platoon Weapon Report

- Input file: `data\processed\pitch_leaderboard_splits.csv`
- Output file: `data\processed\platoon_weapon_scores.csv`
- Input split rows: 988
- Pitcher + pitch type rows with both RHH and LHH scores: 420
- Platoon gap: `score_vs_rhh - score_vs_lhh`
- Positive gap means the pitch grades better versus RHH. Negative gap means it grades better versus LHH.
- Reverse Split Weapon is defined from this file only: the pitch's gap is at least 5 points and opposite the typical median gap for that pitch type.

## Category Counts

| Category | Count |
|---|---:|
| Balanced Weapon | 324 |
| Right-Handed Killer | 62 |
| Left-Handed Killer | 30 |
| Reverse Split Weapon | 4 |

## Top 20 Right-Handed Killing Pitches

| Pitcher | Team | Pitch Type | RHH | LHH | Gap | Avg | R Pitches | L Pitches | Category |
|---|---|---|---|---|---|---|---|---|---|
| Gamelin, Shaun | JOL_SLA | Slider | 59.4 | 45.8 | 13.6 | 52.6 | 31 | 30 | Right-Handed Killer |
| Hagan, Jack | DOW_EAS1 | Slider | 62.2 | 48.8 | 13.3 | 55.5 | 73 | 43 | Right-Handed Killer |
| MacMillan, Blake | TRO_AIG | Four-Seam | 61.2 | 50.0 | 11.2 | 55.6 | 54 | 38 | Right-Handed Killer |
| Perdomo, Rafael | QUE_CAP | Slider | 56.4 | 45.4 | 11.0 | 50.9 | 46 | 38 | Right-Handed Killer |
| Leak, Anthony | NEW_YOR13 | Slider | 61.7 | 50.7 | 11.0 | 56.2 | 94 | 48 | Right-Handed Killer |
| Smith, Ethan | WIN_CIT29 | Slider | 57.9 | 47.5 | 10.5 | 52.7 | 30 | 28 | Right-Handed Killer |
| Perozzi, John | SUS_COU1 | Slider | 64.3 | 54.0 | 10.3 | 59.2 | 46 | 37 | Right-Handed Killer |
| Cohn, Cooper | NIU_HUS | Slider | 63.2 | 53.1 | 10.1 | 58.2 | 27 | 36 | Right-Handed Killer |
| Bice, Emmett | NEW_YOR13 | Slider | 59.4 | 49.3 | 10.1 | 54.4 | 83 | 104 | Right-Handed Killer |
| Perozzi, John | SUS_COU1 | Four-Seam | 55.1 | 45.2 | 9.9 | 50.1 | 51 | 79 | Right-Handed Killer |
| Ginn, Landon | WAS_WIL3 | Four-Seam | 58.8 | 49.1 | 9.7 | 53.9 | 44 | 52 | Right-Handed Killer |
| Blair, Davis | DOW_EAS1 | Slider | 59.7 | 50.1 | 9.6 | 54.9 | 61 | 38 | Right-Handed Killer |
| Vailes, Gage | GAT_GRI | Slider | 63.4 | 53.8 | 9.5 | 58.6 | 125 | 52 | Right-Handed Killer |
| Nova, Fraynel | LAK_ERI24 | Slider | 64.7 | 55.2 | 9.5 | 60.0 | 100 | 98 | Right-Handed Killer |
| Heredia-Bustos, Rolando | DOW_EAS1 | Slider | 61.9 | 52.5 | 9.4 | 57.2 | 181 | 119 | Right-Handed Killer |
| Binns, Malik | NEW_JER6 | Four-Seam | 58.2 | 49.9 | 8.3 | 54.0 | 25 | 28 | Right-Handed Killer |
| Almonte, Lisandro | NEW_JER6 | Four-Seam | 55.1 | 47.0 | 8.1 | 51.0 | 37 | 54 | Right-Handed Killer |
| Albert, Wes | TRI_VAL | Four-Seam | 57.0 | 49.1 | 7.9 | 53.0 | 52 | 71 | Right-Handed Killer |
| Long, Maddox | WAS_WIL3 | Slider | 65.6 | 57.7 | 7.9 | 61.6 | 111 | 33 | Right-Handed Killer |
| Cerda, Junior | EVA_OTT | Four-Seam | 56.2 | 48.5 | 7.7 | 52.3 | 41 | 54 | Right-Handed Killer |

## Top 20 Left-Handed Killing Pitches

| Pitcher | Team | Pitch Type | RHH | LHH | Gap | Avg | R Pitches | L Pitches | Category |
|---|---|---|---|---|---|---|---|---|---|
| Hampton, Ky | OTT_TIT | Changeup | 42.6 | 55.1 | -12.5 | 48.9 | 31 | 74 | Left-Handed Killer |
| Lawson, Nathan | FLO_Y'A | Sinker | 53.7 | 63.2 | -9.5 | 58.5 | 27 | 28 | Left-Handed Killer |
| Davis, Tyler | WAS_WIL3 | Four-Seam | 46.6 | 55.4 | -8.8 | 51.0 | 71 | 48 | Left-Handed Killer |
| Fowler, Dalton | SUS_COU1 | Four-Seam | 48.7 | 57.1 | -8.4 | 52.9 | 46 | 43 | Left-Handed Killer |
| Dill, Austin | TRI_VAL | Changeup | 51.8 | 60.1 | -8.3 | 56.0 | 77 | 107 | Left-Handed Killer |
| Odonnell, Brendan | NEW_ENG23 | Slider | 49.5 | 56.5 | -7.0 | 53.0 | 51 | 47 | Reverse Split Weapon |
| Zentko, Dylan | EVA_OTT | Four-Seam | 55.1 | 61.8 | -6.7 | 58.4 | 28 | 41 | Left-Handed Killer |
| Cooper, Garrett | NEW_YOR13 | Changeup | 54.5 | 61.1 | -6.6 | 57.8 | 36 | 73 | Left-Handed Killer |
| Alpern, Liam | FLO_Y'A | Four-Seam | 50.6 | 57.1 | -6.5 | 53.9 | 178 | 86 | Left-Handed Killer |
| Cartwright, Eli | GAT_GRI | Four-Seam | 57.9 | 64.1 | -6.2 | 61.0 | 79 | 42 | Left-Handed Killer |
| Willeman, Landon | EVA_OTT | Changeup | 60.2 | 66.2 | -6.0 | 63.2 | 32 | 80 | Left-Handed Killer |
| Cook, Cole | SCH_BOO | Slider | 54.0 | 59.7 | -5.7 | 56.8 | 39 | 87 | Reverse Split Weapon |
| Glickstein, Aaron | SCH_BOO | Four-Seam | 50.8 | 56.2 | -5.4 | 53.5 | 41 | 59 | Left-Handed Killer |
| Armstrong, Andrew | NEW_YOR13 | Slider | 54.8 | 59.9 | -5.1 | 57.3 | 28 | 40 | Reverse Split Weapon |
| McEvoy, Aidan | FLO_Y'A | Slider | 63.1 | 68.2 | -5.1 | 65.6 | 27 | 51 | Reverse Split Weapon |

## Top 20 Balanced Pitches

| Pitcher | Team | Pitch Type | RHH | LHH | Gap | Avg | R Pitches | L Pitches | Category |
|---|---|---|---|---|---|---|---|---|---|
| Grounds, Jackson | DOW_EAS1 | Curveball | 71.6 | 68.7 | 2.9 | 70.2 | 43 | 39 | Balanced Weapon |
| Grounds, Jackson | DOW_EAS1 | Four-Seam | 70.8 | 69.0 | 1.9 | 69.9 | 48 | 59 | Balanced Weapon |
| Ryan, Dillon | NEW_ENG23 | Slider | 69.4 | 67.6 | 1.8 | 68.5 | 39 | 54 | Balanced Weapon |
| Jones, Logan | TRI_VAL | Slider | 65.5 | 67.2 | -1.7 | 66.3 | 32 | 33 | Balanced Weapon |
| Webster, Evan | FLO_Y'A | Cutter | 64.2 | 66.7 | -2.5 | 65.5 | 29 | 70 | Balanced Weapon |
| Rodriguez, Joe Joe | NEW_JER6 | Four-Seam | 61.8 | 63.7 | -1.9 | 62.8 | 28 | 27 | Balanced Weapon |
| Harris, Ben | GAT_GRI | Curveball | 64.1 | 61.2 | 2.9 | 62.6 | 86 | 52 | Balanced Weapon |
| Mannering, Shawn | DOW_EAS1 | Sinker | 62.3 | 61.3 | 1.0 | 61.8 | 32 | 27 | Balanced Weapon |
| Zaffiro, Cole | SCH_BOO | Four-Seam | 61.0 | 61.3 | -0.3 | 61.1 | 64 | 44 | Balanced Weapon |
| Wiltse, Ryan | EVA_OTT | Changeup | 61.6 | 60.1 | 1.5 | 60.8 | 29 | 78 | Balanced Weapon |
| Colon, Jeffrey | TRO_AIG | Sinker | 60.7 | 60.1 | 0.6 | 60.4 | 26 | 30 | Balanced Weapon |
| Kines, Gunnar | JOL_SLA | Four-Seam | 59.8 | 59.6 | 0.2 | 59.7 | 131 | 121 | Balanced Weapon |
| Plumadore, Carson | WIN_CIT29 | Sinker | 60.7 | 58.6 | 2.1 | 59.7 | 32 | 47 | Balanced Weapon |
| Langhorne, Miles | SUS_COU1 | Four-Seam | 59.4 | 59.4 | 0.0 | 59.4 | 40 | 30 | Balanced Weapon |
| Widener, Jacob | SUS_COU1 | Four-Seam | 58.4 | 59.8 | -1.5 | 59.1 | 34 | 26 | Balanced Weapon |
| Villers, Ian | QUE_CAP | Splitter | 58.9 | 58.2 | 0.7 | 58.6 | 25 | 39 | Balanced Weapon |
| Boies, Emiles | QUE_CAP | Changeup | 59.9 | 57.2 | 2.6 | 58.6 | 34 | 88 | Balanced Weapon |
| Pindel, Buddie | SCH_BOO | Splitter | 58.6 | 58.5 | 0.1 | 58.6 | 30 | 50 | Balanced Weapon |
| Eisenbarger, Jack | QUE_CAP | Four-Seam | 57.2 | 59.3 | -2.1 | 58.2 | 34 | 50 | Balanced Weapon |
| Quigley, Michael | NEW_ENG23 | Four-Seam | 59.0 | 57.4 | 1.7 | 58.2 | 61 | 84 | Balanced Weapon |

## Pitch Type Typical Gaps

| Pitch Type | Median Gap | Rows |
|---|---:|---:|
| Slider | 3.5 | 74 |
| Curveball | 1.2 | 31 |
| Four-Seam | 0.9 | 179 |
| Splitter | 0.4 | 2 |
| Cutter | 0.3 | 15 |
| Sinker | -0.5 | 80 |
| Changeup | -0.5 | 39 |