# Execution+ Report

- Master input file: `data\processed\master_pitch_evaluation_table.csv`
- Stuff+ input file: `data\processed\stuff_plus_scores.csv`
- Output file: `data\processed\execution_plus_scores.csv`
- Scored rows: 1,527

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
| Low Priority | 408 | 42.8 | 42.6 | 43.1 |
| Development Target | 395 | 46.2 | 57.7 | 42.1 |
| Command/Deception Weapon | 366 | 53.3 | 42.4 | 57.8 |
| Elite Weapon | 358 | 58.0 | 57.6 | 58.7 |

## Top 25 Execution+

| Rank | Pitcher | Team | Pitch Type | Side | Final | Stuff+ | Exec+ | Exec Raw | Quadrant | Archetype |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | Moore, Kyle | SCH_BOO | Slider | RHH | 72.8 | 46.5 | 80.0 | 23.96 | Command/Deception Weapon | Tight High-Spin Breakers |
| 2 | Grounds, Jackson | DOW_EAS1 | Four-Seam | RHH | 72.6 | 49.8 | 80.0 | 22.94 | Command/Deception Weapon | Soft-Speed Separation |
| 3 | Ryan, Dillon | NEW_ENG23 | Slider | RHH | 76.7 | 65.2 | 80.0 | 22.82 | Elite Weapon | Tight High-Spin Breakers |
| 4 | Morgan, Cooper | QUE_CAP | Curveball | LHH | 71.2 | 45.8 | 80.0 | 22.66 | Command/Deception Weapon | Tight High-Spin Breakers |
| 5 | Peyton, Blake | GAT_GRI | Changeup | RHH | 70.8 | 47.5 | 80.0 | 21.70 | Command/Deception Weapon | Tight High-Spin Breakers |
| 6 | Debban, Caleb | NEW_JER6 | Four-Seam | RHH | 68.5 | 39.3 | 80.0 | 21.68 | Command/Deception Weapon | Soft-Speed Separation |
| 7 | Bargo, Casey | NEW_ENG23 | Slider | RHH | 74.1 | 60.9 | 80.0 | 21.42 | Elite Weapon | Tight High-Spin Breakers |
| 8 | Grounds, Jackson | DOW_EAS1 | Curveball | RHH | 73.3 | 59.8 | 79.2 | 20.85 | Elite Weapon | Tight High-Spin Breakers |
| 9 | Davis, Tyler | WIN_CIT29 | Four-Seam | RHH | 71.5 | 53.7 | 79.0 | 20.71 | Elite Weapon | Soft-Speed Separation |
| 10 | Cameron, Zach | WIN_CIT29 | Four-Seam | RHH | 68.9 | 44.7 | 78.9 | 20.62 | Command/Deception Weapon | Soft-Speed Separation |
| 11 | Lawson, Nathan | FLO_Y'A | Changeup | LHH | 72.5 | 58.9 | 78.4 | 20.29 | Elite Weapon | Soft-Speed Separation |
| 12 | Zentko, Dylan | EVA_OTT | Changeup | RHH | 71.8 | 56.7 | 78.4 | 20.24 | Elite Weapon | Tight High-Spin Breakers |
| 13 | Alpern, Liam | FLO_Y'A | Slider | LHH | 72.0 | 60.2 | 77.2 | 19.44 | Elite Weapon | Tight High-Spin Breakers |
| 14 | Grounds, Jackson | DOW_EAS1 | Four-Seam | LHH | 68.9 | 49.8 | 77.0 | 19.24 | Command/Deception Weapon | Soft-Speed Separation |
| 15 | Glickstein, Aaron | SCH_BOO | Sinker | RHH | 66.2 | 40.8 | 76.6 | 19.00 | Command/Deception Weapon | Soft-Speed Separation |
| 16 | Kirby, Zach | WAS_WIL3 | Slider | RHH | 74.2 | 70.9 | 76.3 | 18.73 | Elite Weapon | Tight High-Spin Breakers |
| 17 | Serrano, Elio | NEW_JER6 | Changeup | LHH | 69.4 | 53.6 | 76.2 | 18.68 | Elite Weapon | Soft-Speed Separation |
| 18 | Hickey, Matt | GAT_GRI | Slider | RHH | 71.7 | 63.2 | 75.7 | 18.34 | Elite Weapon | Tight High-Spin Breakers |
| 19 | Leduc, Zachary | TRO_AIG | Slider | RHH | 71.5 | 64.1 | 75.1 | 17.92 | Elite Weapon | Tight High-Spin Breakers |
| 20 | Carroll, Jake | JOL_SLA | Slider | LHH | 70.3 | 60.9 | 74.7 | 17.63 | Elite Weapon | Tight High-Spin Breakers |
| 21 | Ryan, Dillon | NEW_ENG23 | Slider | LHH | 71.3 | 65.2 | 74.5 | 17.46 | Elite Weapon | Tight High-Spin Breakers |
| 22 | Leduc, Zachary | TRO_AIG | Slider | LHH | 71.0 | 64.1 | 74.4 | 17.43 | Elite Weapon | Tight High-Spin Breakers |
| 23 | Vecerka, Boris | QUE_CAP | Slider | RHH | 72.5 | 69.8 | 74.3 | 17.34 | Elite Weapon | Tight High-Spin Breakers |
| 24 | Sabatine, Gino | TRI_VAL | Sinker | LHH | 58.7 | 20.0 | 74.1 | 17.21 | Command/Deception Weapon | Soft-Speed Separation |
| 25 | Grounds, Jackson | DOW_EAS1 | Curveball | LHH | 69.6 | 59.8 | 74.0 | 17.14 | Elite Weapon | Tight High-Spin Breakers |

## Top 25 Development Targets

| Rank | Pitcher | Team | Pitch Type | Side | Final | Stuff+ | Exec+ | Exec Raw | Quadrant | Archetype |
|---|---|---|---|---|---|---|---|---|---|---|
| 949 | Harris, Everette | TRI_VAL | Slider | LHH | 57.9 | 80.0 | 46.7 | -2.32 | Development Target | Tight High-Spin Breakers |
| 893 | Vega, Lucas | TRO_AIG | Slider | LHH | 57.0 | 80.0 | 47.5 | -1.79 | Development Target | Tight High-Spin Breakers |
| 740 | Plumadore, Carson | WIN_CIT29 | Slider | LHH | 57.5 | 78.9 | 49.8 | -0.15 | Development Target | Tight High-Spin Breakers |
| 1316 | Petery, Dylan | WIN_CIT29 | Slider | RHH | 49.8 | 77.4 | 39.6 | -7.42 | Development Target | Tight High-Spin Breakers |
| 1044 | Saturria, Michael | NEW_ENG23 | Slider | LHH | 53.6 | 76.1 | 45.4 | -3.30 | Development Target | Tight High-Spin Breakers |
| 952 | Saturria, Michael | NEW_ENG23 | Slider | RHH | 54.6 | 76.1 | 46.7 | -2.34 | Development Target | Tight High-Spin Breakers |
| 1386 | Conklin, MacCallan | TRO_AIG | Slider | LHH | 47.9 | 76.1 | 37.4 | -8.98 | Development Target | Soft-Speed Separation |
| 1322 | Conklin, MacCallan | TRO_AIG | Slider | RHH | 49.4 | 76.1 | 39.5 | -7.51 | Development Target | Soft-Speed Separation |
| 1353 | Campbell, Tyler | MIS_MUD | Slider | RHH | 48.8 | 76.1 | 38.7 | -8.08 | Development Target | Tight High-Spin Breakers |
| 1003 | Campbell, Tyler | MIS_MUD | Slider | LHH | 54.1 | 76.1 | 46.0 | -2.83 | Development Target | Tight High-Spin Breakers |
| 1482 | Voytko, Fawster | TRO_AIG | Slider | RHH | 43.8 | 75.3 | 32.0 | -12.85 | Development Target | Tight High-Spin Breakers |
| 1089 | Whitesell, Max | FLO_Y'A | Slider | LHH | 52.6 | 74.7 | 44.6 | -3.87 | Development Target | Tight High-Spin Breakers |
| 1498 | Godwin, Connor | NEW_YOR13 | Slider | LHH | 41.9 | 74.2 | 29.7 | -14.48 | Development Target | Tight High-Spin Breakers |
| 1232 | Godwin, Connor | NEW_YOR13 | Slider | RHH | 50.5 | 74.2 | 41.8 | -5.86 | Development Target | Tight High-Spin Breakers |
| 1230 | Morgan, Marcus | JOL_SLA | Slider | LHH | 50.3 | 73.4 | 41.8 | -5.84 | Development Target | Tight High-Spin Breakers |
| 764 | Martinez, Mason | TRI_VAL | Slider | LHH | 55.6 | 73.0 | 49.4 | -0.44 | Development Target | Soft-Speed Separation |
| 1405 | McKillican, Adam | QUE_CAP | Slider | LHH | 46.6 | 72.7 | 36.8 | -9.39 | Development Target | Tight High-Spin Breakers |
| 991 | Ronne, Andrew | GAT_GRI | Slider | LHH | 53.2 | 72.5 | 46.2 | -2.72 | Development Target | Tight High-Spin Breakers |
| 1480 | Burcham, Jacob | GAT_GRI | Slider | LHH | 43.5 | 72.2 | 32.7 | -12.33 | Development Target | Tight High-Spin Breakers |
| 1286 | Burcham, Jacob | GAT_GRI | Slider | RHH | 49.0 | 72.2 | 40.5 | -6.79 | Development Target | Tight High-Spin Breakers |
| 1076 | Brothers, Kellen | SUS_COU1 | Slider | RHH | 51.9 | 71.3 | 44.9 | -3.66 | Development Target | Soft-Speed Separation |
| 1145 | Gregory, Ben | GAT_GRI | Slider | RHH | 50.8 | 70.9 | 43.4 | -4.68 | Development Target | Tight High-Spin Breakers |
| 1446 | Forsyth, Braden | MIS_MUD | Slider | LHH | 44.5 | 70.5 | 34.8 | -10.88 | Development Target | Tight High-Spin Breakers |
| 1359 | Forsyth, Braden | MIS_MUD | Slider | RHH | 47.1 | 70.5 | 38.5 | -8.22 | Development Target | Tight High-Spin Breakers |
| 1493 | Thiels, Brenton | MIS_MUD | Slider | LHH | 41.0 | 70.2 | 30.0 | -14.30 | Development Target | Soft-Speed Separation |

## Top 25 Elite Weapons

| Rank | Pitcher | Team | Pitch Type | Side | Final | Stuff+ | Exec+ | Exec Raw | Quadrant | Archetype |
|---|---|---|---|---|---|---|---|---|---|---|
| 3 | Ryan, Dillon | NEW_ENG23 | Slider | RHH | 76.7 | 65.2 | 80.0 | 22.82 | Elite Weapon | Tight High-Spin Breakers |
| 16 | Kirby, Zach | WAS_WIL3 | Slider | RHH | 74.2 | 70.9 | 76.3 | 18.73 | Elite Weapon | Tight High-Spin Breakers |
| 7 | Bargo, Casey | NEW_ENG23 | Slider | RHH | 74.1 | 60.9 | 80.0 | 21.42 | Elite Weapon | Tight High-Spin Breakers |
| 8 | Grounds, Jackson | DOW_EAS1 | Curveball | RHH | 73.3 | 59.8 | 79.2 | 20.85 | Elite Weapon | Tight High-Spin Breakers |
| 23 | Vecerka, Boris | QUE_CAP | Slider | RHH | 72.5 | 69.8 | 74.3 | 17.34 | Elite Weapon | Tight High-Spin Breakers |
| 11 | Lawson, Nathan | FLO_Y'A | Changeup | LHH | 72.5 | 58.9 | 78.4 | 20.29 | Elite Weapon | Soft-Speed Separation |
| 13 | Alpern, Liam | FLO_Y'A | Slider | LHH | 72.0 | 60.2 | 77.2 | 19.44 | Elite Weapon | Tight High-Spin Breakers |
| 12 | Zentko, Dylan | EVA_OTT | Changeup | RHH | 71.8 | 56.7 | 78.4 | 20.24 | Elite Weapon | Tight High-Spin Breakers |
| 18 | Hickey, Matt | GAT_GRI | Slider | RHH | 71.7 | 63.2 | 75.7 | 18.34 | Elite Weapon | Tight High-Spin Breakers |
| 55 | Harper, Scott | NEW_YOR13 | Slider | RHH | 71.5 | 80.0 | 68.5 | 13.20 | Elite Weapon | Tight High-Spin Breakers |
| 19 | Leduc, Zachary | TRO_AIG | Slider | RHH | 71.5 | 64.1 | 75.1 | 17.92 | Elite Weapon | Tight High-Spin Breakers |
| 9 | Davis, Tyler | WIN_CIT29 | Four-Seam | RHH | 71.5 | 53.7 | 79.0 | 20.71 | Elite Weapon | Soft-Speed Separation |
| 21 | Ryan, Dillon | NEW_ENG23 | Slider | LHH | 71.3 | 65.2 | 74.5 | 17.46 | Elite Weapon | Tight High-Spin Breakers |
| 22 | Leduc, Zachary | TRO_AIG | Slider | LHH | 71.0 | 64.1 | 74.4 | 17.43 | Elite Weapon | Tight High-Spin Breakers |
| 27 | Escobar, Anthony | TRO_AIG | Changeup | LHH | 70.4 | 63.1 | 73.9 | 17.06 | Elite Weapon | Soft-Speed Separation |
| 20 | Carroll, Jake | JOL_SLA | Slider | LHH | 70.3 | 60.9 | 74.7 | 17.63 | Elite Weapon | Tight High-Spin Breakers |
| 31 | Nakata, Yuto | QUE_CAP | Slider | RHH | 69.8 | 63.3 | 73.0 | 16.44 | Elite Weapon | Tight High-Spin Breakers |
| 25 | Grounds, Jackson | DOW_EAS1 | Curveball | LHH | 69.6 | 59.8 | 74.0 | 17.14 | Elite Weapon | Tight High-Spin Breakers |
| 17 | Serrano, Elio | NEW_JER6 | Changeup | LHH | 69.4 | 53.6 | 76.2 | 18.68 | Elite Weapon | Soft-Speed Separation |
| 49 | Donnan, Blake | FLO_Y'A | Slider | RHH | 68.2 | 67.3 | 69.2 | 13.67 | Elite Weapon | Tight High-Spin Breakers |
| 60 | McEvoy, Aidan | FLO_Y'A | Slider | LHH | 67.9 | 69.4 | 68.0 | 12.87 | Elite Weapon | Tight High-Spin Breakers |
| 38 | Jones, Logan | TRI_VAL | Slider | LHH | 67.7 | 59.0 | 71.7 | 15.45 | Elite Weapon | Tight High-Spin Breakers |
| 179 | Vega, Lucas | TRO_AIG | Slider | RHH | 67.1 | 80.0 | 61.8 | 8.40 | Elite Weapon | Tight High-Spin Breakers |
| 33 | Barraza, Chris | MIS_MUD | Slider | RHH | 67.1 | 54.2 | 72.8 | 16.25 | Elite Weapon | Tight High-Spin Breakers |
| 32 | Rodriguez, Joe Joe | NEW_JER6 | Changeup | LHH | 66.8 | 52.4 | 73.0 | 16.42 | Elite Weapon | Soft-Speed Separation |