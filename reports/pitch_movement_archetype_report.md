# Frontier League Movement Archetypes

- Input file: `data\processed\movement_score_inputs.csv`
- Scored output: `data\processed\pitch_movement_archetypes.csv`
- Cluster summary: `data\processed\pitch_movement_archetype_summary.csv`
- Highest-performing archetype pitch list: `data\processed\highest_performing_archetype_pitches.csv`
- Undervalued pitch list: `data\processed\undervalued_movement_pitches.csv`
- Qualified pitcher-pitch types clustered: 1,002
- Features clustered: IVB, HB, spin rate, velocity, extension
- Selected cluster count: 2
- Full methodology write-up: `reports/FRONTIER_PITCH_VALUE_METHODOLOGY.md`

## How To Read This Report

Higher Pitch Value Score is better. It means the pitch has the outcome profile associated with lower expected xwOBA damage. Archetypes are movement-shape groups, not direct pitcher grades.

The cluster labels describe the average movement identity of each group. Average Pitch Value Score by cluster tells us which movement families performed best in this dataset, but individual pitches within a cluster can still vary widely based on command, usage, sequencing, and sample size.

## Cluster Count Test

| k | Inertia | Silhouette |
|---:|---:|---:|
| 2 | 3425.90 | 0.3005 **selected** |
| 3 | 2761.99 | 0.2968 |
| 4 | 2285.82 | 0.2954 |
| 5 | 2085.91 | 0.2479 |
| 6 | 1900.19 | 0.2251 |
| 7 | 1747.35 | 0.2340 |
| 8 | 1630.99 | 0.2419 |
| 9 | 1519.40 | 0.2447 |
| 10 | 1418.95 | 0.2511 |

## Archetype Summary

| Rank | Archetype | Pitches | Instances | Avg PVS | Avg xwOBA | IVB | HB | Spin | Velo | Ext | Common Pitch Types |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|
| 1 | `Tight High-Spin Breakers` | 56,436 | 401 | 52.4 | 0.237 | 0.5 | -3.4 | 2259 | 79.9 | 5.50 | Slider, Curveball, Changeup |
| 2 | `Soft-Speed Separation` | 109,642 | 601 | 48.4 | 0.244 | 12.8 | 6.1 | 2088 | 88.1 | 5.97 | Four-Seam, Sinker, Changeup |

## Highest-Performing Archetypes

- `Tight High-Spin Breakers`: average PVS 52.4, avg xwOBA 0.237, typical shape 0.5 IVB / -3.4 HB at 79.9 mph.
- `Soft-Speed Separation`: average PVS 48.4, avg xwOBA 0.244, typical shape 12.8 IVB / 6.1 HB at 88.1 mph.

## Pitchers in Highest-Performing Archetypes

| Rank | Pitcher | Team | Pitch | Pitches | PVS | xwOBA | IVB | HB | Spin | Velo | Ext | Archetype |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | Grounds, Jackson | DOW_EAS1 | Curveball | 82 | 80.0 | 0.109 | -10.5 | -12.0 | 1946 | 81.4 | 5.35 | Tight High-Spin Breakers |
| 2 | Morrissey, Joe | EVA_OTT | Cutter | 62 | 80.0 | 0.113 | 12.5 | -3.2 | 2649 | 85.8 | 5.56 | Tight High-Spin Breakers |
| 3 | Vecerka, Boris | QUE_CAP | Slider | 83 | 80.0 | 0.123 | 2.4 | -11.8 | 2472 | 82.5 | 5.64 | Tight High-Spin Breakers |
| 4 | Carroll, Jake | JOL_SLA | Slider | 74 | 80.0 | 0.178 | -5.7 | 7.7 | 2046 | 75.4 | 6.09 | Tight High-Spin Breakers |
| 5 | Flontek, Zac | DOW_EAS1 | Slider | 76 | 80.0 | 0.089 | 2.8 | -3.5 | 2636 | 86.8 | 5.81 | Tight High-Spin Breakers |
| 6 | Ryan, Dillon | NEW_ENG23 | Slider | 149 | 79.6 | 0.145 | -2.2 | -8.5 | 2504 | 85.5 | 5.75 | Tight High-Spin Breakers |
| 7 | Morgan, Cooper | QUE_CAP | Curveball | 99 | 78.8 | 0.148 | -1.6 | 17.7 | 2699 | 75.6 | 5.31 | Tight High-Spin Breakers |
| 8 | Harley, Tristan | SUS_COU1 | Slider | 74 | 77.0 | 0.112 | 1.5 | -8.7 | 2432 | 81.3 | 5.64 | Tight High-Spin Breakers |
| 9 | Sanders, Brayden | MIS_MUD | Slider | 66 | 76.6 | 0.160 | 1.5 | -3.6 | 2010 | 82.0 | 4.58 | Tight High-Spin Breakers |
| 10 | Bauer, Patrick | QUE_CAP | Slider | 71 | 76.5 | 0.151 | 0.1 | -10.5 | 2416 | 78.0 | 6.06 | Tight High-Spin Breakers |
| 11 | Alpern, Liam | FLO_Y'A | Slider | 78 | 76.1 | 0.113 | -4.0 | 11.5 | 2219 | 76.8 | 5.55 | Tight High-Spin Breakers |
| 12 | Sparks, Alec | GAT_GRI | Curveball | 89 | 76.0 | 0.160 | -4.4 | -7.0 | 2566 | 77.6 | 5.37 | Tight High-Spin Breakers |
| 13 | Kramer, Cameron | TRO_AIG | Slider | 63 | 75.7 | 0.176 | 4.7 | -7.2 | 2184 | 81.0 | 5.55 | Tight High-Spin Breakers |
| 14 | Scafidi, Christian | LAK_ERI24 | Cutter | 52 | 74.4 | 0.147 | 6.2 | -0.2 | 2406 | 85.3 | 5.40 | Tight High-Spin Breakers |
| 15 | Jones, Logan | TRI_VAL | Slider | 65 | 74.3 | 0.190 | 2.5 | 2.3 | 2341 | 83.5 | 5.69 | Tight High-Spin Breakers |
| 16 | Bargo, Casey | NEW_ENG23 | Slider | 56 | 73.6 | 0.176 | 1.5 | -5.0 | 2416 | 83.6 | 5.66 | Tight High-Spin Breakers |
| 17 | Harper, Scott | NEW_YOR13 | Slider | 243 | 72.8 | 0.153 | 3.2 | -16.7 | 2664 | 79.7 | 5.58 | Tight High-Spin Breakers |
| 18 | McEvoy, Aidan | FLO_Y'A | Slider | 135 | 71.9 | 0.159 | 6.4 | 10.5 | 2223 | 78.4 | 6.04 | Tight High-Spin Breakers |
| 19 | Kirby, Zach | WAS_WIL3 | Slider | 127 | 71.6 | 0.156 | 5.8 | -13.4 | 2204 | 78.0 | 5.68 | Tight High-Spin Breakers |
| 20 | Peyton, Blake | GAT_GRI | Changeup | 108 | 70.8 | 0.159 | 10.7 | -13.4 | 1927 | 81.1 | 6.09 | Tight High-Spin Breakers |
| 21 | Majick, Eli | NEW_ENG23 | Cutter | 117 | 70.8 | 0.178 | 5.8 | -1.1 | 2491 | 83.1 | 5.71 | Tight High-Spin Breakers |
| 22 | Rodriguez, Ramon | WIN_CIT29 | Curveball | 119 | 69.9 | 0.173 | -0.1 | 8.6 | 2818 | 75.9 | 5.09 | Tight High-Spin Breakers |
| 23 | Bohnert, Matthew | WIN_CIT29 | Curveball | 124 | 69.9 | 0.163 | -16.2 | 13.4 | 2814 | 78.4 | 4.78 | Tight High-Spin Breakers |
| 24 | Donnan, Blake | FLO_Y'A | Slider | 65 | 69.7 | 0.184 | 5.0 | -7.3 | 2367 | 80.5 | 5.42 | Tight High-Spin Breakers |
| 25 | Pierson, Kenny | LAK_ERI24 | Curveball | 91 | 69.3 | 0.204 | -2.7 | 11.8 | 2026 | 70.1 | 4.54 | Tight High-Spin Breakers |
| 26 | Nakata, Yuto | QUE_CAP | Slider | 107 | 69.0 | 0.162 | 3.9 | -8.2 | 2427 | 81.7 | 5.60 | Tight High-Spin Breakers |
| 27 | Jones, Breyln | NEW_JER6 | Curveball | 60 | 68.5 | 0.186 | -17.0 | -9.7 | 2183 | 74.1 | 5.58 | Tight High-Spin Breakers |
| 28 | Parsons, Billy | SUS_COU1 | Changeup | 62 | 68.4 | 0.233 | 1.8 | 7.8 | 1431 | 80.9 | 5.49 | Tight High-Spin Breakers |
| 29 | Townes, Holland | SCH_BOO | Slider | 55 | 68.4 | 0.191 | 1.7 | -3.7 | 2128 | 83.1 | 5.26 | Tight High-Spin Breakers |
| 30 | MacMillan, Blake | TRO_AIG | Slider | 108 | 68.1 | 0.196 | 6.1 | -0.1 | 1925 | 79.5 | 5.32 | Tight High-Spin Breakers |
| 31 | Hickey, Matt | GAT_GRI | Slider | 112 | 67.9 | 0.204 | -1.9 | -6.7 | 2281 | 79.8 | 5.33 | Tight High-Spin Breakers |
| 32 | Balzan, Jackson | SUS_COU1 | Slider | 93 | 67.3 | 0.179 | 5.8 | 0.9 | 2187 | 79.8 | 5.26 | Tight High-Spin Breakers |
| 33 | Hohenstein, Liam | WIN_CIT29 | Curveball | 109 | 67.0 | 0.160 | -7.3 | -11.9 | 2585 | 75.8 | 5.35 | Tight High-Spin Breakers |
| 34 | Jones, Logan | FLO_Y'A | Slider | 82 | 66.7 | 0.176 | -3.1 | -2.6 | 2517 | 80.8 | 5.53 | Tight High-Spin Breakers |
| 35 | Marynczak, Arlo | TRI_VAL | Slider | 57 | 66.7 | 0.170 | 0.7 | -13.1 | 2321 | 77.9 | 5.63 | Tight High-Spin Breakers |
| 36 | Vega, Lucas | TRO_AIG | Slider | 134 | 66.7 | 0.155 | 6.6 | -9.3 | 2697 | 79.2 | 5.94 | Tight High-Spin Breakers |
| 37 | Tomczak, Anthony | EVA_OTT | Slider | 74 | 66.4 | 0.149 | 5.6 | -0.4 | 2069 | 83.8 | 5.71 | Tight High-Spin Breakers |
| 38 | Messina, Chris | FDU_KNI | Changeup | 68 | 66.4 | 0.253 | 11.9 | -18.0 | 1836 | 79.8 | 5.18 | Tight High-Spin Breakers |
| 39 | Binns, Malik | NEW_JER6 | Curveball | 55 | 66.2 | 0.184 | -7.6 | -16.2 | 2448 | 74.8 | 5.95 | Tight High-Spin Breakers |
| 40 | O'Dell, Casey | JOL_SLA | Slider | 61 | 66.1 | 0.168 | 0.3 | -5.1 | 2596 | 82.8 | 5.64 | Tight High-Spin Breakers |
| 41 | Heredia-Bustos, Rolando | DOW_EAS1 | Curveball | 75 | 66.0 | 0.177 | 5.6 | -11.0 | 2220 | 73.7 | 5.05 | Tight High-Spin Breakers |
| 42 | Campbell, Tyler | MIS_MUD | Changeup | 138 | 65.6 | 0.194 | 11.4 | -8.1 | 1851 | 74.7 | 6.32 | Tight High-Spin Breakers |
| 43 | Morin, Jacob | QUE_CAP | Slider | 85 | 65.6 | 0.205 | 7.4 | -6.2 | 2495 | 77.4 | 5.50 | Tight High-Spin Breakers |
| 44 | Shears, Tanner | SCH_BOO | Splitter | 78 | 65.2 | 0.197 | -1.8 | 6.7 | 910 | 82.0 | 5.07 | Tight High-Spin Breakers |
| 45 | Hickey, Matt | GAT_GRI | Curveball | 84 | 65.0 | 0.200 | -4.1 | -5.7 | 2254 | 79.7 | 5.45 | Tight High-Spin Breakers |
| 46 | Earwood, Micah | SUS_COU1 | Slider | 129 | 64.8 | 0.193 | 1.2 | -2.7 | 2326 | 78.9 | 5.69 | Tight High-Spin Breakers |
| 47 | Benitez, Jorge | NEW_JER6 | Slider | 108 | 64.5 | 0.186 | 4.2 | 15.5 | 2663 | 79.6 | 5.77 | Tight High-Spin Breakers |
| 48 | Petschke, Ben | EVA_OTT | Slider | 144 | 64.5 | 0.185 | -1.7 | -13.5 | 2628 | 81.1 | 5.04 | Tight High-Spin Breakers |
| 49 | Cerda, Junior | EVA_OTT | Sweeper | 53 | 64.2 | 0.178 | -3.2 | -11.9 | 2677 | 81.2 | 5.00 | Tight High-Spin Breakers |
| 50 | Barraza, Chris | MIS_MUD | Slider | 82 | 64.2 | 0.186 | 3.6 | -3.2 | 2317 | 84.1 | 5.27 | Tight High-Spin Breakers |
| 51 | Conklin, MacCallan | TRO_AIG | Curveball | 55 | 64.2 | 0.197 | -7.1 | -15.4 | 2745 | 78.4 | 5.97 | Tight High-Spin Breakers |
| 52 | Parsons, Billy | SUS_COU1 | Cutter | 68 | 64.1 | 0.172 | 9.7 | -2.8 | 2563 | 86.5 | 5.55 | Tight High-Spin Breakers |
| 53 | Eisenbarger, Jack | QUE_CAP | Curveball | 98 | 63.9 | 0.232 | -3.6 | 12.2 | 2801 | 77.3 | 5.25 | Tight High-Spin Breakers |
| 54 | Good, Ty | GAT_GRI | Slider | 228 | 63.6 | 0.191 | 3.7 | -0.4 | 2055 | 79.2 | 5.82 | Tight High-Spin Breakers |
| 55 | Widener, Jacob | SUS_COU1 | Slider | 101 | 63.4 | 0.215 | 3.3 | 16.7 | 2865 | 80.3 | 6.07 | Tight High-Spin Breakers |
| 56 | Salata, Derek | SCH_BOO | Curveball | 187 | 63.1 | 0.213 | -12.6 | -12.2 | 2571 | 74.1 | 5.55 | Tight High-Spin Breakers |
| 57 | Harris, Ben | GAT_GRI | Curveball | 324 | 63.1 | 0.215 | -14.2 | -7.0 | 2165 | 77.5 | 4.92 | Tight High-Spin Breakers |
| 58 | Smith, Ben | NEW_ENG23 | Changeup | 73 | 62.9 | 0.186 | 3.9 | -14.3 | 1567 | 82.5 | 5.99 | Tight High-Spin Breakers |
| 59 | Moore, Kyle | SCH_BOO | Slider | 106 | 62.2 | 0.219 | 6.8 | -1.6 | 2168 | 82.7 | 4.80 | Tight High-Spin Breakers |
| 60 | Garcia, Brett | OTT_TIT | Curveball | 153 | 62.1 | 0.193 | -17.5 | -8.4 | 2162 | 81.2 | 5.33 | Tight High-Spin Breakers |
| 61 | Pierson, Kenny | LAK_ERI24 | Slider | 122 | 62.1 | 0.206 | -1.0 | 7.2 | 2052 | 72.0 | 4.65 | Tight High-Spin Breakers |
| 62 | Morgan, Cooper | QUE_CAP | Changeup | 92 | 61.9 | 0.196 | 6.0 | -16.5 | 2000 | 82.2 | 5.92 | Tight High-Spin Breakers |
| 63 | Soto, Carlos | JOL_SLA | Splitter | 71 | 61.9 | 0.228 | 3.8 | 5.6 | 989 | 80.7 | 5.10 | Tight High-Spin Breakers |
| 64 | Perozzi, John | SUS_COU1 | Slider | 149 | 61.8 | 0.182 | 7.8 | -3.6 | 2411 | 83.5 | 5.91 | Tight High-Spin Breakers |
| 65 | Foster, Kobe | WAS_WIL3 | Slider | 149 | 61.7 | 0.187 | 5.2 | 5.2 | 2328 | 78.4 | 5.35 | Tight High-Spin Breakers |
| 66 | Baird, Dustin | MIS_MUD | Slider | 57 | 61.4 | 0.212 | 8.2 | -9.0 | 2365 | 81.3 | 5.87 | Tight High-Spin Breakers |
| 67 | Hampton, Ky | OTT_TIT | Curveball | 76 | 61.3 | 0.176 | -5.3 | -13.8 | 2227 | 81.7 | 5.54 | Tight High-Spin Breakers |
| 68 | Boies, Emiles | QUE_CAP | Curveball | 118 | 61.2 | 0.173 | -4.4 | -3.4 | 2203 | 77.0 | 5.63 | Tight High-Spin Breakers |
| 69 | Gollert, Harley | QUE_CAP | Slider | 57 | 61.2 | 0.214 | 1.0 | 5.1 | 2222 | 79.4 | 5.09 | Tight High-Spin Breakers |
| 70 | Hill, Kaleb | OTT_TIT | Curveball | 269 | 61.2 | 0.204 | -4.2 | 13.2 | 2161 | 73.4 | 5.35 | Tight High-Spin Breakers |
| 71 | Scafidi, Christian | LAK_ERI24 | Curveball | 61 | 61.2 | 0.193 | -6.9 | -2.8 | 2246 | 77.7 | 5.79 | Tight High-Spin Breakers |
| 72 | Morgan, Cooper | QUE_CAP | Slider | 74 | 61.1 | 0.212 | 3.1 | 10.7 | 2473 | 79.0 | 5.49 | Tight High-Spin Breakers |
| 73 | Morgan, Marcus | JOL_SLA | Cutter | 63 | 61.0 | 0.181 | 6.4 | -3.1 | 2670 | 86.9 | 5.76 | Tight High-Spin Breakers |
| 74 | Tokar, Heitor | OTT_TIT | Slider | 154 | 60.8 | 0.219 | 3.8 | -3.4 | 2105 | 81.9 | 5.90 | Tight High-Spin Breakers |
| 75 | Kostura, Brit | WAS_WIL3 | Curveball | 87 | 60.8 | 0.209 | -3.0 | 4.6 | 2169 | 74.2 | 5.35 | Tight High-Spin Breakers |
| 76 | Kemlage, Joe | NEW_ENG23 | Slider | 89 | 60.7 | 0.203 | -2.8 | 14.4 | 2608 | 82.2 | 5.52 | Tight High-Spin Breakers |
| 77 | Dill, Austin | TRI_VAL | Slider | 72 | 60.7 | 0.228 | 1.6 | -3.6 | 2565 | 79.3 | 4.97 | Tight High-Spin Breakers |
| 78 | Eisenbarger, Jack | QUE_CAP | Changeup | 227 | 60.5 | 0.192 | 14.3 | -14.5 | 2316 | 78.6 | 5.92 | Tight High-Spin Breakers |
| 79 | Cameron, Zach | WIN_CIT29 | Slider | 194 | 60.4 | 0.198 | 6.9 | -1.9 | 2363 | 81.8 | 5.43 | Tight High-Spin Breakers |
| 80 | Ronne, Andrew | GAT_GRI | Slider | 185 | 60.3 | 0.197 | -0.5 | -14.5 | 2602 | 81.3 | 5.91 | Tight High-Spin Breakers |
| 81 | Cook, Cole | SCH_BOO | Curveball | 132 | 60.1 | 0.224 | -3.8 | 6.0 | 2486 | 76.7 | 4.93 | Tight High-Spin Breakers |
| 82 | Harajli, Ahmad | FLO_Y'A | Slider | 76 | 60.1 | 0.190 | -2.5 | -2.9 | 2056 | 80.5 | 5.99 | Tight High-Spin Breakers |
| 83 | Cook, Cole | SCH_BOO | Slider | 278 | 60.0 | 0.221 | 3.1 | 4.6 | 2469 | 79.3 | 5.10 | Tight High-Spin Breakers |
| 84 | Leduc, Zachary | TRO_AIG | Slider | 116 | 60.0 | 0.171 | 1.7 | -4.6 | 2108 | 82.9 | 6.22 | Tight High-Spin Breakers |
| 85 | Foster, Kobe | WAS_WIL3 | Changeup | 219 | 59.9 | 0.214 | 15.9 | -14.1 | 1886 | 79.3 | 5.80 | Tight High-Spin Breakers |
| 86 | Hocom, Quinn | TRI_VAL | Curveball | 120 | 59.8 | 0.228 | -12.9 | -11.3 | 2376 | 77.1 | 5.48 | Tight High-Spin Breakers |
| 87 | Odonnell, Brendan | NEW_ENG23 | Slider | 264 | 59.8 | 0.212 | -1.2 | 12.2 | 2651 | 84.1 | 6.10 | Tight High-Spin Breakers |
| 88 | Ginn, Landon | WAS_WIL3 | Slider | 142 | 59.8 | 0.199 | 1.0 | -3.5 | 2878 | 85.8 | 5.35 | Tight High-Spin Breakers |
| 89 | Campbell, AJ | WIN_CIT29 | Curveball | 80 | 59.8 | 0.191 | -0.9 | -16.1 | 2587 | 75.2 | 4.85 | Tight High-Spin Breakers |
| 90 | Villers, Ian | QUE_CAP | Slider | 66 | 59.5 | 0.239 | -0.3 | -5.1 | 2117 | 82.3 | 5.94 | Tight High-Spin Breakers |
| 91 | Zaffiro, Cole | SCH_BOO | Curveball | 66 | 59.5 | 0.212 | -10.3 | -5.4 | 2048 | 79.2 | 5.73 | Tight High-Spin Breakers |
| 92 | Allemann, Braeden | QUE_CAP | Slider | 99 | 59.4 | 0.208 | 3.1 | -3.7 | 2257 | 83.2 | 6.20 | Tight High-Spin Breakers |
| 93 | Calderon, Jean | LAK_ERI24 | Slider | 73 | 59.2 | 0.197 | 1.3 | -9.7 | 2593 | 86.4 | 6.05 | Tight High-Spin Breakers |
| 94 | Langrell, Connor | MIS_MUD | Curveball | 156 | 59.1 | 0.216 | -15.8 | -11.1 | 2744 | 77.4 | 6.04 | Tight High-Spin Breakers |
| 95 | Langhorne, Miles | SUS_COU1 | Slider | 61 | 58.9 | 0.223 | 0.0 | -3.1 | 2487 | 86.8 | 5.90 | Tight High-Spin Breakers |
| 96 | Grills, Evan | OTT_TIT | Curveball | 130 | 58.9 | 0.271 | -13.1 | 10.2 | 2473 | 72.8 | 5.20 | Tight High-Spin Breakers |
| 97 | Scott, Brandon | LAK_ERI24 | Slider | 148 | 58.9 | 0.194 | -0.3 | 6.8 | 2401 | 77.9 | 5.41 | Tight High-Spin Breakers |
| 98 | Smith, Jackson | MIS_MUD | Slider | 140 | 58.8 | 0.210 | 1.7 | -9.2 | 2644 | 78.5 | 4.85 | Tight High-Spin Breakers |
| 99 | Long, Maddox | WAS_WIL3 | Slider | 226 | 58.8 | 0.197 | 2.8 | -8.6 | 2598 | 82.8 | 5.52 | Tight High-Spin Breakers |
| 100 | Townes, Holland | SCH_BOO | Curveball | 99 | 58.8 | 0.223 | -9.4 | -13.5 | 2322 | 78.4 | 4.93 | Tight High-Spin Breakers |
| 101 | Eckaus, David | EVA_OTT | Slider | 216 | 58.7 | 0.210 | 1.9 | 4.9 | 2604 | 82.3 | 5.54 | Tight High-Spin Breakers |
| 102 | Brito, Richard | NEW_ENG23 | Slider | 73 | 58.6 | 0.197 | 3.6 | -6.0 | 2287 | 81.7 | 6.09 | Tight High-Spin Breakers |
| 103 | Wiltse, Ryan | EVA_OTT | Curveball | 171 | 58.6 | 0.239 | -13.0 | -4.2 | 1930 | 73.9 | 5.82 | Tight High-Spin Breakers |
| 104 | Cohn, Cooper | NIU_HUS | Slider | 63 | 58.5 | 0.187 | -1.2 | -13.7 | 2534 | 78.9 | 5.40 | Tight High-Spin Breakers |
| 105 | Lefebvre, Charles | TRO_AIG | Curveball | 124 | 58.5 | 0.235 | -9.3 | -8.9 | 2479 | 77.4 | 6.11 | Tight High-Spin Breakers |
| 106 | Leak, Anthony | NEW_YOR13 | Slider | 325 | 58.5 | 0.183 | 4.7 | -6.5 | 2296 | 82.9 | 5.80 | Tight High-Spin Breakers |
| 107 | Vail, Tyler | NEW_YOR13 | Slider | 263 | 58.4 | 0.247 | 0.8 | -1.4 | 2271 | 80.7 | 5.91 | Tight High-Spin Breakers |
| 108 | Shinn, Nathan | LAK_ERI24 | Slider | 138 | 58.4 | 0.217 | 0.3 | 0.8 | 2179 | 82.1 | 5.24 | Tight High-Spin Breakers |
| 109 | Marklund, Brandon | OTT_TIT | Slider | 124 | 58.3 | 0.242 | 6.4 | -14.2 | 2707 | 79.6 | 4.87 | Tight High-Spin Breakers |
| 110 | Vail, Tyler | NEW_YOR13 | Curveball | 187 | 58.2 | 0.220 | -2.9 | -5.5 | 2224 | 74.8 | 5.73 | Tight High-Spin Breakers |
| 111 | Lodes, Jett | FLO_Y'A | Slider | 78 | 58.2 | 0.230 | 1.2 | -6.3 | 2544 | 81.0 | 5.16 | Tight High-Spin Breakers |
| 112 | Wilcenski, Blaise | WIN_CIT29 | Slider | 56 | 58.2 | 0.222 | 1.0 | -2.8 | 2145 | 80.2 | 5.88 | Tight High-Spin Breakers |
| 113 | Earwood, Micah | SUS_COU1 | Curveball | 234 | 58.2 | 0.242 | -3.3 | -4.7 | 2354 | 75.4 | 5.55 | Tight High-Spin Breakers |
| 114 | Andueza, Axel | DOW_EAS1 | Changeup | 116 | 58.0 | 0.228 | 5.5 | 11.4 | 2119 | 82.3 | 5.21 | Tight High-Spin Breakers |
| 115 | Long, Jalon | NEW_YOR13 | Slider | 201 | 57.9 | 0.230 | 4.7 | -1.9 | 2175 | 84.1 | 5.74 | Tight High-Spin Breakers |
| 116 | Garcia, Andrew | EVA_OTT | Slider | 227 | 57.7 | 0.195 | 2.2 | -7.2 | 2338 | 82.2 | 5.38 | Tight High-Spin Breakers |
| 117 | Hagan, Jack | DOW_EAS1 | Slider | 297 | 57.6 | 0.214 | 3.8 | -3.3 | 2439 | 84.6 | 5.69 | Tight High-Spin Breakers |
| 118 | Valdez, Alex | EVA_OTT | Cutter | 105 | 57.6 | 0.233 | 4.5 | -1.8 | 2065 | 86.4 | 5.36 | Tight High-Spin Breakers |
| 119 | Sanchez, Sergio | MIS_MUD | Slider | 104 | 57.6 | 0.240 | -1.6 | -3.7 | 2468 | 81.2 | 5.67 | Tight High-Spin Breakers |
| 120 | Majick, Eli | NEW_ENG23 | Slider | 288 | 57.4 | 0.224 | 4.0 | 8.4 | 2553 | 79.5 | 5.51 | Tight High-Spin Breakers |
| 121 | Dima, Josh | GAT_GRI | Slider | 143 | 57.3 | 0.206 | 2.6 | 2.1 | 1934 | 82.0 | 5.98 | Tight High-Spin Breakers |
| 122 | Vailes, Gage | GAT_GRI | Slider | 367 | 57.2 | 0.208 | 5.8 | -11.5 | 2556 | 81.6 | 4.56 | Tight High-Spin Breakers |
| 123 | Bauer, Patrick | QUE_CAP | Curveball | 137 | 57.2 | 0.233 | -12.4 | -14.5 | 2332 | 70.5 | 6.11 | Tight High-Spin Breakers |
| 124 | Garcia, Hector | WAS_WIL3 | Slider | 56 | 57.2 | 0.229 | 2.0 | -7.1 | 2355 | 77.3 | 5.72 | Tight High-Spin Breakers |
| 125 | Maher, Adam | TRI_VAL | Slider | 144 | 57.1 | 0.219 | 5.1 | 0.7 | 1886 | 79.3 | 5.71 | Tight High-Spin Breakers |
| 126 | Balzan, Jackson | SUS_COU1 | Curveball | 83 | 57.1 | 0.234 | -5.1 | 5.1 | 2104 | 76.1 | 5.12 | Tight High-Spin Breakers |
| 127 | Sparks, Alec | GAT_GRI | Slider | 214 | 57.0 | 0.200 | 0.7 | -7.0 | 2587 | 80.3 | 5.49 | Tight High-Spin Breakers |
| 128 | Grounds, Jackson | TRO_AIG | Curveball | 67 | 57.0 | 0.204 | -11.3 | -11.1 | 2036 | 81.9 | 5.55 | Tight High-Spin Breakers |
| 129 | Saturria, Michael | NEW_ENG23 | Slider | 272 | 56.9 | 0.207 | 4.0 | -7.0 | 2703 | 80.8 | 5.88 | Tight High-Spin Breakers |
| 130 | Correa, Nelvin | QUE_CAP | Slider | 201 | 56.9 | 0.201 | 4.4 | -7.0 | 2411 | 84.4 | 5.55 | Tight High-Spin Breakers |
| 131 | Petschke, Ben | EVA_OTT | Curveball | 171 | 56.9 | 0.228 | -9.7 | -15.8 | 2768 | 77.2 | 4.96 | Tight High-Spin Breakers |
| 132 | Maryniak, Connor | NEW_JER6 | Curveball | 202 | 56.8 | 0.229 | -9.6 | -4.5 | 2514 | 81.3 | 4.77 | Tight High-Spin Breakers |
| 133 | Williams, Brian | MIS_MUD | Splitter | 126 | 56.8 | 0.204 | 2.7 | 4.9 | 1775 | 78.6 | 5.99 | Tight High-Spin Breakers |
| 134 | Rohde, Isaac | NEW_YOR13 | Changeup | 951 | 56.6 | 0.224 | 3.8 | -20.2 | 1988 | 76.4 | 6.22 | Tight High-Spin Breakers |
| 135 | Whitesell, Max | FLO_Y'A | Slider | 178 | 56.5 | 0.210 | 6.3 | -4.6 | 2066 | 80.3 | 6.32 | Tight High-Spin Breakers |
| 136 | Bice, Emmett | NEW_YOR13 | Slider | 314 | 56.5 | 0.231 | 2.1 | -2.5 | 2372 | 82.9 | 5.70 | Tight High-Spin Breakers |
| 137 | Sechrist, Zander | WAS_WIL3 | Slider | 90 | 56.4 | 0.220 | 3.4 | 6.9 | 1879 | 69.6 | 5.18 | Tight High-Spin Breakers |
| 138 | Kirby, Zach | WAS_WIL3 | Curveball | 105 | 56.4 | 0.231 | -18.3 | -10.7 | 2261 | 70.8 | 5.41 | Tight High-Spin Breakers |
| 139 | Harris, Everette | TRI_VAL | Slider | 59 | 56.3 | 0.214 | 1.1 | -8.3 | 2845 | 80.5 | 6.14 | Tight High-Spin Breakers |
| 140 | Morgan, Marcus | JOL_SLA | Slider | 66 | 56.2 | 0.212 | 7.0 | -9.2 | 2844 | 84.9 | 5.71 | Tight High-Spin Breakers |
| 141 | Morrissey, Joe | EVA_OTT | Slider | 71 | 56.1 | 0.235 | 2.0 | -13.3 | 2768 | 79.8 | 5.39 | Tight High-Spin Breakers |
| 142 | Allemann, Braeden | QUE_CAP | Curveball | 307 | 56.1 | 0.234 | -6.9 | -15.7 | 2201 | 77.1 | 6.14 | Tight High-Spin Breakers |
| 143 | Majick, Eli | NEW_ENG23 | Curveball | 70 | 55.9 | 0.206 | -1.0 | 5.0 | 2207 | 77.0 | 5.51 | Tight High-Spin Breakers |
| 144 | Gamelin, Shaun | JOL_SLA | Slider | 101 | 55.9 | 0.218 | 3.6 | -0.6 | 2286 | 82.2 | 4.78 | Tight High-Spin Breakers |
| 145 | Petschke, Ben | EVA_OTT | Sweeper | 62 | 55.8 | 0.234 | -2.7 | -17.1 | 2741 | 79.7 | 4.90 | Tight High-Spin Breakers |
| 146 | Gregory, Ben | GAT_GRI | Curveball | 62 | 55.8 | 0.260 | -7.0 | -6.0 | 2285 | 77.8 | 6.13 | Tight High-Spin Breakers |
| 147 | Masick, Jason | NEW_YOR13 | Slider | 62 | 55.7 | 0.216 | 3.2 | -4.7 | 2291 | 85.4 | 5.66 | Tight High-Spin Breakers |
| 148 | Helt, Robert | LAK_ERI24 | Slider | 233 | 55.7 | 0.225 | -1.2 | -5.1 | 2405 | 81.1 | 5.76 | Tight High-Spin Breakers |
| 149 | Zentko, Dylan | EVA_OTT | Slider | 94 | 55.4 | 0.225 | 4.3 | 0.9 | 1932 | 77.6 | 5.62 | Tight High-Spin Breakers |
| 150 | Heredia-Bustos, Rolando | DOW_EAS1 | Slider | 449 | 55.4 | 0.211 | 6.7 | -3.9 | 2321 | 78.5 | 5.26 | Tight High-Spin Breakers |
| 151 | Brothers, Kellen | SUS_COU1 | Curveball | 117 | 55.3 | 0.232 | -14.8 | -12.9 | 2240 | 74.2 | 5.84 | Tight High-Spin Breakers |
| 152 | Vitas, Ben | JOL_SLA | Splitter | 161 | 55.2 | 0.220 | -0.0 | 6.3 | 1042 | 81.3 | 4.93 | Tight High-Spin Breakers |
| 153 | Hocom, Quinn | TRI_VAL | Changeup | 126 | 55.1 | 0.225 | 6.6 | 17.0 | 1994 | 78.5 | 5.64 | Tight High-Spin Breakers |
| 154 | Valdez, Alex | EVA_OTT | Slider | 190 | 55.1 | 0.193 | 3.7 | -2.5 | 2143 | 86.0 | 5.33 | Tight High-Spin Breakers |
| 155 | Johnston, Spencer | DOW_EAS1 | Slider | 221 | 55.0 | 0.208 | 6.8 | 1.0 | 2085 | 78.5 | 5.99 | Tight High-Spin Breakers |
| 156 | Williams, Pierce | NEW_ENG23 | Changeup | 540 | 55.0 | 0.224 | 10.0 | -14.0 | 1786 | 79.3 | 5.95 | Tight High-Spin Breakers |
| 157 | Thornton, Tyler | NEW_ENG23 | Splitter | 146 | 54.9 | 0.244 | 4.7 | 11.2 | 966 | 77.4 | 4.77 | Tight High-Spin Breakers |
| 158 | Puccetti, Dominic | OTT_TIT | Curveball | 195 | 54.8 | 0.235 | -13.4 | 9.8 | 2685 | 73.5 | 5.29 | Tight High-Spin Breakers |
| 159 | Moore, Kyle | SCH_BOO | Cutter | 164 | 54.8 | 0.238 | 9.6 | 1.4 | 2126 | 84.2 | 4.69 | Tight High-Spin Breakers |
| 160 | Moore, Kyle | SCH_BOO | Curveball | 149 | 54.7 | 0.229 | -8.6 | -7.7 | 2521 | 76.9 | 4.14 | Tight High-Spin Breakers |
| 161 | Kines, Gunnar | JOL_SLA | Changeup | 373 | 54.7 | 0.230 | 12.1 | -12.6 | 1900 | 75.2 | 6.01 | Tight High-Spin Breakers |
| 162 | Floyd, Conner | QUE_CAP | Curveball | 67 | 54.6 | 0.233 | -3.3 | -16.5 | 2116 | 77.5 | 5.06 | Tight High-Spin Breakers |
| 163 | Gordillo, Lucas | TRI_VAL | Slider | 69 | 54.4 | 0.246 | 3.4 | -5.7 | 2012 | 80.6 | 5.59 | Tight High-Spin Breakers |
| 164 | O'Hanlon, Michael | WAS_WIL3 | Slider | 78 | 54.3 | 0.259 | 3.2 | -2.7 | 2509 | 83.6 | 5.40 | Tight High-Spin Breakers |
| 165 | Snyder, Jack | SCH_BOO | Slider | 104 | 54.1 | 0.241 | 4.5 | -5.5 | 2478 | 83.6 | 5.19 | Tight High-Spin Breakers |
| 166 | Nabholz, Nate | TRI_VAL | Slider | 98 | 54.0 | 0.218 | 6.4 | -1.6 | 1992 | 83.4 | 5.68 | Tight High-Spin Breakers |
| 167 | Helt, Robert | LAK_ERI24 | Curveball | 165 | 53.9 | 0.252 | -5.6 | -5.9 | 2380 | 79.0 | 5.79 | Tight High-Spin Breakers |
| 168 | Gamelin, Shaun | JOL_SLA | Cutter | 148 | 53.9 | 0.227 | 5.7 | -0.3 | 2313 | 84.0 | 5.06 | Tight High-Spin Breakers |
| 169 | Noriega, Branden | LAK_ERI24 | Curveball | 128 | 53.9 | 0.255 | -9.4 | 7.5 | 2847 | 79.3 | 5.27 | Tight High-Spin Breakers |
| 170 | Anibal, Trevor | NEW_ENG23 | Curveball | 120 | 53.8 | 0.246 | -15.2 | -9.3 | 2493 | 76.0 | 5.43 | Tight High-Spin Breakers |
| 171 | Long, Jalon | NEW_YOR13 | Curveball | 58 | 53.8 | 0.231 | -7.9 | -3.4 | 2335 | 75.7 | 5.52 | Tight High-Spin Breakers |
| 172 | DeCastro, Justin | LON_ISL22 | Changeup | 122 | 53.8 | 0.235 | 9.6 | 18.6 | 1979 | 79.4 | 5.06 | Tight High-Spin Breakers |
| 173 | Folkman, Max | WAS_WIL3 | Slider | 53 | 53.7 | 0.251 | 3.2 | 11.2 | 2213 | 72.7 | 5.67 | Tight High-Spin Breakers |
| 174 | Biddinger, Tyler | WIN_CIT29 | Slider | 123 | 53.7 | 0.211 | 0.1 | -11.9 | 2662 | 79.9 | 4.91 | Tight High-Spin Breakers |
| 175 | Sechrist, Zander | WAS_WIL3 | Curveball | 173 | 53.7 | 0.225 | 2.1 | 7.6 | 1859 | 67.7 | 5.33 | Tight High-Spin Breakers |
| 176 | Thebiay, Nolan | EVA_OTT | Slider | 61 | 53.6 | 0.253 | -0.7 | -1.1 | 1840 | 79.1 | 6.18 | Tight High-Spin Breakers |
| 177 | Campbell, AJ | WIN_CIT29 | Slider | 498 | 53.5 | 0.230 | 5.5 | -8.3 | 2558 | 80.4 | 4.93 | Tight High-Spin Breakers |
| 178 | Thompson, Ross | SCH_BOO | Slider | 283 | 53.4 | 0.222 | 3.2 | -2.2 | 2027 | 79.3 | 5.23 | Tight High-Spin Breakers |
| 179 | Rivera, Matthew | NEW_ENG23 | Curveball | 80 | 53.4 | 0.248 | -16.3 | -8.1 | 2202 | 73.9 | 5.64 | Tight High-Spin Breakers |
| 180 | Cerda, Junior | EVA_OTT | Slider | 171 | 53.4 | 0.223 | -2.0 | -7.2 | 2609 | 82.5 | 4.89 | Tight High-Spin Breakers |
| 181 | Oe, Ryoya | OTT_TIT | Curveball | 57 | 53.2 | 0.209 | -4.6 | 5.0 | 2303 | 73.3 | 4.90 | Tight High-Spin Breakers |
| 182 | Estrella, Noah | TRI_VAL | Slider | 207 | 53.2 | 0.211 | -2.8 | 0.6 | 2585 | 85.3 | 5.59 | Tight High-Spin Breakers |
| 183 | Turner, Eric | JOL_SLA | Changeup | 214 | 53.1 | 0.239 | 4.7 | 15.3 | 1668 | 79.6 | 5.11 | Tight High-Spin Breakers |
| 184 | Bihm, Gage | MIS_MUD | Slider | 86 | 53.1 | 0.242 | -2.4 | 10.1 | 2270 | 80.5 | 4.99 | Tight High-Spin Breakers |
| 185 | Woolfolk, Dallas | MIS_MUD | Slider | 109 | 52.9 | 0.259 | 0.4 | -1.3 | 2281 | 82.0 | 5.20 | Tight High-Spin Breakers |
| 186 | Zeplin, Blane | JOL_SLA | Slider | 108 | 52.9 | 0.211 | -0.7 | -6.9 | 2273 | 77.7 | 5.32 | Tight High-Spin Breakers |
| 187 | Plumadore, Carson | WIN_CIT29 | Slider | 139 | 52.8 | 0.206 | 2.6 | -4.8 | 2432 | 76.1 | 5.51 | Tight High-Spin Breakers |
| 188 | Milburn, Isaac | FLO_Y'A | Slider | 241 | 52.8 | 0.221 | -1.4 | 15.5 | 2674 | 78.9 | 4.82 | Tight High-Spin Breakers |
| 189 | Sittinger, Brandyn | LAK_ERI24 | Slider | 180 | 52.8 | 0.231 | 3.6 | -0.7 | 2455 | 87.6 | 5.75 | Tight High-Spin Breakers |
| 190 | Perez, Kelvin | WAS_WIL3 | Slider | 210 | 52.5 | 0.222 | 5.1 | -3.2 | 2169 | 80.9 | 5.83 | Tight High-Spin Breakers |
| 191 | Nova, Fraynel | LAK_ERI24 | Slider | 374 | 52.5 | 0.243 | -0.7 | -6.9 | 2288 | 80.7 | 5.59 | Tight High-Spin Breakers |
| 192 | House, Tristan | MIS_MUD | Slider | 93 | 52.4 | 0.222 | -1.7 | -1.7 | 2336 | 78.3 | 5.79 | Tight High-Spin Breakers |
| 193 | Misla, Luis | TRI_VAL | Slider | 96 | 52.4 | 0.228 | 1.8 | 10.6 | 2723 | 79.0 | 5.27 | Tight High-Spin Breakers |
| 194 | Simone, Andrew | TRO_AIG | Slider | 145 | 52.4 | 0.218 | 3.3 | -3.5 | 2173 | 84.1 | 5.77 | Tight High-Spin Breakers |
| 195 | Fauci, Sonny | NEW_JER6 | Slider | 184 | 52.3 | 0.261 | -1.7 | -6.1 | 2318 | 83.8 | 6.00 | Tight High-Spin Breakers |
| 196 | Balzan, Jackson | SUS_COU1 | Changeup | 341 | 52.3 | 0.240 | 9.5 | -13.8 | 1872 | 79.9 | 5.37 | Tight High-Spin Breakers |
| 197 | Escobar, Anthony | TRO_AIG | Curveball | 76 | 52.2 | 0.223 | -2.4 | -6.7 | 2217 | 77.1 | 6.10 | Tight High-Spin Breakers |
| 198 | Conklin, MacCallan | TRO_AIG | Slider | 127 | 52.2 | 0.228 | 6.1 | -3.8 | 2592 | 83.8 | 6.37 | Tight High-Spin Breakers |
| 199 | Gollert, Harley | TRO_AIG | Changeup | 237 | 52.2 | 0.245 | 9.7 | -13.4 | 1538 | 79.9 | 5.33 | Tight High-Spin Breakers |
| 200 | Pierson, Kenny | LAK_ERI24 | Sinker | 245 | 52.1 | 0.238 | 0.4 | -17.7 | 1762 | 81.0 | 4.82 | Tight High-Spin Breakers |
| 201 | Cooper, Garrett | NEW_YOR13 | Curveball | 194 | 52.0 | 0.223 | -5.7 | -6.5 | 2196 | 76.2 | 5.54 | Tight High-Spin Breakers |
| 202 | Scafidi, Christian | LAK_ERI24 | Slider | 206 | 51.9 | 0.238 | 4.2 | -1.7 | 2388 | 84.3 | 5.61 | Tight High-Spin Breakers |
| 203 | Galva, Claudio | GAT_GRI | Changeup | 110 | 51.8 | 0.233 | 4.6 | -13.4 | 1481 | 84.4 | 4.83 | Tight High-Spin Breakers |
| 204 | Fuenmayor, Liu | OTT_TIT | Sinker | 131 | 51.8 | 0.223 | 9.2 | -20.6 | 2235 | 90.6 | 4.59 | Tight High-Spin Breakers |
| 205 | Foster, Kobe | WAS_WIL3 | Curveball | 207 | 51.7 | 0.248 | -8.3 | 15.0 | 2257 | 67.7 | 5.34 | Tight High-Spin Breakers |
| 206 | Leach, Landon | TRO_AIG | Slider | 72 | 51.6 | 0.238 | 2.4 | -6.9 | 2109 | 82.1 | 5.34 | Tight High-Spin Breakers |
| 207 | Walsh, John | MIS_MUD | Slider | 142 | 51.6 | 0.241 | 0.4 | 9.4 | 2178 | 73.9 | 5.08 | Tight High-Spin Breakers |
| 208 | Hill, Kaleb | OTT_TIT | Slider | 160 | 51.5 | 0.242 | 0.6 | 9.3 | 2254 | 78.8 | 5.25 | Tight High-Spin Breakers |
| 209 | McCartney, Seth | MIS_MUD | Slider | 57 | 51.5 | 0.195 | 4.2 | -3.0 | 2474 | 81.9 | 5.45 | Tight High-Spin Breakers |
| 210 | Boies, Emiles | QUE_CAP | Slider | 102 | 51.4 | 0.253 | 4.5 | -0.1 | 2102 | 80.5 | 5.94 | Tight High-Spin Breakers |
| 211 | Figueredo, Kevin | WIN_CIT29 | Changeup | 111 | 51.2 | 0.253 | 6.0 | -12.7 | 1696 | 84.0 | 5.34 | Tight High-Spin Breakers |
| 212 | Blair, Davis | DOW_EAS1 | Slider | 99 | 51.1 | 0.259 | 3.6 | -5.9 | 2146 | 81.9 | 5.11 | Tight High-Spin Breakers |
| 213 | Martzolf, Max | JOL_SLA | Sinker | 337 | 51.1 | 0.226 | 10.2 | -19.6 | 2135 | 84.9 | 5.48 | Tight High-Spin Breakers |
| 214 | Campbell, AJ | WIN_CIT29 | Cutter | 98 | 51.1 | 0.283 | 8.2 | 0.6 | 2507 | 84.4 | 5.17 | Tight High-Spin Breakers |
| 215 | Miner, Jace | DOW_EAS1 | Curveball | 199 | 51.1 | 0.244 | 2.1 | 11.7 | 1841 | 75.6 | 5.44 | Tight High-Spin Breakers |
| 216 | Carroll, Jake | JOL_SLA | Curveball | 72 | 51.1 | 0.247 | -6.2 | 7.5 | 2018 | 75.5 | 6.21 | Tight High-Spin Breakers |
| 217 | Hill, Kaleb | OTT_TIT | Changeup | 321 | 51.0 | 0.231 | 9.2 | -15.0 | 1783 | 83.0 | 5.67 | Tight High-Spin Breakers |
| 218 | Smith, Jackson | MIS_MUD | Cutter | 143 | 51.0 | 0.237 | 3.4 | 5.8 | 2422 | 82.2 | 5.09 | Tight High-Spin Breakers |
| 219 | Pindel, Buddie | SCH_BOO | Slider | 239 | 51.0 | 0.236 | 0.8 | -7.8 | 2468 | 81.1 | 5.40 | Tight High-Spin Breakers |
| 220 | Glickstein, Aaron | SCH_BOO | Slider | 58 | 50.7 | 0.239 | 7.7 | -0.3 | 2233 | 84.7 | 5.58 | Tight High-Spin Breakers |
| 221 | Toribio, Noe | TRO_AIG | Slider | 237 | 50.5 | 0.221 | 2.6 | 1.2 | 2221 | 82.3 | 5.81 | Tight High-Spin Breakers |
| 222 | Williams, Brian | MIS_MUD | Slider | 325 | 50.5 | 0.246 | 4.1 | -0.6 | 2161 | 81.5 | 5.91 | Tight High-Spin Breakers |
| 223 | Primeaux, Parker | SUS_COU1 | Slider | 52 | 50.5 | 0.201 | 0.6 | -16.3 | 2302 | 79.1 | 5.21 | Tight High-Spin Breakers |
| 224 | Joven, Art | MIS_MUD | Sinker | 383 | 50.4 | 0.250 | 7.0 | -15.3 | 1789 | 83.6 | 5.15 | Tight High-Spin Breakers |
| 225 | Linderman, Greyson | JOL_SLA | Slider | 67 | 50.4 | 0.268 | -3.9 | -13.7 | 2206 | 81.2 | 4.95 | Tight High-Spin Breakers |
| 226 | Castro, Alexander | TRO_AIG | Slider | 147 | 50.3 | 0.253 | 0.9 | -4.6 | 2470 | 83.4 | 4.91 | Tight High-Spin Breakers |
| 227 | Perdomo, Rafael | QUE_CAP | Curveball | 95 | 50.3 | 0.257 | -12.1 | -6.5 | 2185 | 79.9 | 5.49 | Tight High-Spin Breakers |
| 228 | Milburn, Isaac | FLO_Y'A | Curveball | 221 | 50.3 | 0.278 | -9.5 | 13.4 | 2602 | 76.8 | 4.93 | Tight High-Spin Breakers |
| 229 | Bargo, Casey | FLO_Y'A | Slider | 101 | 50.2 | 0.221 | 0.1 | -3.9 | 2278 | 81.4 | 5.35 | Tight High-Spin Breakers |
| 230 | Joven, Art | MIS_MUD | Slider | 354 | 50.2 | 0.241 | 2.1 | -0.1 | 2239 | 77.7 | 5.18 | Tight High-Spin Breakers |
| 231 | Pardinho, Eric | OTT_TIT | Slider | 222 | 50.2 | 0.246 | 4.5 | 1.4 | 2352 | 85.9 | 5.53 | Tight High-Spin Breakers |
| 232 | Peyton, Blake | GAT_GRI | Curveball | 138 | 50.1 | 0.223 | -7.2 | 9.4 | 2714 | 77.6 | 5.22 | Tight High-Spin Breakers |
| 233 | Sechrist, Zander | WAS_WIL3 | Four-Seam | 156 | 50.0 | 0.220 | 13.9 | -16.6 | 1911 | 80.2 | 5.66 | Tight High-Spin Breakers |
| 234 | Campbell, Tyler | MIS_MUD | Slider | 300 | 49.9 | 0.254 | 7.3 | 4.6 | 2196 | 73.9 | 5.71 | Tight High-Spin Breakers |
| 235 | Gilleran, Jimmy | NEW_ENG23 | Slider | 159 | 49.9 | 0.239 | 3.9 | -3.2 | 2247 | 80.8 | 5.35 | Tight High-Spin Breakers |
| 236 | Belton, Hunter | MIS_MUD | Slider | 99 | 49.9 | 0.244 | 6.5 | -2.6 | 2108 | 78.5 | 5.82 | Tight High-Spin Breakers |
| 237 | Rohde, Isaac | NEW_YOR13 | Sinker | 51 | 49.9 | 0.271 | 9.5 | -19.0 | 2109 | 84.1 | 5.83 | Tight High-Spin Breakers |
| 238 | Petery, Dylan | WIN_CIT29 | Slider | 67 | 49.8 | 0.208 | -0.4 | -12.4 | 2605 | 78.0 | 5.76 | Tight High-Spin Breakers |
| 239 | Peters, Garrett | NEW_YOR13 | Curveball | 201 | 49.8 | 0.242 | 0.5 | -0.3 | 2039 | 75.9 | 5.78 | Tight High-Spin Breakers |
| 240 | Wehrle, Tyler | WIN_CIT29 | Slider | 216 | 49.8 | 0.239 | 1.8 | -10.9 | 2552 | 80.8 | 5.29 | Tight High-Spin Breakers |
| 241 | Villalobos, Jonaiker | FLO_Y'A | Changeup | 251 | 49.7 | 0.244 | 7.8 | -13.2 | 1579 | 80.2 | 5.84 | Tight High-Spin Breakers |
| 242 | Parks, Pavin | LAK_ERI24 | Cutter | 136 | 49.7 | 0.246 | 7.1 | -3.6 | 2429 | 84.7 | 5.77 | Tight High-Spin Breakers |
| 243 | Sakurai, Masatoshi | QUE_CAP | Slider | 170 | 49.6 | 0.254 | -0.3 | 4.2 | 2213 | 79.0 | 5.75 | Tight High-Spin Breakers |
| 244 | Stegura, Drew | WAS_WIL3 | Curveball | 52 | 49.5 | 0.266 | -12.6 | -9.8 | 2322 | 76.1 | 5.99 | Tight High-Spin Breakers |
| 245 | Perdomo, Rafael | QUE_CAP | Slider | 116 | 49.5 | 0.233 | 2.3 | -0.3 | 2198 | 82.5 | 5.69 | Tight High-Spin Breakers |
| 246 | Willeman, Landon | EVA_OTT | Slider | 145 | 49.3 | 0.228 | 1.0 | -4.1 | 2261 | 80.9 | 5.47 | Tight High-Spin Breakers |
| 247 | Armstrong, Andrew | NEW_YOR13 | Slider | 160 | 49.1 | 0.267 | 2.6 | 7.5 | 2385 | 80.0 | 5.91 | Tight High-Spin Breakers |
| 248 | Walsh, John | MIS_MUD | Changeup | 70 | 49.0 | 0.275 | 8.0 | -13.5 | 1676 | 77.2 | 5.25 | Tight High-Spin Breakers |
| 249 | Gollert, Harley | TRO_AIG | Curveball | 163 | 48.9 | 0.244 | -6.0 | 6.3 | 2261 | 77.3 | 4.97 | Tight High-Spin Breakers |
| 250 | Misla, Luis | TRI_VAL | Curveball | 177 | 48.9 | 0.246 | -5.2 | 9.5 | 2786 | 77.2 | 5.13 | Tight High-Spin Breakers |
| 251 | Sesar, Jorden | SUS_COU1 | Curveball | 136 | 48.9 | 0.262 | -11.9 | -11.2 | 2418 | 74.9 | 6.03 | Tight High-Spin Breakers |
| 252 | Ginn, Landon | WAS_WIL3 | Cutter | 122 | 48.8 | 0.238 | 3.3 | -2.0 | 2836 | 86.4 | 5.39 | Tight High-Spin Breakers |
| 253 | De Los Santos, Enmanuel | NEW_ENG23 | Curveball | 127 | 48.8 | 0.247 | -5.5 | -10.9 | 2210 | 71.5 | 6.46 | Tight High-Spin Breakers |
| 254 | Villalobos, Jonaiker | FLO_Y'A | Curveball | 177 | 48.7 | 0.240 | -4.9 | 5.1 | 2263 | 74.9 | 5.33 | Tight High-Spin Breakers |
| 255 | Hampton, Ky | OTT_TIT | Slider | 138 | 48.6 | 0.249 | 1.1 | -5.2 | 2308 | 83.4 | 5.75 | Tight High-Spin Breakers |
| 256 | Kostura, Brit | WAS_WIL3 | Sinker | 136 | 48.6 | 0.238 | 13.2 | -16.7 | 2075 | 84.9 | 5.55 | Tight High-Spin Breakers |
| 257 | Sanchez, Edwin | LAK_ERI24 | Curveball | 146 | 48.6 | 0.235 | -4.7 | 5.6 | 2465 | 76.1 | 5.26 | Tight High-Spin Breakers |
| 258 | Misla, Luis | TRI_VAL | Changeup | 60 | 48.4 | 0.253 | 11.6 | -15.8 | 2021 | 84.7 | 5.52 | Tight High-Spin Breakers |
| 259 | Henderson, Drew | DOW_EAS1 | Curveball | 352 | 48.4 | 0.245 | -7.7 | -4.7 | 2287 | 76.9 | 5.08 | Tight High-Spin Breakers |
| 260 | Bell, Brendan | NEW_ENG23 | Slider | 81 | 48.4 | 0.295 | -1.5 | -9.2 | 2406 | 82.5 | 5.45 | Tight High-Spin Breakers |
| 261 | Delaney, Carter | WIN_CIT29 | Slider | 85 | 48.3 | 0.273 | -0.3 | -7.0 | 2277 | 80.1 | 5.47 | Tight High-Spin Breakers |
| 262 | Vilchez, Michael | OTT_TIT | Slider | 120 | 48.3 | 0.251 | 1.2 | -4.8 | 2302 | 82.6 | 5.71 | Tight High-Spin Breakers |
| 263 | Kostura, Brit | WAS_WIL3 | Changeup | 90 | 48.3 | 0.241 | 9.7 | -16.0 | 1872 | 80.4 | 5.78 | Tight High-Spin Breakers |
| 264 | Rodriguez, Luis | TRO_AIG | Slider | 58 | 48.3 | 0.239 | 2.2 | -1.6 | 2525 | 87.7 | 5.92 | Tight High-Spin Breakers |
| 265 | Peters, Garrett | NEW_YOR13 | Changeup | 610 | 48.2 | 0.249 | 12.0 | -14.2 | 1850 | 80.1 | 5.96 | Tight High-Spin Breakers |
| 266 | Hicks, Jackson | DOW_EAS1 | Slider | 116 | 48.2 | 0.268 | 2.4 | -1.0 | 2195 | 80.0 | 5.23 | Tight High-Spin Breakers |
| 267 | Pierson, Kenny | LAK_ERI24 | Changeup | 333 | 48.1 | 0.252 | -1.2 | -16.3 | 1743 | 76.9 | 4.92 | Tight High-Spin Breakers |
| 268 | Kaminer, Brandon | DOW_EAS1 | Slider | 133 | 48.1 | 0.236 | 6.1 | 2.3 | 2474 | 83.8 | 5.28 | Tight High-Spin Breakers |
| 269 | Moore, Kyle | SCH_BOO | Changeup | 124 | 47.9 | 0.233 | 9.9 | 16.4 | 2015 | 82.1 | 4.69 | Tight High-Spin Breakers |
| 270 | Smith, Ethan | WIN_CIT29 | Slider | 58 | 47.8 | 0.280 | -0.2 | -6.4 | 2423 | 80.6 | 5.91 | Tight High-Spin Breakers |
| 271 | Campbell, AJ | WIN_CIT29 | Sinker | 59 | 47.7 | 0.252 | 8.3 | 6.1 | 2441 | 86.0 | 5.33 | Tight High-Spin Breakers |
| 272 | Simpson, Garret | EVA_OTT | Curveball | 140 | 47.7 | 0.266 | -11.0 | -12.8 | 2630 | 76.7 | 5.17 | Tight High-Spin Breakers |
| 273 | Kaftan, Eddie | FLO_Y'A | Slider | 62 | 47.7 | 0.232 | 1.1 | -6.3 | 2437 | 77.1 | 4.72 | Tight High-Spin Breakers |
| 274 | Almonte, Lisandro | NEW_JER6 | Slider | 57 | 47.7 | 0.241 | 3.6 | -0.9 | 2194 | 85.7 | 5.45 | Tight High-Spin Breakers |
| 275 | Smith, Jackson | MIS_MUD | Sinker | 585 | 47.6 | 0.262 | 1.0 | 21.7 | 2403 | 85.2 | 5.14 | Tight High-Spin Breakers |
| 276 | Baker, Luke | EVA_OTT | Curveball | 59 | 47.6 | 0.244 | -7.4 | 9.7 | 2694 | 75.5 | 5.51 | Tight High-Spin Breakers |
| 277 | Lefebvre, Charles | TRO_AIG | Slider | 130 | 47.5 | 0.222 | 2.3 | -1.6 | 2165 | 81.7 | 6.46 | Tight High-Spin Breakers |
| 278 | Majick, Eli | NEW_ENG23 | Changeup | 198 | 47.5 | 0.258 | 3.1 | -13.3 | 1826 | 82.1 | 5.92 | Tight High-Spin Breakers |
| 279 | Anglin, Mack | WAS_WIL3 | Slider | 67 | 47.5 | 0.220 | -0.1 | -13.0 | 2583 | 83.2 | 5.45 | Tight High-Spin Breakers |
| 280 | Scott, Brandon | LAK_ERI24 | Changeup | 242 | 47.4 | 0.278 | 2.2 | -12.4 | 1515 | 81.2 | 5.76 | Tight High-Spin Breakers |
| 281 | Matos, Dwayne | OTT_TIT | Slider | 143 | 47.3 | 0.260 | 4.4 | -0.8 | 2026 | 81.5 | 6.17 | Tight High-Spin Breakers |
| 282 | Good, Ty | GAT_GRI | Curveball | 196 | 47.1 | 0.259 | -7.8 | -4.6 | 2128 | 74.9 | 5.64 | Tight High-Spin Breakers |
| 283 | Marynczak, Arlo | TRI_VAL | Curveball | 59 | 47.1 | 0.253 | -2.6 | -13.9 | 2178 | 76.3 | 5.71 | Tight High-Spin Breakers |
| 284 | Cook, Cole | SCH_BOO | Four-Seam | 410 | 47.0 | 0.247 | 14.4 | -9.8 | 2288 | 84.7 | 5.29 | Tight High-Spin Breakers |
| 285 | Sanchez, Edwin | LAK_ERI24 | Slider | 115 | 47.0 | 0.265 | -0.4 | 4.3 | 2402 | 77.3 | 5.17 | Tight High-Spin Breakers |
| 286 | Foy, Corbin | LAK_ERI24 | Slider | 78 | 46.9 | 0.269 | -1.1 | -7.6 | 2653 | 82.4 | 5.56 | Tight High-Spin Breakers |
| 287 | Drakeford, Dosie | NEW_JER6 | Slider | 82 | 46.9 | 0.294 | 1.9 | -6.7 | 2396 | 79.7 | 5.44 | Tight High-Spin Breakers |
| 288 | Petery, Dylan | WIN_CIT29 | Curveball | 94 | 46.8 | 0.264 | -6.8 | -14.6 | 2561 | 74.4 | 5.54 | Tight High-Spin Breakers |
| 289 | McKillican, Adam | QUE_CAP | Slider | 50 | 46.8 | 0.242 | 3.3 | -3.5 | 2162 | 80.1 | 6.44 | Tight High-Spin Breakers |
| 290 | Turner, Eric | JOL_SLA | Slider | 250 | 46.6 | 0.248 | 1.4 | -7.7 | 2354 | 78.2 | 4.96 | Tight High-Spin Breakers |
| 291 | Hopewell, Chase | FLO_Y'A | Slider | 161 | 46.6 | 0.273 | 0.4 | -2.1 | 1912 | 81.1 | 6.15 | Tight High-Spin Breakers |
| 292 | Parra, Andres | LAK_ERI24 | Slider | 161 | 46.5 | 0.265 | 2.8 | 2.0 | 2288 | 79.6 | 5.71 | Tight High-Spin Breakers |
| 293 | Cook, Cole | SCH_BOO | Sinker | 146 | 46.4 | 0.242 | 11.8 | -11.7 | 2251 | 84.7 | 5.30 | Tight High-Spin Breakers |
| 294 | Reeves, Cobe | NEW_YOR13 | Curveball | 52 | 46.3 | 0.274 | -8.0 | 7.0 | 2370 | 80.1 | 5.53 | Tight High-Spin Breakers |
| 295 | Foltz Jr., Michael | WAS_WIL3 | Curveball | 105 | 46.3 | 0.264 | -6.0 | 4.6 | 2306 | 79.3 | 5.39 | Tight High-Spin Breakers |
| 296 | Debban, Caleb | NEW_JER6 | Curveball | 219 | 46.3 | 0.278 | -7.1 | 18.5 | 2812 | 77.0 | 5.94 | Tight High-Spin Breakers |
| 297 | Salata, Derek | SCH_BOO | Slider | 266 | 45.8 | 0.261 | 3.6 | -7.2 | 2512 | 81.6 | 5.56 | Tight High-Spin Breakers |
| 298 | Khan, Sebastian | QUE_CAP | Changeup | 81 | 45.8 | 0.249 | -2.0 | 18.0 | 1809 | 85.7 | 5.04 | Tight High-Spin Breakers |
| 299 | Cook, Cole | SCH_BOO | Cutter | 136 | 45.8 | 0.219 | 9.5 | -3.7 | 2387 | 82.5 | 5.27 | Tight High-Spin Breakers |
| 300 | Rodriguez, Joe Joe | NEW_JER6 | Slider | 77 | 45.8 | 0.261 | 5.0 | 2.6 | 2114 | 82.0 | 5.56 | Tight High-Spin Breakers |
| 301 | Burcham, Jacob | GAT_GRI | Slider | 164 | 45.8 | 0.238 | -0.2 | -9.4 | 2380 | 80.6 | 5.84 | Tight High-Spin Breakers |
| 302 | Simpson, Garret | EVA_OTT | Cutter | 240 | 45.7 | 0.272 | 7.3 | 1.4 | 2365 | 86.8 | 5.47 | Tight High-Spin Breakers |
| 303 | Nakata, Yuto | QUE_CAP | Curveball | 88 | 45.7 | 0.262 | -12.9 | -13.2 | 2627 | 74.7 | 5.20 | Tight High-Spin Breakers |
| 304 | Rodriguez, Ramon | WIN_CIT29 | Changeup | 79 | 45.6 | 0.268 | 9.7 | -11.0 | 2225 | 83.6 | 5.89 | Tight High-Spin Breakers |
| 305 | Sakurai, Masatoshi | QUE_CAP | Curveball | 201 | 45.6 | 0.263 | -4.5 | 5.3 | 2442 | 78.3 | 5.57 | Tight High-Spin Breakers |
| 306 | Gregory, Ben | GAT_GRI | Slider | 112 | 45.5 | 0.291 | 1.4 | -4.7 | 2329 | 79.6 | 6.04 | Tight High-Spin Breakers |
| 307 | Campbell, AJ | WIN_CIT29 | Changeup | 92 | 45.4 | 0.257 | 7.4 | 9.7 | 2099 | 81.1 | 5.36 | Tight High-Spin Breakers |
| 308 | Girard, John | FLO_Y'A | Changeup | 71 | 45.4 | 0.277 | 8.3 | -12.3 | 1636 | 80.9 | 5.61 | Tight High-Spin Breakers |
| 309 | Willeman, Landon | EVA_OTT | Curveball | 150 | 45.3 | 0.284 | -8.6 | -10.4 | 2093 | 77.3 | 5.36 | Tight High-Spin Breakers |
| 310 | Joven, Art | MIS_MUD | Changeup | 489 | 45.2 | 0.263 | 5.2 | -15.5 | 1807 | 81.6 | 5.25 | Tight High-Spin Breakers |
| 311 | Smith, Ben | NEW_ENG23 | Slider | 143 | 45.0 | 0.298 | 0.3 | 12.0 | 2292 | 79.1 | 5.39 | Tight High-Spin Breakers |
| 312 | Barker, Alex | NEW_YOR13 | Slider | 199 | 45.0 | 0.246 | 3.6 | 4.1 | 2243 | 81.7 | 5.83 | Tight High-Spin Breakers |
| 313 | Delaney, Carter | WIN_CIT29 | Curveball | 96 | 44.9 | 0.283 | -5.4 | -6.9 | 2258 | 79.9 | 5.56 | Tight High-Spin Breakers |
| 314 | Cook, Cole | SCH_BOO | Changeup | 315 | 44.8 | 0.261 | 9.4 | -9.9 | 1863 | 80.9 | 5.47 | Tight High-Spin Breakers |
| 315 | Martzolf, Max | OTT_TIT | Changeup | 194 | 44.8 | 0.246 | 9.4 | -19.5 | 2044 | 83.2 | 5.42 | Tight High-Spin Breakers |
| 316 | Forsyth, Braden | MIS_MUD | Slider | 181 | 44.7 | 0.274 | 3.8 | -6.8 | 2368 | 80.8 | 6.09 | Tight High-Spin Breakers |
| 317 | Huter, Blayne | SUS_COU1 | Curveball | 103 | 44.5 | 0.271 | -5.1 | -14.2 | 2137 | 73.7 | 6.01 | Tight High-Spin Breakers |
| 318 | Dima, Josh | GAT_GRI | Curveball | 65 | 44.3 | 0.268 | -3.7 | 2.7 | 1970 | 80.0 | 5.95 | Tight High-Spin Breakers |
| 319 | Grills, Evan | OTT_TIT | Changeup | 65 | 44.1 | 0.242 | 12.6 | -14.4 | 1799 | 79.4 | 5.82 | Tight High-Spin Breakers |
| 320 | Rodriguez, Leonardo | NEW_JER6 | Slider | 98 | 44.1 | 0.266 | 2.7 | -3.1 | 2606 | 84.1 | 5.98 | Tight High-Spin Breakers |
| 321 | Figueredo, Kevin | WIN_CIT29 | Curveball | 78 | 44.0 | 0.277 | -3.5 | 4.9 | 2324 | 75.8 | 5.00 | Tight High-Spin Breakers |
| 322 | Bradford, Ethan | NEW_YOR13 | Slider | 196 | 44.0 | 0.284 | -1.2 | 5.7 | 2467 | 82.5 | 5.50 | Tight High-Spin Breakers |
| 323 | Cooper, Garrett | NEW_YOR13 | Slider | 127 | 43.9 | 0.253 | 2.1 | -2.8 | 2069 | 80.3 | 5.75 | Tight High-Spin Breakers |
| 324 | Rivas, Albert | GAT_GRI | Slider | 67 | 43.8 | 0.242 | 6.5 | 0.3 | 2340 | 83.0 | 5.78 | Tight High-Spin Breakers |
| 325 | Gollert, Harley | QUE_CAP | Changeup | 52 | 43.7 | 0.253 | 10.2 | -8.4 | 1676 | 81.0 | 5.46 | Tight High-Spin Breakers |
| 326 | Okumura, Shuto | WAS_WIL3 | Four-Seam | 60 | 43.5 | 0.273 | 6.1 | 7.6 | 1757 | 75.3 | 5.56 | Tight High-Spin Breakers |
| 327 | Encarnacion, J.D. | EVA_OTT | Slider | 143 | 43.5 | 0.252 | 2.5 | -5.4 | 2352 | 81.2 | 5.43 | Tight High-Spin Breakers |
| 328 | Serrano, Elio | NEW_JER6 | Curveball | 107 | 43.4 | 0.287 | -9.8 | -13.8 | 2283 | 75.7 | 5.13 | Tight High-Spin Breakers |
| 329 | Godwin, Connor | NEW_YOR13 | Slider | 93 | 43.4 | 0.261 | 0.0 | -10.2 | 2535 | 82.4 | 6.11 | Tight High-Spin Breakers |
| 330 | Smith, Donny | JOL_SLA | Slider | 66 | 43.3 | 0.245 | -2.4 | -5.4 | 2476 | 78.5 | 5.16 | Tight High-Spin Breakers |
| 331 | Lockhart, Gauge | LAK_ERI24 | Slider | 71 | 43.2 | 0.292 | 3.0 | -2.0 | 2111 | 84.1 | 5.92 | Tight High-Spin Breakers |
| 332 | McEvoy, Aidan | FLO_Y'A | Changeup | 73 | 43.2 | 0.246 | 2.8 | -14.2 | 1735 | 82.9 | 6.32 | Tight High-Spin Breakers |
| 333 | Smith, Jackson | MIS_MUD | Changeup | 126 | 43.1 | 0.289 | -1.1 | 18.0 | 2235 | 81.5 | 5.12 | Tight High-Spin Breakers |
| 334 | Reeves, Cobe | NEW_YOR13 | Slider | 62 | 43.1 | 0.261 | 0.2 | 3.0 | 2196 | 83.1 | 5.82 | Tight High-Spin Breakers |
| 335 | Martzolf, Max | OTT_TIT | Four-Seam | 71 | 43.1 | 0.246 | 10.5 | -20.4 | 2140 | 84.5 | 5.83 | Tight High-Spin Breakers |
| 336 | Martzolf, Max | OTT_TIT | Curveball | 71 | 43.1 | 0.288 | -4.2 | 11.1 | 2155 | 73.9 | 5.43 | Tight High-Spin Breakers |
| 337 | Maher, Adam | TRI_VAL | Curveball | 76 | 42.7 | 0.251 | 1.6 | 2.4 | 2007 | 77.3 | 5.53 | Tight High-Spin Breakers |
| 338 | Parsons, Billy | SUS_COU1 | Slider | 253 | 42.5 | 0.244 | 5.8 | -6.2 | 2477 | 83.0 | 5.44 | Tight High-Spin Breakers |
| 339 | Blence, Connor | WIN_CIT29 | Slider | 79 | 42.4 | 0.268 | 3.8 | -4.9 | 2552 | 79.5 | 5.97 | Tight High-Spin Breakers |
| 340 | Lovin, Xander | GAT_GRI | Slider | 173 | 42.3 | 0.280 | 3.2 | -3.6 | 2429 | 84.9 | 4.90 | Tight High-Spin Breakers |
| 341 | Vitas, Ben | JOL_SLA | Slider | 202 | 42.3 | 0.259 | 1.9 | -3.5 | 2091 | 81.6 | 4.93 | Tight High-Spin Breakers |
| 342 | Westcott, Zac | FLO_Y'A | Changeup | 196 | 42.3 | 0.262 | 6.5 | 16.7 | 1915 | 76.5 | 5.73 | Tight High-Spin Breakers |
| 343 | Sanchez, Edwin | LAK_ERI24 | Changeup | 158 | 42.3 | 0.277 | 6.7 | -15.8 | 1951 | 80.4 | 5.77 | Tight High-Spin Breakers |
| 344 | Catrambone, Ben | JOL_SLA | Cutter | 81 | 42.2 | 0.288 | 6.6 | -0.2 | 2348 | 83.4 | 5.23 | Tight High-Spin Breakers |
| 345 | Andueza, Axel | DOW_EAS1 | Curveball | 194 | 42.0 | 0.254 | -3.6 | -3.3 | 2195 | 79.2 | 5.11 | Tight High-Spin Breakers |
| 346 | Williams, Pierce | NEW_ENG23 | Curveball | 172 | 42.0 | 0.265 | -5.7 | 6.5 | 2179 | 75.2 | 5.77 | Tight High-Spin Breakers |
| 347 | Anderson, Colt | WAS_WIL3 | Curveball | 91 | 42.0 | 0.285 | -10.6 | 10.3 | 1994 | 73.8 | 6.03 | Tight High-Spin Breakers |
| 348 | Noble, Nick | FDU_KNI | Changeup | 71 | 41.9 | 0.301 | 0.2 | 17.6 | 1612 | 77.3 | 5.00 | Tight High-Spin Breakers |
| 349 | Rohde, Isaac | NEW_YOR13 | Curveball | 54 | 41.8 | 0.249 | -4.0 | 10.7 | 2456 | 70.9 | 5.90 | Tight High-Spin Breakers |
| 350 | Escobar, Anthony | TRO_AIG | Slider | 338 | 41.7 | 0.271 | 3.4 | -5.1 | 2155 | 81.8 | 6.14 | Tight High-Spin Breakers |
| 351 | Gollert, Harley | TRO_AIG | Slider | 83 | 41.6 | 0.276 | -2.0 | 8.0 | 2233 | 78.2 | 4.96 | Tight High-Spin Breakers |
| 352 | Serrano, Elio | NEW_JER6 | Slider | 176 | 41.6 | 0.264 | 5.4 | -2.1 | 2240 | 82.5 | 5.34 | Tight High-Spin Breakers |
| 353 | Barker, Alex | NEW_YOR13 | Curveball | 114 | 41.5 | 0.265 | -5.7 | 10.0 | 2269 | 76.3 | 5.62 | Tight High-Spin Breakers |
| 354 | Tiburcio, David | DOW_EAS1 | Slider | 119 | 40.9 | 0.284 | 5.9 | 1.0 | 2343 | 86.4 | 5.44 | Tight High-Spin Breakers |
| 355 | Shinn, Nathan | LAK_ERI24 | Curveball | 88 | 40.4 | 0.278 | -5.9 | 0.6 | 2113 | 79.6 | 5.29 | Tight High-Spin Breakers |
| 356 | Sanchez, Dikember | LAK_ERI24 | Slider | 111 | 40.4 | 0.274 | 2.1 | -3.7 | 2555 | 85.9 | 5.32 | Tight High-Spin Breakers |
| 357 | Sabatine, Gino | TRI_VAL | Slider | 138 | 40.3 | 0.289 | 4.2 | -3.6 | 2322 | 79.9 | 4.89 | Tight High-Spin Breakers |
| 358 | Lawson, Nathan | FLO_Y'A | Cutter | 101 | 40.2 | 0.248 | 7.6 | -1.1 | 2307 | 83.7 | 5.76 | Tight High-Spin Breakers |
| 359 | Soto, Carlos | JOL_SLA | Slider | 112 | 40.1 | 0.292 | -1.7 | -8.8 | 2512 | 78.2 | 5.08 | Tight High-Spin Breakers |
| 360 | Andueza, Axel | DOW_EAS1 | Slider | 122 | 40.0 | 0.281 | -0.6 | -1.5 | 2082 | 80.7 | 5.21 | Tight High-Spin Breakers |
| 361 | Sechrist, Zander | WAS_WIL3 | Sinker | 98 | 40.0 | 0.267 | 13.2 | -17.8 | 1893 | 80.1 | 5.60 | Tight High-Spin Breakers |
| 362 | Simpson, Garret | EVA_OTT | Slider | 139 | 39.8 | 0.280 | -2.0 | -6.2 | 2431 | 80.7 | 5.12 | Tight High-Spin Breakers |
| 363 | Kassebaum, Torin | LON_ISL22 | Curveball | 55 | 39.8 | 0.306 | 1.1 | 10.2 | 2155 | 71.6 | 5.31 | Tight High-Spin Breakers |
| 364 | Sechrist, Zander | WAS_WIL3 | Changeup | 261 | 39.6 | 0.280 | 8.0 | -14.9 | 1671 | 76.7 | 5.78 | Tight High-Spin Breakers |
| 365 | Brouwer, Adam | LAK_ERI24 | Curveball | 114 | 39.5 | 0.268 | -9.3 | -6.2 | 2333 | 77.9 | 5.30 | Tight High-Spin Breakers |
| 366 | Eldred, Zach | NEW_ENG23 | Slider | 202 | 39.4 | 0.278 | 1.4 | -7.3 | 2422 | 82.3 | 5.82 | Tight High-Spin Breakers |
| 367 | Brodsky, Jack | WAS_WIL3 | Curveball | 146 | 39.4 | 0.312 | -8.7 | -12.3 | 2634 | 75.9 | 5.52 | Tight High-Spin Breakers |
| 368 | Bice, Emmett | NEW_YOR13 | Curveball | 214 | 39.1 | 0.300 | -10.3 | -13.3 | 2998 | 79.2 | 5.59 | Tight High-Spin Breakers |
| 369 | Fauci, Sonny | NEW_JER6 | Curveball | 147 | 39.0 | 0.331 | -14.5 | -6.7 | 2303 | 78.5 | 5.95 | Tight High-Spin Breakers |
| 370 | Galva, Claudio | GAT_GRI | Slider | 241 | 38.7 | 0.273 | 2.9 | -0.4 | 2241 | 83.7 | 4.78 | Tight High-Spin Breakers |
| 371 | Thornton, Tyler | NEW_ENG23 | Slider | 176 | 38.4 | 0.303 | 2.0 | -0.5 | 1948 | 79.6 | 4.85 | Tight High-Spin Breakers |
| 372 | Tokar, Heitor | OTT_TIT | Curveball | 57 | 38.3 | 0.297 | -14.6 | -9.2 | 2124 | 73.4 | 5.82 | Tight High-Spin Breakers |
| 373 | Quigley, Michael | NEW_ENG23 | Curveball | 84 | 38.2 | 0.293 | -12.1 | -12.5 | 2560 | 78.8 | 5.40 | Tight High-Spin Breakers |
| 374 | Voytko, Fawster | TRO_AIG | Slider | 87 | 38.2 | 0.283 | 1.6 | -11.3 | 2320 | 78.8 | 6.19 | Tight High-Spin Breakers |
| 375 | Gilleran, Jimmy | NEW_ENG23 | Splitter | 58 | 38.2 | 0.316 | 0.0 | 7.7 | 1520 | 79.1 | 5.13 | Tight High-Spin Breakers |
| 376 | Fuenmayor, Liu | OTT_TIT | Changeup | 56 | 37.6 | 0.265 | -1.2 | -15.3 | 1375 | 83.1 | 4.90 | Tight High-Spin Breakers |
| 377 | Chabot, Henry | LAK_ERI24 | Slider | 69 | 37.2 | 0.332 | 4.0 | -1.5 | 2413 | 84.3 | 5.11 | Tight High-Spin Breakers |
| 378 | Eldred, Zach | NEW_ENG23 | Curveball | 95 | 35.7 | 0.327 | -10.0 | -12.4 | 2500 | 77.6 | 5.83 | Tight High-Spin Breakers |
| 379 | Kostura, Brit | WAS_WIL3 | Slider | 65 | 35.3 | 0.295 | -0.6 | 5.2 | 2160 | 74.8 | 5.09 | Tight High-Spin Breakers |
| 380 | Gorgen, Grady | NEW_YOR13 | Curveball | 94 | 35.2 | 0.296 | -7.5 | 7.1 | 2150 | 79.9 | 5.70 | Tight High-Spin Breakers |
| 381 | Nova, Fraynel | LAK_ERI24 | Curveball | 68 | 33.2 | 0.310 | -4.4 | -6.1 | 2300 | 80.3 | 5.59 | Tight High-Spin Breakers |
| 382 | Hargrove, Dawson | LAK_ERI24 | Curveball | 82 | 32.8 | 0.313 | -6.8 | -7.7 | 2243 | 76.7 | 5.21 | Tight High-Spin Breakers |
| 383 | Catrambone, Ben | JOL_SLA | Slider | 126 | 32.8 | 0.329 | 2.6 | -1.4 | 2279 | 82.8 | 4.87 | Tight High-Spin Breakers |
| 384 | Brodsky, Jack | WAS_WIL3 | Slider | 55 | 32.7 | 0.298 | -0.9 | -11.2 | 2586 | 79.1 | 5.53 | Tight High-Spin Breakers |
| 385 | Garbrick, Alex | LAK_ERI24 | Slider | 71 | 32.2 | 0.326 | 1.9 | -3.3 | 2560 | 82.9 | 5.05 | Tight High-Spin Breakers |
| 386 | Gorgen, Grady | NEW_YOR13 | Slider | 139 | 32.1 | 0.314 | 1.4 | 1.1 | 2154 | 83.0 | 5.98 | Tight High-Spin Breakers |
| 387 | Voytko, Fawster | TRO_AIG | Curveball | 94 | 32.0 | 0.319 | -7.2 | -11.8 | 2338 | 74.9 | 6.04 | Tight High-Spin Breakers |
| 388 | Lawson, Nathan | FLO_Y'A | Slider | 63 | 31.4 | 0.300 | 6.9 | -2.5 | 2435 | 83.1 | 5.79 | Tight High-Spin Breakers |
| 389 | Albert, Wes | DOW_EAS1 | Slider | 65 | 31.0 | 0.302 | 5.7 | -1.4 | 1823 | 80.6 | 5.71 | Tight High-Spin Breakers |
| 390 | Plumadore, Carson | WIN_CIT29 | Curveball | 111 | 30.6 | 0.313 | 0.6 | -6.6 | 2489 | 75.5 | 5.58 | Tight High-Spin Breakers |
| 391 | Johnston, Spencer | DOW_EAS1 | Curveball | 74 | 30.0 | 0.304 | -4.9 | -6.1 | 2132 | 74.4 | 5.70 | Tight High-Spin Breakers |
| 392 | Galva, Claudio | GAT_GRI | Sinker | 222 | 30.0 | 0.306 | 10.4 | -12.2 | 1974 | 89.1 | 4.93 | Tight High-Spin Breakers |
| 393 | Moreno, Jose | DOW_EAS1 | Slider | 50 | 29.2 | 0.282 | 5.2 | -0.7 | 2307 | 83.4 | 5.57 | Tight High-Spin Breakers |
| 394 | Townes, Holland | SCH_BOO | Cutter | 79 | 29.0 | 0.302 | 3.4 | -1.9 | 2151 | 84.1 | 4.96 | Tight High-Spin Breakers |
| 395 | Gilleran, Jimmy | NEW_ENG23 | Curveball | 51 | 28.8 | 0.303 | -5.5 | -5.4 | 2387 | 75.5 | 5.06 | Tight High-Spin Breakers |
| 396 | Lawson, Nathan | FLO_Y'A | Curveball | 81 | 26.9 | 0.391 | -15.9 | -11.9 | 2381 | 74.2 | 5.59 | Tight High-Spin Breakers |
| 397 | Webster, Evan | FLO_Y'A | Curveball | 105 | 26.7 | 0.347 | -3.0 | 4.7 | 1787 | 73.6 | 6.70 | Tight High-Spin Breakers |
| 398 | Cameron, Wyatt | SCH_BOO | Curveball | 109 | 26.6 | 0.358 | -13.5 | -9.7 | 2296 | 81.1 | 5.24 | Tight High-Spin Breakers |
| 399 | Miranda, Kevin | OTT_TIT | Slider | 86 | 26.2 | 0.344 | 3.5 | -0.3 | 2211 | 81.0 | 5.61 | Tight High-Spin Breakers |
| 400 | Lovin, Xander | GAT_GRI | Curveball | 75 | 25.3 | 0.329 | -9.1 | -12.1 | 2620 | 76.8 | 4.64 | Tight High-Spin Breakers |
| 401 | Westcott, Zac | FLO_Y'A | Curveball | 163 | 20.5 | 0.375 | -15.2 | -9.2 | 1872 | 67.1 | 5.48 | Tight High-Spin Breakers |
| 402 | Heintz, Danny | FLO_Y'A | Four-Seam | 60 | 75.8 | 0.092 | 14.2 | 10.4 | 2180 | 92.2 | 5.82 | Soft-Speed Separation |
| 403 | Davis, Tyler | WIN_CIT29 | Four-Seam | 76 | 74.4 | 0.111 | 21.2 | 5.6 | 2171 | 89.3 | 5.86 | Soft-Speed Separation |
| 404 | Grounds, Jackson | DOW_EAS1 | Four-Seam | 107 | 74.1 | 0.159 | 17.0 | 14.2 | 2163 | 92.5 | 5.59 | Soft-Speed Separation |
| 405 | Debban, Caleb | NEW_JER6 | Four-Seam | 57 | 73.5 | 0.176 | 13.1 | -4.6 | 2325 | 87.2 | 6.58 | Soft-Speed Separation |
| 406 | Garcia, Hector | WAS_WIL3 | Splitter | 62 | 73.4 | 0.184 | 11.7 | 7.6 | 1216 | 78.2 | 5.92 | Soft-Speed Separation |
| 407 | Earwood, Micah | SUS_COU1 | Four-Seam | 98 | 73.3 | 0.231 | 18.3 | 2.9 | 2068 | 80.8 | 5.65 | Soft-Speed Separation |
| 408 | Barreto, Brayhans | TRI_VAL | Cutter | 51 | 72.4 | 0.163 | 9.1 | 0.1 | 1919 | 83.5 | 6.44 | Soft-Speed Separation |
| 409 | Good, Ty | GAT_GRI | Changeup | 73 | 70.7 | 0.244 | 17.1 | 4.5 | 1773 | 77.9 | 6.30 | Soft-Speed Separation |
| 410 | Riedel, Caleb | SCH_BOO | Sinker | 91 | 70.6 | 0.125 | 15.9 | -15.9 | 2306 | 88.9 | 6.00 | Soft-Speed Separation |
| 411 | Webster, Evan | FLO_Y'A | Cutter | 151 | 70.3 | 0.169 | 5.7 | -0.5 | 2031 | 84.5 | 6.94 | Soft-Speed Separation |
| 412 | Still, Stephen | TRI_VAL | Sinker | 61 | 69.4 | 0.212 | 14.1 | -18.1 | 2325 | 90.6 | 5.39 | Soft-Speed Separation |
| 413 | Perdomo, Rafael | QUE_CAP | Changeup | 55 | 69.1 | 0.186 | 14.3 | 13.8 | 1925 | 81.9 | 5.78 | Soft-Speed Separation |
| 414 | Rodriguez, Joe Joe | NEW_JER6 | Changeup | 187 | 69.1 | 0.169 | 9.0 | 14.5 | 1832 | 81.8 | 5.36 | Soft-Speed Separation |
| 415 | Lawson, Nathan | FLO_Y'A | Changeup | 107 | 68.9 | 0.196 | 8.5 | 9.2 | 1403 | 79.4 | 5.82 | Soft-Speed Separation |
| 416 | Cameron, Zach | WIN_CIT29 | Four-Seam | 144 | 68.7 | 0.198 | 15.7 | 9.9 | 2182 | 88.2 | 5.56 | Soft-Speed Separation |
| 417 | Leak, Anthony | NEW_YOR13 | Cutter | 52 | 68.6 | 0.157 | 7.7 | -1.7 | 2188 | 86.9 | 5.69 | Soft-Speed Separation |
| 418 | Campbell, Tyler | MIS_MUD | Four-Seam | 60 | 68.6 | 0.178 | 8.4 | -5.4 | 2307 | 85.2 | 6.31 | Soft-Speed Separation |
| 419 | Duncan, Tanner | DOW_EAS1 | Slider | 88 | 67.9 | 0.162 | 6.9 | -0.2 | 2208 | 86.5 | 5.91 | Soft-Speed Separation |
| 420 | Correa, Nelvin | QUE_CAP | Cutter | 139 | 67.8 | 0.172 | 11.4 | -0.7 | 2236 | 87.7 | 5.98 | Soft-Speed Separation |
| 421 | Correa, Nelvin | QUE_CAP | Four-Seam | 108 | 67.7 | 0.182 | 15.4 | 6.9 | 2129 | 89.6 | 5.96 | Soft-Speed Separation |
| 422 | Escobar, Anthony | TRO_AIG | Changeup | 195 | 67.6 | 0.169 | 10.1 | 10.9 | 1590 | 78.9 | 6.26 | Soft-Speed Separation |
| 423 | Coles, Chad | WAS_WIL3 | Splitter | 63 | 67.5 | 0.165 | 2.3 | 7.1 | 1031 | 86.2 | 5.59 | Soft-Speed Separation |
| 424 | Wiltse, Ryan | EVA_OTT | Changeup | 202 | 67.4 | 0.190 | 13.6 | 10.2 | 1834 | 78.1 | 6.30 | Soft-Speed Separation |
| 425 | Glickstein, Aaron | SCH_BOO | Sinker | 125 | 66.6 | 0.185 | 9.7 | 13.7 | 2161 | 88.2 | 6.08 | Soft-Speed Separation |
| 426 | O'Hanlon, Michael | WAS_WIL3 | Changeup | 66 | 66.4 | 0.174 | 7.3 | 13.4 | 1554 | 79.9 | 5.39 | Soft-Speed Separation |
| 427 | Harris, Everette | TRI_VAL | Changeup | 118 | 66.3 | 0.181 | 2.1 | 16.4 | 2098 | 82.6 | 6.54 | Soft-Speed Separation |
| 428 | Foy, Corbin | LAK_ERI24 | Four-Seam | 96 | 65.5 | 0.175 | 16.5 | 10.4 | 2337 | 91.3 | 6.15 | Soft-Speed Separation |
| 429 | Villers, Ian | QUE_CAP | Splitter | 64 | 65.2 | 0.218 | 7.5 | 11.5 | 1086 | 83.1 | 5.98 | Soft-Speed Separation |
| 430 | Colon, Jeffrey | TRO_AIG | Sinker | 56 | 64.6 | 0.170 | 13.9 | 17.7 | 2262 | 90.2 | 5.61 | Soft-Speed Separation |
| 431 | Drakeford, Dosie | NEW_JER6 | Changeup | 84 | 64.5 | 0.158 | 9.9 | 14.8 | 1850 | 81.0 | 6.11 | Soft-Speed Separation |
| 432 | Leak, Anthony | NEW_YOR13 | Changeup | 91 | 64.3 | 0.190 | 6.7 | 11.5 | 1736 | 83.4 | 6.53 | Soft-Speed Separation |
| 433 | Widener, Jacob | SUS_COU1 | Sinker | 192 | 64.0 | 0.191 | 8.2 | -11.0 | 2348 | 88.7 | 6.76 | Soft-Speed Separation |
| 434 | Tokar, Heitor | OTT_TIT | Changeup | 80 | 63.9 | 0.203 | 9.5 | 13.2 | 1403 | 82.1 | 6.07 | Soft-Speed Separation |
| 435 | Pindel, Buddie | SCH_BOO | Splitter | 96 | 63.6 | 0.218 | 5.3 | 7.2 | 1119 | 80.4 | 5.75 | Soft-Speed Separation |
| 436 | Earwood, Micah | SUS_COU1 | Changeup | 216 | 63.3 | 0.187 | 8.6 | 5.5 | 1843 | 79.1 | 6.19 | Soft-Speed Separation |
| 437 | Odonnell, Brendan | NEW_ENG23 | Sinker | 135 | 63.1 | 0.210 | 8.1 | -11.8 | 2344 | 90.1 | 6.89 | Soft-Speed Separation |
| 438 | Mannering, Shawn | DOW_EAS1 | Sinker | 59 | 63.1 | 0.258 | 13.5 | 18.6 | 2231 | 89.1 | 5.82 | Soft-Speed Separation |
| 439 | Hensey, Rob | SUS_COU1 | Four-Seam | 244 | 63.0 | 0.180 | 16.5 | -13.9 | 2201 | 92.2 | 6.19 | Soft-Speed Separation |
| 440 | Garcia, Andrew | EVA_OTT | Sinker | 52 | 62.7 | 0.240 | 10.5 | 14.2 | 2058 | 91.0 | 5.92 | Soft-Speed Separation |
| 441 | Lockhart, Gauge | LAK_ERI24 | Cutter | 148 | 62.6 | 0.203 | 5.9 | -0.6 | 2081 | 86.5 | 6.22 | Soft-Speed Separation |
| 442 | Sesar, Jorden | SUS_COU1 | Changeup | 99 | 62.5 | 0.173 | 12.0 | 11.7 | 1973 | 83.0 | 6.50 | Soft-Speed Separation |
| 443 | Brown, Ethan | WAS_WIL3 | Four-Seam | 67 | 61.9 | 0.216 | 12.7 | -10.8 | 2077 | 90.4 | 6.09 | Soft-Speed Separation |
| 444 | Hensey, Rob | SUS_COU1 | Slider | 113 | 61.9 | 0.199 | 5.1 | -0.5 | 2208 | 82.8 | 6.20 | Soft-Speed Separation |
| 445 | Morgan, Cooper | QUE_CAP | Four-Seam | 87 | 61.9 | 0.196 | 13.3 | -8.4 | 2203 | 87.5 | 6.13 | Soft-Speed Separation |
| 446 | Serrano, Elio | NEW_JER6 | Changeup | 101 | 61.8 | 0.191 | 10.9 | 11.5 | 1857 | 82.1 | 6.00 | Soft-Speed Separation |
| 447 | Lovell, Justin | WIN_CIT29 | Sinker | 183 | 61.8 | 0.187 | 12.5 | -15.1 | 2233 | 93.3 | 6.25 | Soft-Speed Separation |
| 448 | Zentko, Dylan | EVA_OTT | Changeup | 110 | 61.6 | 0.223 | 10.0 | -11.3 | 1420 | 79.9 | 5.79 | Soft-Speed Separation |
| 449 | Maietta, Dante | WIN_CIT29 | Changeup | 330 | 61.5 | 0.189 | 15.3 | 13.9 | 1871 | 77.7 | 6.31 | Soft-Speed Separation |
| 450 | Grills, Evan | OTT_TIT | Sinker | 55 | 61.4 | 0.206 | 15.2 | -14.1 | 2176 | 87.6 | 5.46 | Soft-Speed Separation |
| 451 | Plumadore, Carson | WIN_CIT29 | Sinker | 162 | 61.4 | 0.174 | 13.9 | 18.4 | 2381 | 87.3 | 5.82 | Soft-Speed Separation |
| 452 | Lyons, Kendall | QUE_CAP | Four-Seam | 79 | 61.4 | 0.180 | 18.5 | 11.2 | 2284 | 90.9 | 6.60 | Soft-Speed Separation |
| 453 | Cartwright, Eli | GAT_GRI | Four-Seam | 207 | 61.4 | 0.193 | 18.4 | -8.6 | 2100 | 90.3 | 6.40 | Soft-Speed Separation |
| 454 | Barreto, Brayhans | TRI_VAL | Changeup | 130 | 60.9 | 0.220 | 10.8 | -12.9 | 1789 | 81.1 | 6.16 | Soft-Speed Separation |
| 455 | Gregory, Ben | GAT_GRI | Four-Seam | 149 | 60.9 | 0.201 | 15.0 | 13.9 | 2230 | 88.4 | 6.46 | Soft-Speed Separation |
| 456 | Mercado, Nelson | OTT_TIT | Four-Seam | 81 | 60.6 | 0.169 | 19.2 | 12.6 | 2126 | 87.8 | 5.67 | Soft-Speed Separation |
| 457 | Petschke, Ben | EVA_OTT | Sinker | 59 | 60.6 | 0.206 | 6.5 | 13.0 | 2111 | 89.9 | 5.29 | Soft-Speed Separation |
| 458 | Hagan, Jack | DOW_EAS1 | Changeup | 52 | 60.6 | 0.188 | 6.0 | 17.3 | 1975 | 85.8 | 5.96 | Soft-Speed Separation |
| 459 | Garcia, Jorge | SUS_COU1 | Cutter | 58 | 60.5 | 0.185 | 16.6 | 1.8 | 2128 | 85.2 | 6.20 | Soft-Speed Separation |
| 460 | Anderson, Colt | WAS_WIL3 | Four-Seam | 315 | 59.8 | 0.219 | 11.7 | -7.1 | 2052 | 88.9 | 6.72 | Soft-Speed Separation |
| 461 | Martinez, Mason | TRI_VAL | Slider | 132 | 59.5 | 0.212 | 6.4 | 0.1 | 2349 | 83.3 | 6.40 | Soft-Speed Separation |
| 462 | Shears, Tanner | SCH_BOO | Four-Seam | 285 | 59.4 | 0.198 | 16.8 | 12.4 | 2030 | 92.2 | 5.20 | Soft-Speed Separation |
| 463 | Sabatine, Gino | TRI_VAL | Sinker | 54 | 59.4 | 0.193 | 9.5 | 14.0 | 1890 | 88.2 | 5.03 | Soft-Speed Separation |
| 464 | Kaminer, Brandon | DOW_EAS1 | Four-Seam | 185 | 59.4 | 0.226 | 18.1 | -4.8 | 2365 | 89.4 | 5.38 | Soft-Speed Separation |
| 465 | Boies, Emiles | QUE_CAP | Four-Seam | 147 | 59.2 | 0.202 | 16.9 | 8.0 | 2132 | 87.9 | 6.14 | Soft-Speed Separation |
| 466 | VanMarter, Luke | LEM_COL | Changeup | 53 | 59.0 | 0.257 | 12.9 | 11.7 | 1756 | 77.6 | 6.55 | Soft-Speed Separation |
| 467 | Langhorne, Miles | SUS_COU1 | Four-Seam | 70 | 58.9 | 0.245 | 14.2 | 3.8 | 2304 | 93.9 | 6.50 | Soft-Speed Separation |
| 468 | Duby, Bill | NEW_JER6 | Slider | 102 | 58.8 | 0.199 | 7.3 | -0.2 | 2077 | 80.1 | 6.54 | Soft-Speed Separation |
| 469 | MacMillan, Blake | TRO_AIG | Four-Seam | 152 | 58.7 | 0.200 | 21.9 | -5.8 | 2202 | 88.3 | 5.56 | Soft-Speed Separation |
| 470 | Brothers, Kellen | SUS_COU1 | Changeup | 224 | 58.7 | 0.212 | 10.3 | 12.2 | 1495 | 79.7 | 6.03 | Soft-Speed Separation |
| 471 | Willeman, Landon | EVA_OTT | Changeup | 217 | 58.6 | 0.215 | 5.9 | 14.3 | 1684 | 83.8 | 6.22 | Soft-Speed Separation |
| 472 | Saturria, Michael | NEW_ENG23 | Cutter | 264 | 58.5 | 0.232 | 12.9 | -0.6 | 2506 | 86.5 | 6.36 | Soft-Speed Separation |
| 473 | Ortiz, Julio | GAT_GRI | Four-Seam | 389 | 58.5 | 0.200 | 18.2 | 8.4 | 2184 | 95.5 | 6.13 | Soft-Speed Separation |
| 474 | Webster, Evan | FLO_Y'A | Slider | 119 | 58.5 | 0.199 | 3.2 | 0.9 | 1949 | 81.4 | 6.83 | Soft-Speed Separation |
| 475 | Foster, Kobe | WAS_WIL3 | Four-Seam | 478 | 58.4 | 0.194 | 20.7 | -9.9 | 2209 | 86.7 | 5.71 | Soft-Speed Separation |
| 476 | Kelly, Colin | SUS_COU1 | Four-Seam | 82 | 58.4 | 0.213 | 17.4 | 10.6 | 1990 | 90.6 | 5.94 | Soft-Speed Separation |
| 477 | Blowers, CJ | FLO_Y'A | Four-Seam | 165 | 58.2 | 0.208 | 17.2 | -11.4 | 1885 | 85.1 | 5.97 | Soft-Speed Separation |
| 478 | Salata, Derek | SCH_BOO | Changeup | 137 | 58.1 | 0.236 | 8.1 | 8.3 | 1615 | 81.2 | 6.00 | Soft-Speed Separation |
| 479 | Zaffiro, Cole | SCH_BOO | Four-Seam | 440 | 58.0 | 0.197 | 17.7 | 8.7 | 2160 | 90.8 | 6.13 | Soft-Speed Separation |
| 480 | Flontek, Zac | DOW_EAS1 | Cutter | 64 | 57.9 | 0.219 | 8.0 | -1.5 | 2653 | 88.8 | 6.04 | Soft-Speed Separation |
| 481 | Morgan, Marcus | JOL_SLA | Sinker | 96 | 57.9 | 0.227 | 10.3 | 15.2 | 2455 | 91.9 | 6.20 | Soft-Speed Separation |
| 482 | Kemlage, Joe | NEW_ENG23 | Four-Seam | 53 | 57.8 | 0.176 | 12.8 | -8.7 | 2447 | 92.1 | 6.04 | Soft-Speed Separation |
| 483 | McMahon, Chris | LAK_ERI24 | Four-Seam | 69 | 57.7 | 0.232 | 13.9 | 9.7 | 2266 | 88.2 | 6.54 | Soft-Speed Separation |
| 484 | Brouwer, Adam | LAK_ERI24 | Four-Seam | 50 | 57.7 | 0.204 | 18.6 | 8.4 | 2133 | 91.0 | 5.92 | Soft-Speed Separation |
| 485 | Herbert, Andrew | WAS_WIL3 | Four-Seam | 55 | 57.5 | 0.175 | 15.8 | 10.9 | 2226 | 91.2 | 6.43 | Soft-Speed Separation |
| 486 | Garcia, Brett | OTT_TIT | Four-Seam | 326 | 57.4 | 0.211 | 16.7 | 6.2 | 2379 | 91.9 | 6.10 | Soft-Speed Separation |
| 487 | Lawson, Nathan | FLO_Y'A | Sinker | 276 | 57.3 | 0.210 | 9.8 | 15.7 | 2181 | 88.8 | 6.15 | Soft-Speed Separation |
| 488 | Dima, Josh | GAT_GRI | Four-Seam | 295 | 57.3 | 0.209 | 17.9 | -10.9 | 2047 | 90.2 | 6.19 | Soft-Speed Separation |
| 489 | Culley, Wesley | LAK_ERI24 | Four-Seam | 86 | 57.2 | 0.200 | 14.3 | -12.4 | 2106 | 89.6 | 5.30 | Soft-Speed Separation |
| 490 | Grounds, Jackson | DOW_EAS1 | Sinker | 116 | 57.0 | 0.215 | 15.0 | 16.4 | 2139 | 92.2 | 5.50 | Soft-Speed Separation |
| 491 | Cameron, Zach | WIN_CIT29 | Changeup | 249 | 57.0 | 0.216 | 7.7 | 20.9 | 2125 | 80.5 | 5.56 | Soft-Speed Separation |
| 492 | Marynczak, Arlo | TRI_VAL | Changeup | 200 | 56.9 | 0.234 | 6.8 | 13.2 | 1679 | 81.7 | 6.29 | Soft-Speed Separation |
| 493 | Long, Maddox | WAS_WIL3 | Four-Seam | 155 | 56.7 | 0.221 | 12.7 | 9.4 | 2343 | 91.7 | 6.13 | Soft-Speed Separation |
| 494 | Flontek, Zac | DOW_EAS1 | Four-Seam | 453 | 56.7 | 0.183 | 18.4 | 5.2 | 2601 | 91.8 | 6.46 | Soft-Speed Separation |
| 495 | Riedel, Caleb | SCH_BOO | Four-Seam | 315 | 56.7 | 0.235 | 17.1 | -15.1 | 2318 | 89.5 | 5.87 | Soft-Speed Separation |
| 496 | McCartney, Seth | MIS_MUD | Sinker | 120 | 56.6 | 0.238 | 10.4 | 15.2 | 2316 | 90.2 | 5.76 | Soft-Speed Separation |
| 497 | Daly, Ryan | JOL_SLA | Changeup | 287 | 56.6 | 0.231 | 5.3 | 16.3 | 2115 | 79.1 | 6.81 | Soft-Speed Separation |
| 498 | Williams, Pierce | NEW_ENG23 | Four-Seam | 342 | 56.6 | 0.217 | 16.4 | -11.6 | 1916 | 85.6 | 6.16 | Soft-Speed Separation |
| 499 | Savinon, Jordan | NEW_YOR13 | Cutter | 56 | 56.5 | 0.243 | 8.7 | -2.7 | 2196 | 87.4 | 6.13 | Soft-Speed Separation |
| 500 | Good, Ty | GAT_GRI | Cutter | 66 | 56.4 | 0.216 | 17.0 | 7.6 | 2054 | 88.3 | 6.15 | Soft-Speed Separation |
| 501 | Luera, Ashton | QUE_CAP | Four-Seam | 65 | 56.3 | 0.233 | 19.4 | 7.1 | 1910 | 87.3 | 6.05 | Soft-Speed Separation |
| 502 | Debban, Caleb | NEW_JER6 | Cutter | 145 | 56.3 | 0.237 | 10.7 | -0.5 | 2336 | 85.9 | 6.59 | Soft-Speed Separation |
| 503 | Jones, Breyln | NEW_JER6 | Slider | 104 | 56.3 | 0.214 | 8.2 | -0.6 | 2073 | 86.1 | 5.86 | Soft-Speed Separation |
| 504 | Dill, Austin | TRI_VAL | Changeup | 204 | 56.2 | 0.208 | 10.7 | 16.5 | 1931 | 80.5 | 5.23 | Soft-Speed Separation |
| 505 | Vilchez, Michael | OTT_TIT | Four-Seam | 224 | 56.1 | 0.200 | 16.3 | 9.6 | 2263 | 93.6 | 6.18 | Soft-Speed Separation |
| 506 | Kowalski, Benjamin | WAS_WIL3 | Changeup | 51 | 56.0 | 0.236 | 4.7 | 11.1 | 1315 | 80.7 | 5.87 | Soft-Speed Separation |
| 507 | Lodes, Jett | FLO_Y'A | Sinker | 96 | 55.9 | 0.218 | 4.4 | 13.9 | 2107 | 89.6 | 5.29 | Soft-Speed Separation |
| 508 | Long, Maddox | WAS_WIL3 | Sinker | 285 | 55.9 | 0.233 | 7.1 | 16.6 | 2182 | 89.9 | 5.89 | Soft-Speed Separation |
| 509 | Fauci, Sonny | NEW_JER6 | Sinker | 122 | 55.8 | 0.219 | 14.4 | 15.9 | 2227 | 92.7 | 6.54 | Soft-Speed Separation |
| 510 | Burcham, Jacob | GAT_GRI | Changeup | 118 | 55.8 | 0.204 | 3.4 | 17.9 | 1906 | 83.5 | 6.18 | Soft-Speed Separation |
| 511 | Wiltse, Ryan | EVA_OTT | Cutter | 68 | 55.8 | 0.218 | 8.3 | -0.6 | 1939 | 80.8 | 6.02 | Soft-Speed Separation |
| 512 | Thompson, Ross | SCH_BOO | Splitter | 221 | 55.6 | 0.227 | 3.6 | 8.7 | 1049 | 79.1 | 5.45 | Soft-Speed Separation |
| 513 | Bell, Brendan | NEW_ENG23 | Four-Seam | 153 | 55.6 | 0.262 | 11.2 | 3.2 | 2365 | 92.1 | 5.96 | Soft-Speed Separation |
| 514 | Hensey, Rob | SUS_COU1 | Changeup | 290 | 55.6 | 0.230 | 6.4 | -15.9 | 1698 | 84.1 | 6.12 | Soft-Speed Separation |
| 515 | Milburn, Isaac | FLO_Y'A | Sinker | 137 | 55.6 | 0.233 | 10.0 | -13.1 | 2092 | 88.2 | 5.48 | Soft-Speed Separation |
| 516 | Brouwer, Adam | LAK_ERI24 | Four-Seam | 264 | 55.6 | 0.195 | 19.3 | 10.5 | 2261 | 90.6 | 5.88 | Soft-Speed Separation |
| 517 | Fritz, AJ | MIS_MUD | Sinker | 55 | 55.6 | 0.237 | 6.8 | 16.5 | 2042 | 88.4 | 5.39 | Soft-Speed Separation |
| 518 | Soto, Noel | TRI_VAL | Changeup | 61 | 55.5 | 0.255 | 5.4 | 15.2 | 1645 | 83.0 | 5.57 | Soft-Speed Separation |
| 519 | Turner, Eric | JOL_SLA | Sinker | 113 | 55.5 | 0.209 | 14.9 | 16.1 | 2318 | 88.2 | 5.09 | Soft-Speed Separation |
| 520 | Gorgen, Grady | NEW_YOR13 | Cutter | 83 | 55.4 | 0.203 | 8.1 | -3.6 | 2126 | 86.5 | 6.27 | Soft-Speed Separation |
| 521 | Boies, Emiles | QUE_CAP | Changeup | 275 | 55.4 | 0.210 | 11.5 | 14.7 | 1906 | 82.5 | 6.20 | Soft-Speed Separation |
| 522 | Melendez, Omar | NEW_ENG23 | Four-Seam | 101 | 55.4 | 0.226 | 19.0 | -3.9 | 2140 | 82.3 | 6.95 | Soft-Speed Separation |
| 523 | Leak, Anthony | NEW_YOR13 | Sinker | 154 | 55.3 | 0.230 | 10.4 | 14.2 | 2110 | 89.4 | 6.27 | Soft-Speed Separation |
| 524 | Barrett, Gabriel | NEW_YOR13 | Sinker | 60 | 55.3 | 0.209 | 11.0 | 14.4 | 2012 | 91.2 | 5.70 | Soft-Speed Separation |
| 525 | Henderson, Drew | DOW_EAS1 | Sinker | 145 | 55.2 | 0.221 | 16.1 | 15.5 | 2218 | 89.0 | 5.58 | Soft-Speed Separation |
| 526 | Tiburcio, David | DOW_EAS1 | Four-Seam | 78 | 55.1 | 0.219 | 16.7 | 13.4 | 2270 | 93.7 | 5.19 | Soft-Speed Separation |
| 527 | Shinn, Nathan | LAK_ERI24 | Four-Seam | 250 | 55.1 | 0.214 | 17.4 | -9.5 | 1970 | 89.1 | 5.88 | Soft-Speed Separation |
| 528 | Scafidi, Christian | LAK_ERI24 | Four-Seam | 358 | 55.0 | 0.205 | 17.9 | 5.1 | 2498 | 90.0 | 6.15 | Soft-Speed Separation |
| 529 | MacMillan, Blake | TRO_AIG | Cutter | 150 | 54.8 | 0.207 | 21.9 | -6.9 | 2195 | 88.0 | 5.53 | Soft-Speed Separation |
| 530 | McKillican, Adam | QUE_CAP | Changeup | 70 | 54.8 | 0.211 | 10.3 | 13.1 | 1714 | 85.5 | 6.79 | Soft-Speed Separation |
| 531 | Calderon, Jean | LAK_ERI24 | Four-Seam | 87 | 54.8 | 0.241 | 12.0 | 0.8 | 2526 | 94.1 | 6.38 | Soft-Speed Separation |
| 532 | Campbell, Tyler | MIS_MUD | Cutter | 256 | 54.8 | 0.232 | 7.9 | -3.4 | 2242 | 84.1 | 6.03 | Soft-Speed Separation |
| 533 | Hagan, Jack | DOW_EAS1 | Four-Seam | 98 | 54.8 | 0.175 | 13.5 | 12.9 | 2392 | 91.6 | 6.01 | Soft-Speed Separation |
| 534 | Moore, Kyle | SCH_BOO | Four-Seam | 203 | 54.7 | 0.221 | 17.9 | 14.1 | 2167 | 88.2 | 4.71 | Soft-Speed Separation |
| 535 | Rodriguez, Joe Joe | NEW_JER6 | Four-Seam | 157 | 54.6 | 0.208 | 16.4 | 13.3 | 2159 | 91.3 | 5.79 | Soft-Speed Separation |
| 536 | Widener, Jacob | SUS_COU1 | Four-Seam | 152 | 54.5 | 0.237 | 10.1 | -7.3 | 2359 | 88.9 | 6.67 | Soft-Speed Separation |
| 537 | Hensey, Rob | SUS_COU1 | Sinker | 515 | 54.5 | 0.228 | 13.5 | -16.0 | 2144 | 91.7 | 6.22 | Soft-Speed Separation |
| 538 | Kines, Gunnar | JOL_SLA | Four-Seam | 710 | 54.5 | 0.213 | 17.5 | -12.5 | 2238 | 86.3 | 5.86 | Soft-Speed Separation |
| 539 | Kelly, Colin | SUS_COU1 | Sinker | 96 | 54.3 | 0.189 | 14.3 | 15.8 | 2008 | 90.5 | 5.91 | Soft-Speed Separation |
| 540 | Vega, Lucas | TRO_AIG | Changeup | 74 | 54.3 | 0.273 | 8.6 | 14.7 | 1967 | 83.6 | 6.24 | Soft-Speed Separation |
| 541 | Salata, Derek | SCH_BOO | Splitter | 102 | 54.3 | 0.212 | 5.8 | 8.6 | 1116 | 83.1 | 5.72 | Soft-Speed Separation |
| 542 | Plumadore, Carson | WIN_CIT29 | Changeup | 330 | 54.3 | 0.214 | 8.7 | 18.6 | 2255 | 83.3 | 5.92 | Soft-Speed Separation |
| 543 | Ronne, Andrew | GAT_GRI | Four-Seam | 318 | 54.2 | 0.218 | 13.1 | 7.2 | 2180 | 91.8 | 6.34 | Soft-Speed Separation |
| 544 | Morgan, Cooper | QUE_CAP | Sinker | 153 | 54.2 | 0.215 | 12.0 | -12.4 | 2170 | 87.7 | 6.23 | Soft-Speed Separation |
| 545 | Barker, Alex | NEW_YOR13 | Changeup | 189 | 54.2 | 0.241 | 5.3 | -12.0 | 1542 | 82.7 | 6.07 | Soft-Speed Separation |
| 546 | McEvoy, Aidan | FLO_Y'A | Cutter | 110 | 54.1 | 0.229 | 7.9 | 0.8 | 2153 | 83.3 | 6.16 | Soft-Speed Separation |
| 547 | Ronne, Andrew | GAT_GRI | Changeup | 51 | 54.1 | 0.220 | 4.7 | 14.5 | 1507 | 85.3 | 5.95 | Soft-Speed Separation |
| 548 | Aldeano, Austin | TRO_AIG | Sinker | 70 | 54.1 | 0.217 | 16.0 | 17.8 | 2219 | 90.2 | 6.06 | Soft-Speed Separation |
| 549 | Garcia, Jorge | SUS_COU1 | Four-Seam | 343 | 54.0 | 0.205 | 16.6 | 4.6 | 2153 | 86.4 | 6.07 | Soft-Speed Separation |
| 550 | Sanchez, Edwin | LAK_ERI24 | Four-Seam | 205 | 54.0 | 0.204 | 15.7 | -13.3 | 2103 | 87.2 | 5.53 | Soft-Speed Separation |
| 551 | Roland, Cole | QUE_CAP | Changeup | 71 | 54.0 | 0.244 | 10.4 | 9.6 | 2033 | 82.6 | 5.56 | Soft-Speed Separation |
| 552 | Barraza, Chris | MIS_MUD | Four-Seam | 687 | 53.9 | 0.186 | 20.0 | 10.2 | 2447 | 93.1 | 5.85 | Soft-Speed Separation |
| 553 | Almanzar, Elian | DOW_EAS1 | Four-Seam | 147 | 53.9 | 0.196 | 16.0 | 3.7 | 2279 | 95.1 | 6.18 | Soft-Speed Separation |
| 554 | Grounds, Jackson | TRO_AIG | Four-Seam | 119 | 53.9 | 0.196 | 14.8 | 11.3 | 2221 | 92.3 | 5.93 | Soft-Speed Separation |
| 555 | Alpern, Liam | FLO_Y'A | Four-Seam | 264 | 53.8 | 0.215 | 17.2 | -12.7 | 2227 | 89.1 | 6.04 | Soft-Speed Separation |
| 556 | McEvoy, Aidan | FLO_Y'A | Sinker | 239 | 53.8 | 0.212 | 12.7 | -16.5 | 1969 | 90.5 | 6.47 | Soft-Speed Separation |
| 557 | Daly, Ryan | JOL_SLA | Four-Seam | 695 | 53.8 | 0.231 | 14.7 | 13.5 | 2208 | 90.4 | 6.80 | Soft-Speed Separation |
| 558 | Long, Jalon | NEW_YOR13 | Four-Seam | 267 | 53.7 | 0.202 | 20.3 | 8.2 | 2127 | 92.1 | 6.05 | Soft-Speed Separation |
| 559 | Hungate, Chase | NEW_JER6 | Sinker | 135 | 53.7 | 0.225 | -0.1 | 19.9 | 2241 | 88.4 | 5.91 | Soft-Speed Separation |
| 560 | Hopewell, Chase | FLO_Y'A | Four-Seam | 300 | 53.7 | 0.211 | 16.4 | 11.2 | 2211 | 92.4 | 6.54 | Soft-Speed Separation |
| 561 | Gregory, Ben | GAT_GRI | Sinker | 227 | 53.6 | 0.211 | 14.7 | 15.9 | 2260 | 89.1 | 6.54 | Soft-Speed Separation |
| 562 | Martinez, Mason | TRI_VAL | Sinker | 347 | 53.6 | 0.231 | 12.1 | 18.9 | 2279 | 88.8 | 6.45 | Soft-Speed Separation |
| 563 | Wehrle, Tyler | WIN_CIT29 | Four-Seam | 396 | 53.5 | 0.211 | 16.3 | 13.0 | 2340 | 91.8 | 5.68 | Soft-Speed Separation |
| 564 | Perez, Kelvin | WAS_WIL3 | Four-Seam | 151 | 53.4 | 0.224 | 15.1 | 11.2 | 2065 | 88.8 | 6.17 | Soft-Speed Separation |
| 565 | Glickstein, Aaron | SCH_BOO | Four-Seam | 266 | 53.4 | 0.214 | 14.6 | 9.6 | 2217 | 88.9 | 6.09 | Soft-Speed Separation |
| 566 | McEvoy, Aidan | FLO_Y'A | Four-Seam | 63 | 53.3 | 0.204 | 14.4 | -15.0 | 1967 | 90.1 | 6.45 | Soft-Speed Separation |
| 567 | Delaney, Carter | WIN_CIT29 | Four-Seam | 181 | 53.3 | 0.234 | 17.9 | 9.5 | 2219 | 89.1 | 6.30 | Soft-Speed Separation |
| 568 | De Jesus, Larry | DOW_EAS1 | Four-Seam | 97 | 53.3 | 0.217 | 16.8 | 12.4 | 2407 | 89.7 | 5.25 | Soft-Speed Separation |
| 569 | Westcott, Zac | FLO_Y'A | Four-Seam | 327 | 53.3 | 0.216 | 16.5 | 14.5 | 2099 | 83.4 | 5.90 | Soft-Speed Separation |
| 570 | Hickey, Matt | GAT_GRI | Sinker | 82 | 53.2 | 0.231 | 5.5 | 17.8 | 2259 | 88.5 | 5.64 | Soft-Speed Separation |
| 571 | Whitesell, Max | FLO_Y'A | Four-Seam | 239 | 53.1 | 0.226 | 14.0 | 12.7 | 1910 | 88.8 | 6.41 | Soft-Speed Separation |
| 572 | Jones, Breyln | NEW_JER6 | Four-Seam | 60 | 53.1 | 0.265 | 13.4 | 6.1 | 1990 | 88.9 | 5.89 | Soft-Speed Separation |
| 573 | Albert, Wes | TRI_VAL | Four-Seam | 125 | 53.0 | 0.192 | 16.1 | 9.3 | 2014 | 89.1 | 5.65 | Soft-Speed Separation |
| 574 | Simone, Andrew | TRO_AIG | Changeup | 108 | 52.8 | 0.219 | 9.8 | 13.0 | 1681 | 85.3 | 5.94 | Soft-Speed Separation |
| 575 | Soto, Noel | TRI_VAL | Four-Seam | 92 | 52.7 | 0.231 | 19.4 | 11.4 | 2097 | 87.8 | 5.51 | Soft-Speed Separation |
| 576 | Daly, Ryan | JOL_SLA | Sinker | 182 | 52.7 | 0.224 | 12.7 | 15.6 | 2201 | 90.0 | 6.83 | Soft-Speed Separation |
| 577 | Whitesell, Max | FLO_Y'A | Cutter | 65 | 52.7 | 0.234 | 10.9 | 0.8 | 2027 | 82.3 | 6.32 | Soft-Speed Separation |
| 578 | Fowler, Dalton | SUS_COU1 | Four-Seam | 89 | 52.7 | 0.232 | 14.6 | -10.9 | 2107 | 92.2 | 5.57 | Soft-Speed Separation |
| 579 | Hughes, Grif | EVA_OTT | Four-Seam | 57 | 52.6 | 0.188 | 17.7 | -12.9 | 2419 | 88.0 | 6.38 | Soft-Speed Separation |
| 580 | Vecerka, Boris | QUE_CAP | Sinker | 232 | 52.6 | 0.208 | 10.3 | 17.7 | 2434 | 93.4 | 5.89 | Soft-Speed Separation |
| 581 | Hernandez, Nyan | NEW_JER6 | Changeup | 242 | 52.6 | 0.216 | 11.7 | 16.0 | 1922 | 82.1 | 6.32 | Soft-Speed Separation |
| 582 | Vailes, Gage | GAT_GRI | Changeup | 195 | 52.5 | 0.240 | 6.1 | 11.5 | 1883 | 85.6 | 5.12 | Soft-Speed Separation |
| 583 | Stuka, Ted | OTT_TIT | Sinker | 225 | 52.5 | 0.223 | 11.8 | 19.5 | 2324 | 95.1 | 5.23 | Soft-Speed Separation |
| 584 | Agosto, Justus | TRI_VAL | Changeup | 65 | 52.5 | 0.246 | 10.7 | 9.6 | 1721 | 81.1 | 5.87 | Soft-Speed Separation |
| 585 | Vail, Tyler | NEW_YOR13 | Sinker | 60 | 52.4 | 0.236 | 7.6 | 13.7 | 2040 | 87.8 | 5.93 | Soft-Speed Separation |
| 586 | Hungate, Chase | NEW_JER6 | Changeup | 56 | 52.4 | 0.291 | -1.5 | 16.4 | 1705 | 81.1 | 6.37 | Soft-Speed Separation |
| 587 | Benitez, Jorge | NEW_JER6 | Sinker | 209 | 52.4 | 0.214 | 9.3 | -12.6 | 2195 | 93.2 | 6.17 | Soft-Speed Separation |
| 588 | Hargrove, Dawson | LAK_ERI24 | Four-Seam | 188 | 52.4 | 0.226 | 19.3 | 7.6 | 1980 | 89.4 | 5.47 | Soft-Speed Separation |
| 589 | Castro, Alexander | TRO_AIG | Changeup | 75 | 52.3 | 0.237 | 5.9 | 10.7 | 1336 | 83.4 | 6.08 | Soft-Speed Separation |
| 590 | Anglin, Mack | WAS_WIL3 | Four-Seam | 76 | 52.2 | 0.238 | 16.1 | 9.4 | 2418 | 94.1 | 6.08 | Soft-Speed Separation |
| 591 | Catrambone, Ben | JOL_SLA | Four-Seam | 214 | 52.2 | 0.212 | 20.1 | 8.8 | 2123 | 87.9 | 5.13 | Soft-Speed Separation |
| 592 | Cerda, Junior | EVA_OTT | Four-Seam | 132 | 52.2 | 0.225 | 15.3 | 15.7 | 2230 | 93.2 | 5.52 | Soft-Speed Separation |
| 593 | Maher, Adam | TRI_VAL | Four-Seam | 319 | 52.2 | 0.214 | 20.4 | -9.7 | 2076 | 87.8 | 5.85 | Soft-Speed Separation |
| 594 | Harley, Tristan | SUS_COU1 | Four-Seam | 102 | 52.2 | 0.229 | 13.6 | 15.6 | 2039 | 91.9 | 5.78 | Soft-Speed Separation |
| 595 | Ryan, Dillon | NEW_ENG23 | Sinker | 281 | 52.1 | 0.237 | 12.2 | 16.2 | 2330 | 91.3 | 6.25 | Soft-Speed Separation |
| 596 | Whitesell, Max | FLO_Y'A | Changeup | 71 | 52.1 | 0.257 | 9.0 | 10.9 | 1630 | 85.5 | 6.44 | Soft-Speed Separation |
| 597 | Agosto, Justus | TRI_VAL | Four-Seam | 109 | 52.0 | 0.213 | 17.1 | 8.1 | 2006 | 89.4 | 6.03 | Soft-Speed Separation |
| 598 | Webster, Evan | FLO_Y'A | Four-Seam | 639 | 52.0 | 0.214 | 16.5 | -10.9 | 1966 | 89.1 | 6.81 | Soft-Speed Separation |
| 599 | Kelly, Aiden | TRI_VAL | Sinker | 78 | 52.0 | 0.242 | 9.3 | 13.8 | 2221 | 88.8 | 5.90 | Soft-Speed Separation |
| 600 | Wilson, Bradley | FLO_Y'A | Four-Seam | 60 | 51.9 | 0.215 | 12.5 | 5.0 | 2261 | 92.2 | 6.77 | Soft-Speed Separation |
| 601 | Castro, Alexander | TRO_AIG | Sinker | 57 | 51.9 | 0.211 | 15.8 | 16.9 | 2193 | 93.4 | 5.26 | Soft-Speed Separation |
| 602 | Morse, Colby | EVA_OTT | Four-Seam | 86 | 51.9 | 0.206 | 15.1 | 10.5 | 2368 | 89.3 | 6.42 | Soft-Speed Separation |
| 603 | Sanchez, Sergio | MIS_MUD | Four-Seam | 311 | 51.9 | 0.217 | 15.4 | 11.2 | 2286 | 91.5 | 6.21 | Soft-Speed Separation |
| 604 | Marynczak, Arlo | TRI_VAL | Four-Seam | 378 | 51.9 | 0.223 | 17.0 | 10.9 | 2156 | 89.1 | 6.37 | Soft-Speed Separation |
| 605 | Almonte, Lisandro | NEW_JER6 | Four-Seam | 210 | 51.9 | 0.208 | 16.4 | 12.7 | 2195 | 96.6 | 5.67 | Soft-Speed Separation |
| 606 | Balzan, Jackson | SUS_COU1 | Sinker | 142 | 51.9 | 0.219 | 17.3 | -14.6 | 2224 | 86.1 | 5.28 | Soft-Speed Separation |
| 607 | Stegura, Drew | WAS_WIL3 | Four-Seam | 77 | 51.8 | 0.234 | 18.3 | 6.2 | 2003 | 88.5 | 6.36 | Soft-Speed Separation |
| 608 | Martinez, Gregory | DOW_EAS1 | Four-Seam | 149 | 51.7 | 0.262 | 16.4 | 13.1 | 2329 | 95.1 | 5.59 | Soft-Speed Separation |
| 609 | Darden, Nathan | FLO_Y'A | Four-Seam | 151 | 51.7 | 0.244 | 15.8 | 7.6 | 1935 | 91.6 | 5.38 | Soft-Speed Separation |
| 610 | Bell, Brendan | NEW_ENG23 | Cutter | 124 | 51.7 | 0.243 | 9.2 | -0.4 | 2395 | 92.0 | 5.74 | Soft-Speed Separation |
| 611 | Johnston, Spencer | DOW_EAS1 | Changeup | 319 | 51.6 | 0.234 | 8.6 | 9.9 | 1605 | 77.5 | 5.95 | Soft-Speed Separation |
| 612 | Sittinger, Brandyn | LAK_ERI24 | Four-Seam | 302 | 51.5 | 0.233 | 17.5 | 13.4 | 2299 | 94.7 | 5.68 | Soft-Speed Separation |
| 613 | Odonnell, Brendan | NEW_ENG23 | Four-Seam | 76 | 51.5 | 0.259 | 13.2 | -7.4 | 2448 | 91.3 | 6.94 | Soft-Speed Separation |
| 614 | Kirby, Zach | WAS_WIL3 | Changeup | 122 | 51.5 | 0.226 | 9.9 | 15.4 | 1690 | 79.8 | 6.07 | Soft-Speed Separation |
| 615 | Rodriguez, Esteban | TRO_AIG | Four-Seam | 142 | 51.5 | 0.232 | 16.8 | 5.0 | 2157 | 88.7 | 5.81 | Soft-Speed Separation |
| 616 | Tokar, Heitor | OTT_TIT | Four-Seam | 265 | 51.4 | 0.225 | 17.4 | 6.4 | 2014 | 88.1 | 6.36 | Soft-Speed Separation |
| 617 | Brothers, Kellen | SUS_COU1 | Four-Seam | 446 | 51.4 | 0.233 | 18.1 | 14.5 | 2350 | 89.2 | 6.44 | Soft-Speed Separation |
| 618 | Peyton, Blake | GAT_GRI | Four-Seam | 339 | 51.4 | 0.214 | 18.1 | -13.0 | 2274 | 89.2 | 5.94 | Soft-Speed Separation |
| 619 | Scott, Brandon | LAK_ERI24 | Four-Seam | 472 | 51.4 | 0.230 | 13.4 | -8.8 | 2304 | 88.8 | 6.19 | Soft-Speed Separation |
| 620 | Thebiay, Nolan | EVA_OTT | Four-Seam | 593 | 51.2 | 0.218 | 17.5 | 9.1 | 2279 | 89.5 | 6.84 | Soft-Speed Separation |
| 621 | Kirby, Zach | WAS_WIL3 | Four-Seam | 350 | 51.1 | 0.230 | 20.2 | 7.2 | 2174 | 87.8 | 6.12 | Soft-Speed Separation |
| 622 | Maietta, Dante | WIN_CIT29 | Slider | 145 | 51.1 | 0.254 | 7.3 | -1.5 | 2072 | 81.0 | 6.27 | Soft-Speed Separation |
| 623 | Zaffiro, Cole | SCH_BOO | Changeup | 90 | 50.9 | 0.239 | 4.0 | 16.3 | 1795 | 80.2 | 5.91 | Soft-Speed Separation |
| 624 | Bauer, Patrick | QUE_CAP | Four-Seam | 222 | 50.8 | 0.203 | 17.8 | 10.6 | 2436 | 88.0 | 6.59 | Soft-Speed Separation |
| 625 | Johnson, Caiden | OTT_TIT | Sinker | 84 | 50.8 | 0.238 | 12.8 | -15.5 | 2225 | 90.0 | 5.95 | Soft-Speed Separation |
| 626 | Harley, Tristan | SUS_COU1 | Sinker | 177 | 50.8 | 0.231 | 12.4 | 15.6 | 2026 | 91.5 | 5.71 | Soft-Speed Separation |
| 627 | Petschke, Ben | EVA_OTT | Four-Seam | 236 | 50.8 | 0.249 | 11.7 | 5.3 | 2254 | 89.7 | 5.51 | Soft-Speed Separation |
| 628 | Brothers, Kellen | SUS_COU1 | Sinker | 236 | 50.8 | 0.226 | 16.0 | 16.3 | 2338 | 89.0 | 6.37 | Soft-Speed Separation |
| 629 | Foltz Jr., Michael | WAS_WIL3 | Four-Seam | 326 | 50.7 | 0.243 | 18.8 | -3.8 | 2189 | 92.5 | 6.03 | Soft-Speed Separation |
| 630 | Harris, Ben | GAT_GRI | Changeup | 407 | 50.7 | 0.245 | 8.7 | 15.9 | 1791 | 82.6 | 5.59 | Soft-Speed Separation |
| 631 | Ferguson, Francis | QUE_CAP | Four-Seam | 129 | 50.7 | 0.230 | 14.7 | -8.1 | 2190 | 90.1 | 5.70 | Soft-Speed Separation |
| 632 | Gilleran, Jimmy | NEW_ENG23 | Sinker | 297 | 50.6 | 0.249 | 11.6 | 15.9 | 2089 | 87.7 | 5.55 | Soft-Speed Separation |
| 633 | Rivas, Albert | GAT_GRI | Four-Seam | 71 | 50.6 | 0.241 | 16.7 | 13.9 | 2370 | 89.9 | 5.82 | Soft-Speed Separation |
| 634 | Vega, Lucas | TRO_AIG | Four-Seam | 124 | 50.5 | 0.225 | 11.7 | 10.1 | 2081 | 89.8 | 6.13 | Soft-Speed Separation |
| 635 | Primeaux, Parker | SUS_COU1 | Changeup | 102 | 50.5 | 0.247 | 0.8 | 17.7 | 2014 | 85.9 | 5.57 | Soft-Speed Separation |
| 636 | Zeplin, Blane | JOL_SLA | Four-Seam | 236 | 50.4 | 0.217 | 18.6 | 9.0 | 2288 | 89.7 | 5.93 | Soft-Speed Separation |
| 637 | Hickey, Matt | GAT_GRI | Four-Seam | 117 | 50.4 | 0.223 | 16.3 | 11.5 | 2310 | 90.1 | 5.51 | Soft-Speed Separation |
| 638 | Cook, Avery | WIN_CIT29 | Sinker | 113 | 50.4 | 0.238 | -0.1 | 16.3 | 2187 | 88.4 | 6.56 | Soft-Speed Separation |
| 639 | Geshel, James | JOL_SLA | Four-Seam | 87 | 50.4 | 0.206 | 18.9 | 9.1 | 2235 | 88.8 | 5.91 | Soft-Speed Separation |
| 640 | O'Dell, Casey | JOL_SLA | Four-Seam | 170 | 50.4 | 0.223 | 17.3 | 9.1 | 2216 | 90.9 | 6.05 | Soft-Speed Separation |
| 641 | Langrell, Connor | MIS_MUD | Cutter | 352 | 50.3 | 0.232 | 9.3 | -0.7 | 2286 | 86.1 | 6.14 | Soft-Speed Separation |
| 642 | Brodsky, Jack | WAS_WIL3 | Four-Seam | 447 | 50.2 | 0.232 | 15.0 | 6.3 | 2153 | 89.8 | 6.27 | Soft-Speed Separation |
| 643 | Kines, Gunnar | JOL_SLA | Sinker | 113 | 50.2 | 0.240 | 17.3 | -12.7 | 2195 | 84.7 | 5.85 | Soft-Speed Separation |
| 644 | Hoeymans, Jack | GAT_GRI | Sinker | 66 | 50.1 | 0.221 | 7.4 | 15.1 | 2157 | 89.4 | 6.32 | Soft-Speed Separation |
| 645 | Delongchamp, Luke | TRI_VAL | Changeup | 426 | 50.1 | 0.237 | 7.8 | 15.7 | 1862 | 82.2 | 5.65 | Soft-Speed Separation |
| 646 | Carsten, Will | FLO_Y'A | Sinker | 84 | 50.1 | 0.219 | 13.2 | 18.0 | 2246 | 91.6 | 5.79 | Soft-Speed Separation |
| 647 | Hocom, Quinn | TRI_VAL | Four-Seam | 359 | 50.1 | 0.241 | 21.0 | 10.3 | 2176 | 89.0 | 5.99 | Soft-Speed Separation |
| 648 | Johnson, Preston | MIS_MUD | Four-Seam | 90 | 50.0 | 0.197 | 20.3 | 6.9 | 2368 | 92.2 | 6.33 | Soft-Speed Separation |
| 649 | Baird, Dustin | MIS_MUD | Four-Seam | 81 | 50.0 | 0.247 | 14.4 | 13.4 | 2056 | 89.5 | 5.99 | Soft-Speed Separation |
| 650 | Vail, Tyler | NEW_YOR13 | Changeup | 228 | 49.9 | 0.255 | 6.2 | 13.2 | 1779 | 83.2 | 6.20 | Soft-Speed Separation |
| 651 | Eisenbarger, Jack | QUE_CAP | Four-Seam | 406 | 49.8 | 0.235 | 18.9 | -13.8 | 2545 | 90.0 | 5.78 | Soft-Speed Separation |
| 652 | Cameron, Wyatt | TRI_VAL | Four-Seam | 69 | 49.8 | 0.253 | 16.3 | 11.4 | 2253 | 91.6 | 5.50 | Soft-Speed Separation |
| 653 | Good, Ty | GAT_GRI | Four-Seam | 572 | 49.8 | 0.220 | 18.6 | 5.0 | 2094 | 89.2 | 6.19 | Soft-Speed Separation |
| 654 | Kalisky, Jack | OTT_TIT | Four-Seam | 99 | 49.8 | 0.215 | 13.4 | 7.7 | 2398 | 88.4 | 5.76 | Soft-Speed Separation |
| 655 | Zentko, Dylan | EVA_OTT | Four-Seam | 238 | 49.8 | 0.239 | 17.5 | -8.1 | 1946 | 86.8 | 5.67 | Soft-Speed Separation |
| 656 | Phelps, Travis | FLO_Y'A | Four-Seam | 154 | 49.7 | 0.246 | 15.3 | 6.9 | 2131 | 91.1 | 6.39 | Soft-Speed Separation |
| 657 | Hill, Kaleb | OTT_TIT | Four-Seam | 58 | 49.6 | 0.236 | 14.2 | -10.0 | 1952 | 89.6 | 5.53 | Soft-Speed Separation |
| 658 | Parra, Andres | LAK_ERI24 | Four-Seam | 241 | 49.6 | 0.240 | 14.2 | -13.0 | 2044 | 88.4 | 6.07 | Soft-Speed Separation |
| 659 | Pardinho, Eric | OTT_TIT | Changeup | 182 | 49.5 | 0.254 | 4.3 | 14.5 | 1562 | 83.7 | 5.37 | Soft-Speed Separation |
| 660 | Kostura, Brit | WAS_WIL3 | Four-Seam | 77 | 49.5 | 0.252 | 16.4 | -14.5 | 2069 | 85.3 | 5.66 | Soft-Speed Separation |
| 661 | Primeaux, Parker | SUS_COU1 | Sinker | 120 | 49.4 | 0.227 | -0.2 | 18.7 | 2062 | 87.5 | 5.51 | Soft-Speed Separation |
| 662 | Toribio, Noe | TRO_AIG | Changeup | 373 | 49.4 | 0.255 | 6.9 | 16.7 | 1976 | 83.2 | 5.63 | Soft-Speed Separation |
| 663 | Traver, Eliott | LAK_ERI24 | Sinker | 65 | 49.3 | 0.203 | 8.8 | 16.7 | 2147 | 80.7 | 5.77 | Soft-Speed Separation |
| 664 | Albert, Wes | DOW_EAS1 | Changeup | 94 | 49.3 | 0.263 | 11.8 | 12.8 | 1807 | 82.5 | 6.00 | Soft-Speed Separation |
| 665 | Binns, Malik | NEW_JER6 | Cutter | 88 | 49.3 | 0.212 | 9.5 | -1.9 | 2229 | 88.9 | 6.18 | Soft-Speed Separation |
| 666 | Marklund, Brandon | OTT_TIT | Four-Seam | 279 | 49.3 | 0.239 | 16.9 | 10.5 | 2209 | 90.8 | 5.25 | Soft-Speed Separation |
| 667 | Cohn, Cooper | NIU_HUS | Four-Seam | 72 | 49.2 | 0.215 | 17.8 | 12.6 | 2195 | 91.1 | 5.96 | Soft-Speed Separation |
| 668 | Thompson, Ross | SCH_BOO | Sinker | 70 | 49.1 | 0.226 | 13.2 | 12.2 | 1957 | 89.9 | 6.02 | Soft-Speed Separation |
| 669 | Garbrick, Alex | LAK_ERI24 | Four-Seam | 162 | 49.1 | 0.252 | 15.7 | 10.9 | 2259 | 90.5 | 5.46 | Soft-Speed Separation |
| 670 | Leach, Landon | TRO_AIG | Four-Seam | 208 | 49.1 | 0.246 | 10.6 | 5.2 | 1971 | 91.6 | 5.66 | Soft-Speed Separation |
| 671 | Rodriguez, Leonardo | NEW_JER6 | Four-Seam | 271 | 49.1 | 0.230 | 15.7 | 10.9 | 2440 | 92.4 | 6.57 | Soft-Speed Separation |
| 672 | Dill, Austin | TRI_VAL | Four-Seam | 113 | 49.1 | 0.220 | 16.4 | 13.3 | 2324 | 87.2 | 5.33 | Soft-Speed Separation |
| 673 | Aldeano, Austin | TRO_AIG | Changeup | 51 | 49.0 | 0.246 | 7.1 | 17.6 | 1856 | 81.3 | 6.28 | Soft-Speed Separation |
| 674 | Cooper, Garrett | NEW_YOR13 | Changeup | 404 | 49.0 | 0.245 | 9.2 | 7.8 | 1389 | 77.3 | 6.37 | Soft-Speed Separation |
| 675 | Miranda, Kevin | OTT_TIT | Changeup | 161 | 49.0 | 0.251 | 8.6 | 12.4 | 1429 | 79.6 | 6.10 | Soft-Speed Separation |
| 676 | Pardinho, Eric | OTT_TIT | Four-Seam | 460 | 49.0 | 0.234 | 19.1 | 12.9 | 2231 | 92.7 | 5.46 | Soft-Speed Separation |
| 677 | Miner, Jace | DOW_EAS1 | Four-Seam | 61 | 49.0 | 0.244 | 10.8 | -8.0 | 1873 | 88.5 | 5.99 | Soft-Speed Separation |
| 678 | Harajli, Ahmad | FLO_Y'A | Four-Seam | 189 | 49.0 | 0.267 | 14.7 | 8.8 | 2042 | 92.0 | 6.43 | Soft-Speed Separation |
| 679 | Floyd, Conner | QUE_CAP | Four-Seam | 463 | 49.0 | 0.215 | 20.5 | 10.9 | 2410 | 92.7 | 5.55 | Soft-Speed Separation |
| 680 | Sakurai, Masatoshi | QUE_CAP | Four-Seam | 561 | 48.9 | 0.240 | 16.3 | -7.2 | 2025 | 87.6 | 6.48 | Soft-Speed Separation |
| 681 | Huter, Blayne | SUS_COU1 | Four-Seam | 142 | 48.9 | 0.241 | 17.1 | 6.2 | 2055 | 87.1 | 6.54 | Soft-Speed Separation |
| 682 | Vailes, Gage | GAT_GRI | Sinker | 519 | 48.8 | 0.259 | 7.5 | 16.2 | 1955 | 89.9 | 4.99 | Soft-Speed Separation |
| 683 | Burcham, Jacob | GAT_GRI | Sinker | 318 | 48.8 | 0.254 | 6.4 | 16.3 | 2276 | 91.0 | 6.59 | Soft-Speed Separation |
| 684 | Forsyth, Braden | MIS_MUD | Four-Seam | 347 | 48.8 | 0.213 | 19.1 | 9.6 | 2236 | 90.6 | 6.59 | Soft-Speed Separation |
| 685 | Reeves, Cobe | NEW_YOR13 | Sinker | 214 | 48.7 | 0.259 | 8.9 | -15.2 | 1821 | 90.3 | 6.02 | Soft-Speed Separation |
| 686 | Eckaus, David | EVA_OTT | Four-Seam | 270 | 48.7 | 0.240 | 15.1 | -11.4 | 2346 | 91.1 | 6.12 | Soft-Speed Separation |
| 687 | Eldred, Zach | NEW_ENG23 | Sinker | 120 | 48.6 | 0.250 | 11.6 | 13.3 | 2394 | 89.0 | 6.46 | Soft-Speed Separation |
| 688 | Noriega, Branden | LAK_ERI24 | Sinker | 104 | 48.6 | 0.267 | 13.0 | -15.4 | 2200 | 90.2 | 6.21 | Soft-Speed Separation |
| 689 | Eldred, Zach | NEW_ENG23 | Changeup | 52 | 48.5 | 0.302 | 10.6 | 7.8 | 1674 | 84.2 | 6.28 | Soft-Speed Separation |
| 690 | Encarnacion, J.D. | EVA_OTT | Four-Seam | 326 | 48.5 | 0.229 | 14.4 | 8.1 | 2333 | 88.7 | 5.89 | Soft-Speed Separation |
| 691 | Andueza, Axel | DOW_EAS1 | Four-Seam | 504 | 48.5 | 0.232 | 13.9 | 8.0 | 2130 | 90.5 | 5.53 | Soft-Speed Separation |
| 692 | Parsons, Billy | SUS_COU1 | Four-Seam | 390 | 48.5 | 0.223 | 17.4 | 9.4 | 2234 | 90.6 | 5.75 | Soft-Speed Separation |
| 693 | Ferguson, Francis | WIN_CIT29 | Four-Seam | 162 | 48.5 | 0.251 | 10.7 | -5.8 | 1966 | 90.2 | 5.46 | Soft-Speed Separation |
| 694 | Puccetti, Dominic | OTT_TIT | Four-Seam | 359 | 48.4 | 0.229 | 20.3 | -5.1 | 1866 | 87.9 | 5.63 | Soft-Speed Separation |
| 695 | Henderson, Drew | DOW_EAS1 | Changeup | 201 | 48.4 | 0.233 | 9.4 | 14.4 | 1733 | 81.3 | 5.73 | Soft-Speed Separation |
| 696 | Williams, Brian | MIS_MUD | Cutter | 173 | 48.4 | 0.259 | 6.4 | -0.1 | 2198 | 83.1 | 6.38 | Soft-Speed Separation |
| 697 | Castro, Alexander | TRO_AIG | Four-Seam | 146 | 48.4 | 0.247 | 18.5 | 12.3 | 2227 | 92.9 | 5.31 | Soft-Speed Separation |
| 698 | Misla, Luis | TRI_VAL | Sinker | 76 | 48.4 | 0.237 | 14.3 | -14.9 | 2325 | 88.6 | 5.68 | Soft-Speed Separation |
| 699 | Morgan, Cooper | QUE_CAP | Cutter | 132 | 48.3 | 0.238 | 8.8 | -3.0 | 2150 | 86.4 | 5.91 | Soft-Speed Separation |
| 700 | Bihm, Gage | MIS_MUD | Four-Seam | 270 | 48.3 | 0.218 | 15.2 | -11.0 | 1940 | 91.9 | 5.42 | Soft-Speed Separation |
| 701 | Moreno, Jose | DOW_EAS1 | Changeup | 114 | 48.3 | 0.238 | 7.0 | 10.8 | 1805 | 82.0 | 5.60 | Soft-Speed Separation |
| 702 | Rodriguez, Luis | TRO_AIG | Four-Seam | 276 | 48.2 | 0.254 | 20.6 | 7.0 | 2360 | 95.1 | 6.06 | Soft-Speed Separation |
| 703 | Tomczak, Anthony | EVA_OTT | Sinker | 202 | 48.2 | 0.208 | 12.5 | 17.0 | 2293 | 93.4 | 6.00 | Soft-Speed Separation |
| 704 | Snyder, Jack | SCH_BOO | Four-Seam | 183 | 48.2 | 0.244 | 16.9 | 4.8 | 2451 | 90.2 | 5.74 | Soft-Speed Separation |
| 705 | Duquette, Jagger | LAK_ERI24 | Changeup | 81 | 48.2 | 0.258 | 7.8 | 12.6 | 1830 | 77.9 | 6.48 | Soft-Speed Separation |
| 706 | Martinez, Gregory | DOW_EAS1 | Sinker | 128 | 48.2 | 0.246 | 11.9 | 15.8 | 2303 | 94.2 | 5.55 | Soft-Speed Separation |
| 707 | Maietta, Dante | WIN_CIT29 | Four-Seam | 569 | 48.1 | 0.232 | 19.6 | 9.3 | 2060 | 88.2 | 6.05 | Soft-Speed Separation |
| 708 | Petschke, Ben | EVA_OTT | Cutter | 284 | 48.0 | 0.230 | 9.9 | 2.4 | 2258 | 89.0 | 5.45 | Soft-Speed Separation |
| 709 | Sparks, Alec | GAT_GRI | Four-Seam | 487 | 48.0 | 0.236 | 17.1 | 4.3 | 2177 | 91.1 | 5.95 | Soft-Speed Separation |
| 710 | Gorgen, Grady | NEW_YOR13 | Changeup | 76 | 48.0 | 0.267 | 6.6 | -12.1 | 1888 | 84.0 | 6.10 | Soft-Speed Separation |
| 711 | Perozzi, John | SUS_COU1 | Four-Seam | 258 | 47.9 | 0.213 | 21.4 | 9.0 | 2209 | 91.6 | 6.00 | Soft-Speed Separation |
| 712 | Conklin, MacCallan | TRO_AIG | Four-Seam | 78 | 47.9 | 0.240 | 15.9 | 9.8 | 2404 | 90.5 | 6.29 | Soft-Speed Separation |
| 713 | Girard, John | FLO_Y'A | Four-Seam | 153 | 47.9 | 0.275 | 17.9 | -12.7 | 2114 | 86.1 | 5.43 | Soft-Speed Separation |
| 714 | Lefebvre, Charles | TRO_AIG | Sinker | 487 | 47.9 | 0.240 | 12.4 | 16.6 | 2230 | 89.0 | 6.54 | Soft-Speed Separation |
| 715 | Shears, Tanner | SCH_BOO | Sinker | 65 | 47.8 | 0.258 | 12.9 | 14.6 | 1950 | 92.6 | 5.32 | Soft-Speed Separation |
| 716 | Miranda, Kevin | OTT_TIT | Four-Seam | 210 | 47.8 | 0.236 | 19.3 | 13.4 | 2159 | 87.1 | 5.77 | Soft-Speed Separation |
| 717 | Hagan, Jack | DOW_EAS1 | Sinker | 349 | 47.8 | 0.243 | 10.5 | 16.6 | 2389 | 91.5 | 6.05 | Soft-Speed Separation |
| 718 | Lovell, Justin | WIN_CIT29 | Four-Seam | 239 | 47.8 | 0.240 | 15.3 | -13.4 | 2309 | 93.5 | 6.28 | Soft-Speed Separation |
| 719 | Johnston, Spencer | DOW_EAS1 | Four-Seam | 66 | 47.8 | 0.239 | 17.8 | 11.8 | 2141 | 84.9 | 5.98 | Soft-Speed Separation |
| 720 | Miner, Jace | DOW_EAS1 | Changeup | 268 | 47.8 | 0.261 | 6.6 | -12.1 | 1690 | 83.9 | 6.02 | Soft-Speed Separation |
| 721 | Lovell, Justin | WIN_CIT29 | Cutter | 66 | 47.7 | 0.236 | 10.5 | -8.7 | 2268 | 91.3 | 6.38 | Soft-Speed Separation |
| 722 | Webster, Evan | FLO_Y'A | Sinker | 80 | 47.6 | 0.253 | 15.8 | -11.2 | 1879 | 89.0 | 6.94 | Soft-Speed Separation |
| 723 | Webster, Evan | FLO_Y'A | Changeup | 213 | 47.6 | 0.257 | 11.3 | -11.9 | 1787 | 82.5 | 6.92 | Soft-Speed Separation |
| 724 | Cihocki, Danny | NIU_HUS | Four-Seam | 55 | 47.5 | 0.218 | 15.8 | 12.3 | 2221 | 89.2 | 6.54 | Soft-Speed Separation |
| 725 | Earwood, Micah | SUS_COU1 | Sinker | 165 | 47.5 | 0.237 | 6.8 | 15.3 | 2179 | 87.3 | 6.21 | Soft-Speed Separation |
| 726 | Fauci, Sonny | NEW_JER6 | Four-Seam | 478 | 47.5 | 0.240 | 16.9 | 12.5 | 2240 | 93.9 | 6.48 | Soft-Speed Separation |
| 727 | Ginn, Landon | WAS_WIL3 | Four-Seam | 158 | 47.3 | 0.263 | 15.2 | 3.2 | 2602 | 91.9 | 5.65 | Soft-Speed Separation |
| 728 | Brothers, Kellen | SUS_COU1 | Slider | 75 | 47.3 | 0.220 | 7.9 | -1.9 | 2355 | 82.3 | 6.25 | Soft-Speed Separation |
| 729 | Savinon, Jordan | NEW_YOR13 | Four-Seam | 116 | 47.2 | 0.240 | 18.2 | -9.0 | 2150 | 88.9 | 5.86 | Soft-Speed Separation |
| 730 | Gollert, Harley | QUE_CAP | Four-Seam | 81 | 47.2 | 0.246 | 16.6 | -8.3 | 2169 | 88.7 | 5.59 | Soft-Speed Separation |
| 731 | Esposito, Michael | NEW_ENG23 | Four-Seam | 139 | 47.2 | 0.249 | 16.9 | -11.5 | 2083 | 90.5 | 6.33 | Soft-Speed Separation |
| 732 | Bargo, Casey | FLO_Y'A | Four-Seam | 189 | 47.2 | 0.254 | 14.5 | 11.6 | 2211 | 91.3 | 5.89 | Soft-Speed Separation |
| 733 | Garcia, Andrew | EVA_OTT | Four-Seam | 246 | 47.1 | 0.252 | 13.2 | 7.1 | 2107 | 91.6 | 6.03 | Soft-Speed Separation |
| 734 | Heredia-Bustos, Rolando | DOW_EAS1 | Changeup | 329 | 47.1 | 0.267 | 9.1 | 17.6 | 2064 | 79.4 | 5.62 | Soft-Speed Separation |
| 735 | King, Jacob | DOW_EAS1 | Four-Seam | 65 | 47.0 | 0.232 | 17.9 | 11.7 | 2174 | 90.5 | 6.63 | Soft-Speed Separation |
| 736 | Petery, Dylan | WIN_CIT29 | Four-Seam | 106 | 47.0 | 0.285 | 17.1 | 9.8 | 2346 | 86.3 | 6.19 | Soft-Speed Separation |
| 737 | Steinhauer, Ryan | NEW_JER6 | Four-Seam | 58 | 47.0 | 0.269 | 16.0 | -9.3 | 1936 | 86.4 | 6.05 | Soft-Speed Separation |
| 738 | Agosto, Justus | TRI_VAL | Slider | 76 | 46.9 | 0.222 | 8.5 | -1.8 | 2249 | 85.0 | 5.78 | Soft-Speed Separation |
| 739 | Cerda, Junior | EVA_OTT | Sinker | 232 | 46.9 | 0.263 | 11.6 | 16.4 | 2222 | 94.2 | 5.39 | Soft-Speed Separation |
| 740 | Wilcenski, Blaise | WIN_CIT29 | Four-Seam | 117 | 46.8 | 0.224 | 15.4 | 9.1 | 2016 | 90.4 | 6.21 | Soft-Speed Separation |
| 741 | Shoemaker, Adam | QUE_CAP | Sinker | 62 | 46.8 | 0.263 | 10.5 | -15.2 | 2056 | 91.7 | 6.06 | Soft-Speed Separation |
| 742 | Barreto, Brayhans | TRI_VAL | Sinker | 185 | 46.8 | 0.263 | 12.3 | -14.1 | 2051 | 88.4 | 6.24 | Soft-Speed Separation |
| 743 | Kemlage, Joe | NEW_ENG23 | Sinker | 206 | 46.8 | 0.255 | 8.5 | -15.3 | 2433 | 91.0 | 5.86 | Soft-Speed Separation |
| 744 | Townes, Holland | SCH_BOO | Four-Seam | 193 | 46.8 | 0.233 | 15.4 | 13.1 | 2219 | 92.7 | 5.38 | Soft-Speed Separation |
| 745 | Thebiay, Nolan | EVA_OTT | Changeup | 125 | 46.7 | 0.275 | 5.0 | 16.2 | 1931 | 83.2 | 6.38 | Soft-Speed Separation |
| 746 | Quigley, Michael | NEW_ENG23 | Four-Seam | 322 | 46.7 | 0.230 | 17.6 | 12.5 | 2290 | 92.6 | 5.91 | Soft-Speed Separation |
| 747 | Allemann, Braeden | QUE_CAP | Sinker | 90 | 46.7 | 0.254 | 14.9 | 16.1 | 2300 | 90.5 | 6.23 | Soft-Speed Separation |
| 748 | Milburn, Isaac | FLO_Y'A | Four-Seam | 320 | 46.6 | 0.246 | 11.9 | -9.2 | 2114 | 87.8 | 5.54 | Soft-Speed Separation |
| 749 | Armstrong, Andrew | NEW_YOR13 | Sinker | 97 | 46.6 | 0.261 | 12.9 | -12.3 | 2101 | 88.7 | 6.47 | Soft-Speed Separation |
| 750 | Simpson, Garret | EVA_OTT | Four-Seam | 407 | 46.6 | 0.256 | 11.0 | 3.3 | 2340 | 89.0 | 5.74 | Soft-Speed Separation |
| 751 | Cameron, Wyatt | SCH_BOO | Four-Seam | 185 | 46.6 | 0.260 | 14.8 | 10.9 | 2243 | 91.2 | 5.48 | Soft-Speed Separation |
| 752 | Pindel, Buddie | SCH_BOO | Four-Seam | 607 | 46.5 | 0.249 | 16.0 | 13.6 | 2188 | 89.7 | 5.66 | Soft-Speed Separation |
| 753 | Simpson, Garret | EVA_OTT | Changeup | 119 | 46.5 | 0.267 | 4.8 | 11.3 | 1666 | 83.5 | 5.13 | Soft-Speed Separation |
| 754 | Soto, Carlos | JOL_SLA | Four-Seam | 223 | 46.5 | 0.275 | 13.0 | 10.0 | 2213 | 88.5 | 5.45 | Soft-Speed Separation |
| 755 | Potteiger, Jack | JOL_SLA | Sinker | 79 | 46.5 | 0.261 | 5.1 | -14.7 | 1942 | 89.4 | 6.39 | Soft-Speed Separation |
| 756 | Barreto, Brayhans | TRI_VAL | Slider | 139 | 46.4 | 0.268 | 3.9 | 0.7 | 1951 | 81.2 | 6.26 | Soft-Speed Separation |
| 757 | Villalobos, Jonaiker | FLO_Y'A | Four-Seam | 595 | 46.4 | 0.248 | 14.8 | -10.0 | 2216 | 87.9 | 5.87 | Soft-Speed Separation |
| 758 | Davis, Tyler | WAS_WIL3 | Four-Seam | 119 | 46.3 | 0.252 | 18.5 | -11.2 | 2340 | 92.6 | 5.88 | Soft-Speed Separation |
| 759 | Sakurai, Masatoshi | QUE_CAP | Changeup | 169 | 46.2 | 0.260 | 8.3 | -5.5 | 1436 | 80.5 | 5.96 | Soft-Speed Separation |
| 760 | Escobar, Anthony | TRO_AIG | Four-Seam | 506 | 46.2 | 0.242 | 17.6 | 10.1 | 2131 | 90.7 | 6.37 | Soft-Speed Separation |
| 761 | Duby, Bill | NEW_JER6 | Sinker | 230 | 46.2 | 0.250 | 14.0 | 16.1 | 2080 | 87.6 | 6.44 | Soft-Speed Separation |
| 762 | Galva, Claudio | GAT_GRI | Four-Seam | 181 | 46.2 | 0.254 | 12.4 | -10.0 | 1987 | 89.0 | 4.91 | Soft-Speed Separation |
| 763 | Hohenstein, Liam | WIN_CIT29 | Changeup | 84 | 46.1 | 0.284 | 11.1 | 9.0 | 1547 | 84.1 | 6.04 | Soft-Speed Separation |
| 764 | Orth, Harry | SCH_BOO | Sinker | 57 | 46.1 | 0.255 | 13.1 | 15.4 | 1963 | 90.9 | 6.24 | Soft-Speed Separation |
| 765 | Serrano, Elio | NEW_JER6 | Four-Seam | 580 | 46.1 | 0.238 | 17.4 | 10.7 | 2455 | 91.2 | 5.75 | Soft-Speed Separation |
| 766 | Woolfolk, Dallas | MIS_MUD | Four-Seam | 286 | 46.1 | 0.241 | 19.4 | 13.0 | 2377 | 92.6 | 5.48 | Soft-Speed Separation |
| 767 | Thompson, Ross | SCH_BOO | Changeup | 102 | 46.0 | 0.269 | 6.4 | 9.1 | 1202 | 80.9 | 5.74 | Soft-Speed Separation |
| 768 | Hines, Carter | FLO_Y'A | Four-Seam | 53 | 46.0 | 0.269 | 16.6 | -8.1 | 2502 | 91.0 | 5.91 | Soft-Speed Separation |
| 769 | Jones, Logan | FLO_Y'A | Sinker | 125 | 46.0 | 0.238 | 10.9 | 17.9 | 2212 | 89.6 | 5.28 | Soft-Speed Separation |
| 770 | Simone, Andrew | TRO_AIG | Four-Seam | 245 | 46.0 | 0.243 | 16.0 | 8.8 | 1956 | 91.4 | 6.02 | Soft-Speed Separation |
| 771 | Binns, Malik | NEW_JER6 | Four-Seam | 100 | 46.0 | 0.266 | 13.7 | 7.5 | 2102 | 91.3 | 6.52 | Soft-Speed Separation |
| 772 | Cirino, Miguel | DOW_EAS1 | Sinker | 125 | 45.8 | 0.229 | 9.4 | 19.0 | 2288 | 90.4 | 6.24 | Soft-Speed Separation |
| 773 | Estrella, Noah | TRI_VAL | Sinker | 75 | 45.8 | 0.286 | 14.4 | 14.5 | 2090 | 91.5 | 5.66 | Soft-Speed Separation |
| 774 | Perdomo, Rafael | QUE_CAP | Four-Seam | 202 | 45.8 | 0.227 | 20.2 | 11.0 | 2309 | 89.1 | 5.85 | Soft-Speed Separation |
| 775 | Gartland, Chad | SUS_COU1 | Four-Seam | 104 | 45.8 | 0.250 | 15.6 | 9.7 | 2115 | 91.0 | 6.26 | Soft-Speed Separation |
| 776 | Gordillo, Lucas | TRI_VAL | Changeup | 76 | 45.7 | 0.271 | 10.9 | 15.7 | 2125 | 80.0 | 6.07 | Soft-Speed Separation |
| 777 | Eldred, Zach | NEW_ENG23 | Four-Seam | 650 | 45.6 | 0.256 | 16.2 | 6.7 | 2504 | 89.8 | 6.40 | Soft-Speed Separation |
| 778 | Godwin, Connor | NEW_YOR13 | Sinker | 149 | 45.6 | 0.268 | 6.0 | 14.5 | 2153 | 91.8 | 6.07 | Soft-Speed Separation |
| 779 | House, Tristan | MIS_MUD | Four-Seam | 407 | 45.5 | 0.253 | 17.0 | 9.4 | 1974 | 89.4 | 6.15 | Soft-Speed Separation |
| 780 | Morel, Yohanse | OTT_TIT | Sinker | 349 | 45.5 | 0.266 | 8.8 | 18.4 | 2269 | 91.1 | 5.25 | Soft-Speed Separation |
| 781 | Kelly, Aiden | TRI_VAL | Four-Seam | 148 | 45.4 | 0.251 | 15.5 | 8.5 | 2248 | 90.1 | 5.99 | Soft-Speed Separation |
| 782 | Sanders, Brayden | MIS_MUD | Four-Seam | 296 | 45.4 | 0.259 | 18.7 | 11.1 | 1986 | 91.6 | 4.93 | Soft-Speed Separation |
| 783 | Long, Jalon | NEW_YOR13 | Changeup | 145 | 45.4 | 0.263 | 5.6 | 13.9 | 1517 | 82.1 | 6.06 | Soft-Speed Separation |
| 784 | Vitas, Ben | JOL_SLA | Sinker | 297 | 45.4 | 0.249 | 14.7 | 17.6 | 2179 | 90.2 | 5.11 | Soft-Speed Separation |
| 785 | Bradford, Ethan | NEW_YOR13 | Sinker | 297 | 45.4 | 0.254 | 6.9 | -15.7 | 2204 | 90.2 | 5.69 | Soft-Speed Separation |
| 786 | Dill, Austin | TRI_VAL | Sinker | 197 | 45.4 | 0.263 | 14.8 | 15.8 | 2315 | 88.1 | 5.43 | Soft-Speed Separation |
| 787 | Parenteau, Matt | EVA_OTT | Four-Seam | 66 | 45.4 | 0.232 | 14.6 | 4.9 | 2252 | 92.0 | 6.39 | Soft-Speed Separation |
| 788 | Gordillo, Lucas | TRI_VAL | Four-Seam | 348 | 45.3 | 0.271 | 16.7 | 9.9 | 2100 | 90.7 | 6.17 | Soft-Speed Separation |
| 789 | Smith, Ben | NEW_ENG23 | Sinker | 70 | 45.3 | 0.254 | 10.5 | -12.1 | 2139 | 86.8 | 5.79 | Soft-Speed Separation |
| 790 | Lockhart, Gauge | LAK_ERI24 | Sinker | 79 | 45.3 | 0.279 | 9.5 | 14.8 | 1960 | 89.1 | 6.22 | Soft-Speed Separation |
| 791 | Henderson, Drew | DOW_EAS1 | Four-Seam | 538 | 45.1 | 0.243 | 18.6 | 13.1 | 2248 | 89.1 | 5.67 | Soft-Speed Separation |
| 792 | Armstrong, Andrew | NEW_YOR13 | Four-Seam | 166 | 45.1 | 0.280 | 14.8 | -9.5 | 2136 | 89.1 | 6.43 | Soft-Speed Separation |
| 793 | Gartland, Chad | TRI_VAL | Sinker | 99 | 45.1 | 0.276 | 13.2 | 12.4 | 2073 | 88.4 | 6.10 | Soft-Speed Separation |
| 794 | McKillican, Adam | QUE_CAP | Sinker | 59 | 45.1 | 0.269 | 11.5 | 12.6 | 1988 | 88.6 | 6.73 | Soft-Speed Separation |
| 795 | Garcia, Hector | WAS_WIL3 | Four-Seam | 199 | 45.1 | 0.253 | 19.5 | 4.6 | 2221 | 91.0 | 6.05 | Soft-Speed Separation |
| 796 | Salata, Derek | SCH_BOO | Four-Seam | 765 | 44.9 | 0.248 | 16.6 | 5.3 | 2290 | 89.4 | 6.16 | Soft-Speed Separation |
| 797 | Maher, Adam | TRI_VAL | Changeup | 116 | 44.8 | 0.267 | 12.9 | -11.2 | 1854 | 81.5 | 6.01 | Soft-Speed Separation |
| 798 | Sesar, Jorden | SUS_COU1 | Four-Seam | 748 | 44.8 | 0.244 | 19.3 | 8.9 | 2470 | 91.5 | 6.25 | Soft-Speed Separation |
| 799 | Chapple, Bronson | TRO_AIG | Changeup | 51 | 44.7 | 0.283 | 3.7 | 14.5 | 1828 | 83.2 | 6.34 | Soft-Speed Separation |
| 800 | Gollert, Harley | TRO_AIG | Four-Seam | 242 | 44.7 | 0.229 | 15.7 | -9.8 | 2175 | 88.7 | 5.51 | Soft-Speed Separation |
| 801 | Shinn, Nathan | LAK_ERI24 | Sinker | 50 | 44.5 | 0.240 | 15.9 | -10.4 | 1907 | 89.3 | 5.76 | Soft-Speed Separation |
| 802 | Primeaux, Parker | SUS_COU1 | Four-Seam | 62 | 44.4 | 0.252 | 6.0 | 15.8 | 2099 | 87.8 | 5.56 | Soft-Speed Separation |
| 803 | Majick, Eli | NEW_ENG23 | Sinker | 343 | 44.4 | 0.264 | 7.1 | -16.7 | 2014 | 87.4 | 5.84 | Soft-Speed Separation |
| 804 | Bargo, Casey | NEW_ENG23 | Four-Seam | 147 | 44.4 | 0.251 | 16.0 | 12.7 | 2282 | 92.2 | 6.19 | Soft-Speed Separation |
| 805 | Cooper, Garrett | NEW_YOR13 | Four-Seam | 281 | 44.4 | 0.269 | 16.1 | 7.6 | 2066 | 89.4 | 5.84 | Soft-Speed Separation |
| 806 | Smith, Ethan | WIN_CIT29 | Four-Seam | 169 | 44.2 | 0.244 | 16.6 | 9.8 | 2211 | 89.3 | 6.29 | Soft-Speed Separation |
| 807 | Grills, Evan | OTT_TIT | Four-Seam | 144 | 44.1 | 0.245 | 17.5 | -10.7 | 2214 | 87.8 | 5.50 | Soft-Speed Separation |
| 808 | Morrissey, Joe | EVA_OTT | Four-Seam | 223 | 44.1 | 0.241 | 19.8 | 11.1 | 2371 | 89.6 | 5.74 | Soft-Speed Separation |
| 809 | Bargo, Casey | FLO_Y'A | Sinker | 111 | 44.0 | 0.255 | 12.5 | 15.6 | 2216 | 91.1 | 5.85 | Soft-Speed Separation |
| 810 | Peyton, Blake | GAT_GRI | Sinker | 87 | 43.9 | 0.220 | 16.5 | -15.0 | 2216 | 88.8 | 6.02 | Soft-Speed Separation |
| 811 | Helt, Robert | LAK_ERI24 | Four-Seam | 499 | 43.9 | 0.263 | 14.9 | 7.0 | 2284 | 91.5 | 6.31 | Soft-Speed Separation |
| 812 | Barker, Alex | NEW_YOR13 | Four-Seam | 347 | 43.9 | 0.267 | 15.3 | -8.3 | 2183 | 87.2 | 6.10 | Soft-Speed Separation |
| 813 | Balzan, Jackson | SUS_COU1 | Four-Seam | 327 | 43.8 | 0.253 | 18.5 | -12.4 | 2246 | 86.3 | 5.46 | Soft-Speed Separation |
| 814 | Whitesell, Max | FLO_Y'A | Sinker | 87 | 43.7 | 0.284 | 12.5 | 14.1 | 1918 | 89.5 | 6.36 | Soft-Speed Separation |
| 815 | De Los Santos, Enmanuel | NEW_ENG23 | Four-Seam | 258 | 43.7 | 0.250 | 18.1 | 4.3 | 2112 | 88.1 | 6.80 | Soft-Speed Separation |
| 816 | Morel, Yohanse | OTT_TIT | Changeup | 136 | 43.7 | 0.280 | 4.7 | 16.9 | 2149 | 85.4 | 5.34 | Soft-Speed Separation |
| 817 | Blair, Davis | DOW_EAS1 | Four-Seam | 204 | 43.7 | 0.238 | 16.6 | 8.1 | 2084 | 91.7 | 5.59 | Soft-Speed Separation |
| 818 | Valdez, Alex | EVA_OTT | Four-Seam | 216 | 43.6 | 0.250 | 13.1 | 5.9 | 2159 | 91.7 | 5.95 | Soft-Speed Separation |
| 819 | Hampton, Ky | OTT_TIT | Changeup | 295 | 43.5 | 0.279 | 2.5 | 15.6 | 1730 | 83.9 | 5.98 | Soft-Speed Separation |
| 820 | Fowler, Dalton | SUS_COU1 | Sinker | 51 | 43.5 | 0.284 | 11.3 | -12.9 | 2160 | 91.4 | 5.54 | Soft-Speed Separation |
| 821 | Andueza, Axel | DOW_EAS1 | Sinker | 121 | 43.4 | 0.265 | 11.5 | 11.4 | 2058 | 89.9 | 5.49 | Soft-Speed Separation |
| 822 | Vega, Lucas | TRO_AIG | Sinker | 257 | 43.4 | 0.252 | 9.1 | 14.6 | 2018 | 89.6 | 6.10 | Soft-Speed Separation |
| 823 | Leach, Landon | TRO_AIG | Sinker | 93 | 43.4 | 0.275 | 9.4 | 11.4 | 1913 | 91.6 | 5.69 | Soft-Speed Separation |
| 824 | Misla, Luis | TRI_VAL | Four-Seam | 381 | 43.4 | 0.268 | 17.5 | -11.4 | 2404 | 88.8 | 5.82 | Soft-Speed Separation |
| 825 | Bohnert, Matthew | WIN_CIT29 | Four-Seam | 430 | 43.3 | 0.255 | 17.2 | -8.6 | 2136 | 91.6 | 5.23 | Soft-Speed Separation |
| 826 | Gamelin, Shaun | JOL_SLA | Four-Seam | 465 | 43.3 | 0.245 | 20.2 | 10.2 | 2100 | 89.9 | 4.84 | Soft-Speed Separation |
| 827 | Anibal, Trevor | NEW_ENG23 | Four-Seam | 264 | 43.2 | 0.276 | 18.8 | 12.0 | 2253 | 90.5 | 5.84 | Soft-Speed Separation |
| 828 | Harris, Ben | GAT_GRI | Four-Seam | 618 | 43.1 | 0.266 | 17.1 | 8.3 | 2345 | 90.8 | 5.87 | Soft-Speed Separation |
| 829 | Perez, Kelvin | WAS_WIL3 | Changeup | 89 | 43.1 | 0.287 | 6.5 | 14.5 | 1577 | 81.4 | 6.31 | Soft-Speed Separation |
| 830 | Sanchez, Edwin | LAK_ERI24 | Sinker | 328 | 43.0 | 0.259 | 15.6 | -14.2 | 2123 | 87.7 | 5.87 | Soft-Speed Separation |
| 831 | Noriega, Branden | LAK_ERI24 | Four-Seam | 186 | 43.0 | 0.238 | 15.2 | -14.6 | 2239 | 90.8 | 5.96 | Soft-Speed Separation |
| 832 | Bargo, Casey | FLO_Y'A | Changeup | 53 | 42.9 | 0.268 | 5.1 | 12.1 | 1489 | 83.0 | 6.12 | Soft-Speed Separation |
| 833 | Wehrle, Tyler | WIN_CIT29 | Sinker | 106 | 42.9 | 0.257 | 15.4 | 16.4 | 2321 | 91.4 | 5.68 | Soft-Speed Separation |
| 834 | Leak, Anthony | NEW_YOR13 | Four-Seam | 224 | 42.8 | 0.229 | 17.4 | 10.5 | 2208 | 90.7 | 6.16 | Soft-Speed Separation |
| 835 | Austin, Zack | SUS_COU1 | Four-Seam | 179 | 42.8 | 0.245 | 16.1 | 6.4 | 2287 | 91.6 | 5.89 | Soft-Speed Separation |
| 836 | Villers, Ian | QUE_CAP | Four-Seam | 162 | 42.7 | 0.274 | 17.9 | 11.9 | 2261 | 93.4 | 6.11 | Soft-Speed Separation |
| 837 | Allemann, Braeden | QUE_CAP | Four-Seam | 785 | 42.7 | 0.254 | 18.8 | 12.7 | 2344 | 91.3 | 6.37 | Soft-Speed Separation |
| 838 | Vitas, Ben | JOL_SLA | Four-Seam | 411 | 42.7 | 0.258 | 13.8 | 16.3 | 2163 | 90.1 | 5.17 | Soft-Speed Separation |
| 839 | Nakata, Yuto | QUE_CAP | Splitter | 116 | 42.7 | 0.296 | 3.0 | 6.8 | 1011 | 84.1 | 5.48 | Soft-Speed Separation |
| 840 | Long, Maddox | WAS_WIL3 | Changeup | 61 | 42.7 | 0.281 | 7.9 | 15.7 | 1932 | 84.2 | 5.97 | Soft-Speed Separation |
| 841 | Boies, Emiles | QUE_CAP | Sinker | 267 | 42.6 | 0.265 | 14.6 | 16.0 | 2122 | 87.6 | 6.10 | Soft-Speed Separation |
| 842 | Gordillo, Lucas | TRI_VAL | Sinker | 104 | 42.6 | 0.258 | 13.7 | 14.0 | 2090 | 91.2 | 6.01 | Soft-Speed Separation |
| 843 | Voytko, Fawster | TRO_AIG | Changeup | 126 | 42.6 | 0.238 | 11.4 | 12.6 | 1869 | 83.7 | 6.58 | Soft-Speed Separation |
| 844 | Matos, Dwayne | OTT_TIT | Changeup | 235 | 42.6 | 0.251 | 3.6 | 15.9 | 1525 | 84.0 | 6.38 | Soft-Speed Separation |
| 845 | Gorgen, Grady | NEW_YOR13 | Sinker | 52 | 42.5 | 0.265 | 8.1 | -8.3 | 2174 | 86.9 | 6.21 | Soft-Speed Separation |
| 846 | Harper, Scott | NEW_YOR13 | Sinker | 247 | 42.5 | 0.262 | 3.3 | 19.3 | 2285 | 89.2 | 6.25 | Soft-Speed Separation |
| 847 | Coles, Chad | WAS_WIL3 | Four-Seam | 239 | 42.5 | 0.258 | 17.9 | 9.8 | 2391 | 93.2 | 5.80 | Soft-Speed Separation |
| 848 | Hernandez, Nyan | NEW_JER6 | Sinker | 148 | 42.5 | 0.266 | 14.6 | 16.6 | 2096 | 88.8 | 6.47 | Soft-Speed Separation |
| 849 | Masick, Jason | NEW_YOR13 | Four-Seam | 134 | 42.5 | 0.261 | 14.4 | 7.8 | 2140 | 94.5 | 6.05 | Soft-Speed Separation |
| 850 | Turner, Eric | JOL_SLA | Four-Seam | 532 | 42.4 | 0.249 | 16.3 | 13.9 | 2287 | 88.1 | 5.15 | Soft-Speed Separation |
| 851 | Wiltse, Ryan | EVA_OTT | Four-Seam | 657 | 42.4 | 0.254 | 20.3 | 9.5 | 2163 | 87.0 | 6.05 | Soft-Speed Separation |
| 852 | Jensik, CJ | WIN_CIT29 | Sinker | 62 | 42.4 | 0.257 | 8.4 | 15.2 | 2079 | 92.5 | 5.78 | Soft-Speed Separation |
| 853 | Benitez, Jorge | NEW_JER6 | Four-Seam | 123 | 42.4 | 0.255 | 10.6 | -10.4 | 2178 | 93.3 | 6.05 | Soft-Speed Separation |
| 854 | De Jesus, Larry | DOW_EAS1 | Sinker | 103 | 42.4 | 0.263 | 14.2 | 16.3 | 2375 | 89.5 | 5.17 | Soft-Speed Separation |
| 855 | Marynczak, Arlo | TRI_VAL | Sinker | 120 | 42.3 | 0.259 | 14.7 | 13.8 | 2132 | 88.9 | 6.36 | Soft-Speed Separation |
| 856 | Reeves, Cobe | NEW_YOR13 | Four-Seam | 51 | 42.2 | 0.251 | 13.0 | -9.2 | 1965 | 90.7 | 5.86 | Soft-Speed Separation |
| 857 | Rodriguez, Joe Joe | NEW_JER6 | Sinker | 317 | 42.2 | 0.261 | 13.4 | 15.6 | 2114 | 91.4 | 5.74 | Soft-Speed Separation |
| 858 | Peters, Garrett | NEW_YOR13 | Four-Seam | 78 | 42.1 | 0.227 | 17.3 | -15.8 | 2237 | 86.0 | 5.66 | Soft-Speed Separation |
| 859 | Williams, Brian | MIS_MUD | Four-Seam | 772 | 42.0 | 0.260 | 17.8 | 8.2 | 2252 | 89.2 | 6.32 | Soft-Speed Separation |
| 860 | Voytko, Fawster | TRO_AIG | Four-Seam | 252 | 42.0 | 0.261 | 15.6 | 5.8 | 2132 | 89.5 | 6.66 | Soft-Speed Separation |
| 861 | Grounds, Jackson | TRO_AIG | Sinker | 111 | 42.0 | 0.285 | 13.6 | 13.8 | 2149 | 92.2 | 5.80 | Soft-Speed Separation |
| 862 | Correa, Nelvin | QUE_CAP | Changeup | 84 | 41.9 | 0.256 | 10.6 | 14.0 | 1990 | 84.7 | 6.02 | Soft-Speed Separation |
| 863 | Williams, Pierce | NEW_ENG23 | Sinker | 90 | 41.9 | 0.273 | 12.4 | -14.2 | 1874 | 85.7 | 6.11 | Soft-Speed Separation |
| 864 | Ortiz, Julio | GAT_GRI | Slider | 65 | 41.9 | 0.314 | 2.8 | 0.3 | 1938 | 85.7 | 5.94 | Soft-Speed Separation |
| 865 | Duncan, Tanner | DOW_EAS1 | Four-Seam | 246 | 41.9 | 0.277 | 16.2 | 9.0 | 2286 | 93.8 | 5.91 | Soft-Speed Separation |
| 866 | Barreto, Brayhans | TRI_VAL | Four-Seam | 142 | 41.8 | 0.277 | 15.4 | -9.2 | 2036 | 88.6 | 6.19 | Soft-Speed Separation |
| 867 | Garcia, Jorge | SUS_COU1 | Changeup | 90 | 41.8 | 0.249 | 11.9 | 9.6 | 1532 | 82.0 | 5.98 | Soft-Speed Separation |
| 868 | Anderson, Colt | WAS_WIL3 | Sinker | 59 | 41.8 | 0.276 | 8.4 | -11.5 | 2032 | 89.4 | 6.82 | Soft-Speed Separation |
| 869 | Bell, Brendan | NEW_ENG23 | Changeup | 56 | 41.8 | 0.249 | 7.3 | 15.4 | 1950 | 82.7 | 5.16 | Soft-Speed Separation |
| 870 | Leduc, Zachary | TRO_AIG | Sinker | 143 | 41.7 | 0.269 | 11.7 | 15.3 | 2115 | 90.3 | 6.54 | Soft-Speed Separation |
| 871 | Eldred, Zach | NEW_ENG23 | Splitter | 92 | 41.6 | 0.290 | 5.1 | 4.3 | 981 | 84.2 | 6.05 | Soft-Speed Separation |
| 872 | Nova, Fraynel | LAK_ERI24 | Four-Seam | 541 | 41.5 | 0.262 | 12.4 | 6.8 | 2054 | 90.6 | 6.03 | Soft-Speed Separation |
| 873 | Nova, Fraynel | LAK_ERI24 | Sinker | 140 | 41.5 | 0.272 | 9.2 | 13.4 | 2043 | 90.3 | 6.07 | Soft-Speed Separation |
| 874 | Hill, Kaleb | OTT_TIT | Sinker | 505 | 41.5 | 0.278 | 10.3 | -15.4 | 1869 | 89.7 | 5.54 | Soft-Speed Separation |
| 875 | Willeman, Landon | EVA_OTT | Four-Seam | 703 | 41.4 | 0.263 | 18.3 | 12.2 | 2191 | 90.8 | 5.82 | Soft-Speed Separation |
| 876 | Gartland, Chad | TRI_VAL | Changeup | 86 | 41.4 | 0.282 | 8.3 | 14.3 | 1731 | 83.7 | 6.00 | Soft-Speed Separation |
| 877 | Figueredo, Kevin | WIN_CIT29 | Sinker | 209 | 41.4 | 0.271 | 12.1 | -14.4 | 2017 | 88.1 | 5.39 | Soft-Speed Separation |
| 878 | Hicks, Jackson | DOW_EAS1 | Four-Seam | 72 | 41.4 | 0.278 | 17.9 | 12.2 | 2119 | 86.5 | 5.41 | Soft-Speed Separation |
| 879 | Bice, Emmett | NEW_YOR13 | Four-Seam | 244 | 41.4 | 0.262 | 15.4 | 7.3 | 2226 | 89.2 | 5.95 | Soft-Speed Separation |
| 880 | Estrella, Noah | TRI_VAL | Four-Seam | 330 | 41.2 | 0.252 | 17.1 | 12.4 | 2245 | 92.7 | 5.80 | Soft-Speed Separation |
| 881 | Brito, Richard | NEW_ENG23 | Four-Seam | 61 | 41.2 | 0.295 | 16.3 | 11.3 | 2385 | 93.5 | 6.54 | Soft-Speed Separation |
| 882 | Anderson, Nathan | EVA_OTT | Four-Seam | 52 | 41.1 | 0.288 | 16.3 | 10.3 | 2267 | 90.5 | 6.39 | Soft-Speed Separation |
| 883 | Manning, Noah | WIN_CIT29 | Sinker | 74 | 41.0 | 0.296 | 4.5 | 18.9 | 2343 | 90.7 | 5.46 | Soft-Speed Separation |
| 884 | Kaftan, Eddie | FLO_Y'A | Sinker | 128 | 41.0 | 0.263 | 7.4 | 13.6 | 2035 | 86.0 | 5.43 | Soft-Speed Separation |
| 885 | Mays, Justin | LAK_ERI24 | Four-Seam | 77 | 40.9 | 0.248 | 16.1 | 11.1 | 1996 | 88.1 | 5.61 | Soft-Speed Separation |
| 886 | Townes, Holland | SCH_BOO | Sinker | 126 | 40.9 | 0.261 | 13.0 | 15.4 | 2244 | 92.3 | 5.20 | Soft-Speed Separation |
| 887 | Elliott, Eric | MIS_MUD | Four-Seam | 127 | 40.8 | 0.239 | 21.2 | -3.9 | 2228 | 87.2 | 6.24 | Soft-Speed Separation |
| 888 | Hohenstein, Liam | WIN_CIT29 | Four-Seam | 206 | 40.8 | 0.269 | 17.4 | 4.4 | 1938 | 87.9 | 5.84 | Soft-Speed Separation |
| 889 | Jones, Breyln | NEW_JER6 | Cutter | 72 | 40.8 | 0.281 | 8.5 | -0.1 | 2061 | 87.2 | 5.85 | Soft-Speed Separation |
| 890 | Biddinger, Tyler | WIN_CIT29 | Changeup | 88 | 40.8 | 0.264 | 1.4 | 16.5 | 1969 | 83.9 | 5.50 | Soft-Speed Separation |
| 891 | Moore, Kyle | SCH_BOO | Sinker | 97 | 40.7 | 0.306 | 14.6 | 14.6 | 2159 | 87.8 | 4.77 | Soft-Speed Separation |
| 892 | Potteiger, Jack | JOL_SLA | Sinker | 155 | 40.6 | 0.285 | 5.8 | -14.1 | 1958 | 89.7 | 6.13 | Soft-Speed Separation |
| 893 | Trizuto, Colin | WAG_SEA | Changeup | 69 | 40.5 | 0.269 | 7.0 | 18.5 | 1961 | 84.0 | 5.35 | Soft-Speed Separation |
| 894 | Lefebvre, Charles | TRO_AIG | Four-Seam | 68 | 40.5 | 0.258 | 16.0 | 12.1 | 2254 | 89.7 | 6.41 | Soft-Speed Separation |
| 895 | Smith, Donny | JOL_SLA | Four-Seam | 52 | 40.4 | 0.291 | 15.1 | 11.0 | 2198 | 88.1 | 5.87 | Soft-Speed Separation |
| 896 | Bohnert, Matthew | WIN_CIT29 | Cutter | 55 | 40.4 | 0.245 | 10.9 | -3.6 | 2299 | 89.4 | 5.20 | Soft-Speed Separation |
| 897 | Phelps, Travis | FLO_Y'A | Four-Seam | 53 | 40.3 | 0.281 | 13.7 | 5.1 | 2092 | 90.6 | 6.64 | Soft-Speed Separation |
| 898 | Drakeford, Dosie | NEW_JER6 | Four-Seam | 130 | 40.3 | 0.251 | 19.1 | 10.1 | 2340 | 91.4 | 5.83 | Soft-Speed Separation |
| 899 | Lawson, Nathan | FLO_Y'A | Four-Seam | 113 | 40.3 | 0.291 | 14.5 | 8.5 | 2237 | 88.8 | 6.17 | Soft-Speed Separation |
| 900 | Chapple, Bronson | TRO_AIG | Four-Seam | 95 | 40.2 | 0.293 | 11.2 | 8.8 | 2129 | 90.2 | 6.67 | Soft-Speed Separation |
| 901 | Wehrle, Tyler | WIN_CIT29 | Changeup | 87 | 40.2 | 0.277 | 6.5 | 15.0 | 1874 | 84.5 | 5.57 | Soft-Speed Separation |
| 902 | Thompson, Ross | SCH_BOO | Four-Seam | 574 | 40.1 | 0.265 | 15.8 | 12.0 | 2029 | 89.0 | 5.73 | Soft-Speed Separation |
| 903 | Belton, Hunter | MIS_MUD | Four-Seam | 129 | 40.1 | 0.295 | 13.0 | 10.6 | 2231 | 86.4 | 6.13 | Soft-Speed Separation |
| 904 | Thiels, Brenton | MIS_MUD | Cutter | 51 | 39.8 | 0.314 | 9.4 | 4.5 | 2311 | 86.3 | 6.84 | Soft-Speed Separation |
| 905 | Serratos, Oscar | WIN_CIT29 | Four-Seam | 87 | 39.8 | 0.280 | 13.2 | 10.2 | 2207 | 91.5 | 5.58 | Soft-Speed Separation |
| 906 | Campbell, AJ | WIN_CIT29 | Four-Seam | 478 | 39.8 | 0.280 | 11.4 | 8.0 | 2413 | 88.2 | 5.48 | Soft-Speed Separation |
| 907 | Miranda, Kevin | OTT_TIT | Sinker | 58 | 39.7 | 0.264 | 17.0 | 15.7 | 2124 | 87.7 | 5.74 | Soft-Speed Separation |
| 908 | Kowalski, Benjamin | WAS_WIL3 | Four-Seam | 60 | 39.5 | 0.255 | 15.0 | 10.2 | 2148 | 89.0 | 5.69 | Soft-Speed Separation |
| 909 | Sohosky, Zac | MIA_RED | Four-Seam | 58 | 39.5 | 0.270 | 14.3 | -7.5 | 1888 | 88.4 | 6.33 | Soft-Speed Separation |
| 910 | Steinhauer, Ryan | NEW_JER6 | Changeup | 93 | 39.5 | 0.260 | 10.8 | -12.5 | 1665 | 82.3 | 6.31 | Soft-Speed Separation |
| 911 | Maryniak, Connor | NEW_JER6 | Four-Seam | 134 | 39.4 | 0.258 | 13.2 | 7.2 | 2453 | 89.9 | 5.77 | Soft-Speed Separation |
| 912 | Kramer, Cameron | TRO_AIG | Four-Seam | 136 | 39.3 | 0.266 | 17.9 | 4.5 | 2175 | 89.6 | 5.90 | Soft-Speed Separation |
| 913 | Frey, Hayden | TOL_ROC | Four-Seam | 55 | 39.3 | 0.324 | 9.7 | -17.4 | 2137 | 88.8 | 6.37 | Soft-Speed Separation |
| 914 | Givens-Craig, Hayden | SUS_COU1 | Four-Seam | 68 | 39.3 | 0.276 | 14.0 | 8.5 | 2022 | 84.7 | 5.64 | Soft-Speed Separation |
| 915 | Vincent, Tom | SCH_BOO | Four-Seam | 64 | 39.3 | 0.298 | 10.5 | -8.6 | 2339 | 92.3 | 6.02 | Soft-Speed Separation |
| 916 | Perez, Kelvin | WAS_WIL3 | Sinker | 128 | 39.2 | 0.298 | 9.5 | 14.1 | 2019 | 88.8 | 6.04 | Soft-Speed Separation |
| 917 | Pindel, Buddie | SCH_BOO | Sinker | 203 | 39.2 | 0.285 | 13.7 | 14.7 | 2128 | 89.8 | 5.69 | Soft-Speed Separation |
| 918 | Linderman, Greyson | JOL_SLA | Four-Seam | 95 | 39.0 | 0.283 | 13.7 | 12.2 | 2174 | 93.7 | 5.38 | Soft-Speed Separation |
| 919 | Lucas, Brock | JOL_SLA | Four-Seam | 110 | 39.0 | 0.265 | 14.9 | 6.6 | 2231 | 91.0 | 6.58 | Soft-Speed Separation |
| 920 | Pindel, Buddie | SCH_BOO | Changeup | 142 | 39.0 | 0.293 | 3.4 | 11.7 | 1370 | 80.8 | 5.51 | Soft-Speed Separation |
| 921 | Hampton, Ky | OTT_TIT | Sinker | 201 | 38.8 | 0.282 | 7.5 | 16.1 | 2166 | 88.3 | 6.13 | Soft-Speed Separation |
| 922 | Gilleran, Jimmy | NEW_ENG23 | Four-Seam | 114 | 38.8 | 0.265 | 16.0 | 13.9 | 2163 | 88.3 | 5.63 | Soft-Speed Separation |
| 923 | Blence, Connor | WIN_CIT29 | Sinker | 60 | 38.4 | 0.305 | 11.2 | 14.0 | 2237 | 87.7 | 6.01 | Soft-Speed Separation |
| 924 | Oe, Ryoya | OTT_TIT | Four-Seam | 58 | 38.3 | 0.281 | 18.1 | -3.8 | 2125 | 84.6 | 5.70 | Soft-Speed Separation |
| 925 | Sanchez, Dikember | LAK_ERI24 | Four-Seam | 131 | 38.2 | 0.277 | 11.7 | 7.8 | 2279 | 91.3 | 5.77 | Soft-Speed Separation |
| 926 | Chapple, Bronson | TRO_AIG | Sinker | 128 | 38.2 | 0.290 | 7.5 | 13.4 | 2067 | 90.5 | 6.50 | Soft-Speed Separation |
| 927 | Delongchamp, Luke | TRI_VAL | Sinker | 149 | 38.2 | 0.271 | 11.4 | 16.5 | 2047 | 87.1 | 5.73 | Soft-Speed Separation |
| 928 | Glickstein, Aaron | SCH_BOO | Cutter | 84 | 38.1 | 0.245 | 10.1 | 0.9 | 2236 | 85.5 | 5.66 | Soft-Speed Separation |
| 929 | Martinez, Mason | TRI_VAL | Changeup | 76 | 38.0 | 0.284 | 8.2 | 17.5 | 2180 | 82.3 | 6.67 | Soft-Speed Separation |
| 930 | Peters, Andrew | NEW_JER6 | Four-Seam | 376 | 38.0 | 0.275 | 15.5 | 7.6 | 2258 | 93.4 | 6.69 | Soft-Speed Separation |
| 931 | Wohlgemuth, Nate | EVA_OTT | Four-Seam | 52 | 38.0 | 0.284 | 13.9 | 11.1 | 2073 | 93.0 | 4.89 | Soft-Speed Separation |
| 932 | Donnan, Blake | FLO_Y'A | Sinker | 170 | 37.9 | 0.293 | 6.6 | 17.4 | 1978 | 90.7 | 5.86 | Soft-Speed Separation |
| 933 | Lovin, Xander | GAT_GRI | Four-Seam | 344 | 37.9 | 0.278 | 15.9 | 6.0 | 2308 | 91.2 | 4.96 | Soft-Speed Separation |
| 934 | Baker, Luke | EVA_OTT | Four-Seam | 87 | 37.8 | 0.306 | 14.2 | -10.6 | 2426 | 87.1 | 5.86 | Soft-Speed Separation |
| 935 | Nakata, Yuto | QUE_CAP | Four-Seam | 276 | 37.8 | 0.288 | 15.8 | 10.1 | 2079 | 92.5 | 5.76 | Soft-Speed Separation |
| 936 | Walsh, John | MIS_MUD | Four-Seam | 173 | 37.8 | 0.262 | 13.3 | -12.0 | 1889 | 84.2 | 5.71 | Soft-Speed Separation |
| 937 | Rodriguez, Esteban | WAS_WIL3 | Four-Seam | 167 | 37.7 | 0.288 | 17.0 | 4.4 | 2187 | 87.9 | 5.97 | Soft-Speed Separation |
| 938 | Campbell, Tyler | MIS_MUD | Sinker | 134 | 37.7 | 0.276 | 7.2 | -9.7 | 2283 | 84.6 | 6.14 | Soft-Speed Separation |
| 939 | Gartland, Chad | TRI_VAL | Four-Seam | 199 | 37.6 | 0.256 | 15.2 | 9.7 | 2083 | 89.0 | 6.15 | Soft-Speed Separation |
| 940 | Thiels, Brenton | MIS_MUD | Four-Seam | 193 | 37.5 | 0.280 | 15.9 | 11.2 | 2254 | 89.4 | 6.78 | Soft-Speed Separation |
| 941 | Tiburcio, David | DOW_EAS1 | Sinker | 207 | 37.5 | 0.283 | 11.9 | 17.6 | 2236 | 92.7 | 5.18 | Soft-Speed Separation |
| 942 | Matos, Dwayne | OTT_TIT | Sinker | 342 | 37.4 | 0.286 | 11.6 | 18.5 | 2124 | 90.6 | 6.01 | Soft-Speed Separation |
| 943 | Rivera, Matthew | NEW_ENG23 | Four-Seam | 249 | 37.3 | 0.263 | 18.1 | 9.7 | 2385 | 88.2 | 6.36 | Soft-Speed Separation |
| 944 | Woolfolk, Dallas | SCH_BOO | Four-Seam | 101 | 37.3 | 0.238 | 19.4 | 13.4 | 2327 | 92.5 | 5.63 | Soft-Speed Separation |
| 945 | Parsons, Billy | SUS_COU1 | Sinker | 64 | 37.2 | 0.264 | 12.9 | 9.9 | 2278 | 89.5 | 5.78 | Soft-Speed Separation |
| 946 | Voytko, Fawster | TRO_AIG | Sinker | 52 | 37.1 | 0.299 | 12.5 | 13.2 | 2070 | 88.1 | 6.51 | Soft-Speed Separation |
| 947 | Sabatine, Gino | TRI_VAL | Changeup | 287 | 37.0 | 0.293 | 8.3 | 15.5 | 1784 | 85.1 | 5.07 | Soft-Speed Separation |
| 948 | Biddinger, Tyler | WIN_CIT29 | Sinker | 260 | 36.9 | 0.291 | 7.7 | 17.0 | 2221 | 90.0 | 5.38 | Soft-Speed Separation |
| 949 | Reeves, Cobe | NEW_YOR13 | Changeup | 72 | 36.9 | 0.308 | 5.0 | -13.1 | 1385 | 84.3 | 6.35 | Soft-Speed Separation |
| 950 | Almonte, Dawil | EVA_OTT | Four-Seam | 142 | 36.8 | 0.295 | 11.2 | 9.4 | 2028 | 92.0 | 5.50 | Soft-Speed Separation |
| 951 | Salata, Derek | SCH_BOO | Sinker | 107 | 36.7 | 0.323 | 12.1 | 5.2 | 2152 | 89.6 | 6.13 | Soft-Speed Separation |
| 952 | Jones, Logan | TRI_VAL | Sinker | 109 | 36.6 | 0.287 | 12.1 | 17.9 | 2286 | 90.0 | 5.34 | Soft-Speed Separation |
| 953 | Duby, Bill | NEW_JER6 | Splitter | 78 | 36.5 | 0.309 | 5.9 | 3.5 | 958 | 78.9 | 6.13 | Soft-Speed Separation |
| 954 | Andueza, Axel | DOW_EAS1 | Splitter | 144 | 36.4 | 0.315 | 3.8 | 8.7 | 898 | 81.6 | 5.18 | Soft-Speed Separation |
| 955 | Thiels, Brenton | MIS_MUD | Slider | 86 | 36.3 | 0.320 | 6.5 | 1.3 | 2273 | 83.2 | 6.72 | Soft-Speed Separation |
| 956 | Escobar, Anthony | TRO_AIG | Sinker | 176 | 35.9 | 0.328 | 13.0 | 13.4 | 2103 | 89.2 | 6.35 | Soft-Speed Separation |
| 957 | Burcham, Jacob | GAT_GRI | Four-Seam | 93 | 35.9 | 0.283 | 12.6 | 11.7 | 2346 | 92.3 | 6.34 | Soft-Speed Separation |
| 958 | Lefebvre, Charles | TRO_AIG | Changeup | 153 | 35.9 | 0.289 | 6.0 | 14.7 | 1622 | 82.4 | 6.66 | Soft-Speed Separation |
| 959 | Peters, Garrett | NEW_YOR13 | Sinker | 70 | 35.8 | 0.280 | 17.3 | -15.9 | 2197 | 85.9 | 5.93 | Soft-Speed Separation |
| 960 | Sabatine, Gino | TRI_VAL | Four-Seam | 63 | 35.6 | 0.315 | 14.6 | 11.5 | 1846 | 88.6 | 5.02 | Soft-Speed Separation |
| 961 | Harris, Ben | GAT_GRI | Sinker | 123 | 35.6 | 0.296 | 13.4 | 14.9 | 2244 | 90.2 | 5.87 | Soft-Speed Separation |
| 962 | Linderman, Greyson | JOL_SLA | Sinker | 84 | 35.5 | 0.312 | 11.7 | 14.6 | 2128 | 93.6 | 5.43 | Soft-Speed Separation |
| 963 | Albert, Wes | DOW_EAS1 | Four-Seam | 112 | 35.3 | 0.292 | 17.7 | 8.9 | 1979 | 88.2 | 5.74 | Soft-Speed Separation |
| 964 | Toribio, Noe | TRO_AIG | Sinker | 532 | 35.2 | 0.286 | 11.4 | 17.8 | 2023 | 90.3 | 5.77 | Soft-Speed Separation |
| 965 | Bell, Jacob | SCH_BOO | Four-Seam | 98 | 35.0 | 0.281 | 16.7 | 11.7 | 2325 | 87.1 | 6.10 | Soft-Speed Separation |
| 966 | Cosentino, Nick | JOL_SLA | Four-Seam | 84 | 35.0 | 0.276 | 16.9 | 11.1 | 2220 | 90.5 | 5.48 | Soft-Speed Separation |
| 967 | Duby, Bill | NEW_JER6 | Changeup | 178 | 34.9 | 0.271 | 11.4 | 13.2 | 1941 | 83.8 | 6.62 | Soft-Speed Separation |
| 968 | Salata, Derek | SCH_BOO | Cutter | 199 | 34.8 | 0.302 | 12.3 | 0.4 | 2324 | 87.5 | 5.88 | Soft-Speed Separation |
| 969 | Gwin, Riley | QUE_CAP | Changeup | 52 | 34.8 | 0.292 | 13.0 | -10.7 | 1784 | 82.8 | 6.25 | Soft-Speed Separation |
| 970 | O'Hanlon, Michael | WAS_WIL3 | Four-Seam | 181 | 34.7 | 0.309 | 16.2 | 11.0 | 2138 | 88.5 | 5.95 | Soft-Speed Separation |
| 971 | Heredia-Bustos, Rolando | DOW_EAS1 | Sinker | 135 | 34.6 | 0.273 | 13.4 | 16.8 | 2111 | 87.9 | 5.71 | Soft-Speed Separation |
| 972 | Carroll, Jake | JOL_SLA | Four-Seam | 300 | 34.2 | 0.297 | 17.8 | -6.7 | 2146 | 86.2 | 7.05 | Soft-Speed Separation |
| 973 | Thornton, Tyler | NEW_ENG23 | Changeup | 195 | 34.1 | 0.293 | 9.4 | 14.0 | 1800 | 83.3 | 4.93 | Soft-Speed Separation |
| 974 | Gregory, Ben | GAT_GRI | Changeup | 88 | 34.0 | 0.303 | 8.6 | 13.7 | 1916 | 82.0 | 6.53 | Soft-Speed Separation |
| 975 | Nettleton, Blake | WIN_CIT29 | Four-Seam | 231 | 34.0 | 0.312 | 14.5 | 8.0 | 2139 | 89.5 | 6.49 | Soft-Speed Separation |
| 976 | Puccetti, Dominic | OTT_TIT | Changeup | 193 | 33.8 | 0.301 | 14.5 | -6.6 | 1696 | 84.4 | 5.46 | Soft-Speed Separation |
| 977 | Smith, Ben | NEW_ENG23 | Four-Seam | 91 | 33.8 | 0.281 | 10.5 | -10.2 | 2167 | 86.8 | 6.28 | Soft-Speed Separation |
| 978 | Thornton, Tyler | NEW_ENG23 | Sinker | 183 | 33.7 | 0.301 | 9.0 | 14.1 | 1962 | 84.4 | 5.36 | Soft-Speed Separation |
| 979 | Miner, Jace | DOW_EAS1 | Sinker | 156 | 33.7 | 0.305 | 7.2 | -11.5 | 1878 | 88.6 | 5.98 | Soft-Speed Separation |
| 980 | Gartland, Chad | TRI_VAL | Slider | 167 | 33.5 | 0.287 | 5.8 | -0.4 | 2207 | 82.7 | 6.09 | Soft-Speed Separation |
| 981 | Supple, Rayne | NEW_JER6 | Sinker | 97 | 33.1 | 0.269 | 8.3 | 16.1 | 2093 | 93.1 | 5.96 | Soft-Speed Separation |
| 982 | McKillican, Adam | QUE_CAP | Four-Seam | 52 | 32.9 | 0.318 | 14.5 | 9.9 | 2042 | 88.7 | 6.70 | Soft-Speed Separation |
| 983 | Cox, Carter | NIU_HUS | Four-Seam | 75 | 32.4 | 0.297 | 14.5 | -7.5 | 2226 | 87.3 | 6.59 | Soft-Speed Separation |
| 984 | Belton, Hunter | MIS_MUD | Changeup | 55 | 32.1 | 0.334 | 11.4 | 13.9 | 2006 | 81.0 | 6.10 | Soft-Speed Separation |
| 985 | Hickey, Matt | GAT_GRI | Changeup | 58 | 32.0 | 0.323 | 3.6 | 10.1 | 1519 | 81.9 | 5.50 | Soft-Speed Separation |
| 986 | Pardinho, Eric | OTT_TIT | Sinker | 83 | 31.2 | 0.309 | 15.1 | 15.2 | 2072 | 92.3 | 5.41 | Soft-Speed Separation |
| 987 | Duncan, Tanner | DOW_EAS1 | Changeup | 55 | 31.0 | 0.314 | 6.4 | 13.5 | 1564 | 87.4 | 6.43 | Soft-Speed Separation |
| 988 | Kramer, Cameron | TRO_AIG | Sinker | 69 | 30.4 | 0.283 | 13.1 | 16.0 | 2251 | 90.5 | 6.25 | Soft-Speed Separation |
| 989 | Rybarczyk, Ty | JOL_SLA | Four-Seam | 61 | 30.4 | 0.320 | 19.0 | 11.7 | 2309 | 91.3 | 5.50 | Soft-Speed Separation |
| 990 | O'Brien, Keenan | SUS_COU1 | Sinker | 91 | 30.3 | 0.296 | 10.4 | 16.1 | 2072 | 90.3 | 5.83 | Soft-Speed Separation |
| 991 | Beriguete, Randy | LAK_ERI24 | Four-Seam | 102 | 30.1 | 0.324 | 11.6 | 7.3 | 2284 | 93.3 | 6.47 | Soft-Speed Separation |
| 992 | Gaskey, Blake | NIU_HUS | Four-Seam | 62 | 29.1 | 0.344 | 10.3 | 13.8 | 2190 | 85.0 | 6.73 | Soft-Speed Separation |
| 993 | Anderson, Colt | WAS_WIL3 | Changeup | 58 | 28.7 | 0.300 | 7.4 | -6.1 | 1519 | 79.3 | 6.50 | Soft-Speed Separation |
| 994 | Foy, Corbin | LAK_ERI24 | Sinker | 57 | 28.5 | 0.333 | 11.4 | 13.2 | 2243 | 91.8 | 6.33 | Soft-Speed Separation |
| 995 | Givens-Craig, Hayden | SUS_COU1 | Changeup | 126 | 28.0 | 0.330 | 8.2 | 12.5 | 1656 | 79.9 | 5.76 | Soft-Speed Separation |
| 996 | Morse, Colby | EVA_OTT | Four-Seam | 54 | 27.2 | 0.283 | 16.5 | 9.2 | 2297 | 89.4 | 6.50 | Soft-Speed Separation |
| 997 | Smith, Ethan | WIN_CIT29 | Changeup | 52 | 26.7 | 0.317 | 9.1 | 14.6 | 2000 | 82.7 | 6.38 | Soft-Speed Separation |
| 998 | Miranda, Agnel | NEW_JER6 | Four-Seam | 50 | 26.5 | 0.276 | 15.6 | 9.8 | 2186 | 91.4 | 7.45 | Soft-Speed Separation |
| 999 | Smith, Donny | JOL_SLA | Sinker | 146 | 25.4 | 0.326 | 10.8 | 15.5 | 2124 | 88.8 | 5.76 | Soft-Speed Separation |
| 1000 | Bice, Emmett | NEW_YOR13 | Sinker | 65 | 21.9 | 0.347 | 7.5 | 12.2 | 2217 | 88.5 | 5.97 | Soft-Speed Separation |
| 1001 | Dima, Josh | GAT_GRI | Sinker | 87 | 20.9 | 0.331 | 16.9 | -13.0 | 1976 | 89.9 | 6.18 | Soft-Speed Separation |
| 1002 | Nabholz, Nate | TRI_VAL | Four-Seam | 99 | 20.0 | 0.356 | 18.5 | 10.3 | 2088 | 91.2 | 5.75 | Soft-Speed Separation |

## Undervalued Movement Pitches

Definition: movement quality percentile at least 75, with Pitch Value Score at or below league average.

| Rank | Pitcher | Team | Pitch | Pitches | PVS | xwOBA | IVB | HB | Spin | Velo | Ext | Archetype |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | Rohde, Isaac | NEW_YOR13 | Curveball | 54 | 41.8 | 0.249 | -4.0 | 10.7 | 2456 | 70.9 | 5.90 | Tight High-Spin Breakers |
| 2 | De Los Santos, Enmanuel | NEW_ENG23 | Curveball | 127 | 48.8 | 0.247 | -5.5 | -10.9 | 2210 | 71.5 | 6.46 | Tight High-Spin Breakers |
| 3 | Petery, Dylan | WIN_CIT29 | Curveball | 94 | 46.8 | 0.264 | -6.8 | -14.6 | 2561 | 74.4 | 5.54 | Tight High-Spin Breakers |
| 4 | Plumadore, Carson | WIN_CIT29 | Curveball | 111 | 30.6 | 0.313 | 0.6 | -6.6 | 2489 | 75.5 | 5.58 | Tight High-Spin Breakers |
| 5 | Westcott, Zac | FLO_Y'A | Curveball | 163 | 20.5 | 0.375 | -15.2 | -9.2 | 1872 | 67.1 | 5.48 | Tight High-Spin Breakers |
| 6 | Nakata, Yuto | QUE_CAP | Curveball | 88 | 45.7 | 0.262 | -12.9 | -13.2 | 2627 | 74.7 | 5.20 | Tight High-Spin Breakers |
| 7 | Campbell, Tyler | MIS_MUD | Slider | 300 | 49.9 | 0.254 | 7.3 | 4.6 | 2196 | 73.9 | 5.71 | Tight High-Spin Breakers |
| 8 | Brodsky, Jack | WAS_WIL3 | Curveball | 146 | 39.4 | 0.312 | -8.7 | -12.3 | 2634 | 75.9 | 5.52 | Tight High-Spin Breakers |
| 9 | Kassebaum, Torin | LON_ISL22 | Curveball | 55 | 39.8 | 0.306 | 1.1 | 10.2 | 2155 | 71.6 | 5.31 | Tight High-Spin Breakers |
| 10 | Petery, Dylan | WIN_CIT29 | Slider | 67 | 49.8 | 0.208 | -0.4 | -12.4 | 2605 | 78.0 | 5.76 | Tight High-Spin Breakers |
| 11 | Bice, Emmett | NEW_YOR13 | Curveball | 214 | 39.1 | 0.300 | -10.3 | -13.3 | 2998 | 79.2 | 5.59 | Tight High-Spin Breakers |
| 12 | Huter, Blayne | SUS_COU1 | Curveball | 103 | 44.5 | 0.271 | -5.1 | -14.2 | 2137 | 73.7 | 6.01 | Tight High-Spin Breakers |
| 13 | Voytko, Fawster | TRO_AIG | Curveball | 94 | 32.0 | 0.319 | -7.2 | -11.8 | 2338 | 74.9 | 6.04 | Tight High-Spin Breakers |
| 14 | Lovin, Xander | GAT_GRI | Curveball | 75 | 25.3 | 0.329 | -9.1 | -12.1 | 2620 | 76.8 | 4.64 | Tight High-Spin Breakers |
| 15 | Kaftan, Eddie | FLO_Y'A | Slider | 62 | 47.7 | 0.232 | 1.1 | -6.3 | 2437 | 77.1 | 4.72 | Tight High-Spin Breakers |
| 16 | Simpson, Garret | EVA_OTT | Curveball | 140 | 47.7 | 0.266 | -11.0 | -12.8 | 2630 | 76.7 | 5.17 | Tight High-Spin Breakers |
| 17 | Baker, Luke | EVA_OTT | Curveball | 59 | 47.6 | 0.244 | -7.4 | 9.7 | 2694 | 75.5 | 5.51 | Tight High-Spin Breakers |
| 18 | Sesar, Jorden | SUS_COU1 | Curveball | 136 | 48.9 | 0.262 | -11.9 | -11.2 | 2418 | 74.9 | 6.03 | Tight High-Spin Breakers |
| 19 | Gilleran, Jimmy | NEW_ENG23 | Curveball | 51 | 28.8 | 0.303 | -5.5 | -5.4 | 2387 | 75.5 | 5.06 | Tight High-Spin Breakers |
| 20 | Brodsky, Jack | WAS_WIL3 | Slider | 55 | 32.7 | 0.298 | -0.9 | -11.2 | 2586 | 79.1 | 5.53 | Tight High-Spin Breakers |
| 21 | Misla, Luis | TRI_VAL | Curveball | 177 | 48.9 | 0.246 | -5.2 | 9.5 | 2786 | 77.2 | 5.13 | Tight High-Spin Breakers |
| 22 | Soto, Carlos | JOL_SLA | Slider | 112 | 40.1 | 0.292 | -1.7 | -8.8 | 2512 | 78.2 | 5.08 | Tight High-Spin Breakers |
| 23 | Blence, Connor | WIN_CIT29 | Slider | 79 | 42.4 | 0.268 | 3.8 | -4.9 | 2552 | 79.5 | 5.97 | Tight High-Spin Breakers |
| 24 | Lawson, Nathan | FLO_Y'A | Curveball | 81 | 26.9 | 0.391 | -15.9 | -11.9 | 2381 | 74.2 | 5.59 | Tight High-Spin Breakers |
| 25 | Johnston, Spencer | DOW_EAS1 | Curveball | 74 | 30.0 | 0.304 | -4.9 | -6.1 | 2132 | 74.4 | 5.70 | Tight High-Spin Breakers |
| 26 | Marynczak, Arlo | TRI_VAL | Curveball | 59 | 47.1 | 0.253 | -2.6 | -13.9 | 2178 | 76.3 | 5.71 | Tight High-Spin Breakers |
| 27 | Turner, Eric | JOL_SLA | Slider | 250 | 46.6 | 0.248 | 1.4 | -7.7 | 2354 | 78.2 | 4.96 | Tight High-Spin Breakers |
| 28 | Serrano, Elio | NEW_JER6 | Curveball | 107 | 43.4 | 0.287 | -9.8 | -13.8 | 2283 | 75.7 | 5.13 | Tight High-Spin Breakers |
| 29 | Sanchez, Edwin | LAK_ERI24 | Curveball | 146 | 48.6 | 0.235 | -4.7 | 5.6 | 2465 | 76.1 | 5.26 | Tight High-Spin Breakers |
| 30 | Kostura, Brit | WAS_WIL3 | Slider | 65 | 35.3 | 0.295 | -0.6 | 5.2 | 2160 | 74.8 | 5.09 | Tight High-Spin Breakers |

## Top 20 Scouting Reports

1. **Grounds, Jackson, DOW_EAS1 Curveball** (Tight High-Spin Breakers): PVS 80.0, xwOBA 0.109. Shape: IVB -10.5, HB -12.0, 81.4 mph, 1946 rpm, 5.35 ft extension. Scouting read: low ride/drop, big horizontal; current results place it #1 overall and #1 within its pitch type.
2. **Morrissey, Joe, EVA_OTT Cutter** (Tight High-Spin Breakers): PVS 80.0, xwOBA 0.113. Shape: IVB 12.5, HB -3.2, 85.8 mph, 2649 rpm, 5.56 ft extension. Scouting read: high spin; current results place it #2 overall and #1 within its pitch type.
3. **Vecerka, Boris, QUE_CAP Slider** (Tight High-Spin Breakers): PVS 80.0, xwOBA 0.123. Shape: IVB 2.4, HB -11.8, 82.5 mph, 2472 rpm, 5.64 ft extension. Scouting read: low ride/drop, big horizontal, high spin; current results place it #3 overall and #1 within its pitch type.
4. **Carroll, Jake, JOL_SLA Slider** (Tight High-Spin Breakers): PVS 80.0, xwOBA 0.178. Shape: IVB -5.7, HB 7.7, 75.4 mph, 2046 rpm, 6.09 ft extension. Scouting read: low ride/drop, soft velo; current results place it #4 overall and #2 within its pitch type.
5. **Flontek, Zac, DOW_EAS1 Slider** (Tight High-Spin Breakers): PVS 80.0, xwOBA 0.089. Shape: IVB 2.8, HB -3.5, 86.8 mph, 2636 rpm, 5.81 ft extension. Scouting read: low ride/drop, high spin; current results place it #5 overall and #3 within its pitch type.
6. **Ryan, Dillon, NEW_ENG23 Slider** (Tight High-Spin Breakers): PVS 79.6, xwOBA 0.145. Shape: IVB -2.2, HB -8.5, 85.5 mph, 2504 rpm, 5.75 ft extension. Scouting read: low ride/drop, high spin; current results place it #6 overall and #4 within its pitch type.
7. **Morgan, Cooper, QUE_CAP Curveball** (Tight High-Spin Breakers): PVS 78.8, xwOBA 0.148. Shape: IVB -1.6, HB 17.7, 75.6 mph, 2699 rpm, 5.31 ft extension. Scouting read: low ride/drop, big horizontal, high spin, soft velo; current results place it #7 overall and #2 within its pitch type.
8. **Harley, Tristan, SUS_COU1 Slider** (Tight High-Spin Breakers): PVS 77.0, xwOBA 0.112. Shape: IVB 1.5, HB -8.7, 81.3 mph, 2432 rpm, 5.64 ft extension. Scouting read: low ride/drop, high spin; current results place it #8 overall and #5 within its pitch type.
9. **Sanders, Brayden, MIS_MUD Slider** (Tight High-Spin Breakers): PVS 76.6, xwOBA 0.160. Shape: IVB 1.5, HB -3.6, 82.0 mph, 2010 rpm, 4.58 ft extension. Scouting read: low ride/drop; current results place it #9 overall and #6 within its pitch type.
10. **Bauer, Patrick, QUE_CAP Slider** (Tight High-Spin Breakers): PVS 76.5, xwOBA 0.151. Shape: IVB 0.1, HB -10.5, 78.0 mph, 2416 rpm, 6.06 ft extension. Scouting read: low ride/drop, big horizontal, high spin, soft velo; current results place it #10 overall and #7 within its pitch type.
11. **Alpern, Liam, FLO_Y'A Slider** (Tight High-Spin Breakers): PVS 76.1, xwOBA 0.113. Shape: IVB -4.0, HB 11.5, 76.8 mph, 2219 rpm, 5.55 ft extension. Scouting read: low ride/drop, big horizontal, soft velo; current results place it #11 overall and #8 within its pitch type.
12. **Sparks, Alec, GAT_GRI Curveball** (Tight High-Spin Breakers): PVS 76.0, xwOBA 0.160. Shape: IVB -4.4, HB -7.0, 77.6 mph, 2566 rpm, 5.37 ft extension. Scouting read: low ride/drop, high spin, soft velo; current results place it #12 overall and #3 within its pitch type.
13. **Heintz, Danny, FLO_Y'A Four-Seam** (Soft-Speed Separation): PVS 75.8, xwOBA 0.092. Shape: IVB 14.2, HB 10.4, 92.2 mph, 2180 rpm, 5.82 ft extension. Scouting read: big horizontal, power velocity; current results place it #13 overall and #1 within its pitch type.
14. **Kramer, Cameron, TRO_AIG Slider** (Tight High-Spin Breakers): PVS 75.7, xwOBA 0.176. Shape: IVB 4.7, HB -7.2, 81.0 mph, 2184 rpm, 5.55 ft extension. Scouting read: average movement blend; current results place it #14 overall and #9 within its pitch type.
15. **Scafidi, Christian, LAK_ERI24 Cutter** (Tight High-Spin Breakers): PVS 74.4, xwOBA 0.147. Shape: IVB 6.2, HB -0.2, 85.3 mph, 2406 rpm, 5.40 ft extension. Scouting read: high spin; current results place it #15 overall and #2 within its pitch type.
16. **Davis, Tyler, WIN_CIT29 Four-Seam** (Soft-Speed Separation): PVS 74.4, xwOBA 0.111. Shape: IVB 21.2, HB 5.6, 89.3 mph, 2171 rpm, 5.86 ft extension. Scouting read: plus ride, power velocity; current results place it #16 overall and #2 within its pitch type.
17. **Jones, Logan, TRI_VAL Slider** (Tight High-Spin Breakers): PVS 74.3, xwOBA 0.190. Shape: IVB 2.5, HB 2.3, 83.5 mph, 2341 rpm, 5.69 ft extension. Scouting read: low ride/drop, high spin; current results place it #17 overall and #10 within its pitch type.
18. **Grounds, Jackson, DOW_EAS1 Four-Seam** (Soft-Speed Separation): PVS 74.1, xwOBA 0.159. Shape: IVB 17.0, HB 14.2, 92.5 mph, 2163 rpm, 5.59 ft extension. Scouting read: plus ride, big horizontal, power velocity; current results place it #18 overall and #3 within its pitch type.
19. **Bargo, Casey, NEW_ENG23 Slider** (Tight High-Spin Breakers): PVS 73.6, xwOBA 0.176. Shape: IVB 1.5, HB -5.0, 83.6 mph, 2416 rpm, 5.66 ft extension. Scouting read: low ride/drop, high spin; current results place it #19 overall and #11 within its pitch type.
20. **Debban, Caleb, NEW_JER6 Four-Seam** (Soft-Speed Separation): PVS 73.5, xwOBA 0.176. Shape: IVB 13.1, HB -4.6, 87.2 mph, 2325 rpm, 6.58 ft extension. Scouting read: high spin, extension; current results place it #20 overall and #4 within its pitch type.

## Plots

- `plots\pitch_movement_archetypes\cluster_count_selection.png`
- `plots\pitch_movement_archetypes\archetypes_hb_ivb.png`
- `plots\pitch_movement_archetypes\archetypes_velocity_spin.png`
- `plots\pitch_movement_archetypes\archetypes_pca.png`
- `plots\pitch_movement_archetypes\archetype_pitch_value.png`