# Platoon Weapon Report

- Input file: `data\processed\pitch_leaderboard_splits.csv`
- Output file: `data\processed\platoon_weapon_scores.csv`
- Input split rows: 1,581
- Pitcher + pitch type rows with both RHH and LHH scores: 692
- Platoon gap: `score_vs_rhh - score_vs_lhh`
- Positive gap means the pitch grades better versus RHH. Negative gap means it grades better versus LHH.
- Reverse Split Weapon is defined from this file only: the pitch's gap is at least 5 points and opposite the typical median gap for that pitch type.

## Category Counts

| Category | Count |
|---|---:|
| Balanced Weapon | 544 |
| Right-Handed Killer | 112 |
| Left-Handed Killer | 29 |
| Reverse Split Weapon | 7 |

## Top 20 Right-Handed Killing Pitches

| Pitcher | Team | Pitch Type | RHH | LHH | Gap | Avg | R Pitches | L Pitches | Category |
|---|---|---|---|---|---|---|---|---|---|
| Thompson, Ross | SCH_BOO | Slider | 60.8 | 44.0 | 16.8 | 52.4 | 196 | 27 | Right-Handed Killer |
| Vailes, Gage | GAT_GRI | Slider | 63.8 | 49.6 | 14.1 | 56.7 | 220 | 95 | Right-Handed Killer |
| Nova, Fraynel | LAK_ERI24 | Slider | 61.9 | 49.3 | 12.6 | 55.6 | 153 | 174 | Right-Handed Killer |
| Hagan, Jack | DOW_EAS1 | Slider | 61.7 | 49.6 | 12.1 | 55.6 | 135 | 87 | Right-Handed Killer |
| Helt, Robert | LAK_ERI24 | Slider | 62.6 | 50.8 | 11.7 | 56.7 | 147 | 86 | Right-Handed Killer |
| Perdomo, Rafael | QUE_CAP | Slider | 57.2 | 45.7 | 11.5 | 51.4 | 48 | 39 | Right-Handed Killer |
| Leak, Anthony | NEW_YOR13 | Slider | 64.2 | 52.8 | 11.4 | 58.5 | 177 | 97 | Right-Handed Killer |
| Cohn, Cooper | NIU_HUS | Slider | 62.5 | 51.1 | 11.3 | 56.8 | 27 | 36 | Right-Handed Killer |
| Heredia-Bustos, Rolando | DOW_EAS1 | Slider | 60.2 | 49.0 | 11.2 | 54.6 | 267 | 182 | Right-Handed Killer |
| Woolfolk, Dallas | MIS_MUD | Slider | 56.2 | 45.1 | 11.1 | 50.6 | 51 | 29 | Right-Handed Killer |
| Bargo, Casey | NEW_ENG23 | Slider | 73.9 | 62.9 | 11.0 | 68.4 | 29 | 27 | Right-Handed Killer |
| Gamelin, Shaun | JOL_SLA | Slider | 58.9 | 47.9 | 11.0 | 53.4 | 46 | 32 | Right-Handed Killer |
| Smith, Ethan | WIN_CIT29 | Slider | 57.4 | 46.6 | 10.9 | 52.0 | 30 | 28 | Right-Handed Killer |
| Blair, Davis | DOW_EAS1 | Slider | 59.7 | 48.9 | 10.8 | 54.3 | 61 | 38 | Right-Handed Killer |
| Turner, Eric | JOL_SLA | Slider | 55.7 | 45.1 | 10.6 | 50.4 | 135 | 86 | Right-Handed Killer |
| Cerda, Junior | EVA_OTT | Slider | 59.5 | 49.0 | 10.5 | 54.2 | 79 | 43 | Right-Handed Killer |
| Ginn, Landon | WAS_WIL3 | Four-Seam | 59.5 | 49.1 | 10.4 | 54.3 | 68 | 77 | Right-Handed Killer |
| Pardinho, Eric | OTT_TIT | Slider | 55.3 | 45.1 | 10.2 | 50.2 | 137 | 34 | Right-Handed Killer |
| Duncan, Tanner | DOW_EAS1 | Slider | 69.2 | 59.3 | 9.9 | 64.3 | 38 | 26 | Right-Handed Killer |
| Leach, Landon | TRO_AIG | Slider | 56.6 | 46.8 | 9.8 | 51.7 | 34 | 31 | Right-Handed Killer |

## Top 20 Left-Handed Killing Pitches

| Pitcher | Team | Pitch Type | RHH | LHH | Gap | Avg | R Pitches | L Pitches | Category |
|---|---|---|---|---|---|---|---|---|---|
| Fowler, Dalton | SUS_COU1 | Four-Seam | 46.1 | 56.1 | -10.0 | 51.1 | 46 | 43 | Left-Handed Killer |
| McEvoy, Aidan | FLO_Y'A | Slider | 61.5 | 69.4 | -7.8 | 65.4 | 40 | 76 | Reverse Split Weapon |
| Dill, Austin | TRI_VAL | Changeup | 52.2 | 59.9 | -7.7 | 56.0 | 86 | 118 | Left-Handed Killer |
| Morgan, Cooper | QUE_CAP | Four-Seam | 54.4 | 61.6 | -7.3 | 58.0 | 36 | 43 | Left-Handed Killer |
| Cook, Cole | SCH_BOO | Slider | 49.5 | 56.4 | -6.9 | 53.0 | 84 | 129 | Reverse Split Weapon |
| Alpern, Liam | FLO_Y'A | Four-Seam | 50.4 | 57.1 | -6.7 | 53.7 | 178 | 86 | Left-Handed Killer |
| Alpern, Liam | FLO_Y'A | Slider | 64.7 | 71.3 | -6.5 | 68.0 | 40 | 38 | Reverse Split Weapon |
| Odonnell, Brendan | NEW_ENG23 | Slider | 51.2 | 57.6 | -6.4 | 54.4 | 144 | 91 | Reverse Split Weapon |
| Sechrist, Zander | WAS_WIL3 | Slider | 53.6 | 59.8 | -6.2 | 56.7 | 33 | 48 | Reverse Split Weapon |
| Maietta, Dante | WIN_CIT29 | Changeup | 56.5 | 62.6 | -6.1 | 59.6 | 125 | 158 | Left-Handed Killer |
| Hensey, Rob | SUS_COU1 | Slider | 53.0 | 58.3 | -5.3 | 55.6 | 27 | 81 | Reverse Split Weapon |
| Dima, Josh | GAT_GRI | Slider | 53.2 | 58.4 | -5.2 | 55.8 | 44 | 75 | Reverse Split Weapon |

## Top 20 Balanced Pitches

| Pitcher | Team | Pitch Type | RHH | LHH | Gap | Avg | R Pitches | L Pitches | Category |
|---|---|---|---|---|---|---|---|---|---|
| Jones, Logan | TRI_VAL | Slider | 65.7 | 67.7 | -2.0 | 66.7 | 32 | 33 | Balanced Weapon |
| Leduc, Zachary | TRO_AIG | Slider | 66.1 | 64.0 | 2.1 | 65.0 | 49 | 38 | Balanced Weapon |
| Rodriguez, Joe Joe | NEW_JER6 | Changeup | 63.1 | 64.4 | -1.4 | 63.7 | 33 | 111 | Balanced Weapon |
| Bohnert, Matthew | WIN_CIT29 | Curveball | 62.6 | 64.1 | -1.6 | 63.4 | 52 | 46 | Balanced Weapon |
| Riedel, Caleb | SCH_BOO | Sinker | 62.9 | 63.1 | -0.2 | 63.0 | 48 | 33 | Balanced Weapon |
| Harris, Everette | TRI_VAL | Changeup | 62.1 | 63.7 | -1.5 | 62.9 | 40 | 56 | Balanced Weapon |
| Wehrle, Tyler | WIN_CIT29 | Four-Seam | 61.7 | 63.5 | -1.9 | 62.6 | 156 | 80 | Balanced Weapon |
| Wiltse, Ryan | EVA_OTT | Changeup | 62.9 | 61.5 | 1.5 | 62.2 | 55 | 110 | Balanced Weapon |
| MacMillan, Blake | TRO_AIG | Slider | 61.7 | 62.3 | -0.6 | 62.0 | 43 | 63 | Balanced Weapon |
| Webster, Evan | FLO_Y'A | Cutter | 60.7 | 62.4 | -1.8 | 61.6 | 39 | 99 | Balanced Weapon |
| Binns, Malik | NEW_JER6 | Curveball | 62.6 | 60.3 | 2.3 | 61.4 | 28 | 27 | Balanced Weapon |
| Mannering, Shawn | DOW_EAS1 | Sinker | 60.9 | 61.2 | -0.3 | 61.1 | 32 | 27 | Balanced Weapon |
| Colon, Jeffrey | TRO_AIG | Sinker | 62.2 | 59.8 | 2.4 | 61.0 | 26 | 30 | Balanced Weapon |
| Correa, Nelvin | QUE_CAP | Cutter | 61.6 | 60.0 | 1.6 | 60.8 | 55 | 63 | Balanced Weapon |
| Salata, Derek | SCH_BOO | Curveball | 61.7 | 59.8 | 2.0 | 60.8 | 72 | 50 | Balanced Weapon |
| Grounds, Jackson | TRO_AIG | Four-Seam | 62.1 | 59.4 | 2.7 | 60.8 | 45 | 34 | Balanced Weapon |
| Majick, Eli | NEW_ENG23 | Cutter | 61.0 | 60.4 | 0.6 | 60.7 | 60 | 28 | Balanced Weapon |
| Shears, Tanner | SCH_BOO | Four-Seam | 61.0 | 59.9 | 1.0 | 60.4 | 143 | 97 | Balanced Weapon |
| Coles, Chad | WAS_WIL3 | Splitter | 59.6 | 61.3 | -1.6 | 60.4 | 25 | 38 | Balanced Weapon |
| Foy, Corbin | LAK_ERI24 | Four-Seam | 61.1 | 58.7 | 2.4 | 59.9 | 47 | 48 | Balanced Weapon |

## Pitch Type Typical Gaps

| Pitch Type | Median Gap | Rows |
|---|---:|---:|
| Slider | 5.3 | 139 |
| Curveball | 1.5 | 78 |
| Four-Seam | 1.3 | 240 |
| Cutter | 0.6 | 32 |
| Sinker | 0.4 | 124 |
| Changeup | -0.8 | 68 |
| Splitter | -0.9 | 11 |