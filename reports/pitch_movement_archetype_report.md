# Frontier League Movement Archetypes

- Input file: `data\processed\movement_score_inputs.csv`
- Scored output: `data\processed\pitch_movement_archetypes.csv`
- Cluster summary: `data\processed\pitch_movement_archetype_summary.csv`
- Highest-performing archetype pitch list: `data\processed\highest_performing_archetype_pitches.csv`
- Undervalued pitch list: `data\processed\undervalued_movement_pitches.csv`
- Qualified pitcher-pitch types clustered: 744
- Features clustered: IVB, HB, spin rate, velocity, extension
- Selected cluster count: 4
- Full methodology write-up: `reports/FRONTIER_PITCH_VALUE_METHODOLOGY.md`

## How To Read This Report

Higher Pitch Value Score is better. It means the pitch has the outcome profile associated with lower expected xwOBA damage. Archetypes are movement-shape groups, not direct pitcher grades.

The cluster labels describe the average movement identity of each group. Average Pitch Value Score by cluster tells us which movement families performed best in this dataset, but individual pitches within a cluster can still vary widely based on command, usage, sequencing, and sample size.

## Cluster Count Test

| k | Inertia | Silhouette |
|---:|---:|---:|
| 2 | 2556.94 | 0.3031 |
| 3 | 2056.39 | 0.2998 |
| 4 | 1691.58 | 0.3060 **selected** |
| 5 | 1541.30 | 0.2478 |
| 6 | 1405.49 | 0.2315 |
| 7 | 1288.27 | 0.2345 |
| 8 | 1202.54 | 0.2456 |
| 9 | 1116.65 | 0.2461 |
| 10 | 1044.81 | 0.2526 |

## Archetype Summary

| Rank | Archetype | Pitches | Instances | Avg PVS | Avg xwOBA | IVB | HB | Spin | Velo | Ext | Common Pitch Types |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|
| 1 | `Tight High-Spin Breakers` | 23,940 | 216 | 52.7 | 0.239 | -1.0 | -2.4 | 2370 | 79.7 | 5.45 | Slider, Curveball, Cutter |
| 2 | `Soft-Speed Separation` | 11,479 | 108 | 52.2 | 0.241 | 6.8 | 10.7 | 1725 | 81.3 | 5.80 | Changeup, Splitter, Slider |
| 3 | `Glove-Side Power Break` | 23,900 | 162 | 49.6 | 0.244 | 12.1 | -10.1 | 2092 | 86.4 | 6.00 | Four-Seam, Sinker, Changeup |
| 4 | `Arm-Side Run Power` | 41,914 | 258 | 47.0 | 0.250 | 14.8 | 11.4 | 2206 | 90.3 | 5.96 | Four-Seam, Sinker, Cutter |

## Highest-Performing Archetypes

- `Tight High-Spin Breakers`: average PVS 52.7, avg xwOBA 0.239, typical shape -1.0 IVB / -2.4 HB at 79.7 mph.
- `Soft-Speed Separation`: average PVS 52.2, avg xwOBA 0.241, typical shape 6.8 IVB / 10.7 HB at 81.3 mph.

## Pitchers in Highest-Performing Archetypes

| Rank | Pitcher | Team | Pitch | Pitches | PVS | xwOBA | IVB | HB | Spin | Velo | Ext | Archetype |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | Grounds, Jackson | DOW_EAS1 | Curveball | 82 | 80.0 | 0.110 | -10.5 | -12.0 | 1946 | 81.4 | 5.35 | Tight High-Spin Breakers |
| 2 | Morgan, Cooper | QUE_CAP | Curveball | 51 | 80.0 | 0.119 | -1.0 | 16.8 | 2657 | 75.6 | 5.26 | Tight High-Spin Breakers |
| 3 | Vecerka, Boris | QUE_CAP | Slider | 61 | 80.0 | 0.109 | 2.5 | -11.8 | 2496 | 83.0 | 5.65 | Tight High-Spin Breakers |
| 4 | Carroll, Jake | JOL_SLA | Slider | 62 | 80.0 | 0.208 | -6.2 | 7.8 | 2033 | 75.2 | 6.10 | Tight High-Spin Breakers |
| 5 | Ryan, Dillon | NEW_ENG23 | Slider | 113 | 79.2 | 0.149 | -2.2 | -8.5 | 2495 | 85.4 | 5.84 | Tight High-Spin Breakers |
| 6 | Harper, Scott | NEW_YOR13 | Slider | 174 | 76.7 | 0.146 | 3.5 | -16.7 | 2675 | 79.8 | 5.63 | Tight High-Spin Breakers |
| 7 | Alpern, Liam | FLO_Y'A | Slider | 78 | 75.5 | 0.115 | -4.0 | 11.5 | 2219 | 76.8 | 5.55 | Tight High-Spin Breakers |
| 8 | Jones, Logan | TRI_VAL | Slider | 65 | 73.7 | 0.191 | 2.5 | 2.3 | 2341 | 83.5 | 5.69 | Tight High-Spin Breakers |
| 9 | Bargo, Casey | NEW_ENG23 | Slider | 56 | 72.8 | 0.178 | 1.5 | -5.0 | 2416 | 83.6 | 5.66 | Tight High-Spin Breakers |
| 10 | Kirby, Zach | WAS_WIL3 | Slider | 127 | 70.9 | 0.158 | 5.8 | -13.4 | 2204 | 78.0 | 5.68 | Tight High-Spin Breakers |
| 11 | Moore, Kyle | SCH_BOO | Slider | 53 | 70.4 | 0.178 | 8.8 | -1.2 | 2162 | 84.1 | 4.87 | Tight High-Spin Breakers |
| 12 | Nakata, Yuto | QUE_CAP | Slider | 90 | 69.8 | 0.162 | 4.4 | -7.8 | 2412 | 81.6 | 5.61 | Tight High-Spin Breakers |
| 13 | Toribio, Noe | TRO_AIG | Slider | 107 | 69.7 | 0.154 | 2.9 | 0.8 | 2241 | 82.6 | 5.77 | Tight High-Spin Breakers |
| 14 | Donnan, Blake | FLO_Y'A | Slider | 65 | 69.2 | 0.187 | 5.0 | -7.3 | 2367 | 80.5 | 5.42 | Tight High-Spin Breakers |
| 15 | Valdez, Alex | EVA_OTT | Cutter | 56 | 67.9 | 0.200 | 4.6 | -1.3 | 2085 | 86.3 | 5.32 | Tight High-Spin Breakers |
| 16 | Hickey, Matt | GAT_GRI | Slider | 75 | 67.6 | 0.194 | -1.8 | -6.8 | 2269 | 79.9 | 5.37 | Tight High-Spin Breakers |
| 17 | Balzan, Jackson | SUS_COU1 | Slider | 65 | 66.6 | 0.189 | 4.6 | 1.3 | 2165 | 79.6 | 5.24 | Tight High-Spin Breakers |
| 18 | Eisenbarger, Jack | QUE_CAP | Curveball | 71 | 66.4 | 0.214 | -3.6 | 12.2 | 2812 | 77.3 | 5.37 | Tight High-Spin Breakers |
| 19 | Garcia, Brett | OTT_TIT | Curveball | 104 | 66.1 | 0.177 | -16.9 | -8.0 | 2137 | 81.3 | 5.38 | Tight High-Spin Breakers |
| 20 | Salata, Derek | SCH_BOO | Curveball | 83 | 66.0 | 0.205 | -12.5 | -13.6 | 2678 | 74.7 | 5.46 | Tight High-Spin Breakers |
| 21 | Vega, Lucas | TRO_AIG | Slider | 117 | 66.0 | 0.153 | 6.5 | -10.3 | 2707 | 79.0 | 5.87 | Tight High-Spin Breakers |
| 22 | Smith, Jackson | MIS_MUD | Slider | 106 | 65.9 | 0.199 | 1.7 | -10.3 | 2663 | 77.9 | 4.79 | Tight High-Spin Breakers |
| 23 | Harris, Ben | GAT_GRI | Curveball | 205 | 65.7 | 0.218 | -14.2 | -7.5 | 2126 | 77.9 | 4.99 | Tight High-Spin Breakers |
| 24 | Binns, Malik | NEW_JER6 | Curveball | 55 | 65.6 | 0.187 | -7.6 | -16.2 | 2448 | 74.8 | 5.95 | Tight High-Spin Breakers |
| 25 | Morin, Jacob | QUE_CAP | Slider | 85 | 65.1 | 0.208 | 7.4 | -6.2 | 2495 | 77.4 | 5.50 | Tight High-Spin Breakers |
| 26 | Harajli, Ahmad | FLO_Y'A | Slider | 69 | 65.0 | 0.169 | -2.3 | -2.6 | 2060 | 80.6 | 6.04 | Tight High-Spin Breakers |
| 27 | Bohnert, Matthew | WIN_CIT29 | Curveball | 83 | 64.0 | 0.170 | -16.3 | 13.4 | 2816 | 78.2 | 4.77 | Tight High-Spin Breakers |
| 28 | Parsons, Billy | SUS_COU1 | Cutter | 56 | 64.0 | 0.184 | 9.5 | -2.9 | 2552 | 86.3 | 5.56 | Tight High-Spin Breakers |
| 29 | Petschke, Ben | EVA_OTT | Slider | 138 | 63.9 | 0.184 | -1.8 | -13.5 | 2637 | 81.0 | 5.06 | Tight High-Spin Breakers |
| 30 | Hill, Kaleb | OTT_TIT | Curveball | 201 | 63.4 | 0.211 | -4.4 | 13.2 | 2139 | 72.9 | 5.31 | Tight High-Spin Breakers |
| 31 | Fauci, Sonny | NEW_JER6 | Slider | 87 | 62.8 | 0.229 | -2.5 | -7.5 | 2331 | 83.4 | 5.95 | Tight High-Spin Breakers |
| 32 | Ronne, Andrew | GAT_GRI | Slider | 122 | 62.8 | 0.179 | 0.4 | -14.7 | 2597 | 81.4 | 5.96 | Tight High-Spin Breakers |
| 33 | Heredia-Bustos, Rolando | DOW_EAS1 | Curveball | 53 | 62.7 | 0.190 | 5.4 | -10.6 | 2199 | 73.7 | 5.06 | Tight High-Spin Breakers |
| 34 | Foster, Kobe | WAS_WIL3 | Slider | 118 | 62.6 | 0.187 | 5.0 | 5.9 | 2322 | 78.0 | 5.41 | Tight High-Spin Breakers |
| 35 | Simpson, Garret | EVA_OTT | Curveball | 94 | 62.3 | 0.203 | -12.2 | -13.3 | 2693 | 76.8 | 5.19 | Tight High-Spin Breakers |
| 36 | Hagan, Jack | DOW_EAS1 | Slider | 184 | 62.2 | 0.211 | 4.0 | -3.7 | 2437 | 84.3 | 5.72 | Tight High-Spin Breakers |
| 37 | Woolfolk, Dallas | MIS_MUD | Slider | 53 | 62.0 | 0.234 | 0.6 | -1.2 | 2299 | 82.5 | 5.08 | Tight High-Spin Breakers |
| 38 | Gregory, Ben | GAT_GRI | Slider | 60 | 61.9 | 0.239 | 1.3 | -4.9 | 2362 | 79.6 | 6.19 | Tight High-Spin Breakers |
| 39 | Maryniak, Connor | NEW_JER6 | Curveball | 121 | 61.8 | 0.225 | -8.9 | -4.6 | 2506 | 81.6 | 4.98 | Tight High-Spin Breakers |
| 40 | O'Hanlon, Michael | WAS_WIL3 | Slider | 57 | 61.8 | 0.239 | 2.8 | -2.4 | 2501 | 83.3 | 5.40 | Tight High-Spin Breakers |
| 41 | Gollert, Harley | QUE_CAP | Slider | 57 | 61.0 | 0.218 | 1.0 | 5.1 | 2222 | 79.4 | 5.09 | Tight High-Spin Breakers |
| 42 | Petery, Dylan | WIN_CIT29 | Curveball | 56 | 60.5 | 0.217 | -7.4 | -14.8 | 2567 | 74.4 | 5.40 | Tight High-Spin Breakers |
| 43 | Scafidi, Christian | LAK_ERI24 | Curveball | 55 | 60.5 | 0.195 | -6.9 | -3.1 | 2245 | 77.5 | 5.84 | Tight High-Spin Breakers |
| 44 | Good, Ty | GAT_GRI | Slider | 156 | 60.5 | 0.199 | 2.7 | -0.8 | 2067 | 79.3 | 5.83 | Tight High-Spin Breakers |
| 45 | Garcia, Andrew | EVA_OTT | Slider | 216 | 60.4 | 0.179 | 2.2 | -7.2 | 2331 | 82.2 | 5.39 | Tight High-Spin Breakers |
| 46 | Morgan, Cooper | QUE_CAP | Slider | 55 | 60.4 | 0.213 | 3.2 | 11.8 | 2501 | 78.2 | 5.50 | Tight High-Spin Breakers |
| 47 | Earwood, Micah | SUS_COU1 | Curveball | 82 | 60.1 | 0.204 | -7.1 | -6.8 | 2456 | 78.5 | 5.42 | Tight High-Spin Breakers |
| 48 | Widener, Jacob | SUS_COU1 | Slider | 85 | 60.1 | 0.229 | 3.3 | 16.1 | 2857 | 80.6 | 6.11 | Tight High-Spin Breakers |
| 49 | Gollert, Harley | TRO_AIG | Curveball | 52 | 59.8 | 0.240 | -6.4 | 6.2 | 2250 | 77.4 | 4.86 | Tight High-Spin Breakers |
| 50 | Majick, Eli | NEW_ENG23 | Cutter | 66 | 59.8 | 0.187 | 5.5 | -0.9 | 2502 | 82.8 | 5.72 | Tight High-Spin Breakers |
| 51 | Wiltse, Ryan | EVA_OTT | Curveball | 116 | 59.4 | 0.233 | -12.4 | -4.0 | 1911 | 74.3 | 5.89 | Tight High-Spin Breakers |
| 52 | Kemlage, Joe | NEW_ENG23 | Slider | 65 | 59.3 | 0.203 | -2.4 | 13.8 | 2610 | 82.2 | 5.50 | Tight High-Spin Breakers |
| 53 | Villers, Ian | QUE_CAP | Slider | 66 | 59.1 | 0.243 | -0.3 | -5.1 | 2117 | 82.3 | 5.94 | Tight High-Spin Breakers |
| 54 | Calderon, Jean | LAK_ERI24 | Slider | 73 | 59.0 | 0.200 | 1.3 | -9.7 | 2593 | 86.4 | 6.05 | Tight High-Spin Breakers |
| 55 | Vail, Tyler | NEW_YOR13 | Slider | 154 | 58.8 | 0.247 | 1.7 | -2.4 | 2269 | 80.4 | 6.04 | Tight High-Spin Breakers |
| 56 | Armstrong, Andrew | NEW_YOR13 | Slider | 105 | 58.7 | 0.244 | 2.4 | 8.0 | 2386 | 79.7 | 5.92 | Tight High-Spin Breakers |
| 57 | Langhorne, Miles | SUS_COU1 | Slider | 61 | 58.6 | 0.225 | 0.0 | -3.1 | 2487 | 86.8 | 5.90 | Tight High-Spin Breakers |
| 58 | Anibal, Trevor | NEW_ENG23 | Curveball | 99 | 58.6 | 0.236 | -15.3 | -9.3 | 2489 | 75.9 | 5.46 | Tight High-Spin Breakers |
| 59 | Long, Maddox | WAS_WIL3 | Slider | 226 | 58.5 | 0.199 | 2.8 | -8.6 | 2598 | 82.8 | 5.52 | Tight High-Spin Breakers |
| 60 | Leak, Anthony | NEW_YOR13 | Slider | 196 | 58.5 | 0.183 | 4.9 | -6.3 | 2316 | 83.3 | 5.87 | Tight High-Spin Breakers |
| 61 | Dill, Austin | TRI_VAL | Slider | 70 | 58.4 | 0.241 | 1.6 | -3.7 | 2565 | 79.3 | 4.97 | Tight High-Spin Breakers |
| 62 | Vailes, Gage | GAT_GRI | Slider | 249 | 58.3 | 0.211 | 6.1 | -11.7 | 2569 | 81.8 | 4.64 | Tight High-Spin Breakers |
| 63 | Brito, Richard | NEW_ENG23 | Slider | 73 | 58.1 | 0.202 | 3.6 | -6.0 | 2287 | 81.7 | 6.09 | Tight High-Spin Breakers |
| 64 | Vail, Tyler | NEW_YOR13 | Curveball | 182 | 58.1 | 0.217 | -2.9 | -5.5 | 2225 | 74.7 | 5.72 | Tight High-Spin Breakers |
| 65 | Shinn, Nathan | LAK_ERI24 | Slider | 138 | 58.1 | 0.220 | 0.3 | 0.8 | 2179 | 82.1 | 5.24 | Tight High-Spin Breakers |
| 66 | Plumadore, Carson | WIN_CIT29 | Slider | 96 | 58.1 | 0.206 | 2.7 | -5.3 | 2445 | 75.9 | 5.48 | Tight High-Spin Breakers |
| 67 | Cohn, Cooper | NIU_HUS | Slider | 63 | 58.1 | 0.190 | -1.2 | -13.7 | 2534 | 78.9 | 5.40 | Tight High-Spin Breakers |
| 68 | Marklund, Brandon | OTT_TIT | Slider | 124 | 57.9 | 0.247 | 6.4 | -14.2 | 2707 | 79.6 | 4.87 | Tight High-Spin Breakers |
| 69 | Bargo, Casey | FLO_Y'A | Slider | 60 | 57.8 | 0.211 | 0.0 | -3.7 | 2327 | 81.7 | 5.37 | Tight High-Spin Breakers |
| 70 | Gilleran, Jimmy | NEW_ENG23 | Slider | 80 | 57.8 | 0.200 | 3.4 | -3.8 | 2264 | 80.7 | 5.31 | Tight High-Spin Breakers |
| 71 | De Los Santos, Enmanuel | NEW_ENG23 | Curveball | 87 | 57.8 | 0.220 | -5.7 | -10.9 | 2219 | 71.2 | 6.48 | Tight High-Spin Breakers |
| 72 | Bice, Emmett | NEW_YOR13 | Slider | 260 | 57.7 | 0.228 | 2.1 | -2.7 | 2386 | 82.9 | 5.67 | Tight High-Spin Breakers |
| 73 | Saturria, Michael | NEW_ENG23 | Slider | 192 | 57.5 | 0.196 | 3.9 | -7.5 | 2712 | 80.4 | 5.84 | Tight High-Spin Breakers |
| 74 | Scott, Brandon | LAK_ERI24 | Slider | 139 | 57.4 | 0.202 | -0.3 | 6.9 | 2402 | 77.9 | 5.41 | Tight High-Spin Breakers |
| 75 | Cameron, Zach | WIN_CIT29 | Slider | 110 | 57.3 | 0.203 | 7.1 | -1.7 | 2347 | 81.5 | 5.43 | Tight High-Spin Breakers |
| 76 | Lefebvre, Charles | TRO_AIG | Curveball | 89 | 56.9 | 0.255 | -9.5 | -8.9 | 2468 | 77.8 | 6.13 | Tight High-Spin Breakers |
| 77 | Morgan, Marcus | JOL_SLA | Cutter | 56 | 56.8 | 0.197 | 6.5 | -3.1 | 2678 | 87.0 | 5.76 | Tight High-Spin Breakers |
| 78 | Helt, Robert | LAK_ERI24 | Slider | 213 | 56.8 | 0.233 | -1.3 | -5.1 | 2411 | 81.1 | 5.75 | Tight High-Spin Breakers |
| 79 | Garcia, Hector | WAS_WIL3 | Slider | 56 | 56.8 | 0.232 | 2.0 | -7.1 | 2355 | 77.3 | 5.72 | Tight High-Spin Breakers |
| 80 | Cooper, Garrett | NEW_YOR13 | Slider | 80 | 56.6 | 0.191 | 2.2 | -3.6 | 2143 | 81.0 | 5.71 | Tight High-Spin Breakers |
| 81 | Heredia-Bustos, Rolando | DOW_EAS1 | Slider | 369 | 56.5 | 0.207 | 6.7 | -4.2 | 2332 | 78.7 | 5.29 | Tight High-Spin Breakers |
| 82 | Peters, Garrett | NEW_YOR13 | Curveball | 118 | 56.5 | 0.230 | 0.7 | -0.7 | 2048 | 75.9 | 5.77 | Tight High-Spin Breakers |
| 83 | Eckaus, David | EVA_OTT | Slider | 151 | 56.4 | 0.217 | 1.9 | 4.6 | 2591 | 82.5 | 5.58 | Tight High-Spin Breakers |
| 84 | Smith, Jackson | MIS_MUD | Changeup | 76 | 56.3 | 0.242 | -1.4 | 17.6 | 2175 | 80.3 | 4.94 | Tight High-Spin Breakers |
| 85 | Petschke, Ben | EVA_OTT | Curveball | 164 | 56.3 | 0.235 | -9.7 | -15.7 | 2771 | 77.2 | 4.98 | Tight High-Spin Breakers |
| 86 | Cook, Cole | SCH_BOO | Slider | 155 | 56.2 | 0.234 | 3.5 | 5.7 | 2506 | 79.6 | 5.12 | Tight High-Spin Breakers |
| 87 | Balzan, Jackson | SUS_COU1 | Curveball | 69 | 56.1 | 0.218 | -4.9 | 5.4 | 2105 | 76.3 | 5.08 | Tight High-Spin Breakers |
| 88 | Harris, Everette | TRI_VAL | Slider | 53 | 56.1 | 0.219 | 1.2 | -8.7 | 2862 | 80.5 | 6.15 | Tight High-Spin Breakers |
| 89 | Kirby, Zach | WAS_WIL3 | Curveball | 105 | 56.1 | 0.233 | -18.3 | -10.7 | 2261 | 70.8 | 5.41 | Tight High-Spin Breakers |
| 90 | Simone, Andrew | TRO_AIG | Slider | 86 | 56.0 | 0.201 | 3.4 | -4.5 | 2155 | 83.6 | 5.68 | Tight High-Spin Breakers |
| 91 | Sesar, Jorden | SUS_COU1 | Curveball | 98 | 56.0 | 0.238 | -12.4 | -11.5 | 2425 | 74.8 | 6.02 | Tight High-Spin Breakers |
| 92 | Boies, Emiles | QUE_CAP | Curveball | 65 | 55.7 | 0.190 | -3.6 | -5.8 | 2119 | 76.8 | 5.69 | Tight High-Spin Breakers |
| 93 | Cook, Cole | SCH_BOO | Curveball | 89 | 55.7 | 0.226 | -3.2 | 6.0 | 2501 | 77.6 | 4.95 | Tight High-Spin Breakers |
| 94 | Majick, Eli | NEW_ENG23 | Slider | 175 | 55.5 | 0.229 | 3.7 | 8.3 | 2545 | 79.3 | 5.58 | Tight High-Spin Breakers |
| 95 | Milburn, Isaac | FLO_Y'A | Slider | 157 | 55.4 | 0.223 | -1.7 | 16.0 | 2649 | 78.6 | 4.84 | Tight High-Spin Breakers |
| 96 | Nova, Fraynel | LAK_ERI24 | Slider | 267 | 54.9 | 0.233 | -0.5 | -6.7 | 2273 | 80.6 | 5.62 | Tight High-Spin Breakers |
| 97 | Boies, Emiles | QUE_CAP | Slider | 70 | 54.5 | 0.245 | 5.0 | -0.1 | 2125 | 80.5 | 5.95 | Tight High-Spin Breakers |
| 98 | Odonnell, Brendan | NEW_ENG23 | Slider | 161 | 54.4 | 0.224 | -1.6 | 12.4 | 2658 | 84.3 | 6.11 | Tight High-Spin Breakers |
| 99 | Pierson, Kenny | LAK_ERI24 | Sinker | 192 | 54.3 | 0.227 | 0.6 | -17.2 | 1770 | 81.1 | 4.81 | Tight High-Spin Breakers |
| 100 | Moore, Kyle | SCH_BOO | Cutter | 106 | 54.2 | 0.241 | 9.6 | 1.4 | 2144 | 84.6 | 4.74 | Tight High-Spin Breakers |
| 101 | Pardinho, Eric | OTT_TIT | Slider | 123 | 54.1 | 0.226 | 5.6 | 2.0 | 2352 | 86.7 | 5.76 | Tight High-Spin Breakers |
| 102 | Hill, Kaleb | OTT_TIT | Slider | 137 | 54.0 | 0.240 | 0.8 | 9.0 | 2252 | 79.0 | 5.24 | Tight High-Spin Breakers |
| 103 | Allemann, Braeden | QUE_CAP | Curveball | 215 | 53.8 | 0.242 | -7.1 | -15.9 | 2192 | 76.8 | 6.11 | Tight High-Spin Breakers |
| 104 | Cerda, Junior | EVA_OTT | Slider | 60 | 53.8 | 0.219 | -1.8 | -8.3 | 2587 | 81.2 | 4.90 | Tight High-Spin Breakers |
| 105 | Smith, Jackson | MIS_MUD | Cutter | 92 | 53.7 | 0.221 | 3.3 | 5.0 | 2424 | 81.6 | 5.07 | Tight High-Spin Breakers |
| 106 | Thompson, Ross | SCH_BOO | Slider | 207 | 53.6 | 0.231 | 3.6 | -2.4 | 2054 | 79.8 | 5.25 | Tight High-Spin Breakers |
| 107 | Noriega, Branden | LAK_ERI24 | Curveball | 115 | 53.4 | 0.258 | -9.7 | 7.8 | 2843 | 79.3 | 5.24 | Tight High-Spin Breakers |
| 108 | Oe, Ryoya | OTT_TIT | Curveball | 57 | 53.2 | 0.211 | -4.6 | 5.0 | 2303 | 73.3 | 4.90 | Tight High-Spin Breakers |
| 109 | Zeplin, Blane | JOL_SLA | Slider | 84 | 52.7 | 0.204 | -0.7 | -6.4 | 2277 | 77.8 | 5.37 | Tight High-Spin Breakers |
| 110 | Sanchez, Edwin | LAK_ERI24 | Curveball | 77 | 52.6 | 0.230 | -5.4 | 6.3 | 2464 | 75.4 | 5.34 | Tight High-Spin Breakers |
| 111 | Floyd, Conner | QUE_CAP | Curveball | 54 | 52.4 | 0.231 | -2.6 | -17.3 | 2111 | 77.3 | 5.03 | Tight High-Spin Breakers |
| 112 | Cooper, Garrett | NEW_YOR13 | Curveball | 123 | 52.4 | 0.221 | -5.1 | -6.4 | 2185 | 76.7 | 5.63 | Tight High-Spin Breakers |
| 113 | Henderson, Drew | DOW_EAS1 | Curveball | 235 | 52.0 | 0.232 | -8.2 | -5.1 | 2308 | 76.8 | 5.15 | Tight High-Spin Breakers |
| 114 | Gamelin, Shaun | JOL_SLA | Slider | 64 | 52.0 | 0.238 | 2.2 | -1.4 | 2287 | 81.5 | 4.81 | Tight High-Spin Breakers |
| 115 | Sanchez, Edwin | LAK_ERI24 | Slider | 59 | 51.9 | 0.245 | -0.9 | 3.7 | 2399 | 76.6 | 5.13 | Tight High-Spin Breakers |
| 116 | Sakurai, Masatoshi | QUE_CAP | Slider | 119 | 51.8 | 0.245 | -0.7 | 4.5 | 2281 | 79.0 | 5.78 | Tight High-Spin Breakers |
| 117 | Perez, Kelvin | WAS_WIL3 | Slider | 106 | 51.8 | 0.226 | 4.1 | -4.6 | 2243 | 81.5 | 5.80 | Tight High-Spin Breakers |
| 118 | Puccetti, Dominic | OTT_TIT | Curveball | 172 | 51.7 | 0.249 | -13.5 | 9.8 | 2684 | 73.7 | 5.27 | Tight High-Spin Breakers |
| 119 | Joven, Art | MIS_MUD | Slider | 258 | 51.6 | 0.242 | 2.1 | -0.1 | 2235 | 77.5 | 5.16 | Tight High-Spin Breakers |
| 120 | Moore, Kyle | SCH_BOO | Curveball | 101 | 51.6 | 0.253 | -8.8 | -8.3 | 2536 | 76.8 | 4.13 | Tight High-Spin Breakers |
| 121 | Bauer, Patrick | QUE_CAP | Curveball | 56 | 51.4 | 0.250 | -12.8 | -14.4 | 2212 | 69.2 | 6.05 | Tight High-Spin Breakers |
| 122 | McCartney, Seth | MIS_MUD | Slider | 57 | 51.4 | 0.199 | 4.2 | -3.0 | 2474 | 81.9 | 5.45 | Tight High-Spin Breakers |
| 123 | Serrano, Elio | NEW_JER6 | Curveball | 64 | 51.4 | 0.281 | -10.4 | -14.0 | 2302 | 75.8 | 5.10 | Tight High-Spin Breakers |
| 124 | Willeman, Landon | EVA_OTT | Curveball | 104 | 51.4 | 0.260 | -7.8 | -9.8 | 2121 | 77.8 | 5.37 | Tight High-Spin Breakers |
| 125 | Blair, Davis | DOW_EAS1 | Slider | 99 | 50.9 | 0.262 | 3.6 | -5.9 | 2146 | 81.9 | 5.11 | Tight High-Spin Breakers |
| 126 | Smith, Ben | NEW_ENG23 | Slider | 87 | 50.6 | 0.287 | 0.1 | 13.7 | 2329 | 78.5 | 5.47 | Tight High-Spin Breakers |
| 127 | Morgan, Marcus | JOL_SLA | Slider | 53 | 50.6 | 0.237 | 7.5 | -10.1 | 2872 | 84.7 | 5.73 | Tight High-Spin Breakers |
| 128 | Langrell, Connor | MIS_MUD | Curveball | 95 | 50.5 | 0.260 | -15.3 | -11.9 | 2692 | 77.5 | 5.99 | Tight High-Spin Breakers |
| 129 | Wehrle, Tyler | WIN_CIT29 | Slider | 146 | 50.2 | 0.233 | 2.4 | -10.0 | 2521 | 80.7 | 5.33 | Tight High-Spin Breakers |
| 130 | Linderman, Greyson | JOL_SLA | Slider | 66 | 50.1 | 0.273 | -4.0 | -13.7 | 2207 | 81.2 | 4.96 | Tight High-Spin Breakers |
| 131 | Campbell, AJ | WIN_CIT29 | Slider | 281 | 49.9 | 0.238 | 4.8 | -11.0 | 2572 | 79.7 | 4.81 | Tight High-Spin Breakers |
| 132 | Belton, Hunter | MIS_MUD | Slider | 99 | 49.7 | 0.248 | 6.5 | -2.6 | 2108 | 78.5 | 5.82 | Tight High-Spin Breakers |
| 133 | Campbell, Tyler | MIS_MUD | Slider | 169 | 49.7 | 0.274 | 8.6 | 3.8 | 2220 | 74.5 | 5.74 | Tight High-Spin Breakers |
| 134 | Pierson, Kenny | LAK_ERI24 | Changeup | 220 | 49.3 | 0.248 | -1.2 | -16.3 | 1762 | 77.0 | 4.99 | Tight High-Spin Breakers |
| 135 | Williams, Brian | MIS_MUD | Slider | 187 | 49.2 | 0.257 | 4.3 | -0.8 | 2154 | 81.3 | 5.92 | Tight High-Spin Breakers |
| 136 | Sparks, Alec | GAT_GRI | Slider | 131 | 49.2 | 0.250 | 0.2 | -7.3 | 2606 | 79.9 | 5.48 | Tight High-Spin Breakers |
| 137 | Foster, Kobe | WAS_WIL3 | Curveball | 133 | 49.2 | 0.255 | -8.0 | 15.1 | 2232 | 67.6 | 5.46 | Tight High-Spin Breakers |
| 138 | Catrambone, Ben | JOL_SLA | Cutter | 56 | 49.0 | 0.290 | 5.9 | -0.4 | 2373 | 83.2 | 5.27 | Tight High-Spin Breakers |
| 139 | Scafidi, Christian | LAK_ERI24 | Slider | 167 | 48.9 | 0.239 | 4.1 | -2.1 | 2383 | 84.1 | 5.65 | Tight High-Spin Breakers |
| 140 | Willeman, Landon | EVA_OTT | Slider | 85 | 48.8 | 0.226 | 0.2 | -5.3 | 2241 | 80.6 | 5.52 | Tight High-Spin Breakers |
| 141 | Helt, Robert | LAK_ERI24 | Curveball | 130 | 48.7 | 0.268 | -6.0 | -6.1 | 2389 | 78.7 | 5.77 | Tight High-Spin Breakers |
| 142 | Gamelin, Shaun | JOL_SLA | Cutter | 137 | 48.5 | 0.246 | 5.6 | -0.4 | 2316 | 84.0 | 5.06 | Tight High-Spin Breakers |
| 143 | Hicks, Jackson | DOW_EAS1 | Slider | 116 | 48.1 | 0.272 | 2.4 | -1.0 | 2195 | 80.0 | 5.23 | Tight High-Spin Breakers |
| 144 | Parks, Pavin | LAK_ERI24 | Cutter | 135 | 48.0 | 0.256 | 7.0 | -3.6 | 2428 | 84.7 | 5.77 | Tight High-Spin Breakers |
| 145 | Kaminer, Brandon | DOW_EAS1 | Slider | 133 | 48.0 | 0.239 | 6.1 | 2.3 | 2474 | 83.8 | 5.28 | Tight High-Spin Breakers |
| 146 | Rodriguez, Luis | TRO_AIG | Slider | 54 | 47.9 | 0.243 | 2.2 | -1.5 | 2536 | 87.7 | 5.94 | Tight High-Spin Breakers |
| 147 | Simpson, Garret | EVA_OTT | Cutter | 75 | 47.9 | 0.275 | 1.3 | -1.3 | 2506 | 84.0 | 5.30 | Tight High-Spin Breakers |
| 148 | Good, Ty | GAT_GRI | Curveball | 139 | 47.8 | 0.251 | -7.7 | -4.6 | 2134 | 75.0 | 5.65 | Tight High-Spin Breakers |
| 149 | Smith, Ethan | WIN_CIT29 | Slider | 58 | 47.8 | 0.283 | -0.2 | -6.4 | 2423 | 80.6 | 5.91 | Tight High-Spin Breakers |
| 150 | Castro, Alexander | TRO_AIG | Slider | 101 | 47.6 | 0.271 | 0.7 | -4.9 | 2498 | 83.5 | 4.81 | Tight High-Spin Breakers |
| 151 | Kaftan, Eddie | FLO_Y'A | Slider | 62 | 47.6 | 0.236 | 1.1 | -6.3 | 2437 | 77.1 | 4.72 | Tight High-Spin Breakers |
| 152 | Baker, Luke | EVA_OTT | Curveball | 59 | 47.5 | 0.248 | -7.4 | 9.7 | 2694 | 75.5 | 5.51 | Tight High-Spin Breakers |
| 153 | Barker, Alex | NEW_YOR13 | Curveball | 83 | 47.4 | 0.244 | -5.5 | 10.3 | 2251 | 76.2 | 5.78 | Tight High-Spin Breakers |
| 154 | Pierson, Kenny | LAK_ERI24 | Slider | 82 | 47.3 | 0.284 | -1.6 | 7.0 | 2095 | 72.6 | 4.64 | Tight High-Spin Breakers |
| 155 | Milburn, Isaac | FLO_Y'A | Curveball | 151 | 47.3 | 0.308 | -9.4 | 13.7 | 2579 | 76.6 | 4.96 | Tight High-Spin Breakers |
| 156 | Perdomo, Rafael | QUE_CAP | Slider | 84 | 47.2 | 0.265 | 3.1 | 0.8 | 2184 | 82.9 | 5.80 | Tight High-Spin Breakers |
| 157 | Foy, Corbin | LAK_ERI24 | Slider | 78 | 46.9 | 0.272 | -1.1 | -7.6 | 2653 | 82.4 | 5.56 | Tight High-Spin Breakers |
| 158 | Sittinger, Brandyn | LAK_ERI24 | Slider | 109 | 46.8 | 0.253 | 3.4 | -1.2 | 2479 | 87.7 | 5.72 | Tight High-Spin Breakers |
| 159 | Debban, Caleb | NEW_JER6 | Curveball | 182 | 46.5 | 0.281 | -7.2 | 18.5 | 2802 | 76.9 | 5.97 | Tight High-Spin Breakers |
| 160 | Parra, Andres | LAK_ERI24 | Slider | 161 | 46.5 | 0.268 | 2.8 | 2.0 | 2288 | 79.6 | 5.71 | Tight High-Spin Breakers |
| 161 | Valdez, Alex | EVA_OTT | Slider | 116 | 46.2 | 0.235 | 3.5 | -2.6 | 2179 | 85.8 | 5.32 | Tight High-Spin Breakers |
| 162 | Ginn, Landon | WAS_WIL3 | Cutter | 98 | 45.6 | 0.248 | 3.3 | -1.9 | 2836 | 86.2 | 5.41 | Tight High-Spin Breakers |
| 163 | Andueza, Axel | DOW_EAS1 | Curveball | 134 | 44.9 | 0.252 | -3.4 | -3.3 | 2193 | 79.3 | 5.09 | Tight High-Spin Breakers |
| 164 | Smith, Jackson | MIS_MUD | Sinker | 427 | 44.8 | 0.275 | 0.9 | 21.8 | 2411 | 85.3 | 5.12 | Tight High-Spin Breakers |
| 165 | Peyton, Blake | GAT_GRI | Curveball | 87 | 44.6 | 0.228 | -5.5 | 8.6 | 2676 | 77.9 | 5.24 | Tight High-Spin Breakers |
| 166 | Turner, Eric | JOL_SLA | Slider | 160 | 44.5 | 0.263 | 1.3 | -7.6 | 2351 | 78.3 | 5.00 | Tight High-Spin Breakers |
| 167 | Huter, Blayne | SUS_COU1 | Curveball | 103 | 44.4 | 0.275 | -5.1 | -14.2 | 2137 | 73.7 | 6.01 | Tight High-Spin Breakers |
| 168 | Estrella, Noah | TRI_VAL | Slider | 107 | 44.3 | 0.228 | -2.2 | 0.6 | 2581 | 85.3 | 5.65 | Tight High-Spin Breakers |
| 169 | Figueredo, Kevin | WIN_CIT29 | Curveball | 78 | 44.1 | 0.281 | -3.5 | 4.9 | 2324 | 75.8 | 5.00 | Tight High-Spin Breakers |
| 170 | Forsyth, Braden | MIS_MUD | Slider | 143 | 44.0 | 0.281 | 3.4 | -6.8 | 2362 | 80.5 | 6.06 | Tight High-Spin Breakers |
| 171 | Barker, Alex | NEW_YOR13 | Slider | 112 | 43.9 | 0.271 | 3.2 | 4.4 | 2210 | 81.4 | 6.01 | Tight High-Spin Breakers |
| 172 | Serrano, Elio | NEW_JER6 | Slider | 96 | 43.7 | 0.262 | 5.5 | -2.3 | 2243 | 82.9 | 5.34 | Tight High-Spin Breakers |
| 173 | Misla, Luis | TRI_VAL | Curveball | 120 | 43.7 | 0.260 | -6.0 | 9.5 | 2802 | 76.8 | 5.14 | Tight High-Spin Breakers |
| 174 | Encarnacion, J.D. | EVA_OTT | Slider | 143 | 43.5 | 0.255 | 2.5 | -5.4 | 2352 | 81.2 | 5.43 | Tight High-Spin Breakers |
| 175 | Bradford, Ethan | NEW_YOR13 | Slider | 115 | 43.4 | 0.296 | -1.0 | 6.3 | 2418 | 81.8 | 5.42 | Tight High-Spin Breakers |
| 176 | Smith, Donny | JOL_SLA | Slider | 66 | 43.4 | 0.250 | -2.4 | -5.4 | 2476 | 78.5 | 5.16 | Tight High-Spin Breakers |
| 177 | Lovin, Xander | GAT_GRI | Slider | 114 | 43.4 | 0.283 | 2.7 | -3.9 | 2444 | 85.0 | 4.99 | Tight High-Spin Breakers |
| 178 | Godwin, Connor | NEW_YOR13 | Slider | 93 | 43.3 | 0.264 | 0.0 | -10.2 | 2535 | 82.4 | 6.11 | Tight High-Spin Breakers |
| 179 | Salata, Derek | SCH_BOO | Slider | 156 | 43.3 | 0.278 | 3.2 | -9.5 | 2556 | 81.2 | 5.54 | Tight High-Spin Breakers |
| 180 | Burcham, Jacob | GAT_GRI | Slider | 98 | 43.2 | 0.240 | 0.4 | -9.4 | 2375 | 80.8 | 5.89 | Tight High-Spin Breakers |
| 181 | Martzolf, Max | OTT_TIT | Curveball | 71 | 43.1 | 0.294 | -4.2 | 11.1 | 2155 | 73.9 | 5.43 | Tight High-Spin Breakers |
| 182 | Cook, Cole | SCH_BOO | Cutter | 98 | 42.4 | 0.223 | 9.2 | -3.4 | 2417 | 82.4 | 5.28 | Tight High-Spin Breakers |
| 183 | Bihm, Gage | MIS_MUD | Slider | 58 | 42.3 | 0.313 | -2.2 | 10.7 | 2332 | 80.6 | 5.03 | Tight High-Spin Breakers |
| 184 | Hocom, Quinn | TRI_VAL | Curveball | 79 | 41.9 | 0.286 | -13.5 | -11.9 | 2377 | 76.9 | 5.52 | Tight High-Spin Breakers |
| 185 | Galva, Claudio | GAT_GRI | Slider | 151 | 41.6 | 0.268 | 2.9 | -0.6 | 2233 | 83.6 | 4.84 | Tight High-Spin Breakers |
| 186 | Bice, Emmett | NEW_YOR13 | Curveball | 140 | 41.6 | 0.305 | -10.3 | -13.4 | 2985 | 79.0 | 5.54 | Tight High-Spin Breakers |
| 187 | Gorgen, Grady | NEW_YOR13 | Curveball | 61 | 40.9 | 0.277 | -6.3 | 6.6 | 2078 | 79.8 | 5.70 | Tight High-Spin Breakers |
| 188 | Gollert, Harley | TRO_AIG | Slider | 58 | 40.9 | 0.279 | -2.1 | 7.8 | 2219 | 78.3 | 4.92 | Tight High-Spin Breakers |
| 189 | Sakurai, Masatoshi | QUE_CAP | Curveball | 126 | 40.6 | 0.294 | -4.3 | 5.3 | 2460 | 78.4 | 5.61 | Tight High-Spin Breakers |
| 190 | Shinn, Nathan | LAK_ERI24 | Curveball | 88 | 40.5 | 0.282 | -5.9 | 0.6 | 2113 | 79.6 | 5.29 | Tight High-Spin Breakers |
| 191 | Sanchez, Dikember | LAK_ERI24 | Slider | 111 | 40.4 | 0.278 | 2.1 | -3.7 | 2555 | 85.9 | 5.32 | Tight High-Spin Breakers |
| 192 | Sabatine, Gino | TRI_VAL | Slider | 138 | 40.4 | 0.294 | 4.2 | -3.6 | 2322 | 79.9 | 4.89 | Tight High-Spin Breakers |
| 193 | Parsons, Billy | SUS_COU1 | Slider | 241 | 40.3 | 0.253 | 5.9 | -6.3 | 2486 | 82.9 | 5.45 | Tight High-Spin Breakers |
| 194 | Andueza, Axel | DOW_EAS1 | Slider | 97 | 40.2 | 0.285 | -0.4 | -1.4 | 2073 | 80.9 | 5.25 | Tight High-Spin Breakers |
| 195 | Kassebaum, Torin | LON_ISL22 | Curveball | 55 | 39.9 | 0.309 | 1.1 | 10.2 | 2155 | 71.6 | 5.31 | Tight High-Spin Breakers |
| 196 | Delaney, Carter | WIN_CIT29 | Curveball | 55 | 39.5 | 0.294 | -5.6 | -8.3 | 2325 | 79.8 | 5.56 | Tight High-Spin Breakers |
| 197 | Fauci, Sonny | NEW_JER6 | Curveball | 69 | 38.8 | 0.349 | -14.7 | -6.8 | 2298 | 78.6 | 5.94 | Tight High-Spin Breakers |
| 198 | Correa, Nelvin | QUE_CAP | Slider | 96 | 38.7 | 0.263 | 4.6 | -7.3 | 2403 | 83.2 | 5.50 | Tight High-Spin Breakers |
| 199 | Hampton, Ky | OTT_TIT | Slider | 88 | 38.4 | 0.281 | 1.8 | -4.3 | 2297 | 83.6 | 5.91 | Tight High-Spin Breakers |
| 200 | Pindel, Buddie | SCH_BOO | Slider | 144 | 38.4 | 0.289 | 2.2 | -6.9 | 2473 | 81.8 | 5.35 | Tight High-Spin Breakers |
| 201 | Williams, Pierce | NEW_ENG23 | Curveball | 135 | 38.1 | 0.282 | -5.9 | 6.6 | 2173 | 75.5 | 5.76 | Tight High-Spin Breakers |
| 202 | Thornton, Tyler | NEW_ENG23 | Slider | 92 | 38.1 | 0.307 | 1.5 | 0.0 | 1930 | 79.5 | 4.84 | Tight High-Spin Breakers |
| 203 | Soto, Carlos | JOL_SLA | Slider | 67 | 36.4 | 0.289 | -1.4 | -8.2 | 2487 | 78.4 | 5.15 | Tight High-Spin Breakers |
| 204 | Villalobos, Jonaiker | FLO_Y'A | Curveball | 103 | 36.3 | 0.286 | -5.2 | 5.6 | 2260 | 74.5 | 5.33 | Tight High-Spin Breakers |
| 205 | Eldred, Zach | NEW_ENG23 | Curveball | 73 | 35.3 | 0.329 | -9.8 | -12.5 | 2484 | 78.0 | 5.87 | Tight High-Spin Breakers |
| 206 | Miranda, Kevin | OTT_TIT | Slider | 64 | 35.1 | 0.340 | 4.1 | -0.1 | 2229 | 81.1 | 5.62 | Tight High-Spin Breakers |
| 207 | Tiburcio, David | DOW_EAS1 | Slider | 80 | 34.7 | 0.311 | 6.3 | 0.9 | 2354 | 86.2 | 5.41 | Tight High-Spin Breakers |
| 208 | Eldred, Zach | NEW_ENG23 | Slider | 148 | 33.4 | 0.309 | 1.9 | -7.4 | 2398 | 82.3 | 5.81 | Tight High-Spin Breakers |
| 209 | Gorgen, Grady | NEW_YOR13 | Slider | 107 | 32.9 | 0.313 | 1.9 | 0.5 | 2137 | 83.1 | 5.97 | Tight High-Spin Breakers |
| 210 | Catrambone, Ben | JOL_SLA | Slider | 79 | 30.2 | 0.336 | 1.0 | -2.1 | 2280 | 82.3 | 4.82 | Tight High-Spin Breakers |
| 211 | Vitas, Ben | JOL_SLA | Slider | 119 | 28.2 | 0.316 | 1.5 | -4.6 | 2123 | 81.2 | 4.95 | Tight High-Spin Breakers |
| 212 | Lovin, Xander | GAT_GRI | Curveball | 55 | 27.8 | 0.332 | -9.6 | -12.6 | 2634 | 77.0 | 4.70 | Tight High-Spin Breakers |
| 213 | Delaney, Carter | WIN_CIT29 | Slider | 62 | 27.2 | 0.354 | -0.4 | -7.9 | 2332 | 79.8 | 5.44 | Tight High-Spin Breakers |
| 214 | Cameron, Wyatt | SCH_BOO | Curveball | 109 | 27.0 | 0.362 | -13.5 | -9.7 | 2296 | 81.1 | 5.24 | Tight High-Spin Breakers |
| 215 | Johnston, Spencer | DOW_EAS1 | Curveball | 66 | 25.6 | 0.324 | -4.7 | -6.0 | 2133 | 74.4 | 5.68 | Tight High-Spin Breakers |
| 216 | Westcott, Zac | FLO_Y'A | Curveball | 163 | 21.1 | 0.379 | -15.2 | -9.2 | 1872 | 67.1 | 5.48 | Tight High-Spin Breakers |
| 217 | Lawson, Nathan | FLO_Y'A | Changeup | 51 | 77.0 | 0.168 | 8.0 | 10.8 | 1438 | 79.8 | 5.78 | Soft-Speed Separation |
| 218 | Rodriguez, Joe Joe | NEW_JER6 | Changeup | 82 | 74.8 | 0.120 | 8.7 | 15.3 | 1799 | 81.4 | 5.41 | Soft-Speed Separation |
| 219 | Serrano, Elio | NEW_JER6 | Changeup | 55 | 74.3 | 0.162 | 10.8 | 11.9 | 1834 | 82.2 | 5.93 | Soft-Speed Separation |
| 220 | Garcia, Hector | WAS_WIL3 | Splitter | 62 | 72.7 | 0.187 | 11.7 | 7.6 | 1216 | 78.2 | 5.92 | Soft-Speed Separation |
| 221 | Escobar, Anthony | TRO_AIG | Changeup | 104 | 72.0 | 0.150 | 10.2 | 11.6 | 1617 | 79.6 | 6.22 | Soft-Speed Separation |
| 222 | McEvoy, Aidan | FLO_Y'A | Slider | 100 | 71.7 | 0.146 | 6.6 | 10.0 | 2213 | 78.8 | 6.04 | Soft-Speed Separation |
| 223 | Sesar, Jorden | SUS_COU1 | Changeup | 64 | 69.1 | 0.150 | 12.2 | 11.2 | 1954 | 82.9 | 6.41 | Soft-Speed Separation |
| 224 | Harris, Everette | TRI_VAL | Changeup | 96 | 69.0 | 0.171 | 2.1 | 16.6 | 2144 | 82.6 | 6.54 | Soft-Speed Separation |
| 225 | Sechrist, Zander | WAS_WIL3 | Slider | 60 | 68.5 | 0.183 | 1.3 | 9.7 | 1831 | 68.3 | 5.12 | Soft-Speed Separation |
| 226 | Parsons, Billy | SUS_COU1 | Changeup | 61 | 67.8 | 0.235 | 1.7 | 7.8 | 1428 | 80.9 | 5.49 | Soft-Speed Separation |
| 227 | Sechrist, Zander | WAS_WIL3 | Curveball | 70 | 67.7 | 0.187 | -0.7 | 9.6 | 1804 | 66.6 | 4.94 | Soft-Speed Separation |
| 228 | Vitas, Ben | JOL_SLA | Splitter | 98 | 67.3 | 0.198 | 1.3 | 7.3 | 1028 | 81.5 | 5.01 | Soft-Speed Separation |
| 229 | Shears, Tanner | SCH_BOO | Splitter | 65 | 67.2 | 0.190 | -1.0 | 7.3 | 903 | 82.0 | 5.08 | Soft-Speed Separation |
| 230 | Tokar, Heitor | OTT_TIT | Changeup | 63 | 66.7 | 0.189 | 9.6 | 13.1 | 1387 | 82.0 | 6.07 | Soft-Speed Separation |
| 231 | Hocom, Quinn | TRI_VAL | Changeup | 73 | 66.0 | 0.186 | 6.4 | 17.5 | 1996 | 78.1 | 5.66 | Soft-Speed Separation |
| 232 | Drakeford, Dosie | NEW_JER6 | Changeup | 71 | 66.0 | 0.143 | 10.0 | 14.7 | 1852 | 81.5 | 6.14 | Soft-Speed Separation |
| 233 | Villers, Ian | QUE_CAP | Splitter | 64 | 64.6 | 0.221 | 7.5 | 11.5 | 1086 | 83.1 | 5.98 | Soft-Speed Separation |
| 234 | Pindel, Buddie | SCH_BOO | Splitter | 82 | 64.0 | 0.225 | 4.7 | 7.3 | 1101 | 80.3 | 5.78 | Soft-Speed Separation |
| 235 | Cooper, Garrett | NEW_YOR13 | Changeup | 198 | 63.8 | 0.202 | 8.4 | 7.4 | 1395 | 77.5 | 6.44 | Soft-Speed Separation |
| 236 | Maietta, Dante | WIN_CIT29 | Changeup | 191 | 63.8 | 0.180 | 15.6 | 13.8 | 1859 | 78.0 | 6.29 | Soft-Speed Separation |
| 237 | Wiltse, Ryan | EVA_OTT | Changeup | 120 | 63.7 | 0.204 | 14.1 | 10.4 | 1844 | 78.6 | 6.38 | Soft-Speed Separation |
| 238 | Leak, Anthony | NEW_YOR13 | Changeup | 60 | 62.9 | 0.203 | 5.7 | 10.6 | 1718 | 82.9 | 6.55 | Soft-Speed Separation |
| 239 | MacMillan, Blake | TRO_AIG | Slider | 96 | 61.7 | 0.229 | 5.8 | -0.0 | 1921 | 79.5 | 5.30 | Soft-Speed Separation |
| 240 | Thornton, Tyler | NEW_ENG23 | Splitter | 88 | 61.4 | 0.217 | 4.6 | 11.6 | 963 | 77.5 | 4.86 | Soft-Speed Separation |
| 241 | Willeman, Landon | EVA_OTT | Changeup | 154 | 61.0 | 0.200 | 6.5 | 14.3 | 1706 | 84.2 | 6.26 | Soft-Speed Separation |
| 242 | Thompson, Ross | SCH_BOO | Splitter | 132 | 59.9 | 0.206 | 4.1 | 9.4 | 1052 | 79.4 | 5.43 | Soft-Speed Separation |
| 243 | Henderson, Drew | DOW_EAS1 | Changeup | 126 | 59.1 | 0.212 | 9.3 | 13.8 | 1657 | 81.6 | 5.86 | Soft-Speed Separation |
| 244 | Sabatine, Gino | TRI_VAL | Sinker | 54 | 59.1 | 0.195 | 9.5 | 14.0 | 1890 | 88.2 | 5.03 | Soft-Speed Separation |
| 245 | Webster, Evan | FLO_Y'A | Slider | 110 | 58.8 | 0.203 | 3.0 | 0.9 | 1960 | 81.4 | 6.82 | Soft-Speed Separation |
| 246 | VanMarter, Luke | LEM_COL | Changeup | 53 | 58.6 | 0.260 | 12.9 | 11.7 | 1756 | 77.6 | 6.55 | Soft-Speed Separation |
| 247 | Boies, Emiles | QUE_CAP | Changeup | 168 | 57.7 | 0.203 | 11.7 | 15.0 | 1913 | 82.5 | 6.28 | Soft-Speed Separation |
| 248 | Dima, Josh | GAT_GRI | Slider | 114 | 56.9 | 0.212 | 2.4 | 2.1 | 1924 | 81.9 | 6.01 | Soft-Speed Separation |
| 249 | Gollert, Harley | TRO_AIG | Changeup | 121 | 56.1 | 0.240 | 9.7 | -14.1 | 1568 | 79.7 | 5.27 | Soft-Speed Separation |
| 250 | Cameron, Zach | WIN_CIT29 | Changeup | 178 | 56.0 | 0.227 | 7.4 | 21.1 | 2119 | 80.3 | 5.55 | Soft-Speed Separation |
| 251 | Williams, Brian | MIS_MUD | Splitter | 86 | 55.7 | 0.202 | 2.3 | 5.3 | 1674 | 78.8 | 6.08 | Soft-Speed Separation |
| 252 | Whitesell, Max | FLO_Y'A | Changeup | 55 | 55.6 | 0.255 | 9.3 | 10.7 | 1655 | 85.2 | 6.44 | Soft-Speed Separation |
| 253 | Brothers, Kellen | SUS_COU1 | Changeup | 131 | 55.5 | 0.237 | 10.5 | 12.4 | 1501 | 79.9 | 6.05 | Soft-Speed Separation |
| 254 | Vail, Tyler | NEW_YOR13 | Changeup | 184 | 55.4 | 0.249 | 7.0 | 12.5 | 1803 | 82.6 | 6.27 | Soft-Speed Separation |
| 255 | Dill, Austin | TRI_VAL | Changeup | 184 | 55.2 | 0.221 | 10.7 | 16.9 | 1930 | 80.4 | 5.24 | Soft-Speed Separation |
| 256 | Pardinho, Eric | OTT_TIT | Changeup | 98 | 54.9 | 0.233 | 4.8 | 15.3 | 1614 | 84.2 | 5.40 | Soft-Speed Separation |
| 257 | Miner, Jace | DOW_EAS1 | Curveball | 60 | 54.6 | 0.281 | 2.8 | 10.8 | 1854 | 76.2 | 5.47 | Soft-Speed Separation |
| 258 | Morel, Yohanse | OTT_TIT | Changeup | 83 | 54.4 | 0.229 | 5.2 | 17.4 | 2095 | 85.2 | 5.39 | Soft-Speed Separation |
| 259 | Roland, Cole | QUE_CAP | Changeup | 71 | 53.7 | 0.247 | 10.4 | 9.6 | 2033 | 82.6 | 5.56 | Soft-Speed Separation |
| 260 | DeCastro, Justin | LON_ISL22 | Changeup | 122 | 53.5 | 0.238 | 9.6 | 18.6 | 1979 | 79.4 | 5.06 | Soft-Speed Separation |
| 261 | Andueza, Axel | DOW_EAS1 | Changeup | 80 | 53.5 | 0.238 | 5.9 | 10.9 | 2039 | 82.8 | 5.26 | Soft-Speed Separation |
| 262 | Galva, Claudio | GAT_GRI | Changeup | 73 | 53.4 | 0.237 | 4.2 | -13.1 | 1497 | 84.0 | 4.90 | Soft-Speed Separation |
| 263 | Salata, Derek | SCH_BOO | Splitter | 90 | 53.4 | 0.211 | 7.2 | 9.3 | 1137 | 83.2 | 5.80 | Soft-Speed Separation |
| 264 | Long, Jalon | NEW_YOR13 | Changeup | 96 | 53.2 | 0.242 | 6.1 | 14.2 | 1531 | 82.2 | 6.16 | Soft-Speed Separation |
| 265 | Johnston, Spencer | DOW_EAS1 | Slider | 190 | 53.2 | 0.216 | 6.7 | 0.9 | 2083 | 78.4 | 5.96 | Soft-Speed Separation |
| 266 | Campbell, AJ | WIN_CIT29 | Changeup | 62 | 52.9 | 0.221 | 7.0 | 9.4 | 2076 | 80.5 | 5.32 | Soft-Speed Separation |
| 267 | Daly, Ryan | JOL_SLA | Changeup | 180 | 52.7 | 0.247 | 5.2 | 16.1 | 2080 | 78.9 | 6.89 | Soft-Speed Separation |
| 268 | Hopewell, Chase | FLO_Y'A | Slider | 124 | 52.4 | 0.259 | 0.3 | -2.0 | 1929 | 81.2 | 6.14 | Soft-Speed Separation |
| 269 | Toribio, Noe | TRO_AIG | Changeup | 197 | 52.1 | 0.263 | 6.4 | 16.5 | 1999 | 83.2 | 5.62 | Soft-Speed Separation |
| 270 | Kirby, Zach | WAS_WIL3 | Changeup | 122 | 51.3 | 0.229 | 9.9 | 15.4 | 1690 | 79.8 | 6.07 | Soft-Speed Separation |
| 271 | Sakurai, Masatoshi | QUE_CAP | Changeup | 131 | 51.2 | 0.263 | 8.5 | -5.7 | 1438 | 80.4 | 5.98 | Soft-Speed Separation |
| 272 | Heredia-Bustos, Rolando | DOW_EAS1 | Changeup | 253 | 50.7 | 0.263 | 9.1 | 17.6 | 2058 | 79.4 | 5.68 | Soft-Speed Separation |
| 273 | Miranda, Kevin | OTT_TIT | Changeup | 118 | 50.6 | 0.243 | 8.9 | 12.9 | 1433 | 79.5 | 6.10 | Soft-Speed Separation |
| 274 | Marynczak, Arlo | TRI_VAL | Changeup | 95 | 50.5 | 0.258 | 7.9 | 12.2 | 1681 | 81.4 | 6.21 | Soft-Speed Separation |
| 275 | Primeaux, Parker | SUS_COU1 | Changeup | 101 | 50.3 | 0.251 | 0.8 | 17.7 | 2014 | 85.9 | 5.56 | Soft-Speed Separation |
| 276 | Garcia, Jorge | SUS_COU1 | Changeup | 51 | 50.1 | 0.234 | 12.6 | 9.6 | 1512 | 81.8 | 5.95 | Soft-Speed Separation |
| 277 | Johnston, Spencer | DOW_EAS1 | Changeup | 299 | 50.0 | 0.244 | 8.7 | 10.0 | 1618 | 77.6 | 5.93 | Soft-Speed Separation |
| 278 | Traver, Eliott | LAK_ERI24 | Sinker | 65 | 49.4 | 0.206 | 8.8 | 16.7 | 2147 | 80.7 | 5.77 | Soft-Speed Separation |
| 279 | Maher, Adam | TRI_VAL | Slider | 89 | 49.3 | 0.257 | 4.6 | 1.2 | 1941 | 79.5 | 5.67 | Soft-Speed Separation |
| 280 | Burcham, Jacob | GAT_GRI | Changeup | 79 | 49.1 | 0.233 | 3.8 | 18.1 | 1909 | 83.3 | 6.23 | Soft-Speed Separation |
| 281 | Aldeano, Austin | TRO_AIG | Changeup | 51 | 48.9 | 0.250 | 7.1 | 17.6 | 1856 | 81.3 | 6.28 | Soft-Speed Separation |
| 282 | Hampton, Ky | OTT_TIT | Changeup | 184 | 48.7 | 0.260 | 2.2 | 15.7 | 1702 | 83.9 | 6.12 | Soft-Speed Separation |
| 283 | Vailes, Gage | GAT_GRI | Changeup | 109 | 48.7 | 0.258 | 6.1 | 10.4 | 1890 | 85.0 | 5.28 | Soft-Speed Separation |
| 284 | Simone, Andrew | TRO_AIG | Changeup | 83 | 48.6 | 0.228 | 10.6 | 12.4 | 1691 | 85.4 | 5.97 | Soft-Speed Separation |
| 285 | Moreno, Jose | DOW_EAS1 | Changeup | 75 | 48.4 | 0.244 | 7.1 | 11.1 | 1736 | 81.3 | 5.76 | Soft-Speed Separation |
| 286 | Barreto, Brayhans | TRI_VAL | Slider | 80 | 48.0 | 0.267 | 4.1 | 0.1 | 1918 | 80.9 | 6.17 | Soft-Speed Separation |
| 287 | Delongchamp, Luke | TRI_VAL | Changeup | 222 | 48.0 | 0.257 | 7.8 | 16.4 | 1854 | 82.3 | 5.50 | Soft-Speed Separation |
| 288 | Vega, Lucas | TRO_AIG | Changeup | 60 | 47.5 | 0.325 | 9.0 | 15.0 | 2021 | 83.5 | 6.20 | Soft-Speed Separation |
| 289 | Turner, Eric | JOL_SLA | Changeup | 124 | 47.3 | 0.264 | 4.6 | 15.5 | 1656 | 79.9 | 5.18 | Soft-Speed Separation |
| 290 | Thompson, Ross | SCH_BOO | Changeup | 85 | 47.3 | 0.259 | 5.4 | 9.0 | 1095 | 79.7 | 5.67 | Soft-Speed Separation |
| 291 | Pindel, Buddie | SCH_BOO | Changeup | 108 | 46.3 | 0.262 | 3.6 | 11.7 | 1380 | 80.9 | 5.50 | Soft-Speed Separation |
| 292 | Harris, Ben | GAT_GRI | Changeup | 259 | 46.2 | 0.254 | 8.9 | 16.3 | 1792 | 83.1 | 5.67 | Soft-Speed Separation |
| 293 | Hernandez, Nyan | NEW_JER6 | Changeup | 156 | 45.9 | 0.242 | 12.2 | 15.7 | 1931 | 82.3 | 6.38 | Soft-Speed Separation |
| 294 | Chapple, Bronson | TRO_AIG | Changeup | 51 | 44.7 | 0.286 | 3.7 | 14.5 | 1828 | 83.2 | 6.34 | Soft-Speed Separation |
| 295 | Lefebvre, Charles | TRO_AIG | Changeup | 104 | 44.4 | 0.266 | 5.5 | 14.6 | 1597 | 82.6 | 6.71 | Soft-Speed Separation |
| 296 | Castro, Alexander | TRO_AIG | Changeup | 54 | 44.3 | 0.231 | 5.5 | 10.7 | 1295 | 83.2 | 6.07 | Soft-Speed Separation |
| 297 | Eldred, Zach | NEW_ENG23 | Splitter | 66 | 44.2 | 0.292 | 5.4 | 4.7 | 975 | 84.1 | 6.04 | Soft-Speed Separation |
| 298 | Wehrle, Tyler | WIN_CIT29 | Changeup | 65 | 44.0 | 0.270 | 6.4 | 15.8 | 1898 | 84.2 | 5.56 | Soft-Speed Separation |
| 299 | Scott, Brandon | LAK_ERI24 | Changeup | 217 | 43.8 | 0.281 | 2.0 | -12.4 | 1504 | 81.1 | 5.76 | Soft-Speed Separation |
| 300 | Nakata, Yuto | QUE_CAP | Splitter | 94 | 43.8 | 0.288 | 2.6 | 6.7 | 1001 | 83.8 | 5.52 | Soft-Speed Separation |
| 301 | Gollert, Harley | QUE_CAP | Changeup | 52 | 43.7 | 0.256 | 10.2 | -8.4 | 1676 | 81.0 | 5.46 | Soft-Speed Separation |
| 302 | Okumura, Shuto | WAS_WIL3 | Four-Seam | 60 | 43.6 | 0.277 | 6.1 | 7.6 | 1757 | 75.3 | 5.56 | Soft-Speed Separation |
| 303 | Thebiay, Nolan | EVA_OTT | Changeup | 78 | 43.4 | 0.268 | 5.2 | 16.1 | 1923 | 83.3 | 6.44 | Soft-Speed Separation |
| 304 | Matos, Dwayne | OTT_TIT | Changeup | 218 | 43.3 | 0.254 | 3.5 | 16.0 | 1519 | 83.9 | 6.36 | Soft-Speed Separation |
| 305 | Long, Maddox | WAS_WIL3 | Changeup | 61 | 42.9 | 0.283 | 7.9 | 15.7 | 1932 | 84.2 | 5.97 | Soft-Speed Separation |
| 306 | Moore, Kyle | SCH_BOO | Changeup | 88 | 42.7 | 0.263 | 9.7 | 16.3 | 2040 | 82.8 | 4.70 | Soft-Speed Separation |
| 307 | Westcott, Zac | FLO_Y'A | Changeup | 196 | 42.4 | 0.266 | 6.5 | 16.7 | 1915 | 76.5 | 5.73 | Soft-Speed Separation |
| 308 | Noble, Nick | FDU_KNI | Changeup | 71 | 42.0 | 0.305 | 0.2 | 17.6 | 1612 | 77.3 | 5.00 | Soft-Speed Separation |
| 309 | Primeaux, Parker | SUS_COU1 | Sinker | 58 | 42.0 | 0.271 | 0.4 | 19.2 | 2108 | 88.0 | 5.53 | Soft-Speed Separation |
| 310 | Bell, Brendan | NEW_ENG23 | Changeup | 56 | 42.0 | 0.252 | 7.3 | 15.4 | 1950 | 82.7 | 5.16 | Soft-Speed Separation |
| 311 | Dima, Josh | GAT_GRI | Curveball | 52 | 41.7 | 0.279 | -3.6 | 2.0 | 1960 | 80.3 | 6.00 | Soft-Speed Separation |
| 312 | Kaftan, Eddie | FLO_Y'A | Sinker | 128 | 41.0 | 0.267 | 7.4 | 13.6 | 2035 | 86.0 | 5.43 | Soft-Speed Separation |
| 313 | Trizuto, Colin | WAG_SEA | Changeup | 69 | 40.5 | 0.274 | 7.0 | 18.5 | 1961 | 84.0 | 5.35 | Soft-Speed Separation |
| 314 | Correa, Nelvin | QUE_CAP | Changeup | 56 | 39.6 | 0.276 | 11.0 | 13.8 | 1994 | 84.5 | 6.08 | Soft-Speed Separation |
| 315 | Simpson, Garret | EVA_OTT | Changeup | 75 | 38.8 | 0.322 | 4.4 | 10.3 | 1739 | 83.8 | 5.19 | Soft-Speed Separation |
| 316 | Thornton, Tyler | NEW_ENG23 | Changeup | 113 | 37.3 | 0.281 | 9.3 | 13.9 | 1811 | 83.0 | 4.75 | Soft-Speed Separation |
| 317 | Sabatine, Gino | TRI_VAL | Changeup | 287 | 37.2 | 0.296 | 8.3 | 15.5 | 1784 | 85.1 | 5.07 | Soft-Speed Separation |
| 318 | Sechrist, Zander | WAS_WIL3 | Changeup | 166 | 35.8 | 0.311 | 6.8 | -14.7 | 1631 | 76.2 | 5.72 | Soft-Speed Separation |
| 319 | Belton, Hunter | MIS_MUD | Changeup | 55 | 32.3 | 0.339 | 11.4 | 13.9 | 2006 | 81.0 | 6.10 | Soft-Speed Separation |
| 320 | Duby, Bill | NEW_JER6 | Splitter | 52 | 32.0 | 0.326 | 7.0 | 4.0 | 997 | 78.8 | 6.09 | Soft-Speed Separation |
| 321 | Givens-Craig, Hayden | SUS_COU1 | Changeup | 85 | 31.1 | 0.334 | 7.9 | 11.6 | 1666 | 80.6 | 5.80 | Soft-Speed Separation |
| 322 | Duby, Bill | NEW_JER6 | Changeup | 147 | 30.5 | 0.289 | 11.4 | 13.3 | 1938 | 83.7 | 6.65 | Soft-Speed Separation |
| 323 | Smith, Ethan | WIN_CIT29 | Changeup | 52 | 27.1 | 0.321 | 9.1 | 14.6 | 2000 | 82.7 | 6.38 | Soft-Speed Separation |
| 324 | Thornton, Tyler | NEW_ENG23 | Sinker | 104 | 26.8 | 0.342 | 9.5 | 15.2 | 1950 | 84.4 | 5.54 | Soft-Speed Separation |

## Undervalued Movement Pitches

Definition: movement quality percentile at least 75, with Pitch Value Score at or below league average.

| Rank | Pitcher | Team | Pitch | Pitches | PVS | xwOBA | IVB | HB | Spin | Velo | Ext | Archetype |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | Foster, Kobe | WAS_WIL3 | Curveball | 133 | 49.2 | 0.255 | -8.0 | 15.1 | 2232 | 67.6 | 5.46 | Tight High-Spin Breakers |
| 2 | Westcott, Zac | FLO_Y'A | Curveball | 163 | 21.1 | 0.379 | -15.2 | -9.2 | 1872 | 67.1 | 5.48 | Tight High-Spin Breakers |
| 3 | Kassebaum, Torin | LON_ISL22 | Curveball | 55 | 39.9 | 0.309 | 1.1 | 10.2 | 2155 | 71.6 | 5.31 | Tight High-Spin Breakers |
| 4 | Campbell, Tyler | MIS_MUD | Slider | 169 | 49.7 | 0.274 | 8.6 | 3.8 | 2220 | 74.5 | 5.74 | Tight High-Spin Breakers |
| 5 | Huter, Blayne | SUS_COU1 | Curveball | 103 | 44.4 | 0.275 | -5.1 | -14.2 | 2137 | 73.7 | 6.01 | Tight High-Spin Breakers |
| 6 | Pierson, Kenny | LAK_ERI24 | Slider | 82 | 47.3 | 0.284 | -1.6 | 7.0 | 2095 | 72.6 | 4.64 | Tight High-Spin Breakers |
| 7 | Johnston, Spencer | DOW_EAS1 | Curveball | 66 | 25.6 | 0.324 | -4.7 | -6.0 | 2133 | 74.4 | 5.68 | Tight High-Spin Breakers |
| 8 | Baker, Luke | EVA_OTT | Curveball | 59 | 47.5 | 0.248 | -7.4 | 9.7 | 2694 | 75.5 | 5.51 | Tight High-Spin Breakers |
| 9 | Martzolf, Max | OTT_TIT | Curveball | 71 | 43.1 | 0.294 | -4.2 | 11.1 | 2155 | 73.9 | 5.43 | Tight High-Spin Breakers |
| 10 | Villalobos, Jonaiker | FLO_Y'A | Curveball | 103 | 36.3 | 0.286 | -5.2 | 5.6 | 2260 | 74.5 | 5.33 | Tight High-Spin Breakers |
| 11 | Good, Ty | GAT_GRI | Curveball | 139 | 47.8 | 0.251 | -7.7 | -4.6 | 2134 | 75.0 | 5.65 | Tight High-Spin Breakers |
| 12 | Kaftan, Eddie | FLO_Y'A | Slider | 62 | 47.6 | 0.236 | 1.1 | -6.3 | 2437 | 77.1 | 4.72 | Tight High-Spin Breakers |
| 13 | Sechrist, Zander | WAS_WIL3 | Changeup | 166 | 35.8 | 0.311 | 6.8 | -14.7 | 1631 | 76.2 | 5.72 | Soft-Speed Separation |
| 14 | Misla, Luis | TRI_VAL | Curveball | 120 | 43.7 | 0.260 | -6.0 | 9.5 | 2802 | 76.8 | 5.14 | Tight High-Spin Breakers |
| 15 | Figueredo, Kevin | WIN_CIT29 | Curveball | 78 | 44.1 | 0.281 | -3.5 | 4.9 | 2324 | 75.8 | 5.00 | Tight High-Spin Breakers |
| 16 | Bice, Emmett | NEW_YOR13 | Curveball | 140 | 41.6 | 0.305 | -10.3 | -13.4 | 2985 | 79.0 | 5.54 | Tight High-Spin Breakers |
| 17 | Lovin, Xander | GAT_GRI | Curveball | 55 | 27.8 | 0.332 | -9.6 | -12.6 | 2634 | 77.0 | 4.70 | Tight High-Spin Breakers |
| 18 | Debban, Caleb | NEW_JER6 | Curveball | 182 | 46.5 | 0.281 | -7.2 | 18.5 | 2802 | 76.9 | 5.97 | Tight High-Spin Breakers |
| 19 | Williams, Pierce | NEW_ENG23 | Curveball | 135 | 38.1 | 0.282 | -5.9 | 6.6 | 2173 | 75.5 | 5.76 | Tight High-Spin Breakers |
| 20 | Okumura, Shuto | WAS_WIL3 | Four-Seam | 60 | 43.6 | 0.277 | 6.1 | 7.6 | 1757 | 75.3 | 5.56 | Soft-Speed Separation |
| 21 | Campbell, AJ | WIN_CIT29 | Slider | 281 | 49.9 | 0.238 | 4.8 | -11.0 | 2572 | 79.7 | 4.81 | Tight High-Spin Breakers |
| 22 | Soto, Carlos | JOL_SLA | Slider | 67 | 36.4 | 0.289 | -1.4 | -8.2 | 2487 | 78.4 | 5.15 | Tight High-Spin Breakers |
| 23 | Belton, Hunter | MIS_MUD | Slider | 99 | 49.7 | 0.248 | 6.5 | -2.6 | 2108 | 78.5 | 5.82 | Tight High-Spin Breakers |
| 24 | Eisenbarger, Jack | QUE_CAP | Changeup | 141 | 46.5 | 0.229 | 14.9 | -14.5 | 2314 | 78.7 | 6.09 | Glove-Side Power Break |
| 25 | Eldred, Zach | NEW_ENG23 | Curveball | 73 | 35.3 | 0.329 | -9.8 | -12.5 | 2484 | 78.0 | 5.87 | Tight High-Spin Breakers |
| 26 | Turner, Eric | JOL_SLA | Slider | 160 | 44.5 | 0.263 | 1.3 | -7.6 | 2351 | 78.3 | 5.00 | Tight High-Spin Breakers |
| 27 | Barker, Alex | NEW_YOR13 | Curveball | 83 | 47.4 | 0.244 | -5.5 | 10.3 | 2251 | 76.2 | 5.78 | Tight High-Spin Breakers |
| 28 | Smith, Donny | JOL_SLA | Slider | 66 | 43.4 | 0.250 | -2.4 | -5.4 | 2476 | 78.5 | 5.16 | Tight High-Spin Breakers |
| 29 | Hocom, Quinn | TRI_VAL | Curveball | 79 | 41.9 | 0.286 | -13.5 | -11.9 | 2377 | 76.9 | 5.52 | Tight High-Spin Breakers |
| 30 | Sparks, Alec | GAT_GRI | Slider | 131 | 49.2 | 0.250 | 0.2 | -7.3 | 2606 | 79.9 | 5.48 | Tight High-Spin Breakers |

## Top 20 Scouting Reports

1. **Grounds, Jackson, DOW_EAS1 Curveball** (Tight High-Spin Breakers): PVS 80.0, xwOBA 0.110. Shape: IVB -10.5, HB -12.0, 81.4 mph, 1946 rpm, 5.35 ft extension. Scouting read: low ride/drop, big horizontal; current results place it #1 overall and #1 within its pitch type.
2. **Morgan, Cooper, QUE_CAP Curveball** (Tight High-Spin Breakers): PVS 80.0, xwOBA 0.119. Shape: IVB -1.0, HB 16.8, 75.6 mph, 2657 rpm, 5.26 ft extension. Scouting read: low ride/drop, big horizontal, high spin, soft velo; current results place it #2 overall and #2 within its pitch type.
3. **Vecerka, Boris, QUE_CAP Slider** (Tight High-Spin Breakers): PVS 80.0, xwOBA 0.109. Shape: IVB 2.5, HB -11.8, 83.0 mph, 2496 rpm, 5.65 ft extension. Scouting read: low ride/drop, big horizontal, high spin; current results place it #3 overall and #1 within its pitch type.
4. **Carroll, Jake, JOL_SLA Slider** (Tight High-Spin Breakers): PVS 80.0, xwOBA 0.208. Shape: IVB -6.2, HB 7.8, 75.2 mph, 2033 rpm, 6.10 ft extension. Scouting read: low ride/drop, soft velo; current results place it #4 overall and #2 within its pitch type.
5. **Ryan, Dillon, NEW_ENG23 Slider** (Tight High-Spin Breakers): PVS 79.2, xwOBA 0.149. Shape: IVB -2.2, HB -8.5, 85.4 mph, 2495 rpm, 5.84 ft extension. Scouting read: low ride/drop, high spin; current results place it #5 overall and #3 within its pitch type.
6. **Lawson, Nathan, FLO_Y'A Changeup** (Soft-Speed Separation): PVS 77.0, xwOBA 0.168. Shape: IVB 8.0, HB 10.8, 79.8 mph, 1438 rpm, 5.78 ft extension. Scouting read: big horizontal, soft velo; current results place it #6 overall and #1 within its pitch type.
7. **Harper, Scott, NEW_YOR13 Slider** (Tight High-Spin Breakers): PVS 76.7, xwOBA 0.146. Shape: IVB 3.5, HB -16.7, 79.8 mph, 2675 rpm, 5.63 ft extension. Scouting read: big horizontal, high spin, soft velo; current results place it #7 overall and #4 within its pitch type.
8. **Peyton, Blake, GAT_GRI Changeup** (Glove-Side Power Break): PVS 76.4, xwOBA 0.142. Shape: IVB 10.4, HB -13.2, 81.0 mph, 1937 rpm, 6.10 ft extension. Scouting read: big horizontal, soft velo; current results place it #8 overall and #2 within its pitch type.
9. **Alpern, Liam, FLO_Y'A Slider** (Tight High-Spin Breakers): PVS 75.5, xwOBA 0.115. Shape: IVB -4.0, HB 11.5, 76.8 mph, 2219 rpm, 5.55 ft extension. Scouting read: low ride/drop, big horizontal, soft velo; current results place it #9 overall and #5 within its pitch type.
10. **Rodriguez, Joe Joe, NEW_JER6 Changeup** (Soft-Speed Separation): PVS 74.8, xwOBA 0.120. Shape: IVB 8.7, HB 15.3, 81.4 mph, 1799 rpm, 5.41 ft extension. Scouting read: big horizontal; current results place it #10 overall and #3 within its pitch type.
11. **Serrano, Elio, NEW_JER6 Changeup** (Soft-Speed Separation): PVS 74.3, xwOBA 0.162. Shape: IVB 10.8, HB 11.9, 82.2 mph, 1834 rpm, 5.93 ft extension. Scouting read: big horizontal; current results place it #11 overall and #4 within its pitch type.
12. **Jones, Logan, TRI_VAL Slider** (Tight High-Spin Breakers): PVS 73.7, xwOBA 0.191. Shape: IVB 2.5, HB 2.3, 83.5 mph, 2341 rpm, 5.69 ft extension. Scouting read: low ride/drop, high spin; current results place it #12 overall and #6 within its pitch type.
13. **Davis, Tyler, WIN_CIT29 Four-Seam** (Arm-Side Run Power): PVS 73.6, xwOBA 0.113. Shape: IVB 21.2, HB 5.6, 89.3 mph, 2171 rpm, 5.86 ft extension. Scouting read: plus ride, power velocity; current results place it #13 overall and #1 within its pitch type.
14. **Grounds, Jackson, DOW_EAS1 Four-Seam** (Arm-Side Run Power): PVS 73.5, xwOBA 0.161. Shape: IVB 17.0, HB 14.2, 92.5 mph, 2163 rpm, 5.59 ft extension. Scouting read: plus ride, big horizontal, power velocity; current results place it #14 overall and #2 within its pitch type.
15. **Webster, Evan, FLO_Y'A Cutter** (Glove-Side Power Break): PVS 73.5, xwOBA 0.147. Shape: IVB 5.8, HB -0.1, 84.2 mph, 2054 rpm, 6.96 ft extension. Scouting read: extension; current results place it #15 overall and #1 within its pitch type.
16. **Bargo, Casey, NEW_ENG23 Slider** (Tight High-Spin Breakers): PVS 72.8, xwOBA 0.178. Shape: IVB 1.5, HB -5.0, 83.6 mph, 2416 rpm, 5.66 ft extension. Scouting read: low ride/drop, high spin; current results place it #16 overall and #7 within its pitch type.
17. **Garcia, Hector, WAS_WIL3 Splitter** (Soft-Speed Separation): PVS 72.7, xwOBA 0.187. Shape: IVB 11.7, HB 7.6, 78.2 mph, 1216 rpm, 5.92 ft extension. Scouting read: soft velo; current results place it #17 overall and #1 within its pitch type.
18. **Lovell, Justin, WIN_CIT29 Sinker** (Glove-Side Power Break): PVS 72.2, xwOBA 0.127. Shape: IVB 12.6, HB -15.2, 93.2 mph, 2268 rpm, 6.29 ft extension. Scouting read: big horizontal, power velocity, extension; current results place it #18 overall and #1 within its pitch type.
19. **Escobar, Anthony, TRO_AIG Changeup** (Soft-Speed Separation): PVS 72.0, xwOBA 0.150. Shape: IVB 10.2, HB 11.6, 79.6 mph, 1617 rpm, 6.22 ft extension. Scouting read: big horizontal, soft velo, extension; current results place it #19 overall and #5 within its pitch type.
20. **McEvoy, Aidan, FLO_Y'A Slider** (Soft-Speed Separation): PVS 71.7, xwOBA 0.146. Shape: IVB 6.6, HB 10.0, 78.8 mph, 2213 rpm, 6.04 ft extension. Scouting read: soft velo; current results place it #20 overall and #8 within its pitch type.

## Plots

- `plots\pitch_movement_archetypes\cluster_count_selection.png`
- `plots\pitch_movement_archetypes\archetypes_hb_ivb.png`
- `plots\pitch_movement_archetypes\archetypes_velocity_spin.png`
- `plots\pitch_movement_archetypes\archetypes_pca.png`
- `plots\pitch_movement_archetypes\archetype_pitch_value.png`