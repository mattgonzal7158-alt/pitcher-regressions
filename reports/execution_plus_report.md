# Execution+ Report

- Master input file: `data\processed\master_pitch_evaluation_table.csv`
- Stuff+ input file: `data\processed\stuff_plus_scores.csv`
- Output file: `data\processed\execution_plus_scores.csv`
- Scored rows: 1,581

## Method

`execution_raw = final_pitch_score_20_80 - stuff_plus_raw`

Execution+ captures how much a pitch's actual final score exceeds, or falls short of, its movement/release-only expected score.

Quadrant labels use `50` as the high/low cutoff on both 20-80 scales:

- High Stuff+, low Execution+: Development Target.
- Low Stuff+, high Execution+: Command/Deception Weapon.
- High Stuff+, high Execution+: Elite Weapon.
- Low Stuff+, low Execution+: Low Priority.

## Quadrant Table

| Quadrant | Rows | Avg Final | Avg Stuff+ | Avg Execution+ |
|---|---:|---:|---:|---:|
| Low Priority | 422 | 42.6 | 42.9 | 42.7 |
| Command/Deception Weapon | 406 | 53.2 | 42.9 | 57.7 |
| Development Target | 388 | 46.1 | 57.6 | 41.8 |
| Elite Weapon | 365 | 57.9 | 58.0 | 58.5 |

## Top 25 Execution+

| Rank | Pitcher | Team | Pitch Type | Side | Final | Stuff+ | Exec+ | Exec Raw | Quadrant | Archetype |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | Ryan, Dillon | NEW_ENG23 | Slider | RHH | 77.6 | 64.9 | 80.0 | 23.76 | Elite Weapon | Tight High-Spin Breakers |
| 2 | Grounds, Jackson | DOW_EAS1 | Four-Seam | RHH | 72.1 | 49.8 | 80.0 | 22.46 | Command/Deception Weapon | Soft-Speed Separation |
| 3 | Grounds, Jackson | DOW_EAS1 | Curveball | RHH | 73.3 | 56.2 | 80.0 | 21.86 | Elite Weapon | Tight High-Spin Breakers |
| 4 | Peyton, Blake | GAT_GRI | Changeup | RHH | 70.9 | 48.7 | 80.0 | 21.61 | Command/Deception Weapon | Tight High-Spin Breakers |
| 5 | Morgan, Cooper | QUE_CAP | Curveball | LHH | 69.6 | 44.4 | 80.0 | 21.48 | Command/Deception Weapon | Tight High-Spin Breakers |
| 6 | Debban, Caleb | NEW_JER6 | Four-Seam | RHH | 68.8 | 43.3 | 79.7 | 20.92 | Command/Deception Weapon | Soft-Speed Separation |
| 7 | Bargo, Casey | NEW_ENG23 | Slider | RHH | 73.9 | 62.4 | 79.5 | 20.79 | Elite Weapon | Tight High-Spin Breakers |
| 8 | Davis, Tyler | WIN_CIT29 | Four-Seam | RHH | 71.2 | 53.1 | 79.2 | 20.60 | Elite Weapon | Soft-Speed Separation |
| 9 | Zentko, Dylan | EVA_OTT | Changeup | RHH | 71.9 | 56.7 | 78.8 | 20.29 | Elite Weapon | Tight High-Spin Breakers |
| 10 | Cameron, Zach | WIN_CIT29 | Four-Seam | RHH | 68.6 | 46.5 | 78.2 | 19.85 | Command/Deception Weapon | Soft-Speed Separation |
| 11 | Alpern, Liam | FLO_Y'A | Slider | LHH | 71.3 | 58.4 | 77.3 | 19.24 | Elite Weapon | Tight High-Spin Breakers |
| 12 | Serrano, Elio | NEW_JER6 | Changeup | LHH | 69.5 | 52.8 | 77.0 | 19.05 | Elite Weapon | Soft-Speed Separation |
| 13 | Vecerka, Boris | QUE_CAP | Slider | RHH | 74.3 | 70.6 | 76.8 | 18.86 | Elite Weapon | Tight High-Spin Breakers |
| 14 | Kirby, Zach | WAS_WIL3 | Slider | RHH | 74.2 | 71.2 | 76.4 | 18.59 | Elite Weapon | Tight High-Spin Breakers |
| 15 | Grounds, Jackson | DOW_EAS1 | Four-Seam | LHH | 67.9 | 49.8 | 75.9 | 18.22 | Command/Deception Weapon | Soft-Speed Separation |
| 16 | Carroll, Jake | JOL_SLA | Slider | LHH | 70.4 | 60.5 | 75.3 | 17.82 | Elite Weapon | Tight High-Spin Breakers |
| 17 | Duncan, Tanner | DOW_EAS1 | Slider | RHH | 69.2 | 56.7 | 75.1 | 17.67 | Elite Weapon | Soft-Speed Separation |
| 18 | Ryan, Dillon | NEW_ENG23 | Slider | LHH | 71.4 | 64.9 | 74.9 | 17.58 | Elite Weapon | Tight High-Spin Breakers |
| 19 | Sabatine, Gino | TRI_VAL | Sinker | LHH | 58.4 | 20.0 | 74.9 | 17.57 | Command/Deception Weapon | Soft-Speed Separation |
| 20 | Grounds, Jackson | DOW_EAS1 | Curveball | LHH | 69.0 | 56.2 | 74.9 | 17.55 | Elite Weapon | Tight High-Spin Breakers |
| 21 | Glickstein, Aaron | SCH_BOO | Sinker | RHH | 64.0 | 40.9 | 73.9 | 16.86 | Command/Deception Weapon | Soft-Speed Separation |
| 22 | Petschke, Ben | EVA_OTT | Sinker | RHH | 60.3 | 28.1 | 73.6 | 16.64 | Command/Deception Weapon | Soft-Speed Separation |
| 23 | Mercado, Nelson | OTT_TIT | Four-Seam | RHH | 66.2 | 49.8 | 73.5 | 16.55 | Command/Deception Weapon | Soft-Speed Separation |
| 24 | Moore, Kyle | SCH_BOO | Slider | RHH | 65.6 | 47.6 | 73.5 | 16.53 | Command/Deception Weapon | Tight High-Spin Breakers |
| 25 | Garcia, Andrew | EVA_OTT | Sinker | RHH | 61.7 | 33.6 | 73.4 | 16.51 | Command/Deception Weapon | Soft-Speed Separation |

## Top 25 Development Targets

| Rank | Pitcher | Team | Pitch Type | Side | Final | Stuff+ | Exec+ | Exec Raw | Quadrant | Archetype |
|---|---|---|---|---|---|---|---|---|---|---|
| 1016 | Harris, Everette | TRI_VAL | Slider | LHH | 58.0 | 80.0 | 46.1 | -2.75 | Development Target | Tight High-Spin Breakers |
| 931 | Vega, Lucas | TRO_AIG | Slider | LHH | 57.3 | 80.0 | 47.3 | -1.87 | Development Target | Tight High-Spin Breakers |
| 924 | Plumadore, Carson | WIN_CIT29 | Slider | LHH | 56.0 | 79.2 | 47.4 | -1.80 | Development Target | Tight High-Spin Breakers |
| 1129 | Saturria, Michael | NEW_ENG23 | Slider | LHH | 53.7 | 78.9 | 44.4 | -3.98 | Development Target | Tight High-Spin Breakers |
| 1036 | Saturria, Michael | NEW_ENG23 | Slider | RHH | 54.8 | 78.9 | 45.9 | -2.91 | Development Target | Tight High-Spin Breakers |
| 1384 | Petery, Dylan | WIN_CIT29 | Slider | RHH | 50.1 | 78.7 | 39.3 | -7.56 | Development Target | Tight High-Spin Breakers |
| 1505 | Conklin, MacCallan | TRO_AIG | Slider | LHH | 46.1 | 76.4 | 34.5 | -10.90 | Development Target | Soft-Speed Separation |
| 1420 | Conklin, MacCallan | TRO_AIG | Slider | RHH | 48.5 | 76.4 | 38.0 | -8.49 | Development Target | Soft-Speed Separation |
| 1552 | Voytko, Fawster | TRO_AIG | Slider | RHH | 41.6 | 75.9 | 28.4 | -15.22 | Development Target | Tight High-Spin Breakers |
| 1303 | Morgan, Marcus | JOL_SLA | Slider | LHH | 50.4 | 75.6 | 41.0 | -6.35 | Development Target | Tight High-Spin Breakers |
| 1551 | Godwin, Connor | NEW_YOR13 | Slider | LHH | 41.5 | 75.2 | 28.5 | -15.17 | Development Target | Tight High-Spin Breakers |
| 1342 | Godwin, Connor | NEW_YOR13 | Slider | RHH | 49.9 | 75.2 | 40.3 | -6.83 | Development Target | Tight High-Spin Breakers |
| 1130 | Ronne, Andrew | GAT_GRI | Slider | LHH | 52.5 | 74.3 | 44.3 | -3.98 | Development Target | Tight High-Spin Breakers |
| 1144 | Whitesell, Max | FLO_Y'A | Slider | LHH | 52.1 | 73.7 | 44.1 | -4.14 | Development Target | Tight High-Spin Breakers |
| 839 | Martinez, Mason | TRI_VAL | Slider | LHH | 55.4 | 73.6 | 48.8 | -0.87 | Development Target | Soft-Speed Separation |
| 1374 | Campbell, Tyler | MIS_MUD | Slider | RHH | 48.8 | 73.0 | 39.6 | -7.32 | Development Target | Tight High-Spin Breakers |
| 1052 | Campbell, Tyler | MIS_MUD | Slider | LHH | 53.0 | 73.0 | 45.6 | -3.07 | Development Target | Tight High-Spin Breakers |
| 1143 | Brothers, Kellen | SUS_COU1 | Slider | RHH | 51.9 | 72.8 | 44.1 | -4.14 | Development Target | Soft-Speed Separation |
| 1546 | Burcham, Jacob | GAT_GRI | Slider | LHH | 42.4 | 72.6 | 30.7 | -13.60 | Development Target | Tight High-Spin Breakers |
| 1349 | Burcham, Jacob | GAT_GRI | Slider | RHH | 49.0 | 72.6 | 40.1 | -6.95 | Development Target | Tight High-Spin Breakers |
| 1453 | McKillican, Adam | QUE_CAP | Slider | LHH | 46.6 | 72.6 | 36.8 | -9.33 | Development Target | Tight High-Spin Breakers |
| 1553 | Thiels, Brenton | MIS_MUD | Slider | LHH | 40.3 | 72.3 | 27.9 | -15.55 | Development Target | Soft-Speed Separation |
| 1503 | Thiels, Brenton | MIS_MUD | Slider | RHH | 45.1 | 72.3 | 34.7 | -10.77 | Development Target | Soft-Speed Separation |
| 1524 | Forsyth, Braden | MIS_MUD | Slider | LHH | 44.1 | 71.9 | 33.4 | -11.67 | Development Target | Tight High-Spin Breakers |
| 1364 | Forsyth, Braden | MIS_MUD | Slider | RHH | 48.6 | 71.9 | 39.8 | -7.18 | Development Target | Tight High-Spin Breakers |

## Top 25 Elite Weapons

| Rank | Pitcher | Team | Pitch Type | Side | Final | Stuff+ | Exec+ | Exec Raw | Quadrant | Archetype |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | Ryan, Dillon | NEW_ENG23 | Slider | RHH | 77.6 | 64.9 | 80.0 | 23.76 | Elite Weapon | Tight High-Spin Breakers |
| 13 | Vecerka, Boris | QUE_CAP | Slider | RHH | 74.3 | 70.6 | 76.8 | 18.86 | Elite Weapon | Tight High-Spin Breakers |
| 14 | Kirby, Zach | WAS_WIL3 | Slider | RHH | 74.2 | 71.2 | 76.4 | 18.59 | Elite Weapon | Tight High-Spin Breakers |
| 7 | Bargo, Casey | NEW_ENG23 | Slider | RHH | 73.9 | 62.4 | 79.5 | 20.79 | Elite Weapon | Tight High-Spin Breakers |
| 3 | Grounds, Jackson | DOW_EAS1 | Curveball | RHH | 73.3 | 56.2 | 80.0 | 21.86 | Elite Weapon | Tight High-Spin Breakers |
| 47 | Harper, Scott | NEW_YOR13 | Slider | RHH | 72.1 | 80.0 | 69.6 | 13.81 | Elite Weapon | Tight High-Spin Breakers |
| 9 | Zentko, Dylan | EVA_OTT | Changeup | RHH | 71.9 | 56.7 | 78.8 | 20.29 | Elite Weapon | Tight High-Spin Breakers |
| 18 | Ryan, Dillon | NEW_ENG23 | Slider | LHH | 71.4 | 64.9 | 74.9 | 17.58 | Elite Weapon | Tight High-Spin Breakers |
| 11 | Alpern, Liam | FLO_Y'A | Slider | LHH | 71.3 | 58.4 | 77.3 | 19.24 | Elite Weapon | Tight High-Spin Breakers |
| 8 | Davis, Tyler | WIN_CIT29 | Four-Seam | RHH | 71.2 | 53.1 | 79.2 | 20.60 | Elite Weapon | Soft-Speed Separation |
| 38 | Bauer, Patrick | QUE_CAP | Slider | RHH | 70.9 | 73.6 | 70.8 | 14.69 | Elite Weapon | Tight High-Spin Breakers |
| 16 | Carroll, Jake | JOL_SLA | Slider | LHH | 70.4 | 60.5 | 75.3 | 17.82 | Elite Weapon | Tight High-Spin Breakers |
| 12 | Serrano, Elio | NEW_JER6 | Changeup | LHH | 69.5 | 52.8 | 77.0 | 19.05 | Elite Weapon | Soft-Speed Separation |
| 33 | McEvoy, Aidan | FLO_Y'A | Slider | LHH | 69.4 | 66.8 | 71.3 | 14.99 | Elite Weapon | Tight High-Spin Breakers |
| 17 | Duncan, Tanner | DOW_EAS1 | Slider | RHH | 69.2 | 56.7 | 75.1 | 17.67 | Elite Weapon | Soft-Speed Separation |
| 31 | Hickey, Matt | GAT_GRI | Slider | RHH | 69.1 | 63.2 | 72.3 | 15.70 | Elite Weapon | Tight High-Spin Breakers |
| 20 | Grounds, Jackson | DOW_EAS1 | Curveball | LHH | 69.0 | 56.2 | 74.9 | 17.55 | Elite Weapon | Tight High-Spin Breakers |
| 35 | Nakata, Yuto | QUE_CAP | Slider | RHH | 68.7 | 64.7 | 71.2 | 14.94 | Elite Weapon | Tight High-Spin Breakers |
| 26 | Lawson, Nathan | FLO_Y'A | Changeup | LHH | 68.4 | 58.4 | 73.3 | 16.40 | Elite Weapon | Soft-Speed Separation |
| 78 | Morrissey, Joe | EVA_OTT | Slider | RHH | 67.9 | 73.4 | 66.7 | 11.75 | Elite Weapon | Tight High-Spin Breakers |
| 34 | Jones, Logan | TRI_VAL | Slider | LHH | 67.7 | 60.8 | 71.3 | 14.99 | Elite Weapon | Tight High-Spin Breakers |
| 63 | Donnan, Blake | FLO_Y'A | Slider | RHH | 67.6 | 68.5 | 68.2 | 12.80 | Elite Weapon | Tight High-Spin Breakers |
| 29 | Barraza, Chris | MIS_MUD | Slider | RHH | 67.4 | 55.4 | 72.9 | 16.14 | Elite Weapon | Tight High-Spin Breakers |
| 49 | Escobar, Anthony | TRO_AIG | Changeup | LHH | 66.9 | 62.6 | 69.5 | 13.74 | Elite Weapon | Soft-Speed Separation |
| 218 | Vega, Lucas | TRO_AIG | Slider | RHH | 66.8 | 80.0 | 60.8 | 7.61 | Elite Weapon | Tight High-Spin Breakers |