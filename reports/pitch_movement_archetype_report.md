# Frontier League Movement Archetypes

- Input file: `data\processed\pitch_value_movement_model_data.csv`
- Scored output: `data\processed\pitch_movement_archetypes.csv`
- Cluster summary: `data\processed\pitch_movement_archetype_summary.csv`
- Highest-performing archetype pitch list: `data\processed\highest_performing_archetype_pitches.csv`
- Undervalued pitch list: `data\processed\undervalued_movement_pitches.csv`
- Qualified pitcher-pitch types clustered: 568
- Features clustered: IVB, HB, spin rate, velocity, extension
- Selected cluster count: 4
- Full methodology write-up: `reports/FRONTIER_PITCH_VALUE_METHODOLOGY.md`

## How To Read This Report

Higher Pitch Value Score is better. It means the pitch has the outcome profile associated with lower expected xwOBA damage. Archetypes are movement-shape groups, not direct pitcher grades.

The cluster labels describe the average movement identity of each group. Average Pitch Value Score by cluster tells us which movement families performed best in this dataset, but individual pitches within a cluster can still vary widely based on command, usage, sequencing, and sample size.

## Cluster Count Test

| k | Inertia | Silhouette |
|---:|---:|---:|
| 2 | 1970.85 | 0.3032 |
| 3 | 1595.00 | 0.3001 |
| 4 | 1305.10 | 0.3093 **selected** |
| 5 | 1172.50 | 0.2555 |
| 6 | 1068.10 | 0.2406 |
| 7 | 971.20 | 0.2526 |
| 8 | 904.92 | 0.2513 |
| 9 | 842.27 | 0.2612 |
| 10 | 798.68 | 0.2510 |

## Archetype Summary

| Rank | Archetype | Pitches | Instances | Avg PVS | Avg xwOBA | IVB | HB | Spin | Velo | Ext | Common Pitch Types |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|
| 1 | `Tight High-Spin Breakers` | 14,369 | 149 | 52.7 | 0.235 | -0.4 | -2.6 | 2359 | 79.9 | 5.49 | Slider, Curveball, Cutter |
| 2 | `Soft-Speed Separation` | 7,204 | 77 | 51.1 | 0.242 | 7.1 | 9.6 | 1742 | 81.3 | 5.80 | Changeup, Slider, Splitter |
| 3 | `Riding Shape / Lower Velo` | 14,895 | 120 | 50.1 | 0.242 | 13.1 | -10.8 | 2099 | 86.9 | 5.98 | Four-Seam, Sinker, Changeup |
| 4 | `Arm-Side Run Power` | 28,872 | 222 | 47.7 | 0.247 | 14.7 | 11.3 | 2213 | 90.3 | 5.99 | Four-Seam, Sinker, Cutter |

## Highest-Performing Archetypes

- `Tight High-Spin Breakers`: average PVS 52.7, avg xwOBA 0.235, typical shape -0.4 IVB / -2.6 HB at 79.9 mph.
- `Soft-Speed Separation`: average PVS 51.1, avg xwOBA 0.242, typical shape 7.1 IVB / 9.6 HB at 81.3 mph.

## Pitchers in Highest-Performing Archetypes

| Rank | Pitcher | Team | Pitch | Pitches | PVS | xwOBA | IVB | HB | Spin | Velo | Ext | Archetype |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | Grounds, Jackson | DOW_EAS1 | Curveball | 82 | 80.0 | 0.104 | -10.5 | -12.0 | 1946 | 81.4 | 5.35 | Tight High-Spin Breakers |
| 2 | Carroll, Jake | JOL_SLA | Slider | 56 | 80.0 | 0.204 | -6.4 | 7.7 | 2019 | 75.2 | 6.09 | Tight High-Spin Breakers |
| 3 | Harper, Scott | NEW_YOR13 | Slider | 114 | 77.6 | 0.133 | 3.2 | -16.4 | 2650 | 79.8 | 5.70 | Tight High-Spin Breakers |
| 4 | Ryan, Dillon | NEW_ENG23 | Slider | 93 | 76.3 | 0.154 | -2.3 | -8.2 | 2494 | 85.4 | 5.85 | Tight High-Spin Breakers |
| 5 | Alpern, Liam | FLO_Y'A | Slider | 78 | 74.3 | 0.113 | -4.0 | 11.5 | 2219 | 76.8 | 5.55 | Tight High-Spin Breakers |
| 6 | Foster, Kobe | WAS_WIL3 | Slider | 94 | 73.0 | 0.133 | 5.0 | 6.2 | 2332 | 78.1 | 5.38 | Tight High-Spin Breakers |
| 7 | Jones, Logan | TRI_VAL | Slider | 65 | 72.7 | 0.189 | 2.5 | 2.3 | 2341 | 83.5 | 5.69 | Tight High-Spin Breakers |
| 8 | Perez, Kelvin | WAS_WIL3 | Slider | 56 | 72.4 | 0.127 | 3.7 | -5.7 | 2239 | 81.3 | 5.81 | Tight High-Spin Breakers |
| 9 | Bargo, Casey | NEW_ENG23 | Slider | 56 | 71.8 | 0.177 | 1.5 | -5.0 | 2416 | 83.6 | 5.66 | Tight High-Spin Breakers |
| 10 | Harajli, Ahmad | FLO_Y'A | Slider | 58 | 68.9 | 0.149 | -2.3 | -2.4 | 2057 | 80.6 | 6.03 | Tight High-Spin Breakers |
| 11 | Harris, Ben | GAT_GRI | Curveball | 138 | 68.7 | 0.215 | -14.0 | -7.2 | 2124 | 78.0 | 4.99 | Tight High-Spin Breakers |
| 12 | Donnan, Blake | FLO_Y'A | Slider | 65 | 68.5 | 0.186 | 5.0 | -7.3 | 2367 | 80.5 | 5.42 | Tight High-Spin Breakers |
| 13 | Smith, Jackson | MIS_MUD | Slider | 69 | 68.5 | 0.177 | 2.1 | -10.2 | 2661 | 78.1 | 4.80 | Tight High-Spin Breakers |
| 14 | Kirby, Zach | WAS_WIL3 | Slider | 102 | 67.9 | 0.168 | 5.6 | -13.2 | 2235 | 77.9 | 5.68 | Tight High-Spin Breakers |
| 15 | Nakata, Yuto | QUE_CAP | Slider | 57 | 67.1 | 0.146 | 5.1 | -6.4 | 2360 | 81.9 | 5.72 | Tight High-Spin Breakers |
| 16 | Sesar, Jorden | SUS_COU1 | Curveball | 76 | 66.8 | 0.192 | -12.7 | -11.8 | 2431 | 74.8 | 6.01 | Tight High-Spin Breakers |
| 17 | Long, Maddox | WAS_WIL3 | Slider | 145 | 64.8 | 0.174 | 3.1 | -8.9 | 2639 | 82.8 | 5.40 | Tight High-Spin Breakers |
| 18 | Morin, Jacob | QUE_CAP | Slider | 85 | 64.6 | 0.206 | 7.4 | -6.2 | 2495 | 77.4 | 5.50 | Tight High-Spin Breakers |
| 19 | Hill, Kaleb | OTT_TIT | Curveball | 179 | 64.2 | 0.198 | -4.0 | 13.1 | 2136 | 73.1 | 5.33 | Tight High-Spin Breakers |
| 20 | Lefebvre, Charles | TRO_AIG | Slider | 66 | 62.3 | 0.139 | 2.1 | -1.6 | 2181 | 82.5 | 6.36 | Tight High-Spin Breakers |
| 21 | Armstrong, Andrew | NEW_YOR13 | Slider | 68 | 61.9 | 0.223 | 1.6 | 9.9 | 2437 | 78.9 | 5.85 | Tight High-Spin Breakers |
| 22 | Toribio, Noe | TRO_AIG | Slider | 82 | 61.6 | 0.180 | 2.8 | 0.8 | 2249 | 82.5 | 5.67 | Tight High-Spin Breakers |
| 23 | Tokar, Heitor | OTT_TIT | Slider | 80 | 61.6 | 0.188 | 4.4 | -3.6 | 2124 | 81.9 | 5.96 | Tight High-Spin Breakers |
| 24 | Baird, Dustin | MIS_MUD | Slider | 57 | 61.0 | 0.212 | 8.2 | -9.0 | 2365 | 81.3 | 5.87 | Tight High-Spin Breakers |
| 25 | Pierson, Kenny | LAK_ERI24 | Sinker | 88 | 60.9 | 0.183 | -0.1 | -20.2 | 1736 | 80.5 | 4.79 | Tight High-Spin Breakers |
| 26 | Gollert, Harley | QUE_CAP | Slider | 57 | 60.7 | 0.216 | 1.0 | 5.1 | 2222 | 79.4 | 5.09 | Tight High-Spin Breakers |
| 27 | Simpson, Garret | EVA_OTT | Curveball | 64 | 60.7 | 0.190 | -13.4 | -13.3 | 2725 | 76.8 | 5.21 | Tight High-Spin Breakers |
| 28 | Vailes, Gage | GAT_GRI | Slider | 177 | 60.6 | 0.196 | 6.3 | -12.0 | 2576 | 81.8 | 4.57 | Tight High-Spin Breakers |
| 29 | Garcia, Brett | OTT_TIT | Curveball | 72 | 60.1 | 0.191 | -16.8 | -7.5 | 2116 | 81.1 | 5.34 | Tight High-Spin Breakers |
| 30 | Cook, Cole | SCH_BOO | Slider | 126 | 60.0 | 0.209 | 3.5 | 5.6 | 2501 | 79.7 | 5.13 | Tight High-Spin Breakers |
| 31 | Heredia-Bustos, Rolando | DOW_EAS1 | Slider | 300 | 59.0 | 0.193 | 6.7 | -4.7 | 2341 | 79.0 | 5.34 | Tight High-Spin Breakers |
| 32 | Villers, Ian | QUE_CAP | Slider | 66 | 59.0 | 0.239 | -0.3 | -5.1 | 2117 | 82.3 | 5.94 | Tight High-Spin Breakers |
| 33 | Calderon, Jean | LAK_ERI24 | Slider | 73 | 59.0 | 0.199 | 1.3 | -9.7 | 2593 | 86.4 | 6.05 | Tight High-Spin Breakers |
| 34 | Plumadore, Carson | WIN_CIT29 | Slider | 63 | 58.7 | 0.194 | 3.4 | -6.0 | 2452 | 75.7 | 5.52 | Tight High-Spin Breakers |
| 35 | Vega, Lucas | TRO_AIG | Slider | 73 | 58.7 | 0.185 | 6.2 | -10.8 | 2705 | 79.0 | 5.78 | Tight High-Spin Breakers |
| 36 | Garcia, Andrew | EVA_OTT | Slider | 178 | 58.7 | 0.188 | 2.5 | -6.9 | 2313 | 82.3 | 5.37 | Tight High-Spin Breakers |
| 37 | Langhorne, Miles | SUS_COU1 | Slider | 61 | 58.5 | 0.223 | 0.0 | -3.1 | 2487 | 86.8 | 5.90 | Tight High-Spin Breakers |
| 38 | Salata, Derek | SCH_BOO | Curveball | 52 | 58.5 | 0.238 | -11.9 | -13.3 | 2664 | 74.6 | 5.62 | Tight High-Spin Breakers |
| 39 | Dill, Austin | TRI_VAL | Slider | 70 | 58.4 | 0.237 | 1.6 | -3.7 | 2565 | 79.3 | 4.97 | Tight High-Spin Breakers |
| 40 | Joven, Art | MIS_MUD | Slider | 161 | 58.4 | 0.207 | 2.1 | -0.3 | 2228 | 77.7 | 5.14 | Tight High-Spin Breakers |
| 41 | Shinn, Nathan | LAK_ERI24 | Slider | 138 | 58.2 | 0.217 | 0.3 | 0.8 | 2179 | 82.1 | 5.24 | Tight High-Spin Breakers |
| 42 | Nova, Fraynel | LAK_ERI24 | Slider | 198 | 58.2 | 0.214 | -0.5 | -6.5 | 2253 | 80.5 | 5.64 | Tight High-Spin Breakers |
| 43 | Brito, Richard | NEW_ENG23 | Slider | 73 | 58.1 | 0.197 | 3.6 | -6.0 | 2287 | 81.7 | 6.09 | Tight High-Spin Breakers |
| 44 | Cohn, Cooper | NIU_HUS | Slider | 63 | 58.1 | 0.190 | -1.2 | -13.7 | 2534 | 78.9 | 5.40 | Tight High-Spin Breakers |
| 45 | Odonnell, Brendan | NEW_ENG23 | Slider | 98 | 57.7 | 0.209 | -2.0 | 12.3 | 2652 | 84.3 | 6.25 | Tight High-Spin Breakers |
| 46 | Fauci, Sonny | NEW_JER6 | Slider | 69 | 57.7 | 0.253 | -2.6 | -7.4 | 2329 | 83.1 | 6.07 | Tight High-Spin Breakers |
| 47 | Kirby, Zach | WAS_WIL3 | Curveball | 98 | 57.5 | 0.225 | -18.3 | -10.7 | 2271 | 70.9 | 5.42 | Tight High-Spin Breakers |
| 48 | Leak, Anthony | NEW_YOR13 | Slider | 142 | 57.2 | 0.180 | 4.5 | -6.8 | 2325 | 82.9 | 5.84 | Tight High-Spin Breakers |
| 49 | Hagan, Jack | DOW_EAS1 | Slider | 116 | 57.2 | 0.240 | 3.9 | -4.0 | 2427 | 84.0 | 5.74 | Tight High-Spin Breakers |
| 50 | Petschke, Ben | EVA_OTT | Slider | 111 | 57.2 | 0.204 | -1.3 | -12.7 | 2605 | 81.6 | 5.14 | Tight High-Spin Breakers |
| 51 | Moore, Kyle | SCH_BOO | Cutter | 97 | 57.1 | 0.225 | 9.7 | 1.4 | 2150 | 84.7 | 4.75 | Tight High-Spin Breakers |
| 52 | Anibal, Trevor | NEW_ENG23 | Curveball | 71 | 57.1 | 0.233 | -15.4 | -9.6 | 2476 | 75.9 | 5.47 | Tight High-Spin Breakers |
| 53 | Morgan, Marcus | JOL_SLA | Cutter | 56 | 56.9 | 0.196 | 6.5 | -3.1 | 2678 | 87.0 | 5.76 | Tight High-Spin Breakers |
| 54 | Garcia, Hector | WAS_WIL3 | Slider | 56 | 56.9 | 0.229 | 2.0 | -7.1 | 2355 | 77.3 | 5.72 | Tight High-Spin Breakers |
| 55 | Petschke, Ben | EVA_OTT | Curveball | 158 | 56.4 | 0.232 | -9.6 | -15.8 | 2769 | 77.3 | 4.98 | Tight High-Spin Breakers |
| 56 | Thompson, Ross | SCH_BOO | Slider | 118 | 56.3 | 0.214 | 3.8 | -2.8 | 2052 | 79.7 | 5.20 | Tight High-Spin Breakers |
| 57 | Majick, Eli | NEW_ENG23 | Slider | 107 | 56.3 | 0.223 | 3.7 | 7.3 | 2519 | 79.8 | 5.66 | Tight High-Spin Breakers |
| 58 | Bice, Emmett | NEW_YOR13 | Slider | 187 | 55.9 | 0.234 | 1.8 | -3.1 | 2420 | 82.9 | 5.68 | Tight High-Spin Breakers |
| 59 | Gamelin, Shaun | JOL_SLA | Cutter | 113 | 55.8 | 0.225 | 5.7 | -0.3 | 2313 | 83.7 | 5.07 | Tight High-Spin Breakers |
| 60 | Noriega, Branden | LAK_ERI24 | Curveball | 90 | 54.9 | 0.244 | -10.3 | 8.6 | 2837 | 79.2 | 5.23 | Tight High-Spin Breakers |
| 61 | Kaminer, Brandon | DOW_EAS1 | Slider | 99 | 54.7 | 0.213 | 5.6 | 3.2 | 2499 | 84.3 | 5.27 | Tight High-Spin Breakers |
| 62 | Milburn, Isaac | FLO_Y'A | Curveball | 134 | 54.7 | 0.249 | -9.4 | 13.7 | 2595 | 76.7 | 4.99 | Tight High-Spin Breakers |
| 63 | Milburn, Isaac | FLO_Y'A | Slider | 149 | 54.6 | 0.224 | -1.7 | 16.0 | 2655 | 78.6 | 4.85 | Tight High-Spin Breakers |
| 64 | Cooper, Garrett | NEW_YOR13 | Slider | 57 | 54.3 | 0.205 | 2.4 | -4.4 | 2163 | 81.0 | 5.62 | Tight High-Spin Breakers |
| 65 | Puccetti, Dominic | OTT_TIT | Curveball | 148 | 53.9 | 0.240 | -14.0 | 9.9 | 2699 | 73.6 | 5.25 | Tight High-Spin Breakers |
| 66 | Balzan, Jackson | SUS_COU1 | Curveball | 56 | 53.8 | 0.205 | -4.7 | 5.3 | 2090 | 76.3 | 5.10 | Tight High-Spin Breakers |
| 67 | Oe, Ryoya | OTT_TIT | Curveball | 57 | 53.5 | 0.210 | -4.6 | 5.0 | 2303 | 73.3 | 4.90 | Tight High-Spin Breakers |
| 68 | Cameron, Zach | WIN_CIT29 | Slider | 51 | 53.4 | 0.231 | 5.3 | -3.9 | 2333 | 80.8 | 5.51 | Tight High-Spin Breakers |
| 69 | Eckaus, David | EVA_OTT | Slider | 70 | 53.2 | 0.230 | 3.2 | 3.8 | 2527 | 82.6 | 5.61 | Tight High-Spin Breakers |
| 70 | Simpson, Garret | EVA_OTT | Cutter | 64 | 52.9 | 0.260 | 1.6 | -1.2 | 2503 | 84.3 | 5.29 | Tight High-Spin Breakers |
| 71 | Williams, Brian | MIS_MUD | Slider | 160 | 52.7 | 0.248 | 4.4 | -0.8 | 2156 | 81.4 | 5.94 | Tight High-Spin Breakers |
| 72 | Peyton, Blake | GAT_GRI | Curveball | 58 | 52.6 | 0.209 | -5.8 | 9.0 | 2690 | 77.6 | 5.20 | Tight High-Spin Breakers |
| 73 | Gamelin, Shaun | JOL_SLA | Slider | 61 | 52.3 | 0.234 | 2.1 | -1.3 | 2286 | 81.4 | 4.79 | Tight High-Spin Breakers |
| 74 | Pierson, Kenny | LAK_ERI24 | Changeup | 145 | 52.3 | 0.242 | -1.5 | -18.1 | 1777 | 76.7 | 5.00 | Tight High-Spin Breakers |
| 75 | Good, Ty | GAT_GRI | Slider | 81 | 52.1 | 0.221 | 3.8 | -1.0 | 2067 | 79.7 | 5.88 | Tight High-Spin Breakers |
| 76 | Peters, Garrett | NEW_YOR13 | Curveball | 89 | 51.9 | 0.236 | 0.8 | -1.0 | 2047 | 75.8 | 5.67 | Tight High-Spin Breakers |
| 77 | McCartney, Seth | MIS_MUD | Slider | 57 | 51.8 | 0.197 | 4.2 | -3.0 | 2474 | 81.9 | 5.45 | Tight High-Spin Breakers |
| 78 | Pardinho, Eric | OTT_TIT | Slider | 50 | 51.7 | 0.242 | 5.9 | 1.9 | 2310 | 86.7 | 5.67 | Tight High-Spin Breakers |
| 79 | Sanchez, Edwin | LAK_ERI24 | Curveball | 53 | 51.6 | 0.242 | -5.1 | 6.6 | 2473 | 75.9 | 5.40 | Tight High-Spin Breakers |
| 80 | Blair, Davis | DOW_EAS1 | Slider | 99 | 51.3 | 0.259 | 3.6 | -5.9 | 2146 | 81.9 | 5.11 | Tight High-Spin Breakers |
| 81 | Morgan, Marcus | JOL_SLA | Slider | 53 | 51.2 | 0.236 | 7.5 | -10.1 | 2872 | 84.7 | 5.73 | Tight High-Spin Breakers |
| 82 | Wiltse, Ryan | EVA_OTT | Curveball | 75 | 51.1 | 0.245 | -11.8 | -4.1 | 1872 | 74.4 | 5.95 | Tight High-Spin Breakers |
| 83 | Barker, Alex | NEW_YOR13 | Curveball | 66 | 51.0 | 0.228 | -5.6 | 10.3 | 2250 | 76.2 | 5.77 | Tight High-Spin Breakers |
| 84 | Henderson, Drew | DOW_EAS1 | Curveball | 171 | 51.0 | 0.213 | -8.1 | -4.8 | 2319 | 76.9 | 5.18 | Tight High-Spin Breakers |
| 85 | Langrell, Connor | MIS_MUD | Curveball | 73 | 50.7 | 0.255 | -15.1 | -12.3 | 2676 | 77.6 | 6.00 | Tight High-Spin Breakers |
| 86 | Saturria, Michael | NEW_ENG23 | Slider | 144 | 50.6 | 0.227 | 4.1 | -7.8 | 2707 | 80.3 | 5.86 | Tight High-Spin Breakers |
| 87 | Cooper, Garrett | NEW_YOR13 | Curveball | 92 | 50.6 | 0.221 | -4.4 | -6.2 | 2160 | 76.8 | 5.56 | Tight High-Spin Breakers |
| 88 | Wehrle, Tyler | WIN_CIT29 | Slider | 142 | 50.6 | 0.229 | 2.4 | -9.9 | 2516 | 80.8 | 5.35 | Tight High-Spin Breakers |
| 89 | Belton, Hunter | MIS_MUD | Slider | 99 | 50.3 | 0.246 | 6.5 | -2.6 | 2108 | 78.5 | 5.82 | Tight High-Spin Breakers |
| 90 | Helt, Robert | LAK_ERI24 | Curveball | 106 | 50.1 | 0.259 | -5.6 | -5.7 | 2386 | 79.0 | 5.83 | Tight High-Spin Breakers |
| 91 | Galva, Claudio | GAT_GRI | Slider | 117 | 50.0 | 0.226 | 2.9 | -0.7 | 2249 | 83.7 | 4.81 | Tight High-Spin Breakers |
| 92 | Forsyth, Braden | MIS_MUD | Slider | 97 | 49.6 | 0.269 | 4.1 | -6.4 | 2352 | 80.7 | 6.05 | Tight High-Spin Breakers |
| 93 | Sparks, Alec | GAT_GRI | Slider | 108 | 49.2 | 0.245 | 0.5 | -7.0 | 2625 | 80.1 | 5.48 | Tight High-Spin Breakers |
| 94 | Hicks, Jackson | DOW_EAS1 | Slider | 116 | 48.7 | 0.270 | 2.4 | -1.0 | 2195 | 80.0 | 5.23 | Tight High-Spin Breakers |
| 95 | Smith, Ethan | WIN_CIT29 | Slider | 58 | 48.5 | 0.282 | -0.2 | -6.4 | 2423 | 80.6 | 5.91 | Tight High-Spin Breakers |
| 96 | Kaftan, Eddie | FLO_Y'A | Slider | 62 | 48.4 | 0.233 | 1.1 | -6.3 | 2437 | 77.1 | 4.72 | Tight High-Spin Breakers |
| 97 | Sakurai, Masatoshi | QUE_CAP | Slider | 92 | 48.4 | 0.256 | -0.6 | 4.7 | 2260 | 78.8 | 5.77 | Tight High-Spin Breakers |
| 98 | Campbell, AJ | WIN_CIT29 | Slider | 162 | 48.3 | 0.253 | 4.7 | -10.1 | 2556 | 80.2 | 4.92 | Tight High-Spin Breakers |
| 99 | Baker, Luke | EVA_OTT | Curveball | 59 | 48.2 | 0.246 | -7.4 | 9.7 | 2694 | 75.5 | 5.51 | Tight High-Spin Breakers |
| 100 | Perdomo, Rafael | QUE_CAP | Slider | 84 | 48.0 | 0.262 | 3.1 | 0.8 | 2184 | 82.9 | 5.80 | Tight High-Spin Breakers |
| 101 | Hill, Kaleb | OTT_TIT | Slider | 58 | 47.9 | 0.246 | 0.2 | 8.9 | 2235 | 78.6 | 5.26 | Tight High-Spin Breakers |
| 102 | Smith, Jackson | MIS_MUD | Sinker | 297 | 47.9 | 0.258 | 0.8 | 22.0 | 2414 | 85.6 | 5.10 | Tight High-Spin Breakers |
| 103 | Allemann, Braeden | QUE_CAP | Curveball | 146 | 47.8 | 0.251 | -7.2 | -15.6 | 2185 | 76.7 | 6.17 | Tight High-Spin Breakers |
| 104 | Castro, Alexander | TRO_AIG | Slider | 73 | 47.8 | 0.268 | 0.8 | -4.8 | 2513 | 83.7 | 4.73 | Tight High-Spin Breakers |
| 105 | Foy, Corbin | LAK_ERI24 | Slider | 78 | 47.7 | 0.270 | -1.1 | -7.6 | 2653 | 82.4 | 5.56 | Tight High-Spin Breakers |
| 106 | Parra, Andres | LAK_ERI24 | Slider | 161 | 47.3 | 0.266 | 2.8 | 2.0 | 2288 | 79.6 | 5.71 | Tight High-Spin Breakers |
| 107 | Campbell, Tyler | MIS_MUD | Slider | 71 | 47.1 | 0.271 | 8.0 | 5.4 | 2236 | 74.0 | 5.57 | Tight High-Spin Breakers |
| 108 | Foster, Kobe | WAS_WIL3 | Curveball | 99 | 47.0 | 0.272 | -8.0 | 15.4 | 2246 | 67.8 | 5.41 | Tight High-Spin Breakers |
| 109 | Helt, Robert | LAK_ERI24 | Slider | 120 | 46.9 | 0.263 | -1.4 | -5.9 | 2406 | 80.6 | 5.90 | Tight High-Spin Breakers |
| 110 | Turner, Eric | JOL_SLA | Slider | 118 | 46.9 | 0.259 | 1.4 | -7.1 | 2341 | 78.6 | 4.95 | Tight High-Spin Breakers |
| 111 | Moore, Kyle | SCH_BOO | Curveball | 85 | 46.9 | 0.265 | -8.9 | -8.6 | 2532 | 76.8 | 4.14 | Tight High-Spin Breakers |
| 112 | Cook, Cole | SCH_BOO | Cutter | 93 | 46.8 | 0.214 | 9.0 | -3.2 | 2420 | 82.3 | 5.28 | Tight High-Spin Breakers |
| 113 | Escobar, Anthony | TRO_AIG | Slider | 149 | 46.5 | 0.268 | 3.3 | -5.0 | 2184 | 82.0 | 6.12 | Tight High-Spin Breakers |
| 114 | Encarnacion, J.D. | EVA_OTT | Slider | 88 | 46.4 | 0.229 | 2.2 | -5.1 | 2356 | 81.1 | 5.39 | Tight High-Spin Breakers |
| 115 | Sittinger, Brandyn | LAK_ERI24 | Slider | 73 | 46.4 | 0.278 | 3.1 | -1.3 | 2489 | 87.7 | 5.76 | Tight High-Spin Breakers |
| 116 | Scafidi, Christian | LAK_ERI24 | Slider | 117 | 46.4 | 0.242 | 3.9 | -2.5 | 2389 | 83.8 | 5.74 | Tight High-Spin Breakers |
| 117 | Andueza, Axel | DOW_EAS1 | Curveball | 118 | 46.2 | 0.248 | -3.2 | -3.5 | 2183 | 79.3 | 5.06 | Tight High-Spin Breakers |
| 118 | Lovin, Xander | GAT_GRI | Slider | 95 | 46.2 | 0.270 | 2.7 | -3.9 | 2440 | 85.2 | 4.99 | Tight High-Spin Breakers |
| 119 | Burcham, Jacob | GAT_GRI | Slider | 64 | 46.1 | 0.229 | 0.1 | -8.0 | 2376 | 81.6 | 5.90 | Tight High-Spin Breakers |
| 120 | Willeman, Landon | EVA_OTT | Curveball | 66 | 46.1 | 0.289 | -7.4 | -10.1 | 2132 | 78.1 | 5.28 | Tight High-Spin Breakers |
| 121 | Hampton, Ky | OTT_TIT | Slider | 67 | 45.8 | 0.253 | 2.1 | -3.7 | 2304 | 83.7 | 5.90 | Tight High-Spin Breakers |
| 122 | Bradford, Ethan | NEW_YOR13 | Slider | 69 | 45.6 | 0.283 | -1.2 | 7.3 | 2397 | 81.3 | 5.37 | Tight High-Spin Breakers |
| 123 | Huter, Blayne | SUS_COU1 | Curveball | 103 | 45.3 | 0.273 | -5.1 | -14.2 | 2137 | 73.7 | 6.01 | Tight High-Spin Breakers |
| 124 | Figueredo, Kevin | WIN_CIT29 | Curveball | 78 | 45.1 | 0.277 | -3.5 | 4.9 | 2324 | 75.8 | 5.00 | Tight High-Spin Breakers |
| 125 | Godwin, Connor | NEW_YOR13 | Slider | 93 | 44.3 | 0.262 | 0.0 | -10.2 | 2535 | 82.4 | 6.11 | Tight High-Spin Breakers |
| 126 | Martzolf, Max | OTT_TIT | Curveball | 71 | 44.2 | 0.292 | -4.2 | 11.1 | 2155 | 73.9 | 5.43 | Tight High-Spin Breakers |
| 127 | Misla, Luis | TRI_VAL | Curveball | 82 | 43.9 | 0.259 | -6.3 | 9.7 | 2805 | 76.9 | 5.11 | Tight High-Spin Breakers |
| 128 | Scott, Brandon | LAK_ERI24 | Slider | 90 | 42.8 | 0.266 | -0.4 | 8.0 | 2450 | 77.9 | 5.53 | Tight High-Spin Breakers |
| 129 | Parsons, Billy | SUS_COU1 | Slider | 187 | 42.6 | 0.241 | 6.3 | -6.3 | 2496 | 83.3 | 5.51 | Tight High-Spin Breakers |
| 130 | Shinn, Nathan | LAK_ERI24 | Curveball | 88 | 41.8 | 0.279 | -5.9 | 0.6 | 2113 | 79.6 | 5.29 | Tight High-Spin Breakers |
| 131 | Sanchez, Dikember | LAK_ERI24 | Slider | 111 | 41.7 | 0.275 | 2.1 | -3.7 | 2555 | 85.9 | 5.32 | Tight High-Spin Breakers |
| 132 | Bice, Emmett | NEW_YOR13 | Curveball | 87 | 41.1 | 0.317 | -10.1 | -13.8 | 2963 | 79.2 | 5.65 | Tight High-Spin Breakers |
| 133 | Kassebaum, Torin | LON_ISL22 | Curveball | 55 | 41.1 | 0.307 | 1.1 | 10.2 | 2155 | 71.6 | 5.31 | Tight High-Spin Breakers |
| 134 | Williams, Pierce | NEW_ENG23 | Curveball | 120 | 41.1 | 0.273 | -5.9 | 6.7 | 2174 | 75.4 | 5.74 | Tight High-Spin Breakers |
| 135 | Sabatine, Gino | TRI_VAL | Slider | 109 | 40.9 | 0.289 | 4.6 | -3.0 | 2300 | 80.0 | 4.86 | Tight High-Spin Breakers |
| 136 | Sakurai, Masatoshi | QUE_CAP | Curveball | 89 | 39.6 | 0.301 | -3.9 | 5.7 | 2472 | 78.2 | 5.61 | Tight High-Spin Breakers |
| 137 | Barker, Alex | NEW_YOR13 | Slider | 92 | 39.4 | 0.295 | 3.1 | 4.4 | 2208 | 81.4 | 5.99 | Tight High-Spin Breakers |
| 138 | Salata, Derek | SCH_BOO | Slider | 108 | 38.7 | 0.307 | 2.5 | -10.7 | 2567 | 80.5 | 5.63 | Tight High-Spin Breakers |
| 139 | Parks, Pavin | LAK_ERI24 | Cutter | 113 | 38.1 | 0.302 | 6.9 | -3.8 | 2443 | 85.0 | 5.91 | Tight High-Spin Breakers |
| 140 | Correa, Nelvin | QUE_CAP | Slider | 72 | 37.8 | 0.276 | 5.1 | -7.0 | 2384 | 83.2 | 5.48 | Tight High-Spin Breakers |
| 141 | Villalobos, Jonaiker | FLO_Y'A | Curveball | 90 | 37.8 | 0.282 | -5.2 | 5.5 | 2262 | 74.8 | 5.36 | Tight High-Spin Breakers |
| 142 | Andueza, Axel | DOW_EAS1 | Slider | 61 | 37.2 | 0.297 | -0.6 | -1.9 | 2096 | 80.8 | 5.14 | Tight High-Spin Breakers |
| 143 | Valdez, Alex | EVA_OTT | Slider | 95 | 36.5 | 0.265 | 3.3 | -2.7 | 2195 | 85.6 | 5.32 | Tight High-Spin Breakers |
| 144 | Tiburcio, David | DOW_EAS1 | Slider | 61 | 36.3 | 0.304 | 6.1 | 0.6 | 2387 | 86.0 | 5.35 | Tight High-Spin Breakers |
| 145 | Gorgen, Grady | NEW_YOR13 | Slider | 75 | 34.9 | 0.320 | 1.9 | 0.6 | 2131 | 83.2 | 5.99 | Tight High-Spin Breakers |
| 146 | Vitas, Ben | JOL_SLA | Slider | 88 | 28.5 | 0.318 | 0.8 | -5.3 | 2112 | 80.8 | 4.93 | Tight High-Spin Breakers |
| 147 | Eldred, Zach | NEW_ENG23 | Slider | 84 | 24.0 | 0.360 | 2.2 | -7.7 | 2444 | 82.2 | 5.76 | Tight High-Spin Breakers |
| 148 | Johnston, Spencer | DOW_EAS1 | Curveball | 60 | 20.2 | 0.357 | -4.2 | -5.5 | 2129 | 74.5 | 5.71 | Tight High-Spin Breakers |
| 149 | Westcott, Zac | FLO_Y'A | Curveball | 127 | 20.0 | 0.398 | -15.1 | -9.5 | 1870 | 67.1 | 5.48 | Tight High-Spin Breakers |
| 150 | Escobar, Anthony | TRO_AIG | Changeup | 82 | 77.2 | 0.123 | 10.0 | 11.5 | 1579 | 79.5 | 6.26 | Soft-Speed Separation |
| 151 | Vitas, Ben | JOL_SLA | Splitter | 59 | 75.0 | 0.171 | 2.2 | 7.9 | 1048 | 81.6 | 5.04 | Soft-Speed Separation |
| 152 | McEvoy, Aidan | FLO_Y'A | Slider | 78 | 74.6 | 0.142 | 6.7 | 10.2 | 2207 | 78.8 | 6.10 | Soft-Speed Separation |
| 153 | Webster, Evan | FLO_Y'A | Slider | 52 | 71.9 | 0.150 | 1.2 | 2.3 | 1931 | 79.3 | 6.83 | Soft-Speed Separation |
| 154 | Garcia, Hector | WAS_WIL3 | Splitter | 62 | 71.8 | 0.185 | 11.7 | 7.6 | 1216 | 78.2 | 5.92 | Soft-Speed Separation |
| 155 | Willeman, Landon | EVA_OTT | Changeup | 112 | 68.7 | 0.160 | 6.8 | 14.0 | 1723 | 84.4 | 6.23 | Soft-Speed Separation |
| 156 | Sechrist, Zander | WAS_WIL3 | Curveball | 61 | 68.4 | 0.172 | -0.4 | 9.5 | 1806 | 66.5 | 4.90 | Soft-Speed Separation |
| 157 | Rodriguez, Joe Joe | NEW_JER6 | Changeup | 59 | 68.3 | 0.132 | 8.9 | 14.5 | 1793 | 81.2 | 5.40 | Soft-Speed Separation |
| 158 | Maietta, Dante | WIN_CIT29 | Changeup | 112 | 67.3 | 0.151 | 15.5 | 14.9 | 1846 | 77.1 | 6.33 | Soft-Speed Separation |
| 159 | Boies, Emiles | QUE_CAP | Changeup | 122 | 66.8 | 0.170 | 11.6 | 14.8 | 1885 | 82.5 | 6.31 | Soft-Speed Separation |
| 160 | Wiltse, Ryan | EVA_OTT | Changeup | 107 | 66.0 | 0.187 | 14.0 | 10.2 | 1832 | 78.7 | 6.40 | Soft-Speed Separation |
| 161 | Moreno, Jose | DOW_EAS1 | Changeup | 52 | 65.5 | 0.174 | 6.8 | 11.6 | 1752 | 81.2 | 5.65 | Soft-Speed Separation |
| 162 | Villers, Ian | QUE_CAP | Splitter | 64 | 64.3 | 0.219 | 7.5 | 11.5 | 1086 | 83.1 | 5.98 | Soft-Speed Separation |
| 163 | Pindel, Buddie | SCH_BOO | Splitter | 80 | 63.6 | 0.222 | 4.8 | 7.3 | 1095 | 80.3 | 5.79 | Soft-Speed Separation |
| 164 | Cooper, Garrett | NEW_YOR13 | Changeup | 109 | 61.7 | 0.222 | 8.5 | 6.7 | 1449 | 78.1 | 6.24 | Soft-Speed Separation |
| 165 | Thompson, Ross | SCH_BOO | Splitter | 78 | 59.8 | 0.199 | 4.4 | 9.4 | 1066 | 79.6 | 5.41 | Soft-Speed Separation |
| 166 | VanMarter, Luke | LEM_COL | Changeup | 53 | 58.5 | 0.253 | 12.9 | 11.7 | 1756 | 77.6 | 6.55 | Soft-Speed Separation |
| 167 | Duby, Bill | NEW_JER6 | Slider | 55 | 58.3 | 0.204 | 8.1 | 0.4 | 2027 | 79.7 | 6.65 | Soft-Speed Separation |
| 168 | Pindel, Buddie | SCH_BOO | Changeup | 88 | 57.9 | 0.219 | 3.7 | 11.5 | 1359 | 80.6 | 5.51 | Soft-Speed Separation |
| 169 | Salata, Derek | SCH_BOO | Splitter | 65 | 57.6 | 0.179 | 6.5 | 8.9 | 1104 | 83.0 | 5.92 | Soft-Speed Separation |
| 170 | Cameron, Zach | WIN_CIT29 | Changeup | 111 | 56.9 | 0.215 | 6.9 | 20.3 | 2068 | 80.1 | 5.61 | Soft-Speed Separation |
| 171 | Dima, Josh | GAT_GRI | Slider | 97 | 56.3 | 0.213 | 2.4 | 1.8 | 1936 | 82.1 | 5.99 | Soft-Speed Separation |
| 172 | Johnston, Spencer | DOW_EAS1 | Slider | 171 | 56.1 | 0.204 | 6.6 | 1.0 | 2086 | 78.4 | 5.97 | Soft-Speed Separation |
| 173 | Dill, Austin | TRI_VAL | Changeup | 184 | 55.4 | 0.218 | 10.7 | 16.9 | 1930 | 80.4 | 5.24 | Soft-Speed Separation |
| 174 | Sakurai, Masatoshi | QUE_CAP | Changeup | 103 | 54.2 | 0.250 | 8.6 | -5.5 | 1452 | 80.2 | 6.02 | Soft-Speed Separation |
| 175 | Nabholz, Nate | TRI_VAL | Slider | 98 | 54.1 | 0.219 | 6.4 | -1.6 | 1992 | 83.4 | 5.68 | Soft-Speed Separation |
| 176 | Roland, Cole | QUE_CAP | Changeup | 71 | 54.0 | 0.244 | 10.4 | 9.6 | 2033 | 82.6 | 5.56 | Soft-Speed Separation |
| 177 | DeCastro, Justin | LON_ISL22 | Changeup | 122 | 53.8 | 0.236 | 9.6 | 18.6 | 1979 | 79.4 | 5.06 | Soft-Speed Separation |
| 178 | Thompson, Ross | SCH_BOO | Changeup | 82 | 53.0 | 0.234 | 5.3 | 9.1 | 1084 | 79.6 | 5.66 | Soft-Speed Separation |
| 179 | Kirby, Zach | WAS_WIL3 | Changeup | 117 | 52.2 | 0.217 | 10.1 | 15.4 | 1694 | 79.9 | 6.07 | Soft-Speed Separation |
| 180 | Hopewell, Chase | FLO_Y'A | Slider | 72 | 51.8 | 0.244 | -0.2 | -2.0 | 1983 | 81.4 | 6.10 | Soft-Speed Separation |
| 181 | Toribio, Noe | TRO_AIG | Changeup | 147 | 51.6 | 0.256 | 6.3 | 16.7 | 2013 | 82.8 | 5.51 | Soft-Speed Separation |
| 182 | Vailes, Gage | GAT_GRI | Changeup | 84 | 51.1 | 0.248 | 6.1 | 10.5 | 1882 | 85.0 | 5.22 | Soft-Speed Separation |
| 183 | Turner, Eric | JOL_SLA | Changeup | 98 | 51.0 | 0.256 | 4.3 | 15.6 | 1650 | 80.0 | 5.16 | Soft-Speed Separation |
| 184 | Henderson, Drew | DOW_EAS1 | Changeup | 91 | 50.9 | 0.244 | 9.1 | 13.9 | 1622 | 81.7 | 5.88 | Soft-Speed Separation |
| 185 | Johnston, Spencer | DOW_EAS1 | Changeup | 259 | 50.4 | 0.243 | 9.1 | 10.0 | 1668 | 78.1 | 5.93 | Soft-Speed Separation |
| 186 | Hampton, Ky | OTT_TIT | Changeup | 105 | 50.4 | 0.252 | 2.6 | 15.7 | 1706 | 83.9 | 6.19 | Soft-Speed Separation |
| 187 | Aldeano, Austin | TRO_AIG | Changeup | 51 | 49.5 | 0.245 | 7.1 | 17.6 | 1856 | 81.3 | 6.28 | Soft-Speed Separation |
| 188 | Burcham, Jacob | GAT_GRI | Changeup | 63 | 49.3 | 0.236 | 4.3 | 17.8 | 1900 | 83.7 | 6.22 | Soft-Speed Separation |
| 189 | Miranda, Kevin | OTT_TIT | Changeup | 82 | 49.2 | 0.251 | 9.8 | 12.7 | 1444 | 79.5 | 6.06 | Soft-Speed Separation |
| 190 | Barker, Alex | NEW_YOR13 | Changeup | 65 | 48.5 | 0.291 | 6.1 | -12.2 | 1491 | 82.3 | 6.34 | Soft-Speed Separation |
| 191 | Daly, Ryan | JOL_SLA | Changeup | 135 | 47.9 | 0.272 | 5.0 | 16.2 | 2076 | 78.9 | 6.89 | Soft-Speed Separation |
| 192 | Primeaux, Parker | SUS_COU1 | Changeup | 85 | 47.4 | 0.268 | 0.8 | 17.5 | 2012 | 86.0 | 5.55 | Soft-Speed Separation |
| 193 | Andueza, Axel | DOW_EAS1 | Changeup | 54 | 47.3 | 0.243 | 6.3 | 11.2 | 2003 | 82.8 | 5.15 | Soft-Speed Separation |
| 194 | Villalobos, Jonaiker | FLO_Y'A | Changeup | 124 | 46.8 | 0.250 | 8.0 | -13.1 | 1585 | 80.4 | 5.90 | Soft-Speed Separation |
| 195 | Delongchamp, Luke | TRI_VAL | Changeup | 100 | 46.7 | 0.252 | 7.4 | 16.2 | 1808 | 81.9 | 5.59 | Soft-Speed Separation |
| 196 | Heredia-Bustos, Rolando | DOW_EAS1 | Changeup | 162 | 46.7 | 0.272 | 8.8 | 18.1 | 2087 | 79.5 | 5.81 | Soft-Speed Separation |
| 197 | Harris, Ben | GAT_GRI | Changeup | 179 | 46.4 | 0.256 | 8.6 | 16.0 | 1791 | 83.3 | 5.65 | Soft-Speed Separation |
| 198 | Bell, Brendan | NEW_ENG23 | Changeup | 55 | 46.4 | 0.218 | 7.3 | 15.6 | 1950 | 82.7 | 5.14 | Soft-Speed Separation |
| 199 | Nakata, Yuto | QUE_CAP | Splitter | 66 | 46.3 | 0.258 | 3.0 | 6.7 | 989 | 83.6 | 5.63 | Soft-Speed Separation |
| 200 | Sechrist, Zander | WAS_WIL3 | Changeup | 136 | 45.7 | 0.270 | 8.0 | -15.4 | 1696 | 76.9 | 5.61 | Soft-Speed Separation |
| 201 | Galva, Claudio | GAT_GRI | Changeup | 54 | 45.6 | 0.268 | 3.7 | -12.6 | 1525 | 84.0 | 4.89 | Soft-Speed Separation |
| 202 | Chapple, Bronson | TRO_AIG | Changeup | 51 | 45.6 | 0.284 | 3.7 | 14.5 | 1828 | 83.2 | 6.34 | Soft-Speed Separation |
| 203 | Matos, Dwayne | OTT_TIT | Slider | 80 | 45.5 | 0.245 | 4.4 | -1.0 | 2018 | 81.1 | 6.02 | Soft-Speed Separation |
| 204 | Gollert, Harley | QUE_CAP | Changeup | 52 | 44.7 | 0.254 | 10.2 | -8.4 | 1676 | 81.0 | 5.46 | Soft-Speed Separation |
| 205 | Moore, Kyle | SCH_BOO | Changeup | 73 | 44.0 | 0.268 | 9.5 | 16.4 | 2037 | 82.9 | 4.73 | Soft-Speed Separation |
| 206 | Brothers, Kellen | SUS_COU1 | Changeup | 50 | 43.8 | 0.252 | 11.7 | 12.4 | 1559 | 80.0 | 6.25 | Soft-Speed Separation |
| 207 | Barreto, Brayhans | TRI_VAL | Slider | 51 | 43.6 | 0.289 | 4.8 | -0.7 | 1873 | 80.2 | 6.10 | Soft-Speed Separation |
| 208 | Hernandez, Nyan | NEW_JER6 | Changeup | 114 | 43.1 | 0.268 | 12.0 | 15.7 | 1914 | 82.2 | 6.47 | Soft-Speed Separation |
| 209 | Noble, Nick | FDU_KNI | Changeup | 71 | 43.1 | 0.302 | 0.2 | 17.6 | 1612 | 77.3 | 5.00 | Soft-Speed Separation |
| 210 | Matos, Dwayne | OTT_TIT | Changeup | 188 | 42.8 | 0.256 | 3.5 | 16.1 | 1517 | 83.6 | 6.36 | Soft-Speed Separation |
| 211 | Delongchamp, Luke | TRI_VAL | Sinker | 50 | 42.7 | 0.275 | 9.4 | 17.0 | 1954 | 86.8 | 5.54 | Soft-Speed Separation |
| 212 | Kaftan, Eddie | FLO_Y'A | Sinker | 128 | 42.2 | 0.263 | 7.4 | 13.6 | 2035 | 86.0 | 5.43 | Soft-Speed Separation |
| 213 | Simone, Andrew | TRO_AIG | Changeup | 57 | 42.1 | 0.275 | 10.4 | 12.6 | 1683 | 84.9 | 5.91 | Soft-Speed Separation |
| 214 | Wehrle, Tyler | WIN_CIT29 | Changeup | 61 | 42.1 | 0.265 | 6.4 | 15.6 | 1888 | 84.1 | 5.61 | Soft-Speed Separation |
| 215 | Trizuto, Colin | WAG_SEA | Changeup | 69 | 41.7 | 0.270 | 7.0 | 18.5 | 1961 | 84.0 | 5.35 | Soft-Speed Separation |
| 216 | Long, Jalon | NEW_YOR13 | Changeup | 50 | 40.7 | 0.295 | 7.0 | 14.3 | 1541 | 82.9 | 6.31 | Soft-Speed Separation |
| 217 | Cook, Cole | SCH_BOO | Changeup | 112 | 40.4 | 0.272 | 8.2 | -8.4 | 1798 | 80.3 | 5.52 | Soft-Speed Separation |
| 218 | Scott, Brandon | LAK_ERI24 | Changeup | 143 | 39.6 | 0.303 | 2.0 | -12.3 | 1486 | 81.6 | 5.90 | Soft-Speed Separation |
| 219 | Sabatine, Gino | TRI_VAL | Changeup | 269 | 38.2 | 0.300 | 8.3 | 15.5 | 1783 | 85.1 | 5.06 | Soft-Speed Separation |
| 220 | Thornton, Tyler | NEW_ENG23 | Changeup | 65 | 37.6 | 0.288 | 9.2 | 13.7 | 1799 | 82.9 | 4.55 | Soft-Speed Separation |
| 221 | Westcott, Zac | FLO_Y'A | Changeup | 123 | 36.0 | 0.288 | 4.9 | 16.4 | 1891 | 75.1 | 5.74 | Soft-Speed Separation |
| 222 | Simpson, Garret | EVA_OTT | Changeup | 61 | 35.2 | 0.351 | 3.9 | 9.9 | 1781 | 83.9 | 5.19 | Soft-Speed Separation |
| 223 | Belton, Hunter | MIS_MUD | Changeup | 55 | 34.1 | 0.334 | 11.4 | 13.9 | 2006 | 81.0 | 6.10 | Soft-Speed Separation |
| 224 | Thornton, Tyler | NEW_ENG23 | Sinker | 73 | 30.2 | 0.341 | 10.2 | 15.9 | 1985 | 84.6 | 5.53 | Soft-Speed Separation |
| 225 | Smith, Ethan | WIN_CIT29 | Changeup | 52 | 29.2 | 0.319 | 9.1 | 14.6 | 2000 | 82.7 | 6.38 | Soft-Speed Separation |
| 226 | Duby, Bill | NEW_JER6 | Changeup | 133 | 28.4 | 0.306 | 11.4 | 13.3 | 1928 | 83.7 | 6.70 | Soft-Speed Separation |

## Undervalued Movement Pitches

Definition: movement quality percentile at least 75, with Pitch Value Score at or below league average.

| Rank | Pitcher | Team | Pitch | Pitches | PVS | xwOBA | IVB | HB | Spin | Velo | Ext | Archetype |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | Westcott, Zac | FLO_Y'A | Curveball | 127 | 20.0 | 0.398 | -15.1 | -9.5 | 1870 | 67.1 | 5.48 | Tight High-Spin Breakers |
| 2 | Huter, Blayne | SUS_COU1 | Curveball | 103 | 45.3 | 0.273 | -5.1 | -14.2 | 2137 | 73.7 | 6.01 | Tight High-Spin Breakers |
| 3 | Foster, Kobe | WAS_WIL3 | Curveball | 99 | 47.0 | 0.272 | -8.0 | 15.4 | 2246 | 67.8 | 5.41 | Tight High-Spin Breakers |
| 4 | Allemann, Braeden | QUE_CAP | Curveball | 146 | 47.8 | 0.251 | -7.2 | -15.6 | 2185 | 76.7 | 6.17 | Tight High-Spin Breakers |
| 5 | Kassebaum, Torin | LON_ISL22 | Curveball | 55 | 41.1 | 0.307 | 1.1 | 10.2 | 2155 | 71.6 | 5.31 | Tight High-Spin Breakers |
| 6 | Johnston, Spencer | DOW_EAS1 | Curveball | 60 | 20.2 | 0.357 | -4.2 | -5.5 | 2129 | 74.5 | 5.71 | Tight High-Spin Breakers |
| 7 | Campbell, Tyler | MIS_MUD | Slider | 71 | 47.1 | 0.271 | 8.0 | 5.4 | 2236 | 74.0 | 5.57 | Tight High-Spin Breakers |
| 8 | Bice, Emmett | NEW_YOR13 | Curveball | 87 | 41.1 | 0.317 | -10.1 | -13.8 | 2963 | 79.2 | 5.65 | Tight High-Spin Breakers |
| 9 | Baker, Luke | EVA_OTT | Curveball | 59 | 48.2 | 0.246 | -7.4 | 9.7 | 2694 | 75.5 | 5.51 | Tight High-Spin Breakers |
| 10 | Kaftan, Eddie | FLO_Y'A | Slider | 62 | 48.4 | 0.233 | 1.1 | -6.3 | 2437 | 77.1 | 4.72 | Tight High-Spin Breakers |
| 11 | Villalobos, Jonaiker | FLO_Y'A | Curveball | 90 | 37.8 | 0.282 | -5.2 | 5.5 | 2262 | 74.8 | 5.36 | Tight High-Spin Breakers |
| 12 | Martzolf, Max | OTT_TIT | Curveball | 71 | 44.2 | 0.292 | -4.2 | 11.1 | 2155 | 73.9 | 5.43 | Tight High-Spin Breakers |
| 13 | Salata, Derek | SCH_BOO | Slider | 108 | 38.7 | 0.307 | 2.5 | -10.7 | 2567 | 80.5 | 5.63 | Tight High-Spin Breakers |
| 14 | Williams, Pierce | NEW_ENG23 | Curveball | 120 | 41.1 | 0.273 | -5.9 | 6.7 | 2174 | 75.4 | 5.74 | Tight High-Spin Breakers |
| 15 | Moore, Kyle | SCH_BOO | Curveball | 85 | 46.9 | 0.265 | -8.9 | -8.6 | 2532 | 76.8 | 4.14 | Tight High-Spin Breakers |
| 16 | Sparks, Alec | GAT_GRI | Slider | 108 | 49.2 | 0.245 | 0.5 | -7.0 | 2625 | 80.1 | 5.48 | Tight High-Spin Breakers |
| 17 | Figueredo, Kevin | WIN_CIT29 | Curveball | 78 | 45.1 | 0.277 | -3.5 | 4.9 | 2324 | 75.8 | 5.00 | Tight High-Spin Breakers |
| 18 | Misla, Luis | TRI_VAL | Curveball | 82 | 43.9 | 0.259 | -6.3 | 9.7 | 2805 | 76.9 | 5.11 | Tight High-Spin Breakers |
| 19 | Eisenbarger, Jack | QUE_CAP | Changeup | 69 | 30.6 | 0.313 | 14.9 | -13.6 | 2297 | 78.8 | 6.23 | Riding Shape / Lower Velo |
| 20 | Turner, Eric | JOL_SLA | Slider | 118 | 46.9 | 0.259 | 1.4 | -7.1 | 2341 | 78.6 | 4.95 | Tight High-Spin Breakers |
| 21 | Willeman, Landon | EVA_OTT | Curveball | 66 | 46.1 | 0.289 | -7.4 | -10.1 | 2132 | 78.1 | 5.28 | Tight High-Spin Breakers |
| 22 | Campbell, AJ | WIN_CIT29 | Slider | 162 | 48.3 | 0.253 | 4.7 | -10.1 | 2556 | 80.2 | 4.92 | Tight High-Spin Breakers |
| 23 | Forsyth, Braden | MIS_MUD | Slider | 97 | 49.6 | 0.269 | 4.1 | -6.4 | 2352 | 80.7 | 6.05 | Tight High-Spin Breakers |
| 24 | Sechrist, Zander | WAS_WIL3 | Changeup | 136 | 45.7 | 0.270 | 8.0 | -15.4 | 1696 | 76.9 | 5.61 | Soft-Speed Separation |
| 25 | Smith, Ethan | WIN_CIT29 | Slider | 58 | 48.5 | 0.282 | -0.2 | -6.4 | 2423 | 80.6 | 5.91 | Tight High-Spin Breakers |
| 26 | Helt, Robert | LAK_ERI24 | Slider | 120 | 46.9 | 0.263 | -1.4 | -5.9 | 2406 | 80.6 | 5.90 | Tight High-Spin Breakers |
| 27 | Scott, Brandon | LAK_ERI24 | Slider | 90 | 42.8 | 0.266 | -0.4 | 8.0 | 2450 | 77.9 | 5.53 | Tight High-Spin Breakers |
| 28 | Sakurai, Masatoshi | QUE_CAP | Curveball | 89 | 39.6 | 0.301 | -3.9 | 5.7 | 2472 | 78.2 | 5.61 | Tight High-Spin Breakers |
| 29 | Godwin, Connor | NEW_YOR13 | Slider | 93 | 44.3 | 0.262 | 0.0 | -10.2 | 2535 | 82.4 | 6.11 | Tight High-Spin Breakers |
| 30 | Burcham, Jacob | GAT_GRI | Slider | 64 | 46.1 | 0.229 | 0.1 | -8.0 | 2376 | 81.6 | 5.90 | Tight High-Spin Breakers |

## Top 20 Scouting Reports

1. **Grounds, Jackson, DOW_EAS1 Curveball** (Tight High-Spin Breakers): PVS 80.0, xwOBA 0.104. Shape: IVB -10.5, HB -12.0, 81.4 mph, 1946 rpm, 5.35 ft extension. Scouting read: low ride/drop, big horizontal; current results place it #1 overall and #1 within its pitch type.
2. **Carroll, Jake, JOL_SLA Slider** (Tight High-Spin Breakers): PVS 80.0, xwOBA 0.204. Shape: IVB -6.4, HB 7.7, 75.2 mph, 2019 rpm, 6.09 ft extension. Scouting read: low ride/drop, soft velo; current results place it #2 overall and #1 within its pitch type.
3. **Harper, Scott, NEW_YOR13 Slider** (Tight High-Spin Breakers): PVS 77.6, xwOBA 0.133. Shape: IVB 3.2, HB -16.4, 79.8 mph, 2650 rpm, 5.70 ft extension. Scouting read: big horizontal, high spin, soft velo; current results place it #3 overall and #2 within its pitch type.
4. **Escobar, Anthony, TRO_AIG Changeup** (Soft-Speed Separation): PVS 77.2, xwOBA 0.123. Shape: IVB 10.0, HB 11.5, 79.5 mph, 1579 rpm, 6.26 ft extension. Scouting read: big horizontal, soft velo, extension; current results place it #4 overall and #1 within its pitch type.
5. **Ryan, Dillon, NEW_ENG23 Slider** (Tight High-Spin Breakers): PVS 76.3, xwOBA 0.154. Shape: IVB -2.3, HB -8.2, 85.4 mph, 2494 rpm, 5.85 ft extension. Scouting read: low ride/drop, high spin; current results place it #5 overall and #3 within its pitch type.
6. **Webster, Evan, FLO_Y'A Cutter** (Riding Shape / Lower Velo): PVS 75.4, xwOBA 0.136. Shape: IVB 5.6, HB -0.2, 84.3 mph, 2064 rpm, 6.96 ft extension. Scouting read: extension; current results place it #6 overall and #1 within its pitch type.
7. **Vitas, Ben, JOL_SLA Splitter** (Soft-Speed Separation): PVS 75.0, xwOBA 0.171. Shape: IVB 2.2, HB 7.9, 81.6 mph, 1048 rpm, 5.04 ft extension. Scouting read: low ride/drop; current results place it #7 overall and #1 within its pitch type.
8. **McEvoy, Aidan, FLO_Y'A Slider** (Soft-Speed Separation): PVS 74.6, xwOBA 0.142. Shape: IVB 6.7, HB 10.2, 78.8 mph, 2207 rpm, 6.10 ft extension. Scouting read: big horizontal, soft velo; current results place it #8 overall and #4 within its pitch type.
9. **Alpern, Liam, FLO_Y'A Slider** (Tight High-Spin Breakers): PVS 74.3, xwOBA 0.113. Shape: IVB -4.0, HB 11.5, 76.8 mph, 2219 rpm, 5.55 ft extension. Scouting read: low ride/drop, big horizontal, soft velo; current results place it #9 overall and #5 within its pitch type.
10. **Correa, Nelvin, QUE_CAP Cutter** (Riding Shape / Lower Velo): PVS 74.2, xwOBA 0.137. Shape: IVB 12.4, HB -0.7, 87.0 mph, 2250 rpm, 5.98 ft extension. Scouting read: average movement blend; current results place it #10 overall and #2 within its pitch type.
11. **Foster, Kobe, WAS_WIL3 Slider** (Tight High-Spin Breakers): PVS 73.0, xwOBA 0.133. Shape: IVB 5.0, HB 6.2, 78.1 mph, 2332 rpm, 5.38 ft extension. Scouting read: high spin, soft velo; current results place it #11 overall and #6 within its pitch type.
12. **Jones, Logan, TRI_VAL Slider** (Tight High-Spin Breakers): PVS 72.7, xwOBA 0.189. Shape: IVB 2.5, HB 2.3, 83.5 mph, 2341 rpm, 5.69 ft extension. Scouting read: low ride/drop, high spin; current results place it #12 overall and #7 within its pitch type.
13. **Davis, Tyler, WIN_CIT29 Four-Seam** (Arm-Side Run Power): PVS 72.5, xwOBA 0.110. Shape: IVB 21.2, HB 5.6, 89.3 mph, 2171 rpm, 5.86 ft extension. Scouting read: plus ride, power velocity; current results place it #13 overall and #1 within its pitch type.
14. **Grounds, Jackson, DOW_EAS1 Four-Seam** (Arm-Side Run Power): PVS 72.4, xwOBA 0.156. Shape: IVB 17.0, HB 14.2, 92.5 mph, 2163 rpm, 5.59 ft extension. Scouting read: plus ride, big horizontal, power velocity; current results place it #14 overall and #2 within its pitch type.
15. **Perez, Kelvin, WAS_WIL3 Slider** (Tight High-Spin Breakers): PVS 72.4, xwOBA 0.127. Shape: IVB 3.7, HB -5.7, 81.3 mph, 2239 rpm, 5.81 ft extension. Scouting read: average movement blend; current results place it #15 overall and #8 within its pitch type.
16. **Webster, Evan, FLO_Y'A Slider** (Soft-Speed Separation): PVS 71.9, xwOBA 0.150. Shape: IVB 1.2, HB 2.3, 79.3 mph, 1931 rpm, 6.83 ft extension. Scouting read: low ride/drop, soft velo, extension; current results place it #16 overall and #9 within its pitch type.
17. **Bargo, Casey, NEW_ENG23 Slider** (Tight High-Spin Breakers): PVS 71.8, xwOBA 0.177. Shape: IVB 1.5, HB -5.0, 83.6 mph, 2416 rpm, 5.66 ft extension. Scouting read: low ride/drop, high spin; current results place it #17 overall and #10 within its pitch type.
18. **Garcia, Hector, WAS_WIL3 Splitter** (Soft-Speed Separation): PVS 71.8, xwOBA 0.185. Shape: IVB 11.7, HB 7.6, 78.2 mph, 1216 rpm, 5.92 ft extension. Scouting read: soft velo; current results place it #18 overall and #2 within its pitch type.
19. **Peyton, Blake, GAT_GRI Changeup** (Riding Shape / Lower Velo): PVS 71.7, xwOBA 0.149. Shape: IVB 11.4, HB -14.7, 81.1 mph, 1885 rpm, 6.20 ft extension. Scouting read: big horizontal, extension; current results place it #19 overall and #2 within its pitch type.
20. **Hensey, Rob, SUS_COU1 Changeup** (Riding Shape / Lower Velo): PVS 69.6, xwOBA 0.169. Shape: IVB 7.1, HB -16.5, 84.2 mph, 1717 rpm, 6.27 ft extension. Scouting read: big horizontal, extension; current results place it #20 overall and #3 within its pitch type.

## Plots

- `plots\pitch_movement_archetypes\cluster_count_selection.png`
- `plots\pitch_movement_archetypes\archetypes_hb_ivb.png`
- `plots\pitch_movement_archetypes\archetypes_velocity_spin.png`
- `plots\pitch_movement_archetypes\archetypes_pca.png`
- `plots\pitch_movement_archetypes\archetype_pitch_value.png`