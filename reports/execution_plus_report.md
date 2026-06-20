# Execution+ Report

- Master input file: `data\processed\master_pitch_evaluation_table.csv`
- Stuff+ input file: `data\processed\stuff_plus_scores.csv`
- Output file: `data\processed\execution_plus_scores.csv`
- Scored rows: 988

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
| Low Priority | 279 | 42.6 | 43.1 | 43.0 |
| Command/Deception Weapon | 255 | 52.8 | 42.8 | 57.6 |
| Elite Weapon | 229 | 58.4 | 58.2 | 58.6 |
| Development Target | 225 | 46.2 | 58.2 | 41.4 |

## Top 25 Execution+

| Rank | Pitcher | Team | Pitch Type | Side | Final | Stuff+ | Exec+ | Exec Raw | Quadrant | Archetype |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | Sechrist, Zander | WAS_WIL3 | Curveball | RHH | 64.3 | 25.6 | 80.0 | 22.37 | Command/Deception Weapon | Soft-Speed Separation |
| 2 | Perez, Kelvin | WAS_WIL3 | Slider | RHH | 74.6 | 61.7 | 80.0 | 21.21 | Elite Weapon | Tight High-Spin Breakers |
| 3 | Grounds, Jackson | DOW_EAS1 | Four-Seam | RHH | 70.8 | 50.5 | 79.7 | 20.98 | Elite Weapon | Arm-Side Run Power |
| 4 | Davis, Tyler | WIN_CIT29 | Four-Seam | RHH | 71.9 | 56.7 | 78.4 | 20.01 | Elite Weapon | Arm-Side Run Power |
| 5 | Bargo, Casey | NEW_ENG23 | Slider | RHH | 71.9 | 57.9 | 77.9 | 19.72 | Elite Weapon | Tight High-Spin Breakers |
| 6 | Grounds, Jackson | DOW_EAS1 | Four-Seam | LHH | 69.0 | 50.5 | 77.1 | 19.11 | Elite Weapon | Arm-Side Run Power |
| 7 | Escobar, Anthony | TRO_AIG | Changeup | LHH | 71.3 | 59.6 | 76.3 | 18.53 | Elite Weapon | Soft-Speed Separation |
| 8 | Cameron, Zach | WIN_CIT29 | Four-Seam | RHH | 66.0 | 43.1 | 76.2 | 18.46 | Command/Deception Weapon | Arm-Side Run Power |
| 9 | Willeman, Landon | EVA_OTT | Changeup | LHH | 66.2 | 43.9 | 76.1 | 18.43 | Command/Deception Weapon | Soft-Speed Separation |
| 10 | Correa, Nelvin | QUE_CAP | Cutter | RHH | 67.6 | 51.4 | 74.8 | 17.47 | Elite Weapon | Riding Shape / Lower Velo |
| 11 | Sesar, Jorden | SUS_COU1 | Curveball | RHH | 64.2 | 40.6 | 74.7 | 17.46 | Command/Deception Weapon | Tight High-Spin Breakers |
| 12 | Peyton, Blake | GAT_GRI | Changeup | RHH | 65.8 | 45.9 | 74.6 | 17.39 | Command/Deception Weapon | Riding Shape / Lower Velo |
| 13 | Wehrle, Tyler | WIN_CIT29 | Four-Seam | LHH | 65.0 | 47.9 | 72.6 | 15.98 | Command/Deception Weapon | Arm-Side Run Power |
| 14 | Pierson, Kenny | LAK_ERI24 | Sinker | RHH | 58.5 | 28.0 | 72.5 | 15.84 | Command/Deception Weapon | Tight High-Spin Breakers |
| 15 | Grounds, Jackson | DOW_EAS1 | Curveball | RHH | 71.6 | 69.1 | 72.4 | 15.84 | Elite Weapon | Tight High-Spin Breakers |
| 16 | Davis, Tyler | WIN_CIT29 | Four-Seam | LHH | 67.6 | 56.7 | 72.3 | 15.72 | Elite Weapon | Arm-Side Run Power |
| 17 | Lawson, Nathan | FLO_Y'A | Sinker | LHH | 63.2 | 43.3 | 72.1 | 15.62 | Command/Deception Weapon | Arm-Side Run Power |
| 18 | Ryan, Dillon | NEW_ENG23 | Slider | RHH | 69.4 | 63.4 | 71.8 | 15.41 | Elite Weapon | Tight High-Spin Breakers |
| 19 | Harper, Scott | NEW_YOR13 | Slider | RHH | 74.5 | 80.0 | 71.5 | 15.20 | Elite Weapon | Tight High-Spin Breakers |
| 20 | Jones, Logan | TRI_VAL | Slider | LHH | 67.2 | 58.7 | 70.8 | 14.71 | Elite Weapon | Tight High-Spin Breakers |
| 21 | Hensey, Rob | SUS_COU1 | Changeup | RHH | 60.3 | 37.9 | 70.4 | 14.41 | Command/Deception Weapon | Riding Shape / Lower Velo |
| 22 | Perez, Kelvin | WAS_WIL3 | Four-Seam | RHH | 63.0 | 47.1 | 70.2 | 14.25 | Command/Deception Weapon | Arm-Side Run Power |
| 23 | Rodriguez, Joe Joe | NEW_JER6 | Four-Seam | LHH | 63.7 | 49.4 | 70.2 | 14.24 | Command/Deception Weapon | Arm-Side Run Power |
| 24 | Widener, Jacob | SUS_COU1 | Four-Seam | LHH | 59.8 | 37.4 | 70.1 | 14.15 | Command/Deception Weapon | Riding Shape / Lower Velo |
| 25 | Correa, Nelvin | QUE_CAP | Cutter | LHH | 64.1 | 51.4 | 69.8 | 13.99 | Elite Weapon | Riding Shape / Lower Velo |

## Top 25 Development Targets

| Rank | Pitcher | Team | Pitch Type | Side | Final | Stuff+ | Exec+ | Exec Raw | Quadrant | Archetype |
|---|---|---|---|---|---|---|---|---|---|---|
| 943 | Campbell, Tyler | MIS_MUD | Slider | RHH | 48.0 | 80.0 | 33.8 | -11.46 | Development Target | Tight High-Spin Breakers |
| 783 | Plumadore, Carson | WIN_CIT29 | Slider | RHH | 56.5 | 80.0 | 41.9 | -5.72 | Development Target | Tight High-Spin Breakers |
| 721 | Garcia, Brett | OTT_TIT | Curveball | LHH | 56.3 | 80.0 | 43.9 | -4.28 | Development Target | Tight High-Spin Breakers |
| 641 | Garcia, Brett | OTT_TIT | Curveball | RHH | 57.8 | 80.0 | 46.1 | -2.75 | Development Target | Tight High-Spin Breakers |
| 609 | Whitesell, Max | FLO_Y'A | Slider | LHH | 56.2 | 77.2 | 46.9 | -2.21 | Development Target | Riding Shape / Lower Velo |
| 671 | Salata, Derek | SCH_BOO | Splitter | LHH | 54.6 | 75.6 | 45.4 | -3.28 | Development Target | Soft-Speed Separation |
| 581 | Thompson, Ross | SCH_BOO | Splitter | LHH | 56.1 | 75.4 | 47.6 | -1.67 | Development Target | Soft-Speed Separation |
| 867 | Saturria, Michael | NEW_ENG23 | Slider | RHH | 49.7 | 73.9 | 39.2 | -7.62 | Development Target | Tight High-Spin Breakers |
| 858 | Saturria, Michael | NEW_ENG23 | Slider | LHH | 49.9 | 73.9 | 39.5 | -7.42 | Development Target | Tight High-Spin Breakers |
| 969 | Godwin, Connor | NEW_YOR13 | Slider | LHH | 43.0 | 72.7 | 30.2 | -13.95 | Development Target | Tight High-Spin Breakers |
| 780 | Godwin, Connor | NEW_YOR13 | Slider | RHH | 51.2 | 72.7 | 41.9 | -5.69 | Development Target | Tight High-Spin Breakers |
| 849 | Burcham, Jacob | GAT_GRI | Slider | RHH | 49.7 | 72.6 | 39.7 | -7.24 | Development Target | Tight High-Spin Breakers |
| 946 | Nakata, Yuto | QUE_CAP | Splitter | LHH | 44.8 | 71.5 | 33.3 | -11.81 | Development Target | Soft-Speed Separation |
| 570 | Armstrong, Andrew | NEW_YOR13 | Slider | RHH | 54.8 | 70.5 | 48.0 | -1.44 | Development Target | Tight High-Spin Breakers |
| 915 | Matos, Dwayne | OTT_TIT | Slider | LHH | 46.1 | 69.5 | 36.0 | -9.85 | Development Target | Soft-Speed Separation |
| 644 | Matos, Dwayne | OTT_TIT | Slider | RHH | 53.1 | 69.5 | 45.9 | -2.86 | Development Target | Soft-Speed Separation |
| 617 | Cohn, Cooper | NIU_HUS | Slider | LHH | 53.1 | 68.1 | 46.7 | -2.35 | Development Target | Tight High-Spin Breakers |
| 853 | Forsyth, Braden | MIS_MUD | Slider | LHH | 48.1 | 67.9 | 39.6 | -7.31 | Development Target | Tight High-Spin Breakers |
| 654 | Forsyth, Braden | MIS_MUD | Slider | RHH | 52.4 | 67.9 | 45.7 | -3.01 | Development Target | Tight High-Spin Breakers |
| 939 | Scott, Brandon | LAK_ERI24 | Slider | LHH | 44.3 | 67.9 | 34.3 | -11.09 | Development Target | Tight High-Spin Breakers |
| 866 | Scott, Brandon | LAK_ERI24 | Slider | RHH | 47.8 | 67.9 | 39.2 | -7.61 | Development Target | Tight High-Spin Breakers |
| 959 | Thiels, Brenton | MIS_MUD | Cutter | RHH | 42.1 | 67.8 | 31.1 | -13.33 | Development Target | Arm-Side Run Power |
| 872 | Smith, Ethan | WIN_CIT29 | Slider | LHH | 47.5 | 67.4 | 39.0 | -7.78 | Development Target | Tight High-Spin Breakers |
| 944 | Shinn, Nathan | LAK_ERI24 | Curveball | RHH | 43.4 | 67.0 | 33.4 | -11.70 | Development Target | Tight High-Spin Breakers |
| 917 | Shinn, Nathan | LAK_ERI24 | Curveball | LHH | 45.2 | 67.0 | 36.0 | -9.90 | Development Target | Tight High-Spin Breakers |

## Top 25 Elite Weapons

| Rank | Pitcher | Team | Pitch Type | Side | Final | Stuff+ | Exec+ | Exec Raw | Quadrant | Archetype |
|---|---|---|---|---|---|---|---|---|---|---|
| 2 | Perez, Kelvin | WAS_WIL3 | Slider | RHH | 74.6 | 61.7 | 80.0 | 21.21 | Elite Weapon | Tight High-Spin Breakers |
| 19 | Harper, Scott | NEW_YOR13 | Slider | RHH | 74.5 | 80.0 | 71.5 | 15.20 | Elite Weapon | Tight High-Spin Breakers |
| 5 | Bargo, Casey | NEW_ENG23 | Slider | RHH | 71.9 | 57.9 | 77.9 | 19.72 | Elite Weapon | Tight High-Spin Breakers |
| 4 | Davis, Tyler | WIN_CIT29 | Four-Seam | RHH | 71.9 | 56.7 | 78.4 | 20.01 | Elite Weapon | Arm-Side Run Power |
| 15 | Grounds, Jackson | DOW_EAS1 | Curveball | RHH | 71.6 | 69.1 | 72.4 | 15.84 | Elite Weapon | Tight High-Spin Breakers |
| 7 | Escobar, Anthony | TRO_AIG | Changeup | LHH | 71.3 | 59.6 | 76.3 | 18.53 | Elite Weapon | Soft-Speed Separation |
| 3 | Grounds, Jackson | DOW_EAS1 | Four-Seam | RHH | 70.8 | 50.5 | 79.7 | 20.98 | Elite Weapon | Arm-Side Run Power |
| 42 | Carroll, Jake | JOL_SLA | Slider | LHH | 69.8 | 72.8 | 68.2 | 12.83 | Elite Weapon | Tight High-Spin Breakers |
| 41 | Alpern, Liam | FLO_Y'A | Slider | LHH | 69.7 | 72.3 | 68.3 | 12.88 | Elite Weapon | Tight High-Spin Breakers |
| 18 | Ryan, Dillon | NEW_ENG23 | Slider | RHH | 69.4 | 63.4 | 71.8 | 15.41 | Elite Weapon | Tight High-Spin Breakers |
| 6 | Grounds, Jackson | DOW_EAS1 | Four-Seam | LHH | 69.0 | 50.5 | 77.1 | 19.11 | Elite Weapon | Arm-Side Run Power |
| 40 | Grounds, Jackson | DOW_EAS1 | Curveball | LHH | 68.7 | 69.1 | 68.3 | 12.94 | Elite Weapon | Tight High-Spin Breakers |
| 54 | Kirby, Zach | WAS_WIL3 | Slider | RHH | 68.2 | 70.5 | 67.0 | 11.97 | Elite Weapon | Tight High-Spin Breakers |
| 62 | McEvoy, Aidan | FLO_Y'A | Slider | LHH | 68.2 | 72.4 | 66.0 | 11.31 | Elite Weapon | Soft-Speed Separation |
| 104 | Smith, Jackson | MIS_MUD | Slider | RHH | 67.7 | 79.3 | 62.2 | 8.64 | Elite Weapon | Tight High-Spin Breakers |
| 10 | Correa, Nelvin | QUE_CAP | Cutter | RHH | 67.6 | 51.4 | 74.8 | 17.47 | Elite Weapon | Riding Shape / Lower Velo |
| 16 | Davis, Tyler | WIN_CIT29 | Four-Seam | LHH | 67.6 | 56.7 | 72.3 | 15.72 | Elite Weapon | Arm-Side Run Power |
| 29 | Ryan, Dillon | NEW_ENG23 | Slider | LHH | 67.6 | 63.4 | 69.2 | 13.58 | Elite Weapon | Tight High-Spin Breakers |
| 20 | Jones, Logan | TRI_VAL | Slider | LHH | 67.2 | 58.7 | 70.8 | 14.71 | Elite Weapon | Tight High-Spin Breakers |
| 47 | Harajli, Ahmad | FLO_Y'A | Slider | RHH | 66.8 | 64.6 | 67.7 | 12.48 | Elite Weapon | Tight High-Spin Breakers |
| 60 | Donnan, Blake | FLO_Y'A | Slider | RHH | 66.8 | 67.8 | 66.2 | 11.41 | Elite Weapon | Tight High-Spin Breakers |
| 56 | Webster, Evan | FLO_Y'A | Cutter | LHH | 66.7 | 66.7 | 66.5 | 11.67 | Elite Weapon | Riding Shape / Lower Velo |
| 84 | Vitas, Ben | JOL_SLA | Splitter | LHH | 66.3 | 71.9 | 63.6 | 9.62 | Elite Weapon | Soft-Speed Separation |
| 83 | Webster, Evan | FLO_Y'A | Slider | LHH | 66.3 | 71.8 | 63.7 | 9.64 | Elite Weapon | Soft-Speed Separation |
| 46 | Maietta, Dante | WIN_CIT29 | Changeup | LHH | 66.1 | 62.3 | 67.7 | 12.52 | Elite Weapon | Soft-Speed Separation |