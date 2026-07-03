# Platoon Weapon Report

- Input file: `data\processed\pitch_leaderboard_splits.csv`
- Output file: `data\processed\platoon_weapon_scores.csv`
- Input split rows: 1,323
- Pitcher + pitch type rows with both RHH and LHH scores: 579
- Platoon gap: `score_vs_rhh - score_vs_lhh`
- Positive gap means the pitch grades better versus RHH. Negative gap means it grades better versus LHH.
- Reverse Split Weapon is defined from this file only: the pitch's gap is at least 5 points and opposite the typical median gap for that pitch type.

## Category Counts

| Category | Count |
|---|---:|
| Balanced Weapon | 460 |
| Right-Handed Killer | 83 |
| Left-Handed Killer | 29 |
| Reverse Split Weapon | 7 |

## Top 20 Right-Handed Killing Pitches

| Pitcher | Team | Pitch Type | RHH | LHH | Gap | Avg | R Pitches | L Pitches | Category |
|---|---|---|---|---|---|---|---|---|---|
| Thompson, Ross | SCH_BOO | Slider | 61.5 | 44.6 | 16.9 | 53.1 | 181 | 26 | Right-Handed Killer |
| Vailes, Gage | GAT_GRI | Slider | 64.8 | 50.5 | 14.4 | 57.6 | 177 | 71 | Right-Handed Killer |
| Hagan, Jack | DOW_EAS1 | Slider | 66.1 | 52.5 | 13.6 | 59.3 | 118 | 66 | Right-Handed Killer |
| Gamelin, Shaun | JOL_SLA | Slider | 59.9 | 46.6 | 13.3 | 53.2 | 34 | 30 | Right-Handed Killer |
| Pardinho, Eric | OTT_TIT | Slider | 58.8 | 46.0 | 12.8 | 52.4 | 96 | 27 | Right-Handed Killer |
| Leak, Anthony | NEW_YOR13 | Slider | 64.9 | 52.2 | 12.7 | 58.6 | 131 | 65 | Right-Handed Killer |
| Helt, Robert | LAK_ERI24 | Slider | 63.6 | 51.0 | 12.6 | 57.3 | 137 | 76 | Right-Handed Killer |
| Nova, Fraynel | LAK_ERI24 | Slider | 62.3 | 50.8 | 11.5 | 56.5 | 126 | 141 | Right-Handed Killer |
| Heredia-Bustos, Rolando | DOW_EAS1 | Slider | 61.4 | 50.1 | 11.3 | 55.8 | 227 | 142 | Right-Handed Killer |
| Perdomo, Rafael | QUE_CAP | Slider | 56.8 | 45.6 | 11.3 | 51.2 | 46 | 38 | Right-Handed Killer |
| Vega, Lucas | TRO_AIG | Slider | 66.4 | 55.6 | 10.8 | 61.0 | 84 | 33 | Right-Handed Killer |
| Blair, Davis | DOW_EAS1 | Slider | 59.6 | 49.0 | 10.6 | 54.3 | 61 | 38 | Right-Handed Killer |
| Smith, Ethan | WIN_CIT29 | Slider | 57.4 | 46.8 | 10.6 | 52.1 | 30 | 28 | Right-Handed Killer |
| Bice, Emmett | NEW_YOR13 | Slider | 61.9 | 52.1 | 9.8 | 57.0 | 127 | 133 | Right-Handed Killer |
| Cerda, Junior | EVA_OTT | Four-Seam | 55.8 | 46.1 | 9.7 | 51.0 | 50 | 54 | Right-Handed Killer |
| Willeman, Landon | EVA_OTT | Slider | 56.3 | 46.7 | 9.6 | 51.5 | 59 | 26 | Right-Handed Killer |
| Ginn, Landon | WAS_WIL3 | Four-Seam | 58.8 | 49.5 | 9.4 | 54.2 | 59 | 64 | Right-Handed Killer |
| Campbell, AJ | WIN_CIT29 | Slider | 55.9 | 46.8 | 9.2 | 51.4 | 180 | 101 | Right-Handed Killer |
| Bargo, Casey | NEW_ENG23 | Slider | 73.0 | 63.9 | 9.1 | 68.5 | 29 | 27 | Right-Handed Killer |
| Cohn, Cooper | NIU_HUS | Slider | 61.6 | 52.6 | 8.9 | 57.1 | 27 | 36 | Right-Handed Killer |

## Top 20 Left-Handed Killing Pitches

| Pitcher | Team | Pitch Type | RHH | LHH | Gap | Avg | R Pitches | L Pitches | Category |
|---|---|---|---|---|---|---|---|---|---|
| Smith, Jackson | MIS_MUD | Changeup | 50.5 | 61.4 | -10.9 | 55.9 | 25 | 51 | Left-Handed Killer |
| Dill, Austin | TRI_VAL | Changeup | 51.9 | 59.5 | -7.6 | 55.7 | 77 | 107 | Left-Handed Killer |
| Fowler, Dalton | SUS_COU1 | Four-Seam | 48.4 | 55.9 | -7.5 | 52.1 | 46 | 43 | Left-Handed Killer |
| McEvoy, Aidan | FLO_Y'A | Slider | 61.6 | 68.9 | -7.4 | 65.3 | 35 | 65 | Reverse Split Weapon |
| Armstrong, Andrew | NEW_YOR13 | Slider | 52.3 | 59.5 | -7.2 | 55.9 | 45 | 60 | Reverse Split Weapon |
| Cook, Cole | SCH_BOO | Slider | 50.6 | 57.6 | -7.0 | 54.1 | 53 | 102 | Reverse Split Weapon |
| Alpern, Liam | FLO_Y'A | Slider | 64.8 | 71.4 | -6.6 | 68.1 | 40 | 38 | Reverse Split Weapon |
| Hensey, Rob | SUS_COU1 | Slider | 49.0 | 55.2 | -6.2 | 52.1 | 25 | 67 | Reverse Split Weapon |
| Alpern, Liam | FLO_Y'A | Four-Seam | 49.9 | 56.1 | -6.2 | 53.0 | 178 | 86 | Left-Handed Killer |
| Dima, Josh | GAT_GRI | Slider | 52.4 | 58.1 | -5.8 | 55.2 | 43 | 71 | Reverse Split Weapon |
| Eckaus, David | EVA_OTT | Slider | 52.0 | 57.5 | -5.5 | 54.7 | 44 | 107 | Reverse Split Weapon |
| Daly, Ryan | JOL_SLA | Changeup | 49.7 | 55.1 | -5.4 | 52.4 | 57 | 123 | Left-Handed Killer |
| Burcham, Jacob | GAT_GRI | Changeup | 50.1 | 55.2 | -5.1 | 52.7 | 30 | 49 | Left-Handed Killer |
| Hensey, Rob | SUS_COU1 | Changeup | 54.8 | 59.9 | -5.0 | 57.3 | 188 | 38 | Left-Handed Killer |

## Top 20 Balanced Pitches

| Pitcher | Team | Pitch Type | RHH | LHH | Gap | Avg | R Pitches | L Pitches | Category |
|---|---|---|---|---|---|---|---|---|---|
| Grounds, Jackson | DOW_EAS1 | Curveball | 72.5 | 69.5 | 3.0 | 71.0 | 43 | 39 | Balanced Weapon |
| Jones, Logan | TRI_VAL | Slider | 65.1 | 67.5 | -2.4 | 66.3 | 32 | 33 | Balanced Weapon |
| Webster, Evan | FLO_Y'A | Cutter | 62.2 | 64.8 | -2.6 | 63.5 | 32 | 76 | Balanced Weapon |
| Correa, Nelvin | QUE_CAP | Cutter | 64.4 | 62.1 | 2.2 | 63.2 | 41 | 47 | Balanced Weapon |
| Harris, Everette | TRI_VAL | Changeup | 62.5 | 63.8 | -1.2 | 63.2 | 40 | 56 | Balanced Weapon |
| Rodriguez, Joe Joe | NEW_JER6 | Four-Seam | 63.7 | 61.8 | 2.0 | 62.7 | 36 | 31 | Balanced Weapon |
| Foster, Kobe | WAS_WIL3 | Four-Seam | 61.9 | 63.1 | -1.2 | 62.5 | 220 | 133 | Balanced Weapon |
| Lovell, Justin | WIN_CIT29 | Sinker | 61.3 | 63.2 | -1.9 | 62.3 | 30 | 59 | Balanced Weapon |
| Wehrle, Tyler | WIN_CIT29 | Four-Seam | 60.9 | 62.7 | -1.8 | 61.8 | 156 | 80 | Balanced Weapon |
| Mannering, Shawn | DOW_EAS1 | Sinker | 61.0 | 61.6 | -0.5 | 61.3 | 32 | 27 | Balanced Weapon |
| Colon, Jeffrey | TRO_AIG | Sinker | 61.9 | 60.6 | 1.3 | 61.2 | 26 | 30 | Balanced Weapon |
| Garcia, Brett | OTT_TIT | Curveball | 61.6 | 59.6 | 2.0 | 60.6 | 60 | 44 | Balanced Weapon |
| Cooper, Garrett | NEW_YOR13 | Changeup | 59.1 | 61.9 | -2.8 | 60.5 | 84 | 114 | Balanced Weapon |
| Shears, Tanner | SCH_BOO | Four-Seam | 61.4 | 59.0 | 2.4 | 60.2 | 118 | 87 | Balanced Weapon |
| MacMillan, Blake | TRO_AIG | Slider | 59.3 | 61.0 | -1.6 | 60.2 | 39 | 57 | Balanced Weapon |
| Harris, Ben | GAT_GRI | Curveball | 61.5 | 58.7 | 2.8 | 60.1 | 133 | 72 | Balanced Weapon |
| Shears, Tanner | SCH_BOO | Splitter | 60.1 | 59.9 | 0.2 | 60.0 | 30 | 35 | Balanced Weapon |
| Vitas, Ben | JOL_SLA | Splitter | 59.5 | 60.2 | -0.6 | 59.9 | 30 | 68 | Balanced Weapon |
| Eisenbarger, Jack | QUE_CAP | Curveball | 59.0 | 60.5 | -1.5 | 59.8 | 25 | 46 | Balanced Weapon |
| Wiltse, Ryan | EVA_OTT | Changeup | 60.4 | 58.5 | 1.9 | 59.4 | 32 | 88 | Balanced Weapon |

## Pitch Type Typical Gaps

| Pitch Type | Median Gap | Rows |
|---|---:|---:|
| Slider | 4.4 | 113 |
| Four-Seam | 1.5 | 215 |
| Curveball | 1.2 | 55 |
| Cutter | 0.7 | 24 |
| Sinker | 0.4 | 105 |
| Changeup | 0.2 | 58 |
| Splitter | -0.6 | 9 |