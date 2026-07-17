# Frontier League Movement Archetypes

- Input file: `data\processed\movement_score_inputs.csv`
- Scored output: `data\processed\pitch_movement_archetypes.csv`
- Cluster summary: `data\processed\pitch_movement_archetype_summary.csv`
- Highest-performing archetype pitch list: `data\processed\highest_performing_archetype_pitches.csv`
- Undervalued pitch list: `data\processed\undervalued_movement_pitches.csv`
- Qualified pitcher-pitch types clustered: 853
- Features clustered: IVB, HB, spin rate, velocity, extension
- Selected cluster count: 2
- Full methodology write-up: `reports/FRONTIER_PITCH_VALUE_METHODOLOGY.md`

## How To Read This Report

Higher Pitch Value Score is better. It means the pitch has the outcome profile associated with lower expected xwOBA damage. Archetypes are movement-shape groups, not direct pitcher grades.

The cluster labels describe the average movement identity of each group. Average Pitch Value Score by cluster tells us which movement families performed best in this dataset, but individual pitches within a cluster can still vary widely based on command, usage, sequencing, and sample size.

## Cluster Count Test

| k | Inertia | Silhouette |
|---:|---:|---:|
| 2 | 2911.29 | 0.3043 **selected** |
| 3 | 2342.25 | 0.3032 |
| 4 | 1938.55 | 0.3026 |
| 5 | 1764.02 | 0.2517 |
| 6 | 1604.19 | 0.2314 |
| 7 | 1474.53 | 0.2357 |
| 8 | 1377.79 | 0.2392 |
| 9 | 1281.16 | 0.2498 |
| 10 | 1190.98 | 0.2586 |

## Archetype Summary

| Rank | Archetype | Pitches | Instances | Avg PVS | Avg xwOBA | IVB | HB | Spin | Velo | Ext | Common Pitch Types |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|
| 1 | `Tight High-Spin Breakers` | 43,232 | 343 | 52.3 | 0.239 | 0.9 | -3.3 | 2252 | 80.1 | 5.50 | Slider, Curveball, Changeup |
| 2 | `Soft-Speed Separation` | 82,261 | 510 | 48.4 | 0.245 | 13.0 | 6.5 | 2099 | 88.3 | 5.97 | Four-Seam, Sinker, Changeup |

## Highest-Performing Archetypes

- `Tight High-Spin Breakers`: average PVS 52.3, avg xwOBA 0.239, typical shape 0.9 IVB / -3.3 HB at 80.1 mph.
- `Soft-Speed Separation`: average PVS 48.4, avg xwOBA 0.245, typical shape 13.0 IVB / 6.5 HB at 88.3 mph.

## Pitchers in Highest-Performing Archetypes

| Rank | Pitcher | Team | Pitch | Pitches | PVS | xwOBA | IVB | HB | Spin | Velo | Ext | Archetype |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | Grounds, Jackson | DOW_EAS1 | Curveball | 82 | 80.0 | 0.108 | -10.5 | -12.0 | 1946 | 81.4 | 5.35 | Tight High-Spin Breakers |
| 2 | Carroll, Jake | JOL_SLA | Slider | 68 | 80.0 | 0.190 | -6.2 | 7.9 | 2033 | 75.3 | 6.10 | Tight High-Spin Breakers |
| 3 | Morgan, Cooper | QUE_CAP | Curveball | 72 | 80.0 | 0.146 | -1.5 | 17.6 | 2685 | 75.6 | 5.25 | Tight High-Spin Breakers |
| 4 | Ryan, Dillon | NEW_ENG23 | Slider | 125 | 79.9 | 0.144 | -2.0 | -8.1 | 2494 | 85.4 | 5.82 | Tight High-Spin Breakers |
| 5 | Leduc, Zachary | TRO_AIG | Slider | 78 | 79.2 | 0.092 | 1.5 | -4.5 | 2118 | 83.4 | 6.15 | Tight High-Spin Breakers |
| 6 | Zentko, Dylan | EVA_OTT | Changeup | 67 | 78.6 | 0.155 | 7.3 | -11.4 | 1311 | 78.8 | 5.82 | Tight High-Spin Breakers |
| 7 | Vecerka, Boris | QUE_CAP | Slider | 74 | 77.6 | 0.129 | 2.4 | -11.9 | 2472 | 82.5 | 5.61 | Tight High-Spin Breakers |
| 8 | Peyton, Blake | GAT_GRI | Changeup | 93 | 77.3 | 0.141 | 10.3 | -13.2 | 1927 | 81.0 | 6.10 | Tight High-Spin Breakers |
| 9 | Alpern, Liam | FLO_Y'A | Slider | 78 | 76.4 | 0.113 | -4.0 | 11.5 | 2219 | 76.8 | 5.55 | Tight High-Spin Breakers |
| 10 | Jones, Logan | TRI_VAL | Slider | 65 | 74.7 | 0.191 | 2.5 | 2.3 | 2341 | 83.5 | 5.69 | Tight High-Spin Breakers |
| 11 | Bargo, Casey | NEW_ENG23 | Slider | 56 | 73.6 | 0.176 | 1.5 | -5.0 | 2416 | 83.6 | 5.66 | Tight High-Spin Breakers |
| 12 | Hickey, Matt | GAT_GRI | Slider | 86 | 73.5 | 0.191 | -1.7 | -6.5 | 2258 | 79.9 | 5.34 | Tight High-Spin Breakers |
| 13 | Harper, Scott | NEW_YOR13 | Slider | 212 | 72.6 | 0.155 | 3.3 | -16.6 | 2665 | 79.8 | 5.58 | Tight High-Spin Breakers |
| 14 | Bohnert, Matthew | WIN_CIT29 | Curveball | 97 | 71.9 | 0.143 | -16.3 | 13.3 | 2812 | 78.3 | 4.79 | Tight High-Spin Breakers |
| 15 | Kirby, Zach | WAS_WIL3 | Slider | 127 | 71.7 | 0.156 | 5.8 | -13.4 | 2204 | 78.0 | 5.68 | Tight High-Spin Breakers |
| 16 | Moore, Kyle | SCH_BOO | Slider | 53 | 71.2 | 0.177 | 8.8 | -1.2 | 2162 | 84.1 | 4.87 | Tight High-Spin Breakers |
| 17 | Nakata, Yuto | QUE_CAP | Slider | 97 | 70.5 | 0.155 | 4.1 | -7.8 | 2417 | 81.7 | 5.59 | Tight High-Spin Breakers |
| 18 | McEvoy, Aidan | FLO_Y'A | Slider | 107 | 70.5 | 0.157 | 6.7 | 10.2 | 2220 | 78.8 | 6.03 | Tight High-Spin Breakers |
| 19 | Donnan, Blake | FLO_Y'A | Slider | 65 | 70.1 | 0.186 | 5.0 | -7.3 | 2367 | 80.5 | 5.42 | Tight High-Spin Breakers |
| 20 | Townes, Holland | SCH_BOO | Curveball | 82 | 68.7 | 0.189 | -9.4 | -13.5 | 2306 | 78.1 | 4.96 | Tight High-Spin Breakers |
| 21 | Parsons, Billy | SUS_COU1 | Changeup | 61 | 68.5 | 0.234 | 1.7 | 7.8 | 1428 | 80.9 | 5.49 | Tight High-Spin Breakers |
| 22 | Jones, Logan | FLO_Y'A | Slider | 51 | 68.5 | 0.179 | -1.4 | -0.1 | 2446 | 81.5 | 5.66 | Tight High-Spin Breakers |
| 23 | Jones, Breyln | NEW_JER6 | Curveball | 54 | 68.0 | 0.186 | -16.8 | -9.6 | 2166 | 74.1 | 5.56 | Tight High-Spin Breakers |
| 24 | Smith, Ben | NEW_ENG23 | Changeup | 56 | 67.6 | 0.152 | 4.4 | -14.1 | 1591 | 82.6 | 6.12 | Tight High-Spin Breakers |
| 25 | Garcia, Brett | OTT_TIT | Curveball | 115 | 67.4 | 0.175 | -17.1 | -8.2 | 2144 | 81.3 | 5.37 | Tight High-Spin Breakers |
| 26 | Vega, Lucas | TRO_AIG | Slider | 134 | 66.7 | 0.156 | 6.6 | -9.3 | 2697 | 79.2 | 5.94 | Tight High-Spin Breakers |
| 27 | Gregory, Ben | GAT_GRI | Curveball | 53 | 66.7 | 0.227 | -7.0 | -5.7 | 2309 | 78.0 | 6.13 | Tight High-Spin Breakers |
| 28 | Messina, Chris | FDU_KNI | Changeup | 68 | 66.5 | 0.254 | 11.9 | -18.0 | 1836 | 79.8 | 5.18 | Tight High-Spin Breakers |
| 29 | Balzan, Jackson | SUS_COU1 | Slider | 91 | 66.5 | 0.187 | 5.8 | 0.8 | 2187 | 79.7 | 5.26 | Tight High-Spin Breakers |
| 30 | Salata, Derek | SCH_BOO | Curveball | 122 | 66.5 | 0.196 | -13.0 | -13.3 | 2670 | 74.3 | 5.49 | Tight High-Spin Breakers |
| 31 | Binns, Malik | NEW_JER6 | Curveball | 55 | 66.3 | 0.185 | -7.6 | -16.2 | 2448 | 74.8 | 5.95 | Tight High-Spin Breakers |
| 32 | Heredia-Bustos, Rolando | DOW_EAS1 | Curveball | 75 | 66.3 | 0.177 | 5.6 | -11.0 | 2220 | 73.7 | 5.05 | Tight High-Spin Breakers |
| 33 | Hill, Kaleb | OTT_TIT | Curveball | 222 | 66.1 | 0.198 | -4.2 | 13.2 | 2148 | 73.2 | 5.32 | Tight High-Spin Breakers |
| 34 | Morin, Jacob | QUE_CAP | Slider | 85 | 65.8 | 0.207 | 7.4 | -6.2 | 2495 | 77.4 | 5.50 | Tight High-Spin Breakers |
| 35 | Morgan, Cooper | QUE_CAP | Changeup | 74 | 65.6 | 0.190 | 6.1 | -16.2 | 1996 | 82.4 | 5.91 | Tight High-Spin Breakers |
| 36 | Shears, Tanner | SCH_BOO | Splitter | 69 | 65.5 | 0.204 | -1.5 | 7.1 | 897 | 82.0 | 5.08 | Tight High-Spin Breakers |
| 37 | Hickey, Matt | GAT_GRI | Curveball | 62 | 65.5 | 0.190 | -4.1 | -6.0 | 2255 | 79.8 | 5.45 | Tight High-Spin Breakers |
| 38 | Hohenstein, Liam | WIN_CIT29 | Curveball | 103 | 65.2 | 0.168 | -7.3 | -11.9 | 2583 | 75.8 | 5.37 | Tight High-Spin Breakers |
| 39 | Eisenbarger, Jack | QUE_CAP | Curveball | 93 | 64.8 | 0.212 | -3.6 | 12.1 | 2796 | 77.3 | 5.27 | Tight High-Spin Breakers |
| 40 | Parsons, Billy | SUS_COU1 | Cutter | 56 | 64.6 | 0.182 | 9.5 | -2.9 | 2552 | 86.3 | 5.56 | Tight High-Spin Breakers |
| 41 | Petschke, Ben | EVA_OTT | Slider | 144 | 64.6 | 0.186 | -1.7 | -13.5 | 2628 | 81.1 | 5.04 | Tight High-Spin Breakers |
| 42 | Majick, Eli | NEW_ENG23 | Cutter | 68 | 64.6 | 0.190 | 5.6 | -0.9 | 2500 | 82.8 | 5.73 | Tight High-Spin Breakers |
| 43 | Perozzi, John | SUS_COU1 | Slider | 126 | 64.1 | 0.179 | 7.9 | -4.0 | 2405 | 83.1 | 5.93 | Tight High-Spin Breakers |
| 44 | MacMillan, Blake | TRO_AIG | Slider | 106 | 64.1 | 0.211 | 6.1 | -0.1 | 1930 | 79.5 | 5.32 | Tight High-Spin Breakers |
| 45 | Vitas, Ben | JOL_SLA | Splitter | 127 | 63.9 | 0.187 | 0.7 | 6.6 | 1082 | 81.4 | 4.96 | Tight High-Spin Breakers |
| 46 | Cook, Cole | SCH_BOO | Curveball | 114 | 63.8 | 0.197 | -3.7 | 6.1 | 2490 | 76.9 | 4.92 | Tight High-Spin Breakers |
| 47 | Foster, Kobe | WAS_WIL3 | Slider | 144 | 63.6 | 0.184 | 5.1 | 5.4 | 2328 | 78.3 | 5.34 | Tight High-Spin Breakers |
| 48 | Boies, Emiles | QUE_CAP | Curveball | 80 | 63.5 | 0.172 | -4.3 | -5.8 | 2121 | 76.5 | 5.61 | Tight High-Spin Breakers |
| 49 | Barraza, Chris | MIS_MUD | Slider | 57 | 63.4 | 0.194 | 3.3 | -3.8 | 2320 | 84.1 | 5.31 | Tight High-Spin Breakers |
| 50 | Miner, Jace | DOW_EAS1 | Changeup | 156 | 63.3 | 0.219 | 6.2 | -12.6 | 1710 | 84.2 | 5.92 | Tight High-Spin Breakers |
| 51 | Majick, Eli | NEW_ENG23 | Curveball | 52 | 63.1 | 0.186 | -1.0 | 4.5 | 2169 | 77.0 | 5.68 | Tight High-Spin Breakers |
| 52 | Plumadore, Carson | WIN_CIT29 | Slider | 115 | 62.9 | 0.174 | 2.7 | -4.9 | 2439 | 76.0 | 5.51 | Tight High-Spin Breakers |
| 53 | Vail, Tyler | NEW_YOR13 | Slider | 197 | 62.9 | 0.237 | 1.3 | -1.9 | 2267 | 80.6 | 5.97 | Tight High-Spin Breakers |
| 54 | Good, Ty | GAT_GRI | Slider | 189 | 62.4 | 0.192 | 3.9 | -0.2 | 2042 | 79.2 | 5.82 | Tight High-Spin Breakers |
| 55 | Morgan, Cooper | QUE_CAP | Slider | 63 | 62.3 | 0.207 | 3.6 | 10.4 | 2471 | 79.2 | 5.50 | Tight High-Spin Breakers |
| 56 | Tokar, Heitor | OTT_TIT | Slider | 141 | 62.1 | 0.218 | 3.8 | -3.5 | 2107 | 81.9 | 5.92 | Tight High-Spin Breakers |
| 57 | O'Hanlon, Michael | WAS_WIL3 | Slider | 63 | 61.9 | 0.242 | 2.9 | -2.5 | 2499 | 83.4 | 5.38 | Tight High-Spin Breakers |
| 58 | Harris, Ben | GAT_GRI | Curveball | 242 | 61.8 | 0.234 | -14.1 | -7.2 | 2131 | 77.9 | 4.96 | Tight High-Spin Breakers |
| 59 | Kemlage, Joe | NEW_ENG23 | Slider | 83 | 61.7 | 0.195 | -2.7 | 14.1 | 2605 | 82.2 | 5.52 | Tight High-Spin Breakers |
| 60 | Baird, Dustin | MIS_MUD | Slider | 57 | 61.7 | 0.213 | 8.2 | -9.0 | 2365 | 81.3 | 5.87 | Tight High-Spin Breakers |
| 61 | Wiltse, Ryan | EVA_OTT | Curveball | 131 | 61.6 | 0.217 | -12.7 | -4.3 | 1923 | 74.3 | 5.85 | Tight High-Spin Breakers |
| 62 | Gollert, Harley | QUE_CAP | Slider | 57 | 61.5 | 0.217 | 1.0 | 5.1 | 2222 | 79.4 | 5.09 | Tight High-Spin Breakers |
| 63 | Scafidi, Christian | LAK_ERI24 | Curveball | 59 | 61.3 | 0.194 | -6.8 | -2.9 | 2246 | 77.7 | 5.81 | Tight High-Spin Breakers |
| 64 | Hampton, Ky | OTT_TIT | Curveball | 52 | 61.3 | 0.177 | -5.0 | -13.6 | 2195 | 81.6 | 5.56 | Tight High-Spin Breakers |
| 65 | Morgan, Marcus | JOL_SLA | Cutter | 63 | 61.1 | 0.183 | 6.4 | -3.1 | 2670 | 86.9 | 5.76 | Tight High-Spin Breakers |
| 66 | Maryniak, Connor | NEW_JER6 | Curveball | 180 | 61.1 | 0.214 | -9.8 | -4.6 | 2515 | 81.5 | 4.77 | Tight High-Spin Breakers |
| 67 | Dill, Austin | TRI_VAL | Slider | 72 | 61.1 | 0.229 | 1.6 | -3.6 | 2565 | 79.3 | 4.97 | Tight High-Spin Breakers |
| 68 | Campbell, Tyler | MIS_MUD | Changeup | 97 | 60.9 | 0.220 | 11.9 | -7.9 | 1851 | 74.8 | 6.27 | Tight High-Spin Breakers |
| 69 | Cameron, Zach | WIN_CIT29 | Slider | 142 | 60.9 | 0.199 | 7.3 | -1.5 | 2342 | 81.7 | 5.41 | Tight High-Spin Breakers |
| 70 | Widener, Jacob | SUS_COU1 | Slider | 91 | 60.7 | 0.227 | 3.3 | 16.2 | 2854 | 80.5 | 6.11 | Tight High-Spin Breakers |
| 71 | Harajli, Ahmad | FLO_Y'A | Slider | 76 | 60.2 | 0.191 | -2.5 | -2.9 | 2056 | 80.5 | 5.99 | Tight High-Spin Breakers |
| 72 | Villers, Ian | QUE_CAP | Slider | 66 | 59.6 | 0.241 | -0.3 | -5.1 | 2117 | 82.3 | 5.94 | Tight High-Spin Breakers |
| 73 | Calderon, Jean | LAK_ERI24 | Slider | 73 | 59.6 | 0.198 | 1.3 | -9.7 | 2593 | 86.4 | 6.05 | Tight High-Spin Breakers |
| 74 | Hocom, Quinn | TRI_VAL | Changeup | 101 | 59.4 | 0.221 | 6.2 | 17.0 | 1965 | 78.3 | 5.62 | Tight High-Spin Breakers |
| 75 | Smith, Jackson | MIS_MUD | Slider | 129 | 59.2 | 0.217 | 1.7 | -9.0 | 2642 | 78.5 | 4.87 | Tight High-Spin Breakers |
| 76 | Sechrist, Zander | WAS_WIL3 | Curveball | 92 | 59.1 | 0.205 | 0.3 | 8.6 | 1838 | 67.4 | 4.96 | Tight High-Spin Breakers |
| 77 | Eckaus, David | EVA_OTT | Slider | 175 | 59.1 | 0.224 | 2.0 | 4.9 | 2594 | 82.5 | 5.56 | Tight High-Spin Breakers |
| 78 | Scott, Brandon | LAK_ERI24 | Slider | 145 | 59.0 | 0.194 | -0.3 | 6.9 | 2405 | 77.9 | 5.41 | Tight High-Spin Breakers |
| 79 | Hensey, Rob | SUS_COU1 | Slider | 108 | 59.0 | 0.211 | 5.0 | -0.5 | 2206 | 82.8 | 6.21 | Tight High-Spin Breakers |
| 80 | Langhorne, Miles | SUS_COU1 | Slider | 61 | 59.0 | 0.223 | 0.0 | -3.1 | 2487 | 86.8 | 5.90 | Tight High-Spin Breakers |
| 81 | Walsh, John | MIS_MUD | Slider | 67 | 59.0 | 0.213 | -1.0 | 11.1 | 2213 | 73.2 | 4.96 | Tight High-Spin Breakers |
| 82 | Ronne, Andrew | GAT_GRI | Slider | 142 | 58.9 | 0.206 | 0.0 | -14.6 | 2593 | 81.4 | 5.94 | Tight High-Spin Breakers |
| 83 | Long, Maddox | WAS_WIL3 | Slider | 226 | 58.9 | 0.197 | 2.8 | -8.6 | 2598 | 82.8 | 5.52 | Tight High-Spin Breakers |
| 84 | Lefebvre, Charles | TRO_AIG | Curveball | 99 | 58.7 | 0.247 | -9.3 | -8.7 | 2467 | 77.6 | 6.11 | Tight High-Spin Breakers |
| 85 | Shinn, Nathan | LAK_ERI24 | Slider | 138 | 58.6 | 0.218 | 0.3 | 0.8 | 2179 | 82.1 | 5.24 | Tight High-Spin Breakers |
| 86 | Brito, Richard | NEW_ENG23 | Slider | 73 | 58.6 | 0.197 | 3.6 | -6.0 | 2287 | 81.7 | 6.09 | Tight High-Spin Breakers |
| 87 | Vail, Tyler | NEW_YOR13 | Curveball | 183 | 58.5 | 0.215 | -2.9 | -5.5 | 2225 | 74.7 | 5.72 | Tight High-Spin Breakers |
| 88 | Cohn, Cooper | NIU_HUS | Slider | 63 | 58.4 | 0.188 | -1.2 | -13.7 | 2534 | 78.9 | 5.40 | Tight High-Spin Breakers |
| 89 | Marklund, Brandon | OTT_TIT | Slider | 124 | 58.4 | 0.244 | 6.4 | -14.2 | 2707 | 79.6 | 4.87 | Tight High-Spin Breakers |
| 90 | Rohde, Isaac | NEW_YOR13 | Changeup | 801 | 58.4 | 0.217 | 4.0 | -20.4 | 1977 | 76.3 | 6.19 | Tight High-Spin Breakers |
| 91 | Williams, Brian | MIS_MUD | Splitter | 101 | 58.3 | 0.186 | 2.5 | 5.0 | 1728 | 78.6 | 6.05 | Tight High-Spin Breakers |
| 92 | Allemann, Braeden | QUE_CAP | Slider | 71 | 58.3 | 0.222 | 3.5 | -2.9 | 2261 | 83.4 | 6.19 | Tight High-Spin Breakers |
| 93 | Sechrist, Zander | WAS_WIL3 | Slider | 80 | 58.3 | 0.224 | 3.0 | 7.6 | 1875 | 69.5 | 5.14 | Tight High-Spin Breakers |
| 94 | Gollert, Harley | TRO_AIG | Curveball | 86 | 58.1 | 0.225 | -5.7 | 5.8 | 2235 | 77.1 | 4.85 | Tight High-Spin Breakers |
| 95 | Andueza, Axel | DOW_EAS1 | Changeup | 104 | 58.0 | 0.227 | 5.7 | 11.2 | 2087 | 82.4 | 5.22 | Tight High-Spin Breakers |
| 96 | Leak, Anthony | NEW_YOR13 | Slider | 260 | 58.0 | 0.187 | 5.0 | -6.0 | 2302 | 83.2 | 5.81 | Tight High-Spin Breakers |
| 97 | Hagan, Jack | DOW_EAS1 | Slider | 210 | 57.9 | 0.228 | 3.8 | -3.7 | 2436 | 84.4 | 5.70 | Tight High-Spin Breakers |
| 98 | Garcia, Andrew | EVA_OTT | Slider | 227 | 57.9 | 0.196 | 2.2 | -7.2 | 2338 | 82.2 | 5.38 | Tight High-Spin Breakers |
| 99 | Foster, Kobe | WAS_WIL3 | Changeup | 190 | 57.7 | 0.228 | 15.8 | -14.0 | 1869 | 79.4 | 5.78 | Tight High-Spin Breakers |
| 100 | Vailes, Gage | GAT_GRI | Slider | 316 | 57.5 | 0.212 | 5.8 | -11.6 | 2553 | 81.7 | 4.59 | Tight High-Spin Breakers |
| 101 | Cooper, Garrett | NEW_YOR13 | Slider | 91 | 57.4 | 0.185 | 2.0 | -3.4 | 2118 | 80.9 | 5.69 | Tight High-Spin Breakers |
| 102 | Woolfolk, Dallas | MIS_MUD | Slider | 67 | 57.4 | 0.252 | 0.4 | -1.3 | 2297 | 82.3 | 5.17 | Tight High-Spin Breakers |
| 103 | Dima, Josh | GAT_GRI | Slider | 119 | 57.3 | 0.204 | 2.4 | 2.1 | 1923 | 81.9 | 6.00 | Tight High-Spin Breakers |
| 104 | Odonnell, Brendan | NEW_ENG23 | Slider | 210 | 57.2 | 0.215 | -1.4 | 12.0 | 2645 | 84.3 | 6.12 | Tight High-Spin Breakers |
| 105 | Garcia, Hector | WAS_WIL3 | Slider | 56 | 57.2 | 0.230 | 2.0 | -7.1 | 2355 | 77.3 | 5.72 | Tight High-Spin Breakers |
| 106 | Thornton, Tyler | NEW_ENG23 | Splitter | 119 | 57.2 | 0.243 | 4.9 | 11.5 | 952 | 77.6 | 4.85 | Tight High-Spin Breakers |
| 107 | Anibal, Trevor | NEW_ENG23 | Curveball | 107 | 57.1 | 0.234 | -15.3 | -9.3 | 2496 | 76.0 | 5.44 | Tight High-Spin Breakers |
| 108 | Bice, Emmett | NEW_YOR13 | Slider | 273 | 57.1 | 0.231 | 2.1 | -2.6 | 2380 | 82.8 | 5.66 | Tight High-Spin Breakers |
| 109 | Balzan, Jackson | SUS_COU1 | Curveball | 80 | 57.0 | 0.236 | -4.9 | 4.9 | 2104 | 76.2 | 5.11 | Tight High-Spin Breakers |
| 110 | Pierson, Kenny | LAK_ERI24 | Slider | 98 | 57.0 | 0.244 | -1.4 | 7.4 | 2088 | 72.3 | 4.62 | Tight High-Spin Breakers |
| 111 | Petery, Dylan | WIN_CIT29 | Curveball | 69 | 56.9 | 0.226 | -7.0 | -14.6 | 2556 | 74.6 | 5.46 | Tight High-Spin Breakers |
| 112 | Moore, Kyle | SCH_BOO | Cutter | 128 | 56.9 | 0.224 | 9.6 | 1.7 | 2133 | 84.5 | 4.71 | Tight High-Spin Breakers |
| 113 | Saturria, Michael | NEW_ENG23 | Slider | 248 | 56.8 | 0.208 | 3.9 | -7.3 | 2706 | 80.7 | 5.90 | Tight High-Spin Breakers |
| 114 | Nova, Fraynel | LAK_ERI24 | Slider | 304 | 56.8 | 0.223 | -0.6 | -7.0 | 2284 | 80.6 | 5.61 | Tight High-Spin Breakers |
| 115 | Morgan, Marcus | JOL_SLA | Slider | 66 | 56.7 | 0.214 | 7.0 | -9.2 | 2844 | 84.9 | 5.71 | Tight High-Spin Breakers |
| 116 | Simpson, Garret | EVA_OTT | Curveball | 120 | 56.6 | 0.231 | -11.8 | -13.0 | 2637 | 76.4 | 5.13 | Tight High-Spin Breakers |
| 117 | Petschke, Ben | EVA_OTT | Curveball | 169 | 56.6 | 0.233 | -9.7 | -15.8 | 2767 | 77.2 | 4.96 | Tight High-Spin Breakers |
| 118 | Kirby, Zach | WAS_WIL3 | Curveball | 105 | 56.5 | 0.232 | -18.3 | -10.7 | 2261 | 70.8 | 5.41 | Tight High-Spin Breakers |
| 119 | Harris, Everette | TRI_VAL | Slider | 53 | 56.5 | 0.215 | 1.2 | -8.7 | 2862 | 80.5 | 6.15 | Tight High-Spin Breakers |
| 120 | Earwood, Micah | SUS_COU1 | Curveball | 104 | 56.4 | 0.230 | -6.8 | -6.2 | 2458 | 78.6 | 5.46 | Tight High-Spin Breakers |
| 121 | Langrell, Connor | MIS_MUD | Curveball | 114 | 56.4 | 0.229 | -15.6 | -11.6 | 2718 | 77.5 | 6.01 | Tight High-Spin Breakers |
| 122 | Valdez, Alex | EVA_OTT | Cutter | 78 | 56.3 | 0.246 | 4.5 | -1.8 | 2070 | 86.4 | 5.36 | Tight High-Spin Breakers |
| 123 | Peters, Garrett | NEW_YOR13 | Curveball | 157 | 56.0 | 0.229 | 0.8 | -0.5 | 2043 | 76.0 | 5.72 | Tight High-Spin Breakers |
| 124 | Helt, Robert | LAK_ERI24 | Slider | 229 | 56.0 | 0.226 | -1.2 | -5.1 | 2405 | 81.1 | 5.75 | Tight High-Spin Breakers |
| 125 | Whitesell, Max | FLO_Y'A | Slider | 157 | 55.9 | 0.215 | 6.2 | -4.5 | 2081 | 80.3 | 6.29 | Tight High-Spin Breakers |
| 126 | Long, Jalon | NEW_YOR13 | Slider | 156 | 55.9 | 0.230 | 5.1 | -1.8 | 2158 | 84.1 | 5.80 | Tight High-Spin Breakers |
| 127 | Lefebvre, Charles | TRO_AIG | Slider | 107 | 55.9 | 0.194 | 2.3 | -1.6 | 2171 | 81.9 | 6.43 | Tight High-Spin Breakers |
| 128 | Heredia-Bustos, Rolando | DOW_EAS1 | Slider | 449 | 55.6 | 0.212 | 6.7 | -3.9 | 2321 | 78.5 | 5.26 | Tight High-Spin Breakers |
| 129 | Hocom, Quinn | TRI_VAL | Curveball | 106 | 55.5 | 0.245 | -13.4 | -11.6 | 2373 | 76.8 | 5.48 | Tight High-Spin Breakers |
| 130 | Eisenbarger, Jack | QUE_CAP | Changeup | 166 | 55.1 | 0.199 | 14.6 | -14.6 | 2317 | 78.8 | 6.02 | Tight High-Spin Breakers |
| 131 | Rodriguez, Leonardo | NEW_JER6 | Slider | 68 | 55.1 | 0.218 | 2.5 | -3.2 | 2587 | 83.7 | 5.94 | Tight High-Spin Breakers |
| 132 | Gordillo, Lucas | TRI_VAL | Slider | 58 | 55.0 | 0.254 | 3.0 | -5.9 | 2016 | 80.8 | 5.58 | Tight High-Spin Breakers |
| 133 | Boies, Emiles | QUE_CAP | Slider | 73 | 55.0 | 0.242 | 5.0 | -0.1 | 2127 | 80.5 | 5.94 | Tight High-Spin Breakers |
| 134 | Fauci, Sonny | NEW_JER6 | Slider | 127 | 55.0 | 0.268 | -1.7 | -6.1 | 2337 | 83.8 | 5.96 | Tight High-Spin Breakers |
| 135 | De Los Santos, Enmanuel | NEW_ENG23 | Curveball | 105 | 55.0 | 0.246 | -5.7 | -11.1 | 2219 | 71.3 | 6.47 | Tight High-Spin Breakers |
| 136 | Simone, Andrew | TRO_AIG | Slider | 109 | 54.9 | 0.210 | 3.5 | -3.7 | 2160 | 84.3 | 5.72 | Tight High-Spin Breakers |
| 137 | Milburn, Isaac | FLO_Y'A | Slider | 180 | 54.9 | 0.211 | -1.8 | 15.8 | 2652 | 78.6 | 4.83 | Tight High-Spin Breakers |
| 138 | Allemann, Braeden | QUE_CAP | Curveball | 234 | 54.8 | 0.236 | -7.1 | -15.7 | 2195 | 76.9 | 6.13 | Tight High-Spin Breakers |
| 139 | Zentko, Dylan | EVA_OTT | Slider | 67 | 54.6 | 0.225 | 3.7 | 1.1 | 1951 | 77.4 | 5.63 | Tight High-Spin Breakers |
| 140 | Campbell, AJ | WIN_CIT29 | Slider | 373 | 54.4 | 0.221 | 5.2 | -9.2 | 2571 | 80.3 | 4.87 | Tight High-Spin Breakers |
| 141 | Nabholz, Nate | TRI_VAL | Slider | 98 | 54.3 | 0.219 | 6.4 | -1.6 | 1992 | 83.4 | 5.68 | Tight High-Spin Breakers |
| 142 | Sesar, Jorden | SUS_COU1 | Curveball | 119 | 53.9 | 0.238 | -12.0 | -11.1 | 2419 | 74.9 | 6.03 | Tight High-Spin Breakers |
| 143 | Noriega, Branden | LAK_ERI24 | Curveball | 120 | 53.9 | 0.256 | -9.7 | 7.7 | 2843 | 79.3 | 5.25 | Tight High-Spin Breakers |
| 144 | Cook, Cole | SCH_BOO | Slider | 195 | 53.9 | 0.242 | 3.6 | 5.1 | 2497 | 79.9 | 5.11 | Tight High-Spin Breakers |
| 145 | Turner, Eric | JOL_SLA | Changeup | 163 | 53.9 | 0.240 | 4.6 | 15.4 | 1658 | 79.7 | 5.14 | Tight High-Spin Breakers |
| 146 | Gollert, Harley | TRO_AIG | Changeup | 169 | 53.8 | 0.256 | 9.8 | -13.6 | 1544 | 79.6 | 5.27 | Tight High-Spin Breakers |
| 147 | DeCastro, Justin | LON_ISL22 | Changeup | 122 | 53.8 | 0.235 | 9.6 | 18.6 | 1979 | 79.4 | 5.06 | Tight High-Spin Breakers |
| 148 | Helt, Robert | LAK_ERI24 | Curveball | 159 | 53.7 | 0.255 | -5.7 | -5.9 | 2380 | 78.9 | 5.77 | Tight High-Spin Breakers |
| 149 | Johnston, Spencer | DOW_EAS1 | Slider | 190 | 53.5 | 0.214 | 6.7 | 0.9 | 2083 | 78.4 | 5.96 | Tight High-Spin Breakers |
| 150 | Miner, Jace | DOW_EAS1 | Curveball | 109 | 53.5 | 0.252 | 2.5 | 11.2 | 1843 | 75.8 | 5.42 | Tight High-Spin Breakers |
| 151 | Oe, Ryoya | OTT_TIT | Curveball | 57 | 53.5 | 0.210 | -4.6 | 5.0 | 2303 | 73.3 | 4.90 | Tight High-Spin Breakers |
| 152 | Smith, Jackson | MIS_MUD | Cutter | 97 | 53.3 | 0.219 | 3.3 | 5.0 | 2427 | 81.7 | 5.08 | Tight High-Spin Breakers |
| 153 | Reeves, Cobe | NEW_YOR13 | Slider | 51 | 53.3 | 0.271 | -0.2 | 3.4 | 2215 | 82.8 | 5.74 | Tight High-Spin Breakers |
| 154 | Pardinho, Eric | OTT_TIT | Slider | 151 | 53.2 | 0.237 | 5.3 | 1.9 | 2347 | 86.4 | 5.69 | Tight High-Spin Breakers |
| 155 | Zeplin, Blane | JOL_SLA | Slider | 108 | 53.1 | 0.212 | -0.7 | -6.9 | 2273 | 77.7 | 5.32 | Tight High-Spin Breakers |
| 156 | Gamelin, Shaun | JOL_SLA | Slider | 75 | 53.0 | 0.242 | 2.8 | -1.2 | 2297 | 81.9 | 4.83 | Tight High-Spin Breakers |
| 157 | Williams, Pierce | NEW_ENG23 | Changeup | 485 | 52.9 | 0.232 | 10.6 | -13.8 | 1792 | 79.8 | 5.95 | Tight High-Spin Breakers |
| 158 | Thompson, Ross | SCH_BOO | Slider | 223 | 52.8 | 0.230 | 3.5 | -2.3 | 2054 | 79.8 | 5.25 | Tight High-Spin Breakers |
| 159 | Campbell, AJ | WIN_CIT29 | Curveball | 62 | 52.7 | 0.209 | -0.3 | -15.8 | 2589 | 75.6 | 4.81 | Tight High-Spin Breakers |
| 160 | Sittinger, Brandyn | LAK_ERI24 | Slider | 138 | 52.6 | 0.234 | 3.7 | -0.9 | 2462 | 87.6 | 5.72 | Tight High-Spin Breakers |
| 161 | Correa, Nelvin | QUE_CAP | Slider | 125 | 52.6 | 0.212 | 4.2 | -7.3 | 2416 | 83.4 | 5.46 | Tight High-Spin Breakers |
| 162 | Balzan, Jackson | SUS_COU1 | Changeup | 315 | 52.6 | 0.239 | 9.8 | -13.8 | 1880 | 80.1 | 5.35 | Tight High-Spin Breakers |
| 163 | Majick, Eli | NEW_ENG23 | Slider | 214 | 52.6 | 0.239 | 3.7 | 8.0 | 2540 | 79.6 | 5.61 | Tight High-Spin Breakers |
| 164 | Martzolf, Max | JOL_SLA | Sinker | 241 | 52.4 | 0.236 | 10.3 | -19.7 | 2128 | 84.9 | 5.46 | Tight High-Spin Breakers |
| 165 | Henderson, Drew | DOW_EAS1 | Curveball | 257 | 52.1 | 0.230 | -8.0 | -4.9 | 2303 | 76.8 | 5.13 | Tight High-Spin Breakers |
| 166 | Puccetti, Dominic | OTT_TIT | Curveball | 172 | 52.1 | 0.247 | -13.5 | 9.8 | 2684 | 73.7 | 5.27 | Tight High-Spin Breakers |
| 167 | Pierson, Kenny | LAK_ERI24 | Sinker | 229 | 52.0 | 0.237 | 0.4 | -17.6 | 1765 | 81.1 | 4.80 | Tight High-Spin Breakers |
| 168 | Kines, Gunnar | JOL_SLA | Changeup | 308 | 52.0 | 0.240 | 12.2 | -12.5 | 1909 | 75.4 | 6.01 | Tight High-Spin Breakers |
| 169 | Vilchez, Michael | OTT_TIT | Slider | 99 | 51.9 | 0.229 | 1.6 | -4.7 | 2303 | 82.8 | 5.74 | Tight High-Spin Breakers |
| 170 | Pierson, Kenny | LAK_ERI24 | Changeup | 277 | 51.9 | 0.240 | -1.4 | -16.0 | 1756 | 76.9 | 4.94 | Tight High-Spin Breakers |
| 171 | Sparks, Alec | GAT_GRI | Slider | 163 | 51.9 | 0.220 | 0.7 | -7.3 | 2596 | 80.1 | 5.44 | Tight High-Spin Breakers |
| 172 | Bauer, Patrick | QUE_CAP | Curveball | 75 | 51.8 | 0.257 | -12.5 | -14.2 | 2250 | 69.7 | 6.01 | Tight High-Spin Breakers |
| 173 | Foster, Kobe | WAS_WIL3 | Curveball | 186 | 51.8 | 0.249 | -8.3 | 15.1 | 2248 | 67.6 | 5.34 | Tight High-Spin Breakers |
| 174 | Hill, Kaleb | OTT_TIT | Slider | 155 | 51.8 | 0.244 | 0.6 | 9.2 | 2253 | 78.9 | 5.24 | Tight High-Spin Breakers |
| 175 | McCartney, Seth | MIS_MUD | Slider | 57 | 51.7 | 0.196 | 4.2 | -3.0 | 2474 | 81.9 | 5.45 | Tight High-Spin Breakers |
| 176 | Cook, Cole | SCH_BOO | Sinker | 118 | 51.7 | 0.225 | 12.2 | -11.6 | 2258 | 84.9 | 5.31 | Tight High-Spin Breakers |
| 177 | Joven, Art | MIS_MUD | Sinker | 305 | 51.5 | 0.243 | 7.2 | -15.6 | 1793 | 83.3 | 5.15 | Tight High-Spin Breakers |
| 178 | Leach, Landon | TRO_AIG | Slider | 54 | 51.5 | 0.240 | 2.8 | -6.5 | 2079 | 82.2 | 5.35 | Tight High-Spin Breakers |
| 179 | Sakurai, Masatoshi | QUE_CAP | Slider | 138 | 51.5 | 0.244 | -0.7 | 4.4 | 2272 | 78.9 | 5.77 | Tight High-Spin Breakers |
| 180 | Gilleran, Jimmy | NEW_ENG23 | Slider | 125 | 51.4 | 0.239 | 3.8 | -3.4 | 2238 | 80.8 | 5.33 | Tight High-Spin Breakers |
| 181 | Moore, Kyle | SCH_BOO | Curveball | 110 | 51.4 | 0.249 | -8.7 | -8.1 | 2530 | 76.8 | 4.10 | Tight High-Spin Breakers |
| 182 | Figueredo, Kevin | WIN_CIT29 | Changeup | 111 | 51.4 | 0.253 | 6.0 | -12.7 | 1696 | 84.0 | 5.34 | Tight High-Spin Breakers |
| 183 | Williams, Brian | MIS_MUD | Slider | 243 | 51.2 | 0.246 | 4.3 | -0.8 | 2165 | 81.7 | 5.94 | Tight High-Spin Breakers |
| 184 | Blair, Davis | DOW_EAS1 | Slider | 99 | 51.2 | 0.260 | 3.6 | -5.9 | 2146 | 81.9 | 5.11 | Tight High-Spin Breakers |
| 185 | Glickstein, Aaron | SCH_BOO | Slider | 55 | 51.1 | 0.245 | 7.5 | -0.5 | 2240 | 84.9 | 5.58 | Tight High-Spin Breakers |
| 186 | Escobar, Anthony | TRO_AIG | Curveball | 50 | 50.9 | 0.226 | -2.0 | -5.9 | 2221 | 77.2 | 5.98 | Tight High-Spin Breakers |
| 187 | Campbell, AJ | WIN_CIT29 | Changeup | 73 | 50.8 | 0.240 | 6.9 | 9.4 | 2070 | 80.3 | 5.36 | Tight High-Spin Breakers |
| 188 | Armstrong, Andrew | NEW_YOR13 | Slider | 125 | 50.7 | 0.279 | 2.6 | 7.1 | 2356 | 80.1 | 5.89 | Tight High-Spin Breakers |
| 189 | Sanchez, Edwin | LAK_ERI24 | Slider | 72 | 50.6 | 0.257 | -0.9 | 4.2 | 2397 | 76.9 | 5.13 | Tight High-Spin Breakers |
| 190 | Cooper, Garrett | NEW_YOR13 | Curveball | 161 | 50.5 | 0.232 | -5.6 | -6.7 | 2194 | 76.2 | 5.55 | Tight High-Spin Breakers |
| 191 | Sanchez, Edwin | LAK_ERI24 | Curveball | 97 | 50.5 | 0.222 | -5.1 | 6.2 | 2460 | 75.6 | 5.32 | Tight High-Spin Breakers |
| 192 | Linderman, Greyson | JOL_SLA | Slider | 66 | 50.5 | 0.271 | -4.0 | -13.7 | 2207 | 81.2 | 4.96 | Tight High-Spin Breakers |
| 193 | Carroll, Jake | JOL_SLA | Curveball | 51 | 50.4 | 0.261 | -7.1 | 8.2 | 2028 | 75.6 | 6.18 | Tight High-Spin Breakers |
| 194 | Wehrle, Tyler | WIN_CIT29 | Slider | 146 | 50.4 | 0.231 | 2.4 | -10.0 | 2521 | 80.7 | 5.33 | Tight High-Spin Breakers |
| 195 | Serrano, Elio | NEW_JER6 | Curveball | 79 | 50.3 | 0.277 | -10.3 | -13.9 | 2293 | 75.6 | 5.10 | Tight High-Spin Breakers |
| 196 | Bargo, Casey | FLO_Y'A | Slider | 101 | 50.3 | 0.222 | 0.1 | -3.9 | 2278 | 81.4 | 5.35 | Tight High-Spin Breakers |
| 197 | Castro, Alexander | TRO_AIG | Slider | 126 | 50.2 | 0.253 | 0.6 | -4.8 | 2510 | 83.5 | 4.83 | Tight High-Spin Breakers |
| 198 | Galva, Claudio | GAT_GRI | Changeup | 96 | 50.1 | 0.239 | 4.6 | -13.5 | 1474 | 84.4 | 4.83 | Tight High-Spin Breakers |
| 199 | Toribio, Noe | TRO_AIG | Slider | 150 | 50.0 | 0.218 | 3.0 | 0.9 | 2223 | 82.5 | 5.80 | Tight High-Spin Breakers |
| 200 | Belton, Hunter | MIS_MUD | Slider | 99 | 49.9 | 0.245 | 6.5 | -2.6 | 2108 | 78.5 | 5.82 | Tight High-Spin Breakers |
| 201 | Ginn, Landon | WAS_WIL3 | Slider | 79 | 49.9 | 0.227 | 1.6 | -3.4 | 2876 | 85.3 | 5.12 | Tight High-Spin Breakers |
| 202 | Campbell, Tyler | MIS_MUD | Slider | 199 | 49.9 | 0.271 | 8.1 | 3.9 | 2211 | 74.3 | 5.70 | Tight High-Spin Breakers |
| 203 | Floyd, Conner | QUE_CAP | Curveball | 58 | 49.9 | 0.252 | -2.7 | -17.4 | 2113 | 77.3 | 5.02 | Tight High-Spin Breakers |
| 204 | Scafidi, Christian | LAK_ERI24 | Slider | 177 | 49.8 | 0.240 | 4.1 | -2.0 | 2384 | 84.2 | 5.64 | Tight High-Spin Breakers |
| 205 | Kostura, Brit | WAS_WIL3 | Sinker | 133 | 49.8 | 0.233 | 13.1 | -16.7 | 2075 | 84.9 | 5.54 | Tight High-Spin Breakers |
| 206 | Snyder, Jack | SCH_BOO | Slider | 65 | 49.8 | 0.228 | 5.7 | -4.7 | 2458 | 84.1 | 5.19 | Tight High-Spin Breakers |
| 207 | Villalobos, Jonaiker | FLO_Y'A | Changeup | 185 | 49.7 | 0.242 | 7.8 | -13.2 | 1583 | 80.0 | 5.82 | Tight High-Spin Breakers |
| 208 | Smith, Ben | NEW_ENG23 | Slider | 112 | 49.6 | 0.281 | 0.1 | 13.6 | 2314 | 78.7 | 5.47 | Tight High-Spin Breakers |
| 209 | Cerda, Junior | EVA_OTT | Slider | 84 | 49.4 | 0.232 | -2.0 | -8.0 | 2593 | 81.6 | 4.87 | Tight High-Spin Breakers |
| 210 | Maher, Adam | TRI_VAL | Slider | 95 | 49.1 | 0.262 | 4.7 | 1.1 | 1935 | 79.4 | 5.66 | Tight High-Spin Breakers |
| 211 | Barreto, Brayhans | TRI_VAL | Slider | 96 | 49.1 | 0.261 | 4.0 | 0.3 | 1929 | 81.0 | 6.19 | Tight High-Spin Breakers |
| 212 | Gamelin, Shaun | JOL_SLA | Cutter | 137 | 48.8 | 0.245 | 5.6 | -0.4 | 2316 | 84.0 | 5.06 | Tight High-Spin Breakers |
| 213 | Misla, Luis | TRI_VAL | Slider | 69 | 48.6 | 0.261 | 1.2 | 10.3 | 2720 | 78.6 | 5.25 | Tight High-Spin Breakers |
| 214 | Joven, Art | MIS_MUD | Slider | 305 | 48.4 | 0.254 | 2.1 | 0.0 | 2241 | 77.5 | 5.18 | Tight High-Spin Breakers |
| 215 | Rodriguez, Luis | TRO_AIG | Slider | 58 | 48.3 | 0.240 | 2.2 | -1.6 | 2525 | 87.7 | 5.92 | Tight High-Spin Breakers |
| 216 | Parks, Pavin | LAK_ERI24 | Cutter | 135 | 48.3 | 0.254 | 7.0 | -3.6 | 2428 | 84.7 | 5.77 | Tight High-Spin Breakers |
| 217 | Kaminer, Brandon | DOW_EAS1 | Slider | 133 | 48.3 | 0.237 | 6.1 | 2.3 | 2474 | 83.8 | 5.28 | Tight High-Spin Breakers |
| 218 | Hicks, Jackson | DOW_EAS1 | Slider | 116 | 48.2 | 0.270 | 2.4 | -1.0 | 2195 | 80.0 | 5.23 | Tight High-Spin Breakers |
| 219 | Scott, Brandon | LAK_ERI24 | Changeup | 239 | 48.2 | 0.275 | 2.2 | -12.4 | 1511 | 81.2 | 5.75 | Tight High-Spin Breakers |
| 220 | Kaftan, Eddie | FLO_Y'A | Slider | 62 | 48.0 | 0.234 | 1.1 | -6.3 | 2437 | 77.1 | 4.72 | Tight High-Spin Breakers |
| 221 | Smith, Ethan | WIN_CIT29 | Slider | 58 | 48.0 | 0.282 | -0.2 | -6.4 | 2423 | 80.6 | 5.91 | Tight High-Spin Breakers |
| 222 | Turner, Eric | JOL_SLA | Slider | 203 | 47.9 | 0.252 | 1.3 | -7.7 | 2354 | 78.3 | 4.98 | Tight High-Spin Breakers |
| 223 | Gorgen, Grady | NEW_YOR13 | Changeup | 68 | 47.9 | 0.269 | 6.8 | -12.1 | 1866 | 83.8 | 6.06 | Tight High-Spin Breakers |
| 224 | Almonte, Lisandro | NEW_JER6 | Slider | 57 | 47.9 | 0.242 | 3.6 | -0.9 | 2194 | 85.7 | 5.45 | Tight High-Spin Breakers |
| 225 | Misla, Luis | TRI_VAL | Curveball | 156 | 47.7 | 0.256 | -5.5 | 9.2 | 2789 | 77.0 | 5.12 | Tight High-Spin Breakers |
| 226 | Baker, Luke | EVA_OTT | Curveball | 59 | 47.6 | 0.245 | -7.4 | 9.7 | 2694 | 75.5 | 5.51 | Tight High-Spin Breakers |
| 227 | Matos, Dwayne | OTT_TIT | Slider | 143 | 47.5 | 0.261 | 4.4 | -0.8 | 2026 | 81.5 | 6.17 | Tight High-Spin Breakers |
| 228 | Peters, Garrett | NEW_YOR13 | Changeup | 480 | 47.5 | 0.257 | 12.2 | -14.9 | 1872 | 80.4 | 5.96 | Tight High-Spin Breakers |
| 229 | Perdomo, Rafael | QUE_CAP | Slider | 84 | 47.5 | 0.261 | 3.1 | 0.8 | 2184 | 82.9 | 5.80 | Tight High-Spin Breakers |
| 230 | Drakeford, Dosie | NEW_JER6 | Slider | 82 | 47.1 | 0.296 | 1.9 | -6.7 | 2396 | 79.7 | 5.44 | Tight High-Spin Breakers |
| 231 | Foy, Corbin | LAK_ERI24 | Slider | 78 | 47.1 | 0.270 | -1.1 | -7.6 | 2653 | 82.4 | 5.56 | Tight High-Spin Breakers |
| 232 | Perez, Kelvin | WAS_WIL3 | Slider | 125 | 47.0 | 0.245 | 4.1 | -4.5 | 2241 | 81.5 | 5.76 | Tight High-Spin Breakers |
| 233 | McKillican, Adam | QUE_CAP | Slider | 50 | 46.9 | 0.243 | 3.3 | -3.5 | 2162 | 80.1 | 6.44 | Tight High-Spin Breakers |
| 234 | Bihm, Gage | MIS_MUD | Slider | 72 | 46.8 | 0.268 | -2.5 | 10.4 | 2278 | 80.4 | 4.98 | Tight High-Spin Breakers |
| 235 | Parra, Andres | LAK_ERI24 | Slider | 161 | 46.7 | 0.266 | 2.8 | 2.0 | 2288 | 79.6 | 5.71 | Tight High-Spin Breakers |
| 236 | Reeves, Cobe | NEW_YOR13 | Curveball | 51 | 46.6 | 0.276 | -7.9 | 6.9 | 2373 | 80.1 | 5.52 | Tight High-Spin Breakers |
| 237 | Hopewell, Chase | FLO_Y'A | Slider | 147 | 46.6 | 0.274 | 0.2 | -2.1 | 1915 | 81.0 | 6.14 | Tight High-Spin Breakers |
| 238 | Estrella, Noah | TRI_VAL | Slider | 146 | 46.5 | 0.227 | -2.6 | 0.6 | 2573 | 85.3 | 5.59 | Tight High-Spin Breakers |
| 239 | Campbell, AJ | WIN_CIT29 | Cutter | 51 | 46.4 | 0.262 | 8.9 | 1.0 | 2502 | 85.7 | 5.15 | Tight High-Spin Breakers |
| 240 | Joven, Art | MIS_MUD | Changeup | 454 | 46.4 | 0.258 | 5.3 | -15.5 | 1803 | 81.7 | 5.27 | Tight High-Spin Breakers |
| 241 | Thebiay, Nolan | EVA_OTT | Slider | 54 | 46.4 | 0.253 | -0.5 | -1.0 | 1826 | 79.2 | 6.17 | Tight High-Spin Breakers |
| 242 | Petery, Dylan | WIN_CIT29 | Slider | 54 | 46.3 | 0.231 | -0.6 | -12.0 | 2606 | 78.1 | 5.74 | Tight High-Spin Breakers |
| 243 | Galva, Claudio | GAT_GRI | Four-Seam | 109 | 46.3 | 0.258 | 12.8 | -10.4 | 2007 | 89.0 | 4.88 | Tight High-Spin Breakers |
| 244 | Debban, Caleb | NEW_JER6 | Curveball | 206 | 46.0 | 0.277 | -7.2 | 18.6 | 2810 | 76.9 | 5.91 | Tight High-Spin Breakers |
| 245 | Majick, Eli | NEW_ENG23 | Changeup | 130 | 46.0 | 0.268 | 3.9 | -13.9 | 1848 | 83.2 | 6.03 | Tight High-Spin Breakers |
| 246 | Smith, Jackson | MIS_MUD | Sinker | 451 | 46.0 | 0.267 | 0.9 | 21.8 | 2407 | 85.3 | 5.13 | Tight High-Spin Breakers |
| 247 | Barker, Alex | NEW_YOR13 | Slider | 166 | 45.9 | 0.243 | 3.6 | 4.1 | 2236 | 81.8 | 5.88 | Tight High-Spin Breakers |
| 248 | Ginn, Landon | WAS_WIL3 | Cutter | 111 | 45.9 | 0.248 | 3.2 | -2.0 | 2841 | 86.3 | 5.37 | Tight High-Spin Breakers |
| 249 | Catrambone, Ben | JOL_SLA | Cutter | 61 | 45.9 | 0.286 | 6.0 | -0.3 | 2368 | 83.2 | 5.25 | Tight High-Spin Breakers |
| 250 | Milburn, Isaac | FLO_Y'A | Curveball | 154 | 45.7 | 0.317 | -9.4 | 13.7 | 2578 | 76.6 | 4.96 | Tight High-Spin Breakers |
| 251 | Andueza, Axel | DOW_EAS1 | Curveball | 168 | 45.7 | 0.243 | -3.5 | -3.1 | 2202 | 79.4 | 5.09 | Tight High-Spin Breakers |
| 252 | Willeman, Landon | EVA_OTT | Slider | 101 | 45.6 | 0.235 | 0.4 | -5.0 | 2251 | 80.6 | 5.50 | Tight High-Spin Breakers |
| 253 | Salata, Derek | SCH_BOO | Slider | 179 | 45.5 | 0.262 | 3.2 | -9.3 | 2553 | 81.4 | 5.57 | Tight High-Spin Breakers |
| 254 | Bell, Brendan | NEW_ENG23 | Slider | 60 | 45.4 | 0.304 | -1.6 | -9.1 | 2408 | 82.4 | 5.51 | Tight High-Spin Breakers |
| 255 | Biddinger, Tyler | WIN_CIT29 | Slider | 66 | 45.0 | 0.251 | -0.1 | -11.0 | 2649 | 80.0 | 4.82 | Tight High-Spin Breakers |
| 256 | Foltz Jr., Michael | WAS_WIL3 | Curveball | 76 | 44.8 | 0.282 | -5.9 | 4.5 | 2315 | 79.2 | 5.34 | Tight High-Spin Breakers |
| 257 | Martzolf, Max | OTT_TIT | Changeup | 194 | 44.8 | 0.247 | 9.4 | -19.5 | 2044 | 83.2 | 5.42 | Tight High-Spin Breakers |
| 258 | Cook, Cole | SCH_BOO | Four-Seam | 268 | 44.8 | 0.270 | 14.1 | -9.3 | 2297 | 84.8 | 5.33 | Tight High-Spin Breakers |
| 259 | Peyton, Blake | GAT_GRI | Curveball | 90 | 44.7 | 0.225 | -5.8 | 8.6 | 2673 | 77.8 | 5.24 | Tight High-Spin Breakers |
| 260 | Huter, Blayne | SUS_COU1 | Curveball | 103 | 44.5 | 0.272 | -5.1 | -14.2 | 2137 | 73.7 | 6.01 | Tight High-Spin Breakers |
| 261 | Smith, Jackson | MIS_MUD | Changeup | 118 | 44.3 | 0.282 | -1.1 | 18.0 | 2242 | 81.7 | 5.12 | Tight High-Spin Breakers |
| 262 | Hill, Kaleb | OTT_TIT | Changeup | 234 | 44.3 | 0.262 | 9.4 | -15.2 | 1811 | 82.6 | 5.64 | Tight High-Spin Breakers |
| 263 | Willeman, Landon | EVA_OTT | Curveball | 121 | 44.3 | 0.287 | -8.2 | -9.9 | 2099 | 77.6 | 5.35 | Tight High-Spin Breakers |
| 264 | Cook, Cole | SCH_BOO | Changeup | 241 | 44.2 | 0.261 | 9.0 | -9.7 | 1865 | 80.9 | 5.45 | Tight High-Spin Breakers |
| 265 | Figueredo, Kevin | WIN_CIT29 | Curveball | 78 | 44.2 | 0.279 | -3.5 | 4.9 | 2324 | 75.8 | 5.00 | Tight High-Spin Breakers |
| 266 | Sechrist, Zander | WAS_WIL3 | Four-Seam | 135 | 44.1 | 0.252 | 13.9 | -16.1 | 1905 | 80.2 | 5.65 | Tight High-Spin Breakers |
| 267 | Simpson, Garret | EVA_OTT | Slider | 52 | 44.1 | 0.290 | -0.2 | -4.5 | 2432 | 81.9 | 5.10 | Tight High-Spin Breakers |
| 268 | Lovin, Xander | GAT_GRI | Slider | 157 | 44.0 | 0.287 | 3.1 | -3.6 | 2438 | 85.0 | 4.91 | Tight High-Spin Breakers |
| 269 | Majick, Eli | NEW_ENG23 | Sinker | 258 | 43.9 | 0.276 | 6.9 | -16.5 | 2011 | 87.5 | 5.85 | Tight High-Spin Breakers |
| 270 | Simpson, Garret | EVA_OTT | Cutter | 143 | 43.9 | 0.281 | 5.4 | 0.4 | 2406 | 85.9 | 5.38 | Tight High-Spin Breakers |
| 271 | Gregory, Ben | GAT_GRI | Slider | 96 | 43.8 | 0.305 | 1.6 | -4.3 | 2336 | 79.8 | 6.02 | Tight High-Spin Breakers |
| 272 | Forsyth, Braden | MIS_MUD | Slider | 151 | 43.8 | 0.277 | 3.4 | -6.9 | 2364 | 80.6 | 6.06 | Tight High-Spin Breakers |
| 273 | Gollert, Harley | QUE_CAP | Changeup | 52 | 43.8 | 0.254 | 10.2 | -8.4 | 1676 | 81.0 | 5.46 | Tight High-Spin Breakers |
| 274 | Delaney, Carter | WIN_CIT29 | Curveball | 71 | 43.7 | 0.290 | -5.5 | -7.6 | 2296 | 79.9 | 5.56 | Tight High-Spin Breakers |
| 275 | Encarnacion, J.D. | EVA_OTT | Slider | 143 | 43.6 | 0.253 | 2.5 | -5.4 | 2352 | 81.2 | 5.43 | Tight High-Spin Breakers |
| 276 | Sakurai, Masatoshi | QUE_CAP | Curveball | 177 | 43.6 | 0.281 | -4.4 | 5.4 | 2455 | 78.4 | 5.60 | Tight High-Spin Breakers |
| 277 | Okumura, Shuto | WAS_WIL3 | Four-Seam | 60 | 43.6 | 0.275 | 6.1 | 7.6 | 1757 | 75.3 | 5.56 | Tight High-Spin Breakers |
| 278 | Bradford, Ethan | NEW_YOR13 | Slider | 145 | 43.6 | 0.287 | -1.1 | 5.9 | 2428 | 82.2 | 5.43 | Tight High-Spin Breakers |
| 279 | Smith, Donny | JOL_SLA | Slider | 66 | 43.6 | 0.245 | -2.4 | -5.4 | 2476 | 78.5 | 5.16 | Tight High-Spin Breakers |
| 280 | Pindel, Buddie | SCH_BOO | Slider | 173 | 43.5 | 0.261 | 1.8 | -7.0 | 2466 | 81.6 | 5.36 | Tight High-Spin Breakers |
| 281 | Godwin, Connor | NEW_YOR13 | Slider | 93 | 43.4 | 0.262 | 0.0 | -10.2 | 2535 | 82.4 | 6.11 | Tight High-Spin Breakers |
| 282 | Brouwer, Adam | LAK_ERI24 | Curveball | 65 | 43.4 | 0.267 | -8.9 | -6.5 | 2357 | 78.1 | 5.33 | Tight High-Spin Breakers |
| 283 | Simpson, Garret | EVA_OTT | Changeup | 88 | 43.4 | 0.293 | 4.6 | 10.7 | 1711 | 83.8 | 5.17 | Tight High-Spin Breakers |
| 284 | Burcham, Jacob | GAT_GRI | Slider | 117 | 43.3 | 0.253 | 0.2 | -9.9 | 2395 | 80.8 | 5.84 | Tight High-Spin Breakers |
| 285 | Martzolf, Max | OTT_TIT | Four-Seam | 71 | 43.3 | 0.247 | 10.5 | -20.4 | 2140 | 84.5 | 5.83 | Tight High-Spin Breakers |
| 286 | Fuenmayor, Liu | OTT_TIT | Sinker | 65 | 43.2 | 0.248 | 10.0 | -20.6 | 2248 | 90.8 | 4.57 | Tight High-Spin Breakers |
| 287 | Valdez, Alex | EVA_OTT | Slider | 129 | 43.2 | 0.241 | 3.5 | -2.5 | 2167 | 85.8 | 5.30 | Tight High-Spin Breakers |
| 288 | Martzolf, Max | OTT_TIT | Curveball | 71 | 43.2 | 0.291 | -4.2 | 11.1 | 2155 | 73.9 | 5.43 | Tight High-Spin Breakers |
| 289 | Good, Ty | GAT_GRI | Curveball | 155 | 43.1 | 0.258 | -7.6 | -4.5 | 2128 | 75.0 | 5.62 | Tight High-Spin Breakers |
| 290 | Cook, Cole | SCH_BOO | Cutter | 109 | 43.0 | 0.227 | 9.2 | -3.6 | 2410 | 82.4 | 5.25 | Tight High-Spin Breakers |
| 291 | Moore, Kyle | SCH_BOO | Changeup | 94 | 42.9 | 0.262 | 9.9 | 16.4 | 2031 | 82.6 | 4.68 | Tight High-Spin Breakers |
| 292 | Westcott, Zac | FLO_Y'A | Changeup | 196 | 42.4 | 0.263 | 6.5 | 16.7 | 1915 | 76.5 | 5.73 | Tight High-Spin Breakers |
| 293 | Noble, Nick | FDU_KNI | Changeup | 71 | 42.1 | 0.303 | 0.2 | 17.6 | 1612 | 77.3 | 5.00 | Tight High-Spin Breakers |
| 294 | Escobar, Anthony | TRO_AIG | Slider | 249 | 42.1 | 0.281 | 3.5 | -5.0 | 2168 | 81.8 | 6.07 | Tight High-Spin Breakers |
| 295 | Serrano, Elio | NEW_JER6 | Slider | 128 | 42.1 | 0.259 | 5.6 | -2.1 | 2246 | 82.7 | 5.30 | Tight High-Spin Breakers |
| 296 | Hampton, Ky | OTT_TIT | Slider | 105 | 41.8 | 0.262 | 1.4 | -4.5 | 2286 | 83.6 | 5.82 | Tight High-Spin Breakers |
| 297 | Kostura, Brit | WAS_WIL3 | Slider | 56 | 41.8 | 0.273 | -0.7 | 5.1 | 2157 | 74.8 | 5.04 | Tight High-Spin Breakers |
| 298 | Delaney, Carter | WIN_CIT29 | Slider | 73 | 41.7 | 0.298 | -0.3 | -7.4 | 2304 | 80.0 | 5.47 | Tight High-Spin Breakers |
| 299 | Dima, Josh | GAT_GRI | Curveball | 54 | 41.6 | 0.277 | -3.6 | 2.1 | 1961 | 80.3 | 5.99 | Tight High-Spin Breakers |
| 300 | Barker, Alex | NEW_YOR13 | Curveball | 90 | 41.2 | 0.263 | -5.6 | 10.1 | 2256 | 76.3 | 5.75 | Tight High-Spin Breakers |
| 301 | Bradford, Ethan | NEW_YOR13 | Sinker | 239 | 41.1 | 0.260 | 6.9 | -15.8 | 2178 | 90.0 | 5.68 | Tight High-Spin Breakers |
| 302 | Bice, Emmett | NEW_YOR13 | Curveball | 170 | 41.0 | 0.296 | -10.3 | -13.3 | 2986 | 79.1 | 5.51 | Tight High-Spin Breakers |
| 303 | Gollert, Harley | TRO_AIG | Slider | 71 | 40.9 | 0.283 | -1.9 | 7.7 | 2221 | 78.2 | 4.91 | Tight High-Spin Breakers |
| 304 | Shinn, Nathan | LAK_ERI24 | Curveball | 88 | 40.5 | 0.279 | -5.9 | 0.6 | 2113 | 79.6 | 5.29 | Tight High-Spin Breakers |
| 305 | Sabatine, Gino | TRI_VAL | Slider | 138 | 40.5 | 0.292 | 4.2 | -3.6 | 2322 | 79.9 | 4.89 | Tight High-Spin Breakers |
| 306 | Vitas, Ben | JOL_SLA | Slider | 154 | 40.4 | 0.262 | 1.7 | -3.9 | 2116 | 81.4 | 4.95 | Tight High-Spin Breakers |
| 307 | Sanchez, Edwin | LAK_ERI24 | Changeup | 115 | 40.4 | 0.285 | 6.5 | -15.7 | 1943 | 80.0 | 5.79 | Tight High-Spin Breakers |
| 308 | Sanchez, Dikember | LAK_ERI24 | Slider | 111 | 40.4 | 0.275 | 2.1 | -3.7 | 2555 | 85.9 | 5.32 | Tight High-Spin Breakers |
| 309 | Parsons, Billy | SUS_COU1 | Slider | 241 | 40.3 | 0.251 | 5.9 | -6.3 | 2486 | 82.9 | 5.45 | Tight High-Spin Breakers |
| 310 | Galva, Claudio | GAT_GRI | Slider | 192 | 40.2 | 0.269 | 2.9 | -0.5 | 2254 | 83.7 | 4.78 | Tight High-Spin Breakers |
| 311 | Andueza, Axel | DOW_EAS1 | Slider | 116 | 40.2 | 0.282 | -0.6 | -1.5 | 2073 | 80.7 | 5.22 | Tight High-Spin Breakers |
| 312 | Sechrist, Zander | WAS_WIL3 | Sinker | 98 | 40.2 | 0.269 | 13.2 | -17.8 | 1893 | 80.1 | 5.60 | Tight High-Spin Breakers |
| 313 | Thornton, Tyler | NEW_ENG23 | Slider | 138 | 40.1 | 0.292 | 1.9 | -0.2 | 1925 | 80.0 | 4.93 | Tight High-Spin Breakers |
| 314 | Fauci, Sonny | NEW_JER6 | Curveball | 99 | 40.0 | 0.328 | -14.9 | -6.6 | 2324 | 78.6 | 5.90 | Tight High-Spin Breakers |
| 315 | Kassebaum, Torin | LON_ISL22 | Curveball | 55 | 39.9 | 0.308 | 1.1 | 10.2 | 2155 | 71.6 | 5.31 | Tight High-Spin Breakers |
| 316 | Nova, Fraynel | LAK_ERI24 | Curveball | 51 | 39.3 | 0.290 | -4.5 | -6.4 | 2301 | 80.1 | 5.61 | Tight High-Spin Breakers |
| 317 | Williams, Pierce | NEW_ENG23 | Curveball | 151 | 38.8 | 0.279 | -5.7 | 6.4 | 2172 | 75.4 | 5.77 | Tight High-Spin Breakers |
| 318 | Quigley, Michael | NEW_ENG23 | Curveball | 79 | 38.5 | 0.296 | -12.3 | -12.7 | 2567 | 78.8 | 5.42 | Tight High-Spin Breakers |
| 319 | Campbell, Tyler | MIS_MUD | Sinker | 124 | 37.7 | 0.275 | 7.3 | -9.7 | 2284 | 84.6 | 6.15 | Tight High-Spin Breakers |
| 320 | Eldred, Zach | NEW_ENG23 | Curveball | 81 | 37.6 | 0.316 | -9.8 | -12.4 | 2489 | 77.6 | 5.88 | Tight High-Spin Breakers |
| 321 | Chabot, Henry | LAK_ERI24 | Slider | 69 | 37.5 | 0.335 | 4.0 | -1.5 | 2413 | 84.3 | 5.11 | Tight High-Spin Breakers |
| 322 | Soto, Carlos | JOL_SLA | Slider | 96 | 37.4 | 0.302 | -1.8 | -8.8 | 2509 | 78.2 | 5.09 | Tight High-Spin Breakers |
| 323 | Villalobos, Jonaiker | FLO_Y'A | Curveball | 110 | 37.4 | 0.274 | -5.3 | 5.5 | 2264 | 74.7 | 5.32 | Tight High-Spin Breakers |
| 324 | Sechrist, Zander | WAS_WIL3 | Changeup | 207 | 37.0 | 0.294 | 7.6 | -14.7 | 1674 | 76.8 | 5.66 | Tight High-Spin Breakers |
| 325 | Gartland, Chad | TRI_VAL | Slider | 85 | 37.0 | 0.250 | 4.9 | -1.3 | 2222 | 82.3 | 6.07 | Tight High-Spin Breakers |
| 326 | Gorgen, Grady | NEW_YOR13 | Curveball | 75 | 36.8 | 0.283 | -7.2 | 6.9 | 2124 | 80.0 | 5.66 | Tight High-Spin Breakers |
| 327 | Brodsky, Jack | WAS_WIL3 | Curveball | 83 | 36.3 | 0.327 | -8.7 | -11.7 | 2668 | 76.9 | 5.33 | Tight High-Spin Breakers |
| 328 | Lawson, Nathan | FLO_Y'A | Cutter | 71 | 36.3 | 0.259 | 7.4 | -1.6 | 2291 | 83.4 | 5.72 | Tight High-Spin Breakers |
| 329 | Eldred, Zach | NEW_ENG23 | Slider | 169 | 35.5 | 0.297 | 1.9 | -7.3 | 2413 | 82.3 | 5.86 | Tight High-Spin Breakers |
| 330 | Tiburcio, David | DOW_EAS1 | Slider | 89 | 35.1 | 0.302 | 6.3 | 0.9 | 2341 | 86.3 | 5.41 | Tight High-Spin Breakers |
| 331 | McEvoy, Aidan | FLO_Y'A | Changeup | 54 | 34.7 | 0.276 | 3.2 | -13.8 | 1727 | 83.0 | 6.24 | Tight High-Spin Breakers |
| 332 | Gorgen, Grady | NEW_YOR13 | Slider | 124 | 34.4 | 0.309 | 1.5 | 0.9 | 2152 | 83.2 | 5.95 | Tight High-Spin Breakers |
| 333 | Voytko, Fawster | TRO_AIG | Curveball | 65 | 33.9 | 0.331 | -7.3 | -11.8 | 2338 | 74.6 | 6.05 | Tight High-Spin Breakers |
| 334 | Galva, Claudio | GAT_GRI | Sinker | 182 | 33.3 | 0.292 | 10.4 | -12.3 | 1989 | 89.1 | 4.94 | Tight High-Spin Breakers |
| 335 | Voytko, Fawster | TRO_AIG | Slider | 51 | 32.4 | 0.310 | 0.7 | -11.9 | 2334 | 78.5 | 6.23 | Tight High-Spin Breakers |
| 336 | Miranda, Kevin | OTT_TIT | Slider | 78 | 31.6 | 0.338 | 3.7 | -0.3 | 2222 | 81.1 | 5.60 | Tight High-Spin Breakers |
| 337 | Catrambone, Ben | JOL_SLA | Slider | 108 | 30.9 | 0.347 | 2.1 | -1.6 | 2266 | 82.6 | 4.86 | Tight High-Spin Breakers |
| 338 | Townes, Holland | SCH_BOO | Cutter | 61 | 28.6 | 0.299 | 3.3 | -2.0 | 2145 | 83.7 | 4.95 | Tight High-Spin Breakers |
| 339 | Cameron, Wyatt | SCH_BOO | Curveball | 109 | 26.8 | 0.359 | -13.5 | -9.7 | 2296 | 81.1 | 5.24 | Tight High-Spin Breakers |
| 340 | Johnston, Spencer | DOW_EAS1 | Curveball | 66 | 25.2 | 0.323 | -4.7 | -6.0 | 2133 | 74.4 | 5.68 | Tight High-Spin Breakers |
| 341 | Plumadore, Carson | WIN_CIT29 | Curveball | 77 | 21.9 | 0.366 | 1.3 | -6.9 | 2483 | 75.4 | 5.57 | Tight High-Spin Breakers |
| 342 | Lovin, Xander | GAT_GRI | Curveball | 65 | 21.1 | 0.355 | -9.3 | -12.3 | 2634 | 76.9 | 4.64 | Tight High-Spin Breakers |
| 343 | Westcott, Zac | FLO_Y'A | Curveball | 163 | 20.7 | 0.378 | -15.2 | -9.2 | 1872 | 67.1 | 5.48 | Tight High-Spin Breakers |
| 344 | Lawson, Nathan | FLO_Y'A | Changeup | 60 | 78.2 | 0.166 | 7.9 | 10.2 | 1409 | 79.6 | 5.77 | Soft-Speed Separation |
| 345 | Serrano, Elio | NEW_JER6 | Changeup | 63 | 75.9 | 0.148 | 11.1 | 11.7 | 1829 | 82.1 | 5.92 | Soft-Speed Separation |
| 346 | Grounds, Jackson | DOW_EAS1 | Four-Seam | 107 | 74.4 | 0.159 | 17.0 | 14.2 | 2163 | 92.5 | 5.59 | Soft-Speed Separation |
| 347 | Davis, Tyler | WIN_CIT29 | Four-Seam | 76 | 74.4 | 0.111 | 21.2 | 5.6 | 2171 | 89.3 | 5.86 | Soft-Speed Separation |
| 348 | Debban, Caleb | NEW_JER6 | Four-Seam | 57 | 73.8 | 0.174 | 13.1 | -4.6 | 2325 | 87.2 | 6.58 | Soft-Speed Separation |
| 349 | Garcia, Hector | WAS_WIL3 | Splitter | 62 | 73.6 | 0.185 | 11.7 | 7.6 | 1216 | 78.2 | 5.92 | Soft-Speed Separation |
| 350 | Escobar, Anthony | TRO_AIG | Changeup | 147 | 72.7 | 0.156 | 10.3 | 11.7 | 1630 | 79.1 | 6.21 | Soft-Speed Separation |
| 351 | Lockhart, Gauge | LAK_ERI24 | Cutter | 95 | 72.5 | 0.160 | 5.4 | -0.9 | 2105 | 86.6 | 6.09 | Soft-Speed Separation |
| 352 | Cameron, Zach | WIN_CIT29 | Four-Seam | 115 | 71.7 | 0.201 | 15.7 | 10.2 | 2169 | 88.1 | 5.54 | Soft-Speed Separation |
| 353 | Webster, Evan | FLO_Y'A | Cutter | 133 | 71.1 | 0.166 | 5.5 | -0.3 | 2041 | 84.4 | 6.94 | Soft-Speed Separation |
| 354 | Rodriguez, Joe Joe | NEW_JER6 | Changeup | 125 | 70.6 | 0.155 | 8.4 | 15.2 | 1810 | 81.7 | 5.32 | Soft-Speed Separation |
| 355 | Riedel, Caleb | SCH_BOO | Sinker | 77 | 70.0 | 0.141 | 16.3 | -15.9 | 2308 | 88.8 | 6.00 | Soft-Speed Separation |
| 356 | Harris, Everette | TRI_VAL | Changeup | 96 | 69.7 | 0.168 | 2.1 | 16.6 | 2144 | 82.6 | 6.54 | Soft-Speed Separation |
| 357 | Still, Stephen | TRI_VAL | Sinker | 61 | 69.5 | 0.212 | 14.1 | -18.1 | 2325 | 90.6 | 5.39 | Soft-Speed Separation |
| 358 | Glickstein, Aaron | SCH_BOO | Sinker | 101 | 68.3 | 0.180 | 9.4 | 13.8 | 2164 | 88.3 | 6.10 | Soft-Speed Separation |
| 359 | Grounds, Jackson | TRO_AIG | Four-Seam | 62 | 67.9 | 0.148 | 14.6 | 12.2 | 2229 | 92.4 | 5.79 | Soft-Speed Separation |
| 360 | Correa, Nelvin | QUE_CAP | Cutter | 110 | 67.6 | 0.167 | 11.8 | -0.5 | 2243 | 87.5 | 5.98 | Soft-Speed Separation |
| 361 | Coles, Chad | WAS_WIL3 | Splitter | 63 | 67.6 | 0.164 | 2.3 | 7.1 | 1031 | 86.2 | 5.59 | Soft-Speed Separation |
| 362 | Correa, Nelvin | QUE_CAP | Four-Seam | 86 | 67.2 | 0.192 | 15.4 | 7.3 | 2109 | 89.3 | 5.95 | Soft-Speed Separation |
| 363 | Foy, Corbin | LAK_ERI24 | Four-Seam | 96 | 65.8 | 0.177 | 16.5 | 10.4 | 2337 | 91.3 | 6.15 | Soft-Speed Separation |
| 364 | Wiltse, Ryan | EVA_OTT | Changeup | 150 | 65.8 | 0.203 | 14.0 | 10.2 | 1838 | 78.5 | 6.32 | Soft-Speed Separation |
| 365 | Pindel, Buddie | SCH_BOO | Splitter | 89 | 65.3 | 0.221 | 4.9 | 7.2 | 1105 | 80.3 | 5.76 | Soft-Speed Separation |
| 366 | Villers, Ian | QUE_CAP | Splitter | 64 | 65.2 | 0.219 | 7.5 | 11.5 | 1086 | 83.1 | 5.98 | Soft-Speed Separation |
| 367 | Colon, Jeffrey | TRO_AIG | Sinker | 56 | 64.9 | 0.170 | 13.9 | 17.7 | 2262 | 90.2 | 5.61 | Soft-Speed Separation |
| 368 | Drakeford, Dosie | NEW_JER6 | Changeup | 84 | 64.7 | 0.159 | 9.9 | 14.8 | 1850 | 81.0 | 6.11 | Soft-Speed Separation |
| 369 | Tokar, Heitor | OTT_TIT | Changeup | 70 | 64.6 | 0.198 | 9.5 | 13.2 | 1391 | 82.1 | 6.08 | Soft-Speed Separation |
| 370 | Sesar, Jorden | SUS_COU1 | Changeup | 75 | 64.3 | 0.181 | 12.2 | 11.6 | 1988 | 83.2 | 6.45 | Soft-Speed Separation |
| 371 | Gregory, Ben | GAT_GRI | Four-Seam | 93 | 64.1 | 0.186 | 15.7 | 13.6 | 2230 | 88.9 | 6.45 | Soft-Speed Separation |
| 372 | Leak, Anthony | NEW_YOR13 | Changeup | 75 | 64.0 | 0.199 | 6.0 | 11.3 | 1728 | 83.1 | 6.52 | Soft-Speed Separation |
| 373 | Widener, Jacob | SUS_COU1 | Sinker | 139 | 63.7 | 0.189 | 9.0 | -11.4 | 2364 | 88.9 | 6.94 | Soft-Speed Separation |
| 374 | Garbrick, Alex | LAK_ERI24 | Four-Seam | 82 | 63.4 | 0.224 | 15.2 | 10.7 | 2266 | 91.4 | 5.61 | Soft-Speed Separation |
| 375 | Maietta, Dante | WIN_CIT29 | Changeup | 259 | 63.3 | 0.186 | 15.2 | 13.7 | 1858 | 77.9 | 6.31 | Soft-Speed Separation |
| 376 | Mannering, Shawn | DOW_EAS1 | Sinker | 59 | 63.3 | 0.258 | 13.5 | 18.6 | 2231 | 89.1 | 5.82 | Soft-Speed Separation |
| 377 | Garcia, Andrew | EVA_OTT | Sinker | 52 | 62.9 | 0.239 | 10.5 | 14.2 | 2058 | 91.0 | 5.92 | Soft-Speed Separation |
| 378 | Brown, Ethan | WAS_WIL3 | Four-Seam | 67 | 62.2 | 0.217 | 12.7 | -10.8 | 2077 | 90.4 | 6.09 | Soft-Speed Separation |
| 379 | Hensey, Rob | SUS_COU1 | Four-Seam | 220 | 62.2 | 0.187 | 16.5 | -13.9 | 2201 | 92.1 | 6.20 | Soft-Speed Separation |
| 380 | Morgan, Cooper | QUE_CAP | Four-Seam | 65 | 61.9 | 0.208 | 13.8 | -8.3 | 2214 | 87.4 | 6.11 | Soft-Speed Separation |
| 381 | Cartwright, Eli | GAT_GRI | Four-Seam | 207 | 61.5 | 0.194 | 18.4 | -8.6 | 2100 | 90.3 | 6.40 | Soft-Speed Separation |
| 382 | Willeman, Landon | EVA_OTT | Changeup | 179 | 61.2 | 0.202 | 6.2 | 14.5 | 1696 | 84.0 | 6.23 | Soft-Speed Separation |
| 383 | Anderson, Colt | WAS_WIL3 | Four-Seam | 258 | 61.0 | 0.215 | 11.8 | -6.9 | 2042 | 88.8 | 6.68 | Soft-Speed Separation |
| 384 | Mercado, Nelson | OTT_TIT | Four-Seam | 81 | 60.8 | 0.169 | 19.2 | 12.6 | 2126 | 87.8 | 5.67 | Soft-Speed Separation |
| 385 | Shears, Tanner | SCH_BOO | Four-Seam | 219 | 60.6 | 0.190 | 16.8 | 12.4 | 2036 | 92.3 | 5.18 | Soft-Speed Separation |
| 386 | Petschke, Ben | EVA_OTT | Sinker | 54 | 60.6 | 0.206 | 6.5 | 13.1 | 2110 | 90.0 | 5.27 | Soft-Speed Separation |
| 387 | Hensey, Rob | SUS_COU1 | Changeup | 277 | 60.5 | 0.212 | 6.4 | -15.8 | 1698 | 84.1 | 6.13 | Soft-Speed Separation |
| 388 | Plumadore, Carson | WIN_CIT29 | Changeup | 269 | 60.5 | 0.196 | 8.6 | 18.8 | 2259 | 83.3 | 5.93 | Soft-Speed Separation |
| 389 | Lovell, Justin | WIN_CIT29 | Sinker | 129 | 60.5 | 0.175 | 12.3 | -14.9 | 2239 | 93.1 | 6.27 | Soft-Speed Separation |
| 390 | Zaffiro, Cole | SCH_BOO | Four-Seam | 289 | 60.1 | 0.195 | 18.0 | 8.1 | 2159 | 90.7 | 6.04 | Soft-Speed Separation |
| 391 | Bell, Brendan | NEW_ENG23 | Cutter | 85 | 59.9 | 0.218 | 9.3 | -0.3 | 2392 | 92.0 | 5.79 | Soft-Speed Separation |
| 392 | Wehrle, Tyler | WIN_CIT29 | Four-Seam | 236 | 59.8 | 0.189 | 16.5 | 14.0 | 2322 | 91.3 | 5.66 | Soft-Speed Separation |
| 393 | Hungate, Chase | NEW_JER6 | Sinker | 66 | 59.7 | 0.202 | 0.2 | 20.5 | 2240 | 88.3 | 5.79 | Soft-Speed Separation |
| 394 | Martinez, Mason | TRI_VAL | Slider | 132 | 59.7 | 0.213 | 6.4 | 0.1 | 2349 | 83.3 | 6.40 | Soft-Speed Separation |
| 395 | Harley, Tristan | SUS_COU1 | Sinker | 97 | 59.6 | 0.188 | 11.7 | 14.7 | 1999 | 92.1 | 5.83 | Soft-Speed Separation |
| 396 | Sabatine, Gino | TRI_VAL | Sinker | 54 | 59.6 | 0.194 | 9.5 | 14.0 | 1890 | 88.2 | 5.03 | Soft-Speed Separation |
| 397 | Kaminer, Brandon | DOW_EAS1 | Four-Seam | 185 | 59.5 | 0.227 | 18.1 | -4.8 | 2365 | 89.4 | 5.38 | Soft-Speed Separation |
| 398 | Ortiz, Julio | GAT_GRI | Four-Seam | 330 | 59.4 | 0.199 | 18.2 | 8.2 | 2173 | 95.3 | 6.12 | Soft-Speed Separation |
| 399 | Dima, Josh | GAT_GRI | Four-Seam | 238 | 59.3 | 0.205 | 18.1 | -10.8 | 2054 | 90.3 | 6.22 | Soft-Speed Separation |
| 400 | Webster, Evan | FLO_Y'A | Slider | 111 | 59.3 | 0.201 | 3.0 | 0.9 | 1957 | 81.4 | 6.82 | Soft-Speed Separation |
| 401 | Gartland, Chad | TRI_VAL | Changeup | 52 | 59.2 | 0.206 | 8.3 | 14.4 | 1716 | 84.0 | 6.01 | Soft-Speed Separation |
| 402 | VanMarter, Luke | LEM_COL | Changeup | 53 | 59.2 | 0.256 | 12.9 | 11.7 | 1756 | 77.6 | 6.55 | Soft-Speed Separation |
| 403 | Langhorne, Miles | SUS_COU1 | Four-Seam | 70 | 59.1 | 0.246 | 14.2 | 3.8 | 2304 | 93.9 | 6.50 | Soft-Speed Separation |
| 404 | MacMillan, Blake | TRO_AIG | Four-Seam | 148 | 59.0 | 0.201 | 21.9 | -5.8 | 2200 | 88.3 | 5.56 | Soft-Speed Separation |
| 405 | Cerda, Junior | EVA_OTT | Sinker | 114 | 58.9 | 0.211 | 11.5 | 16.5 | 2194 | 93.7 | 5.34 | Soft-Speed Separation |
| 406 | Brothers, Kellen | SUS_COU1 | Changeup | 177 | 58.8 | 0.218 | 10.5 | 12.0 | 1497 | 79.9 | 6.06 | Soft-Speed Separation |
| 407 | Foster, Kobe | WAS_WIL3 | Four-Seam | 442 | 58.7 | 0.194 | 20.6 | -9.8 | 2207 | 86.7 | 5.72 | Soft-Speed Separation |
| 408 | Garcia, Brett | OTT_TIT | Four-Seam | 258 | 58.7 | 0.203 | 17.1 | 6.4 | 2365 | 91.8 | 6.14 | Soft-Speed Separation |
| 409 | Barreto, Brayhans | TRI_VAL | Changeup | 115 | 58.7 | 0.234 | 11.0 | -13.0 | 1788 | 81.0 | 6.11 | Soft-Speed Separation |
| 410 | Good, Ty | GAT_GRI | Cutter | 58 | 58.6 | 0.207 | 17.0 | 7.6 | 2059 | 88.4 | 6.14 | Soft-Speed Separation |
| 411 | Kelly, Colin | SUS_COU1 | Four-Seam | 82 | 58.4 | 0.214 | 17.4 | 10.6 | 1990 | 90.6 | 5.94 | Soft-Speed Separation |
| 412 | Rodriguez, Joe Joe | NEW_JER6 | Four-Seam | 83 | 58.4 | 0.207 | 16.6 | 13.4 | 2119 | 91.8 | 5.75 | Soft-Speed Separation |
| 413 | Morgan, Marcus | JOL_SLA | Sinker | 96 | 58.1 | 0.227 | 10.3 | 15.2 | 2455 | 91.9 | 6.20 | Soft-Speed Separation |
| 414 | McMahon, Chris | LAK_ERI24 | Four-Seam | 69 | 58.0 | 0.234 | 13.9 | 9.7 | 2266 | 88.2 | 6.54 | Soft-Speed Separation |
| 415 | Saturria, Michael | NEW_ENG23 | Cutter | 245 | 58.0 | 0.238 | 12.9 | -0.8 | 2505 | 86.5 | 6.38 | Soft-Speed Separation |
| 416 | Brouwer, Adam | LAK_ERI24 | Four-Seam | 50 | 57.9 | 0.206 | 18.6 | 8.4 | 2133 | 91.0 | 5.92 | Soft-Speed Separation |
| 417 | Duby, Bill | NEW_JER6 | Slider | 80 | 57.6 | 0.205 | 7.8 | 0.3 | 2041 | 79.7 | 6.56 | Soft-Speed Separation |
| 418 | Pardinho, Eric | OTT_TIT | Changeup | 119 | 57.5 | 0.227 | 4.5 | 15.0 | 1607 | 84.1 | 5.39 | Soft-Speed Separation |
| 419 | Herbert, Andrew | WAS_WIL3 | Four-Seam | 55 | 57.5 | 0.175 | 15.8 | 10.9 | 2226 | 91.2 | 6.43 | Soft-Speed Separation |
| 420 | Boies, Emiles | QUE_CAP | Changeup | 215 | 57.4 | 0.204 | 11.8 | 15.0 | 1931 | 82.5 | 6.21 | Soft-Speed Separation |
| 421 | Riedel, Caleb | SCH_BOO | Four-Seam | 231 | 57.3 | 0.245 | 17.3 | -15.1 | 2338 | 89.3 | 5.84 | Soft-Speed Separation |
| 422 | Grounds, Jackson | DOW_EAS1 | Sinker | 116 | 57.2 | 0.215 | 15.0 | 16.4 | 2139 | 92.2 | 5.50 | Soft-Speed Separation |
| 423 | Long, Maddox | WAS_WIL3 | Four-Seam | 155 | 56.8 | 0.222 | 12.7 | 9.4 | 2343 | 91.7 | 6.13 | Soft-Speed Separation |
| 424 | Turner, Eric | JOL_SLA | Sinker | 91 | 56.8 | 0.213 | 15.0 | 16.0 | 2311 | 88.3 | 5.14 | Soft-Speed Separation |
| 425 | McCartney, Seth | MIS_MUD | Sinker | 120 | 56.7 | 0.238 | 10.4 | 15.2 | 2316 | 90.2 | 5.76 | Soft-Speed Separation |
| 426 | Henderson, Drew | DOW_EAS1 | Sinker | 115 | 56.7 | 0.213 | 16.1 | 15.5 | 2211 | 88.9 | 5.61 | Soft-Speed Separation |
| 427 | Lawson, Nathan | FLO_Y'A | Sinker | 186 | 56.7 | 0.211 | 9.8 | 15.8 | 2196 | 88.9 | 6.15 | Soft-Speed Separation |
| 428 | Debban, Caleb | NEW_JER6 | Cutter | 142 | 56.6 | 0.238 | 10.7 | -0.4 | 2337 | 85.9 | 6.59 | Soft-Speed Separation |
| 429 | Dill, Austin | TRI_VAL | Changeup | 204 | 56.4 | 0.209 | 10.7 | 16.5 | 1931 | 80.5 | 5.23 | Soft-Speed Separation |
| 430 | Vilchez, Michael | OTT_TIT | Four-Seam | 138 | 56.3 | 0.211 | 16.1 | 9.0 | 2256 | 93.7 | 6.28 | Soft-Speed Separation |
| 431 | McEvoy, Aidan | FLO_Y'A | Cutter | 81 | 56.3 | 0.215 | 7.6 | 1.4 | 2151 | 83.0 | 6.10 | Soft-Speed Separation |
| 432 | Glickstein, Aaron | SCH_BOO | Four-Seam | 184 | 56.1 | 0.211 | 14.6 | 9.6 | 2236 | 89.1 | 6.12 | Soft-Speed Separation |
| 433 | Jones, Breyln | NEW_JER6 | Slider | 97 | 56.1 | 0.212 | 8.1 | -0.7 | 2078 | 86.1 | 5.85 | Soft-Speed Separation |
| 434 | Brouwer, Adam | LAK_ERI24 | Four-Seam | 165 | 56.1 | 0.197 | 19.3 | 10.3 | 2257 | 90.4 | 5.92 | Soft-Speed Separation |
| 435 | Long, Maddox | WAS_WIL3 | Sinker | 285 | 56.0 | 0.234 | 7.1 | 16.6 | 2182 | 89.9 | 5.89 | Soft-Speed Separation |
| 436 | Williams, Pierce | NEW_ENG23 | Four-Seam | 267 | 55.9 | 0.215 | 16.6 | -11.4 | 1922 | 85.7 | 6.16 | Soft-Speed Separation |
| 437 | Flontek, Zac | DOW_EAS1 | Cutter | 51 | 55.8 | 0.235 | 8.1 | -1.6 | 2644 | 88.6 | 6.05 | Soft-Speed Separation |
| 438 | Fritz, AJ | MIS_MUD | Sinker | 55 | 55.6 | 0.239 | 6.8 | 16.5 | 2042 | 88.4 | 5.39 | Soft-Speed Separation |
| 439 | Salata, Derek | SCH_BOO | Splitter | 92 | 55.4 | 0.202 | 7.1 | 9.2 | 1133 | 83.2 | 5.79 | Soft-Speed Separation |
| 440 | Petery, Dylan | WIN_CIT29 | Four-Seam | 64 | 55.4 | 0.252 | 17.4 | 10.0 | 2349 | 86.3 | 6.10 | Soft-Speed Separation |
| 441 | Sanchez, Edwin | LAK_ERI24 | Four-Seam | 177 | 55.3 | 0.201 | 15.4 | -13.3 | 2092 | 87.0 | 5.51 | Soft-Speed Separation |
| 442 | Odonnell, Brendan | NEW_ENG23 | Four-Seam | 69 | 55.3 | 0.249 | 13.5 | -7.4 | 2453 | 91.4 | 6.98 | Soft-Speed Separation |
| 443 | Long, Jalon | NEW_YOR13 | Four-Seam | 213 | 55.2 | 0.200 | 20.4 | 8.2 | 2129 | 92.0 | 6.09 | Soft-Speed Separation |
| 444 | Shinn, Nathan | LAK_ERI24 | Four-Seam | 250 | 55.2 | 0.214 | 17.4 | -9.5 | 1970 | 89.1 | 5.88 | Soft-Speed Separation |
| 445 | Thompson, Ross | SCH_BOO | Splitter | 175 | 55.2 | 0.229 | 3.9 | 9.3 | 1055 | 79.5 | 5.44 | Soft-Speed Separation |
| 446 | Gorgen, Grady | NEW_YOR13 | Cutter | 74 | 55.2 | 0.208 | 8.0 | -3.5 | 2123 | 86.5 | 6.25 | Soft-Speed Separation |
| 447 | O'Dell, Casey | JOL_SLA | Four-Seam | 114 | 55.1 | 0.202 | 17.8 | 8.8 | 2210 | 91.2 | 6.07 | Soft-Speed Separation |
| 448 | Odonnell, Brendan | NEW_ENG23 | Sinker | 91 | 55.0 | 0.238 | 8.1 | -11.6 | 2351 | 90.2 | 6.95 | Soft-Speed Separation |
| 449 | Cooper, Garrett | NEW_YOR13 | Changeup | 278 | 55.0 | 0.238 | 8.7 | 8.0 | 1400 | 77.7 | 6.39 | Soft-Speed Separation |
| 450 | Calderon, Jean | LAK_ERI24 | Four-Seam | 87 | 55.0 | 0.243 | 12.0 | 0.8 | 2526 | 94.1 | 6.38 | Soft-Speed Separation |
| 451 | McKillican, Adam | QUE_CAP | Changeup | 70 | 54.9 | 0.212 | 10.3 | 13.1 | 1714 | 85.5 | 6.79 | Soft-Speed Separation |
| 452 | Cameron, Zach | WIN_CIT29 | Changeup | 205 | 54.9 | 0.227 | 7.4 | 21.1 | 2121 | 80.3 | 5.55 | Soft-Speed Separation |
| 453 | Plumadore, Carson | WIN_CIT29 | Sinker | 127 | 54.8 | 0.199 | 13.7 | 18.5 | 2384 | 87.3 | 5.81 | Soft-Speed Separation |
| 454 | Sanchez, Sergio | MIS_MUD | Four-Seam | 140 | 54.6 | 0.202 | 15.2 | 9.9 | 2299 | 92.1 | 6.37 | Soft-Speed Separation |
| 455 | Bell, Brendan | NEW_ENG23 | Four-Seam | 140 | 54.6 | 0.269 | 11.0 | 3.0 | 2361 | 92.0 | 5.98 | Soft-Speed Separation |
| 456 | Whitesell, Max | FLO_Y'A | Changeup | 59 | 54.6 | 0.258 | 8.9 | 10.6 | 1626 | 85.2 | 6.38 | Soft-Speed Separation |
| 457 | Vega, Lucas | TRO_AIG | Changeup | 74 | 54.5 | 0.274 | 8.6 | 14.7 | 1967 | 83.6 | 6.24 | Soft-Speed Separation |
| 458 | Kelly, Colin | SUS_COU1 | Sinker | 96 | 54.5 | 0.189 | 14.3 | 15.8 | 2008 | 90.5 | 5.91 | Soft-Speed Separation |
| 459 | Ginn, Landon | WAS_WIL3 | Four-Seam | 142 | 54.4 | 0.244 | 15.4 | 3.4 | 2597 | 91.9 | 5.64 | Soft-Speed Separation |
| 460 | Daly, Ryan | JOL_SLA | Changeup | 242 | 54.4 | 0.243 | 5.1 | 16.2 | 2100 | 79.0 | 6.81 | Soft-Speed Separation |
| 461 | Burcham, Jacob | GAT_GRI | Changeup | 97 | 54.4 | 0.212 | 3.7 | 17.8 | 1899 | 83.4 | 6.18 | Soft-Speed Separation |
| 462 | Hopewell, Chase | FLO_Y'A | Four-Seam | 253 | 54.3 | 0.215 | 16.7 | 11.3 | 2216 | 92.9 | 6.49 | Soft-Speed Separation |
| 463 | Scafidi, Christian | LAK_ERI24 | Four-Seam | 287 | 54.3 | 0.213 | 17.7 | 4.8 | 2487 | 89.8 | 6.16 | Soft-Speed Separation |
| 464 | Aldeano, Austin | TRO_AIG | Sinker | 70 | 54.3 | 0.218 | 16.0 | 17.8 | 2219 | 90.2 | 6.06 | Soft-Speed Separation |
| 465 | Flontek, Zac | DOW_EAS1 | Four-Seam | 346 | 54.3 | 0.193 | 18.1 | 5.1 | 2595 | 91.6 | 6.49 | Soft-Speed Separation |
| 466 | Moore, Kyle | SCH_BOO | Four-Seam | 169 | 54.1 | 0.224 | 17.9 | 14.5 | 2172 | 88.4 | 4.69 | Soft-Speed Separation |
| 467 | MacMillan, Blake | TRO_AIG | Cutter | 144 | 54.1 | 0.214 | 21.8 | -6.9 | 2193 | 87.9 | 5.52 | Soft-Speed Separation |
| 468 | Almanzar, Elian | DOW_EAS1 | Four-Seam | 147 | 54.1 | 0.195 | 16.0 | 3.7 | 2279 | 95.1 | 6.18 | Soft-Speed Separation |
| 469 | Roland, Cole | QUE_CAP | Changeup | 71 | 54.1 | 0.246 | 10.4 | 9.6 | 2033 | 82.6 | 5.56 | Soft-Speed Separation |
| 470 | Alpern, Liam | FLO_Y'A | Four-Seam | 264 | 53.9 | 0.216 | 17.2 | -12.7 | 2227 | 89.1 | 6.04 | Soft-Speed Separation |
| 471 | Allemann, Braeden | QUE_CAP | Sinker | 65 | 53.9 | 0.224 | 15.4 | 16.0 | 2304 | 90.4 | 6.14 | Soft-Speed Separation |
| 472 | Hensey, Rob | SUS_COU1 | Sinker | 469 | 53.9 | 0.232 | 13.5 | -15.9 | 2143 | 91.7 | 6.25 | Soft-Speed Separation |
| 473 | Wilcenski, Blaise | WIN_CIT29 | Four-Seam | 58 | 53.9 | 0.202 | 15.3 | 9.4 | 2049 | 90.6 | 6.28 | Soft-Speed Separation |
| 474 | Vailes, Gage | GAT_GRI | Changeup | 161 | 53.9 | 0.236 | 6.2 | 11.1 | 1873 | 85.7 | 5.16 | Soft-Speed Separation |
| 475 | Gregory, Ben | GAT_GRI | Sinker | 227 | 53.8 | 0.212 | 14.7 | 15.9 | 2260 | 89.1 | 6.54 | Soft-Speed Separation |
| 476 | Martinez, Mason | TRI_VAL | Sinker | 347 | 53.7 | 0.232 | 12.1 | 18.9 | 2279 | 88.8 | 6.45 | Soft-Speed Separation |
| 477 | Toribio, Noe | TRO_AIG | Changeup | 265 | 53.6 | 0.248 | 6.9 | 16.4 | 1985 | 83.1 | 5.65 | Soft-Speed Separation |
| 478 | Agosto, Justus | TRI_VAL | Four-Seam | 78 | 53.5 | 0.221 | 17.6 | 8.1 | 2013 | 89.3 | 6.05 | Soft-Speed Separation |
| 479 | McEvoy, Aidan | FLO_Y'A | Four-Seam | 62 | 53.5 | 0.204 | 14.4 | -15.1 | 1962 | 90.1 | 6.45 | Soft-Speed Separation |
| 480 | Delaney, Carter | WIN_CIT29 | Four-Seam | 150 | 53.4 | 0.236 | 18.0 | 9.4 | 2226 | 88.9 | 6.30 | Soft-Speed Separation |
| 481 | Westcott, Zac | FLO_Y'A | Four-Seam | 327 | 53.4 | 0.217 | 16.5 | 14.5 | 2099 | 83.4 | 5.90 | Soft-Speed Separation |
| 482 | Perez, Kelvin | WAS_WIL3 | Four-Seam | 127 | 53.4 | 0.225 | 15.4 | 10.9 | 2077 | 89.1 | 6.14 | Soft-Speed Separation |
| 483 | Milburn, Isaac | FLO_Y'A | Sinker | 100 | 53.3 | 0.232 | 10.1 | -13.3 | 2067 | 88.1 | 5.48 | Soft-Speed Separation |
| 484 | Hargrove, Dawson | LAK_ERI24 | Four-Seam | 119 | 53.1 | 0.218 | 19.6 | 7.6 | 1991 | 89.7 | 5.48 | Soft-Speed Separation |
| 485 | Leak, Anthony | NEW_YOR13 | Sinker | 121 | 53.1 | 0.237 | 10.2 | 14.3 | 2114 | 89.2 | 6.31 | Soft-Speed Separation |
| 486 | Barraza, Chris | MIS_MUD | Four-Seam | 561 | 53.1 | 0.191 | 19.9 | 10.3 | 2453 | 93.2 | 5.86 | Soft-Speed Separation |
| 487 | Cerda, Junior | EVA_OTT | Four-Seam | 127 | 53.1 | 0.229 | 15.3 | 15.7 | 2225 | 93.2 | 5.52 | Soft-Speed Separation |
| 488 | Albert, Wes | TRI_VAL | Four-Seam | 125 | 53.0 | 0.193 | 16.1 | 9.3 | 2014 | 89.1 | 5.65 | Soft-Speed Separation |
| 489 | Daly, Ryan | JOL_SLA | Four-Seam | 567 | 52.9 | 0.238 | 14.7 | 13.4 | 2207 | 90.4 | 6.77 | Soft-Speed Separation |
| 490 | Fowler, Dalton | SUS_COU1 | Four-Seam | 89 | 52.8 | 0.233 | 14.6 | -10.9 | 2107 | 92.2 | 5.57 | Soft-Speed Separation |
| 491 | Hickey, Matt | GAT_GRI | Sinker | 67 | 52.8 | 0.239 | 5.8 | 17.9 | 2259 | 88.5 | 5.66 | Soft-Speed Separation |
| 492 | Vecerka, Boris | QUE_CAP | Sinker | 219 | 52.8 | 0.209 | 10.2 | 17.7 | 2434 | 93.3 | 5.87 | Soft-Speed Separation |
| 493 | Brothers, Kellen | SUS_COU1 | Sinker | 136 | 52.7 | 0.244 | 16.3 | 16.0 | 2347 | 89.1 | 6.43 | Soft-Speed Separation |
| 494 | Hughes, Grif | EVA_OTT | Four-Seam | 57 | 52.7 | 0.188 | 17.7 | -12.9 | 2419 | 88.0 | 6.38 | Soft-Speed Separation |
| 495 | Jones, Breyln | NEW_JER6 | Four-Seam | 53 | 52.6 | 0.277 | 13.4 | 6.3 | 1995 | 89.1 | 5.89 | Soft-Speed Separation |
| 496 | Castro, Alexander | TRO_AIG | Four-Seam | 115 | 52.5 | 0.245 | 18.2 | 14.6 | 2257 | 93.2 | 5.18 | Soft-Speed Separation |
| 497 | De Jesus, Larry | DOW_EAS1 | Four-Seam | 74 | 52.5 | 0.172 | 17.0 | 12.2 | 2407 | 90.0 | 5.25 | Soft-Speed Separation |
| 498 | McEvoy, Aidan | FLO_Y'A | Sinker | 186 | 52.4 | 0.222 | 12.9 | -16.5 | 1990 | 90.4 | 6.44 | Soft-Speed Separation |
| 499 | Bauer, Patrick | QUE_CAP | Four-Seam | 150 | 52.4 | 0.194 | 17.5 | 11.1 | 2381 | 87.8 | 6.43 | Soft-Speed Separation |
| 500 | Benitez, Jorge | NEW_JER6 | Sinker | 117 | 52.4 | 0.222 | 8.7 | -11.9 | 2140 | 93.3 | 6.07 | Soft-Speed Separation |
| 501 | Daly, Ryan | JOL_SLA | Sinker | 133 | 52.2 | 0.220 | 12.7 | 15.4 | 2200 | 90.2 | 6.93 | Soft-Speed Separation |
| 502 | Kelly, Aiden | TRI_VAL | Sinker | 78 | 52.2 | 0.243 | 9.3 | 13.8 | 2221 | 88.8 | 5.90 | Soft-Speed Separation |
| 503 | Brodsky, Jack | WAS_WIL3 | Four-Seam | 267 | 52.2 | 0.228 | 15.4 | 6.7 | 2170 | 90.6 | 6.12 | Soft-Speed Separation |
| 504 | Kines, Gunnar | JOL_SLA | Four-Seam | 511 | 52.2 | 0.221 | 17.3 | -12.3 | 2230 | 86.2 | 5.85 | Soft-Speed Separation |
| 505 | Webster, Evan | FLO_Y'A | Four-Seam | 508 | 52.2 | 0.217 | 16.6 | -10.8 | 1982 | 89.1 | 6.79 | Soft-Speed Separation |
| 506 | Webster, Evan | FLO_Y'A | Sinker | 63 | 52.2 | 0.239 | 15.6 | -11.2 | 1888 | 88.9 | 6.91 | Soft-Speed Separation |
| 507 | Tokar, Heitor | OTT_TIT | Four-Seam | 241 | 52.1 | 0.227 | 17.4 | 6.4 | 2015 | 88.1 | 6.39 | Soft-Speed Separation |
| 508 | Vail, Tyler | NEW_YOR13 | Changeup | 214 | 52.1 | 0.257 | 6.4 | 13.1 | 1798 | 83.1 | 6.21 | Soft-Speed Separation |
| 509 | Marynczak, Arlo | TRI_VAL | Four-Seam | 277 | 52.0 | 0.225 | 16.8 | 10.3 | 2143 | 88.8 | 6.35 | Soft-Speed Separation |
| 510 | Scott, Brandon | LAK_ERI24 | Four-Seam | 459 | 52.0 | 0.227 | 13.4 | -8.8 | 2304 | 88.8 | 6.19 | Soft-Speed Separation |
| 511 | Almonte, Lisandro | NEW_JER6 | Four-Seam | 210 | 52.0 | 0.209 | 16.4 | 12.7 | 2195 | 96.6 | 5.67 | Soft-Speed Separation |
| 512 | Balzan, Jackson | SUS_COU1 | Sinker | 142 | 51.9 | 0.220 | 17.3 | -14.6 | 2224 | 86.1 | 5.28 | Soft-Speed Separation |
| 513 | Wilson, Bradley | FLO_Y'A | Four-Seam | 60 | 51.9 | 0.215 | 12.5 | 5.0 | 2261 | 92.2 | 6.77 | Soft-Speed Separation |
| 514 | Thebiay, Nolan | EVA_OTT | Four-Seam | 522 | 51.9 | 0.218 | 17.6 | 9.2 | 2276 | 89.5 | 6.81 | Soft-Speed Separation |
| 515 | Tiburcio, David | DOW_EAS1 | Four-Seam | 62 | 51.8 | 0.227 | 16.8 | 13.5 | 2275 | 93.7 | 5.16 | Soft-Speed Separation |
| 516 | Zentko, Dylan | EVA_OTT | Four-Seam | 208 | 51.8 | 0.226 | 17.4 | -8.1 | 1946 | 86.8 | 5.68 | Soft-Speed Separation |
| 517 | Darden, Nathan | FLO_Y'A | Four-Seam | 151 | 51.7 | 0.245 | 15.8 | 7.6 | 1935 | 91.6 | 5.38 | Soft-Speed Separation |
| 518 | Sittinger, Brandyn | LAK_ERI24 | Four-Seam | 248 | 51.7 | 0.243 | 17.3 | 13.5 | 2294 | 94.7 | 5.67 | Soft-Speed Separation |
| 519 | Woolfolk, Dallas | MIS_MUD | Four-Seam | 194 | 51.7 | 0.218 | 19.8 | 13.0 | 2414 | 92.8 | 5.44 | Soft-Speed Separation |
| 520 | Gordillo, Lucas | TRI_VAL | Changeup | 50 | 51.7 | 0.243 | 10.8 | 16.5 | 2145 | 80.3 | 6.02 | Soft-Speed Separation |
| 521 | Kirby, Zach | WAS_WIL3 | Changeup | 122 | 51.6 | 0.227 | 9.9 | 15.4 | 1690 | 79.8 | 6.07 | Soft-Speed Separation |
| 522 | Johnston, Spencer | DOW_EAS1 | Four-Seam | 57 | 51.6 | 0.235 | 17.7 | 11.8 | 2137 | 84.8 | 5.96 | Soft-Speed Separation |
| 523 | Rodriguez, Esteban | TRO_AIG | Four-Seam | 142 | 51.5 | 0.233 | 16.8 | 5.0 | 2157 | 88.7 | 5.81 | Soft-Speed Separation |
| 524 | Brothers, Kellen | SUS_COU1 | Four-Seam | 351 | 51.5 | 0.232 | 18.3 | 14.3 | 2353 | 89.3 | 6.47 | Soft-Speed Separation |
| 525 | Hagan, Jack | DOW_EAS1 | Sinker | 265 | 51.5 | 0.225 | 10.6 | 16.6 | 2377 | 91.4 | 6.03 | Soft-Speed Separation |
| 526 | Stuka, Ted | OTT_TIT | Sinker | 157 | 51.3 | 0.230 | 12.1 | 19.3 | 2340 | 95.1 | 5.21 | Soft-Speed Separation |
| 527 | Martinez, Gregory | DOW_EAS1 | Four-Seam | 83 | 51.3 | 0.232 | 16.3 | 13.6 | 2315 | 94.8 | 5.57 | Soft-Speed Separation |
| 528 | Kirby, Zach | WAS_WIL3 | Four-Seam | 350 | 51.2 | 0.231 | 20.2 | 7.2 | 2174 | 87.8 | 6.12 | Soft-Speed Separation |
| 529 | Forsyth, Braden | MIS_MUD | Four-Seam | 261 | 51.2 | 0.214 | 19.3 | 9.8 | 2233 | 90.4 | 6.57 | Soft-Speed Separation |
| 530 | Petschke, Ben | EVA_OTT | Four-Seam | 223 | 51.0 | 0.252 | 11.8 | 5.4 | 2252 | 89.6 | 5.51 | Soft-Speed Separation |
| 531 | Conklin, MacCallan | TRO_AIG | Slider | 52 | 50.9 | 0.224 | 9.3 | 0.5 | 2526 | 84.1 | 6.59 | Soft-Speed Separation |
| 532 | Johnson, Caiden | OTT_TIT | Sinker | 84 | 50.9 | 0.240 | 12.8 | -15.5 | 2225 | 90.0 | 5.95 | Soft-Speed Separation |
| 533 | Whitesell, Max | FLO_Y'A | Four-Seam | 220 | 50.8 | 0.229 | 14.1 | 12.8 | 1915 | 88.8 | 6.38 | Soft-Speed Separation |
| 534 | Morgan, Cooper | QUE_CAP | Cutter | 97 | 50.8 | 0.226 | 8.7 | -2.9 | 2134 | 86.3 | 5.87 | Soft-Speed Separation |
| 535 | Eisenbarger, Jack | QUE_CAP | Four-Seam | 320 | 50.8 | 0.244 | 18.8 | -13.6 | 2545 | 89.8 | 5.83 | Soft-Speed Separation |
| 536 | Ferguson, Francis | QUE_CAP | Four-Seam | 129 | 50.8 | 0.231 | 14.7 | -8.1 | 2190 | 90.1 | 5.70 | Soft-Speed Separation |
| 537 | Agosto, Justus | TRI_VAL | Slider | 54 | 50.7 | 0.228 | 8.6 | -1.5 | 2249 | 84.8 | 5.80 | Soft-Speed Separation |
| 538 | Vega, Lucas | TRO_AIG | Four-Seam | 124 | 50.6 | 0.226 | 11.7 | 10.1 | 2081 | 89.8 | 6.13 | Soft-Speed Separation |
| 539 | Castro, Alexander | TRO_AIG | Changeup | 67 | 50.6 | 0.236 | 5.9 | 10.5 | 1308 | 83.3 | 6.10 | Soft-Speed Separation |
| 540 | Primeaux, Parker | SUS_COU1 | Changeup | 102 | 50.6 | 0.249 | 0.8 | 17.7 | 2014 | 85.9 | 5.57 | Soft-Speed Separation |
| 541 | Peyton, Blake | GAT_GRI | Four-Seam | 234 | 50.6 | 0.209 | 18.3 | -13.4 | 2258 | 89.3 | 5.92 | Soft-Speed Separation |
| 542 | Zeplin, Blane | JOL_SLA | Four-Seam | 236 | 50.5 | 0.218 | 18.6 | 9.0 | 2288 | 89.7 | 5.93 | Soft-Speed Separation |
| 543 | Garcia, Jorge | SUS_COU1 | Changeup | 53 | 50.5 | 0.232 | 12.6 | 9.4 | 1510 | 81.9 | 5.96 | Soft-Speed Separation |
| 544 | Simone, Andrew | TRO_AIG | Changeup | 89 | 50.5 | 0.221 | 10.3 | 12.7 | 1685 | 85.4 | 5.95 | Soft-Speed Separation |
| 545 | Good, Ty | GAT_GRI | Four-Seam | 442 | 50.5 | 0.215 | 18.7 | 4.8 | 2097 | 89.3 | 6.13 | Soft-Speed Separation |
| 546 | Cook, Avery | WIN_CIT29 | Sinker | 113 | 50.4 | 0.238 | -0.1 | 16.3 | 2187 | 88.4 | 6.56 | Soft-Speed Separation |
| 547 | Peyton, Blake | GAT_GRI | Sinker | 77 | 50.4 | 0.196 | 16.4 | -15.0 | 2211 | 89.1 | 6.05 | Soft-Speed Separation |
| 548 | Kines, Gunnar | JOL_SLA | Sinker | 113 | 50.4 | 0.241 | 17.3 | -12.7 | 2195 | 84.7 | 5.85 | Soft-Speed Separation |
| 549 | Hoeymans, Jack | GAT_GRI | Sinker | 66 | 50.4 | 0.222 | 7.4 | 15.1 | 2157 | 89.4 | 6.32 | Soft-Speed Separation |
| 550 | Thebiay, Nolan | EVA_OTT | Changeup | 113 | 50.3 | 0.267 | 4.9 | 16.1 | 1929 | 83.0 | 6.38 | Soft-Speed Separation |
| 551 | Johnston, Spencer | DOW_EAS1 | Changeup | 299 | 50.2 | 0.242 | 8.7 | 10.0 | 1618 | 77.6 | 5.93 | Soft-Speed Separation |
| 552 | Bihm, Gage | MIS_MUD | Four-Seam | 180 | 50.2 | 0.211 | 15.1 | -10.8 | 1946 | 92.1 | 5.44 | Soft-Speed Separation |
| 553 | Pardinho, Eric | OTT_TIT | Four-Seam | 349 | 50.2 | 0.232 | 19.3 | 12.9 | 2250 | 92.7 | 5.50 | Soft-Speed Separation |
| 554 | Campbell, Tyler | MIS_MUD | Cutter | 132 | 50.1 | 0.242 | 8.4 | -3.8 | 2274 | 83.8 | 6.07 | Soft-Speed Separation |
| 555 | Baird, Dustin | MIS_MUD | Four-Seam | 81 | 50.1 | 0.249 | 14.4 | 13.4 | 2056 | 89.5 | 5.99 | Soft-Speed Separation |
| 556 | Widener, Jacob | SUS_COU1 | Four-Seam | 130 | 50.1 | 0.260 | 10.6 | -7.1 | 2371 | 89.0 | 6.69 | Soft-Speed Separation |
| 557 | Johnson, Preston | MIS_MUD | Four-Seam | 90 | 50.0 | 0.198 | 20.3 | 6.9 | 2368 | 92.2 | 6.33 | Soft-Speed Separation |
| 558 | Hagan, Jack | DOW_EAS1 | Four-Seam | 81 | 49.9 | 0.189 | 13.5 | 13.2 | 2381 | 91.6 | 5.99 | Soft-Speed Separation |
| 559 | Phelps, Travis | FLO_Y'A | Four-Seam | 154 | 49.9 | 0.247 | 15.3 | 6.9 | 2131 | 91.1 | 6.39 | Soft-Speed Separation |
| 560 | Foltz Jr., Michael | WAS_WIL3 | Four-Seam | 284 | 49.8 | 0.247 | 18.9 | -4.1 | 2191 | 92.5 | 6.01 | Soft-Speed Separation |
| 561 | Ronne, Andrew | GAT_GRI | Four-Seam | 216 | 49.8 | 0.240 | 13.3 | 6.8 | 2182 | 91.9 | 6.36 | Soft-Speed Separation |
| 562 | Marynczak, Arlo | TRI_VAL | Changeup | 120 | 49.7 | 0.265 | 7.3 | 12.6 | 1660 | 81.6 | 6.22 | Soft-Speed Separation |
| 563 | Traver, Eliott | LAK_ERI24 | Sinker | 65 | 49.7 | 0.204 | 8.8 | 16.7 | 2147 | 80.7 | 5.77 | Soft-Speed Separation |
| 564 | Parra, Andres | LAK_ERI24 | Four-Seam | 241 | 49.7 | 0.241 | 14.2 | -13.0 | 2044 | 88.4 | 6.07 | Soft-Speed Separation |
| 565 | Ryan, Dillon | NEW_ENG23 | Sinker | 220 | 49.6 | 0.258 | 12.5 | 16.3 | 2323 | 91.2 | 6.32 | Soft-Speed Separation |
| 566 | De Jesus, Larry | DOW_EAS1 | Sinker | 75 | 49.5 | 0.229 | 14.2 | 16.0 | 2347 | 89.5 | 5.18 | Soft-Speed Separation |
| 567 | Moreno, Jose | DOW_EAS1 | Changeup | 93 | 49.5 | 0.231 | 7.1 | 11.0 | 1766 | 81.6 | 5.65 | Soft-Speed Separation |
| 568 | Vitas, Ben | JOL_SLA | Four-Seam | 293 | 49.5 | 0.247 | 13.8 | 16.5 | 2153 | 90.3 | 5.13 | Soft-Speed Separation |
| 569 | Agosto, Justus | TRI_VAL | Changeup | 53 | 49.4 | 0.269 | 10.4 | 9.6 | 1718 | 80.7 | 5.87 | Soft-Speed Separation |
| 570 | Langrell, Connor | MIS_MUD | Cutter | 262 | 49.4 | 0.235 | 9.8 | -0.6 | 2310 | 86.5 | 6.13 | Soft-Speed Separation |
| 571 | Binns, Malik | NEW_JER6 | Cutter | 88 | 49.3 | 0.212 | 9.5 | -1.9 | 2229 | 88.9 | 6.18 | Soft-Speed Separation |
| 572 | Marklund, Brandon | OTT_TIT | Four-Seam | 279 | 49.3 | 0.240 | 16.9 | 10.5 | 2209 | 90.8 | 5.25 | Soft-Speed Separation |
| 573 | Quigley, Michael | NEW_ENG23 | Four-Seam | 292 | 49.3 | 0.223 | 17.7 | 12.6 | 2298 | 92.8 | 5.93 | Soft-Speed Separation |
| 574 | Cohn, Cooper | NIU_HUS | Four-Seam | 72 | 49.3 | 0.216 | 17.8 | 12.6 | 2195 | 91.1 | 5.96 | Soft-Speed Separation |
| 575 | Aldeano, Austin | TRO_AIG | Changeup | 51 | 49.2 | 0.248 | 7.1 | 17.6 | 1856 | 81.3 | 6.28 | Soft-Speed Separation |
| 576 | Dill, Austin | TRI_VAL | Four-Seam | 113 | 49.1 | 0.221 | 16.4 | 13.3 | 2324 | 87.2 | 5.33 | Soft-Speed Separation |
| 577 | Harajli, Ahmad | FLO_Y'A | Four-Seam | 189 | 49.1 | 0.268 | 14.7 | 8.8 | 2042 | 92.0 | 6.43 | Soft-Speed Separation |
| 578 | Reeves, Cobe | NEW_YOR13 | Sinker | 196 | 49.1 | 0.260 | 8.9 | -15.0 | 1826 | 90.2 | 6.00 | Soft-Speed Separation |
| 579 | Castro, Alexander | TRO_AIG | Sinker | 52 | 49.0 | 0.225 | 15.8 | 16.9 | 2189 | 93.4 | 5.27 | Soft-Speed Separation |
| 580 | Primeaux, Parker | SUS_COU1 | Sinker | 79 | 49.0 | 0.233 | 0.2 | 18.7 | 2088 | 87.8 | 5.57 | Soft-Speed Separation |
| 581 | Sesar, Jorden | SUS_COU1 | Four-Seam | 555 | 48.9 | 0.229 | 19.6 | 8.2 | 2485 | 91.7 | 6.27 | Soft-Speed Separation |
| 582 | Huter, Blayne | SUS_COU1 | Four-Seam | 142 | 48.9 | 0.242 | 17.1 | 6.2 | 2055 | 87.1 | 6.54 | Soft-Speed Separation |
| 583 | Garcia, Jorge | SUS_COU1 | Four-Seam | 176 | 48.9 | 0.226 | 16.9 | 4.3 | 2103 | 86.1 | 6.03 | Soft-Speed Separation |
| 584 | Catrambone, Ben | JOL_SLA | Four-Seam | 174 | 48.9 | 0.228 | 19.9 | 8.9 | 2118 | 87.9 | 5.14 | Soft-Speed Separation |
| 585 | Fauci, Sonny | NEW_JER6 | Four-Seam | 271 | 48.8 | 0.247 | 17.0 | 12.8 | 2215 | 93.8 | 6.45 | Soft-Speed Separation |
| 586 | Rodriguez, Leonardo | NEW_JER6 | Four-Seam | 181 | 48.8 | 0.226 | 15.6 | 10.3 | 2440 | 92.2 | 6.57 | Soft-Speed Separation |
| 587 | Lefebvre, Charles | TRO_AIG | Sinker | 412 | 48.7 | 0.241 | 12.3 | 16.7 | 2232 | 89.1 | 6.53 | Soft-Speed Separation |
| 588 | Miranda, Kevin | OTT_TIT | Changeup | 140 | 48.7 | 0.254 | 8.4 | 12.6 | 1414 | 79.4 | 6.08 | Soft-Speed Separation |
| 589 | Encarnacion, J.D. | EVA_OTT | Four-Seam | 326 | 48.7 | 0.231 | 14.4 | 8.1 | 2333 | 88.7 | 5.89 | Soft-Speed Separation |
| 590 | Harris, Ben | GAT_GRI | Changeup | 316 | 48.7 | 0.249 | 8.6 | 16.2 | 1790 | 83.0 | 5.63 | Soft-Speed Separation |
| 591 | Sakurai, Masatoshi | QUE_CAP | Changeup | 145 | 48.7 | 0.262 | 8.6 | -5.6 | 1444 | 80.5 | 5.99 | Soft-Speed Separation |
| 592 | Armstrong, Andrew | NEW_YOR13 | Sinker | 90 | 48.6 | 0.258 | 13.0 | -12.3 | 2102 | 88.6 | 6.46 | Soft-Speed Separation |
| 593 | Ferguson, Francis | WIN_CIT29 | Four-Seam | 162 | 48.6 | 0.252 | 10.7 | -5.8 | 1966 | 90.2 | 5.46 | Soft-Speed Separation |
| 594 | Sakurai, Masatoshi | QUE_CAP | Four-Seam | 489 | 48.6 | 0.239 | 16.5 | -7.2 | 2031 | 87.6 | 6.51 | Soft-Speed Separation |
| 595 | Hocom, Quinn | TRI_VAL | Four-Seam | 296 | 48.5 | 0.254 | 21.1 | 10.3 | 2173 | 89.0 | 5.99 | Soft-Speed Separation |
| 596 | Leach, Landon | TRO_AIG | Four-Seam | 178 | 48.5 | 0.261 | 10.5 | 5.1 | 1971 | 91.6 | 5.66 | Soft-Speed Separation |
| 597 | Miranda, Kevin | OTT_TIT | Four-Seam | 189 | 48.4 | 0.239 | 19.4 | 13.6 | 2170 | 87.2 | 5.75 | Soft-Speed Separation |
| 598 | Eldred, Zach | NEW_ENG23 | Sinker | 100 | 48.4 | 0.242 | 11.7 | 13.2 | 2374 | 88.9 | 6.50 | Soft-Speed Separation |
| 599 | Rodriguez, Luis | TRO_AIG | Four-Seam | 276 | 48.4 | 0.255 | 20.6 | 7.0 | 2360 | 95.1 | 6.06 | Soft-Speed Separation |
| 600 | Simpson, Garret | EVA_OTT | Four-Seam | 370 | 48.0 | 0.250 | 11.0 | 3.2 | 2341 | 89.0 | 5.74 | Soft-Speed Separation |
| 601 | Noriega, Branden | LAK_ERI24 | Sinker | 92 | 48.0 | 0.271 | 13.2 | -15.7 | 2201 | 90.3 | 6.16 | Soft-Speed Separation |
| 602 | Barker, Alex | NEW_YOR13 | Changeup | 121 | 47.9 | 0.260 | 5.4 | -12.2 | 1537 | 82.8 | 6.25 | Soft-Speed Separation |
| 603 | Lovell, Justin | WIN_CIT29 | Cutter | 61 | 47.9 | 0.236 | 10.6 | -9.1 | 2277 | 91.5 | 6.35 | Soft-Speed Separation |
| 604 | Eldred, Zach | NEW_ENG23 | Four-Seam | 531 | 47.9 | 0.245 | 16.4 | 6.7 | 2496 | 89.7 | 6.43 | Soft-Speed Separation |
| 605 | Vailes, Gage | GAT_GRI | Sinker | 387 | 47.8 | 0.265 | 7.6 | 16.1 | 1957 | 90.1 | 5.04 | Soft-Speed Separation |
| 606 | Valdez, Alex | EVA_OTT | Four-Seam | 182 | 47.7 | 0.240 | 13.0 | 5.5 | 2164 | 91.6 | 5.95 | Soft-Speed Separation |
| 607 | Cihocki, Danny | NIU_HUS | Four-Seam | 55 | 47.7 | 0.218 | 15.8 | 12.3 | 2221 | 89.2 | 6.54 | Soft-Speed Separation |
| 608 | Gilleran, Jimmy | NEW_ENG23 | Sinker | 187 | 47.7 | 0.240 | 12.4 | 15.8 | 2106 | 88.1 | 5.52 | Soft-Speed Separation |
| 609 | Hampton, Ky | OTT_TIT | Changeup | 228 | 47.6 | 0.262 | 2.2 | 15.6 | 1705 | 84.0 | 6.01 | Soft-Speed Separation |
| 610 | Maietta, Dante | WIN_CIT29 | Four-Seam | 431 | 47.6 | 0.233 | 19.2 | 9.3 | 2049 | 88.4 | 6.05 | Soft-Speed Separation |
| 611 | Brothers, Kellen | SUS_COU1 | Slider | 74 | 47.5 | 0.221 | 8.0 | -1.8 | 2357 | 82.3 | 6.25 | Soft-Speed Separation |
| 612 | Thompson, Ross | SCH_BOO | Changeup | 85 | 47.5 | 0.256 | 5.4 | 9.0 | 1095 | 79.7 | 5.67 | Soft-Speed Separation |
| 613 | Perozzi, John | SUS_COU1 | Four-Seam | 207 | 47.4 | 0.207 | 21.7 | 9.0 | 2193 | 91.4 | 5.99 | Soft-Speed Separation |
| 614 | Puccetti, Dominic | OTT_TIT | Four-Seam | 327 | 47.3 | 0.228 | 20.4 | -5.1 | 1869 | 87.9 | 5.63 | Soft-Speed Separation |
| 615 | Morgan, Cooper | QUE_CAP | Sinker | 103 | 47.3 | 0.254 | 12.2 | -12.4 | 2163 | 87.4 | 6.15 | Soft-Speed Separation |
| 616 | Bargo, Casey | FLO_Y'A | Four-Seam | 189 | 47.3 | 0.256 | 14.5 | 11.6 | 2211 | 91.3 | 5.89 | Soft-Speed Separation |
| 617 | Esposito, Michael | NEW_ENG23 | Four-Seam | 139 | 47.3 | 0.250 | 16.9 | -11.5 | 2083 | 90.5 | 6.33 | Soft-Speed Separation |
| 618 | Garcia, Andrew | EVA_OTT | Four-Seam | 246 | 47.3 | 0.252 | 13.2 | 7.1 | 2107 | 91.6 | 6.03 | Soft-Speed Separation |
| 619 | Gollert, Harley | QUE_CAP | Four-Seam | 81 | 47.2 | 0.248 | 16.6 | -8.3 | 2169 | 88.7 | 5.59 | Soft-Speed Separation |
| 620 | Pindel, Buddie | SCH_BOO | Four-Seam | 446 | 47.2 | 0.250 | 15.9 | 13.5 | 2200 | 89.8 | 5.63 | Soft-Speed Separation |
| 621 | Heredia-Bustos, Rolando | DOW_EAS1 | Changeup | 329 | 47.2 | 0.268 | 9.1 | 17.6 | 2064 | 79.4 | 5.62 | Soft-Speed Separation |
| 622 | Parsons, Billy | SUS_COU1 | Four-Seam | 341 | 47.1 | 0.228 | 17.5 | 9.5 | 2234 | 90.5 | 5.73 | Soft-Speed Separation |
| 623 | Steinhauer, Ryan | NEW_JER6 | Four-Seam | 58 | 47.1 | 0.270 | 16.0 | -9.3 | 1936 | 86.4 | 6.05 | Soft-Speed Separation |
| 624 | Thompson, Ross | SCH_BOO | Sinker | 51 | 47.0 | 0.222 | 13.6 | 12.6 | 1964 | 90.0 | 5.97 | Soft-Speed Separation |
| 625 | Henderson, Drew | DOW_EAS1 | Changeup | 144 | 46.9 | 0.247 | 9.2 | 14.1 | 1688 | 81.6 | 5.81 | Soft-Speed Separation |
| 626 | Floyd, Conner | QUE_CAP | Four-Seam | 322 | 46.9 | 0.234 | 20.7 | 10.7 | 2394 | 92.6 | 5.50 | Soft-Speed Separation |
| 627 | Wehrle, Tyler | WIN_CIT29 | Sinker | 94 | 46.8 | 0.247 | 15.5 | 16.6 | 2319 | 91.3 | 5.69 | Soft-Speed Separation |
| 628 | Villalobos, Jonaiker | FLO_Y'A | Four-Seam | 464 | 46.8 | 0.245 | 14.8 | -9.7 | 2237 | 87.8 | 5.87 | Soft-Speed Separation |
| 629 | Shoemaker, Adam | QUE_CAP | Sinker | 62 | 46.8 | 0.265 | 10.5 | -15.2 | 2056 | 91.7 | 6.06 | Soft-Speed Separation |
| 630 | Sparks, Alec | GAT_GRI | Four-Seam | 363 | 46.7 | 0.243 | 17.2 | 4.9 | 2179 | 91.0 | 5.90 | Soft-Speed Separation |
| 631 | Maietta, Dante | WIN_CIT29 | Slider | 92 | 46.6 | 0.274 | 7.1 | -1.9 | 2033 | 80.5 | 6.27 | Soft-Speed Separation |
| 632 | Duby, Bill | NEW_JER6 | Sinker | 134 | 46.6 | 0.259 | 14.0 | 15.9 | 2051 | 86.6 | 6.37 | Soft-Speed Separation |
| 633 | Potteiger, Jack | JOL_SLA | Sinker | 79 | 46.6 | 0.263 | 5.1 | -14.7 | 1942 | 89.4 | 6.39 | Soft-Speed Separation |
| 634 | Cameron, Wyatt | SCH_BOO | Four-Seam | 185 | 46.6 | 0.262 | 14.8 | 10.9 | 2243 | 91.2 | 5.48 | Soft-Speed Separation |
| 635 | Eckaus, David | EVA_OTT | Four-Seam | 232 | 46.5 | 0.252 | 15.0 | -11.3 | 2352 | 91.2 | 6.13 | Soft-Speed Separation |
| 636 | Turner, Eric | JOL_SLA | Four-Seam | 433 | 46.4 | 0.235 | 16.2 | 13.9 | 2286 | 88.2 | 5.18 | Soft-Speed Separation |
| 637 | Davis, Tyler | WAS_WIL3 | Four-Seam | 119 | 46.4 | 0.253 | 18.5 | -11.2 | 2340 | 92.6 | 5.88 | Soft-Speed Separation |
| 638 | House, Tristan | MIS_MUD | Four-Seam | 314 | 46.4 | 0.250 | 17.0 | 9.6 | 1975 | 89.3 | 6.15 | Soft-Speed Separation |
| 639 | Orth, Harry | SCH_BOO | Sinker | 57 | 46.3 | 0.257 | 13.1 | 15.4 | 1963 | 90.9 | 6.24 | Soft-Speed Separation |
| 640 | Kramer, Cameron | TRO_AIG | Four-Seam | 81 | 46.3 | 0.256 | 16.6 | 7.9 | 2245 | 89.8 | 5.90 | Soft-Speed Separation |
| 641 | Binns, Malik | NEW_JER6 | Four-Seam | 100 | 46.2 | 0.267 | 13.7 | 7.5 | 2102 | 91.3 | 6.52 | Soft-Speed Separation |
| 642 | Serrano, Elio | NEW_JER6 | Four-Seam | 427 | 46.2 | 0.235 | 17.4 | 10.8 | 2447 | 91.3 | 5.72 | Soft-Speed Separation |
| 643 | Hines, Carter | FLO_Y'A | Four-Seam | 53 | 46.2 | 0.270 | 16.6 | -8.1 | 2502 | 91.0 | 5.91 | Soft-Speed Separation |
| 644 | Andueza, Axel | DOW_EAS1 | Four-Seam | 452 | 46.2 | 0.244 | 13.8 | 7.8 | 2125 | 90.6 | 5.52 | Soft-Speed Separation |
| 645 | Hohenstein, Liam | WIN_CIT29 | Changeup | 84 | 46.1 | 0.286 | 11.1 | 9.0 | 1547 | 84.1 | 6.04 | Soft-Speed Separation |
| 646 | Delongchamp, Luke | TRI_VAL | Changeup | 286 | 46.1 | 0.259 | 8.2 | 16.4 | 1870 | 82.4 | 5.54 | Soft-Speed Separation |
| 647 | Balzan, Jackson | SUS_COU1 | Four-Seam | 298 | 46.1 | 0.247 | 18.6 | -12.1 | 2251 | 86.3 | 5.45 | Soft-Speed Separation |
| 648 | Burcham, Jacob | GAT_GRI | Sinker | 223 | 46.0 | 0.273 | 6.3 | 15.9 | 2269 | 91.0 | 6.62 | Soft-Speed Separation |
| 649 | Escobar, Anthony | TRO_AIG | Four-Seam | 393 | 45.9 | 0.250 | 17.8 | 10.5 | 2144 | 90.6 | 6.33 | Soft-Speed Separation |
| 650 | Long, Jalon | NEW_YOR13 | Changeup | 114 | 45.9 | 0.272 | 5.7 | 14.0 | 1528 | 82.2 | 6.10 | Soft-Speed Separation |
| 651 | Barreto, Brayhans | TRI_VAL | Sinker | 136 | 45.8 | 0.271 | 12.1 | -14.1 | 2051 | 88.3 | 6.11 | Soft-Speed Separation |
| 652 | Gartland, Chad | SUS_COU1 | Four-Seam | 104 | 45.8 | 0.252 | 15.6 | 9.7 | 2115 | 91.0 | 6.26 | Soft-Speed Separation |
| 653 | Correa, Nelvin | QUE_CAP | Changeup | 70 | 45.8 | 0.247 | 10.8 | 14.0 | 1990 | 84.6 | 6.01 | Soft-Speed Separation |
| 654 | Webster, Evan | FLO_Y'A | Changeup | 166 | 45.8 | 0.254 | 11.4 | -11.4 | 1784 | 82.5 | 6.91 | Soft-Speed Separation |
| 655 | Morel, Yohanse | OTT_TIT | Changeup | 103 | 45.8 | 0.259 | 5.1 | 17.1 | 2118 | 85.2 | 5.36 | Soft-Speed Separation |
| 656 | Nova, Fraynel | LAK_ERI24 | Four-Seam | 430 | 45.7 | 0.248 | 12.4 | 6.8 | 2053 | 90.3 | 6.03 | Soft-Speed Separation |
| 657 | Gordillo, Lucas | TRI_VAL | Sinker | 73 | 45.7 | 0.261 | 13.7 | 14.4 | 2120 | 91.6 | 5.98 | Soft-Speed Separation |
| 658 | Boies, Emiles | QUE_CAP | Sinker | 205 | 45.6 | 0.257 | 14.8 | 16.1 | 2127 | 87.5 | 6.07 | Soft-Speed Separation |
| 659 | Godwin, Connor | NEW_YOR13 | Sinker | 149 | 45.6 | 0.269 | 6.0 | 14.5 | 2153 | 91.8 | 6.07 | Soft-Speed Separation |
| 660 | Kelly, Aiden | TRI_VAL | Four-Seam | 148 | 45.6 | 0.252 | 15.5 | 8.5 | 2248 | 90.1 | 5.99 | Soft-Speed Separation |
| 661 | McKillican, Adam | QUE_CAP | Sinker | 59 | 45.5 | 0.271 | 11.5 | 12.6 | 1988 | 88.6 | 6.73 | Soft-Speed Separation |
| 662 | Petschke, Ben | EVA_OTT | Cutter | 254 | 45.5 | 0.241 | 10.1 | 2.7 | 2257 | 89.2 | 5.45 | Soft-Speed Separation |
| 663 | Martinez, Gregory | DOW_EAS1 | Sinker | 89 | 45.5 | 0.240 | 12.1 | 15.9 | 2288 | 94.2 | 5.53 | Soft-Speed Separation |
| 664 | Kalisky, Jack | OTT_TIT | Four-Seam | 68 | 45.5 | 0.239 | 13.3 | 7.4 | 2405 | 88.4 | 5.87 | Soft-Speed Separation |
| 665 | Parenteau, Matt | EVA_OTT | Four-Seam | 66 | 45.5 | 0.233 | 14.6 | 4.9 | 2252 | 92.0 | 6.39 | Soft-Speed Separation |
| 666 | Boies, Emiles | QUE_CAP | Four-Seam | 98 | 45.5 | 0.254 | 17.1 | 12.9 | 2131 | 87.5 | 6.03 | Soft-Speed Separation |
| 667 | Dill, Austin | TRI_VAL | Sinker | 197 | 45.5 | 0.265 | 14.8 | 15.8 | 2315 | 88.1 | 5.43 | Soft-Speed Separation |
| 668 | Perdomo, Rafael | QUE_CAP | Four-Seam | 165 | 45.4 | 0.226 | 20.2 | 11.1 | 2307 | 89.1 | 5.88 | Soft-Speed Separation |
| 669 | Misla, Luis | TRI_VAL | Four-Seam | 280 | 45.3 | 0.265 | 17.4 | -11.2 | 2400 | 88.5 | 5.79 | Soft-Speed Separation |
| 670 | Garcia, Hector | WAS_WIL3 | Four-Seam | 199 | 45.2 | 0.254 | 19.5 | 4.6 | 2221 | 91.0 | 6.05 | Soft-Speed Separation |
| 671 | Zaffiro, Cole | SCH_BOO | Changeup | 59 | 45.2 | 0.239 | 4.5 | 16.0 | 1756 | 80.3 | 5.90 | Soft-Speed Separation |
| 672 | Henderson, Drew | DOW_EAS1 | Four-Seam | 440 | 45.1 | 0.242 | 18.5 | 13.2 | 2250 | 89.1 | 5.71 | Soft-Speed Separation |
| 673 | Noriega, Branden | LAK_ERI24 | Four-Seam | 177 | 45.1 | 0.230 | 15.3 | -14.6 | 2239 | 90.9 | 5.93 | Soft-Speed Separation |
| 674 | Maher, Adam | TRI_VAL | Four-Seam | 191 | 45.1 | 0.257 | 20.3 | -9.7 | 2041 | 88.0 | 5.78 | Soft-Speed Separation |
| 675 | Sanders, Brayden | MIS_MUD | Four-Seam | 207 | 45.1 | 0.275 | 18.9 | 10.9 | 2009 | 91.6 | 4.93 | Soft-Speed Separation |
| 676 | Soto, Carlos | JOL_SLA | Four-Seam | 166 | 45.0 | 0.289 | 13.0 | 9.6 | 2212 | 88.5 | 5.47 | Soft-Speed Separation |
| 677 | Williams, Brian | MIS_MUD | Cutter | 144 | 45.0 | 0.269 | 6.6 | -0.1 | 2190 | 83.2 | 6.47 | Soft-Speed Separation |
| 678 | Shears, Tanner | SCH_BOO | Sinker | 60 | 45.0 | 0.268 | 12.9 | 14.7 | 1945 | 92.7 | 5.31 | Soft-Speed Separation |
| 679 | Gollert, Harley | TRO_AIG | Four-Seam | 160 | 44.9 | 0.234 | 15.5 | -10.1 | 2148 | 88.7 | 5.39 | Soft-Speed Separation |
| 680 | Primeaux, Parker | SUS_COU1 | Four-Seam | 56 | 44.8 | 0.253 | 5.4 | 16.0 | 2089 | 87.6 | 5.56 | Soft-Speed Separation |
| 681 | Wiltse, Ryan | EVA_OTT | Cutter | 51 | 44.8 | 0.264 | 8.3 | -1.0 | 1980 | 81.2 | 6.14 | Soft-Speed Separation |
| 682 | Helt, Robert | LAK_ERI24 | Four-Seam | 480 | 44.8 | 0.261 | 14.9 | 7.1 | 2284 | 91.4 | 6.29 | Soft-Speed Separation |
| 683 | Chapple, Bronson | TRO_AIG | Changeup | 51 | 44.7 | 0.283 | 3.7 | 14.5 | 1828 | 83.2 | 6.34 | Soft-Speed Separation |
| 684 | Shinn, Nathan | LAK_ERI24 | Sinker | 50 | 44.6 | 0.241 | 15.9 | -10.4 | 1907 | 89.3 | 5.76 | Soft-Speed Separation |
| 685 | Bargo, Casey | NEW_ENG23 | Four-Seam | 147 | 44.6 | 0.253 | 16.0 | 12.7 | 2282 | 92.2 | 6.19 | Soft-Speed Separation |
| 686 | De Los Santos, Enmanuel | NEW_ENG23 | Four-Seam | 200 | 44.6 | 0.248 | 18.1 | 4.1 | 2120 | 88.5 | 6.79 | Soft-Speed Separation |
| 687 | Vitas, Ben | JOL_SLA | Sinker | 236 | 44.6 | 0.252 | 14.5 | 17.6 | 2171 | 90.4 | 5.19 | Soft-Speed Separation |
| 688 | Linderman, Greyson | JOL_SLA | Four-Seam | 68 | 44.5 | 0.264 | 14.2 | 12.7 | 2190 | 94.3 | 5.39 | Soft-Speed Separation |
| 689 | Cooper, Garrett | NEW_YOR13 | Four-Seam | 191 | 44.5 | 0.265 | 16.2 | 6.2 | 2084 | 89.6 | 5.90 | Soft-Speed Separation |
| 690 | Smith, Ethan | WIN_CIT29 | Four-Seam | 169 | 44.3 | 0.245 | 16.6 | 9.8 | 2211 | 89.3 | 6.29 | Soft-Speed Separation |
| 691 | Hill, Kaleb | OTT_TIT | Four-Seam | 53 | 44.3 | 0.255 | 14.3 | -10.0 | 1962 | 89.6 | 5.51 | Soft-Speed Separation |
| 692 | Anibal, Trevor | NEW_ENG23 | Four-Seam | 222 | 44.2 | 0.275 | 19.0 | 12.2 | 2256 | 90.4 | 5.85 | Soft-Speed Separation |
| 693 | Andueza, Axel | DOW_EAS1 | Sinker | 88 | 44.2 | 0.272 | 11.3 | 11.0 | 2040 | 89.9 | 5.47 | Soft-Speed Separation |
| 694 | Bargo, Casey | FLO_Y'A | Sinker | 111 | 44.1 | 0.257 | 12.5 | 15.6 | 2216 | 91.1 | 5.85 | Soft-Speed Separation |
| 695 | Harris, Ben | GAT_GRI | Four-Seam | 488 | 44.1 | 0.260 | 17.0 | 8.6 | 2351 | 91.1 | 5.89 | Soft-Speed Separation |
| 696 | Hernandez, Nyan | NEW_JER6 | Changeup | 173 | 44.1 | 0.245 | 12.0 | 15.8 | 1927 | 82.3 | 6.32 | Soft-Speed Separation |
| 697 | Hernandez, Nyan | NEW_JER6 | Sinker | 92 | 44.0 | 0.259 | 14.4 | 16.5 | 2085 | 88.4 | 6.44 | Soft-Speed Separation |
| 698 | Wehrle, Tyler | WIN_CIT29 | Changeup | 65 | 44.0 | 0.268 | 6.4 | 15.8 | 1898 | 84.2 | 5.56 | Soft-Speed Separation |
| 699 | Armstrong, Andrew | NEW_YOR13 | Four-Seam | 129 | 43.9 | 0.275 | 14.8 | -9.4 | 2115 | 88.8 | 6.43 | Soft-Speed Separation |
| 700 | Blair, Davis | DOW_EAS1 | Four-Seam | 204 | 43.9 | 0.239 | 16.6 | 8.1 | 2084 | 91.7 | 5.59 | Soft-Speed Separation |
| 701 | Duncan, Tanner | DOW_EAS1 | Four-Seam | 190 | 43.7 | 0.270 | 16.1 | 9.0 | 2290 | 94.0 | 5.87 | Soft-Speed Separation |
| 702 | Kemlage, Joe | NEW_ENG23 | Sinker | 179 | 43.6 | 0.273 | 8.4 | -15.3 | 2429 | 90.9 | 5.87 | Soft-Speed Separation |
| 703 | Snyder, Jack | SCH_BOO | Four-Seam | 110 | 43.6 | 0.282 | 16.8 | 5.5 | 2427 | 90.3 | 5.80 | Soft-Speed Separation |
| 704 | Barker, Alex | NEW_YOR13 | Four-Seam | 235 | 43.6 | 0.266 | 15.6 | -7.9 | 2170 | 87.4 | 6.28 | Soft-Speed Separation |
| 705 | Estrella, Noah | TRI_VAL | Sinker | 56 | 43.6 | 0.295 | 14.2 | 14.5 | 2086 | 91.7 | 5.64 | Soft-Speed Separation |
| 706 | Fowler, Dalton | SUS_COU1 | Sinker | 51 | 43.5 | 0.285 | 11.3 | -12.9 | 2160 | 91.4 | 5.54 | Soft-Speed Separation |
| 707 | Leak, Anthony | NEW_YOR13 | Four-Seam | 156 | 43.5 | 0.226 | 17.5 | 10.2 | 2233 | 90.8 | 6.13 | Soft-Speed Separation |
| 708 | Vega, Lucas | TRO_AIG | Sinker | 257 | 43.5 | 0.253 | 9.1 | 14.6 | 2018 | 89.6 | 6.10 | Soft-Speed Separation |
| 709 | Potteiger, Jack | JOL_SLA | Sinker | 74 | 43.5 | 0.260 | 5.3 | -13.7 | 1940 | 89.4 | 6.07 | Soft-Speed Separation |
| 710 | Jones, Logan | FLO_Y'A | Sinker | 90 | 43.3 | 0.237 | 10.8 | 18.1 | 2216 | 89.6 | 5.23 | Soft-Speed Separation |
| 711 | Gamelin, Shaun | JOL_SLA | Four-Seam | 387 | 43.3 | 0.244 | 20.2 | 10.1 | 2110 | 90.1 | 4.89 | Soft-Speed Separation |
| 712 | Lovell, Justin | WIN_CIT29 | Four-Seam | 185 | 43.3 | 0.254 | 15.0 | -12.9 | 2308 | 93.4 | 6.29 | Soft-Speed Separation |
| 713 | Lefebvre, Charles | TRO_AIG | Four-Seam | 63 | 43.3 | 0.252 | 16.1 | 12.1 | 2256 | 89.8 | 6.39 | Soft-Speed Separation |
| 714 | Grounds, Jackson | TRO_AIG | Sinker | 55 | 43.2 | 0.273 | 13.8 | 14.5 | 2157 | 92.2 | 5.71 | Soft-Speed Separation |
| 715 | Moore, Kyle | SCH_BOO | Sinker | 86 | 43.2 | 0.299 | 14.9 | 15.4 | 2158 | 87.8 | 4.72 | Soft-Speed Separation |
| 716 | Hohenstein, Liam | WIN_CIT29 | Four-Seam | 175 | 43.1 | 0.254 | 17.4 | 4.3 | 1952 | 88.0 | 5.86 | Soft-Speed Separation |
| 717 | Bargo, Casey | FLO_Y'A | Changeup | 53 | 43.0 | 0.268 | 5.1 | 12.1 | 1489 | 83.0 | 6.12 | Soft-Speed Separation |
| 718 | Long, Maddox | WAS_WIL3 | Changeup | 61 | 42.9 | 0.282 | 7.9 | 15.7 | 1932 | 84.2 | 5.97 | Soft-Speed Separation |
| 719 | Villers, Ian | QUE_CAP | Four-Seam | 162 | 42.8 | 0.275 | 17.9 | 11.9 | 2261 | 93.4 | 6.11 | Soft-Speed Separation |
| 720 | Austin, Zack | SUS_COU1 | Four-Seam | 179 | 42.8 | 0.246 | 16.1 | 6.4 | 2287 | 91.6 | 5.89 | Soft-Speed Separation |
| 721 | Leduc, Zachary | TRO_AIG | Sinker | 67 | 42.7 | 0.262 | 11.6 | 16.1 | 2110 | 91.0 | 6.46 | Soft-Speed Separation |
| 722 | Matos, Dwayne | OTT_TIT | Changeup | 235 | 42.7 | 0.252 | 3.6 | 15.9 | 1525 | 84.0 | 6.38 | Soft-Speed Separation |
| 723 | Coles, Chad | WAS_WIL3 | Four-Seam | 239 | 42.6 | 0.260 | 17.9 | 9.8 | 2391 | 93.2 | 5.80 | Soft-Speed Separation |
| 724 | Salata, Derek | SCH_BOO | Four-Seam | 539 | 42.6 | 0.256 | 16.3 | 4.5 | 2317 | 89.5 | 6.20 | Soft-Speed Separation |
| 725 | Jensik, CJ | WIN_CIT29 | Sinker | 62 | 42.5 | 0.257 | 8.4 | 15.2 | 2079 | 92.5 | 5.78 | Soft-Speed Separation |
| 726 | Townes, Holland | SCH_BOO | Four-Seam | 149 | 42.4 | 0.262 | 15.3 | 13.1 | 2202 | 92.6 | 5.40 | Soft-Speed Separation |
| 727 | Allemann, Braeden | QUE_CAP | Four-Seam | 575 | 42.4 | 0.260 | 18.9 | 12.7 | 2343 | 91.1 | 6.32 | Soft-Speed Separation |
| 728 | Fauci, Sonny | NEW_JER6 | Sinker | 69 | 42.3 | 0.287 | 13.9 | 16.0 | 2223 | 93.0 | 6.51 | Soft-Speed Separation |
| 729 | Nakata, Yuto | QUE_CAP | Splitter | 110 | 42.2 | 0.299 | 3.1 | 6.8 | 1006 | 84.0 | 5.48 | Soft-Speed Separation |
| 730 | Delongchamp, Luke | TRI_VAL | Sinker | 100 | 42.0 | 0.284 | 11.2 | 17.4 | 2025 | 86.9 | 5.61 | Soft-Speed Separation |
| 731 | Bohnert, Matthew | WIN_CIT29 | Four-Seam | 320 | 42.0 | 0.251 | 16.9 | -8.7 | 2141 | 91.6 | 5.23 | Soft-Speed Separation |
| 732 | Willeman, Landon | EVA_OTT | Four-Seam | 554 | 42.0 | 0.263 | 18.5 | 12.6 | 2204 | 90.8 | 5.84 | Soft-Speed Separation |
| 733 | Williams, Pierce | NEW_ENG23 | Sinker | 83 | 42.0 | 0.274 | 12.3 | -14.2 | 1870 | 85.8 | 6.13 | Soft-Speed Separation |
| 734 | Sanchez, Edwin | LAK_ERI24 | Sinker | 217 | 41.9 | 0.255 | 15.5 | -14.0 | 2108 | 87.1 | 5.98 | Soft-Speed Separation |
| 735 | Bell, Brendan | NEW_ENG23 | Changeup | 56 | 41.9 | 0.250 | 7.3 | 15.4 | 1950 | 82.7 | 5.16 | Soft-Speed Separation |
| 736 | Harper, Scott | NEW_YOR13 | Sinker | 215 | 41.8 | 0.267 | 3.5 | 19.4 | 2289 | 89.2 | 6.24 | Soft-Speed Separation |
| 737 | Hicks, Jackson | DOW_EAS1 | Four-Seam | 72 | 41.7 | 0.280 | 17.9 | 12.2 | 2119 | 86.5 | 5.41 | Soft-Speed Separation |
| 738 | Figueredo, Kevin | WIN_CIT29 | Sinker | 209 | 41.6 | 0.272 | 12.1 | -14.4 | 2017 | 88.1 | 5.39 | Soft-Speed Separation |
| 739 | Maryniak, Connor | NEW_JER6 | Four-Seam | 125 | 41.4 | 0.250 | 13.0 | 7.1 | 2456 | 90.0 | 5.78 | Soft-Speed Separation |
| 740 | Gordillo, Lucas | TRI_VAL | Four-Seam | 247 | 41.3 | 0.292 | 16.9 | 9.9 | 2102 | 90.9 | 6.19 | Soft-Speed Separation |
| 741 | Simone, Andrew | TRO_AIG | Four-Seam | 187 | 41.3 | 0.265 | 15.9 | 8.6 | 1932 | 91.0 | 6.06 | Soft-Speed Separation |
| 742 | Anderson, Nathan | EVA_OTT | Four-Seam | 52 | 41.2 | 0.290 | 16.3 | 10.3 | 2267 | 90.5 | 6.39 | Soft-Speed Separation |
| 743 | Brito, Richard | NEW_ENG23 | Four-Seam | 61 | 41.2 | 0.296 | 16.3 | 11.3 | 2385 | 93.5 | 6.54 | Soft-Speed Separation |
| 744 | Lefebvre, Charles | TRO_AIG | Changeup | 115 | 41.2 | 0.275 | 5.8 | 14.7 | 1613 | 82.6 | 6.69 | Soft-Speed Separation |
| 745 | Kaftan, Eddie | FLO_Y'A | Sinker | 128 | 41.1 | 0.264 | 7.4 | 13.6 | 2035 | 86.0 | 5.43 | Soft-Speed Separation |
| 746 | Jones, Breyln | NEW_JER6 | Cutter | 69 | 41.0 | 0.283 | 8.5 | -0.2 | 2062 | 87.1 | 5.84 | Soft-Speed Separation |
| 747 | Elliott, Eric | MIS_MUD | Four-Seam | 127 | 41.0 | 0.239 | 21.2 | -3.9 | 2228 | 87.2 | 6.24 | Soft-Speed Separation |
| 748 | Milburn, Isaac | FLO_Y'A | Four-Seam | 236 | 40.9 | 0.270 | 11.8 | -9.3 | 2089 | 87.6 | 5.53 | Soft-Speed Separation |
| 749 | Perez, Kelvin | WAS_WIL3 | Sinker | 109 | 40.8 | 0.302 | 9.6 | 14.0 | 2030 | 89.0 | 6.01 | Soft-Speed Separation |
| 750 | Morrissey, Joe | EVA_OTT | Four-Seam | 151 | 40.8 | 0.269 | 19.4 | 11.2 | 2355 | 89.5 | 5.76 | Soft-Speed Separation |
| 751 | Smith, Donny | JOL_SLA | Four-Seam | 52 | 40.7 | 0.292 | 15.1 | 11.0 | 2198 | 88.1 | 5.87 | Soft-Speed Separation |
| 752 | Williams, Brian | MIS_MUD | Four-Seam | 606 | 40.6 | 0.262 | 17.8 | 8.3 | 2250 | 89.3 | 6.34 | Soft-Speed Separation |
| 753 | Whitesell, Max | FLO_Y'A | Sinker | 73 | 40.6 | 0.286 | 12.7 | 14.0 | 1932 | 89.4 | 6.30 | Soft-Speed Separation |
| 754 | Trizuto, Colin | WAG_SEA | Changeup | 69 | 40.5 | 0.270 | 7.0 | 18.5 | 1961 | 84.0 | 5.35 | Soft-Speed Separation |
| 755 | Hill, Kaleb | OTT_TIT | Sinker | 379 | 40.5 | 0.280 | 10.6 | -15.5 | 1883 | 89.7 | 5.52 | Soft-Speed Separation |
| 756 | Barreto, Brayhans | TRI_VAL | Four-Seam | 127 | 40.4 | 0.284 | 15.4 | -9.2 | 2034 | 88.6 | 6.14 | Soft-Speed Separation |
| 757 | Phelps, Travis | FLO_Y'A | Four-Seam | 53 | 40.4 | 0.284 | 13.7 | 5.1 | 2092 | 90.6 | 6.64 | Soft-Speed Separation |
| 758 | Chapple, Bronson | TRO_AIG | Four-Seam | 95 | 40.4 | 0.295 | 11.2 | 8.8 | 2129 | 90.2 | 6.67 | Soft-Speed Separation |
| 759 | Parsons, Billy | SUS_COU1 | Sinker | 61 | 40.4 | 0.258 | 13.0 | 9.8 | 2277 | 89.4 | 5.78 | Soft-Speed Separation |
| 760 | Serratos, Oscar | WIN_CIT29 | Four-Seam | 81 | 40.4 | 0.278 | 13.0 | 10.1 | 2204 | 91.7 | 5.61 | Soft-Speed Separation |
| 761 | Drakeford, Dosie | NEW_JER6 | Four-Seam | 130 | 40.4 | 0.252 | 19.1 | 10.1 | 2340 | 91.4 | 5.83 | Soft-Speed Separation |
| 762 | Belton, Hunter | MIS_MUD | Four-Seam | 129 | 40.1 | 0.297 | 13.0 | 10.6 | 2231 | 86.4 | 6.13 | Soft-Speed Separation |
| 763 | Thiels, Brenton | MIS_MUD | Cutter | 51 | 40.1 | 0.314 | 9.4 | 4.5 | 2311 | 86.3 | 6.84 | Soft-Speed Separation |
| 764 | Campbell, AJ | WIN_CIT29 | Four-Seam | 408 | 40.0 | 0.280 | 11.3 | 7.9 | 2412 | 88.4 | 5.47 | Soft-Speed Separation |
| 765 | Thompson, Ross | SCH_BOO | Four-Seam | 464 | 39.9 | 0.263 | 16.0 | 12.0 | 2054 | 89.1 | 5.74 | Soft-Speed Separation |
| 766 | Peters, Andrew | NEW_JER6 | Four-Seam | 270 | 39.9 | 0.274 | 15.3 | 7.9 | 2229 | 93.2 | 6.66 | Soft-Speed Separation |
| 767 | Bice, Emmett | NEW_YOR13 | Four-Seam | 201 | 39.8 | 0.281 | 15.5 | 7.4 | 2231 | 89.1 | 5.90 | Soft-Speed Separation |
| 768 | Steinhauer, Ryan | NEW_JER6 | Changeup | 93 | 39.7 | 0.261 | 10.8 | -12.5 | 1665 | 82.3 | 6.31 | Soft-Speed Separation |
| 769 | Sohosky, Zac | MIA_RED | Four-Seam | 58 | 39.6 | 0.271 | 14.3 | -7.5 | 1888 | 88.4 | 6.33 | Soft-Speed Separation |
| 770 | Frey, Hayden | TOL_ROC | Four-Seam | 55 | 39.6 | 0.323 | 9.7 | -17.4 | 2137 | 88.8 | 6.37 | Soft-Speed Separation |
| 771 | Wiltse, Ryan | EVA_OTT | Four-Seam | 474 | 39.5 | 0.262 | 20.3 | 9.9 | 2165 | 87.3 | 6.06 | Soft-Speed Separation |
| 772 | Pindel, Buddie | SCH_BOO | Changeup | 123 | 39.4 | 0.284 | 3.5 | 11.6 | 1379 | 80.9 | 5.50 | Soft-Speed Separation |
| 773 | Rivera, Matthew | NEW_ENG23 | Four-Seam | 143 | 39.4 | 0.261 | 17.9 | 8.9 | 2393 | 88.2 | 6.42 | Soft-Speed Separation |
| 774 | Gregory, Ben | GAT_GRI | Changeup | 76 | 39.3 | 0.279 | 9.1 | 13.6 | 1914 | 82.1 | 6.54 | Soft-Speed Separation |
| 775 | Tiburcio, David | DOW_EAS1 | Sinker | 173 | 39.3 | 0.275 | 11.7 | 17.6 | 2237 | 92.6 | 5.17 | Soft-Speed Separation |
| 776 | Pindel, Buddie | SCH_BOO | Sinker | 188 | 39.2 | 0.282 | 13.9 | 14.6 | 2135 | 89.9 | 5.69 | Soft-Speed Separation |
| 777 | Estrella, Noah | TRI_VAL | Four-Seam | 200 | 39.0 | 0.265 | 17.1 | 12.5 | 2227 | 92.7 | 5.78 | Soft-Speed Separation |
| 778 | Morel, Yohanse | OTT_TIT | Sinker | 242 | 39.0 | 0.301 | 9.0 | 18.6 | 2256 | 91.1 | 5.26 | Soft-Speed Separation |
| 779 | Walsh, John | MIS_MUD | Four-Seam | 79 | 38.7 | 0.240 | 13.1 | -11.7 | 1910 | 84.4 | 5.62 | Soft-Speed Separation |
| 780 | Marynczak, Arlo | TRI_VAL | Sinker | 53 | 38.6 | 0.281 | 14.6 | 12.6 | 2075 | 88.2 | 6.18 | Soft-Speed Separation |
| 781 | Sanchez, Dikember | LAK_ERI24 | Four-Seam | 131 | 38.5 | 0.278 | 11.7 | 7.8 | 2279 | 91.3 | 5.77 | Soft-Speed Separation |
| 782 | Leach, Landon | TRO_AIG | Sinker | 62 | 38.5 | 0.305 | 9.6 | 11.5 | 1912 | 91.7 | 5.70 | Soft-Speed Separation |
| 783 | Oe, Ryoya | OTT_TIT | Four-Seam | 58 | 38.4 | 0.283 | 18.1 | -3.8 | 2125 | 84.6 | 5.70 | Soft-Speed Separation |
| 784 | Chapple, Bronson | TRO_AIG | Sinker | 128 | 38.4 | 0.292 | 7.5 | 13.4 | 2067 | 90.5 | 6.50 | Soft-Speed Separation |
| 785 | Martinez, Mason | TRI_VAL | Changeup | 76 | 38.1 | 0.285 | 8.2 | 17.5 | 2180 | 82.3 | 6.67 | Soft-Speed Separation |
| 786 | Donnan, Blake | FLO_Y'A | Sinker | 170 | 38.1 | 0.295 | 6.6 | 17.4 | 1978 | 90.7 | 5.86 | Soft-Speed Separation |
| 787 | Escobar, Anthony | TRO_AIG | Sinker | 153 | 38.0 | 0.333 | 13.0 | 13.4 | 2111 | 89.0 | 6.37 | Soft-Speed Separation |
| 788 | Baker, Luke | EVA_OTT | Four-Seam | 87 | 37.9 | 0.309 | 14.2 | -10.6 | 2426 | 87.1 | 5.86 | Soft-Speed Separation |
| 789 | Nova, Fraynel | LAK_ERI24 | Sinker | 126 | 37.9 | 0.294 | 9.1 | 13.4 | 2041 | 90.1 | 6.09 | Soft-Speed Separation |
| 790 | Rodriguez, Esteban | WAS_WIL3 | Four-Seam | 167 | 37.8 | 0.290 | 17.0 | 4.4 | 2187 | 87.9 | 5.97 | Soft-Speed Separation |
| 791 | Eldred, Zach | NEW_ENG23 | Splitter | 80 | 37.6 | 0.309 | 5.0 | 4.2 | 968 | 84.2 | 6.09 | Soft-Speed Separation |
| 792 | Townes, Holland | SCH_BOO | Sinker | 94 | 37.5 | 0.273 | 13.1 | 15.4 | 2241 | 92.2 | 5.21 | Soft-Speed Separation |
| 793 | Matos, Dwayne | OTT_TIT | Sinker | 342 | 37.5 | 0.288 | 11.6 | 18.5 | 2124 | 90.6 | 6.01 | Soft-Speed Separation |
| 794 | Lovin, Xander | GAT_GRI | Four-Seam | 314 | 37.5 | 0.286 | 15.8 | 6.1 | 2312 | 91.3 | 4.97 | Soft-Speed Separation |
| 795 | Thiels, Brenton | MIS_MUD | Four-Seam | 193 | 37.5 | 0.282 | 15.9 | 11.2 | 2254 | 89.4 | 6.78 | Soft-Speed Separation |
| 796 | Woolfolk, Dallas | SCH_BOO | Four-Seam | 101 | 37.4 | 0.239 | 19.4 | 13.4 | 2327 | 92.5 | 5.63 | Soft-Speed Separation |
| 797 | Glickstein, Aaron | SCH_BOO | Cutter | 58 | 37.3 | 0.251 | 9.9 | 1.0 | 2263 | 85.8 | 5.67 | Soft-Speed Separation |
| 798 | Voytko, Fawster | TRO_AIG | Four-Seam | 144 | 37.3 | 0.292 | 15.5 | 5.4 | 2169 | 89.5 | 6.77 | Soft-Speed Separation |
| 799 | Reeves, Cobe | NEW_YOR13 | Changeup | 62 | 37.2 | 0.310 | 5.2 | -13.0 | 1388 | 84.4 | 6.33 | Soft-Speed Separation |
| 800 | Grills, Evan | OTT_TIT | Four-Seam | 51 | 37.2 | 0.264 | 16.8 | -10.6 | 2220 | 88.3 | 5.44 | Soft-Speed Separation |
| 801 | Sabatine, Gino | TRI_VAL | Changeup | 287 | 37.1 | 0.294 | 8.3 | 15.5 | 1784 | 85.1 | 5.07 | Soft-Speed Separation |
| 802 | Rodriguez, Joe Joe | NEW_JER6 | Sinker | 192 | 37.0 | 0.288 | 13.2 | 15.3 | 2070 | 91.8 | 5.71 | Soft-Speed Separation |
| 803 | Almonte, Dawil | EVA_OTT | Four-Seam | 142 | 36.9 | 0.297 | 11.2 | 9.4 | 2028 | 92.0 | 5.50 | Soft-Speed Separation |
| 804 | Salata, Derek | SCH_BOO | Cutter | 139 | 36.8 | 0.308 | 11.6 | 0.2 | 2346 | 87.6 | 5.83 | Soft-Speed Separation |
| 805 | Carroll, Jake | JOL_SLA | Four-Seam | 241 | 36.8 | 0.293 | 17.6 | -6.5 | 2140 | 86.6 | 7.09 | Soft-Speed Separation |
| 806 | Nakata, Yuto | QUE_CAP | Four-Seam | 243 | 36.7 | 0.293 | 15.9 | 9.8 | 2087 | 92.4 | 5.78 | Soft-Speed Separation |
| 807 | Gilleran, Jimmy | NEW_ENG23 | Four-Seam | 101 | 36.7 | 0.281 | 16.3 | 13.9 | 2165 | 88.4 | 5.65 | Soft-Speed Separation |
| 808 | Jones, Logan | TRI_VAL | Sinker | 109 | 36.7 | 0.288 | 12.1 | 17.9 | 2286 | 90.0 | 5.34 | Soft-Speed Separation |
| 809 | Toribio, Noe | TRO_AIG | Sinker | 428 | 36.6 | 0.285 | 11.5 | 17.8 | 2029 | 90.2 | 5.79 | Soft-Speed Separation |
| 810 | Manning, Noah | WIN_CIT29 | Sinker | 55 | 36.5 | 0.324 | 4.7 | 19.5 | 2312 | 90.7 | 5.51 | Soft-Speed Separation |
| 811 | Tomczak, Anthony | EVA_OTT | Sinker | 70 | 36.4 | 0.270 | 12.3 | 17.2 | 2284 | 93.9 | 5.93 | Soft-Speed Separation |
| 812 | Thiels, Brenton | MIS_MUD | Slider | 86 | 36.3 | 0.323 | 6.5 | 1.3 | 2273 | 83.2 | 6.72 | Soft-Speed Separation |
| 813 | Gartland, Chad | TRI_VAL | Four-Seam | 119 | 36.3 | 0.276 | 15.1 | 9.0 | 2072 | 89.0 | 6.12 | Soft-Speed Separation |
| 814 | Burcham, Jacob | GAT_GRI | Four-Seam | 89 | 36.2 | 0.289 | 12.6 | 11.7 | 2346 | 92.3 | 6.33 | Soft-Speed Separation |
| 815 | Hickey, Matt | GAT_GRI | Four-Seam | 89 | 36.1 | 0.283 | 16.1 | 11.7 | 2303 | 89.9 | 5.51 | Soft-Speed Separation |
| 816 | Lawson, Nathan | FLO_Y'A | Four-Seam | 80 | 35.8 | 0.314 | 14.6 | 8.4 | 2239 | 88.8 | 6.10 | Soft-Speed Separation |
| 817 | Harris, Ben | GAT_GRI | Sinker | 111 | 35.8 | 0.298 | 13.3 | 15.0 | 2243 | 90.2 | 5.89 | Soft-Speed Separation |
| 818 | Hampton, Ky | OTT_TIT | Sinker | 155 | 35.7 | 0.294 | 7.2 | 16.1 | 2145 | 88.4 | 6.21 | Soft-Speed Separation |
| 819 | Masick, Jason | NEW_YOR13 | Four-Seam | 73 | 35.7 | 0.282 | 14.8 | 8.0 | 2131 | 94.3 | 6.07 | Soft-Speed Separation |
| 820 | Miner, Jace | DOW_EAS1 | Sinker | 115 | 35.7 | 0.308 | 6.4 | -12.0 | 1854 | 88.6 | 5.98 | Soft-Speed Separation |
| 821 | Sabatine, Gino | TRI_VAL | Four-Seam | 63 | 35.6 | 0.317 | 14.6 | 11.5 | 1846 | 88.6 | 5.02 | Soft-Speed Separation |
| 822 | Linderman, Greyson | JOL_SLA | Sinker | 78 | 35.6 | 0.310 | 11.7 | 14.7 | 2120 | 93.8 | 5.46 | Soft-Speed Separation |
| 823 | Puccetti, Dominic | OTT_TIT | Changeup | 162 | 35.5 | 0.292 | 14.4 | -6.7 | 1711 | 84.2 | 5.42 | Soft-Speed Separation |
| 824 | Duby, Bill | NEW_JER6 | Splitter | 60 | 35.2 | 0.314 | 6.7 | 4.1 | 985 | 78.8 | 6.07 | Soft-Speed Separation |
| 825 | Bell, Jacob | SCH_BOO | Four-Seam | 98 | 35.1 | 0.282 | 16.7 | 11.7 | 2325 | 87.1 | 6.10 | Soft-Speed Separation |
| 826 | Cosentino, Nick | JOL_SLA | Four-Seam | 84 | 35.1 | 0.278 | 16.9 | 11.1 | 2220 | 90.5 | 5.48 | Soft-Speed Separation |
| 827 | Gwin, Riley | QUE_CAP | Changeup | 52 | 35.0 | 0.294 | 13.0 | -10.7 | 1784 | 82.8 | 6.25 | Soft-Speed Separation |
| 828 | Biddinger, Tyler | WIN_CIT29 | Sinker | 118 | 34.9 | 0.324 | 7.0 | 16.7 | 2226 | 90.2 | 5.31 | Soft-Speed Separation |
| 829 | Heredia-Bustos, Rolando | DOW_EAS1 | Sinker | 135 | 34.6 | 0.273 | 13.4 | 16.8 | 2111 | 87.9 | 5.71 | Soft-Speed Separation |
| 830 | Thornton, Tyler | NEW_ENG23 | Changeup | 187 | 34.3 | 0.291 | 9.6 | 14.0 | 1820 | 83.5 | 4.94 | Soft-Speed Separation |
| 831 | Nettleton, Blake | WIN_CIT29 | Four-Seam | 231 | 34.0 | 0.314 | 14.5 | 8.0 | 2139 | 89.5 | 6.49 | Soft-Speed Separation |
| 832 | Smith, Ben | NEW_ENG23 | Four-Seam | 89 | 34.0 | 0.283 | 10.4 | -10.2 | 2167 | 86.8 | 6.30 | Soft-Speed Separation |
| 833 | O'Hanlon, Michael | WAS_WIL3 | Four-Seam | 141 | 33.8 | 0.323 | 15.8 | 10.8 | 2134 | 88.4 | 5.92 | Soft-Speed Separation |
| 834 | McKillican, Adam | QUE_CAP | Four-Seam | 52 | 33.0 | 0.320 | 14.5 | 9.9 | 2042 | 88.7 | 6.70 | Soft-Speed Separation |
| 835 | Peters, Garrett | NEW_YOR13 | Sinker | 62 | 32.7 | 0.282 | 17.4 | -15.9 | 2199 | 85.9 | 5.89 | Soft-Speed Separation |
| 836 | Cox, Carter | NIU_HUS | Four-Seam | 75 | 32.6 | 0.299 | 14.5 | -7.5 | 2226 | 87.3 | 6.59 | Soft-Speed Separation |
| 837 | O'Brien, Keenan | SUS_COU1 | Sinker | 60 | 32.6 | 0.268 | 10.7 | 15.8 | 2090 | 90.2 | 5.79 | Soft-Speed Separation |
| 838 | Belton, Hunter | MIS_MUD | Changeup | 55 | 32.1 | 0.336 | 11.4 | 13.9 | 2006 | 81.0 | 6.10 | Soft-Speed Separation |
| 839 | Duby, Bill | NEW_JER6 | Changeup | 163 | 30.9 | 0.286 | 11.5 | 13.2 | 1945 | 83.7 | 6.61 | Soft-Speed Separation |
| 840 | Givens-Craig, Hayden | SUS_COU1 | Changeup | 85 | 30.9 | 0.331 | 7.9 | 11.6 | 1666 | 80.6 | 5.80 | Soft-Speed Separation |
| 841 | Benitez, Jorge | NEW_JER6 | Four-Seam | 85 | 30.8 | 0.318 | 9.9 | -10.0 | 2107 | 93.1 | 5.96 | Soft-Speed Separation |
| 842 | Rybarczyk, Ty | JOL_SLA | Four-Seam | 61 | 30.6 | 0.322 | 19.0 | 11.7 | 2309 | 91.3 | 5.50 | Soft-Speed Separation |
| 843 | Kramer, Cameron | TRO_AIG | Sinker | 69 | 30.4 | 0.283 | 13.1 | 16.0 | 2251 | 90.5 | 6.25 | Soft-Speed Separation |
| 844 | Beriguete, Randy | LAK_ERI24 | Four-Seam | 102 | 30.2 | 0.326 | 11.6 | 7.3 | 2284 | 93.3 | 6.47 | Soft-Speed Separation |
| 845 | Gaskey, Blake | NIU_HUS | Four-Seam | 62 | 29.3 | 0.346 | 10.3 | 13.8 | 2190 | 85.0 | 6.73 | Soft-Speed Separation |
| 846 | Thornton, Tyler | NEW_ENG23 | Sinker | 121 | 29.2 | 0.326 | 9.7 | 14.8 | 1956 | 84.7 | 5.53 | Soft-Speed Separation |
| 847 | Foy, Corbin | LAK_ERI24 | Sinker | 57 | 28.7 | 0.335 | 11.4 | 13.2 | 2243 | 91.8 | 6.33 | Soft-Speed Separation |
| 848 | Andueza, Axel | DOW_EAS1 | Splitter | 96 | 28.5 | 0.338 | 3.4 | 7.9 | 900 | 81.7 | 5.19 | Soft-Speed Separation |
| 849 | Smith, Ethan | WIN_CIT29 | Changeup | 52 | 26.8 | 0.319 | 9.1 | 14.6 | 2000 | 82.7 | 6.38 | Soft-Speed Separation |
| 850 | Miranda, Agnel | NEW_JER6 | Four-Seam | 50 | 26.7 | 0.277 | 15.6 | 9.8 | 2186 | 91.4 | 7.45 | Soft-Speed Separation |
| 851 | Smith, Donny | JOL_SLA | Sinker | 146 | 25.6 | 0.328 | 10.8 | 15.5 | 2124 | 88.8 | 5.76 | Soft-Speed Separation |
| 852 | Anderson, Colt | WAS_WIL3 | Changeup | 51 | 24.0 | 0.320 | 7.9 | -6.0 | 1491 | 79.2 | 6.51 | Soft-Speed Separation |
| 853 | Nabholz, Nate | TRI_VAL | Four-Seam | 99 | 20.0 | 0.358 | 18.5 | 10.3 | 2088 | 91.2 | 5.75 | Soft-Speed Separation |

## Undervalued Movement Pitches

Definition: movement quality percentile at least 75, with Pitch Value Score at or below league average.

| Rank | Pitcher | Team | Pitch | Pitches | PVS | xwOBA | IVB | HB | Spin | Velo | Ext | Archetype |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | Westcott, Zac | FLO_Y'A | Curveball | 163 | 20.7 | 0.378 | -15.2 | -9.2 | 1872 | 67.1 | 5.48 | Tight High-Spin Breakers |
| 2 | Huter, Blayne | SUS_COU1 | Curveball | 103 | 44.5 | 0.272 | -5.1 | -14.2 | 2137 | 73.7 | 6.01 | Tight High-Spin Breakers |
| 3 | Voytko, Fawster | TRO_AIG | Curveball | 65 | 33.9 | 0.331 | -7.3 | -11.8 | 2338 | 74.6 | 6.05 | Tight High-Spin Breakers |
| 4 | Kassebaum, Torin | LON_ISL22 | Curveball | 55 | 39.9 | 0.308 | 1.1 | 10.2 | 2155 | 71.6 | 5.31 | Tight High-Spin Breakers |
| 5 | Plumadore, Carson | WIN_CIT29 | Curveball | 77 | 21.9 | 0.366 | 1.3 | -6.9 | 2483 | 75.4 | 5.57 | Tight High-Spin Breakers |
| 6 | Campbell, Tyler | MIS_MUD | Slider | 199 | 49.9 | 0.271 | 8.1 | 3.9 | 2211 | 74.3 | 5.70 | Tight High-Spin Breakers |
| 7 | Johnston, Spencer | DOW_EAS1 | Curveball | 66 | 25.2 | 0.323 | -4.7 | -6.0 | 2133 | 74.4 | 5.68 | Tight High-Spin Breakers |
| 8 | Baker, Luke | EVA_OTT | Curveball | 59 | 47.6 | 0.245 | -7.4 | 9.7 | 2694 | 75.5 | 5.51 | Tight High-Spin Breakers |
| 9 | Brodsky, Jack | WAS_WIL3 | Curveball | 83 | 36.3 | 0.327 | -8.7 | -11.7 | 2668 | 76.9 | 5.33 | Tight High-Spin Breakers |
| 10 | Petery, Dylan | WIN_CIT29 | Slider | 54 | 46.3 | 0.231 | -0.6 | -12.0 | 2606 | 78.1 | 5.74 | Tight High-Spin Breakers |
| 11 | Bice, Emmett | NEW_YOR13 | Curveball | 170 | 41.0 | 0.296 | -10.3 | -13.3 | 2986 | 79.1 | 5.51 | Tight High-Spin Breakers |
| 12 | Eldred, Zach | NEW_ENG23 | Curveball | 81 | 37.6 | 0.316 | -9.8 | -12.4 | 2489 | 77.6 | 5.88 | Tight High-Spin Breakers |
| 13 | Good, Ty | GAT_GRI | Curveball | 155 | 43.1 | 0.258 | -7.6 | -4.5 | 2128 | 75.0 | 5.62 | Tight High-Spin Breakers |
| 14 | Voytko, Fawster | TRO_AIG | Slider | 51 | 32.4 | 0.310 | 0.7 | -11.9 | 2334 | 78.5 | 6.23 | Tight High-Spin Breakers |
| 15 | Martzolf, Max | OTT_TIT | Curveball | 71 | 43.2 | 0.291 | -4.2 | 11.1 | 2155 | 73.9 | 5.43 | Tight High-Spin Breakers |
| 16 | Villalobos, Jonaiker | FLO_Y'A | Curveball | 110 | 37.4 | 0.274 | -5.3 | 5.5 | 2264 | 74.7 | 5.32 | Tight High-Spin Breakers |
| 17 | Debban, Caleb | NEW_JER6 | Curveball | 206 | 46.0 | 0.277 | -7.2 | 18.6 | 2810 | 76.9 | 5.91 | Tight High-Spin Breakers |
| 18 | Williams, Pierce | NEW_ENG23 | Curveball | 151 | 38.8 | 0.279 | -5.7 | 6.4 | 2172 | 75.4 | 5.77 | Tight High-Spin Breakers |
| 19 | Lovin, Xander | GAT_GRI | Curveball | 65 | 21.1 | 0.355 | -9.3 | -12.3 | 2634 | 76.9 | 4.64 | Tight High-Spin Breakers |
| 20 | Misla, Luis | TRI_VAL | Curveball | 156 | 47.7 | 0.256 | -5.5 | 9.2 | 2789 | 77.0 | 5.12 | Tight High-Spin Breakers |
| 21 | Kostura, Brit | WAS_WIL3 | Slider | 56 | 41.8 | 0.273 | -0.7 | 5.1 | 2157 | 74.8 | 5.04 | Tight High-Spin Breakers |
| 22 | Kaftan, Eddie | FLO_Y'A | Slider | 62 | 48.0 | 0.234 | 1.1 | -6.3 | 2437 | 77.1 | 4.72 | Tight High-Spin Breakers |
| 23 | Figueredo, Kevin | WIN_CIT29 | Curveball | 78 | 44.2 | 0.279 | -3.5 | 4.9 | 2324 | 75.8 | 5.00 | Tight High-Spin Breakers |
| 24 | Soto, Carlos | JOL_SLA | Slider | 96 | 37.4 | 0.302 | -1.8 | -8.8 | 2509 | 78.2 | 5.09 | Tight High-Spin Breakers |
| 25 | Barker, Alex | NEW_YOR13 | Curveball | 90 | 41.2 | 0.263 | -5.6 | 10.1 | 2256 | 76.3 | 5.75 | Tight High-Spin Breakers |
| 26 | Sechrist, Zander | WAS_WIL3 | Changeup | 207 | 37.0 | 0.294 | 7.6 | -14.7 | 1674 | 76.8 | 5.66 | Tight High-Spin Breakers |
| 27 | Quigley, Michael | NEW_ENG23 | Curveball | 79 | 38.5 | 0.296 | -12.3 | -12.7 | 2567 | 78.8 | 5.42 | Tight High-Spin Breakers |
| 28 | Floyd, Conner | QUE_CAP | Curveball | 58 | 49.9 | 0.252 | -2.7 | -17.4 | 2113 | 77.3 | 5.02 | Tight High-Spin Breakers |
| 29 | Peyton, Blake | GAT_GRI | Curveball | 90 | 44.7 | 0.225 | -5.8 | 8.6 | 2673 | 77.8 | 5.24 | Tight High-Spin Breakers |
| 30 | Okumura, Shuto | WAS_WIL3 | Four-Seam | 60 | 43.6 | 0.275 | 6.1 | 7.6 | 1757 | 75.3 | 5.56 | Tight High-Spin Breakers |

## Top 20 Scouting Reports

1. **Grounds, Jackson, DOW_EAS1 Curveball** (Tight High-Spin Breakers): PVS 80.0, xwOBA 0.108. Shape: IVB -10.5, HB -12.0, 81.4 mph, 1946 rpm, 5.35 ft extension. Scouting read: low ride/drop, big horizontal; current results place it #1 overall and #1 within its pitch type.
2. **Carroll, Jake, JOL_SLA Slider** (Tight High-Spin Breakers): PVS 80.0, xwOBA 0.190. Shape: IVB -6.2, HB 7.9, 75.3 mph, 2033 rpm, 6.10 ft extension. Scouting read: low ride/drop, soft velo; current results place it #2 overall and #1 within its pitch type.
3. **Morgan, Cooper, QUE_CAP Curveball** (Tight High-Spin Breakers): PVS 80.0, xwOBA 0.146. Shape: IVB -1.5, HB 17.6, 75.6 mph, 2685 rpm, 5.25 ft extension. Scouting read: low ride/drop, big horizontal, high spin, soft velo; current results place it #3 overall and #2 within its pitch type.
4. **Ryan, Dillon, NEW_ENG23 Slider** (Tight High-Spin Breakers): PVS 79.9, xwOBA 0.144. Shape: IVB -2.0, HB -8.1, 85.4 mph, 2494 rpm, 5.82 ft extension. Scouting read: low ride/drop, high spin; current results place it #4 overall and #2 within its pitch type.
5. **Leduc, Zachary, TRO_AIG Slider** (Tight High-Spin Breakers): PVS 79.2, xwOBA 0.092. Shape: IVB 1.5, HB -4.5, 83.4 mph, 2118 rpm, 6.15 ft extension. Scouting read: low ride/drop; current results place it #5 overall and #3 within its pitch type.
6. **Zentko, Dylan, EVA_OTT Changeup** (Tight High-Spin Breakers): PVS 78.6, xwOBA 0.155. Shape: IVB 7.3, HB -11.4, 78.8 mph, 1311 rpm, 5.82 ft extension. Scouting read: big horizontal, soft velo; current results place it #6 overall and #1 within its pitch type.
7. **Lawson, Nathan, FLO_Y'A Changeup** (Soft-Speed Separation): PVS 78.2, xwOBA 0.166. Shape: IVB 7.9, HB 10.2, 79.6 mph, 1409 rpm, 5.77 ft extension. Scouting read: big horizontal, soft velo; current results place it #7 overall and #2 within its pitch type.
8. **Vecerka, Boris, QUE_CAP Slider** (Tight High-Spin Breakers): PVS 77.6, xwOBA 0.129. Shape: IVB 2.4, HB -11.9, 82.5 mph, 2472 rpm, 5.61 ft extension. Scouting read: low ride/drop, big horizontal, high spin; current results place it #8 overall and #4 within its pitch type.
9. **Peyton, Blake, GAT_GRI Changeup** (Tight High-Spin Breakers): PVS 77.3, xwOBA 0.141. Shape: IVB 10.3, HB -13.2, 81.0 mph, 1927 rpm, 6.10 ft extension. Scouting read: big horizontal; current results place it #9 overall and #3 within its pitch type.
10. **Alpern, Liam, FLO_Y'A Slider** (Tight High-Spin Breakers): PVS 76.4, xwOBA 0.113. Shape: IVB -4.0, HB 11.5, 76.8 mph, 2219 rpm, 5.55 ft extension. Scouting read: low ride/drop, big horizontal, soft velo; current results place it #10 overall and #5 within its pitch type.
11. **Serrano, Elio, NEW_JER6 Changeup** (Soft-Speed Separation): PVS 75.9, xwOBA 0.148. Shape: IVB 11.1, HB 11.7, 82.1 mph, 1829 rpm, 5.92 ft extension. Scouting read: big horizontal; current results place it #11 overall and #4 within its pitch type.
12. **Jones, Logan, TRI_VAL Slider** (Tight High-Spin Breakers): PVS 74.7, xwOBA 0.191. Shape: IVB 2.5, HB 2.3, 83.5 mph, 2341 rpm, 5.69 ft extension. Scouting read: low ride/drop, high spin; current results place it #12 overall and #6 within its pitch type.
13. **Grounds, Jackson, DOW_EAS1 Four-Seam** (Soft-Speed Separation): PVS 74.4, xwOBA 0.159. Shape: IVB 17.0, HB 14.2, 92.5 mph, 2163 rpm, 5.59 ft extension. Scouting read: plus ride, big horizontal, power velocity; current results place it #13 overall and #1 within its pitch type.
14. **Davis, Tyler, WIN_CIT29 Four-Seam** (Soft-Speed Separation): PVS 74.4, xwOBA 0.111. Shape: IVB 21.2, HB 5.6, 89.3 mph, 2171 rpm, 5.86 ft extension. Scouting read: plus ride, power velocity; current results place it #14 overall and #2 within its pitch type.
15. **Debban, Caleb, NEW_JER6 Four-Seam** (Soft-Speed Separation): PVS 73.8, xwOBA 0.174. Shape: IVB 13.1, HB -4.6, 87.2 mph, 2325 rpm, 6.58 ft extension. Scouting read: high spin, extension; current results place it #15 overall and #3 within its pitch type.
16. **Garcia, Hector, WAS_WIL3 Splitter** (Soft-Speed Separation): PVS 73.6, xwOBA 0.185. Shape: IVB 11.7, HB 7.6, 78.2 mph, 1216 rpm, 5.92 ft extension. Scouting read: soft velo; current results place it #16 overall and #1 within its pitch type.
17. **Bargo, Casey, NEW_ENG23 Slider** (Tight High-Spin Breakers): PVS 73.6, xwOBA 0.176. Shape: IVB 1.5, HB -5.0, 83.6 mph, 2416 rpm, 5.66 ft extension. Scouting read: low ride/drop, high spin; current results place it #17 overall and #7 within its pitch type.
18. **Hickey, Matt, GAT_GRI Slider** (Tight High-Spin Breakers): PVS 73.5, xwOBA 0.191. Shape: IVB -1.7, HB -6.5, 79.9 mph, 2258 rpm, 5.34 ft extension. Scouting read: low ride/drop, soft velo; current results place it #18 overall and #8 within its pitch type.
19. **Escobar, Anthony, TRO_AIG Changeup** (Soft-Speed Separation): PVS 72.7, xwOBA 0.156. Shape: IVB 10.3, HB 11.7, 79.1 mph, 1630 rpm, 6.21 ft extension. Scouting read: big horizontal, soft velo, extension; current results place it #19 overall and #5 within its pitch type.
20. **Harper, Scott, NEW_YOR13 Slider** (Tight High-Spin Breakers): PVS 72.6, xwOBA 0.155. Shape: IVB 3.3, HB -16.6, 79.8 mph, 2665 rpm, 5.58 ft extension. Scouting read: big horizontal, high spin, soft velo; current results place it #20 overall and #9 within its pitch type.

## Plots

- `plots\pitch_movement_archetypes\cluster_count_selection.png`
- `plots\pitch_movement_archetypes\archetypes_hb_ivb.png`
- `plots\pitch_movement_archetypes\archetypes_velocity_spin.png`
- `plots\pitch_movement_archetypes\archetypes_pca.png`
- `plots\pitch_movement_archetypes\archetype_pitch_value.png`