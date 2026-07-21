# Frontier League Movement Archetypes

- Input file: `data\processed\movement_score_inputs.csv`
- Scored output: `data\processed\pitch_movement_archetypes.csv`
- Cluster summary: `data\processed\pitch_movement_archetype_summary.csv`
- Highest-performing archetype pitch list: `data\processed\highest_performing_archetype_pitches.csv`
- Undervalued pitch list: `data\processed\undervalued_movement_pitches.csv`
- Qualified pitcher-pitch types clustered: 889
- Features clustered: IVB, HB, spin rate, velocity, extension
- Selected cluster count: 2
- Full methodology write-up: `reports/FRONTIER_PITCH_VALUE_METHODOLOGY.md`

## How To Read This Report

Higher Pitch Value Score is better. It means the pitch has the outcome profile associated with lower expected xwOBA damage. Archetypes are movement-shape groups, not direct pitcher grades.

The cluster labels describe the average movement identity of each group. Average Pitch Value Score by cluster tells us which movement families performed best in this dataset, but individual pitches within a cluster can still vary widely based on command, usage, sequencing, and sample size.

## Cluster Count Test

| k | Inertia | Silhouette |
|---:|---:|---:|
| 2 | 3034.69 | 0.3042 **selected** |
| 3 | 2444.27 | 0.3009 |
| 4 | 2020.36 | 0.3012 |
| 5 | 1836.26 | 0.2491 |
| 6 | 1674.84 | 0.2270 |
| 7 | 1538.85 | 0.2361 |
| 8 | 1434.69 | 0.2411 |
| 9 | 1335.93 | 0.2462 |
| 10 | 1239.32 | 0.2590 |

## Archetype Summary

| Rank | Archetype | Pitches | Instances | Avg PVS | Avg xwOBA | IVB | HB | Spin | Velo | Ext | Common Pitch Types |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|
| 1 | `Tight High-Spin Breakers` | 46,040 | 355 | 52.3 | 0.238 | 0.7 | -3.2 | 2249 | 80.0 | 5.51 | Slider, Curveball, Changeup |
| 2 | `Soft-Speed Separation` | 88,513 | 534 | 48.4 | 0.244 | 13.0 | 6.3 | 2098 | 88.2 | 5.98 | Four-Seam, Sinker, Changeup |

## Highest-Performing Archetypes

- `Tight High-Spin Breakers`: average PVS 52.3, avg xwOBA 0.238, typical shape 0.7 IVB / -3.2 HB at 80.0 mph.
- `Soft-Speed Separation`: average PVS 48.4, avg xwOBA 0.244, typical shape 13.0 IVB / 6.3 HB at 88.2 mph.

## Pitchers in Highest-Performing Archetypes

| Rank | Pitcher | Team | Pitch | Pitches | PVS | xwOBA | IVB | HB | Spin | Velo | Ext | Archetype |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | Grounds, Jackson | DOW_EAS1 | Curveball | 82 | 80.0 | 0.107 | -10.5 | -12.0 | 1946 | 81.4 | 5.35 | Tight High-Spin Breakers |
| 2 | Vecerka, Boris | QUE_CAP | Slider | 83 | 80.0 | 0.123 | 2.4 | -11.8 | 2472 | 82.5 | 5.64 | Tight High-Spin Breakers |
| 3 | Carroll, Jake | JOL_SLA | Slider | 74 | 80.0 | 0.177 | -5.7 | 7.7 | 2046 | 75.4 | 6.09 | Tight High-Spin Breakers |
| 4 | Ryan, Dillon | NEW_ENG23 | Slider | 125 | 79.9 | 0.144 | -2.0 | -8.1 | 2494 | 85.4 | 5.82 | Tight High-Spin Breakers |
| 5 | Zentko, Dylan | EVA_OTT | Changeup | 67 | 78.5 | 0.155 | 7.3 | -11.4 | 1311 | 78.8 | 5.82 | Tight High-Spin Breakers |
| 6 | Morgan, Cooper | QUE_CAP | Curveball | 85 | 78.0 | 0.149 | -1.4 | 17.7 | 2689 | 75.6 | 5.28 | Tight High-Spin Breakers |
| 7 | Peyton, Blake | GAT_GRI | Changeup | 93 | 77.2 | 0.140 | 10.3 | -13.2 | 1927 | 81.0 | 6.10 | Tight High-Spin Breakers |
| 8 | Alpern, Liam | FLO_Y'A | Slider | 78 | 76.3 | 0.112 | -4.0 | 11.5 | 2219 | 76.8 | 5.55 | Tight High-Spin Breakers |
| 9 | Jones, Logan | TRI_VAL | Slider | 65 | 74.7 | 0.191 | 2.5 | 2.3 | 2341 | 83.5 | 5.69 | Tight High-Spin Breakers |
| 10 | Bauer, Patrick | QUE_CAP | Slider | 51 | 74.4 | 0.170 | 0.1 | -10.6 | 2375 | 77.6 | 6.00 | Tight High-Spin Breakers |
| 11 | Harper, Scott | NEW_YOR13 | Slider | 217 | 73.6 | 0.150 | 3.3 | -16.7 | 2669 | 79.8 | 5.58 | Tight High-Spin Breakers |
| 12 | Bargo, Casey | NEW_ENG23 | Slider | 56 | 73.5 | 0.176 | 1.5 | -5.0 | 2416 | 83.6 | 5.66 | Tight High-Spin Breakers |
| 13 | McEvoy, Aidan | FLO_Y'A | Slider | 119 | 72.5 | 0.153 | 6.4 | 10.3 | 2223 | 78.6 | 6.03 | Tight High-Spin Breakers |
| 14 | Bohnert, Matthew | WIN_CIT29 | Curveball | 98 | 71.8 | 0.143 | -16.3 | 13.3 | 2812 | 78.3 | 4.79 | Tight High-Spin Breakers |
| 15 | Leduc, Zachary | TRO_AIG | Slider | 87 | 71.7 | 0.128 | 1.5 | -4.5 | 2111 | 83.2 | 6.16 | Tight High-Spin Breakers |
| 16 | Kirby, Zach | WAS_WIL3 | Slider | 127 | 71.6 | 0.156 | 5.8 | -13.4 | 2204 | 78.0 | 5.68 | Tight High-Spin Breakers |
| 17 | Soto, Carlos | JOL_SLA | Splitter | 54 | 71.0 | 0.173 | 3.4 | 5.4 | 1003 | 80.8 | 5.17 | Tight High-Spin Breakers |
| 18 | Hickey, Matt | GAT_GRI | Slider | 89 | 70.5 | 0.206 | -1.7 | -6.5 | 2258 | 79.9 | 5.35 | Tight High-Spin Breakers |
| 19 | Donnan, Blake | FLO_Y'A | Slider | 65 | 70.0 | 0.186 | 5.0 | -7.3 | 2367 | 80.5 | 5.42 | Tight High-Spin Breakers |
| 20 | Nakata, Yuto | QUE_CAP | Slider | 107 | 68.9 | 0.161 | 3.9 | -8.2 | 2427 | 81.7 | 5.60 | Tight High-Spin Breakers |
| 21 | Parsons, Billy | SUS_COU1 | Changeup | 61 | 68.4 | 0.234 | 1.7 | 7.8 | 1428 | 80.9 | 5.49 | Tight High-Spin Breakers |
| 22 | Jones, Breyln | NEW_JER6 | Curveball | 60 | 68.4 | 0.186 | -17.0 | -9.7 | 2183 | 74.1 | 5.58 | Tight High-Spin Breakers |
| 23 | Hickey, Matt | GAT_GRI | Curveball | 65 | 68.1 | 0.179 | -4.2 | -5.9 | 2253 | 79.8 | 5.46 | Tight High-Spin Breakers |
| 24 | Smith, Ben | NEW_ENG23 | Changeup | 56 | 67.4 | 0.151 | 4.4 | -14.1 | 1591 | 82.6 | 6.12 | Tight High-Spin Breakers |
| 25 | Balzan, Jackson | SUS_COU1 | Slider | 93 | 67.3 | 0.180 | 5.8 | 0.9 | 2187 | 79.8 | 5.26 | Tight High-Spin Breakers |
| 26 | Garcia, Brett | OTT_TIT | Curveball | 121 | 67.2 | 0.174 | -17.2 | -8.3 | 2151 | 81.3 | 5.36 | Tight High-Spin Breakers |
| 27 | Hohenstein, Liam | WIN_CIT29 | Curveball | 106 | 67.1 | 0.160 | -7.3 | -11.9 | 2581 | 75.8 | 5.36 | Tight High-Spin Breakers |
| 28 | Vega, Lucas | TRO_AIG | Slider | 134 | 66.6 | 0.156 | 6.6 | -9.3 | 2697 | 79.2 | 5.94 | Tight High-Spin Breakers |
| 29 | Jones, Logan | FLO_Y'A | Slider | 56 | 66.5 | 0.190 | -1.8 | -0.6 | 2452 | 81.3 | 5.63 | Tight High-Spin Breakers |
| 30 | Gregory, Ben | GAT_GRI | Curveball | 53 | 66.5 | 0.226 | -7.0 | -5.7 | 2309 | 78.0 | 6.13 | Tight High-Spin Breakers |
| 31 | Majick, Eli | NEW_ENG23 | Cutter | 88 | 66.4 | 0.183 | 5.8 | -1.1 | 2493 | 82.8 | 5.76 | Tight High-Spin Breakers |
| 32 | Salata, Derek | SCH_BOO | Curveball | 122 | 66.3 | 0.195 | -13.0 | -13.3 | 2670 | 74.3 | 5.49 | Tight High-Spin Breakers |
| 33 | Messina, Chris | FDU_KNI | Changeup | 68 | 66.3 | 0.253 | 11.9 | -18.0 | 1836 | 79.8 | 5.18 | Tight High-Spin Breakers |
| 34 | Binns, Malik | NEW_JER6 | Curveball | 55 | 66.2 | 0.185 | -7.6 | -16.2 | 2448 | 74.8 | 5.95 | Tight High-Spin Breakers |
| 35 | Heredia-Bustos, Rolando | DOW_EAS1 | Curveball | 75 | 66.2 | 0.177 | 5.6 | -11.0 | 2220 | 73.7 | 5.05 | Tight High-Spin Breakers |
| 36 | Shears, Tanner | SCH_BOO | Splitter | 74 | 66.0 | 0.199 | -1.7 | 6.9 | 907 | 82.0 | 5.07 | Tight High-Spin Breakers |
| 37 | Earwood, Micah | SUS_COU1 | Slider | 108 | 65.8 | 0.193 | 2.3 | -2.6 | 2298 | 78.8 | 5.77 | Tight High-Spin Breakers |
| 38 | Morin, Jacob | QUE_CAP | Slider | 85 | 65.7 | 0.207 | 7.4 | -6.2 | 2495 | 77.4 | 5.50 | Tight High-Spin Breakers |
| 39 | Eisenbarger, Jack | QUE_CAP | Curveball | 93 | 64.7 | 0.212 | -3.6 | 12.1 | 2796 | 77.3 | 5.27 | Tight High-Spin Breakers |
| 40 | Perozzi, John | SUS_COU1 | Slider | 129 | 64.7 | 0.174 | 7.9 | -4.0 | 2408 | 83.1 | 5.93 | Tight High-Spin Breakers |
| 41 | Petschke, Ben | EVA_OTT | Slider | 144 | 64.5 | 0.185 | -1.7 | -13.5 | 2628 | 81.1 | 5.04 | Tight High-Spin Breakers |
| 42 | Cerda, Junior | EVA_OTT | Sweeper | 53 | 64.2 | 0.178 | -3.2 | -11.9 | 2677 | 81.2 | 5.00 | Tight High-Spin Breakers |
| 43 | Townes, Holland | SCH_BOO | Curveball | 90 | 64.1 | 0.211 | -9.4 | -13.6 | 2317 | 78.2 | 4.94 | Tight High-Spin Breakers |
| 44 | Harris, Ben | GAT_GRI | Curveball | 278 | 64.1 | 0.215 | -14.1 | -7.0 | 2163 | 77.6 | 4.96 | Tight High-Spin Breakers |
| 45 | Parsons, Billy | SUS_COU1 | Cutter | 59 | 64.0 | 0.183 | 9.4 | -2.8 | 2556 | 86.4 | 5.57 | Tight High-Spin Breakers |
| 46 | MacMillan, Blake | TRO_AIG | Slider | 106 | 63.9 | 0.210 | 6.1 | -0.1 | 1930 | 79.5 | 5.32 | Tight High-Spin Breakers |
| 47 | Vitas, Ben | JOL_SLA | Splitter | 127 | 63.7 | 0.186 | 0.7 | 6.6 | 1082 | 81.4 | 4.96 | Tight High-Spin Breakers |
| 48 | Cook, Cole | SCH_BOO | Curveball | 116 | 63.6 | 0.196 | -3.6 | 6.0 | 2490 | 77.0 | 4.92 | Tight High-Spin Breakers |
| 49 | Campbell, Tyler | MIS_MUD | Changeup | 115 | 63.6 | 0.205 | 11.6 | -7.9 | 1847 | 74.6 | 6.35 | Tight High-Spin Breakers |
| 50 | Moore, Kyle | SCH_BOO | Slider | 58 | 63.5 | 0.208 | 8.1 | -1.4 | 2191 | 83.8 | 4.78 | Tight High-Spin Breakers |
| 51 | Foster, Kobe | WAS_WIL3 | Slider | 144 | 63.4 | 0.184 | 5.1 | 5.4 | 2328 | 78.3 | 5.34 | Tight High-Spin Breakers |
| 52 | Barraza, Chris | MIS_MUD | Slider | 59 | 63.2 | 0.194 | 3.3 | -3.8 | 2317 | 84.1 | 5.32 | Tight High-Spin Breakers |
| 53 | Miner, Jace | DOW_EAS1 | Changeup | 156 | 63.2 | 0.217 | 6.2 | -12.6 | 1710 | 84.2 | 5.92 | Tight High-Spin Breakers |
| 54 | Majick, Eli | NEW_ENG23 | Curveball | 52 | 63.0 | 0.185 | -1.0 | 4.5 | 2169 | 77.0 | 5.68 | Tight High-Spin Breakers |
| 55 | Vail, Tyler | NEW_YOR13 | Slider | 200 | 62.8 | 0.235 | 1.3 | -1.9 | 2266 | 80.6 | 5.97 | Tight High-Spin Breakers |
| 56 | Morrissey, Joe | EVA_OTT | Slider | 51 | 62.8 | 0.223 | 2.6 | -13.0 | 2766 | 80.2 | 5.41 | Tight High-Spin Breakers |
| 57 | Morgan, Cooper | QUE_CAP | Changeup | 86 | 62.8 | 0.199 | 6.1 | -16.5 | 1996 | 82.2 | 5.91 | Tight High-Spin Breakers |
| 58 | Hill, Kaleb | OTT_TIT | Curveball | 247 | 62.6 | 0.206 | -4.2 | 13.2 | 2157 | 73.4 | 5.34 | Tight High-Spin Breakers |
| 59 | Good, Ty | GAT_GRI | Slider | 194 | 62.3 | 0.191 | 3.8 | -0.2 | 2042 | 79.2 | 5.83 | Tight High-Spin Breakers |
| 60 | Plumadore, Carson | WIN_CIT29 | Slider | 123 | 62.0 | 0.175 | 2.6 | -4.8 | 2435 | 76.0 | 5.51 | Tight High-Spin Breakers |
| 61 | Tokar, Heitor | OTT_TIT | Slider | 143 | 62.0 | 0.218 | 3.9 | -3.5 | 2108 | 81.9 | 5.91 | Tight High-Spin Breakers |
| 62 | Wiltse, Ryan | EVA_OTT | Curveball | 146 | 61.6 | 0.217 | -12.7 | -4.2 | 1924 | 74.2 | 5.85 | Tight High-Spin Breakers |
| 63 | Kemlage, Joe | NEW_ENG23 | Slider | 84 | 61.6 | 0.194 | -2.7 | 14.1 | 2605 | 82.2 | 5.53 | Tight High-Spin Breakers |
| 64 | Baird, Dustin | MIS_MUD | Slider | 57 | 61.5 | 0.213 | 8.2 | -9.0 | 2365 | 81.3 | 5.87 | Tight High-Spin Breakers |
| 65 | Gollert, Harley | QUE_CAP | Slider | 57 | 61.4 | 0.216 | 1.0 | 5.1 | 2222 | 79.4 | 5.09 | Tight High-Spin Breakers |
| 66 | Scafidi, Christian | LAK_ERI24 | Curveball | 59 | 61.2 | 0.193 | -6.8 | -2.9 | 2246 | 77.7 | 5.81 | Tight High-Spin Breakers |
| 67 | Hampton, Ky | OTT_TIT | Curveball | 52 | 61.1 | 0.176 | -5.0 | -13.6 | 2195 | 81.6 | 5.56 | Tight High-Spin Breakers |
| 68 | Morgan, Marcus | JOL_SLA | Cutter | 63 | 61.0 | 0.183 | 6.4 | -3.1 | 2670 | 86.9 | 5.76 | Tight High-Spin Breakers |
| 69 | Dill, Austin | TRI_VAL | Slider | 72 | 60.9 | 0.228 | 1.6 | -3.6 | 2565 | 79.3 | 4.97 | Tight High-Spin Breakers |
| 70 | Cameron, Zach | WIN_CIT29 | Slider | 145 | 60.8 | 0.198 | 7.3 | -1.5 | 2342 | 81.7 | 5.42 | Tight High-Spin Breakers |
| 71 | Widener, Jacob | SUS_COU1 | Slider | 94 | 60.7 | 0.226 | 3.4 | 16.4 | 2855 | 80.4 | 6.11 | Tight High-Spin Breakers |
| 72 | Earwood, Micah | SUS_COU1 | Curveball | 218 | 60.5 | 0.235 | -3.1 | -4.7 | 2342 | 75.0 | 5.59 | Tight High-Spin Breakers |
| 73 | Sechrist, Zander | WAS_WIL3 | Slider | 81 | 60.5 | 0.213 | 3.1 | 7.5 | 1877 | 69.5 | 5.14 | Tight High-Spin Breakers |
| 74 | O'Hanlon, Michael | WAS_WIL3 | Slider | 66 | 60.5 | 0.252 | 3.1 | -2.3 | 2484 | 83.4 | 5.39 | Tight High-Spin Breakers |
| 75 | Morgan, Cooper | QUE_CAP | Slider | 69 | 60.5 | 0.218 | 3.2 | 10.5 | 2474 | 79.0 | 5.48 | Tight High-Spin Breakers |
| 76 | Ginn, Landon | WAS_WIL3 | Slider | 108 | 60.3 | 0.196 | 1.3 | -3.4 | 2877 | 85.7 | 5.33 | Tight High-Spin Breakers |
| 77 | Harajli, Ahmad | FLO_Y'A | Slider | 76 | 60.1 | 0.191 | -2.5 | -2.9 | 2056 | 80.5 | 5.99 | Tight High-Spin Breakers |
| 78 | Villers, Ian | QUE_CAP | Slider | 66 | 59.5 | 0.240 | -0.3 | -5.1 | 2117 | 82.3 | 5.94 | Tight High-Spin Breakers |
| 79 | Calderon, Jean | LAK_ERI24 | Slider | 73 | 59.4 | 0.197 | 1.3 | -9.7 | 2593 | 86.4 | 6.05 | Tight High-Spin Breakers |
| 80 | Hocom, Quinn | TRI_VAL | Changeup | 101 | 59.3 | 0.220 | 6.2 | 17.0 | 1965 | 78.3 | 5.62 | Tight High-Spin Breakers |
| 81 | Leak, Anthony | NEW_YOR13 | Slider | 274 | 59.1 | 0.182 | 5.1 | -5.8 | 2295 | 83.2 | 5.83 | Tight High-Spin Breakers |
| 82 | Smith, Jackson | MIS_MUD | Slider | 129 | 59.0 | 0.216 | 1.7 | -9.0 | 2642 | 78.5 | 4.87 | Tight High-Spin Breakers |
| 83 | Scott, Brandon | LAK_ERI24 | Slider | 148 | 58.9 | 0.194 | -0.3 | 6.8 | 2401 | 77.9 | 5.41 | Tight High-Spin Breakers |
| 84 | Ronne, Andrew | GAT_GRI | Slider | 142 | 58.8 | 0.205 | 0.0 | -14.6 | 2593 | 81.4 | 5.94 | Tight High-Spin Breakers |
| 85 | Langhorne, Miles | SUS_COU1 | Slider | 61 | 58.8 | 0.223 | 0.0 | -3.1 | 2487 | 86.8 | 5.90 | Tight High-Spin Breakers |
| 86 | Long, Maddox | WAS_WIL3 | Slider | 226 | 58.7 | 0.196 | 2.8 | -8.6 | 2598 | 82.8 | 5.52 | Tight High-Spin Breakers |
| 87 | Lefebvre, Charles | TRO_AIG | Curveball | 99 | 58.6 | 0.246 | -9.3 | -8.7 | 2467 | 77.6 | 6.11 | Tight High-Spin Breakers |
| 88 | Brito, Richard | NEW_ENG23 | Slider | 73 | 58.5 | 0.196 | 3.6 | -6.0 | 2287 | 81.7 | 6.09 | Tight High-Spin Breakers |
| 89 | Shinn, Nathan | LAK_ERI24 | Slider | 138 | 58.5 | 0.217 | 0.3 | 0.8 | 2179 | 82.1 | 5.24 | Tight High-Spin Breakers |
| 90 | Cohn, Cooper | NIU_HUS | Slider | 63 | 58.3 | 0.188 | -1.2 | -13.7 | 2534 | 78.9 | 5.40 | Tight High-Spin Breakers |
| 91 | Odonnell, Brendan | NEW_ENG23 | Slider | 235 | 58.3 | 0.214 | -1.3 | 12.1 | 2645 | 84.1 | 6.12 | Tight High-Spin Breakers |
| 92 | Rohde, Isaac | NEW_YOR13 | Changeup | 801 | 58.2 | 0.217 | 4.0 | -20.4 | 1977 | 76.3 | 6.19 | Tight High-Spin Breakers |
| 93 | Marklund, Brandon | OTT_TIT | Slider | 124 | 58.2 | 0.244 | 6.4 | -14.2 | 2707 | 79.6 | 4.87 | Tight High-Spin Breakers |
| 94 | Williams, Brian | MIS_MUD | Splitter | 101 | 58.2 | 0.185 | 2.5 | 5.0 | 1728 | 78.6 | 6.05 | Tight High-Spin Breakers |
| 95 | Vail, Tyler | NEW_YOR13 | Curveball | 186 | 58.1 | 0.220 | -2.9 | -5.5 | 2225 | 74.8 | 5.72 | Tight High-Spin Breakers |
| 96 | Allemann, Braeden | QUE_CAP | Slider | 79 | 58.0 | 0.226 | 3.4 | -3.2 | 2259 | 83.3 | 6.20 | Tight High-Spin Breakers |
| 97 | Gollert, Harley | TRO_AIG | Curveball | 86 | 58.0 | 0.224 | -5.7 | 5.8 | 2235 | 77.1 | 4.85 | Tight High-Spin Breakers |
| 98 | Boies, Emiles | QUE_CAP | Curveball | 91 | 58.0 | 0.187 | -4.0 | -5.9 | 2121 | 76.6 | 5.65 | Tight High-Spin Breakers |
| 99 | Andueza, Axel | DOW_EAS1 | Changeup | 104 | 57.9 | 0.226 | 5.7 | 11.2 | 2087 | 82.4 | 5.22 | Tight High-Spin Breakers |
| 100 | Garcia, Andrew | EVA_OTT | Slider | 227 | 57.8 | 0.195 | 2.2 | -7.2 | 2338 | 82.2 | 5.38 | Tight High-Spin Breakers |
| 101 | Foster, Kobe | WAS_WIL3 | Changeup | 190 | 57.6 | 0.227 | 15.8 | -14.0 | 1869 | 79.4 | 5.78 | Tight High-Spin Breakers |
| 102 | Pierson, Kenny | LAK_ERI24 | Slider | 108 | 57.5 | 0.235 | -1.3 | 7.7 | 2088 | 72.1 | 4.65 | Tight High-Spin Breakers |
| 103 | Vailes, Gage | GAT_GRI | Slider | 316 | 57.4 | 0.211 | 5.8 | -11.6 | 2553 | 81.7 | 4.59 | Tight High-Spin Breakers |
| 104 | Valdez, Alex | EVA_OTT | Cutter | 92 | 57.3 | 0.234 | 4.4 | -2.0 | 2076 | 86.4 | 5.37 | Tight High-Spin Breakers |
| 105 | Dima, Josh | GAT_GRI | Slider | 119 | 57.2 | 0.203 | 2.4 | 2.1 | 1923 | 81.9 | 6.00 | Tight High-Spin Breakers |
| 106 | Garcia, Hector | WAS_WIL3 | Slider | 56 | 57.1 | 0.229 | 2.0 | -7.1 | 2355 | 77.3 | 5.72 | Tight High-Spin Breakers |
| 107 | Anibal, Trevor | NEW_ENG23 | Curveball | 112 | 57.1 | 0.232 | -15.3 | -9.2 | 2493 | 76.0 | 5.45 | Tight High-Spin Breakers |
| 108 | Thornton, Tyler | NEW_ENG23 | Splitter | 119 | 57.0 | 0.242 | 4.9 | 11.5 | 952 | 77.6 | 4.85 | Tight High-Spin Breakers |
| 109 | Bice, Emmett | NEW_YOR13 | Slider | 273 | 57.0 | 0.230 | 2.1 | -2.6 | 2380 | 82.8 | 5.66 | Tight High-Spin Breakers |
| 110 | Balzan, Jackson | SUS_COU1 | Curveball | 83 | 56.9 | 0.235 | -5.1 | 5.1 | 2104 | 76.1 | 5.12 | Tight High-Spin Breakers |
| 111 | Petery, Dylan | WIN_CIT29 | Curveball | 70 | 56.8 | 0.225 | -7.0 | -14.6 | 2554 | 74.6 | 5.46 | Tight High-Spin Breakers |
| 112 | Maryniak, Connor | NEW_JER6 | Curveball | 202 | 56.8 | 0.229 | -9.6 | -4.5 | 2514 | 81.3 | 4.77 | Tight High-Spin Breakers |
| 113 | Eckaus, David | EVA_OTT | Slider | 187 | 56.8 | 0.225 | 1.9 | 4.9 | 2598 | 82.4 | 5.56 | Tight High-Spin Breakers |
| 114 | Saturria, Michael | NEW_ENG23 | Slider | 254 | 56.6 | 0.208 | 3.9 | -7.3 | 2705 | 80.7 | 5.90 | Tight High-Spin Breakers |
| 115 | House, Tristan | MIS_MUD | Slider | 74 | 56.6 | 0.212 | -1.6 | -1.6 | 2334 | 78.3 | 5.82 | Tight High-Spin Breakers |
| 116 | Morgan, Marcus | JOL_SLA | Slider | 66 | 56.5 | 0.213 | 7.0 | -9.2 | 2844 | 84.9 | 5.71 | Tight High-Spin Breakers |
| 117 | Hagan, Jack | DOW_EAS1 | Slider | 222 | 56.5 | 0.231 | 3.8 | -3.6 | 2437 | 84.4 | 5.69 | Tight High-Spin Breakers |
| 118 | Petschke, Ben | EVA_OTT | Curveball | 169 | 56.5 | 0.232 | -9.7 | -15.8 | 2767 | 77.2 | 4.96 | Tight High-Spin Breakers |
| 119 | Simpson, Garret | EVA_OTT | Curveball | 120 | 56.4 | 0.231 | -11.8 | -13.0 | 2637 | 76.4 | 5.13 | Tight High-Spin Breakers |
| 120 | Bauer, Patrick | QUE_CAP | Curveball | 96 | 56.4 | 0.238 | -11.8 | -14.3 | 2295 | 70.3 | 6.07 | Tight High-Spin Breakers |
| 121 | Allemann, Braeden | QUE_CAP | Curveball | 254 | 56.4 | 0.229 | -7.0 | -15.7 | 2192 | 76.9 | 6.14 | Tight High-Spin Breakers |
| 122 | Kirby, Zach | WAS_WIL3 | Curveball | 105 | 56.4 | 0.232 | -18.3 | -10.7 | 2261 | 70.8 | 5.41 | Tight High-Spin Breakers |
| 123 | Harris, Everette | TRI_VAL | Slider | 53 | 56.3 | 0.214 | 1.2 | -8.7 | 2862 | 80.5 | 6.15 | Tight High-Spin Breakers |
| 124 | Langrell, Connor | MIS_MUD | Curveball | 117 | 56.3 | 0.228 | -15.7 | -11.6 | 2720 | 77.5 | 6.01 | Tight High-Spin Breakers |
| 125 | Fauci, Sonny | NEW_JER6 | Slider | 137 | 56.0 | 0.263 | -1.6 | -6.1 | 2333 | 83.8 | 5.94 | Tight High-Spin Breakers |
| 126 | Whitesell, Max | FLO_Y'A | Slider | 162 | 55.8 | 0.215 | 6.2 | -4.6 | 2078 | 80.3 | 6.30 | Tight High-Spin Breakers |
| 127 | Helt, Robert | LAK_ERI24 | Slider | 233 | 55.8 | 0.225 | -1.2 | -5.1 | 2405 | 81.1 | 5.76 | Tight High-Spin Breakers |
| 128 | Boies, Emiles | QUE_CAP | Slider | 82 | 55.8 | 0.231 | 4.7 | -0.5 | 2122 | 80.3 | 5.96 | Tight High-Spin Breakers |
| 129 | Lefebvre, Charles | TRO_AIG | Slider | 107 | 55.7 | 0.194 | 2.3 | -1.6 | 2171 | 81.9 | 6.43 | Tight High-Spin Breakers |
| 130 | Long, Jalon | NEW_YOR13 | Curveball | 53 | 55.7 | 0.215 | -7.8 | -3.3 | 2331 | 75.6 | 5.54 | Tight High-Spin Breakers |
| 131 | Fuenmayor, Liu | OTT_TIT | Sinker | 81 | 55.7 | 0.212 | 9.8 | -20.6 | 2241 | 90.8 | 4.57 | Tight High-Spin Breakers |
| 132 | Heredia-Bustos, Rolando | DOW_EAS1 | Slider | 449 | 55.4 | 0.211 | 6.7 | -3.9 | 2321 | 78.5 | 5.26 | Tight High-Spin Breakers |
| 133 | Hocom, Quinn | TRI_VAL | Curveball | 106 | 55.3 | 0.244 | -13.4 | -11.6 | 2373 | 76.8 | 5.48 | Tight High-Spin Breakers |
| 134 | Walsh, John | MIS_MUD | Slider | 91 | 55.2 | 0.223 | -0.5 | 10.6 | 2223 | 73.4 | 4.99 | Tight High-Spin Breakers |
| 135 | Moore, Kyle | SCH_BOO | Cutter | 147 | 55.1 | 0.237 | 9.6 | 1.7 | 2141 | 84.5 | 4.68 | Tight High-Spin Breakers |
| 136 | Campbell, AJ | WIN_CIT29 | Slider | 401 | 55.0 | 0.219 | 5.1 | -9.4 | 2565 | 80.0 | 4.88 | Tight High-Spin Breakers |
| 137 | Eisenbarger, Jack | QUE_CAP | Changeup | 166 | 54.9 | 0.198 | 14.6 | -14.6 | 2317 | 78.8 | 6.02 | Tight High-Spin Breakers |
| 138 | Rodriguez, Leonardo | NEW_JER6 | Slider | 68 | 54.9 | 0.218 | 2.5 | -3.2 | 2587 | 83.7 | 5.94 | Tight High-Spin Breakers |
| 139 | De Los Santos, Enmanuel | NEW_ENG23 | Curveball | 105 | 54.9 | 0.245 | -5.7 | -11.1 | 2219 | 71.3 | 6.47 | Tight High-Spin Breakers |
| 140 | Gordillo, Lucas | TRI_VAL | Slider | 58 | 54.9 | 0.253 | 3.0 | -5.9 | 2016 | 80.8 | 5.58 | Tight High-Spin Breakers |
| 141 | Floyd, Conner | QUE_CAP | Curveball | 62 | 54.8 | 0.233 | -3.2 | -17.0 | 2117 | 77.6 | 5.04 | Tight High-Spin Breakers |
| 142 | Campbell, AJ | WIN_CIT29 | Cutter | 91 | 54.7 | 0.274 | 8.0 | 0.2 | 2508 | 84.1 | 5.15 | Tight High-Spin Breakers |
| 143 | Simone, Andrew | TRO_AIG | Slider | 112 | 54.7 | 0.209 | 3.4 | -3.8 | 2164 | 84.2 | 5.73 | Tight High-Spin Breakers |
| 144 | Cook, Cole | SCH_BOO | Slider | 213 | 54.6 | 0.242 | 3.3 | 5.1 | 2494 | 79.7 | 5.08 | Tight High-Spin Breakers |
| 145 | Zentko, Dylan | EVA_OTT | Slider | 67 | 54.6 | 0.224 | 3.7 | 1.1 | 1951 | 77.4 | 5.63 | Tight High-Spin Breakers |
| 146 | Biddinger, Tyler | WIN_CIT29 | Slider | 91 | 54.4 | 0.199 | -0.4 | -12.2 | 2663 | 79.5 | 4.87 | Tight High-Spin Breakers |
| 147 | Maher, Adam | TRI_VAL | Slider | 118 | 54.2 | 0.238 | 5.0 | 1.3 | 1915 | 79.3 | 5.73 | Tight High-Spin Breakers |
| 148 | Nova, Fraynel | LAK_ERI24 | Slider | 327 | 54.2 | 0.235 | -0.6 | -7.0 | 2290 | 80.7 | 5.60 | Tight High-Spin Breakers |
| 149 | Nabholz, Nate | TRI_VAL | Slider | 98 | 54.1 | 0.218 | 6.4 | -1.6 | 1992 | 83.4 | 5.68 | Tight High-Spin Breakers |
| 150 | Williams, Pierce | NEW_ENG23 | Changeup | 505 | 54.0 | 0.227 | 10.4 | -13.9 | 1787 | 79.6 | 5.95 | Tight High-Spin Breakers |
| 151 | Smith, Jackson | MIS_MUD | Cutter | 99 | 54.0 | 0.216 | 3.3 | 4.9 | 2425 | 81.7 | 5.08 | Tight High-Spin Breakers |
| 152 | Woolfolk, Dallas | MIS_MUD | Slider | 80 | 54.0 | 0.260 | 0.4 | -1.3 | 2291 | 82.3 | 5.23 | Tight High-Spin Breakers |
| 153 | Noriega, Branden | LAK_ERI24 | Curveball | 128 | 53.9 | 0.256 | -9.4 | 7.5 | 2847 | 79.3 | 5.27 | Tight High-Spin Breakers |
| 154 | Helt, Robert | LAK_ERI24 | Curveball | 165 | 53.8 | 0.253 | -5.6 | -5.9 | 2380 | 79.0 | 5.79 | Tight High-Spin Breakers |
| 155 | Sesar, Jorden | SUS_COU1 | Curveball | 120 | 53.8 | 0.238 | -12.0 | -11.1 | 2419 | 74.9 | 6.03 | Tight High-Spin Breakers |
| 156 | Kostura, Brit | WAS_WIL3 | Curveball | 64 | 53.7 | 0.236 | -2.4 | 4.2 | 2166 | 74.2 | 5.40 | Tight High-Spin Breakers |
| 157 | Gollert, Harley | TRO_AIG | Changeup | 169 | 53.7 | 0.256 | 9.8 | -13.6 | 1544 | 79.6 | 5.27 | Tight High-Spin Breakers |
| 158 | DeCastro, Justin | LON_ISL22 | Changeup | 122 | 53.7 | 0.235 | 9.6 | 18.6 | 1979 | 79.4 | 5.06 | Tight High-Spin Breakers |
| 159 | Long, Jalon | NEW_YOR13 | Slider | 163 | 53.4 | 0.239 | 5.0 | -1.9 | 2164 | 84.1 | 5.81 | Tight High-Spin Breakers |
| 160 | Miner, Jace | DOW_EAS1 | Curveball | 109 | 53.4 | 0.251 | 2.5 | 11.2 | 1843 | 75.8 | 5.42 | Tight High-Spin Breakers |
| 161 | Johnston, Spencer | DOW_EAS1 | Slider | 190 | 53.3 | 0.213 | 6.7 | 0.9 | 2083 | 78.4 | 5.96 | Tight High-Spin Breakers |
| 162 | Oe, Ryoya | OTT_TIT | Curveball | 57 | 53.2 | 0.210 | -4.6 | 5.0 | 2303 | 73.3 | 4.90 | Tight High-Spin Breakers |
| 163 | Zeplin, Blane | JOL_SLA | Slider | 108 | 52.9 | 0.212 | -0.7 | -6.9 | 2273 | 77.7 | 5.32 | Tight High-Spin Breakers |
| 164 | Gamelin, Shaun | JOL_SLA | Slider | 78 | 52.8 | 0.241 | 2.9 | -1.1 | 2294 | 81.9 | 4.83 | Tight High-Spin Breakers |
| 165 | Kines, Gunnar | JOL_SLA | Changeup | 328 | 52.8 | 0.238 | 12.1 | -12.5 | 1907 | 75.4 | 5.99 | Tight High-Spin Breakers |
| 166 | Milburn, Isaac | FLO_Y'A | Slider | 187 | 52.7 | 0.217 | -1.7 | 15.7 | 2652 | 78.7 | 4.83 | Tight High-Spin Breakers |
| 167 | Thompson, Ross | SCH_BOO | Slider | 223 | 52.6 | 0.229 | 3.5 | -2.3 | 2054 | 79.8 | 5.25 | Tight High-Spin Breakers |
| 168 | Sittinger, Brandyn | LAK_ERI24 | Slider | 144 | 52.6 | 0.233 | 3.7 | -0.8 | 2458 | 87.6 | 5.72 | Tight High-Spin Breakers |
| 169 | Campbell, AJ | WIN_CIT29 | Curveball | 62 | 52.5 | 0.208 | -0.3 | -15.8 | 2589 | 75.6 | 4.81 | Tight High-Spin Breakers |
| 170 | Estrella, Noah | TRI_VAL | Slider | 162 | 52.5 | 0.215 | -2.6 | 0.6 | 2584 | 85.3 | 5.63 | Tight High-Spin Breakers |
| 171 | Balzan, Jackson | SUS_COU1 | Changeup | 341 | 52.4 | 0.240 | 9.5 | -13.8 | 1872 | 79.9 | 5.37 | Tight High-Spin Breakers |
| 172 | Peters, Garrett | NEW_YOR13 | Curveball | 194 | 52.3 | 0.232 | 0.9 | -0.5 | 2034 | 76.0 | 5.81 | Tight High-Spin Breakers |
| 173 | Grills, Evan | OTT_TIT | Curveball | 68 | 52.2 | 0.247 | -13.7 | 10.4 | 2441 | 72.6 | 5.18 | Tight High-Spin Breakers |
| 174 | Turner, Eric | JOL_SLA | Changeup | 182 | 52.1 | 0.239 | 4.7 | 15.4 | 1666 | 79.7 | 5.11 | Tight High-Spin Breakers |
| 175 | Correa, Nelvin | QUE_CAP | Slider | 136 | 52.1 | 0.218 | 4.4 | -7.1 | 2407 | 83.6 | 5.50 | Tight High-Spin Breakers |
| 176 | Henderson, Drew | DOW_EAS1 | Curveball | 297 | 52.0 | 0.227 | -8.1 | -5.0 | 2294 | 76.7 | 5.09 | Tight High-Spin Breakers |
| 177 | Sanchez, Edwin | LAK_ERI24 | Curveball | 111 | 52.0 | 0.213 | -5.0 | 5.8 | 2465 | 75.8 | 5.31 | Tight High-Spin Breakers |
| 178 | Sparks, Alec | GAT_GRI | Slider | 181 | 52.0 | 0.225 | 0.6 | -7.3 | 2595 | 80.1 | 5.46 | Tight High-Spin Breakers |
| 179 | Masick, Jason | NEW_YOR13 | Slider | 54 | 51.9 | 0.223 | 3.6 | -4.6 | 2284 | 85.4 | 5.69 | Tight High-Spin Breakers |
| 180 | Toribio, Noe | TRO_AIG | Slider | 188 | 51.9 | 0.215 | 2.8 | 1.1 | 2213 | 82.4 | 5.78 | Tight High-Spin Breakers |
| 181 | Puccetti, Dominic | OTT_TIT | Curveball | 172 | 51.9 | 0.246 | -13.5 | 9.8 | 2684 | 73.7 | 5.27 | Tight High-Spin Breakers |
| 182 | Pierson, Kenny | LAK_ERI24 | Changeup | 279 | 51.8 | 0.240 | -1.4 | -16.0 | 1756 | 76.9 | 4.94 | Tight High-Spin Breakers |
| 183 | Foster, Kobe | WAS_WIL3 | Curveball | 186 | 51.7 | 0.248 | -8.3 | 15.1 | 2248 | 67.6 | 5.34 | Tight High-Spin Breakers |
| 184 | Hill, Kaleb | OTT_TIT | Slider | 159 | 51.7 | 0.243 | 0.6 | 9.3 | 2254 | 78.8 | 5.25 | Tight High-Spin Breakers |
| 185 | Thebiay, Nolan | EVA_OTT | Slider | 58 | 51.6 | 0.260 | -0.6 | -1.1 | 1836 | 79.1 | 6.18 | Tight High-Spin Breakers |
| 186 | Sakurai, Masatoshi | QUE_CAP | Slider | 158 | 51.5 | 0.245 | -0.3 | 4.3 | 2214 | 79.1 | 5.80 | Tight High-Spin Breakers |
| 187 | Leach, Landon | TRO_AIG | Slider | 65 | 51.5 | 0.239 | 2.5 | -7.0 | 2104 | 82.0 | 5.34 | Tight High-Spin Breakers |
| 188 | McCartney, Seth | MIS_MUD | Slider | 57 | 51.5 | 0.195 | 4.2 | -3.0 | 2474 | 81.9 | 5.45 | Tight High-Spin Breakers |
| 189 | Sechrist, Zander | WAS_WIL3 | Curveball | 151 | 51.4 | 0.228 | 2.0 | 7.4 | 1865 | 67.9 | 5.33 | Tight High-Spin Breakers |
| 190 | Joven, Art | MIS_MUD | Sinker | 305 | 51.3 | 0.242 | 7.2 | -15.6 | 1793 | 83.3 | 5.15 | Tight High-Spin Breakers |
| 191 | Cerda, Junior | EVA_OTT | Slider | 122 | 51.3 | 0.217 | -2.0 | -7.3 | 2607 | 82.3 | 4.93 | Tight High-Spin Breakers |
| 192 | Majick, Eli | NEW_ENG23 | Slider | 230 | 51.2 | 0.246 | 3.7 | 8.3 | 2543 | 79.5 | 5.61 | Tight High-Spin Breakers |
| 193 | Figueredo, Kevin | WIN_CIT29 | Changeup | 111 | 51.2 | 0.252 | 6.0 | -12.7 | 1696 | 84.0 | 5.34 | Tight High-Spin Breakers |
| 194 | Moore, Kyle | SCH_BOO | Curveball | 125 | 51.1 | 0.252 | -8.5 | -7.8 | 2531 | 76.9 | 4.07 | Tight High-Spin Breakers |
| 195 | Blair, Davis | DOW_EAS1 | Slider | 99 | 51.0 | 0.259 | 3.6 | -5.9 | 2146 | 81.9 | 5.11 | Tight High-Spin Breakers |
| 196 | Williams, Brian | MIS_MUD | Slider | 243 | 51.0 | 0.245 | 4.3 | -0.8 | 2165 | 81.7 | 5.94 | Tight High-Spin Breakers |
| 197 | Glickstein, Aaron | SCH_BOO | Slider | 55 | 50.9 | 0.244 | 7.5 | -0.5 | 2240 | 84.9 | 5.58 | Tight High-Spin Breakers |
| 198 | Pierson, Kenny | LAK_ERI24 | Sinker | 239 | 50.8 | 0.242 | 0.3 | -17.7 | 1765 | 81.0 | 4.81 | Tight High-Spin Breakers |
| 199 | Cooper, Garrett | NEW_YOR13 | Curveball | 173 | 50.7 | 0.227 | -5.5 | -6.6 | 2188 | 76.2 | 5.57 | Tight High-Spin Breakers |
| 200 | Campbell, AJ | WIN_CIT29 | Changeup | 73 | 50.6 | 0.239 | 6.9 | 9.4 | 2070 | 80.3 | 5.36 | Tight High-Spin Breakers |
| 201 | Martzolf, Max | JOL_SLA | Sinker | 259 | 50.5 | 0.235 | 10.4 | -19.7 | 2131 | 84.8 | 5.44 | Tight High-Spin Breakers |
| 202 | Scafidi, Christian | LAK_ERI24 | Slider | 185 | 50.4 | 0.244 | 4.2 | -2.0 | 2387 | 84.3 | 5.64 | Tight High-Spin Breakers |
| 203 | Linderman, Greyson | JOL_SLA | Slider | 66 | 50.3 | 0.270 | -4.0 | -13.7 | 2207 | 81.2 | 4.96 | Tight High-Spin Breakers |
| 204 | Pardinho, Eric | OTT_TIT | Slider | 171 | 50.3 | 0.249 | 4.9 | 1.6 | 2344 | 86.2 | 5.65 | Tight High-Spin Breakers |
| 205 | Carroll, Jake | JOL_SLA | Curveball | 53 | 50.3 | 0.260 | -7.1 | 8.2 | 2029 | 75.5 | 6.16 | Tight High-Spin Breakers |
| 206 | Gilleran, Jimmy | NEW_ENG23 | Slider | 141 | 50.3 | 0.247 | 3.8 | -3.4 | 2244 | 80.8 | 5.36 | Tight High-Spin Breakers |
| 207 | Wehrle, Tyler | WIN_CIT29 | Slider | 146 | 50.2 | 0.230 | 2.4 | -10.0 | 2521 | 80.7 | 5.33 | Tight High-Spin Breakers |
| 208 | Escobar, Anthony | TRO_AIG | Curveball | 64 | 50.2 | 0.227 | -2.3 | -6.3 | 2220 | 77.1 | 6.04 | Tight High-Spin Breakers |
| 209 | Serrano, Elio | NEW_JER6 | Curveball | 79 | 50.2 | 0.276 | -10.3 | -13.9 | 2293 | 75.6 | 5.10 | Tight High-Spin Breakers |
| 210 | Castro, Alexander | TRO_AIG | Slider | 131 | 50.1 | 0.252 | 0.5 | -4.8 | 2515 | 83.5 | 4.84 | Tight High-Spin Breakers |
| 211 | Bargo, Casey | FLO_Y'A | Slider | 101 | 50.0 | 0.221 | 0.1 | -3.9 | 2278 | 81.4 | 5.35 | Tight High-Spin Breakers |
| 212 | Belton, Hunter | MIS_MUD | Slider | 99 | 49.7 | 0.244 | 6.5 | -2.6 | 2108 | 78.5 | 5.82 | Tight High-Spin Breakers |
| 213 | Valdez, Alex | EVA_OTT | Slider | 139 | 49.6 | 0.215 | 3.7 | -2.5 | 2161 | 85.9 | 5.31 | Tight High-Spin Breakers |
| 214 | Campbell, Tyler | MIS_MUD | Slider | 232 | 49.6 | 0.265 | 7.8 | 4.1 | 2204 | 74.2 | 5.73 | Tight High-Spin Breakers |
| 215 | Smith, Ben | NEW_ENG23 | Slider | 112 | 49.4 | 0.280 | 0.1 | 13.6 | 2314 | 78.7 | 5.47 | Tight High-Spin Breakers |
| 216 | Milburn, Isaac | FLO_Y'A | Curveball | 167 | 49.2 | 0.301 | -9.3 | 13.4 | 2580 | 76.7 | 4.95 | Tight High-Spin Breakers |
| 217 | Sanchez, Edwin | LAK_ERI24 | Slider | 93 | 49.2 | 0.248 | -0.7 | 4.3 | 2413 | 77.1 | 5.19 | Tight High-Spin Breakers |
| 218 | Villalobos, Jonaiker | FLO_Y'A | Changeup | 200 | 49.1 | 0.246 | 7.8 | -13.1 | 1580 | 80.0 | 5.83 | Tight High-Spin Breakers |
| 219 | Barreto, Brayhans | TRI_VAL | Slider | 106 | 49.0 | 0.259 | 3.9 | 0.5 | 1935 | 81.1 | 6.24 | Tight High-Spin Breakers |
| 220 | Misla, Luis | TRI_VAL | Slider | 75 | 48.9 | 0.260 | 1.3 | 10.6 | 2729 | 78.8 | 5.27 | Tight High-Spin Breakers |
| 221 | Armstrong, Andrew | NEW_YOR13 | Slider | 128 | 48.7 | 0.282 | 2.7 | 7.1 | 2356 | 80.1 | 5.90 | Tight High-Spin Breakers |
| 222 | Gamelin, Shaun | JOL_SLA | Cutter | 138 | 48.5 | 0.244 | 5.6 | -0.4 | 2316 | 84.0 | 5.06 | Tight High-Spin Breakers |
| 223 | Kostura, Brit | WAS_WIL3 | Sinker | 136 | 48.5 | 0.238 | 13.2 | -16.7 | 2075 | 84.9 | 5.55 | Tight High-Spin Breakers |
| 224 | Cooper, Garrett | NEW_YOR13 | Slider | 106 | 48.4 | 0.228 | 2.0 | -3.1 | 2095 | 80.7 | 5.75 | Tight High-Spin Breakers |
| 225 | Vilchez, Michael | OTT_TIT | Slider | 108 | 48.2 | 0.251 | 1.4 | -4.6 | 2301 | 82.7 | 5.73 | Tight High-Spin Breakers |
| 226 | Kostura, Brit | WAS_WIL3 | Changeup | 86 | 48.2 | 0.242 | 9.8 | -16.0 | 1880 | 80.6 | 5.79 | Tight High-Spin Breakers |
| 227 | Rodriguez, Luis | TRO_AIG | Slider | 58 | 48.2 | 0.239 | 2.2 | -1.6 | 2525 | 87.7 | 5.92 | Tight High-Spin Breakers |
| 228 | Joven, Art | MIS_MUD | Slider | 305 | 48.2 | 0.253 | 2.1 | 0.0 | 2241 | 77.5 | 5.18 | Tight High-Spin Breakers |
| 229 | Kaminer, Brandon | DOW_EAS1 | Slider | 133 | 48.1 | 0.236 | 6.1 | 2.3 | 2474 | 83.8 | 5.28 | Tight High-Spin Breakers |
| 230 | Parks, Pavin | LAK_ERI24 | Cutter | 135 | 48.1 | 0.253 | 7.0 | -3.6 | 2428 | 84.7 | 5.77 | Tight High-Spin Breakers |
| 231 | Galva, Claudio | GAT_GRI | Changeup | 101 | 48.0 | 0.251 | 4.5 | -13.5 | 1469 | 84.4 | 4.84 | Tight High-Spin Breakers |
| 232 | Hicks, Jackson | DOW_EAS1 | Slider | 116 | 48.0 | 0.269 | 2.4 | -1.0 | 2195 | 80.0 | 5.23 | Tight High-Spin Breakers |
| 233 | Turner, Eric | JOL_SLA | Slider | 221 | 48.0 | 0.248 | 1.4 | -7.7 | 2360 | 78.3 | 4.97 | Tight High-Spin Breakers |
| 234 | Peters, Garrett | NEW_YOR13 | Changeup | 523 | 48.0 | 0.251 | 12.2 | -14.8 | 1867 | 80.3 | 5.99 | Tight High-Spin Breakers |
| 235 | Kaftan, Eddie | FLO_Y'A | Slider | 62 | 47.9 | 0.234 | 1.1 | -6.3 | 2437 | 77.1 | 4.72 | Tight High-Spin Breakers |
| 236 | Gorgen, Grady | NEW_YOR13 | Changeup | 73 | 47.8 | 0.268 | 6.6 | -12.0 | 1877 | 83.9 | 6.08 | Tight High-Spin Breakers |
| 237 | Smith, Ethan | WIN_CIT29 | Slider | 58 | 47.8 | 0.281 | -0.2 | -6.4 | 2423 | 80.6 | 5.91 | Tight High-Spin Breakers |
| 238 | Almonte, Lisandro | NEW_JER6 | Slider | 57 | 47.6 | 0.241 | 3.6 | -0.9 | 2194 | 85.7 | 5.45 | Tight High-Spin Breakers |
| 239 | Cook, Cole | SCH_BOO | Sinker | 131 | 47.6 | 0.232 | 11.9 | -11.7 | 2255 | 84.7 | 5.28 | Tight High-Spin Breakers |
| 240 | Majick, Eli | NEW_ENG23 | Changeup | 150 | 47.5 | 0.255 | 3.2 | -13.4 | 1824 | 82.5 | 6.07 | Tight High-Spin Breakers |
| 241 | Perdomo, Rafael | QUE_CAP | Slider | 87 | 47.4 | 0.260 | 3.1 | 0.7 | 2183 | 82.9 | 5.79 | Tight High-Spin Breakers |
| 242 | Baker, Luke | EVA_OTT | Curveball | 59 | 47.4 | 0.244 | -7.4 | 9.7 | 2694 | 75.5 | 5.51 | Tight High-Spin Breakers |
| 243 | Matos, Dwayne | OTT_TIT | Slider | 143 | 47.3 | 0.260 | 4.4 | -0.8 | 2026 | 81.5 | 6.17 | Tight High-Spin Breakers |
| 244 | Scott, Brandon | LAK_ERI24 | Changeup | 242 | 47.3 | 0.278 | 2.2 | -12.4 | 1515 | 81.2 | 5.76 | Tight High-Spin Breakers |
| 245 | Snyder, Jack | SCH_BOO | Slider | 68 | 47.0 | 0.233 | 5.6 | -4.9 | 2462 | 84.1 | 5.19 | Tight High-Spin Breakers |
| 246 | Drakeford, Dosie | NEW_JER6 | Slider | 82 | 46.9 | 0.294 | 1.9 | -6.7 | 2396 | 79.7 | 5.44 | Tight High-Spin Breakers |
| 247 | Perez, Kelvin | WAS_WIL3 | Slider | 125 | 46.9 | 0.244 | 4.1 | -4.5 | 2241 | 81.5 | 5.76 | Tight High-Spin Breakers |
| 248 | Foy, Corbin | LAK_ERI24 | Slider | 78 | 46.8 | 0.269 | -1.1 | -7.6 | 2653 | 82.4 | 5.56 | Tight High-Spin Breakers |
| 249 | Bihm, Gage | MIS_MUD | Slider | 72 | 46.7 | 0.267 | -2.5 | 10.4 | 2278 | 80.4 | 4.98 | Tight High-Spin Breakers |
| 250 | McKillican, Adam | QUE_CAP | Slider | 50 | 46.7 | 0.241 | 3.3 | -3.5 | 2162 | 80.1 | 6.44 | Tight High-Spin Breakers |
| 251 | Catrambone, Ben | JOL_SLA | Cutter | 66 | 46.5 | 0.285 | 6.2 | -0.1 | 2360 | 83.3 | 5.22 | Tight High-Spin Breakers |
| 252 | Smith, Jackson | MIS_MUD | Sinker | 493 | 46.5 | 0.268 | 0.9 | 21.7 | 2406 | 85.3 | 5.16 | Tight High-Spin Breakers |
| 253 | Parra, Andres | LAK_ERI24 | Slider | 161 | 46.5 | 0.266 | 2.8 | 2.0 | 2288 | 79.6 | 5.71 | Tight High-Spin Breakers |
| 254 | Reeves, Cobe | NEW_YOR13 | Curveball | 52 | 46.4 | 0.276 | -8.0 | 7.0 | 2370 | 80.1 | 5.53 | Tight High-Spin Breakers |
| 255 | Hopewell, Chase | FLO_Y'A | Slider | 147 | 46.4 | 0.273 | 0.2 | -2.1 | 1915 | 81.0 | 6.14 | Tight High-Spin Breakers |
| 256 | Joven, Art | MIS_MUD | Changeup | 454 | 46.2 | 0.258 | 5.3 | -15.5 | 1803 | 81.7 | 5.27 | Tight High-Spin Breakers |
| 257 | Misla, Luis | TRI_VAL | Curveball | 160 | 46.1 | 0.258 | -5.5 | 9.3 | 2791 | 77.0 | 5.12 | Tight High-Spin Breakers |
| 258 | Majick, Eli | NEW_ENG23 | Sinker | 300 | 46.0 | 0.257 | 6.9 | -16.6 | 2014 | 87.3 | 5.87 | Tight High-Spin Breakers |
| 259 | Debban, Caleb | NEW_JER6 | Curveball | 206 | 45.8 | 0.276 | -7.2 | 18.6 | 2810 | 76.9 | 5.91 | Tight High-Spin Breakers |
| 260 | Delaney, Carter | WIN_CIT29 | Slider | 78 | 45.8 | 0.282 | -0.3 | -7.4 | 2286 | 80.0 | 5.46 | Tight High-Spin Breakers |
| 261 | Petery, Dylan | WIN_CIT29 | Slider | 59 | 45.7 | 0.222 | -0.6 | -12.2 | 2611 | 78.0 | 5.74 | Tight High-Spin Breakers |
| 262 | Ginn, Landon | WAS_WIL3 | Cutter | 112 | 45.7 | 0.248 | 3.2 | -2.0 | 2840 | 86.3 | 5.37 | Tight High-Spin Breakers |
| 263 | Andueza, Axel | DOW_EAS1 | Curveball | 168 | 45.6 | 0.242 | -3.5 | -3.1 | 2202 | 79.4 | 5.09 | Tight High-Spin Breakers |
| 264 | Cook, Cole | SCH_BOO | Four-Seam | 302 | 45.4 | 0.261 | 14.2 | -9.4 | 2294 | 84.8 | 5.28 | Tight High-Spin Breakers |
| 265 | Willeman, Landon | EVA_OTT | Slider | 101 | 45.4 | 0.234 | 0.4 | -5.0 | 2251 | 80.6 | 5.50 | Tight High-Spin Breakers |
| 266 | Salata, Derek | SCH_BOO | Slider | 179 | 45.3 | 0.261 | 3.2 | -9.3 | 2553 | 81.4 | 5.57 | Tight High-Spin Breakers |
| 267 | Bell, Brendan | NEW_ENG23 | Slider | 61 | 45.2 | 0.303 | -1.6 | -9.2 | 2407 | 82.4 | 5.52 | Tight High-Spin Breakers |
| 268 | Cook, Cole | SCH_BOO | Changeup | 260 | 45.2 | 0.261 | 9.2 | -9.5 | 1841 | 80.8 | 5.43 | Tight High-Spin Breakers |
| 269 | Brouwer, Adam | LAK_ERI24 | Curveball | 78 | 45.2 | 0.264 | -8.7 | -6.2 | 2348 | 78.0 | 5.36 | Tight High-Spin Breakers |
| 270 | Foltz Jr., Michael | WAS_WIL3 | Curveball | 78 | 44.8 | 0.281 | -5.9 | 4.5 | 2307 | 79.2 | 5.35 | Tight High-Spin Breakers |
| 271 | Martzolf, Max | OTT_TIT | Changeup | 194 | 44.6 | 0.246 | 9.4 | -19.5 | 2044 | 83.2 | 5.42 | Tight High-Spin Breakers |
| 272 | Barker, Alex | NEW_YOR13 | Slider | 183 | 44.5 | 0.250 | 3.6 | 4.0 | 2243 | 81.8 | 5.89 | Tight High-Spin Breakers |
| 273 | Peyton, Blake | GAT_GRI | Curveball | 90 | 44.4 | 0.225 | -5.8 | 8.6 | 2673 | 77.8 | 5.24 | Tight High-Spin Breakers |
| 274 | Huter, Blayne | SUS_COU1 | Curveball | 103 | 44.3 | 0.271 | -5.1 | -14.2 | 2137 | 73.7 | 6.01 | Tight High-Spin Breakers |
| 275 | Hill, Kaleb | OTT_TIT | Changeup | 248 | 44.3 | 0.261 | 9.3 | -15.3 | 1814 | 82.4 | 5.65 | Tight High-Spin Breakers |
| 276 | Cook, Cole | SCH_BOO | Cutter | 117 | 44.1 | 0.220 | 9.3 | -3.6 | 2408 | 82.5 | 5.24 | Tight High-Spin Breakers |
| 277 | Willeman, Landon | EVA_OTT | Curveball | 121 | 44.0 | 0.286 | -8.2 | -9.9 | 2099 | 77.6 | 5.35 | Tight High-Spin Breakers |
| 278 | Smith, Jackson | MIS_MUD | Changeup | 119 | 44.0 | 0.281 | -1.1 | 18.1 | 2243 | 81.7 | 5.12 | Tight High-Spin Breakers |
| 279 | Bradford, Ethan | NEW_YOR13 | Slider | 160 | 44.0 | 0.284 | -1.2 | 5.9 | 2446 | 82.3 | 5.50 | Tight High-Spin Breakers |
| 280 | Figueredo, Kevin | WIN_CIT29 | Curveball | 78 | 44.0 | 0.278 | -3.5 | 4.9 | 2324 | 75.8 | 5.00 | Tight High-Spin Breakers |
| 281 | Simpson, Garret | EVA_OTT | Slider | 52 | 44.0 | 0.289 | -0.2 | -4.5 | 2432 | 81.9 | 5.10 | Tight High-Spin Breakers |
| 282 | Sechrist, Zander | WAS_WIL3 | Four-Seam | 135 | 43.9 | 0.251 | 13.9 | -16.1 | 1905 | 80.2 | 5.65 | Tight High-Spin Breakers |
| 283 | Sakurai, Masatoshi | QUE_CAP | Curveball | 186 | 43.9 | 0.274 | -4.4 | 5.3 | 2451 | 78.4 | 5.61 | Tight High-Spin Breakers |
| 284 | Moore, Kyle | SCH_BOO | Changeup | 97 | 43.8 | 0.251 | 9.9 | 16.4 | 2033 | 82.6 | 4.68 | Tight High-Spin Breakers |
| 285 | Forsyth, Braden | MIS_MUD | Slider | 162 | 43.8 | 0.275 | 3.6 | -6.9 | 2362 | 80.7 | 6.09 | Tight High-Spin Breakers |
| 286 | Lovin, Xander | GAT_GRI | Slider | 157 | 43.7 | 0.286 | 3.1 | -3.6 | 2438 | 85.0 | 4.91 | Tight High-Spin Breakers |
| 287 | Delaney, Carter | WIN_CIT29 | Curveball | 76 | 43.7 | 0.287 | -5.5 | -7.7 | 2280 | 79.9 | 5.54 | Tight High-Spin Breakers |
| 288 | Simpson, Garret | EVA_OTT | Cutter | 143 | 43.6 | 0.280 | 5.4 | 0.4 | 2406 | 85.9 | 5.38 | Tight High-Spin Breakers |
| 289 | Gollert, Harley | QUE_CAP | Changeup | 52 | 43.6 | 0.253 | 10.2 | -8.4 | 1676 | 81.0 | 5.46 | Tight High-Spin Breakers |
| 290 | Gregory, Ben | GAT_GRI | Slider | 96 | 43.6 | 0.304 | 1.6 | -4.3 | 2336 | 79.8 | 6.02 | Tight High-Spin Breakers |
| 291 | Encarnacion, J.D. | EVA_OTT | Slider | 143 | 43.4 | 0.252 | 2.5 | -5.4 | 2352 | 81.2 | 5.43 | Tight High-Spin Breakers |
| 292 | Pindel, Buddie | SCH_BOO | Slider | 199 | 43.4 | 0.255 | 1.4 | -7.2 | 2472 | 81.5 | 5.37 | Tight High-Spin Breakers |
| 293 | Okumura, Shuto | WAS_WIL3 | Four-Seam | 60 | 43.4 | 0.274 | 6.1 | 7.6 | 1757 | 75.3 | 5.56 | Tight High-Spin Breakers |
| 294 | Smith, Donny | JOL_SLA | Slider | 66 | 43.3 | 0.244 | -2.4 | -5.4 | 2476 | 78.5 | 5.16 | Tight High-Spin Breakers |
| 295 | Godwin, Connor | NEW_YOR13 | Slider | 93 | 43.2 | 0.261 | 0.0 | -10.2 | 2535 | 82.4 | 6.11 | Tight High-Spin Breakers |
| 296 | Simpson, Garret | EVA_OTT | Changeup | 88 | 43.1 | 0.292 | 4.6 | 10.7 | 1711 | 83.8 | 5.17 | Tight High-Spin Breakers |
| 297 | Reeves, Cobe | NEW_YOR13 | Slider | 62 | 43.1 | 0.261 | 0.2 | 3.0 | 2196 | 83.1 | 5.82 | Tight High-Spin Breakers |
| 298 | Burcham, Jacob | GAT_GRI | Slider | 117 | 43.1 | 0.252 | 0.2 | -9.9 | 2395 | 80.8 | 5.84 | Tight High-Spin Breakers |
| 299 | Martzolf, Max | OTT_TIT | Four-Seam | 71 | 43.1 | 0.246 | 10.5 | -20.4 | 2140 | 84.5 | 5.83 | Tight High-Spin Breakers |
| 300 | Martzolf, Max | OTT_TIT | Curveball | 71 | 43.0 | 0.290 | -4.2 | 11.1 | 2155 | 73.9 | 5.43 | Tight High-Spin Breakers |
| 301 | Anderson, Colt | WAS_WIL3 | Curveball | 67 | 42.6 | 0.270 | -11.1 | 9.9 | 2026 | 73.5 | 6.09 | Tight High-Spin Breakers |
| 302 | Westcott, Zac | FLO_Y'A | Changeup | 196 | 42.2 | 0.262 | 6.5 | 16.7 | 1915 | 76.5 | 5.73 | Tight High-Spin Breakers |
| 303 | Gilleran, Jimmy | NEW_ENG23 | Splitter | 51 | 42.1 | 0.303 | -0.1 | 7.8 | 1500 | 79.0 | 5.13 | Tight High-Spin Breakers |
| 304 | Sanchez, Edwin | LAK_ERI24 | Changeup | 123 | 42.1 | 0.270 | 6.4 | -15.8 | 1953 | 80.1 | 5.81 | Tight High-Spin Breakers |
| 305 | Maher, Adam | TRI_VAL | Curveball | 54 | 42.0 | 0.261 | 0.8 | 2.1 | 2034 | 77.4 | 5.56 | Tight High-Spin Breakers |
| 306 | Escobar, Anthony | TRO_AIG | Slider | 280 | 42.0 | 0.275 | 3.4 | -5.1 | 2167 | 81.8 | 6.09 | Tight High-Spin Breakers |
| 307 | Noble, Nick | FDU_KNI | Changeup | 71 | 41.9 | 0.302 | 0.2 | 17.6 | 1612 | 77.3 | 5.00 | Tight High-Spin Breakers |
| 308 | Gartland, Chad | TRI_VAL | Slider | 108 | 41.8 | 0.242 | 5.3 | -1.0 | 2224 | 82.6 | 6.14 | Tight High-Spin Breakers |
| 309 | Serrano, Elio | NEW_JER6 | Slider | 128 | 41.8 | 0.258 | 5.6 | -2.1 | 2246 | 82.7 | 5.30 | Tight High-Spin Breakers |
| 310 | Villalobos, Jonaiker | FLO_Y'A | Curveball | 134 | 41.7 | 0.259 | -5.0 | 5.5 | 2265 | 74.8 | 5.33 | Tight High-Spin Breakers |
| 311 | Tiburcio, David | DOW_EAS1 | Slider | 99 | 41.6 | 0.277 | 6.0 | 0.9 | 2342 | 86.3 | 5.40 | Tight High-Spin Breakers |
| 312 | Hampton, Ky | OTT_TIT | Slider | 105 | 41.6 | 0.261 | 1.4 | -4.5 | 2286 | 83.6 | 5.82 | Tight High-Spin Breakers |
| 313 | Kostura, Brit | WAS_WIL3 | Slider | 60 | 41.5 | 0.272 | -0.6 | 5.1 | 2162 | 74.8 | 5.09 | Tight High-Spin Breakers |
| 314 | Dima, Josh | GAT_GRI | Curveball | 54 | 41.4 | 0.277 | -3.6 | 2.1 | 1961 | 80.3 | 5.99 | Tight High-Spin Breakers |
| 315 | Williams, Pierce | NEW_ENG23 | Curveball | 159 | 41.3 | 0.267 | -5.7 | 6.4 | 2173 | 75.3 | 5.78 | Tight High-Spin Breakers |
| 316 | Good, Ty | GAT_GRI | Curveball | 167 | 41.0 | 0.272 | -7.8 | -4.6 | 2132 | 74.9 | 5.66 | Tight High-Spin Breakers |
| 317 | Parsons, Billy | SUS_COU1 | Slider | 242 | 41.0 | 0.246 | 5.9 | -6.3 | 2486 | 82.9 | 5.45 | Tight High-Spin Breakers |
| 318 | Bice, Emmett | NEW_YOR13 | Curveball | 170 | 40.8 | 0.295 | -10.3 | -13.3 | 2986 | 79.1 | 5.51 | Tight High-Spin Breakers |
| 319 | Gollert, Harley | TRO_AIG | Slider | 71 | 40.7 | 0.281 | -1.9 | 7.7 | 2221 | 78.2 | 4.91 | Tight High-Spin Breakers |
| 320 | Shinn, Nathan | LAK_ERI24 | Curveball | 88 | 40.3 | 0.278 | -5.9 | 0.6 | 2113 | 79.6 | 5.29 | Tight High-Spin Breakers |
| 321 | Sabatine, Gino | TRI_VAL | Slider | 138 | 40.2 | 0.291 | 4.2 | -3.6 | 2322 | 79.9 | 4.89 | Tight High-Spin Breakers |
| 322 | Vitas, Ben | JOL_SLA | Slider | 154 | 40.2 | 0.261 | 1.7 | -3.9 | 2116 | 81.4 | 4.95 | Tight High-Spin Breakers |
| 323 | Sanchez, Dikember | LAK_ERI24 | Slider | 111 | 40.2 | 0.274 | 2.1 | -3.7 | 2555 | 85.9 | 5.32 | Tight High-Spin Breakers |
| 324 | Andueza, Axel | DOW_EAS1 | Slider | 116 | 40.0 | 0.281 | -0.6 | -1.5 | 2073 | 80.7 | 5.22 | Tight High-Spin Breakers |
| 325 | Sechrist, Zander | WAS_WIL3 | Sinker | 98 | 39.9 | 0.269 | 13.2 | -17.8 | 1893 | 80.1 | 5.60 | Tight High-Spin Breakers |
| 326 | Thornton, Tyler | NEW_ENG23 | Slider | 138 | 39.8 | 0.292 | 1.9 | -0.2 | 1925 | 80.0 | 4.93 | Tight High-Spin Breakers |
| 327 | Barker, Alex | NEW_YOR13 | Curveball | 95 | 39.8 | 0.267 | -5.5 | 9.9 | 2258 | 76.4 | 5.75 | Tight High-Spin Breakers |
| 328 | Kassebaum, Torin | LON_ISL22 | Curveball | 55 | 39.6 | 0.307 | 1.1 | 10.2 | 2155 | 71.6 | 5.31 | Tight High-Spin Breakers |
| 329 | Lawson, Nathan | FLO_Y'A | Cutter | 98 | 39.5 | 0.254 | 7.6 | -1.2 | 2306 | 83.7 | 5.75 | Tight High-Spin Breakers |
| 330 | Nova, Fraynel | LAK_ERI24 | Curveball | 57 | 39.3 | 0.290 | -4.4 | -6.3 | 2305 | 80.2 | 5.60 | Tight High-Spin Breakers |
| 331 | Sechrist, Zander | WAS_WIL3 | Changeup | 244 | 39.1 | 0.281 | 8.5 | -14.8 | 1694 | 77.0 | 5.75 | Tight High-Spin Breakers |
| 332 | Gorgen, Grady | NEW_YOR13 | Curveball | 86 | 38.8 | 0.275 | -7.3 | 7.0 | 2137 | 79.9 | 5.69 | Tight High-Spin Breakers |
| 333 | Campbell, Tyler | MIS_MUD | Sinker | 125 | 38.5 | 0.270 | 7.3 | -9.8 | 2284 | 84.6 | 6.15 | Tight High-Spin Breakers |
| 334 | Quigley, Michael | NEW_ENG23 | Curveball | 79 | 38.4 | 0.294 | -12.3 | -12.7 | 2567 | 78.8 | 5.42 | Tight High-Spin Breakers |
| 335 | Soto, Carlos | JOL_SLA | Slider | 102 | 37.8 | 0.302 | -1.6 | -8.8 | 2509 | 78.2 | 5.08 | Tight High-Spin Breakers |
| 336 | Brodsky, Jack | WAS_WIL3 | Curveball | 100 | 37.7 | 0.317 | -8.6 | -11.9 | 2662 | 76.6 | 5.45 | Tight High-Spin Breakers |
| 337 | Eldred, Zach | NEW_ENG23 | Curveball | 81 | 37.5 | 0.315 | -9.8 | -12.4 | 2489 | 77.6 | 5.88 | Tight High-Spin Breakers |
| 338 | Fauci, Sonny | NEW_JER6 | Curveball | 114 | 37.4 | 0.341 | -15.1 | -6.6 | 2318 | 78.5 | 5.87 | Tight High-Spin Breakers |
| 339 | Chabot, Henry | LAK_ERI24 | Slider | 69 | 37.3 | 0.334 | 4.0 | -1.5 | 2413 | 84.3 | 5.11 | Tight High-Spin Breakers |
| 340 | Galva, Claudio | GAT_GRI | Slider | 200 | 36.7 | 0.282 | 2.9 | -0.5 | 2251 | 83.7 | 4.79 | Tight High-Spin Breakers |
| 341 | Eldred, Zach | NEW_ENG23 | Slider | 170 | 34.7 | 0.297 | 1.9 | -7.3 | 2413 | 82.3 | 5.86 | Tight High-Spin Breakers |
| 342 | McEvoy, Aidan | FLO_Y'A | Changeup | 58 | 34.3 | 0.275 | 3.1 | -14.0 | 1735 | 82.9 | 6.26 | Tight High-Spin Breakers |
| 343 | Voytko, Fawster | TRO_AIG | Curveball | 75 | 33.6 | 0.319 | -7.1 | -11.8 | 2335 | 74.7 | 6.06 | Tight High-Spin Breakers |
| 344 | Galva, Claudio | GAT_GRI | Sinker | 182 | 33.0 | 0.291 | 10.4 | -12.3 | 1989 | 89.1 | 4.94 | Tight High-Spin Breakers |
| 345 | Gorgen, Grady | NEW_YOR13 | Slider | 137 | 32.0 | 0.314 | 1.5 | 1.0 | 2153 | 83.1 | 5.98 | Tight High-Spin Breakers |
| 346 | Miranda, Kevin | OTT_TIT | Slider | 78 | 31.3 | 0.337 | 3.7 | -0.3 | 2222 | 81.1 | 5.60 | Tight High-Spin Breakers |
| 347 | Catrambone, Ben | JOL_SLA | Slider | 116 | 28.6 | 0.357 | 2.3 | -1.5 | 2271 | 82.7 | 4.85 | Tight High-Spin Breakers |
| 348 | Lawson, Nathan | FLO_Y'A | Curveball | 68 | 26.8 | 0.388 | -16.1 | -12.1 | 2374 | 74.1 | 5.56 | Tight High-Spin Breakers |
| 349 | Townes, Holland | SCH_BOO | Cutter | 69 | 26.7 | 0.305 | 3.3 | -1.9 | 2148 | 83.9 | 4.96 | Tight High-Spin Breakers |
| 350 | Cameron, Wyatt | SCH_BOO | Curveball | 109 | 26.6 | 0.357 | -13.5 | -9.7 | 2296 | 81.1 | 5.24 | Tight High-Spin Breakers |
| 351 | Voytko, Fawster | TRO_AIG | Slider | 60 | 25.3 | 0.323 | 0.9 | -11.4 | 2323 | 78.6 | 6.24 | Tight High-Spin Breakers |
| 352 | Johnston, Spencer | DOW_EAS1 | Curveball | 66 | 24.9 | 0.322 | -4.7 | -6.0 | 2133 | 74.4 | 5.68 | Tight High-Spin Breakers |
| 353 | Plumadore, Carson | WIN_CIT29 | Curveball | 77 | 21.6 | 0.365 | 1.3 | -6.9 | 2483 | 75.4 | 5.57 | Tight High-Spin Breakers |
| 354 | Lovin, Xander | GAT_GRI | Curveball | 65 | 20.8 | 0.353 | -9.3 | -12.3 | 2634 | 76.9 | 4.64 | Tight High-Spin Breakers |
| 355 | Westcott, Zac | FLO_Y'A | Curveball | 163 | 20.3 | 0.376 | -15.2 | -9.2 | 1872 | 67.1 | 5.48 | Tight High-Spin Breakers |
| 356 | Serrano, Elio | NEW_JER6 | Changeup | 63 | 75.9 | 0.148 | 11.1 | 11.7 | 1829 | 82.1 | 5.92 | Soft-Speed Separation |
| 357 | Grounds, Jackson | DOW_EAS1 | Four-Seam | 107 | 74.3 | 0.158 | 17.0 | 14.2 | 2163 | 92.5 | 5.59 | Soft-Speed Separation |
| 358 | Davis, Tyler | WIN_CIT29 | Four-Seam | 76 | 74.3 | 0.111 | 21.2 | 5.6 | 2171 | 89.3 | 5.86 | Soft-Speed Separation |
| 359 | Debban, Caleb | NEW_JER6 | Four-Seam | 57 | 73.7 | 0.173 | 13.1 | -4.6 | 2325 | 87.2 | 6.58 | Soft-Speed Separation |
| 360 | Garcia, Hector | WAS_WIL3 | Splitter | 62 | 73.6 | 0.184 | 11.7 | 7.6 | 1216 | 78.2 | 5.92 | Soft-Speed Separation |
| 361 | Lawson, Nathan | FLO_Y'A | Changeup | 68 | 72.4 | 0.194 | 8.2 | 9.6 | 1396 | 79.6 | 5.77 | Soft-Speed Separation |
| 362 | Cameron, Zach | WIN_CIT29 | Four-Seam | 120 | 71.9 | 0.195 | 15.8 | 10.2 | 2170 | 88.1 | 5.54 | Soft-Speed Separation |
| 363 | Webster, Evan | FLO_Y'A | Cutter | 138 | 70.4 | 0.169 | 5.6 | -0.4 | 2039 | 84.4 | 6.94 | Soft-Speed Separation |
| 364 | Riedel, Caleb | SCH_BOO | Sinker | 81 | 70.0 | 0.140 | 16.1 | -15.9 | 2309 | 88.8 | 5.98 | Soft-Speed Separation |
| 365 | Harris, Everette | TRI_VAL | Changeup | 96 | 69.6 | 0.168 | 2.1 | 16.6 | 2144 | 82.6 | 6.54 | Soft-Speed Separation |
| 366 | Still, Stephen | TRI_VAL | Sinker | 61 | 69.4 | 0.211 | 14.1 | -18.1 | 2325 | 90.6 | 5.39 | Soft-Speed Separation |
| 367 | Escobar, Anthony | TRO_AIG | Changeup | 162 | 69.2 | 0.165 | 10.1 | 11.5 | 1611 | 79.0 | 6.23 | Soft-Speed Separation |
| 368 | Duncan, Tanner | DOW_EAS1 | Slider | 64 | 68.9 | 0.174 | 6.7 | 0.1 | 2214 | 86.9 | 5.83 | Soft-Speed Separation |
| 369 | Campbell, Tyler | MIS_MUD | Four-Seam | 60 | 68.7 | 0.179 | 8.4 | -5.4 | 2307 | 85.2 | 6.31 | Soft-Speed Separation |
| 370 | Rodriguez, Joe Joe | NEW_JER6 | Changeup | 144 | 68.2 | 0.167 | 8.6 | 14.8 | 1823 | 81.9 | 5.34 | Soft-Speed Separation |
| 371 | Wiltse, Ryan | EVA_OTT | Changeup | 165 | 68.1 | 0.195 | 13.9 | 10.3 | 1831 | 78.3 | 6.32 | Soft-Speed Separation |
| 372 | Correa, Nelvin | QUE_CAP | Cutter | 118 | 67.9 | 0.172 | 11.8 | -0.5 | 2239 | 87.6 | 6.00 | Soft-Speed Separation |
| 373 | Coles, Chad | WAS_WIL3 | Splitter | 63 | 67.5 | 0.164 | 2.3 | 7.1 | 1031 | 86.2 | 5.59 | Soft-Speed Separation |
| 374 | Correa, Nelvin | QUE_CAP | Four-Seam | 96 | 67.3 | 0.191 | 15.3 | 6.9 | 2121 | 89.4 | 5.98 | Soft-Speed Separation |
| 375 | Grounds, Jackson | TRO_AIG | Four-Seam | 79 | 66.9 | 0.149 | 14.3 | 11.4 | 2227 | 92.2 | 5.85 | Soft-Speed Separation |
| 376 | Glickstein, Aaron | SCH_BOO | Sinker | 105 | 66.2 | 0.184 | 9.4 | 13.8 | 2164 | 88.3 | 6.09 | Soft-Speed Separation |
| 377 | Leak, Anthony | NEW_YOR13 | Changeup | 77 | 66.0 | 0.192 | 6.1 | 11.3 | 1728 | 83.1 | 6.53 | Soft-Speed Separation |
| 378 | Odonnell, Brendan | NEW_ENG23 | Sinker | 109 | 65.9 | 0.203 | 8.0 | -11.8 | 2337 | 90.1 | 6.94 | Soft-Speed Separation |
| 379 | Foy, Corbin | LAK_ERI24 | Four-Seam | 96 | 65.7 | 0.176 | 16.5 | 10.4 | 2337 | 91.3 | 6.15 | Soft-Speed Separation |
| 380 | Earwood, Micah | SUS_COU1 | Four-Seam | 96 | 65.5 | 0.228 | 18.7 | 2.6 | 2066 | 80.7 | 5.65 | Soft-Speed Separation |
| 381 | Villers, Ian | QUE_CAP | Splitter | 64 | 65.1 | 0.218 | 7.5 | 11.5 | 1086 | 83.1 | 5.98 | Soft-Speed Separation |
| 382 | Pindel, Buddie | SCH_BOO | Splitter | 90 | 65.1 | 0.217 | 5.0 | 7.1 | 1100 | 80.3 | 5.75 | Soft-Speed Separation |
| 383 | Drakeford, Dosie | NEW_JER6 | Changeup | 84 | 64.7 | 0.158 | 9.9 | 14.8 | 1850 | 81.0 | 6.11 | Soft-Speed Separation |
| 384 | Colon, Jeffrey | TRO_AIG | Sinker | 56 | 64.7 | 0.169 | 13.9 | 17.7 | 2262 | 90.2 | 5.61 | Soft-Speed Separation |
| 385 | Gregory, Ben | GAT_GRI | Four-Seam | 93 | 64.0 | 0.186 | 15.7 | 13.6 | 2230 | 88.9 | 6.45 | Soft-Speed Separation |
| 386 | Earwood, Micah | SUS_COU1 | Changeup | 211 | 63.7 | 0.185 | 8.7 | 5.3 | 1835 | 79.0 | 6.20 | Soft-Speed Separation |
| 387 | Widener, Jacob | SUS_COU1 | Sinker | 139 | 63.6 | 0.188 | 9.0 | -11.4 | 2364 | 88.9 | 6.94 | Soft-Speed Separation |
| 388 | Tokar, Heitor | OTT_TIT | Changeup | 74 | 63.3 | 0.206 | 9.6 | 13.1 | 1407 | 82.1 | 6.07 | Soft-Speed Separation |
| 389 | Sesar, Jorden | SUS_COU1 | Changeup | 80 | 63.2 | 0.167 | 12.1 | 11.5 | 1980 | 83.0 | 6.47 | Soft-Speed Separation |
| 390 | Garbrick, Alex | LAK_ERI24 | Four-Seam | 82 | 63.2 | 0.223 | 15.2 | 10.7 | 2266 | 91.4 | 5.61 | Soft-Speed Separation |
| 391 | Mannering, Shawn | DOW_EAS1 | Sinker | 59 | 63.1 | 0.256 | 13.5 | 18.6 | 2231 | 89.1 | 5.82 | Soft-Speed Separation |
| 392 | Shears, Tanner | SCH_BOO | Four-Seam | 240 | 62.8 | 0.189 | 16.8 | 12.4 | 2039 | 92.3 | 5.18 | Soft-Speed Separation |
| 393 | Garcia, Andrew | EVA_OTT | Sinker | 52 | 62.7 | 0.237 | 10.5 | 14.2 | 2058 | 91.0 | 5.92 | Soft-Speed Separation |
| 394 | Lockhart, Gauge | LAK_ERI24 | Cutter | 139 | 62.7 | 0.204 | 5.6 | -0.8 | 2085 | 86.5 | 6.23 | Soft-Speed Separation |
| 395 | Hensey, Rob | SUS_COU1 | Four-Seam | 220 | 62.1 | 0.186 | 16.5 | -13.9 | 2201 | 92.1 | 6.20 | Soft-Speed Separation |
| 396 | Maietta, Dante | WIN_CIT29 | Changeup | 283 | 62.1 | 0.191 | 15.2 | 13.8 | 1861 | 77.7 | 6.31 | Soft-Speed Separation |
| 397 | Brown, Ethan | WAS_WIL3 | Four-Seam | 67 | 62.0 | 0.217 | 12.7 | -10.8 | 2077 | 90.4 | 6.09 | Soft-Speed Separation |
| 398 | Morgan, Cooper | QUE_CAP | Four-Seam | 85 | 61.6 | 0.198 | 13.3 | -8.4 | 2202 | 87.5 | 6.13 | Soft-Speed Separation |
| 399 | Cartwright, Eli | GAT_GRI | Four-Seam | 207 | 61.4 | 0.193 | 18.4 | -8.6 | 2100 | 90.3 | 6.40 | Soft-Speed Separation |
| 400 | Willeman, Landon | EVA_OTT | Changeup | 179 | 61.0 | 0.202 | 6.2 | 14.5 | 1696 | 84.0 | 6.23 | Soft-Speed Separation |
| 401 | Lyons, Kendall | QUE_CAP | Four-Seam | 71 | 60.9 | 0.181 | 18.4 | 11.2 | 2286 | 90.8 | 6.65 | Soft-Speed Separation |
| 402 | Barreto, Brayhans | TRI_VAL | Changeup | 122 | 60.8 | 0.224 | 10.9 | -13.0 | 1789 | 81.1 | 6.15 | Soft-Speed Separation |
| 403 | Mercado, Nelson | OTT_TIT | Four-Seam | 81 | 60.6 | 0.169 | 19.2 | 12.6 | 2126 | 87.8 | 5.67 | Soft-Speed Separation |
| 404 | Pardinho, Eric | OTT_TIT | Changeup | 141 | 60.5 | 0.219 | 4.4 | 14.7 | 1596 | 83.8 | 5.40 | Soft-Speed Separation |
| 405 | Plumadore, Carson | WIN_CIT29 | Changeup | 272 | 60.5 | 0.196 | 8.5 | 18.7 | 2255 | 83.2 | 5.93 | Soft-Speed Separation |
| 406 | Hensey, Rob | SUS_COU1 | Changeup | 277 | 60.4 | 0.212 | 6.4 | -15.8 | 1698 | 84.1 | 6.13 | Soft-Speed Separation |
| 407 | Petschke, Ben | EVA_OTT | Sinker | 54 | 60.4 | 0.205 | 6.5 | 13.1 | 2110 | 90.0 | 5.27 | Soft-Speed Separation |
| 408 | Anderson, Colt | WAS_WIL3 | Four-Seam | 266 | 60.3 | 0.216 | 11.8 | -7.0 | 2047 | 88.8 | 6.71 | Soft-Speed Separation |
| 409 | Harley, Tristan | SUS_COU1 | Four-Seam | 68 | 60.0 | 0.224 | 13.7 | 16.4 | 2050 | 92.0 | 5.81 | Soft-Speed Separation |
| 410 | Castro, Alexander | TRO_AIG | Changeup | 71 | 59.8 | 0.209 | 5.7 | 10.5 | 1315 | 83.4 | 6.11 | Soft-Speed Separation |
| 411 | Wehrle, Tyler | WIN_CIT29 | Four-Seam | 236 | 59.6 | 0.188 | 16.5 | 14.0 | 2322 | 91.3 | 5.66 | Soft-Speed Separation |
| 412 | Martinez, Mason | TRI_VAL | Slider | 132 | 59.5 | 0.212 | 6.4 | 0.1 | 2349 | 83.3 | 6.40 | Soft-Speed Separation |
| 413 | Sabatine, Gino | TRI_VAL | Sinker | 54 | 59.5 | 0.193 | 9.5 | 14.0 | 1890 | 88.2 | 5.03 | Soft-Speed Separation |
| 414 | Harley, Tristan | SUS_COU1 | Sinker | 97 | 59.4 | 0.187 | 11.7 | 14.7 | 1999 | 92.1 | 5.83 | Soft-Speed Separation |
| 415 | Kaminer, Brandon | DOW_EAS1 | Four-Seam | 185 | 59.4 | 0.226 | 18.1 | -4.8 | 2365 | 89.4 | 5.38 | Soft-Speed Separation |
| 416 | Dima, Josh | GAT_GRI | Four-Seam | 238 | 59.2 | 0.204 | 18.1 | -10.8 | 2054 | 90.3 | 6.22 | Soft-Speed Separation |
| 417 | Webster, Evan | FLO_Y'A | Slider | 111 | 59.2 | 0.200 | 3.0 | 0.9 | 1957 | 81.4 | 6.82 | Soft-Speed Separation |
| 418 | Bell, Brendan | NEW_ENG23 | Cutter | 93 | 59.1 | 0.226 | 9.2 | -0.4 | 2398 | 92.1 | 5.80 | Soft-Speed Separation |
| 419 | VanMarter, Luke | LEM_COL | Changeup | 53 | 59.1 | 0.255 | 12.9 | 11.7 | 1756 | 77.6 | 6.55 | Soft-Speed Separation |
| 420 | Zaffiro, Cole | SCH_BOO | Four-Seam | 335 | 59.0 | 0.198 | 17.9 | 8.4 | 2169 | 90.8 | 6.05 | Soft-Speed Separation |
| 421 | Langhorne, Miles | SUS_COU1 | Four-Seam | 70 | 58.9 | 0.245 | 14.2 | 3.8 | 2304 | 93.9 | 6.50 | Soft-Speed Separation |
| 422 | Hensey, Rob | SUS_COU1 | Slider | 108 | 58.9 | 0.210 | 5.0 | -0.5 | 2206 | 82.8 | 6.21 | Soft-Speed Separation |
| 423 | MacMillan, Blake | TRO_AIG | Four-Seam | 148 | 58.8 | 0.200 | 21.9 | -5.8 | 2200 | 88.3 | 5.56 | Soft-Speed Separation |
| 424 | Brothers, Kellen | SUS_COU1 | Changeup | 177 | 58.7 | 0.218 | 10.5 | 12.0 | 1497 | 79.9 | 6.06 | Soft-Speed Separation |
| 425 | Foster, Kobe | WAS_WIL3 | Four-Seam | 442 | 58.6 | 0.194 | 20.6 | -9.8 | 2207 | 86.7 | 5.72 | Soft-Speed Separation |
| 426 | Lovell, Justin | WIN_CIT29 | Sinker | 136 | 58.5 | 0.180 | 12.3 | -14.8 | 2229 | 93.2 | 6.26 | Soft-Speed Separation |
| 427 | Plumadore, Carson | WIN_CIT29 | Sinker | 138 | 58.4 | 0.187 | 13.7 | 18.6 | 2378 | 87.1 | 5.81 | Soft-Speed Separation |
| 428 | Culley, Wesley | LAK_ERI24 | Four-Seam | 61 | 58.4 | 0.189 | 14.1 | -12.6 | 2100 | 89.6 | 5.39 | Soft-Speed Separation |
| 429 | Good, Ty | GAT_GRI | Cutter | 58 | 58.4 | 0.206 | 17.0 | 7.6 | 2059 | 88.4 | 6.14 | Soft-Speed Separation |
| 430 | Kelly, Colin | SUS_COU1 | Four-Seam | 82 | 58.2 | 0.213 | 17.4 | 10.6 | 1990 | 90.6 | 5.94 | Soft-Speed Separation |
| 431 | Hungate, Chase | NEW_JER6 | Sinker | 83 | 58.1 | 0.210 | 0.1 | 20.5 | 2251 | 88.3 | 5.84 | Soft-Speed Separation |
| 432 | McMahon, Chris | LAK_ERI24 | Four-Seam | 69 | 57.9 | 0.232 | 13.9 | 9.7 | 2266 | 88.2 | 6.54 | Soft-Speed Separation |
| 433 | Morgan, Marcus | JOL_SLA | Sinker | 96 | 57.9 | 0.226 | 10.3 | 15.2 | 2455 | 91.9 | 6.20 | Soft-Speed Separation |
| 434 | Brouwer, Adam | LAK_ERI24 | Four-Seam | 50 | 57.8 | 0.205 | 18.6 | 8.4 | 2133 | 91.0 | 5.92 | Soft-Speed Separation |
| 435 | Riedel, Caleb | SCH_BOO | Four-Seam | 239 | 57.7 | 0.240 | 17.2 | -15.1 | 2342 | 89.4 | 5.84 | Soft-Speed Separation |
| 436 | Boies, Emiles | QUE_CAP | Changeup | 223 | 57.7 | 0.201 | 11.8 | 15.1 | 1932 | 82.5 | 6.22 | Soft-Speed Separation |
| 437 | Flontek, Zac | DOW_EAS1 | Cutter | 57 | 57.7 | 0.220 | 8.0 | -1.5 | 2651 | 88.8 | 6.04 | Soft-Speed Separation |
| 438 | Petery, Dylan | WIN_CIT29 | Four-Seam | 77 | 57.6 | 0.267 | 17.1 | 10.0 | 2361 | 86.3 | 6.14 | Soft-Speed Separation |
| 439 | Ortiz, Julio | GAT_GRI | Four-Seam | 349 | 57.5 | 0.205 | 18.1 | 8.2 | 2176 | 95.4 | 6.14 | Soft-Speed Separation |
| 440 | Herbert, Andrew | WAS_WIL3 | Four-Seam | 55 | 57.4 | 0.175 | 15.8 | 10.9 | 2226 | 91.2 | 6.43 | Soft-Speed Separation |
| 441 | Duby, Bill | NEW_JER6 | Slider | 88 | 57.3 | 0.205 | 7.3 | -0.3 | 2066 | 80.0 | 6.50 | Soft-Speed Separation |
| 442 | Vilchez, Michael | OTT_TIT | Four-Seam | 155 | 57.1 | 0.200 | 16.3 | 9.2 | 2249 | 93.3 | 6.25 | Soft-Speed Separation |
| 443 | Rodriguez, Joe Joe | NEW_JER6 | Four-Seam | 108 | 57.1 | 0.207 | 16.6 | 13.3 | 2142 | 91.8 | 5.78 | Soft-Speed Separation |
| 444 | Grounds, Jackson | DOW_EAS1 | Sinker | 116 | 57.0 | 0.214 | 15.0 | 16.4 | 2139 | 92.2 | 5.50 | Soft-Speed Separation |
| 445 | Henderson, Drew | DOW_EAS1 | Sinker | 129 | 56.9 | 0.214 | 16.1 | 15.5 | 2213 | 89.0 | 5.59 | Soft-Speed Separation |
| 446 | Saturria, Michael | NEW_ENG23 | Cutter | 255 | 56.8 | 0.238 | 12.9 | -0.7 | 2505 | 86.5 | 6.38 | Soft-Speed Separation |
| 447 | Garcia, Brett | OTT_TIT | Four-Seam | 277 | 56.8 | 0.210 | 17.0 | 6.4 | 2372 | 91.9 | 6.13 | Soft-Speed Separation |
| 448 | Gartland, Chad | TRI_VAL | Changeup | 59 | 56.7 | 0.225 | 8.1 | 14.4 | 1711 | 84.0 | 6.04 | Soft-Speed Separation |
| 449 | Long, Maddox | WAS_WIL3 | Four-Seam | 155 | 56.6 | 0.221 | 12.7 | 9.4 | 2343 | 91.7 | 6.13 | Soft-Speed Separation |
| 450 | Williams, Pierce | NEW_ENG23 | Four-Seam | 313 | 56.6 | 0.215 | 16.4 | -11.6 | 1915 | 85.6 | 6.18 | Soft-Speed Separation |
| 451 | McCartney, Seth | MIS_MUD | Sinker | 120 | 56.5 | 0.237 | 10.4 | 15.2 | 2316 | 90.2 | 5.76 | Soft-Speed Separation |
| 452 | Debban, Caleb | NEW_JER6 | Cutter | 142 | 56.5 | 0.238 | 10.7 | -0.4 | 2337 | 85.9 | 6.59 | Soft-Speed Separation |
| 453 | Moore, Kyle | SCH_BOO | Four-Seam | 183 | 56.4 | 0.209 | 17.9 | 14.3 | 2176 | 88.4 | 4.68 | Soft-Speed Separation |
| 454 | McEvoy, Aidan | FLO_Y'A | Cutter | 85 | 56.4 | 0.214 | 7.6 | 1.3 | 2151 | 83.1 | 6.11 | Soft-Speed Separation |
| 455 | Glickstein, Aaron | SCH_BOO | Four-Seam | 195 | 56.3 | 0.207 | 14.5 | 9.6 | 2226 | 89.0 | 6.11 | Soft-Speed Separation |
| 456 | Jones, Breyln | NEW_JER6 | Slider | 104 | 56.3 | 0.214 | 8.2 | -0.6 | 2073 | 86.1 | 5.86 | Soft-Speed Separation |
| 457 | Dill, Austin | TRI_VAL | Changeup | 204 | 56.2 | 0.208 | 10.7 | 16.5 | 1931 | 80.5 | 5.23 | Soft-Speed Separation |
| 458 | Lawson, Nathan | FLO_Y'A | Sinker | 218 | 56.1 | 0.213 | 9.8 | 15.6 | 2186 | 88.8 | 6.14 | Soft-Speed Separation |
| 459 | De Jesus, Larry | DOW_EAS1 | Four-Seam | 89 | 55.9 | 0.198 | 16.8 | 12.4 | 2403 | 89.7 | 5.24 | Soft-Speed Separation |
| 460 | Long, Maddox | WAS_WIL3 | Sinker | 285 | 55.8 | 0.233 | 7.1 | 16.6 | 2182 | 89.9 | 5.89 | Soft-Speed Separation |
| 461 | Fritz, AJ | MIS_MUD | Sinker | 55 | 55.5 | 0.238 | 6.8 | 16.5 | 2042 | 88.4 | 5.39 | Soft-Speed Separation |
| 462 | Turner, Eric | JOL_SLA | Sinker | 113 | 55.5 | 0.210 | 14.9 | 16.1 | 2318 | 88.2 | 5.09 | Soft-Speed Separation |
| 463 | Whitesell, Max | FLO_Y'A | Changeup | 62 | 55.4 | 0.254 | 8.8 | 10.6 | 1621 | 85.3 | 6.40 | Soft-Speed Separation |
| 464 | Salata, Derek | SCH_BOO | Splitter | 92 | 55.3 | 0.201 | 7.1 | 9.2 | 1133 | 83.2 | 5.79 | Soft-Speed Separation |
| 465 | Sanchez, Edwin | LAK_ERI24 | Four-Seam | 178 | 55.3 | 0.201 | 15.4 | -13.3 | 2093 | 87.0 | 5.51 | Soft-Speed Separation |
| 466 | Odonnell, Brendan | NEW_ENG23 | Four-Seam | 70 | 55.2 | 0.248 | 13.5 | -7.3 | 2453 | 91.4 | 6.97 | Soft-Speed Separation |
| 467 | Burcham, Jacob | GAT_GRI | Changeup | 99 | 55.1 | 0.203 | 3.7 | 17.9 | 1901 | 83.5 | 6.19 | Soft-Speed Separation |
| 468 | Hargrove, Dawson | LAK_ERI24 | Four-Seam | 127 | 55.1 | 0.209 | 19.6 | 7.6 | 1999 | 89.7 | 5.51 | Soft-Speed Separation |
| 469 | Shinn, Nathan | LAK_ERI24 | Four-Seam | 250 | 55.1 | 0.214 | 17.4 | -9.5 | 1970 | 89.1 | 5.88 | Soft-Speed Separation |
| 470 | Thompson, Ross | SCH_BOO | Splitter | 175 | 55.1 | 0.229 | 3.9 | 9.3 | 1055 | 79.5 | 5.44 | Soft-Speed Separation |
| 471 | Flontek, Zac | DOW_EAS1 | Four-Seam | 369 | 54.9 | 0.190 | 18.2 | 5.1 | 2598 | 91.7 | 6.47 | Soft-Speed Separation |
| 472 | Calderon, Jean | LAK_ERI24 | Four-Seam | 87 | 54.8 | 0.242 | 12.0 | 0.8 | 2526 | 94.1 | 6.38 | Soft-Speed Separation |
| 473 | Scafidi, Christian | LAK_ERI24 | Four-Seam | 300 | 54.8 | 0.205 | 17.8 | 4.8 | 2492 | 89.9 | 6.15 | Soft-Speed Separation |
| 474 | McKillican, Adam | QUE_CAP | Changeup | 70 | 54.7 | 0.211 | 10.3 | 13.1 | 1714 | 85.5 | 6.79 | Soft-Speed Separation |
| 475 | Brouwer, Adam | LAK_ERI24 | Four-Seam | 190 | 54.7 | 0.206 | 19.1 | 10.3 | 2257 | 90.5 | 5.97 | Soft-Speed Separation |
| 476 | Milburn, Isaac | FLO_Y'A | Sinker | 109 | 54.6 | 0.231 | 10.1 | -13.4 | 2065 | 88.1 | 5.48 | Soft-Speed Separation |
| 477 | Tiburcio, David | DOW_EAS1 | Four-Seam | 67 | 54.5 | 0.226 | 16.7 | 13.6 | 2272 | 93.7 | 5.16 | Soft-Speed Separation |
| 478 | Bell, Brendan | NEW_ENG23 | Four-Seam | 140 | 54.4 | 0.267 | 11.0 | 3.0 | 2361 | 92.0 | 5.98 | Soft-Speed Separation |
| 479 | Kelly, Colin | SUS_COU1 | Sinker | 96 | 54.3 | 0.188 | 14.3 | 15.8 | 2008 | 90.5 | 5.91 | Soft-Speed Separation |
| 480 | Vega, Lucas | TRO_AIG | Changeup | 74 | 54.3 | 0.273 | 8.6 | 14.7 | 1967 | 83.6 | 6.24 | Soft-Speed Separation |
| 481 | Ginn, Landon | WAS_WIL3 | Four-Seam | 145 | 54.3 | 0.243 | 15.4 | 3.3 | 2597 | 91.9 | 5.65 | Soft-Speed Separation |
| 482 | Wilcenski, Blaise | WIN_CIT29 | Four-Seam | 76 | 54.2 | 0.201 | 15.0 | 8.9 | 2012 | 90.7 | 6.28 | Soft-Speed Separation |
| 483 | Hopewell, Chase | FLO_Y'A | Four-Seam | 253 | 54.2 | 0.214 | 16.7 | 11.3 | 2216 | 92.9 | 6.49 | Soft-Speed Separation |
| 484 | Aldeano, Austin | TRO_AIG | Sinker | 70 | 54.1 | 0.217 | 16.0 | 17.8 | 2219 | 90.2 | 6.06 | Soft-Speed Separation |
| 485 | Gorgen, Grady | NEW_YOR13 | Cutter | 78 | 54.1 | 0.212 | 8.1 | -3.5 | 2127 | 86.5 | 6.26 | Soft-Speed Separation |
| 486 | O'Dell, Casey | JOL_SLA | Four-Seam | 127 | 54.1 | 0.209 | 17.8 | 8.9 | 2223 | 91.1 | 6.05 | Soft-Speed Separation |
| 487 | Roland, Cole | QUE_CAP | Changeup | 71 | 54.0 | 0.245 | 10.4 | 9.6 | 2033 | 82.6 | 5.56 | Soft-Speed Separation |
| 488 | MacMillan, Blake | TRO_AIG | Cutter | 144 | 54.0 | 0.213 | 21.8 | -6.9 | 2193 | 87.9 | 5.52 | Soft-Speed Separation |
| 489 | Allemann, Braeden | QUE_CAP | Sinker | 71 | 54.0 | 0.223 | 15.1 | 16.1 | 2295 | 90.4 | 6.17 | Soft-Speed Separation |
| 490 | Almanzar, Elian | DOW_EAS1 | Four-Seam | 147 | 53.9 | 0.194 | 16.0 | 3.7 | 2279 | 95.1 | 6.18 | Soft-Speed Separation |
| 491 | Cameron, Zach | WIN_CIT29 | Changeup | 212 | 53.9 | 0.229 | 7.4 | 21.1 | 2119 | 80.3 | 5.55 | Soft-Speed Separation |
| 492 | Morgan, Cooper | QUE_CAP | Cutter | 115 | 53.9 | 0.212 | 8.8 | -3.0 | 2146 | 86.4 | 5.89 | Soft-Speed Separation |
| 493 | Delaney, Carter | WIN_CIT29 | Four-Seam | 155 | 53.9 | 0.231 | 17.9 | 9.4 | 2220 | 88.9 | 6.30 | Soft-Speed Separation |
| 494 | Kines, Gunnar | JOL_SLA | Four-Seam | 564 | 53.9 | 0.214 | 17.4 | -12.3 | 2235 | 86.3 | 5.83 | Soft-Speed Separation |
| 495 | Martinez, Gregory | DOW_EAS1 | Four-Seam | 95 | 53.8 | 0.220 | 16.3 | 13.5 | 2312 | 94.7 | 5.55 | Soft-Speed Separation |
| 496 | Alpern, Liam | FLO_Y'A | Four-Seam | 264 | 53.8 | 0.216 | 17.2 | -12.7 | 2227 | 89.1 | 6.04 | Soft-Speed Separation |
| 497 | Hensey, Rob | SUS_COU1 | Sinker | 469 | 53.7 | 0.231 | 13.5 | -15.9 | 2143 | 91.7 | 6.25 | Soft-Speed Separation |
| 498 | Vailes, Gage | GAT_GRI | Changeup | 161 | 53.7 | 0.235 | 6.2 | 11.1 | 1873 | 85.7 | 5.16 | Soft-Speed Separation |
| 499 | Long, Jalon | NEW_YOR13 | Four-Seam | 224 | 53.7 | 0.202 | 20.4 | 8.2 | 2129 | 92.0 | 6.09 | Soft-Speed Separation |
| 500 | Gregory, Ben | GAT_GRI | Sinker | 227 | 53.6 | 0.211 | 14.7 | 15.9 | 2260 | 89.1 | 6.54 | Soft-Speed Separation |
| 501 | Daly, Ryan | JOL_SLA | Changeup | 266 | 53.6 | 0.245 | 5.2 | 16.2 | 2108 | 79.0 | 6.79 | Soft-Speed Separation |
| 502 | Morgan, Cooper | QUE_CAP | Sinker | 126 | 53.6 | 0.221 | 11.9 | -12.4 | 2165 | 87.6 | 6.20 | Soft-Speed Separation |
| 503 | Webster, Evan | FLO_Y'A | Four-Seam | 567 | 53.5 | 0.210 | 16.5 | -10.9 | 1975 | 89.0 | 6.80 | Soft-Speed Separation |
| 504 | Martinez, Mason | TRI_VAL | Sinker | 347 | 53.5 | 0.231 | 12.1 | 18.9 | 2279 | 88.8 | 6.45 | Soft-Speed Separation |
| 505 | Daly, Ryan | JOL_SLA | Four-Seam | 604 | 53.4 | 0.235 | 14.8 | 13.4 | 2207 | 90.3 | 6.76 | Soft-Speed Separation |
| 506 | Agosto, Justus | TRI_VAL | Four-Seam | 78 | 53.3 | 0.220 | 17.6 | 8.1 | 2013 | 89.3 | 6.05 | Soft-Speed Separation |
| 507 | McEvoy, Aidan | FLO_Y'A | Four-Seam | 63 | 53.3 | 0.204 | 14.4 | -15.0 | 1967 | 90.1 | 6.45 | Soft-Speed Separation |
| 508 | Westcott, Zac | FLO_Y'A | Four-Seam | 327 | 53.3 | 0.216 | 16.5 | 14.5 | 2099 | 83.4 | 5.90 | Soft-Speed Separation |
| 509 | Jones, Breyln | NEW_JER6 | Four-Seam | 60 | 53.2 | 0.266 | 13.4 | 6.1 | 1990 | 88.9 | 5.89 | Soft-Speed Separation |
| 510 | Perez, Kelvin | WAS_WIL3 | Four-Seam | 127 | 53.2 | 0.224 | 15.4 | 10.9 | 2077 | 89.1 | 6.14 | Soft-Speed Separation |
| 511 | Campbell, Tyler | MIS_MUD | Cutter | 148 | 53.2 | 0.232 | 8.4 | -3.7 | 2268 | 83.9 | 6.08 | Soft-Speed Separation |
| 512 | Barraza, Chris | MIS_MUD | Four-Seam | 568 | 53.1 | 0.190 | 19.9 | 10.3 | 2452 | 93.2 | 5.86 | Soft-Speed Separation |
| 513 | Bauer, Patrick | QUE_CAP | Four-Seam | 186 | 53.1 | 0.198 | 17.6 | 10.8 | 2414 | 87.9 | 6.55 | Soft-Speed Separation |
| 514 | Whitesell, Max | FLO_Y'A | Cutter | 52 | 53.0 | 0.228 | 10.8 | 1.1 | 2025 | 82.3 | 6.27 | Soft-Speed Separation |
| 515 | Cerda, Junior | EVA_OTT | Four-Seam | 129 | 53.0 | 0.228 | 15.3 | 15.7 | 2228 | 93.2 | 5.52 | Soft-Speed Separation |
| 516 | Leak, Anthony | NEW_YOR13 | Sinker | 126 | 52.9 | 0.236 | 10.3 | 14.3 | 2112 | 89.1 | 6.32 | Soft-Speed Separation |
| 517 | Ronne, Andrew | GAT_GRI | Four-Seam | 251 | 52.9 | 0.222 | 13.2 | 7.1 | 2174 | 91.7 | 6.38 | Soft-Speed Separation |
| 518 | Albert, Wes | TRI_VAL | Four-Seam | 125 | 52.9 | 0.192 | 16.1 | 9.3 | 2014 | 89.1 | 5.65 | Soft-Speed Separation |
| 519 | Whitesell, Max | FLO_Y'A | Four-Seam | 228 | 52.8 | 0.223 | 14.0 | 12.7 | 1908 | 88.8 | 6.39 | Soft-Speed Separation |
| 520 | Daly, Ryan | JOL_SLA | Sinker | 182 | 52.7 | 0.225 | 12.7 | 15.6 | 2201 | 90.0 | 6.83 | Soft-Speed Separation |
| 521 | Hickey, Matt | GAT_GRI | Sinker | 68 | 52.7 | 0.238 | 5.7 | 17.8 | 2258 | 88.5 | 5.67 | Soft-Speed Separation |
| 522 | Vecerka, Boris | QUE_CAP | Sinker | 232 | 52.6 | 0.209 | 10.3 | 17.7 | 2434 | 93.4 | 5.89 | Soft-Speed Separation |
| 523 | Fowler, Dalton | SUS_COU1 | Four-Seam | 89 | 52.6 | 0.232 | 14.6 | -10.9 | 2107 | 92.2 | 5.57 | Soft-Speed Separation |
| 524 | Brothers, Kellen | SUS_COU1 | Sinker | 136 | 52.6 | 0.243 | 16.3 | 16.0 | 2347 | 89.1 | 6.43 | Soft-Speed Separation |
| 525 | Hughes, Grif | EVA_OTT | Four-Seam | 57 | 52.5 | 0.187 | 17.7 | -12.9 | 2419 | 88.0 | 6.38 | Soft-Speed Separation |
| 526 | Marynczak, Arlo | TRI_VAL | Four-Seam | 305 | 52.5 | 0.217 | 16.7 | 10.5 | 2145 | 88.9 | 6.39 | Soft-Speed Separation |
| 527 | Brodsky, Jack | WAS_WIL3 | Four-Seam | 321 | 52.3 | 0.227 | 15.3 | 6.6 | 2168 | 90.3 | 6.24 | Soft-Speed Separation |
| 528 | McEvoy, Aidan | FLO_Y'A | Sinker | 201 | 52.2 | 0.221 | 12.8 | -16.6 | 1984 | 90.5 | 6.45 | Soft-Speed Separation |
| 529 | Sanchez, Sergio | MIS_MUD | Four-Seam | 208 | 52.1 | 0.218 | 15.2 | 10.7 | 2290 | 91.9 | 6.32 | Soft-Speed Separation |
| 530 | Webster, Evan | FLO_Y'A | Sinker | 63 | 52.0 | 0.238 | 15.6 | -11.2 | 1888 | 88.9 | 6.91 | Soft-Speed Separation |
| 531 | Kelly, Aiden | TRI_VAL | Sinker | 78 | 52.0 | 0.242 | 9.3 | 13.8 | 2221 | 88.8 | 5.90 | Soft-Speed Separation |
| 532 | Castro, Alexander | TRO_AIG | Four-Seam | 119 | 51.8 | 0.241 | 18.3 | 14.6 | 2258 | 93.2 | 5.19 | Soft-Speed Separation |
| 533 | Almonte, Lisandro | NEW_JER6 | Four-Seam | 210 | 51.8 | 0.208 | 16.4 | 12.7 | 2195 | 96.6 | 5.67 | Soft-Speed Separation |
| 534 | Balzan, Jackson | SUS_COU1 | Sinker | 142 | 51.8 | 0.220 | 17.3 | -14.6 | 2224 | 86.1 | 5.28 | Soft-Speed Separation |
| 535 | Wilson, Bradley | FLO_Y'A | Four-Seam | 60 | 51.7 | 0.214 | 12.5 | 5.0 | 2261 | 92.2 | 6.77 | Soft-Speed Separation |
| 536 | Gilleran, Jimmy | NEW_ENG23 | Sinker | 246 | 51.7 | 0.236 | 11.8 | 15.8 | 2091 | 87.9 | 5.57 | Soft-Speed Separation |
| 537 | Zentko, Dylan | EVA_OTT | Four-Seam | 208 | 51.6 | 0.225 | 17.4 | -8.1 | 1946 | 86.8 | 5.68 | Soft-Speed Separation |
| 538 | Darden, Nathan | FLO_Y'A | Four-Seam | 151 | 51.6 | 0.244 | 15.8 | 7.6 | 1935 | 91.6 | 5.38 | Soft-Speed Separation |
| 539 | Gordillo, Lucas | TRI_VAL | Changeup | 50 | 51.5 | 0.242 | 10.8 | 16.5 | 2145 | 80.3 | 6.02 | Soft-Speed Separation |
| 540 | Cerda, Junior | EVA_OTT | Sinker | 169 | 51.5 | 0.242 | 11.5 | 16.2 | 2218 | 94.0 | 5.43 | Soft-Speed Separation |
| 541 | Kirby, Zach | WAS_WIL3 | Changeup | 122 | 51.5 | 0.226 | 9.9 | 15.4 | 1690 | 79.8 | 6.07 | Soft-Speed Separation |
| 542 | Johnston, Spencer | DOW_EAS1 | Four-Seam | 57 | 51.5 | 0.234 | 17.7 | 11.8 | 2137 | 84.8 | 5.96 | Soft-Speed Separation |
| 543 | Rodriguez, Esteban | TRO_AIG | Four-Seam | 142 | 51.4 | 0.232 | 16.8 | 5.0 | 2157 | 88.7 | 5.81 | Soft-Speed Separation |
| 544 | Scott, Brandon | LAK_ERI24 | Four-Seam | 472 | 51.3 | 0.230 | 13.4 | -8.8 | 2304 | 88.8 | 6.19 | Soft-Speed Separation |
| 545 | Brothers, Kellen | SUS_COU1 | Four-Seam | 351 | 51.3 | 0.231 | 18.3 | 14.3 | 2353 | 89.3 | 6.47 | Soft-Speed Separation |
| 546 | Forsyth, Braden | MIS_MUD | Four-Seam | 280 | 51.1 | 0.208 | 19.1 | 9.7 | 2235 | 90.5 | 6.58 | Soft-Speed Separation |
| 547 | Albert, Wes | DOW_EAS1 | Changeup | 57 | 51.0 | 0.253 | 12.3 | 12.2 | 1781 | 82.9 | 5.74 | Soft-Speed Separation |
| 548 | Cooper, Garrett | NEW_YOR13 | Changeup | 335 | 51.0 | 0.241 | 9.2 | 8.0 | 1402 | 77.8 | 6.42 | Soft-Speed Separation |
| 549 | Tokar, Heitor | OTT_TIT | Four-Seam | 247 | 51.0 | 0.230 | 17.4 | 6.4 | 2012 | 88.1 | 6.38 | Soft-Speed Separation |
| 550 | Kirby, Zach | WAS_WIL3 | Four-Seam | 350 | 51.0 | 0.230 | 20.2 | 7.2 | 2174 | 87.8 | 6.12 | Soft-Speed Separation |
| 551 | Thebiay, Nolan | EVA_OTT | Four-Seam | 549 | 51.0 | 0.221 | 17.5 | 9.1 | 2277 | 89.5 | 6.83 | Soft-Speed Separation |
| 552 | Sittinger, Brandyn | LAK_ERI24 | Four-Seam | 254 | 51.0 | 0.243 | 17.3 | 13.5 | 2293 | 94.7 | 5.67 | Soft-Speed Separation |
| 553 | Hagan, Jack | DOW_EAS1 | Sinker | 272 | 50.8 | 0.225 | 10.6 | 16.6 | 2378 | 91.4 | 6.03 | Soft-Speed Separation |
| 554 | Castro, Alexander | TRO_AIG | Sinker | 54 | 50.8 | 0.212 | 15.8 | 16.9 | 2189 | 93.4 | 5.26 | Soft-Speed Separation |
| 555 | Petschke, Ben | EVA_OTT | Four-Seam | 223 | 50.8 | 0.251 | 11.8 | 5.4 | 2252 | 89.6 | 5.51 | Soft-Speed Separation |
| 556 | Johnson, Caiden | OTT_TIT | Sinker | 84 | 50.8 | 0.239 | 12.8 | -15.5 | 2225 | 90.0 | 5.95 | Soft-Speed Separation |
| 557 | Harris, Ben | GAT_GRI | Changeup | 351 | 50.7 | 0.242 | 8.7 | 16.1 | 1792 | 82.7 | 5.63 | Soft-Speed Separation |
| 558 | Eisenbarger, Jack | QUE_CAP | Four-Seam | 320 | 50.7 | 0.243 | 18.8 | -13.6 | 2545 | 89.8 | 5.83 | Soft-Speed Separation |
| 559 | Ferguson, Francis | QUE_CAP | Four-Seam | 129 | 50.6 | 0.230 | 14.7 | -8.1 | 2190 | 90.1 | 5.70 | Soft-Speed Separation |
| 560 | Widener, Jacob | SUS_COU1 | Four-Seam | 140 | 50.5 | 0.260 | 10.3 | -7.3 | 2362 | 89.0 | 6.70 | Soft-Speed Separation |
| 561 | Agosto, Justus | TRI_VAL | Slider | 54 | 50.5 | 0.228 | 8.6 | -1.5 | 2249 | 84.8 | 5.80 | Soft-Speed Separation |
| 562 | Good, Ty | GAT_GRI | Four-Seam | 488 | 50.5 | 0.213 | 18.6 | 4.9 | 2096 | 89.2 | 6.19 | Soft-Speed Separation |
| 563 | Primeaux, Parker | SUS_COU1 | Changeup | 102 | 50.5 | 0.249 | 0.8 | 17.7 | 2014 | 85.9 | 5.57 | Soft-Speed Separation |
| 564 | Vega, Lucas | TRO_AIG | Four-Seam | 124 | 50.4 | 0.225 | 11.7 | 10.1 | 2081 | 89.8 | 6.13 | Soft-Speed Separation |
| 565 | Peyton, Blake | GAT_GRI | Four-Seam | 234 | 50.4 | 0.208 | 18.3 | -13.4 | 2258 | 89.3 | 5.92 | Soft-Speed Separation |
| 566 | Simone, Andrew | TRO_AIG | Changeup | 92 | 50.4 | 0.222 | 10.3 | 12.8 | 1686 | 85.3 | 5.94 | Soft-Speed Separation |
| 567 | Garcia, Jorge | SUS_COU1 | Changeup | 55 | 50.4 | 0.231 | 12.5 | 9.4 | 1505 | 81.8 | 5.97 | Soft-Speed Separation |
| 568 | Zeplin, Blane | JOL_SLA | Four-Seam | 236 | 50.4 | 0.217 | 18.6 | 9.0 | 2288 | 89.7 | 5.93 | Soft-Speed Separation |
| 569 | Foltz Jr., Michael | WAS_WIL3 | Four-Seam | 298 | 50.3 | 0.245 | 18.9 | -4.1 | 2187 | 92.5 | 6.02 | Soft-Speed Separation |
| 570 | Garcia, Jorge | SUS_COU1 | Four-Seam | 187 | 50.3 | 0.216 | 16.8 | 4.3 | 2100 | 86.0 | 6.05 | Soft-Speed Separation |
| 571 | Peyton, Blake | GAT_GRI | Sinker | 77 | 50.2 | 0.196 | 16.4 | -15.0 | 2211 | 89.1 | 6.05 | Soft-Speed Separation |
| 572 | Kines, Gunnar | JOL_SLA | Sinker | 113 | 50.2 | 0.240 | 17.3 | -12.7 | 2195 | 84.7 | 5.85 | Soft-Speed Separation |
| 573 | Cook, Avery | WIN_CIT29 | Sinker | 113 | 50.2 | 0.238 | -0.1 | 16.3 | 2187 | 88.4 | 6.56 | Soft-Speed Separation |
| 574 | Thebiay, Nolan | EVA_OTT | Changeup | 118 | 50.1 | 0.267 | 4.9 | 16.2 | 1929 | 83.1 | 6.38 | Soft-Speed Separation |
| 575 | Hoeymans, Jack | GAT_GRI | Sinker | 66 | 50.1 | 0.221 | 7.4 | 15.1 | 2157 | 89.4 | 6.32 | Soft-Speed Separation |
| 576 | Johnston, Spencer | DOW_EAS1 | Changeup | 299 | 50.0 | 0.241 | 8.7 | 10.0 | 1618 | 77.6 | 5.93 | Soft-Speed Separation |
| 577 | Benitez, Jorge | NEW_JER6 | Sinker | 153 | 50.0 | 0.219 | 9.0 | -12.5 | 2182 | 93.2 | 6.10 | Soft-Speed Separation |
| 578 | Toribio, Noe | TRO_AIG | Changeup | 299 | 50.0 | 0.257 | 6.9 | 16.5 | 1979 | 83.2 | 5.63 | Soft-Speed Separation |
| 579 | Bihm, Gage | MIS_MUD | Four-Seam | 180 | 50.0 | 0.211 | 15.1 | -10.8 | 1946 | 92.1 | 5.44 | Soft-Speed Separation |
| 580 | Baird, Dustin | MIS_MUD | Four-Seam | 81 | 50.0 | 0.248 | 14.4 | 13.4 | 2056 | 89.5 | 5.99 | Soft-Speed Separation |
| 581 | Pardinho, Eric | OTT_TIT | Four-Seam | 374 | 50.0 | 0.234 | 19.2 | 12.9 | 2238 | 92.7 | 5.50 | Soft-Speed Separation |
| 582 | Langrell, Connor | MIS_MUD | Cutter | 275 | 49.9 | 0.231 | 9.7 | -0.6 | 2306 | 86.4 | 6.14 | Soft-Speed Separation |
| 583 | Johnson, Preston | MIS_MUD | Four-Seam | 90 | 49.8 | 0.197 | 20.3 | 6.9 | 2368 | 92.2 | 6.33 | Soft-Speed Separation |
| 584 | Vail, Tyler | NEW_YOR13 | Changeup | 219 | 49.8 | 0.252 | 6.3 | 13.1 | 1787 | 83.1 | 6.21 | Soft-Speed Separation |
| 585 | Hagan, Jack | DOW_EAS1 | Four-Seam | 82 | 49.7 | 0.188 | 13.5 | 13.2 | 2381 | 91.6 | 5.99 | Soft-Speed Separation |
| 586 | Phelps, Travis | FLO_Y'A | Four-Seam | 154 | 49.7 | 0.246 | 15.3 | 6.9 | 2131 | 91.1 | 6.39 | Soft-Speed Separation |
| 587 | Kalisky, Jack | OTT_TIT | Four-Seam | 76 | 49.6 | 0.214 | 13.2 | 7.3 | 2405 | 88.4 | 5.85 | Soft-Speed Separation |
| 588 | Traver, Eliott | LAK_ERI24 | Sinker | 65 | 49.5 | 0.203 | 8.8 | 16.7 | 2147 | 80.7 | 5.77 | Soft-Speed Separation |
| 589 | Parra, Andres | LAK_ERI24 | Four-Seam | 241 | 49.5 | 0.241 | 14.2 | -13.0 | 2044 | 88.4 | 6.07 | Soft-Speed Separation |
| 590 | Ryan, Dillon | NEW_ENG23 | Sinker | 220 | 49.4 | 0.257 | 12.5 | 16.3 | 2323 | 91.2 | 6.32 | Soft-Speed Separation |
| 591 | Barker, Alex | NEW_YOR13 | Changeup | 136 | 49.4 | 0.243 | 5.4 | -12.3 | 1533 | 82.8 | 6.27 | Soft-Speed Separation |
| 592 | Vitas, Ben | JOL_SLA | Four-Seam | 293 | 49.3 | 0.246 | 13.8 | 16.5 | 2153 | 90.3 | 5.13 | Soft-Speed Separation |
| 593 | Moreno, Jose | DOW_EAS1 | Changeup | 93 | 49.3 | 0.230 | 7.1 | 11.0 | 1766 | 81.6 | 5.65 | Soft-Speed Separation |
| 594 | Agosto, Justus | TRI_VAL | Changeup | 53 | 49.3 | 0.268 | 10.4 | 9.6 | 1718 | 80.7 | 5.87 | Soft-Speed Separation |
| 595 | Leach, Landon | TRO_AIG | Four-Seam | 196 | 49.2 | 0.249 | 10.6 | 5.2 | 1972 | 91.6 | 5.67 | Soft-Speed Separation |
| 596 | De Jesus, Larry | DOW_EAS1 | Sinker | 87 | 49.2 | 0.244 | 14.2 | 16.2 | 2354 | 89.4 | 5.16 | Soft-Speed Separation |
| 597 | Marklund, Brandon | OTT_TIT | Four-Seam | 279 | 49.1 | 0.239 | 16.9 | 10.5 | 2209 | 90.8 | 5.25 | Soft-Speed Separation |
| 598 | Quigley, Michael | NEW_ENG23 | Four-Seam | 292 | 49.1 | 0.222 | 17.7 | 12.6 | 2298 | 92.8 | 5.93 | Soft-Speed Separation |
| 599 | Binns, Malik | NEW_JER6 | Cutter | 88 | 49.1 | 0.212 | 9.5 | -1.9 | 2229 | 88.9 | 6.18 | Soft-Speed Separation |
| 600 | Primeaux, Parker | SUS_COU1 | Sinker | 87 | 49.1 | 0.236 | 0.1 | 18.5 | 2076 | 87.6 | 5.58 | Soft-Speed Separation |
| 601 | Aldeano, Austin | TRO_AIG | Changeup | 51 | 49.0 | 0.247 | 7.1 | 17.6 | 1856 | 81.3 | 6.28 | Soft-Speed Separation |
| 602 | Cohn, Cooper | NIU_HUS | Four-Seam | 72 | 49.0 | 0.215 | 17.8 | 12.6 | 2195 | 91.1 | 5.96 | Soft-Speed Separation |
| 603 | Dill, Austin | TRI_VAL | Four-Seam | 113 | 49.0 | 0.220 | 16.4 | 13.3 | 2324 | 87.2 | 5.33 | Soft-Speed Separation |
| 604 | Marynczak, Arlo | TRI_VAL | Changeup | 145 | 48.9 | 0.265 | 7.1 | 12.5 | 1656 | 81.8 | 6.30 | Soft-Speed Separation |
| 605 | Harajli, Ahmad | FLO_Y'A | Four-Seam | 189 | 48.9 | 0.267 | 14.7 | 8.8 | 2042 | 92.0 | 6.43 | Soft-Speed Separation |
| 606 | Fauci, Sonny | NEW_JER6 | Four-Seam | 312 | 48.8 | 0.240 | 17.1 | 12.9 | 2228 | 93.8 | 6.42 | Soft-Speed Separation |
| 607 | Earwood, Micah | SUS_COU1 | Sinker | 129 | 48.8 | 0.217 | 7.4 | 14.7 | 2168 | 87.4 | 6.29 | Soft-Speed Separation |
| 608 | Huter, Blayne | SUS_COU1 | Four-Seam | 142 | 48.7 | 0.241 | 17.1 | 6.2 | 2055 | 87.1 | 6.54 | Soft-Speed Separation |
| 609 | Rodriguez, Leonardo | NEW_JER6 | Four-Seam | 181 | 48.6 | 0.225 | 15.6 | 10.3 | 2440 | 92.2 | 6.57 | Soft-Speed Separation |
| 610 | Reeves, Cobe | NEW_YOR13 | Sinker | 214 | 48.6 | 0.260 | 8.9 | -15.2 | 1821 | 90.3 | 6.02 | Soft-Speed Separation |
| 611 | Fauci, Sonny | NEW_JER6 | Sinker | 83 | 48.6 | 0.252 | 14.2 | 16.3 | 2239 | 92.8 | 6.46 | Soft-Speed Separation |
| 612 | Eldred, Zach | NEW_ENG23 | Sinker | 103 | 48.6 | 0.242 | 11.8 | 13.3 | 2378 | 88.9 | 6.50 | Soft-Speed Separation |
| 613 | Woolfolk, Dallas | MIS_MUD | Four-Seam | 231 | 48.6 | 0.227 | 19.6 | 12.9 | 2397 | 92.7 | 5.50 | Soft-Speed Separation |
| 614 | Lefebvre, Charles | TRO_AIG | Sinker | 412 | 48.5 | 0.240 | 12.3 | 16.7 | 2232 | 89.1 | 6.53 | Soft-Speed Separation |
| 615 | Encarnacion, J.D. | EVA_OTT | Four-Seam | 326 | 48.5 | 0.230 | 14.4 | 8.1 | 2333 | 88.7 | 5.89 | Soft-Speed Separation |
| 616 | Catrambone, Ben | JOL_SLA | Four-Seam | 186 | 48.5 | 0.226 | 20.0 | 8.9 | 2120 | 87.9 | 5.12 | Soft-Speed Separation |
| 617 | Miranda, Kevin | OTT_TIT | Changeup | 140 | 48.5 | 0.253 | 8.4 | 12.6 | 1414 | 79.4 | 6.08 | Soft-Speed Separation |
| 618 | Duby, Bill | NEW_JER6 | Sinker | 166 | 48.5 | 0.246 | 13.9 | 16.0 | 2067 | 87.2 | 6.34 | Soft-Speed Separation |
| 619 | Delongchamp, Luke | TRI_VAL | Changeup | 312 | 48.4 | 0.246 | 8.4 | 16.2 | 1868 | 82.3 | 5.60 | Soft-Speed Separation |
| 620 | Noriega, Branden | LAK_ERI24 | Sinker | 104 | 48.4 | 0.267 | 13.0 | -15.4 | 2200 | 90.2 | 6.21 | Soft-Speed Separation |
| 621 | Stuka, Ted | OTT_TIT | Sinker | 164 | 48.4 | 0.242 | 12.1 | 19.4 | 2341 | 95.1 | 5.22 | Soft-Speed Separation |
| 622 | Floyd, Conner | QUE_CAP | Four-Seam | 363 | 48.4 | 0.219 | 20.5 | 10.5 | 2401 | 92.7 | 5.52 | Soft-Speed Separation |
| 623 | Ferguson, Francis | WIN_CIT29 | Four-Seam | 162 | 48.4 | 0.251 | 10.7 | -5.8 | 1966 | 90.2 | 5.46 | Soft-Speed Separation |
| 624 | Sparks, Alec | GAT_GRI | Four-Seam | 407 | 48.4 | 0.238 | 17.2 | 4.6 | 2176 | 91.1 | 5.95 | Soft-Speed Separation |
| 625 | Armstrong, Andrew | NEW_YOR13 | Sinker | 91 | 48.3 | 0.257 | 13.0 | -12.3 | 2103 | 88.7 | 6.46 | Soft-Speed Separation |
| 626 | Miranda, Kevin | OTT_TIT | Four-Seam | 189 | 48.3 | 0.238 | 19.4 | 13.6 | 2170 | 87.2 | 5.75 | Soft-Speed Separation |
| 627 | Hocom, Quinn | TRI_VAL | Four-Seam | 296 | 48.3 | 0.253 | 21.1 | 10.3 | 2173 | 89.0 | 5.99 | Soft-Speed Separation |
| 628 | Eckaus, David | EVA_OTT | Four-Seam | 252 | 48.2 | 0.243 | 15.1 | -11.3 | 2351 | 91.2 | 6.13 | Soft-Speed Separation |
| 629 | Rodriguez, Luis | TRO_AIG | Four-Seam | 276 | 48.2 | 0.253 | 20.6 | 7.0 | 2360 | 95.1 | 6.06 | Soft-Speed Separation |
| 630 | Sakurai, Masatoshi | QUE_CAP | Changeup | 158 | 48.2 | 0.258 | 8.4 | -5.5 | 1440 | 80.5 | 6.00 | Soft-Speed Separation |
| 631 | Sesar, Jorden | SUS_COU1 | Four-Seam | 611 | 48.2 | 0.233 | 19.5 | 8.4 | 2477 | 91.5 | 6.29 | Soft-Speed Separation |
| 632 | Burcham, Jacob | GAT_GRI | Sinker | 237 | 48.2 | 0.259 | 6.4 | 15.9 | 2270 | 91.1 | 6.64 | Soft-Speed Separation |
| 633 | Sakurai, Masatoshi | QUE_CAP | Four-Seam | 520 | 48.0 | 0.239 | 16.4 | -7.2 | 2029 | 87.6 | 6.52 | Soft-Speed Separation |
| 634 | Galva, Claudio | GAT_GRI | Four-Seam | 130 | 47.9 | 0.252 | 12.5 | -10.1 | 1989 | 89.0 | 4.92 | Soft-Speed Separation |
| 635 | Simpson, Garret | EVA_OTT | Four-Seam | 370 | 47.8 | 0.248 | 11.0 | 3.2 | 2341 | 89.0 | 5.74 | Soft-Speed Separation |
| 636 | Perozzi, John | SUS_COU1 | Four-Seam | 218 | 47.7 | 0.208 | 21.6 | 9.0 | 2198 | 91.5 | 6.01 | Soft-Speed Separation |
| 637 | Lovell, Justin | WIN_CIT29 | Cutter | 61 | 47.6 | 0.235 | 10.6 | -9.1 | 2277 | 91.5 | 6.35 | Soft-Speed Separation |
| 638 | Eldred, Zach | NEW_ENG23 | Four-Seam | 556 | 47.6 | 0.246 | 16.5 | 6.8 | 2497 | 89.7 | 6.43 | Soft-Speed Separation |
| 639 | Vailes, Gage | GAT_GRI | Sinker | 387 | 47.6 | 0.265 | 7.6 | 16.1 | 1957 | 90.1 | 5.04 | Soft-Speed Separation |
| 640 | Conklin, MacCallan | TRO_AIG | Slider | 62 | 47.5 | 0.234 | 9.1 | 0.6 | 2512 | 84.5 | 6.59 | Soft-Speed Separation |
| 641 | Parsons, Billy | SUS_COU1 | Four-Seam | 347 | 47.5 | 0.226 | 17.5 | 9.4 | 2234 | 90.5 | 5.74 | Soft-Speed Separation |
| 642 | Cihocki, Danny | NIU_HUS | Four-Seam | 55 | 47.5 | 0.217 | 15.8 | 12.3 | 2221 | 89.2 | 6.54 | Soft-Speed Separation |
| 643 | Hampton, Ky | OTT_TIT | Changeup | 228 | 47.4 | 0.261 | 2.2 | 15.6 | 1705 | 84.0 | 6.01 | Soft-Speed Separation |
| 644 | Boies, Emiles | QUE_CAP | Four-Seam | 101 | 47.3 | 0.239 | 17.1 | 12.9 | 2134 | 87.5 | 6.04 | Soft-Speed Separation |
| 645 | Webster, Evan | FLO_Y'A | Changeup | 182 | 47.3 | 0.248 | 11.2 | -11.6 | 1788 | 82.4 | 6.91 | Soft-Speed Separation |
| 646 | Brothers, Kellen | SUS_COU1 | Slider | 74 | 47.3 | 0.220 | 8.0 | -1.8 | 2357 | 82.3 | 6.25 | Soft-Speed Separation |
| 647 | Thompson, Ross | SCH_BOO | Changeup | 85 | 47.3 | 0.254 | 5.4 | 9.0 | 1095 | 79.7 | 5.67 | Soft-Speed Separation |
| 648 | Wiltse, Ryan | EVA_OTT | Cutter | 52 | 47.2 | 0.246 | 8.2 | -0.9 | 1976 | 81.2 | 6.15 | Soft-Speed Separation |
| 649 | Bargo, Casey | FLO_Y'A | Four-Seam | 189 | 47.2 | 0.255 | 14.5 | 11.6 | 2211 | 91.3 | 5.89 | Soft-Speed Separation |
| 650 | Puccetti, Dominic | OTT_TIT | Four-Seam | 327 | 47.1 | 0.227 | 20.4 | -5.1 | 1869 | 87.9 | 5.63 | Soft-Speed Separation |
| 651 | Garcia, Andrew | EVA_OTT | Four-Seam | 246 | 47.1 | 0.251 | 13.2 | 7.1 | 2107 | 91.6 | 6.03 | Soft-Speed Separation |
| 652 | Esposito, Michael | NEW_ENG23 | Four-Seam | 139 | 47.1 | 0.249 | 16.9 | -11.5 | 2083 | 90.5 | 6.33 | Soft-Speed Separation |
| 653 | Gollert, Harley | QUE_CAP | Four-Seam | 81 | 47.1 | 0.247 | 16.6 | -8.3 | 2169 | 88.7 | 5.59 | Soft-Speed Separation |
| 654 | Long, Jalon | NEW_YOR13 | Changeup | 128 | 47.0 | 0.264 | 5.6 | 14.0 | 1519 | 82.0 | 6.10 | Soft-Speed Separation |
| 655 | Henderson, Drew | DOW_EAS1 | Changeup | 151 | 47.0 | 0.240 | 9.3 | 14.2 | 1699 | 81.6 | 5.79 | Soft-Speed Separation |
| 656 | Heredia-Bustos, Rolando | DOW_EAS1 | Changeup | 329 | 47.0 | 0.267 | 9.1 | 17.6 | 2064 | 79.4 | 5.62 | Soft-Speed Separation |
| 657 | Steinhauer, Ryan | NEW_JER6 | Four-Seam | 58 | 46.9 | 0.268 | 16.0 | -9.3 | 1936 | 86.4 | 6.05 | Soft-Speed Separation |
| 658 | Villalobos, Jonaiker | FLO_Y'A | Four-Seam | 506 | 46.8 | 0.245 | 14.8 | -9.7 | 2231 | 87.8 | 5.87 | Soft-Speed Separation |
| 659 | House, Tristan | MIS_MUD | Four-Seam | 320 | 46.8 | 0.245 | 16.9 | 9.6 | 1975 | 89.3 | 6.16 | Soft-Speed Separation |
| 660 | Thompson, Ross | SCH_BOO | Sinker | 51 | 46.8 | 0.222 | 13.6 | 12.6 | 1964 | 90.0 | 5.97 | Soft-Speed Separation |
| 661 | Estrella, Noah | TRI_VAL | Sinker | 59 | 46.8 | 0.280 | 14.3 | 14.6 | 2098 | 91.7 | 5.66 | Soft-Speed Separation |
| 662 | Wehrle, Tyler | WIN_CIT29 | Sinker | 94 | 46.7 | 0.246 | 15.5 | 16.6 | 2319 | 91.3 | 5.69 | Soft-Speed Separation |
| 663 | Pindel, Buddie | SCH_BOO | Four-Seam | 504 | 46.6 | 0.250 | 16.1 | 13.5 | 2199 | 89.8 | 5.64 | Soft-Speed Separation |
| 664 | Shoemaker, Adam | QUE_CAP | Sinker | 62 | 46.6 | 0.264 | 10.5 | -15.2 | 2056 | 91.7 | 6.06 | Soft-Speed Separation |
| 665 | Soto, Carlos | JOL_SLA | Four-Seam | 182 | 46.5 | 0.276 | 13.0 | 9.7 | 2218 | 88.5 | 5.46 | Soft-Speed Separation |
| 666 | Maietta, Dante | WIN_CIT29 | Slider | 92 | 46.5 | 0.273 | 7.1 | -1.9 | 2033 | 80.5 | 6.27 | Soft-Speed Separation |
| 667 | Perdomo, Rafael | QUE_CAP | Four-Seam | 173 | 46.4 | 0.221 | 20.2 | 11.0 | 2306 | 89.1 | 5.87 | Soft-Speed Separation |
| 668 | Cameron, Wyatt | SCH_BOO | Four-Seam | 185 | 46.3 | 0.261 | 14.8 | 10.9 | 2243 | 91.2 | 5.48 | Soft-Speed Separation |
| 669 | Potteiger, Jack | JOL_SLA | Sinker | 79 | 46.3 | 0.262 | 5.1 | -14.7 | 1942 | 89.4 | 6.39 | Soft-Speed Separation |
| 670 | Tomczak, Anthony | EVA_OTT | Sinker | 122 | 46.3 | 0.237 | 12.3 | 17.2 | 2277 | 93.7 | 6.02 | Soft-Speed Separation |
| 671 | Misla, Luis | TRI_VAL | Sinker | 51 | 46.2 | 0.247 | 14.4 | -14.9 | 2313 | 88.4 | 5.72 | Soft-Speed Separation |
| 672 | Misla, Luis | TRI_VAL | Four-Seam | 305 | 46.2 | 0.257 | 17.5 | -11.2 | 2403 | 88.6 | 5.83 | Soft-Speed Separation |
| 673 | Davis, Tyler | WAS_WIL3 | Four-Seam | 119 | 46.2 | 0.252 | 18.5 | -11.2 | 2340 | 92.6 | 5.88 | Soft-Speed Separation |
| 674 | Orth, Harry | SCH_BOO | Sinker | 57 | 46.1 | 0.256 | 13.1 | 15.4 | 1963 | 90.9 | 6.24 | Soft-Speed Separation |
| 675 | Serrano, Elio | NEW_JER6 | Four-Seam | 427 | 46.1 | 0.234 | 17.4 | 10.8 | 2447 | 91.3 | 5.72 | Soft-Speed Separation |
| 676 | Binns, Malik | NEW_JER6 | Four-Seam | 100 | 46.0 | 0.266 | 13.7 | 7.5 | 2102 | 91.3 | 6.52 | Soft-Speed Separation |
| 677 | Andueza, Axel | DOW_EAS1 | Four-Seam | 452 | 46.0 | 0.243 | 13.8 | 7.8 | 2125 | 90.6 | 5.52 | Soft-Speed Separation |
| 678 | Hohenstein, Liam | WIN_CIT29 | Changeup | 84 | 46.0 | 0.285 | 11.1 | 9.0 | 1547 | 84.1 | 6.04 | Soft-Speed Separation |
| 679 | Hines, Carter | FLO_Y'A | Four-Seam | 53 | 45.9 | 0.269 | 16.6 | -8.1 | 2502 | 91.0 | 5.91 | Soft-Speed Separation |
| 680 | Martinez, Gregory | DOW_EAS1 | Sinker | 98 | 45.7 | 0.245 | 12.3 | 16.1 | 2292 | 94.2 | 5.51 | Soft-Speed Separation |
| 681 | Maietta, Dante | WIN_CIT29 | Four-Seam | 472 | 45.6 | 0.240 | 19.3 | 9.3 | 2053 | 88.1 | 6.05 | Soft-Speed Separation |
| 682 | Barreto, Brayhans | TRI_VAL | Sinker | 150 | 45.6 | 0.278 | 12.1 | -14.0 | 2050 | 88.3 | 6.20 | Soft-Speed Separation |
| 683 | Gartland, Chad | SUS_COU1 | Four-Seam | 104 | 45.6 | 0.251 | 15.6 | 9.7 | 2115 | 91.0 | 6.26 | Soft-Speed Separation |
| 684 | Gordillo, Lucas | TRI_VAL | Sinker | 73 | 45.5 | 0.260 | 13.7 | 14.4 | 2120 | 91.6 | 5.98 | Soft-Speed Separation |
| 685 | Morel, Yohanse | OTT_TIT | Changeup | 103 | 45.4 | 0.258 | 5.1 | 17.1 | 2118 | 85.2 | 5.36 | Soft-Speed Separation |
| 686 | Potteiger, Jack | JOL_SLA | Sinker | 101 | 45.4 | 0.262 | 5.6 | -13.7 | 1950 | 89.6 | 6.03 | Soft-Speed Separation |
| 687 | Godwin, Connor | NEW_YOR13 | Sinker | 149 | 45.4 | 0.268 | 6.0 | 14.5 | 2153 | 91.8 | 6.07 | Soft-Speed Separation |
| 688 | Hill, Kaleb | OTT_TIT | Four-Seam | 57 | 45.3 | 0.250 | 14.2 | -10.1 | 1955 | 89.6 | 5.53 | Soft-Speed Separation |
| 689 | Petschke, Ben | EVA_OTT | Cutter | 254 | 45.3 | 0.240 | 10.1 | 2.7 | 2257 | 89.2 | 5.45 | Soft-Speed Separation |
| 690 | Kelly, Aiden | TRI_VAL | Four-Seam | 148 | 45.3 | 0.251 | 15.5 | 8.5 | 2248 | 90.1 | 5.99 | Soft-Speed Separation |
| 691 | Dill, Austin | TRI_VAL | Sinker | 197 | 45.3 | 0.264 | 14.8 | 15.8 | 2315 | 88.1 | 5.43 | Soft-Speed Separation |
| 692 | Parenteau, Matt | EVA_OTT | Four-Seam | 66 | 45.3 | 0.232 | 14.6 | 4.9 | 2252 | 92.0 | 6.39 | Soft-Speed Separation |
| 693 | McKillican, Adam | QUE_CAP | Sinker | 59 | 45.2 | 0.270 | 11.5 | 12.6 | 1988 | 88.6 | 6.73 | Soft-Speed Separation |
| 694 | Armstrong, Andrew | NEW_YOR13 | Four-Seam | 135 | 45.0 | 0.270 | 14.8 | -9.4 | 2121 | 88.9 | 6.44 | Soft-Speed Separation |
| 695 | Maher, Adam | TRI_VAL | Four-Seam | 240 | 45.0 | 0.258 | 20.1 | -9.6 | 2056 | 87.8 | 5.89 | Soft-Speed Separation |
| 696 | Garcia, Hector | WAS_WIL3 | Four-Seam | 199 | 45.0 | 0.253 | 19.5 | 4.6 | 2221 | 91.0 | 6.05 | Soft-Speed Separation |
| 697 | Henderson, Drew | DOW_EAS1 | Four-Seam | 472 | 44.9 | 0.245 | 18.6 | 13.1 | 2247 | 89.0 | 5.69 | Soft-Speed Separation |
| 698 | Escobar, Anthony | TRO_AIG | Four-Seam | 430 | 44.8 | 0.246 | 17.7 | 10.4 | 2142 | 90.6 | 6.34 | Soft-Speed Separation |
| 699 | Sanders, Brayden | MIS_MUD | Four-Seam | 230 | 44.8 | 0.268 | 18.7 | 11.0 | 2004 | 91.6 | 4.94 | Soft-Speed Separation |
| 700 | Williams, Brian | MIS_MUD | Cutter | 144 | 44.8 | 0.268 | 6.6 | -0.1 | 2190 | 83.2 | 6.47 | Soft-Speed Separation |
| 701 | Hernandez, Nyan | NEW_JER6 | Changeup | 177 | 44.8 | 0.241 | 11.9 | 15.8 | 1927 | 82.3 | 6.32 | Soft-Speed Separation |
| 702 | Gollert, Harley | TRO_AIG | Four-Seam | 160 | 44.7 | 0.233 | 15.5 | -10.1 | 2148 | 88.7 | 5.39 | Soft-Speed Separation |
| 703 | Boies, Emiles | QUE_CAP | Sinker | 223 | 44.7 | 0.260 | 14.8 | 16.1 | 2132 | 87.6 | 6.09 | Soft-Speed Separation |
| 704 | Shears, Tanner | SCH_BOO | Sinker | 60 | 44.7 | 0.267 | 12.9 | 14.7 | 1945 | 92.7 | 5.31 | Soft-Speed Separation |
| 705 | Bohnert, Matthew | WIN_CIT29 | Four-Seam | 331 | 44.7 | 0.247 | 16.8 | -8.7 | 2139 | 91.6 | 5.22 | Soft-Speed Separation |
| 706 | Primeaux, Parker | SUS_COU1 | Four-Seam | 56 | 44.7 | 0.252 | 5.4 | 16.0 | 2089 | 87.6 | 5.56 | Soft-Speed Separation |
| 707 | Cooper, Garrett | NEW_YOR13 | Four-Seam | 192 | 44.6 | 0.263 | 16.2 | 6.2 | 2083 | 89.6 | 5.90 | Soft-Speed Separation |
| 708 | Anibal, Trevor | NEW_ENG23 | Four-Seam | 240 | 44.5 | 0.273 | 18.9 | 12.1 | 2252 | 90.4 | 5.86 | Soft-Speed Separation |
| 709 | Townes, Holland | SCH_BOO | Four-Seam | 154 | 44.4 | 0.251 | 15.4 | 13.1 | 2206 | 92.7 | 5.39 | Soft-Speed Separation |
| 710 | Turner, Eric | JOL_SLA | Four-Seam | 465 | 44.4 | 0.240 | 16.2 | 13.9 | 2290 | 88.2 | 5.16 | Soft-Speed Separation |
| 711 | Chapple, Bronson | TRO_AIG | Changeup | 51 | 44.4 | 0.282 | 3.7 | 14.5 | 1828 | 83.2 | 6.34 | Soft-Speed Separation |
| 712 | Shinn, Nathan | LAK_ERI24 | Sinker | 50 | 44.4 | 0.240 | 15.9 | -10.4 | 1907 | 89.3 | 5.76 | Soft-Speed Separation |
| 713 | Vitas, Ben | JOL_SLA | Sinker | 236 | 44.4 | 0.251 | 14.5 | 17.6 | 2171 | 90.4 | 5.19 | Soft-Speed Separation |
| 714 | De Los Santos, Enmanuel | NEW_ENG23 | Four-Seam | 200 | 44.4 | 0.247 | 18.1 | 4.1 | 2120 | 88.5 | 6.79 | Soft-Speed Separation |
| 715 | Bargo, Casey | NEW_ENG23 | Four-Seam | 147 | 44.4 | 0.252 | 16.0 | 12.7 | 2282 | 92.2 | 6.19 | Soft-Speed Separation |
| 716 | Linderman, Greyson | JOL_SLA | Four-Seam | 68 | 44.3 | 0.263 | 14.2 | 12.7 | 2190 | 94.3 | 5.39 | Soft-Speed Separation |
| 717 | Smith, Ethan | WIN_CIT29 | Four-Seam | 169 | 44.1 | 0.244 | 16.6 | 9.8 | 2211 | 89.3 | 6.29 | Soft-Speed Separation |
| 718 | Nova, Fraynel | LAK_ERI24 | Four-Seam | 462 | 44.1 | 0.253 | 12.4 | 6.8 | 2059 | 90.3 | 6.04 | Soft-Speed Separation |
| 719 | Andueza, Axel | DOW_EAS1 | Sinker | 88 | 43.9 | 0.271 | 11.3 | 11.0 | 2040 | 89.9 | 5.47 | Soft-Speed Separation |
| 720 | Bargo, Casey | FLO_Y'A | Sinker | 111 | 43.9 | 0.256 | 12.5 | 15.6 | 2216 | 91.1 | 5.85 | Soft-Speed Separation |
| 721 | Helt, Robert | LAK_ERI24 | Four-Seam | 499 | 43.8 | 0.264 | 14.9 | 7.0 | 2284 | 91.5 | 6.31 | Soft-Speed Separation |
| 722 | Balzan, Jackson | SUS_COU1 | Four-Seam | 327 | 43.8 | 0.253 | 18.5 | -12.4 | 2246 | 86.3 | 5.46 | Soft-Speed Separation |
| 723 | Gamelin, Shaun | JOL_SLA | Four-Seam | 395 | 43.7 | 0.240 | 20.2 | 10.1 | 2109 | 90.1 | 4.88 | Soft-Speed Separation |
| 724 | Wehrle, Tyler | WIN_CIT29 | Changeup | 65 | 43.7 | 0.267 | 6.4 | 15.8 | 1898 | 84.2 | 5.56 | Soft-Speed Separation |
| 725 | Blair, Davis | DOW_EAS1 | Four-Seam | 204 | 43.6 | 0.238 | 16.6 | 8.1 | 2084 | 91.7 | 5.59 | Soft-Speed Separation |
| 726 | Hernandez, Nyan | NEW_JER6 | Sinker | 101 | 43.6 | 0.258 | 14.4 | 16.6 | 2090 | 88.6 | 6.43 | Soft-Speed Separation |
| 727 | Lockhart, Gauge | LAK_ERI24 | Sinker | 56 | 43.6 | 0.302 | 8.4 | 14.7 | 1980 | 89.3 | 6.36 | Soft-Speed Separation |
| 728 | Maher, Adam | TRI_VAL | Changeup | 78 | 43.6 | 0.278 | 11.8 | -10.8 | 1859 | 81.1 | 6.10 | Soft-Speed Separation |
| 729 | Snyder, Jack | SCH_BOO | Four-Seam | 113 | 43.6 | 0.281 | 16.8 | 5.3 | 2428 | 90.3 | 5.79 | Soft-Speed Separation |
| 730 | Zaffiro, Cole | SCH_BOO | Changeup | 65 | 43.5 | 0.256 | 4.4 | 16.2 | 1770 | 80.3 | 5.91 | Soft-Speed Separation |
| 731 | Barker, Alex | NEW_YOR13 | Four-Seam | 256 | 43.5 | 0.270 | 15.6 | -8.0 | 2171 | 87.4 | 6.29 | Soft-Speed Separation |
| 732 | Kemlage, Joe | NEW_ENG23 | Sinker | 187 | 43.5 | 0.273 | 8.4 | -15.4 | 2429 | 91.0 | 5.87 | Soft-Speed Separation |
| 733 | Jones, Logan | FLO_Y'A | Sinker | 96 | 43.3 | 0.237 | 10.9 | 17.9 | 2212 | 89.6 | 5.24 | Soft-Speed Separation |
| 734 | Fowler, Dalton | SUS_COU1 | Sinker | 51 | 43.3 | 0.284 | 11.3 | -12.9 | 2160 | 91.4 | 5.54 | Soft-Speed Separation |
| 735 | Vega, Lucas | TRO_AIG | Sinker | 257 | 43.2 | 0.252 | 9.1 | 14.6 | 2018 | 89.6 | 6.10 | Soft-Speed Separation |
| 736 | Bradford, Ethan | NEW_YOR13 | Sinker | 252 | 43.1 | 0.255 | 6.9 | -15.8 | 2188 | 90.0 | 5.70 | Soft-Speed Separation |
| 737 | Leak, Anthony | NEW_YOR13 | Four-Seam | 171 | 43.1 | 0.223 | 17.5 | 10.2 | 2227 | 90.7 | 6.17 | Soft-Speed Separation |
| 738 | Lovell, Justin | WIN_CIT29 | Four-Seam | 186 | 43.1 | 0.253 | 15.0 | -12.9 | 2306 | 93.4 | 6.29 | Soft-Speed Separation |
| 739 | Morrissey, Joe | EVA_OTT | Four-Seam | 169 | 43.1 | 0.250 | 19.7 | 11.1 | 2365 | 89.7 | 5.76 | Soft-Speed Separation |
| 740 | Lefebvre, Charles | TRO_AIG | Four-Seam | 63 | 43.1 | 0.251 | 16.1 | 12.1 | 2256 | 89.8 | 6.39 | Soft-Speed Separation |
| 741 | Simone, Andrew | TRO_AIG | Four-Seam | 206 | 43.1 | 0.253 | 16.0 | 8.7 | 1947 | 91.2 | 6.04 | Soft-Speed Separation |
| 742 | Moore, Kyle | SCH_BOO | Sinker | 90 | 43.0 | 0.300 | 14.6 | 15.2 | 2160 | 87.6 | 4.72 | Soft-Speed Separation |
| 743 | Valdez, Alex | EVA_OTT | Four-Seam | 201 | 42.9 | 0.251 | 13.1 | 5.8 | 2159 | 91.6 | 5.95 | Soft-Speed Separation |
| 744 | Noriega, Branden | LAK_ERI24 | Four-Seam | 186 | 42.9 | 0.239 | 15.2 | -14.6 | 2239 | 90.8 | 5.96 | Soft-Speed Separation |
| 745 | Sanchez, Edwin | LAK_ERI24 | Sinker | 255 | 42.8 | 0.254 | 15.6 | -13.7 | 2121 | 87.4 | 5.95 | Soft-Speed Separation |
| 746 | Bargo, Casey | FLO_Y'A | Changeup | 53 | 42.7 | 0.267 | 5.1 | 12.1 | 1489 | 83.0 | 6.12 | Soft-Speed Separation |
| 747 | Milburn, Isaac | FLO_Y'A | Four-Seam | 250 | 42.7 | 0.258 | 11.8 | -9.3 | 2089 | 87.7 | 5.53 | Soft-Speed Separation |
| 748 | Leach, Landon | TRO_AIG | Sinker | 79 | 42.7 | 0.281 | 9.5 | 11.5 | 1925 | 91.6 | 5.71 | Soft-Speed Separation |
| 749 | Soto, Noel | TRI_VAL | Four-Seam | 51 | 42.7 | 0.283 | 18.8 | 11.0 | 2096 | 87.8 | 5.59 | Soft-Speed Separation |
| 750 | Austin, Zack | SUS_COU1 | Four-Seam | 179 | 42.6 | 0.246 | 16.1 | 6.4 | 2287 | 91.6 | 5.89 | Soft-Speed Separation |
| 751 | Duncan, Tanner | DOW_EAS1 | Four-Seam | 197 | 42.6 | 0.272 | 16.0 | 8.9 | 2287 | 93.9 | 5.87 | Soft-Speed Separation |
| 752 | Villers, Ian | QUE_CAP | Four-Seam | 162 | 42.6 | 0.274 | 17.9 | 11.9 | 2261 | 93.4 | 6.11 | Soft-Speed Separation |
| 753 | Whitesell, Max | FLO_Y'A | Sinker | 79 | 42.6 | 0.275 | 12.4 | 13.9 | 1920 | 89.4 | 6.33 | Soft-Speed Separation |
| 754 | Nakata, Yuto | QUE_CAP | Splitter | 114 | 42.6 | 0.297 | 3.0 | 6.7 | 1012 | 84.1 | 5.49 | Soft-Speed Separation |
| 755 | Long, Maddox | WAS_WIL3 | Changeup | 61 | 42.5 | 0.281 | 7.9 | 15.7 | 1932 | 84.2 | 5.97 | Soft-Speed Separation |
| 756 | Matos, Dwayne | OTT_TIT | Changeup | 235 | 42.4 | 0.251 | 3.6 | 15.9 | 1525 | 84.0 | 6.38 | Soft-Speed Separation |
| 757 | Coles, Chad | WAS_WIL3 | Four-Seam | 239 | 42.4 | 0.259 | 17.9 | 9.8 | 2391 | 93.2 | 5.80 | Soft-Speed Separation |
| 758 | Salata, Derek | SCH_BOO | Four-Seam | 539 | 42.4 | 0.255 | 16.3 | 4.5 | 2317 | 89.5 | 6.20 | Soft-Speed Separation |
| 759 | Harris, Ben | GAT_GRI | Four-Seam | 532 | 42.3 | 0.265 | 17.1 | 8.5 | 2352 | 91.0 | 5.90 | Soft-Speed Separation |
| 760 | Allemann, Braeden | QUE_CAP | Four-Seam | 651 | 42.3 | 0.258 | 18.8 | 12.7 | 2342 | 91.1 | 6.35 | Soft-Speed Separation |
| 761 | Reeves, Cobe | NEW_YOR13 | Four-Seam | 51 | 42.3 | 0.251 | 13.0 | -9.2 | 1965 | 90.7 | 5.86 | Soft-Speed Separation |
| 762 | Jensik, CJ | WIN_CIT29 | Sinker | 62 | 42.2 | 0.256 | 8.4 | 15.2 | 2079 | 92.5 | 5.78 | Soft-Speed Separation |
| 763 | Grounds, Jackson | TRO_AIG | Sinker | 67 | 41.8 | 0.276 | 13.5 | 14.1 | 2152 | 92.1 | 5.74 | Soft-Speed Separation |
| 764 | Willeman, Landon | EVA_OTT | Four-Seam | 554 | 41.7 | 0.262 | 18.5 | 12.6 | 2204 | 90.8 | 5.84 | Soft-Speed Separation |
| 765 | Gartland, Chad | TRI_VAL | Sinker | 63 | 41.7 | 0.290 | 12.8 | 12.0 | 2061 | 88.4 | 6.13 | Soft-Speed Separation |
| 766 | Williams, Pierce | NEW_ENG23 | Sinker | 83 | 41.7 | 0.273 | 12.3 | -14.2 | 1870 | 85.8 | 6.13 | Soft-Speed Separation |
| 767 | Bell, Brendan | NEW_ENG23 | Changeup | 56 | 41.5 | 0.249 | 7.3 | 15.4 | 1950 | 82.7 | 5.16 | Soft-Speed Separation |
| 768 | Hicks, Jackson | DOW_EAS1 | Four-Seam | 72 | 41.5 | 0.279 | 17.9 | 12.2 | 2119 | 86.5 | 5.41 | Soft-Speed Separation |
| 769 | Hohenstein, Liam | WIN_CIT29 | Four-Seam | 195 | 41.4 | 0.265 | 17.3 | 4.3 | 1933 | 88.0 | 5.86 | Soft-Speed Separation |
| 770 | Figueredo, Kevin | WIN_CIT29 | Sinker | 209 | 41.3 | 0.271 | 12.1 | -14.4 | 2017 | 88.1 | 5.39 | Soft-Speed Separation |
| 771 | Savinon, Jordan | NEW_YOR13 | Four-Seam | 56 | 41.3 | 0.243 | 17.8 | -8.6 | 2173 | 89.1 | 5.71 | Soft-Speed Separation |
| 772 | Correa, Nelvin | QUE_CAP | Changeup | 74 | 41.3 | 0.269 | 10.8 | 13.9 | 1985 | 84.6 | 6.02 | Soft-Speed Separation |
| 773 | Gordillo, Lucas | TRI_VAL | Four-Seam | 247 | 41.1 | 0.291 | 16.9 | 9.9 | 2102 | 90.9 | 6.19 | Soft-Speed Separation |
| 774 | Anderson, Nathan | EVA_OTT | Four-Seam | 52 | 41.0 | 0.289 | 16.3 | 10.3 | 2267 | 90.5 | 6.39 | Soft-Speed Separation |
| 775 | Brito, Richard | NEW_ENG23 | Four-Seam | 61 | 41.0 | 0.295 | 16.3 | 11.3 | 2385 | 93.5 | 6.54 | Soft-Speed Separation |
| 776 | Harper, Scott | NEW_YOR13 | Sinker | 226 | 41.0 | 0.271 | 3.4 | 19.3 | 2287 | 89.2 | 6.25 | Soft-Speed Separation |
| 777 | Campbell, AJ | WIN_CIT29 | Four-Seam | 440 | 41.0 | 0.274 | 11.4 | 7.9 | 2414 | 88.2 | 5.47 | Soft-Speed Separation |
| 778 | Lefebvre, Charles | TRO_AIG | Changeup | 115 | 40.9 | 0.274 | 5.8 | 14.7 | 1613 | 82.6 | 6.69 | Soft-Speed Separation |
| 779 | Kaftan, Eddie | FLO_Y'A | Sinker | 128 | 40.8 | 0.263 | 7.4 | 13.6 | 2035 | 86.0 | 5.43 | Soft-Speed Separation |
| 780 | Hill, Kaleb | OTT_TIT | Sinker | 424 | 40.8 | 0.277 | 10.5 | -15.5 | 1877 | 89.8 | 5.54 | Soft-Speed Separation |
| 781 | Jones, Breyln | NEW_JER6 | Cutter | 72 | 40.8 | 0.282 | 8.5 | -0.1 | 2061 | 87.2 | 5.85 | Soft-Speed Separation |
| 782 | Townes, Holland | SCH_BOO | Sinker | 103 | 40.8 | 0.260 | 13.0 | 15.5 | 2245 | 92.2 | 5.20 | Soft-Speed Separation |
| 783 | Elliott, Eric | MIS_MUD | Four-Seam | 127 | 40.7 | 0.238 | 21.2 | -3.9 | 2228 | 87.2 | 6.24 | Soft-Speed Separation |
| 784 | Wiltse, Ryan | EVA_OTT | Four-Seam | 539 | 40.6 | 0.257 | 20.4 | 9.9 | 2163 | 87.2 | 6.06 | Soft-Speed Separation |
| 785 | Perez, Kelvin | WAS_WIL3 | Sinker | 109 | 40.5 | 0.301 | 9.6 | 14.0 | 2030 | 89.0 | 6.01 | Soft-Speed Separation |
| 786 | Pindel, Buddie | SCH_BOO | Sinker | 195 | 40.5 | 0.280 | 13.8 | 14.6 | 2135 | 89.9 | 5.69 | Soft-Speed Separation |
| 787 | Nova, Fraynel | LAK_ERI24 | Sinker | 132 | 40.4 | 0.279 | 9.1 | 13.3 | 2045 | 90.1 | 6.08 | Soft-Speed Separation |
| 788 | Williams, Brian | MIS_MUD | Four-Seam | 606 | 40.4 | 0.261 | 17.8 | 8.3 | 2250 | 89.3 | 6.34 | Soft-Speed Separation |
| 789 | Smith, Donny | JOL_SLA | Four-Seam | 52 | 40.3 | 0.290 | 15.1 | 11.0 | 2198 | 88.1 | 5.87 | Soft-Speed Separation |
| 790 | Trizuto, Colin | WAG_SEA | Changeup | 69 | 40.3 | 0.269 | 7.0 | 18.5 | 1961 | 84.0 | 5.35 | Soft-Speed Separation |
| 791 | Barreto, Brayhans | TRI_VAL | Four-Seam | 132 | 40.3 | 0.280 | 15.5 | -9.2 | 2036 | 88.6 | 6.18 | Soft-Speed Separation |
| 792 | Walsh, John | MIS_MUD | Four-Seam | 91 | 40.2 | 0.238 | 13.1 | -11.8 | 1911 | 84.5 | 5.64 | Soft-Speed Separation |
| 793 | Phelps, Travis | FLO_Y'A | Four-Seam | 53 | 40.2 | 0.283 | 13.7 | 5.1 | 2092 | 90.6 | 6.64 | Soft-Speed Separation |
| 794 | Estrella, Noah | TRI_VAL | Four-Seam | 247 | 40.2 | 0.253 | 17.2 | 12.7 | 2251 | 92.9 | 5.86 | Soft-Speed Separation |
| 795 | Delongchamp, Luke | TRI_VAL | Sinker | 113 | 40.2 | 0.282 | 11.5 | 17.2 | 2039 | 87.0 | 5.70 | Soft-Speed Separation |
| 796 | Parsons, Billy | SUS_COU1 | Sinker | 61 | 40.2 | 0.257 | 13.0 | 9.8 | 2277 | 89.4 | 5.78 | Soft-Speed Separation |
| 797 | Serratos, Oscar | WIN_CIT29 | Four-Seam | 81 | 40.1 | 0.277 | 13.0 | 10.1 | 2204 | 91.7 | 5.61 | Soft-Speed Separation |
| 798 | Drakeford, Dosie | NEW_JER6 | Four-Seam | 130 | 40.1 | 0.252 | 19.1 | 10.1 | 2340 | 91.4 | 5.83 | Soft-Speed Separation |
| 799 | Chapple, Bronson | TRO_AIG | Four-Seam | 95 | 40.1 | 0.294 | 11.2 | 8.8 | 2129 | 90.2 | 6.67 | Soft-Speed Separation |
| 800 | Belton, Hunter | MIS_MUD | Four-Seam | 129 | 39.9 | 0.296 | 13.0 | 10.6 | 2231 | 86.4 | 6.13 | Soft-Speed Separation |
| 801 | Thompson, Ross | SCH_BOO | Four-Seam | 464 | 39.7 | 0.262 | 16.0 | 12.0 | 2054 | 89.1 | 5.74 | Soft-Speed Separation |
| 802 | Thiels, Brenton | MIS_MUD | Cutter | 51 | 39.7 | 0.313 | 9.4 | 4.5 | 2311 | 86.3 | 6.84 | Soft-Speed Separation |
| 803 | Bice, Emmett | NEW_YOR13 | Four-Seam | 201 | 39.5 | 0.280 | 15.5 | 7.4 | 2231 | 89.1 | 5.90 | Soft-Speed Separation |
| 804 | Steinhauer, Ryan | NEW_JER6 | Changeup | 93 | 39.4 | 0.259 | 10.8 | -12.5 | 1665 | 82.3 | 6.31 | Soft-Speed Separation |
| 805 | Gartland, Chad | TRI_VAL | Four-Seam | 142 | 39.4 | 0.260 | 15.0 | 9.3 | 2081 | 89.2 | 6.18 | Soft-Speed Separation |
| 806 | Sohosky, Zac | MIA_RED | Four-Seam | 58 | 39.3 | 0.271 | 14.3 | -7.5 | 1888 | 88.4 | 6.33 | Soft-Speed Separation |
| 807 | Voytko, Fawster | TRO_AIG | Four-Seam | 166 | 39.3 | 0.287 | 15.6 | 5.4 | 2160 | 89.3 | 6.75 | Soft-Speed Separation |
| 808 | Masick, Jason | NEW_YOR13 | Four-Seam | 87 | 39.3 | 0.278 | 14.6 | 7.9 | 2127 | 94.2 | 6.09 | Soft-Speed Separation |
| 809 | Frey, Hayden | TOL_ROC | Four-Seam | 55 | 39.3 | 0.320 | 9.7 | -17.4 | 2137 | 88.8 | 6.37 | Soft-Speed Separation |
| 810 | Peters, Andrew | NEW_JER6 | Four-Seam | 299 | 39.3 | 0.278 | 15.3 | 7.8 | 2240 | 93.2 | 6.66 | Soft-Speed Separation |
| 811 | Maryniak, Connor | NEW_JER6 | Four-Seam | 134 | 39.3 | 0.258 | 13.2 | 7.2 | 2453 | 89.9 | 5.77 | Soft-Speed Separation |
| 812 | Pindel, Buddie | SCH_BOO | Changeup | 124 | 39.1 | 0.283 | 3.5 | 11.6 | 1379 | 80.9 | 5.50 | Soft-Speed Separation |
| 813 | Rivera, Matthew | NEW_ENG23 | Four-Seam | 143 | 39.1 | 0.259 | 17.9 | 8.9 | 2393 | 88.2 | 6.42 | Soft-Speed Separation |
| 814 | Gregory, Ben | GAT_GRI | Changeup | 76 | 39.1 | 0.278 | 9.1 | 13.6 | 1914 | 82.1 | 6.54 | Soft-Speed Separation |
| 815 | Morel, Yohanse | OTT_TIT | Sinker | 242 | 38.8 | 0.300 | 9.0 | 18.6 | 2256 | 91.1 | 5.26 | Soft-Speed Separation |
| 816 | Hickey, Matt | GAT_GRI | Four-Seam | 91 | 38.7 | 0.265 | 16.0 | 11.6 | 2304 | 89.9 | 5.52 | Soft-Speed Separation |
| 817 | Carroll, Jake | JOL_SLA | Four-Seam | 265 | 38.5 | 0.282 | 17.7 | -6.5 | 2143 | 86.3 | 7.05 | Soft-Speed Separation |
| 818 | Sanchez, Dikember | LAK_ERI24 | Four-Seam | 131 | 38.2 | 0.277 | 11.7 | 7.8 | 2279 | 91.3 | 5.77 | Soft-Speed Separation |
| 819 | Glickstein, Aaron | SCH_BOO | Cutter | 65 | 38.2 | 0.247 | 9.6 | 0.8 | 2247 | 85.5 | 5.64 | Soft-Speed Separation |
| 820 | Oe, Ryoya | OTT_TIT | Four-Seam | 58 | 38.2 | 0.282 | 18.1 | -3.8 | 2125 | 84.6 | 5.70 | Soft-Speed Separation |
| 821 | Chapple, Bronson | TRO_AIG | Sinker | 128 | 38.1 | 0.290 | 7.5 | 13.4 | 2067 | 90.5 | 6.50 | Soft-Speed Separation |
| 822 | Lawson, Nathan | FLO_Y'A | Four-Seam | 90 | 38.0 | 0.304 | 14.4 | 8.5 | 2239 | 88.8 | 6.10 | Soft-Speed Separation |
| 823 | Martinez, Mason | TRI_VAL | Changeup | 76 | 37.9 | 0.284 | 8.2 | 17.5 | 2180 | 82.3 | 6.67 | Soft-Speed Separation |
| 824 | Donnan, Blake | FLO_Y'A | Sinker | 170 | 37.9 | 0.294 | 6.6 | 17.4 | 1978 | 90.7 | 5.86 | Soft-Speed Separation |
| 825 | Rodriguez, Joe Joe | NEW_JER6 | Sinker | 225 | 37.8 | 0.277 | 13.3 | 15.4 | 2088 | 91.7 | 5.74 | Soft-Speed Separation |
| 826 | Baker, Luke | EVA_OTT | Four-Seam | 87 | 37.7 | 0.308 | 14.2 | -10.6 | 2426 | 87.1 | 5.86 | Soft-Speed Separation |
| 827 | Rodriguez, Esteban | WAS_WIL3 | Four-Seam | 167 | 37.6 | 0.289 | 17.0 | 4.4 | 2187 | 87.9 | 5.97 | Soft-Speed Separation |
| 828 | Marynczak, Arlo | TRI_VAL | Sinker | 87 | 37.5 | 0.281 | 14.5 | 13.2 | 2114 | 88.7 | 6.39 | Soft-Speed Separation |
| 829 | Nakata, Yuto | QUE_CAP | Four-Seam | 257 | 37.4 | 0.288 | 15.8 | 9.8 | 2085 | 92.5 | 5.79 | Soft-Speed Separation |
| 830 | Eldred, Zach | NEW_ENG23 | Splitter | 81 | 37.3 | 0.308 | 5.1 | 4.2 | 967 | 84.2 | 6.09 | Soft-Speed Separation |
| 831 | Kramer, Cameron | TRO_AIG | Four-Seam | 106 | 37.3 | 0.271 | 17.5 | 5.2 | 2191 | 89.6 | 5.92 | Soft-Speed Separation |
| 832 | Matos, Dwayne | OTT_TIT | Sinker | 342 | 37.3 | 0.286 | 11.6 | 18.5 | 2124 | 90.6 | 6.01 | Soft-Speed Separation |
| 833 | Thiels, Brenton | MIS_MUD | Four-Seam | 193 | 37.2 | 0.281 | 15.9 | 11.2 | 2254 | 89.4 | 6.78 | Soft-Speed Separation |
| 834 | Lovin, Xander | GAT_GRI | Four-Seam | 314 | 37.2 | 0.285 | 15.8 | 6.1 | 2312 | 91.3 | 4.97 | Soft-Speed Separation |
| 835 | Woolfolk, Dallas | SCH_BOO | Four-Seam | 101 | 37.2 | 0.238 | 19.4 | 13.4 | 2327 | 92.5 | 5.63 | Soft-Speed Separation |
| 836 | Reeves, Cobe | NEW_YOR13 | Changeup | 72 | 36.9 | 0.309 | 5.0 | -13.1 | 1385 | 84.3 | 6.35 | Soft-Speed Separation |
| 837 | Leduc, Zachary | TRO_AIG | Sinker | 87 | 36.8 | 0.287 | 11.6 | 15.9 | 2107 | 90.7 | 6.48 | Soft-Speed Separation |
| 838 | Sabatine, Gino | TRI_VAL | Changeup | 287 | 36.8 | 0.293 | 8.3 | 15.5 | 1784 | 85.1 | 5.07 | Soft-Speed Separation |
| 839 | Almonte, Dawil | EVA_OTT | Four-Seam | 142 | 36.7 | 0.296 | 11.2 | 9.4 | 2028 | 92.0 | 5.50 | Soft-Speed Separation |
| 840 | Gilleran, Jimmy | NEW_ENG23 | Four-Seam | 105 | 36.6 | 0.280 | 16.3 | 14.0 | 2165 | 88.5 | 5.65 | Soft-Speed Separation |
| 841 | Salata, Derek | SCH_BOO | Cutter | 139 | 36.6 | 0.307 | 11.6 | 0.2 | 2346 | 87.6 | 5.83 | Soft-Speed Separation |
| 842 | Tiburcio, David | DOW_EAS1 | Sinker | 188 | 36.6 | 0.286 | 11.8 | 17.6 | 2234 | 92.6 | 5.16 | Soft-Speed Separation |
| 843 | Grills, Evan | OTT_TIT | Four-Seam | 75 | 36.5 | 0.265 | 16.9 | -10.7 | 2210 | 88.2 | 5.46 | Soft-Speed Separation |
| 844 | Jones, Logan | TRI_VAL | Sinker | 109 | 36.4 | 0.287 | 12.1 | 17.9 | 2286 | 90.0 | 5.34 | Soft-Speed Separation |
| 845 | Biddinger, Tyler | WIN_CIT29 | Sinker | 168 | 36.3 | 0.301 | 7.6 | 16.8 | 2218 | 89.9 | 5.35 | Soft-Speed Separation |
| 846 | Manning, Noah | WIN_CIT29 | Sinker | 55 | 36.3 | 0.323 | 4.7 | 19.5 | 2312 | 90.7 | 5.51 | Soft-Speed Separation |
| 847 | Toribio, Noe | TRO_AIG | Sinker | 466 | 36.2 | 0.286 | 11.4 | 17.8 | 2025 | 90.2 | 5.77 | Soft-Speed Separation |
| 848 | Thiels, Brenton | MIS_MUD | Slider | 86 | 36.1 | 0.321 | 6.5 | 1.3 | 2273 | 83.2 | 6.72 | Soft-Speed Separation |
| 849 | Albert, Wes | DOW_EAS1 | Four-Seam | 54 | 36.0 | 0.264 | 17.1 | 8.1 | 1952 | 88.1 | 5.56 | Soft-Speed Separation |
| 850 | Burcham, Jacob | GAT_GRI | Four-Seam | 90 | 35.9 | 0.288 | 12.6 | 11.6 | 2345 | 92.3 | 6.34 | Soft-Speed Separation |
| 851 | Peters, Garrett | NEW_YOR13 | Sinker | 70 | 35.8 | 0.281 | 17.3 | -15.9 | 2197 | 85.9 | 5.93 | Soft-Speed Separation |
| 852 | Escobar, Anthony | TRO_AIG | Sinker | 161 | 35.7 | 0.334 | 13.0 | 13.5 | 2110 | 89.1 | 6.36 | Soft-Speed Separation |
| 853 | Harris, Ben | GAT_GRI | Sinker | 112 | 35.5 | 0.297 | 13.3 | 15.0 | 2243 | 90.3 | 5.90 | Soft-Speed Separation |
| 854 | Hampton, Ky | OTT_TIT | Sinker | 155 | 35.5 | 0.293 | 7.2 | 16.1 | 2145 | 88.4 | 6.21 | Soft-Speed Separation |
| 855 | Miner, Jace | DOW_EAS1 | Sinker | 115 | 35.4 | 0.307 | 6.4 | -12.0 | 1854 | 88.6 | 5.98 | Soft-Speed Separation |
| 856 | Sabatine, Gino | TRI_VAL | Four-Seam | 63 | 35.4 | 0.316 | 14.6 | 11.5 | 1846 | 88.6 | 5.02 | Soft-Speed Separation |
| 857 | Voytko, Fawster | TRO_AIG | Changeup | 73 | 35.3 | 0.247 | 11.8 | 12.4 | 1870 | 83.9 | 6.61 | Soft-Speed Separation |
| 858 | Linderman, Greyson | JOL_SLA | Sinker | 78 | 35.3 | 0.309 | 11.7 | 14.7 | 2120 | 93.8 | 5.46 | Soft-Speed Separation |
| 859 | Puccetti, Dominic | OTT_TIT | Changeup | 162 | 35.3 | 0.291 | 14.4 | -6.7 | 1711 | 84.2 | 5.42 | Soft-Speed Separation |
| 860 | Duby, Bill | NEW_JER6 | Splitter | 63 | 34.9 | 0.313 | 6.1 | 3.8 | 985 | 78.8 | 6.07 | Soft-Speed Separation |
| 861 | Gwin, Riley | QUE_CAP | Changeup | 52 | 34.8 | 0.293 | 13.0 | -10.7 | 1784 | 82.8 | 6.25 | Soft-Speed Separation |
| 862 | Cosentino, Nick | JOL_SLA | Four-Seam | 84 | 34.8 | 0.277 | 16.9 | 11.1 | 2220 | 90.5 | 5.48 | Soft-Speed Separation |
| 863 | Bell, Jacob | SCH_BOO | Four-Seam | 98 | 34.8 | 0.281 | 16.7 | 11.7 | 2325 | 87.1 | 6.10 | Soft-Speed Separation |
| 864 | O'Hanlon, Michael | WAS_WIL3 | Four-Seam | 148 | 34.4 | 0.322 | 15.9 | 10.8 | 2135 | 88.4 | 5.93 | Soft-Speed Separation |
| 865 | Heredia-Bustos, Rolando | DOW_EAS1 | Sinker | 135 | 34.3 | 0.272 | 13.4 | 16.8 | 2111 | 87.9 | 5.71 | Soft-Speed Separation |
| 866 | Thornton, Tyler | NEW_ENG23 | Changeup | 187 | 34.0 | 0.290 | 9.6 | 14.0 | 1820 | 83.5 | 4.94 | Soft-Speed Separation |
| 867 | Smith, Ben | NEW_ENG23 | Four-Seam | 89 | 33.7 | 0.281 | 10.4 | -10.2 | 2167 | 86.8 | 6.30 | Soft-Speed Separation |
| 868 | Nettleton, Blake | WIN_CIT29 | Four-Seam | 231 | 33.7 | 0.312 | 14.5 | 8.0 | 2139 | 89.5 | 6.49 | Soft-Speed Separation |
| 869 | McKillican, Adam | QUE_CAP | Four-Seam | 52 | 32.8 | 0.319 | 14.5 | 9.9 | 2042 | 88.7 | 6.70 | Soft-Speed Separation |
| 870 | Cox, Carter | NIU_HUS | Four-Seam | 75 | 32.3 | 0.297 | 14.5 | -7.5 | 2226 | 87.3 | 6.59 | Soft-Speed Separation |
| 871 | O'Brien, Keenan | SUS_COU1 | Sinker | 60 | 32.3 | 0.267 | 10.7 | 15.8 | 2090 | 90.2 | 5.79 | Soft-Speed Separation |
| 872 | Belton, Hunter | MIS_MUD | Changeup | 55 | 31.9 | 0.334 | 11.4 | 13.9 | 2006 | 81.0 | 6.10 | Soft-Speed Separation |
| 873 | Benitez, Jorge | NEW_JER6 | Four-Seam | 102 | 31.1 | 0.305 | 10.2 | -10.3 | 2151 | 93.3 | 6.00 | Soft-Speed Separation |
| 874 | Duby, Bill | NEW_JER6 | Changeup | 166 | 30.7 | 0.285 | 11.5 | 13.2 | 1947 | 83.8 | 6.61 | Soft-Speed Separation |
| 875 | Givens-Craig, Hayden | SUS_COU1 | Changeup | 85 | 30.6 | 0.330 | 7.9 | 11.6 | 1666 | 80.6 | 5.80 | Soft-Speed Separation |
| 876 | Rybarczyk, Ty | JOL_SLA | Four-Seam | 61 | 30.3 | 0.321 | 19.0 | 11.7 | 2309 | 91.3 | 5.50 | Soft-Speed Separation |
| 877 | Kramer, Cameron | TRO_AIG | Sinker | 69 | 30.1 | 0.282 | 13.1 | 16.0 | 2251 | 90.5 | 6.25 | Soft-Speed Separation |
| 878 | Beriguete, Randy | LAK_ERI24 | Four-Seam | 102 | 30.0 | 0.325 | 11.6 | 7.3 | 2284 | 93.3 | 6.47 | Soft-Speed Separation |
| 879 | Pardinho, Eric | OTT_TIT | Sinker | 73 | 29.1 | 0.321 | 15.0 | 15.2 | 2071 | 92.3 | 5.41 | Soft-Speed Separation |
| 880 | Gaskey, Blake | NIU_HUS | Four-Seam | 62 | 29.0 | 0.345 | 10.3 | 13.8 | 2190 | 85.0 | 6.73 | Soft-Speed Separation |
| 881 | Thornton, Tyler | NEW_ENG23 | Sinker | 121 | 28.9 | 0.325 | 9.7 | 14.8 | 1956 | 84.7 | 5.53 | Soft-Speed Separation |
| 882 | Foy, Corbin | LAK_ERI24 | Sinker | 57 | 28.3 | 0.333 | 11.4 | 13.2 | 2243 | 91.8 | 6.33 | Soft-Speed Separation |
| 883 | Andueza, Axel | DOW_EAS1 | Splitter | 96 | 28.3 | 0.336 | 3.4 | 7.9 | 900 | 81.7 | 5.19 | Soft-Speed Separation |
| 884 | Morse, Colby | EVA_OTT | Four-Seam | 54 | 27.0 | 0.282 | 16.5 | 9.2 | 2297 | 89.4 | 6.50 | Soft-Speed Separation |
| 885 | Smith, Ethan | WIN_CIT29 | Changeup | 52 | 26.6 | 0.317 | 9.1 | 14.6 | 2000 | 82.7 | 6.38 | Soft-Speed Separation |
| 886 | Miranda, Agnel | NEW_JER6 | Four-Seam | 50 | 26.4 | 0.276 | 15.6 | 9.8 | 2186 | 91.4 | 7.45 | Soft-Speed Separation |
| 887 | Smith, Donny | JOL_SLA | Sinker | 146 | 25.2 | 0.327 | 10.8 | 15.5 | 2124 | 88.8 | 5.76 | Soft-Speed Separation |
| 888 | Anderson, Colt | WAS_WIL3 | Changeup | 52 | 23.6 | 0.319 | 7.8 | -6.0 | 1500 | 79.2 | 6.51 | Soft-Speed Separation |
| 889 | Nabholz, Nate | TRI_VAL | Four-Seam | 99 | 20.0 | 0.356 | 18.5 | 10.3 | 2088 | 91.2 | 5.75 | Soft-Speed Separation |

## Undervalued Movement Pitches

Definition: movement quality percentile at least 75, with Pitch Value Score at or below league average.

| Rank | Pitcher | Team | Pitch | Pitches | PVS | xwOBA | IVB | HB | Spin | Velo | Ext | Archetype |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | Westcott, Zac | FLO_Y'A | Curveball | 163 | 20.3 | 0.376 | -15.2 | -9.2 | 1872 | 67.1 | 5.48 | Tight High-Spin Breakers |
| 2 | Huter, Blayne | SUS_COU1 | Curveball | 103 | 44.3 | 0.271 | -5.1 | -14.2 | 2137 | 73.7 | 6.01 | Tight High-Spin Breakers |
| 3 | Voytko, Fawster | TRO_AIG | Curveball | 75 | 33.6 | 0.319 | -7.1 | -11.8 | 2335 | 74.7 | 6.06 | Tight High-Spin Breakers |
| 4 | Plumadore, Carson | WIN_CIT29 | Curveball | 77 | 21.6 | 0.365 | 1.3 | -6.9 | 2483 | 75.4 | 5.57 | Tight High-Spin Breakers |
| 5 | Lawson, Nathan | FLO_Y'A | Curveball | 68 | 26.8 | 0.388 | -16.1 | -12.1 | 2374 | 74.1 | 5.56 | Tight High-Spin Breakers |
| 6 | Kassebaum, Torin | LON_ISL22 | Curveball | 55 | 39.6 | 0.307 | 1.1 | 10.2 | 2155 | 71.6 | 5.31 | Tight High-Spin Breakers |
| 7 | Brodsky, Jack | WAS_WIL3 | Curveball | 100 | 37.7 | 0.317 | -8.6 | -11.9 | 2662 | 76.6 | 5.45 | Tight High-Spin Breakers |
| 8 | Campbell, Tyler | MIS_MUD | Slider | 232 | 49.6 | 0.265 | 7.8 | 4.1 | 2204 | 74.2 | 5.73 | Tight High-Spin Breakers |
| 9 | Petery, Dylan | WIN_CIT29 | Slider | 59 | 45.7 | 0.222 | -0.6 | -12.2 | 2611 | 78.0 | 5.74 | Tight High-Spin Breakers |
| 10 | Johnston, Spencer | DOW_EAS1 | Curveball | 66 | 24.9 | 0.322 | -4.7 | -6.0 | 2133 | 74.4 | 5.68 | Tight High-Spin Breakers |
| 11 | Bice, Emmett | NEW_YOR13 | Curveball | 170 | 40.8 | 0.295 | -10.3 | -13.3 | 2986 | 79.1 | 5.51 | Tight High-Spin Breakers |
| 12 | Eldred, Zach | NEW_ENG23 | Curveball | 81 | 37.5 | 0.315 | -9.8 | -12.4 | 2489 | 77.6 | 5.88 | Tight High-Spin Breakers |
| 13 | Lovin, Xander | GAT_GRI | Curveball | 65 | 20.8 | 0.353 | -9.3 | -12.3 | 2634 | 76.9 | 4.64 | Tight High-Spin Breakers |
| 14 | Baker, Luke | EVA_OTT | Curveball | 59 | 47.4 | 0.244 | -7.4 | 9.7 | 2694 | 75.5 | 5.51 | Tight High-Spin Breakers |
| 15 | Voytko, Fawster | TRO_AIG | Slider | 60 | 25.3 | 0.323 | 0.9 | -11.4 | 2323 | 78.6 | 6.24 | Tight High-Spin Breakers |
| 16 | Good, Ty | GAT_GRI | Curveball | 167 | 41.0 | 0.272 | -7.8 | -4.6 | 2132 | 74.9 | 5.66 | Tight High-Spin Breakers |
| 17 | Kaftan, Eddie | FLO_Y'A | Slider | 62 | 47.9 | 0.234 | 1.1 | -6.3 | 2437 | 77.1 | 4.72 | Tight High-Spin Breakers |
| 18 | Villalobos, Jonaiker | FLO_Y'A | Curveball | 134 | 41.7 | 0.259 | -5.0 | 5.5 | 2265 | 74.8 | 5.33 | Tight High-Spin Breakers |
| 19 | Soto, Carlos | JOL_SLA | Slider | 102 | 37.8 | 0.302 | -1.6 | -8.8 | 2509 | 78.2 | 5.08 | Tight High-Spin Breakers |
| 20 | Anderson, Colt | WAS_WIL3 | Curveball | 67 | 42.6 | 0.270 | -11.1 | 9.9 | 2026 | 73.5 | 6.09 | Tight High-Spin Breakers |
| 21 | Sechrist, Zander | WAS_WIL3 | Changeup | 244 | 39.1 | 0.281 | 8.5 | -14.8 | 1694 | 77.0 | 5.75 | Tight High-Spin Breakers |
| 22 | Martzolf, Max | OTT_TIT | Curveball | 71 | 43.0 | 0.290 | -4.2 | 11.1 | 2155 | 73.9 | 5.43 | Tight High-Spin Breakers |
| 23 | Kostura, Brit | WAS_WIL3 | Slider | 60 | 41.5 | 0.272 | -0.6 | 5.1 | 2162 | 74.8 | 5.09 | Tight High-Spin Breakers |
| 24 | Misla, Luis | TRI_VAL | Curveball | 160 | 46.1 | 0.258 | -5.5 | 9.3 | 2791 | 77.0 | 5.12 | Tight High-Spin Breakers |
| 25 | Quigley, Michael | NEW_ENG23 | Curveball | 79 | 38.4 | 0.294 | -12.3 | -12.7 | 2567 | 78.8 | 5.42 | Tight High-Spin Breakers |
| 26 | Williams, Pierce | NEW_ENG23 | Curveball | 159 | 41.3 | 0.267 | -5.7 | 6.4 | 2173 | 75.3 | 5.78 | Tight High-Spin Breakers |
| 27 | Debban, Caleb | NEW_JER6 | Curveball | 206 | 45.8 | 0.276 | -7.2 | 18.6 | 2810 | 76.9 | 5.91 | Tight High-Spin Breakers |
| 28 | Figueredo, Kevin | WIN_CIT29 | Curveball | 78 | 44.0 | 0.278 | -3.5 | 4.9 | 2324 | 75.8 | 5.00 | Tight High-Spin Breakers |
| 29 | Turner, Eric | JOL_SLA | Slider | 221 | 48.0 | 0.248 | 1.4 | -7.7 | 2360 | 78.3 | 4.97 | Tight High-Spin Breakers |
| 30 | Smith, Donny | JOL_SLA | Slider | 66 | 43.3 | 0.244 | -2.4 | -5.4 | 2476 | 78.5 | 5.16 | Tight High-Spin Breakers |

## Top 20 Scouting Reports

1. **Grounds, Jackson, DOW_EAS1 Curveball** (Tight High-Spin Breakers): PVS 80.0, xwOBA 0.107. Shape: IVB -10.5, HB -12.0, 81.4 mph, 1946 rpm, 5.35 ft extension. Scouting read: low ride/drop, big horizontal; current results place it #1 overall and #1 within its pitch type.
2. **Vecerka, Boris, QUE_CAP Slider** (Tight High-Spin Breakers): PVS 80.0, xwOBA 0.123. Shape: IVB 2.4, HB -11.8, 82.5 mph, 2472 rpm, 5.64 ft extension. Scouting read: low ride/drop, big horizontal, high spin; current results place it #2 overall and #1 within its pitch type.
3. **Carroll, Jake, JOL_SLA Slider** (Tight High-Spin Breakers): PVS 80.0, xwOBA 0.177. Shape: IVB -5.7, HB 7.7, 75.4 mph, 2046 rpm, 6.09 ft extension. Scouting read: low ride/drop, soft velo; current results place it #3 overall and #2 within its pitch type.
4. **Ryan, Dillon, NEW_ENG23 Slider** (Tight High-Spin Breakers): PVS 79.9, xwOBA 0.144. Shape: IVB -2.0, HB -8.1, 85.4 mph, 2494 rpm, 5.82 ft extension. Scouting read: low ride/drop, high spin; current results place it #4 overall and #3 within its pitch type.
5. **Zentko, Dylan, EVA_OTT Changeup** (Tight High-Spin Breakers): PVS 78.5, xwOBA 0.155. Shape: IVB 7.3, HB -11.4, 78.8 mph, 1311 rpm, 5.82 ft extension. Scouting read: big horizontal, soft velo; current results place it #5 overall and #1 within its pitch type.
6. **Morgan, Cooper, QUE_CAP Curveball** (Tight High-Spin Breakers): PVS 78.0, xwOBA 0.149. Shape: IVB -1.4, HB 17.7, 75.6 mph, 2689 rpm, 5.28 ft extension. Scouting read: low ride/drop, big horizontal, high spin, soft velo; current results place it #6 overall and #2 within its pitch type.
7. **Peyton, Blake, GAT_GRI Changeup** (Tight High-Spin Breakers): PVS 77.2, xwOBA 0.140. Shape: IVB 10.3, HB -13.2, 81.0 mph, 1927 rpm, 6.10 ft extension. Scouting read: big horizontal; current results place it #7 overall and #2 within its pitch type.
8. **Alpern, Liam, FLO_Y'A Slider** (Tight High-Spin Breakers): PVS 76.3, xwOBA 0.112. Shape: IVB -4.0, HB 11.5, 76.8 mph, 2219 rpm, 5.55 ft extension. Scouting read: low ride/drop, big horizontal, soft velo; current results place it #8 overall and #4 within its pitch type.
9. **Serrano, Elio, NEW_JER6 Changeup** (Soft-Speed Separation): PVS 75.9, xwOBA 0.148. Shape: IVB 11.1, HB 11.7, 82.1 mph, 1829 rpm, 5.92 ft extension. Scouting read: big horizontal; current results place it #9 overall and #3 within its pitch type.
10. **Jones, Logan, TRI_VAL Slider** (Tight High-Spin Breakers): PVS 74.7, xwOBA 0.191. Shape: IVB 2.5, HB 2.3, 83.5 mph, 2341 rpm, 5.69 ft extension. Scouting read: low ride/drop, high spin; current results place it #10 overall and #5 within its pitch type.
11. **Bauer, Patrick, QUE_CAP Slider** (Tight High-Spin Breakers): PVS 74.4, xwOBA 0.170. Shape: IVB 0.1, HB -10.6, 77.6 mph, 2375 rpm, 6.00 ft extension. Scouting read: low ride/drop, big horizontal, high spin, soft velo; current results place it #11 overall and #6 within its pitch type.
12. **Grounds, Jackson, DOW_EAS1 Four-Seam** (Soft-Speed Separation): PVS 74.3, xwOBA 0.158. Shape: IVB 17.0, HB 14.2, 92.5 mph, 2163 rpm, 5.59 ft extension. Scouting read: plus ride, big horizontal, power velocity; current results place it #12 overall and #1 within its pitch type.
13. **Davis, Tyler, WIN_CIT29 Four-Seam** (Soft-Speed Separation): PVS 74.3, xwOBA 0.111. Shape: IVB 21.2, HB 5.6, 89.3 mph, 2171 rpm, 5.86 ft extension. Scouting read: plus ride, power velocity; current results place it #13 overall and #2 within its pitch type.
14. **Debban, Caleb, NEW_JER6 Four-Seam** (Soft-Speed Separation): PVS 73.7, xwOBA 0.173. Shape: IVB 13.1, HB -4.6, 87.2 mph, 2325 rpm, 6.58 ft extension. Scouting read: high spin, extension; current results place it #14 overall and #3 within its pitch type.
15. **Harper, Scott, NEW_YOR13 Slider** (Tight High-Spin Breakers): PVS 73.6, xwOBA 0.150. Shape: IVB 3.3, HB -16.7, 79.8 mph, 2669 rpm, 5.58 ft extension. Scouting read: big horizontal, high spin, soft velo; current results place it #15 overall and #7 within its pitch type.
16. **Garcia, Hector, WAS_WIL3 Splitter** (Soft-Speed Separation): PVS 73.6, xwOBA 0.184. Shape: IVB 11.7, HB 7.6, 78.2 mph, 1216 rpm, 5.92 ft extension. Scouting read: soft velo; current results place it #16 overall and #1 within its pitch type.
17. **Bargo, Casey, NEW_ENG23 Slider** (Tight High-Spin Breakers): PVS 73.5, xwOBA 0.176. Shape: IVB 1.5, HB -5.0, 83.6 mph, 2416 rpm, 5.66 ft extension. Scouting read: low ride/drop, high spin; current results place it #17 overall and #8 within its pitch type.
18. **McEvoy, Aidan, FLO_Y'A Slider** (Tight High-Spin Breakers): PVS 72.5, xwOBA 0.153. Shape: IVB 6.4, HB 10.3, 78.6 mph, 2223 rpm, 6.03 ft extension. Scouting read: big horizontal, soft velo; current results place it #18 overall and #9 within its pitch type.
19. **Lawson, Nathan, FLO_Y'A Changeup** (Soft-Speed Separation): PVS 72.4, xwOBA 0.194. Shape: IVB 8.2, HB 9.6, 79.6 mph, 1396 rpm, 5.77 ft extension. Scouting read: soft velo; current results place it #19 overall and #4 within its pitch type.
20. **Cameron, Zach, WIN_CIT29 Four-Seam** (Soft-Speed Separation): PVS 71.9, xwOBA 0.195. Shape: IVB 15.8, HB 10.2, 88.1 mph, 2170 rpm, 5.54 ft extension. Scouting read: plus ride, big horizontal; current results place it #20 overall and #4 within its pitch type.

## Plots

- `plots\pitch_movement_archetypes\cluster_count_selection.png`
- `plots\pitch_movement_archetypes\archetypes_hb_ivb.png`
- `plots\pitch_movement_archetypes\archetypes_velocity_spin.png`
- `plots\pitch_movement_archetypes\archetypes_pca.png`
- `plots\pitch_movement_archetypes\archetype_pitch_value.png`