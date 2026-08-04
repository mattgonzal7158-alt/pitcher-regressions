# Execution+ Report

- Master input file: `data\processed\master_pitch_evaluation_table.csv`
- Stuff+ input file: `data\processed\stuff_plus_scores.csv`
- Output file: `data\processed\execution_plus_scores.csv`
- Scored rows: 1,783

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
| Low Priority | 520 | 42.8 | 43.0 | 42.9 |
| Command/Deception Weapon | 462 | 53.1 | 42.7 | 57.9 |
| Development Target | 416 | 46.7 | 58.7 | 42.1 |
| Elite Weapon | 385 | 58.2 | 58.8 | 58.6 |

## Top 25 Execution+

| Rank | Pitcher | Team | Pitch Type | Side | Final | Stuff+ | Exec+ | Exec Raw | Quadrant | Archetype |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | Sanders, Brayden | MIS_MUD | Slider | RHH | 75.3 | 48.8 | 80.0 | 25.89 | Command/Deception Weapon | Tight High-Spin Breakers |
| 2 | Grounds, Jackson | DOW_EAS1 | Curveball | RHH | 74.2 | 47.5 | 80.0 | 25.16 | Command/Deception Weapon | Tight High-Spin Breakers |
| 3 | Grounds, Jackson | DOW_EAS1 | Four-Seam | RHH | 71.2 | 47.0 | 80.0 | 22.34 | Command/Deception Weapon | Soft-Speed Separation |
| 4 | Bargo, Casey | NEW_ENG23 | Slider | RHH | 75.2 | 63.4 | 80.0 | 21.59 | Elite Weapon | Tight High-Spin Breakers |
| 5 | Ryan, Dillon | NEW_ENG23 | Slider | RHH | 74.9 | 62.9 | 80.0 | 21.49 | Elite Weapon | Tight High-Spin Breakers |
| 6 | Morgan, Cooper | QUE_CAP | Curveball | LHH | 70.4 | 48.5 | 80.0 | 21.15 | Command/Deception Weapon | Tight High-Spin Breakers |
| 7 | Heintz, Danny | FLO_Y'A | Four-Seam | RHH | 69.6 | 46.3 | 80.0 | 20.89 | Command/Deception Weapon | Soft-Speed Separation |
| 8 | Grounds, Jackson | DOW_EAS1 | Curveball | LHH | 69.6 | 47.5 | 79.7 | 20.54 | Command/Deception Weapon | Tight High-Spin Breakers |
| 9 | Harley, Tristan | SUS_COU1 | Slider | RHH | 74.9 | 67.2 | 79.3 | 20.25 | Elite Weapon | Tight High-Spin Breakers |
| 10 | Debban, Caleb | NEW_JER6 | Four-Seam | RHH | 68.2 | 44.1 | 79.2 | 20.18 | Command/Deception Weapon | Soft-Speed Separation |
| 11 | Vecerka, Boris | QUE_CAP | Slider | RHH | 74.8 | 68.1 | 78.7 | 19.85 | Elite Weapon | Tight High-Spin Breakers |
| 12 | Davis, Tyler | WIN_CIT29 | Four-Seam | RHH | 70.1 | 52.6 | 78.4 | 19.61 | Elite Weapon | Soft-Speed Separation |
| 13 | Morrissey, Joe | EVA_OTT | Cutter | RHH | 70.1 | 53.0 | 78.3 | 19.52 | Elite Weapon | Tight High-Spin Breakers |
| 14 | Carroll, Jake | JOL_SLA | Slider | LHH | 71.8 | 59.9 | 77.8 | 19.24 | Elite Weapon | Tight High-Spin Breakers |
| 15 | Alpern, Liam | FLO_Y'A | Slider | LHH | 70.0 | 55.3 | 77.2 | 18.78 | Elite Weapon | Tight High-Spin Breakers |
| 16 | Grounds, Jackson | DOW_EAS1 | Four-Seam | LHH | 67.2 | 47.0 | 76.5 | 18.31 | Command/Deception Weapon | Soft-Speed Separation |
| 17 | Duncan, Tanner | DOW_EAS1 | Slider | RHH | 70.3 | 58.4 | 76.4 | 18.20 | Elite Weapon | Soft-Speed Separation |
| 18 | Kirby, Zach | WAS_WIL3 | Slider | RHH | 74.1 | 71.6 | 76.3 | 18.16 | Elite Weapon | Tight High-Spin Breakers |
| 19 | Earwood, Micah | SUS_COU1 | Four-Seam | RHH | 66.2 | 44.6 | 76.1 | 18.02 | Command/Deception Weapon | Soft-Speed Separation |
| 20 | Bauer, Patrick | QUE_CAP | Slider | RHH | 74.8 | 74.8 | 76.1 | 18.00 | Elite Weapon | Tight High-Spin Breakers |
| 21 | Glickstein, Aaron | SCH_BOO | Sinker | RHH | 64.4 | 40.0 | 75.4 | 17.53 | Command/Deception Weapon | Soft-Speed Separation |
| 22 | Ryan, Dillon | NEW_ENG23 | Slider | LHH | 70.8 | 62.9 | 75.2 | 17.38 | Elite Weapon | Tight High-Spin Breakers |
| 23 | Jones, Breyln | NEW_JER6 | Curveball | RHH | 63.6 | 38.0 | 75.1 | 17.31 | Command/Deception Weapon | Tight High-Spin Breakers |
| 24 | Cameron, Zach | WIN_CIT29 | Four-Seam | RHH | 65.5 | 45.1 | 74.8 | 17.13 | Command/Deception Weapon | Soft-Speed Separation |
| 25 | Colon, Jeffrey | TRO_AIG | Sinker | RHH | 63.1 | 37.3 | 74.7 | 17.04 | Command/Deception Weapon | Soft-Speed Separation |

## Top 25 Development Targets

| Rank | Pitcher | Team | Pitch Type | Side | Final | Stuff+ | Exec+ | Exec Raw | Quadrant | Archetype |
|---|---|---|---|---|---|---|---|---|---|---|
| 1490 | Harris, Everette | TRI_VAL | Slider | RHH | 51.3 | 77.1 | 41.0 | -6.23 | Development Target | Tight High-Spin Breakers |
| 1522 | Petery, Dylan | WIN_CIT29 | Slider | LHH | 50.4 | 75.6 | 40.3 | -6.68 | Development Target | Tight High-Spin Breakers |
| 1140 | Petery, Dylan | WIN_CIT29 | Slider | RHH | 54.5 | 75.6 | 46.3 | -2.53 | Development Target | Tight High-Spin Breakers |
| 1150 | Ronne, Andrew | GAT_GRI | Slider | LHH | 54.3 | 75.0 | 46.2 | -2.62 | Development Target | Tight High-Spin Breakers |
| 1227 | Saturria, Michael | NEW_ENG23 | Slider | LHH | 53.5 | 74.8 | 45.2 | -3.34 | Development Target | Tight High-Spin Breakers |
| 1027 | Saturria, Michael | NEW_ENG23 | Slider | RHH | 55.3 | 74.8 | 47.8 | -1.50 | Development Target | Tight High-Spin Breakers |
| 1430 | Morgan, Marcus | JOL_SLA | Slider | LHH | 51.1 | 74.5 | 41.8 | -5.67 | Development Target | Tight High-Spin Breakers |
| 1766 | Voytko, Fawster | TRO_AIG | Slider | LHH | 40.0 | 73.9 | 26.0 | -16.56 | Development Target | Tight High-Spin Breakers |
| 1541 | Voytko, Fawster | TRO_AIG | Slider | RHH | 49.5 | 73.9 | 39.7 | -7.08 | Development Target | Tight High-Spin Breakers |
| 1060 | Marklund, Brandon | OTT_TIT | Slider | LHH | 54.7 | 73.5 | 47.4 | -1.78 | Development Target | Tight High-Spin Breakers |
| 1521 | Conklin, MacCallan | TRO_AIG | Slider | LHH | 49.7 | 73.2 | 40.3 | -6.68 | Development Target | Tight High-Spin Breakers |
| 1202 | Conklin, MacCallan | TRO_AIG | Slider | RHH | 53.3 | 73.2 | 45.5 | -3.12 | Development Target | Tight High-Spin Breakers |
| 1730 | Blence, Connor | WIN_CIT29 | Slider | LHH | 43.3 | 72.8 | 31.2 | -12.97 | Development Target | Tight High-Spin Breakers |
| 1286 | Blence, Connor | WIN_CIT29 | Slider | RHH | 52.4 | 72.8 | 44.4 | -3.89 | Development Target | Tight High-Spin Breakers |
| 1712 | Brodsky, Jack | WAS_WIL3 | Slider | RHH | 44.3 | 71.9 | 33.0 | -11.75 | Development Target | Tight High-Spin Breakers |
| 1307 | Cohn, Cooper | NIU_HUS | Slider | LHH | 51.9 | 71.9 | 44.0 | -4.13 | Development Target | Tight High-Spin Breakers |
| 1734 | Godwin, Connor | NEW_YOR13 | Slider | LHH | 42.4 | 71.1 | 30.6 | -13.39 | Development Target | Tight High-Spin Breakers |
| 1463 | Godwin, Connor | NEW_YOR13 | Slider | RHH | 49.9 | 71.1 | 41.4 | -5.93 | Development Target | Tight High-Spin Breakers |
| 954 | Good, Ty | GAT_GRI | Cutter | RHH | 54.8 | 70.9 | 48.6 | -0.95 | Development Target | Soft-Speed Separation |
| 1695 | Forsyth, Braden | MIS_MUD | Slider | LHH | 44.6 | 70.7 | 34.0 | -11.02 | Development Target | Tight High-Spin Breakers |
| 1404 | Forsyth, Braden | MIS_MUD | Slider | RHH | 50.4 | 70.7 | 42.4 | -5.24 | Development Target | Tight High-Spin Breakers |
| 858 | Sparks, Alec | GAT_GRI | Slider | RHH | 55.4 | 70.2 | 49.9 | -0.09 | Development Target | Tight High-Spin Breakers |
| 1114 | Calderon, Jean | LAK_ERI24 | Slider | LHH | 53.1 | 69.6 | 46.7 | -2.26 | Development Target | Tight High-Spin Breakers |
| 1049 | Long, Maddox | WAS_WIL3 | Slider | LHH | 53.6 | 69.4 | 47.5 | -1.72 | Development Target | Tight High-Spin Breakers |
| 1317 | Kines, Gunnar | JOL_SLA | Changeup | RHH | 51.0 | 69.3 | 43.9 | -4.25 | Development Target | Tight High-Spin Breakers |

## Top 25 Elite Weapons

| Rank | Pitcher | Team | Pitch Type | Side | Final | Stuff+ | Exec+ | Exec Raw | Quadrant | Archetype |
|---|---|---|---|---|---|---|---|---|---|---|
| 4 | Bargo, Casey | NEW_ENG23 | Slider | RHH | 75.2 | 63.4 | 80.0 | 21.59 | Elite Weapon | Tight High-Spin Breakers |
| 9 | Harley, Tristan | SUS_COU1 | Slider | RHH | 74.9 | 67.2 | 79.3 | 20.25 | Elite Weapon | Tight High-Spin Breakers |
| 5 | Ryan, Dillon | NEW_ENG23 | Slider | RHH | 74.9 | 62.9 | 80.0 | 21.49 | Elite Weapon | Tight High-Spin Breakers |
| 20 | Bauer, Patrick | QUE_CAP | Slider | RHH | 74.8 | 74.8 | 76.1 | 18.00 | Elite Weapon | Tight High-Spin Breakers |
| 11 | Vecerka, Boris | QUE_CAP | Slider | RHH | 74.8 | 68.1 | 78.7 | 19.85 | Elite Weapon | Tight High-Spin Breakers |
| 18 | Kirby, Zach | WAS_WIL3 | Slider | RHH | 74.1 | 71.6 | 76.3 | 18.16 | Elite Weapon | Tight High-Spin Breakers |
| 14 | Carroll, Jake | JOL_SLA | Slider | LHH | 71.8 | 59.9 | 77.8 | 19.24 | Elite Weapon | Tight High-Spin Breakers |
| 61 | Harper, Scott | NEW_YOR13 | Slider | RHH | 70.8 | 76.6 | 69.5 | 13.45 | Elite Weapon | Tight High-Spin Breakers |
| 22 | Ryan, Dillon | NEW_ENG23 | Slider | LHH | 70.8 | 62.9 | 75.2 | 17.38 | Elite Weapon | Tight High-Spin Breakers |
| 32 | Flontek, Zac | DOW_EAS1 | Slider | RHH | 70.4 | 66.2 | 73.1 | 15.98 | Elite Weapon | Tight High-Spin Breakers |
| 17 | Duncan, Tanner | DOW_EAS1 | Slider | RHH | 70.3 | 58.4 | 76.4 | 18.20 | Elite Weapon | Soft-Speed Separation |
| 34 | Flontek, Zac | DOW_EAS1 | Slider | LHH | 70.1 | 66.2 | 72.8 | 15.74 | Elite Weapon | Tight High-Spin Breakers |
| 13 | Morrissey, Joe | EVA_OTT | Cutter | RHH | 70.1 | 53.0 | 78.3 | 19.52 | Elite Weapon | Tight High-Spin Breakers |
| 12 | Davis, Tyler | WIN_CIT29 | Four-Seam | RHH | 70.1 | 52.6 | 78.4 | 19.61 | Elite Weapon | Soft-Speed Separation |
| 15 | Alpern, Liam | FLO_Y'A | Slider | LHH | 70.0 | 55.3 | 77.2 | 18.78 | Elite Weapon | Tight High-Spin Breakers |
| 36 | McEvoy, Aidan | FLO_Y'A | Slider | LHH | 69.0 | 63.1 | 72.5 | 15.51 | Elite Weapon | Tight High-Spin Breakers |
| 56 | Nakata, Yuto | QUE_CAP | Slider | RHH | 68.9 | 68.6 | 70.0 | 13.79 | Elite Weapon | Tight High-Spin Breakers |
| 52 | O'Dell, Casey | JOL_SLA | Slider | RHH | 68.7 | 67.5 | 70.2 | 13.97 | Elite Weapon | Tight High-Spin Breakers |
| 38 | Sparks, Alec | GAT_GRI | Curveball | LHH | 68.7 | 62.8 | 72.1 | 15.26 | Elite Weapon | Tight High-Spin Breakers |
| 49 | Donnan, Blake | FLO_Y'A | Slider | RHH | 68.4 | 65.3 | 70.6 | 14.23 | Elite Weapon | Tight High-Spin Breakers |
| 30 | Jones, Logan | TRI_VAL | Slider | LHH | 68.3 | 58.6 | 73.3 | 16.11 | Elite Weapon | Tight High-Spin Breakers |
| 79 | Marynczak, Arlo | TRI_VAL | Slider | RHH | 67.9 | 70.4 | 67.9 | 12.35 | Elite Weapon | Tight High-Spin Breakers |
| 39 | Barraza, Chris | MIS_MUD | Slider | RHH | 67.4 | 58.4 | 72.1 | 15.26 | Elite Weapon | Tight High-Spin Breakers |
| 144 | Vega, Lucas | TRO_AIG | Slider | RHH | 67.2 | 78.9 | 63.3 | 9.17 | Elite Weapon | Tight High-Spin Breakers |
| 35 | Scafidi, Christian | LAK_ERI24 | Cutter | RHH | 67.1 | 55.9 | 72.7 | 15.70 | Elite Weapon | Tight High-Spin Breakers |