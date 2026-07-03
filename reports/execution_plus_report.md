# Execution+ Report

- Master input file: `data\processed\master_pitch_evaluation_table.csv`
- Stuff+ input file: `data\processed\stuff_plus_scores.csv`
- Output file: `data\processed\execution_plus_scores.csv`
- Scored rows: 1,323

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
| Low Priority | 383 | 42.8 | 43.1 | 43.0 |
| Command/Deception Weapon | 337 | 52.9 | 42.7 | 57.7 |
| Development Target | 307 | 46.6 | 58.1 | 41.9 |
| Elite Weapon | 296 | 58.4 | 58.6 | 58.7 |

## Top 25 Execution+

| Rank | Pitcher | Team | Pitch Type | Side | Final | Stuff+ | Exec+ | Exec Raw | Quadrant | Archetype |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | Moore, Kyle | SCH_BOO | Slider | RHH | 72.5 | 42.2 | 80.0 | 25.14 | Command/Deception Weapon | Tight High-Spin Breakers |
| 2 | Grounds, Jackson | DOW_EAS1 | Four-Seam | RHH | 72.2 | 49.0 | 80.0 | 22.80 | Command/Deception Weapon | Arm-Side Run Power |
| 3 | Morgan, Cooper | QUE_CAP | Curveball | LHH | 72.0 | 50.0 | 80.0 | 22.27 | Command/Deception Weapon | Tight High-Spin Breakers |
| 4 | Cameron, Zach | WIN_CIT29 | Four-Seam | RHH | 69.8 | 43.9 | 80.0 | 21.89 | Command/Deception Weapon | Arm-Side Run Power |
| 5 | Grounds, Jackson | DOW_EAS1 | Curveball | RHH | 72.5 | 53.4 | 80.0 | 21.69 | Elite Weapon | Tight High-Spin Breakers |
| 6 | Ryan, Dillon | NEW_ENG23 | Slider | RHH | 74.4 | 62.6 | 79.8 | 20.82 | Elite Weapon | Tight High-Spin Breakers |
| 7 | Bargo, Casey | NEW_ENG23 | Slider | RHH | 73.0 | 59.4 | 79.3 | 20.46 | Elite Weapon | Tight High-Spin Breakers |
| 8 | Peyton, Blake | GAT_GRI | Changeup | RHH | 69.2 | 47.6 | 79.0 | 20.24 | Command/Deception Weapon | Glove-Side Power Break |
| 9 | Davis, Tyler | WIN_CIT29 | Four-Seam | RHH | 70.8 | 53.5 | 78.6 | 19.99 | Elite Weapon | Arm-Side Run Power |
| 10 | Vecerka, Boris | QUE_CAP | Slider | RHH | 75.1 | 67.9 | 78.6 | 19.94 | Elite Weapon | Tight High-Spin Breakers |
| 11 | Lawson, Nathan | FLO_Y'A | Changeup | LHH | 72.0 | 58.4 | 78.3 | 19.74 | Elite Weapon | Soft-Speed Separation |
| 12 | Grounds, Jackson | DOW_EAS1 | Four-Seam | LHH | 68.8 | 49.0 | 77.8 | 19.39 | Command/Deception Weapon | Arm-Side Run Power |
| 13 | Rodriguez, Joe Joe | NEW_JER6 | Changeup | LHH | 69.8 | 53.7 | 77.1 | 18.90 | Elite Weapon | Soft-Speed Separation |
| 14 | Grounds, Jackson | DOW_EAS1 | Curveball | LHH | 69.5 | 53.4 | 76.8 | 18.73 | Elite Weapon | Tight High-Spin Breakers |
| 15 | Sabatine, Gino | TRI_VAL | Sinker | LHH | 59.0 | 21.2 | 75.8 | 17.98 | Command/Deception Weapon | Soft-Speed Separation |
| 16 | Serrano, Elio | NEW_JER6 | Changeup | LHH | 68.2 | 53.2 | 75.1 | 17.53 | Elite Weapon | Soft-Speed Separation |
| 17 | Alpern, Liam | FLO_Y'A | Slider | LHH | 71.4 | 64.5 | 74.7 | 17.24 | Elite Weapon | Tight High-Spin Breakers |
| 18 | Kirby, Zach | WAS_WIL3 | Slider | RHH | 73.6 | 72.6 | 74.4 | 17.04 | Elite Weapon | Tight High-Spin Breakers |
| 19 | Sechrist, Zander | WAS_WIL3 | Curveball | RHH | 63.3 | 40.2 | 73.7 | 16.56 | Command/Deception Weapon | Soft-Speed Separation |
| 20 | Ryan, Dillon | NEW_ENG23 | Slider | LHH | 70.0 | 62.6 | 73.6 | 16.46 | Elite Weapon | Tight High-Spin Breakers |
| 21 | Carroll, Jake | JOL_SLA | Slider | LHH | 70.9 | 68.0 | 72.5 | 15.73 | Elite Weapon | Tight High-Spin Breakers |
| 22 | Glickstein, Aaron | SCH_BOO | Sinker | RHH | 62.4 | 40.0 | 72.5 | 15.73 | Command/Deception Weapon | Arm-Side Run Power |
| 23 | Colon, Jeffrey | TRO_AIG | Sinker | RHH | 61.9 | 38.6 | 72.4 | 15.64 | Command/Deception Weapon | Arm-Side Run Power |
| 24 | Escobar, Anthony | TRO_AIG | Changeup | LHH | 69.0 | 62.2 | 72.3 | 15.57 | Elite Weapon | Soft-Speed Separation |
| 25 | Gregory, Ben | GAT_GRI | Four-Seam | RHH | 63.2 | 43.2 | 72.3 | 15.55 | Command/Deception Weapon | Arm-Side Run Power |

## Top 25 Development Targets

| Rank | Pitcher | Team | Pitch Type | Side | Final | Stuff+ | Exec+ | Exec Raw | Quadrant | Archetype |
|---|---|---|---|---|---|---|---|---|---|---|
| 1019 | Plumadore, Carson | WIN_CIT29 | Slider | LHH | 54.7 | 80.0 | 42.8 | -5.05 | Development Target | Tight High-Spin Breakers |
| 966 | Vega, Lucas | TRO_AIG | Slider | LHH | 55.6 | 80.0 | 43.7 | -4.37 | Development Target | Tight High-Spin Breakers |
| 949 | Harris, Everette | TRI_VAL | Slider | LHH | 57.7 | 80.0 | 44.2 | -4.04 | Development Target | Tight High-Spin Breakers |
| 711 | Plumadore, Carson | WIN_CIT29 | Slider | RHH | 58.9 | 80.0 | 48.7 | -0.89 | Development Target | Tight High-Spin Breakers |
| 1264 | Campbell, Tyler | MIS_MUD | Slider | RHH | 47.4 | 79.2 | 34.0 | -11.18 | Development Target | Tight High-Spin Breakers |
| 1031 | Campbell, Tyler | MIS_MUD | Slider | LHH | 53.4 | 79.2 | 42.5 | -5.20 | Development Target | Tight High-Spin Breakers |
| 991 | Saturria, Michael | NEW_ENG23 | Slider | LHH | 53.4 | 77.2 | 43.3 | -4.65 | Development Target | Tight High-Spin Breakers |
| 861 | Saturria, Michael | NEW_ENG23 | Slider | RHH | 55.2 | 77.2 | 46.1 | -2.76 | Development Target | Tight High-Spin Breakers |
| 1053 | Whitesell, Max | FLO_Y'A | Slider | LHH | 51.7 | 74.5 | 42.1 | -5.51 | Development Target | Glove-Side Power Break |
| 1300 | Godwin, Connor | NEW_YOR13 | Slider | LHH | 42.0 | 74.0 | 28.5 | -15.03 | Development Target | Tight High-Spin Breakers |
| 1109 | Godwin, Connor | NEW_YOR13 | Slider | RHH | 50.7 | 74.0 | 40.9 | -6.34 | Development Target | Tight High-Spin Breakers |
| 829 | Ronne, Andrew | GAT_GRI | Slider | LHH | 54.7 | 73.9 | 46.7 | -2.33 | Development Target | Tight High-Spin Breakers |
| 1306 | Burcham, Jacob | GAT_GRI | Slider | LHH | 40.7 | 73.5 | 26.9 | -16.15 | Development Target | Tight High-Spin Breakers |
| 1130 | Burcham, Jacob | GAT_GRI | Slider | RHH | 50.1 | 73.5 | 40.3 | -6.74 | Development Target | Tight High-Spin Breakers |
| 1271 | Forsyth, Braden | MIS_MUD | Slider | LHH | 44.7 | 71.3 | 33.6 | -11.44 | Development Target | Tight High-Spin Breakers |
| 1240 | Forsyth, Braden | MIS_MUD | Slider | RHH | 46.3 | 71.3 | 35.9 | -9.87 | Development Target | Tight High-Spin Breakers |
| 1255 | Morgan, Marcus | JOL_SLA | Slider | LHH | 45.5 | 71.2 | 34.7 | -10.67 | Development Target | Tight High-Spin Breakers |
| 914 | Cohn, Cooper | NIU_HUS | Slider | LHH | 52.6 | 70.7 | 45.1 | -3.41 | Development Target | Tight High-Spin Breakers |
| 640 | Martinez, Mason | TRI_VAL | Slider | LHH | 55.9 | 70.6 | 49.9 | -0.09 | Development Target | Glove-Side Power Break |
| 924 | Williams, Brian | MIS_MUD | Splitter | RHH | 52.4 | 70.5 | 44.9 | -3.56 | Development Target | Soft-Speed Separation |
| 890 | Williams, Brian | MIS_MUD | Splitter | LHH | 52.9 | 70.5 | 45.6 | -3.10 | Development Target | Soft-Speed Separation |
| 1045 | Brothers, Kellen | SUS_COU1 | Slider | RHH | 50.3 | 69.5 | 42.3 | -5.34 | Development Target | Glove-Side Power Break |
| 790 | Marklund, Brandon | OTT_TIT | Slider | LHH | 53.6 | 69.1 | 47.3 | -1.91 | Development Target | Tight High-Spin Breakers |
| 1206 | Smith, Ethan | WIN_CIT29 | Slider | LHH | 46.8 | 69.0 | 37.5 | -8.70 | Development Target | Tight High-Spin Breakers |
| 1292 | Thiels, Brenton | MIS_MUD | Slider | LHH | 41.4 | 68.8 | 29.8 | -14.06 | Development Target | Glove-Side Power Break |

## Top 25 Elite Weapons

| Rank | Pitcher | Team | Pitch Type | Side | Final | Stuff+ | Exec+ | Exec Raw | Quadrant | Archetype |
|---|---|---|---|---|---|---|---|---|---|---|
| 10 | Vecerka, Boris | QUE_CAP | Slider | RHH | 75.1 | 67.9 | 78.6 | 19.94 | Elite Weapon | Tight High-Spin Breakers |
| 6 | Ryan, Dillon | NEW_ENG23 | Slider | RHH | 74.4 | 62.6 | 79.8 | 20.82 | Elite Weapon | Tight High-Spin Breakers |
| 30 | Harper, Scott | NEW_YOR13 | Slider | RHH | 74.0 | 80.0 | 70.7 | 14.47 | Elite Weapon | Tight High-Spin Breakers |
| 18 | Kirby, Zach | WAS_WIL3 | Slider | RHH | 73.6 | 72.6 | 74.4 | 17.04 | Elite Weapon | Tight High-Spin Breakers |
| 7 | Bargo, Casey | NEW_ENG23 | Slider | RHH | 73.0 | 59.4 | 79.3 | 20.46 | Elite Weapon | Tight High-Spin Breakers |
| 5 | Grounds, Jackson | DOW_EAS1 | Curveball | RHH | 72.5 | 53.4 | 80.0 | 21.69 | Elite Weapon | Tight High-Spin Breakers |
| 11 | Lawson, Nathan | FLO_Y'A | Changeup | LHH | 72.0 | 58.4 | 78.3 | 19.74 | Elite Weapon | Soft-Speed Separation |
| 17 | Alpern, Liam | FLO_Y'A | Slider | LHH | 71.4 | 64.5 | 74.7 | 17.24 | Elite Weapon | Tight High-Spin Breakers |
| 21 | Carroll, Jake | JOL_SLA | Slider | LHH | 70.9 | 68.0 | 72.5 | 15.73 | Elite Weapon | Tight High-Spin Breakers |
| 9 | Davis, Tyler | WIN_CIT29 | Four-Seam | RHH | 70.8 | 53.5 | 78.6 | 19.99 | Elite Weapon | Arm-Side Run Power |
| 20 | Ryan, Dillon | NEW_ENG23 | Slider | LHH | 70.0 | 62.6 | 73.6 | 16.46 | Elite Weapon | Tight High-Spin Breakers |
| 13 | Rodriguez, Joe Joe | NEW_JER6 | Changeup | LHH | 69.8 | 53.7 | 77.1 | 18.90 | Elite Weapon | Soft-Speed Separation |
| 14 | Grounds, Jackson | DOW_EAS1 | Curveball | LHH | 69.5 | 53.4 | 76.8 | 18.73 | Elite Weapon | Tight High-Spin Breakers |
| 24 | Escobar, Anthony | TRO_AIG | Changeup | LHH | 69.0 | 62.2 | 72.3 | 15.57 | Elite Weapon | Soft-Speed Separation |
| 116 | Harper, Scott | NEW_YOR13 | Slider | LHH | 69.0 | 80.0 | 63.6 | 9.50 | Elite Weapon | Tight High-Spin Breakers |
| 46 | McEvoy, Aidan | FLO_Y'A | Slider | LHH | 68.9 | 69.4 | 69.1 | 13.31 | Elite Weapon | Soft-Speed Separation |
| 36 | Hickey, Matt | GAT_GRI | Slider | RHH | 68.5 | 65.4 | 70.2 | 14.08 | Elite Weapon | Tight High-Spin Breakers |
| 16 | Serrano, Elio | NEW_JER6 | Changeup | LHH | 68.2 | 53.2 | 75.1 | 17.53 | Elite Weapon | Soft-Speed Separation |
| 26 | Jones, Logan | TRI_VAL | Slider | LHH | 67.5 | 57.5 | 72.2 | 15.51 | Elite Weapon | Tight High-Spin Breakers |
| 53 | Donnan, Blake | FLO_Y'A | Slider | RHH | 67.5 | 67.1 | 67.9 | 12.52 | Elite Weapon | Tight High-Spin Breakers |
| 29 | Toribio, Noe | TRO_AIG | Slider | RHH | 67.0 | 58.5 | 71.0 | 14.67 | Elite Weapon | Tight High-Spin Breakers |
| 50 | Nakata, Yuto | QUE_CAP | Slider | RHH | 66.8 | 63.0 | 68.8 | 13.10 | Elite Weapon | Tight High-Spin Breakers |
| 226 | Vega, Lucas | TRO_AIG | Slider | RHH | 66.4 | 80.0 | 59.1 | 6.38 | Elite Weapon | Tight High-Spin Breakers |
| 43 | Hagan, Jack | DOW_EAS1 | Slider | RHH | 66.1 | 59.5 | 69.3 | 13.49 | Elite Weapon | Tight High-Spin Breakers |
| 28 | Davis, Tyler | WIN_CIT29 | Four-Seam | LHH | 65.9 | 53.5 | 71.6 | 15.08 | Elite Weapon | Arm-Side Run Power |