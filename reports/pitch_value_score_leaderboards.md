# Frontier League Pitch Value Score

- Input file: `data\processed\pitcher_pitch_type_xwoba_metrics.csv`
- Output file: `data\processed\pitch_value_scores.csv`
- Qualified pitcher-pitch types scored: 568
- Qualification: at least 50 pitches and 10 tracked batted balls
- Score direction: higher is better, meaning lower expected xwOBA damage based on the frozen standardized score weights.
- Pitch type normalization: `Fastball` is grouped with `Four-Seam`; `Two-Seam` is grouped with `Sinker`.

## What The Score Means

Pitch Value Score is a pitch-level quality grade. Higher is better. A high score means that a pitcher-pitch type has a strong mix of miss, strike, and contact-management traits associated with lower expected damage.

This is not a full pitcher grade. It grades one pitch type for one pitcher. A pitcher can have an elite individual pitch and still have a weaker overall arsenal, command profile, workload, or role fit.

The score is built so the interpretation is familiar:

- `50` on the 20-80 scale is league average among qualified pitcher-pitch types.
- `60` is roughly one standard deviation better than average.
- `70` is roughly two standard deviations better than average.
- `80` is the top-end cap used for the report.
- `pitch_value_0_100` is the pitch's percentile rank among qualified pitcher-pitch types.

## Inputs

The score starts from pitcher + pitch type aggregates. Each row represents one pitch type thrown by one pitcher, not a single pitch. To reduce noise, only rows with enough volume are scored.

Pitch type labels are normalized before scoring: `Fastball` and `Four-Seam` are one pitch type labeled `Four-Seam`, while `Two-Seam` and `Sinker` are one pitch type labeled `Sinker`.

| Input Metric | Baseball Meaning | Score Direction |
|---|---|---|
| Whiff% | Ability to miss bats when hitters swing. | Higher is generally better, but this frozen score weight is small after contact metrics are included. |
| CSW% | Called strikes plus whiffs per pitch. | Measures count-control and bat-missing. |
| PutAway% | Strikeouts per two-strike pitch. | Higher means the pitch can finish plate appearances. |
| K% | Strikeouts per terminal PA-ending pitch for that pitch type. | Higher means stronger bat-missing/finishing results. |
| Average Exit Velocity | How hard tracked batted balls are hit. | Lower is better. |
| HardHit% | Share of batted balls at least 95 mph. | Lower is better. |
| Barrel% | Share of batted balls in an approximate barrel launch/EV zone. | Lower is usually better, but the multivariate coefficient is conditional on EV/HardHit/SweetSpot. |
| SweetSpot% | Share of batted balls launched from 8 to 32 degrees. | Lower is better for pitchers because this is a productive launch window. |

## Score Method

The score uses frozen standardized weights on the miss and contact metrics. Those weights encode how strongly each metric is associated with expected damage in the scoring system.

Each metric is standardized across qualified pitcher-pitch type rows. The standardized score weight is applied to estimate xwOBA pressure, then the sign is reversed so lower-xwOBA traits score higher.

`pitch_value_raw = -sum(standardized_weight * metric_z)`

- `pitch_value_20_80`: scouting-style scale, mean 50 and 10 points per standard deviation, clipped from 20 to 80.
- `pitch_value_0_100`: percentile rank of `pitch_value_raw` among qualified pitcher-pitch types.
- `overall_rank`: rank across all qualified pitcher-pitch types.
- `pitch_type_rank`: rank within that exact pitch type label.

Because the sign is reversed, a metric with a positive damage weight hurts the Pitch Value Score when it is high. A metric with a negative damage weight helps the score when it is high.

## Methodology Notes

- The scoring model is descriptive. It identifies which observed pitch-level outcomes were associated with lower expected damage in this dataset.
- Contact quality carries much of the weight because average exit velocity, SweetSpot%, and HardHit% are the strongest damage signals in the current score.
- Miss metrics still matter for baseball evaluation, but in this multivariate score they receive less weight when contact quality already captures most of the damage signal.
- Small samples can still move the leaderboards. The qualification filter helps, but the score should be read with pitch count and batted-ball count nearby.
- The score does not directly include command, sequencing, handedness splits, game context, injury risk, or scouting grades.

## Top 25 Pitches in the League

| Rank | Pitcher | Team | Pitch Type | Pitches | BBE | xwOBA | PVS 20-80 | PVS 0-100 | EV | Whiff% | K% | HardHit% | SweetSpot% | Pitch Type Rank |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | Grounds, Jackson | DOW_EAS1 | Curveball | 82 | 10 | 0.104 | 80.0 | 100.0 | 64.6 | 42.1% | 41.2% | 0.0% | 0.0% | 1 |
| 2 | Carroll, Jake | JOL_SLA | Slider | 56 | 11 | 0.204 | 80.0 | 99.8 | 68.7 | 26.1% | 30.8% | 0.0% | 18.2% | 1 |
| 3 | Harper, Scott | NEW_YOR13 | Slider | 114 | 20 | 0.133 | 77.6 | 99.6 | 71.5 | 42.9% | 37.0% | 0.0% | 10.0% | 2 |
| 4 | Escobar, Anthony | TRO_AIG | Changeup | 82 | 23 | 0.123 | 77.2 | 99.5 | 70.9 | 33.3% | 30.0% | 4.3% | 13.0% | 1 |
| 5 | Ryan, Dillon | NEW_ENG23 | Slider | 93 | 18 | 0.154 | 76.3 | 99.3 | 72.4 | 34.2% | 39.1% | 0.0% | 11.1% | 3 |
| 6 | Webster, Evan | FLO_Y'A | Cutter | 99 | 24 | 0.136 | 75.4 | 99.1 | 71.4 | 27.9% | 26.1% | 8.3% | 12.5% | 1 |
| 7 | Vitas, Ben | JOL_SLA | Splitter | 59 | 10 | 0.171 | 75.0 | 98.9 | 73.9 | 39.1% | 42.1% | 10.0% | 0.0% | 1 |
| 8 | McEvoy, Aidan | FLO_Y'A | Slider | 78 | 20 | 0.142 | 74.6 | 98.8 | 72.6 | 45.9% | 37.5% | 5.0% | 10.0% | 4 |
| 9 | Alpern, Liam | FLO_Y'A | Slider | 78 | 16 | 0.113 | 74.3 | 98.6 | 69.9 | 14.3% | 35.7% | 12.5% | 18.8% | 5 |
| 10 | Correa, Nelvin | QUE_CAP | Cutter | 68 | 19 | 0.137 | 74.2 | 98.4 | 70.4 | 32.4% | 23.5% | 5.3% | 21.1% | 2 |
| 11 | Foster, Kobe | WAS_WIL3 | Slider | 94 | 26 | 0.133 | 73.0 | 98.2 | 69.5 | 33.3% | 33.3% | 7.7% | 26.9% | 6 |
| 12 | Jones, Logan | TRI_VAL | Slider | 65 | 17 | 0.189 | 72.7 | 98.1 | 68.2 | 23.1% | 25.0% | 11.8% | 35.3% | 7 |
| 13 | Davis, Tyler | WIN_CIT29 | Four-Seam | 76 | 19 | 0.110 | 72.5 | 97.9 | 75.6 | 23.1% | 19.0% | 5.3% | 0.0% | 1 |
| 14 | Grounds, Jackson | DOW_EAS1 | Four-Seam | 107 | 27 | 0.156 | 72.4 | 97.7 | 69.9 | 25.5% | 21.7% | 11.1% | 25.9% | 2 |
| 15 | Perez, Kelvin | WAS_WIL3 | Slider | 56 | 13 | 0.127 | 72.4 | 97.5 | 71.8 | 34.6% | 38.5% | 15.4% | 15.4% | 8 |
| 16 | Webster, Evan | FLO_Y'A | Slider | 52 | 11 | 0.150 | 71.9 | 97.4 | 73.6 | 13.6% | 33.3% | 0.0% | 18.2% | 9 |
| 17 | Bargo, Casey | NEW_ENG23 | Slider | 56 | 16 | 0.177 | 71.8 | 97.2 | 74.6 | 28.0% | 40.0% | 0.0% | 12.5% | 10 |
| 18 | Garcia, Hector | WAS_WIL3 | Splitter | 62 | 13 | 0.185 | 71.8 | 97.0 | 71.1 | 45.7% | 40.0% | 7.7% | 23.1% | 2 |
| 19 | Peyton, Blake | GAT_GRI | Changeup | 62 | 17 | 0.149 | 71.7 | 96.8 | 71.2 | 31.0% | 15.8% | 5.9% | 23.5% | 2 |
| 20 | Hensey, Rob | SUS_COU1 | Changeup | 141 | 25 | 0.169 | 69.6 | 96.7 | 72.8 | 53.5% | 43.2% | 4.0% | 24.0% | 3 |
| 21 | Harajli, Ahmad | FLO_Y'A | Slider | 58 | 17 | 0.149 | 68.9 | 96.5 | 73.9 | 34.6% | 30.8% | 0.0% | 23.5% | 11 |
| 22 | Willeman, Landon | EVA_OTT | Changeup | 112 | 38 | 0.160 | 68.7 | 96.3 | 74.1 | 24.6% | 12.9% | 7.9% | 15.8% | 4 |
| 23 | Harris, Ben | GAT_GRI | Curveball | 138 | 10 | 0.215 | 68.7 | 96.1 | 75.6 | 39.3% | 55.0% | 10.0% | 10.0% | 2 |
| 24 | Donnan, Blake | FLO_Y'A | Slider | 65 | 10 | 0.186 | 68.5 | 96.0 | 71.5 | 51.7% | 52.9% | 10.0% | 30.0% | 12 |
| 25 | Smith, Jackson | MIS_MUD | Slider | 69 | 21 | 0.177 | 68.5 | 95.8 | 72.9 | 25.8% | 45.8% | 4.8% | 28.6% | 13 |

## Leaderboards by Pitch Family

### Four-Seams

| Rank | Pitcher | Team | Pitch Type | Pitches | BBE | xwOBA | PVS 20-80 | PVS 0-100 | EV | Whiff% | K% | HardHit% | SweetSpot% | Pitch Type Rank |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 13 | Davis, Tyler | WIN_CIT29 | Four-Seam | 76 | 19 | 0.110 | 72.5 | 97.9 | 75.6 | 23.1% | 19.0% | 5.3% | 0.0% | 1 |
| 14 | Grounds, Jackson | DOW_EAS1 | Four-Seam | 107 | 27 | 0.156 | 72.4 | 97.7 | 69.9 | 25.5% | 21.7% | 11.1% | 25.9% | 2 |
| 30 | Perez, Kelvin | WAS_WIL3 | Four-Seam | 56 | 17 | 0.150 | 67.7 | 94.9 | 73.4 | 10.0% | 15.4% | 5.9% | 23.5% | 3 |
| 35 | Cameron, Zach | WIN_CIT29 | Four-Seam | 64 | 24 | 0.197 | 66.5 | 94.0 | 74.0 | 17.2% | 23.5% | 16.7% | 16.7% | 4 |
| 41 | Rodriguez, Joe Joe | NEW_JER6 | Four-Seam | 55 | 19 | 0.164 | 65.1 | 93.0 | 77.0 | 23.3% | 18.2% | 5.3% | 15.8% | 5 |
| 45 | Foy, Corbin | LAK_ERI24 | Four-Seam | 96 | 19 | 0.176 | 64.6 | 92.3 | 72.9 | 18.5% | 25.0% | 5.3% | 36.8% | 6 |
| 48 | Riedel, Caleb | SCH_BOO | Four-Seam | 93 | 30 | 0.243 | 63.9 | 91.7 | 73.7 | 27.7% | 41.7% | 10.0% | 33.3% | 7 |
| 51 | Cartwright, Eli | GAT_GRI | Four-Seam | 121 | 30 | 0.178 | 63.1 | 91.2 | 75.4 | 28.3% | 25.0% | 10.0% | 23.3% | 8 |
| 53 | Hagan, Jack | DOW_EAS1 | Four-Seam | 50 | 15 | 0.130 | 62.8 | 90.8 | 76.0 | 37.0% | 50.0% | 6.7% | 26.7% | 9 |
| 57 | Foster, Kobe | WAS_WIL3 | Four-Seam | 253 | 83 | 0.186 | 62.2 | 90.1 | 75.3 | 28.0% | 28.3% | 9.6% | 27.7% | 10 |
| 58 | Eisenbarger, Jack | QUE_CAP | Four-Seam | 84 | 17 | 0.166 | 62.0 | 90.0 | 75.9 | 32.0% | 38.9% | 11.8% | 23.5% | 11 |
| 60 | Widener, Jacob | SUS_COU1 | Four-Seam | 60 | 18 | 0.215 | 61.9 | 89.6 | 71.5 | 24.0% | 14.3% | 5.6% | 50.0% | 12 |
| 65 | Maher, Adam | TRI_VAL | Four-Seam | 72 | 21 | 0.221 | 61.5 | 88.7 | 74.2 | 20.0% | 15.8% | 9.5% | 38.1% | 13 |
| 66 | Shears, Tanner | SCH_BOO | Four-Seam | 128 | 19 | 0.197 | 61.5 | 88.6 | 74.4 | 41.0% | 33.3% | 0.0% | 42.1% | 14 |
| 67 | Zaffiro, Cole | SCH_BOO | Four-Seam | 108 | 23 | 0.166 | 61.5 | 88.4 | 75.4 | 36.6% | 26.9% | 4.3% | 34.8% | 15 |
| 68 | Brown, Ethan | WAS_WIL3 | Four-Seam | 67 | 25 | 0.216 | 61.4 | 88.2 | 74.2 | 10.0% | 12.5% | 16.0% | 28.0% | 16 |
| 69 | MacMillan, Blake | TRO_AIG | Four-Seam | 92 | 28 | 0.195 | 61.2 | 88.0 | 76.4 | 33.3% | 38.9% | 14.3% | 21.4% | 17 |
| 73 | Anderson, Colt | WAS_WIL3 | Four-Seam | 107 | 37 | 0.236 | 60.7 | 87.3 | 72.9 | 19.6% | 21.2% | 13.5% | 40.5% | 18 |
| 74 | Kaminer, Brandon | DOW_EAS1 | Four-Seam | 151 | 50 | 0.219 | 60.7 | 87.1 | 76.1 | 10.6% | 13.3% | 8.0% | 28.0% | 19 |
| 76 | Zentko, Dylan | EVA_OTT | Four-Seam | 69 | 19 | 0.197 | 60.7 | 86.8 | 75.8 | 17.9% | 20.0% | 5.3% | 31.6% | 20 |
| 78 | Correa, Nelvin | QUE_CAP | Four-Seam | 55 | 15 | 0.187 | 60.3 | 86.4 | 78.7 | 15.8% | 0.0% | 6.7% | 13.3% | 21 |
| 79 | Wehrle, Tyler | WIN_CIT29 | Four-Seam | 227 | 46 | 0.188 | 60.1 | 86.3 | 75.6 | 34.5% | 31.9% | 8.7% | 32.6% | 22 |
| 81 | Mercado, Nelson | OTT_TIT | Four-Seam | 81 | 27 | 0.170 | 60.1 | 85.9 | 76.2 | 17.9% | 5.9% | 11.1% | 25.9% | 23 |
| 85 | Quigley, Michael | NEW_ENG23 | Four-Seam | 145 | 38 | 0.191 | 59.6 | 85.2 | 76.2 | 37.9% | 36.7% | 13.2% | 28.9% | 24 |
| 90 | Darden, Nathan | FLO_Y'A | Four-Seam | 72 | 29 | 0.191 | 58.9 | 84.3 | 79.7 | 17.9% | 15.8% | 10.3% | 13.8% | 25 |

### Sinkers

| Rank | Pitcher | Team | Pitch Type | Pitches | BBE | xwOBA | PVS 20-80 | PVS 0-100 | EV | Whiff% | K% | HardHit% | SweetSpot% | Pitch Type Rank |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 28 | Still, Stephen | TRI_VAL | Sinker | 61 | 18 | 0.211 | 68.1 | 95.2 | 74.7 | 25.8% | 36.4% | 11.1% | 16.7% | 1 |
| 36 | Widener, Jacob | SUS_COU1 | Sinker | 65 | 22 | 0.163 | 66.4 | 93.8 | 73.3 | 29.4% | 6.2% | 9.1% | 22.7% | 2 |
| 42 | Cerda, Junior | EVA_OTT | Sinker | 54 | 20 | 0.165 | 64.9 | 92.8 | 72.5 | 9.1% | 9.1% | 0.0% | 40.0% | 3 |
| 49 | Colon, Jeffrey | TRO_AIG | Sinker | 56 | 17 | 0.169 | 63.8 | 91.5 | 73.9 | 18.5% | 13.3% | 23.5% | 17.6% | 4 |
| 54 | Lawson, Nathan | FLO_Y'A | Sinker | 55 | 15 | 0.191 | 62.6 | 90.7 | 77.1 | 20.8% | 0.0% | 13.3% | 13.3% | 5 |
| 56 | Mannering, Shawn | DOW_EAS1 | Sinker | 59 | 15 | 0.255 | 62.3 | 90.3 | 74.8 | 22.2% | 6.7% | 13.3% | 26.7% | 6 |
| 64 | Plumadore, Carson | WIN_CIT29 | Sinker | 79 | 24 | 0.166 | 61.5 | 88.9 | 73.6 | 20.6% | 53.3% | 4.2% | 45.8% | 7 |
| 71 | Pierson, Kenny | LAK_ERI24 | Sinker | 88 | 27 | 0.183 | 60.9 | 87.7 | 79.0 | 0.0% | 0.0% | 11.1% | 7.4% | 8 |
| 95 | Morgan, Marcus | JOL_SLA | Sinker | 83 | 18 | 0.219 | 58.7 | 83.5 | 76.1 | 33.3% | 36.8% | 11.1% | 33.3% | 9 |
| 97 | Riedel, Caleb | SCH_BOO | Sinker | 52 | 16 | 0.178 | 58.6 | 83.1 | 75.5 | 23.1% | 20.0% | 12.5% | 31.2% | 10 |
| 110 | Daly, Ryan | JOL_SLA | Sinker | 102 | 31 | 0.191 | 58.0 | 80.8 | 76.9 | 21.3% | 23.8% | 16.1% | 25.8% | 11 |
| 120 | Cook, Cole | SCH_BOO | Sinker | 65 | 18 | 0.212 | 57.4 | 79.0 | 74.7 | 25.0% | 12.5% | 11.1% | 38.9% | 12 |
| 126 | Johnson, Caiden | OTT_TIT | Sinker | 54 | 12 | 0.230 | 57.2 | 78.0 | 76.2 | 35.0% | 10.0% | 0.0% | 41.7% | 13 |
| 137 | Gregory, Ben | GAT_GRI | Sinker | 76 | 21 | 0.187 | 56.8 | 76.1 | 77.9 | 28.1% | 26.3% | 14.3% | 23.8% | 14 |
| 138 | Grounds, Jackson | DOW_EAS1 | Sinker | 116 | 26 | 0.213 | 56.8 | 75.9 | 76.8 | 22.9% | 7.7% | 11.5% | 30.8% | 15 |
| 139 | McCartney, Seth | MIS_MUD | Sinker | 120 | 39 | 0.237 | 56.5 | 75.7 | 78.3 | 8.3% | 5.3% | 20.5% | 17.9% | 16 |
| 154 | Henderson, Drew | DOW_EAS1 | Sinker | 61 | 13 | 0.250 | 55.6 | 73.1 | 78.5 | 5.3% | 13.3% | 15.4% | 23.1% | 17 |
| 156 | Fritz, AJ | MIS_MUD | Sinker | 51 | 18 | 0.241 | 55.4 | 72.7 | 78.8 | 28.6% | 20.0% | 5.6% | 33.3% | 18 |
| 161 | Stuka, Ted | OTT_TIT | Sinker | 74 | 21 | 0.217 | 55.0 | 71.8 | 78.2 | 25.0% | 26.7% | 14.3% | 28.6% | 19 |
| 163 | Hensey, Rob | SUS_COU1 | Sinker | 269 | 100 | 0.224 | 54.9 | 71.5 | 76.4 | 17.3% | 19.4% | 16.0% | 36.0% | 20 |
| 167 | Turner, Eric | JOL_SLA | Sinker | 75 | 29 | 0.229 | 54.8 | 70.8 | 76.5 | 19.5% | 12.0% | 17.2% | 34.5% | 21 |
| 169 | Burcham, Jacob | GAT_GRI | Sinker | 152 | 39 | 0.240 | 54.7 | 70.4 | 78.1 | 17.7% | 6.2% | 10.3% | 30.8% | 22 |
| 172 | Leak, Anthony | NEW_YOR13 | Sinker | 81 | 25 | 0.233 | 54.4 | 69.9 | 75.3 | 12.1% | 5.0% | 16.0% | 40.0% | 23 |
| 173 | Long, Maddox | WAS_WIL3 | Sinker | 186 | 61 | 0.245 | 54.4 | 69.7 | 78.9 | 12.8% | 15.1% | 14.8% | 26.2% | 24 |
| 175 | Kelly, Colin | SUS_COU1 | Sinker | 96 | 29 | 0.188 | 54.3 | 69.4 | 77.5 | 25.0% | 11.1% | 17.2% | 31.0% | 25 |

### Sliders

| Rank | Pitcher | Team | Pitch Type | Pitches | BBE | xwOBA | PVS 20-80 | PVS 0-100 | EV | Whiff% | K% | HardHit% | SweetSpot% | Pitch Type Rank |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 2 | Carroll, Jake | JOL_SLA | Slider | 56 | 11 | 0.204 | 80.0 | 99.8 | 68.7 | 26.1% | 30.8% | 0.0% | 18.2% | 1 |
| 3 | Harper, Scott | NEW_YOR13 | Slider | 114 | 20 | 0.133 | 77.6 | 99.6 | 71.5 | 42.9% | 37.0% | 0.0% | 10.0% | 2 |
| 5 | Ryan, Dillon | NEW_ENG23 | Slider | 93 | 18 | 0.154 | 76.3 | 99.3 | 72.4 | 34.2% | 39.1% | 0.0% | 11.1% | 3 |
| 8 | McEvoy, Aidan | FLO_Y'A | Slider | 78 | 20 | 0.142 | 74.6 | 98.8 | 72.6 | 45.9% | 37.5% | 5.0% | 10.0% | 4 |
| 9 | Alpern, Liam | FLO_Y'A | Slider | 78 | 16 | 0.113 | 74.3 | 98.6 | 69.9 | 14.3% | 35.7% | 12.5% | 18.8% | 5 |
| 11 | Foster, Kobe | WAS_WIL3 | Slider | 94 | 26 | 0.133 | 73.0 | 98.2 | 69.5 | 33.3% | 33.3% | 7.7% | 26.9% | 6 |
| 12 | Jones, Logan | TRI_VAL | Slider | 65 | 17 | 0.189 | 72.7 | 98.1 | 68.2 | 23.1% | 25.0% | 11.8% | 35.3% | 7 |
| 15 | Perez, Kelvin | WAS_WIL3 | Slider | 56 | 13 | 0.127 | 72.4 | 97.5 | 71.8 | 34.6% | 38.5% | 15.4% | 15.4% | 8 |
| 16 | Webster, Evan | FLO_Y'A | Slider | 52 | 11 | 0.150 | 71.9 | 97.4 | 73.6 | 13.6% | 33.3% | 0.0% | 18.2% | 9 |
| 17 | Bargo, Casey | NEW_ENG23 | Slider | 56 | 16 | 0.177 | 71.8 | 97.2 | 74.6 | 28.0% | 40.0% | 0.0% | 12.5% | 10 |
| 21 | Harajli, Ahmad | FLO_Y'A | Slider | 58 | 17 | 0.149 | 68.9 | 96.5 | 73.9 | 34.6% | 30.8% | 0.0% | 23.5% | 11 |
| 24 | Donnan, Blake | FLO_Y'A | Slider | 65 | 10 | 0.186 | 68.5 | 96.0 | 71.5 | 51.7% | 52.9% | 10.0% | 30.0% | 12 |
| 25 | Smith, Jackson | MIS_MUD | Slider | 69 | 21 | 0.177 | 68.5 | 95.8 | 72.9 | 25.8% | 45.8% | 4.8% | 28.6% | 13 |
| 29 | Kirby, Zach | WAS_WIL3 | Slider | 102 | 32 | 0.168 | 67.9 | 95.1 | 73.8 | 20.5% | 17.4% | 3.1% | 25.0% | 14 |
| 32 | Nakata, Yuto | QUE_CAP | Slider | 57 | 14 | 0.146 | 67.1 | 94.5 | 76.9 | 42.3% | 35.7% | 0.0% | 14.3% | 15 |
| 43 | Long, Maddox | WAS_WIL3 | Slider | 145 | 28 | 0.174 | 64.8 | 92.6 | 74.9 | 35.7% | 19.4% | 14.3% | 17.9% | 16 |
| 44 | Morin, Jacob | QUE_CAP | Slider | 85 | 20 | 0.206 | 64.6 | 92.4 | 73.4 | 30.6% | 30.4% | 10.0% | 30.0% | 17 |
| 52 | Long, Jalon | NEW_YOR13 | Slider | 78 | 17 | 0.219 | 63.0 | 91.0 | 78.1 | 25.8% | 33.3% | 5.9% | 17.6% | 18 |
| 55 | Lefebvre, Charles | TRO_AIG | Slider | 66 | 12 | 0.139 | 62.3 | 90.5 | 71.6 | 25.0% | 0.0% | 8.3% | 41.7% | 19 |
| 59 | Armstrong, Andrew | NEW_YOR13 | Slider | 68 | 13 | 0.223 | 61.9 | 89.8 | 75.4 | 37.9% | 45.5% | 7.7% | 30.8% | 20 |
| 62 | Toribio, Noe | TRO_AIG | Slider | 82 | 22 | 0.180 | 61.6 | 89.3 | 74.6 | 19.4% | 18.2% | 9.1% | 31.8% | 21 |
| 63 | Tokar, Heitor | OTT_TIT | Slider | 80 | 30 | 0.188 | 61.6 | 89.1 | 77.2 | 19.6% | 20.8% | 13.3% | 16.7% | 22 |
| 70 | Baird, Dustin | MIS_MUD | Slider | 57 | 10 | 0.212 | 61.0 | 87.9 | 75.7 | 34.8% | 37.5% | 20.0% | 20.0% | 23 |
| 72 | Gollert, Harley | QUE_CAP | Slider | 57 | 22 | 0.216 | 60.7 | 87.5 | 73.9 | 14.8% | 13.3% | 22.7% | 27.3% | 24 |
| 77 | Vailes, Gage | GAT_GRI | Slider | 177 | 49 | 0.196 | 60.6 | 86.6 | 74.9 | 32.6% | 40.8% | 10.2% | 34.7% | 25 |

### Curveballs

| Rank | Pitcher | Team | Pitch Type | Pitches | BBE | xwOBA | PVS 20-80 | PVS 0-100 | EV | Whiff% | K% | HardHit% | SweetSpot% | Pitch Type Rank |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | Grounds, Jackson | DOW_EAS1 | Curveball | 82 | 10 | 0.104 | 80.0 | 100.0 | 64.6 | 42.1% | 41.2% | 0.0% | 0.0% | 1 |
| 23 | Harris, Ben | GAT_GRI | Curveball | 138 | 10 | 0.215 | 68.7 | 96.1 | 75.6 | 39.3% | 55.0% | 10.0% | 10.0% | 2 |
| 26 | Sechrist, Zander | WAS_WIL3 | Curveball | 61 | 20 | 0.172 | 68.4 | 95.6 | 70.7 | 16.7% | 6.7% | 10.0% | 30.0% | 3 |
| 33 | Sesar, Jorden | SUS_COU1 | Curveball | 76 | 17 | 0.192 | 66.8 | 94.4 | 73.7 | 13.0% | 25.0% | 0.0% | 29.4% | 4 |
| 47 | Hill, Kaleb | OTT_TIT | Curveball | 179 | 43 | 0.198 | 64.2 | 91.9 | 74.1 | 29.7% | 16.7% | 9.3% | 25.6% | 5 |
| 75 | Simpson, Garret | EVA_OTT | Curveball | 64 | 11 | 0.190 | 60.7 | 87.0 | 79.6 | 36.4% | 27.8% | 9.1% | 9.1% | 6 |
| 80 | Garcia, Brett | OTT_TIT | Curveball | 72 | 11 | 0.191 | 60.1 | 86.1 | 78.9 | 41.7% | 56.2% | 18.2% | 9.1% | 7 |
| 101 | Salata, Derek | SCH_BOO | Curveball | 52 | 12 | 0.238 | 58.5 | 82.4 | 74.9 | 37.5% | 42.9% | 8.3% | 41.7% | 8 |
| 119 | Kirby, Zach | WAS_WIL3 | Curveball | 98 | 11 | 0.225 | 57.5 | 79.2 | 75.8 | 35.7% | 35.7% | 9.1% | 36.4% | 9 |
| 131 | Anibal, Trevor | NEW_ENG23 | Curveball | 71 | 15 | 0.233 | 57.1 | 77.1 | 74.2 | 28.0% | 40.0% | 20.0% | 40.0% | 10 |
| 140 | Petschke, Ben | EVA_OTT | Curveball | 158 | 40 | 0.232 | 56.4 | 75.5 | 79.8 | 23.3% | 12.2% | 12.5% | 17.5% | 11 |
| 164 | Noriega, Branden | LAK_ERI24 | Curveball | 90 | 10 | 0.244 | 54.9 | 71.3 | 78.8 | 61.8% | 56.5% | 0.0% | 40.0% | 12 |
| 170 | Milburn, Isaac | FLO_Y'A | Curveball | 134 | 15 | 0.249 | 54.7 | 70.2 | 78.5 | 29.4% | 28.0% | 6.7% | 33.3% | 13 |
| 182 | Puccetti, Dominic | OTT_TIT | Curveball | 148 | 30 | 0.240 | 53.9 | 68.1 | 76.5 | 25.0% | 31.6% | 26.7% | 33.3% | 14 |
| 185 | Balzan, Jackson | SUS_COU1 | Curveball | 56 | 10 | 0.205 | 53.8 | 67.6 | 79.6 | 35.0% | 33.3% | 20.0% | 20.0% | 15 |
| 189 | Oe, Ryoya | OTT_TIT | Curveball | 57 | 10 | 0.210 | 53.5 | 66.9 | 77.7 | 29.4% | 20.0% | 30.0% | 20.0% | 16 |
| 211 | Peyton, Blake | GAT_GRI | Curveball | 58 | 13 | 0.209 | 52.6 | 63.0 | 77.1 | 18.2% | 9.1% | 15.4% | 38.5% | 17 |
| 226 | Peters, Garrett | NEW_YOR13 | Curveball | 89 | 22 | 0.236 | 51.9 | 60.4 | 79.8 | 28.9% | 17.4% | 18.2% | 27.3% | 18 |
| 233 | Sanchez, Edwin | LAK_ERI24 | Curveball | 53 | 12 | 0.242 | 51.6 | 59.2 | 79.9 | 42.9% | 28.6% | 8.3% | 33.3% | 19 |
| 243 | Wiltse, Ryan | EVA_OTT | Curveball | 75 | 10 | 0.245 | 51.1 | 57.4 | 81.6 | 31.6% | 18.2% | 30.0% | 10.0% | 20 |
| 250 | Barker, Alex | NEW_YOR13 | Curveball | 66 | 18 | 0.228 | 51.0 | 56.2 | 79.5 | 13.6% | 8.3% | 11.1% | 33.3% | 21 |
| 251 | Henderson, Drew | DOW_EAS1 | Curveball | 171 | 53 | 0.213 | 51.0 | 56.0 | 80.4 | 15.7% | 16.3% | 28.3% | 18.9% | 22 |
| 260 | Langrell, Connor | MIS_MUD | Curveball | 73 | 17 | 0.255 | 50.7 | 54.4 | 81.1 | 31.0% | 36.8% | 11.8% | 29.4% | 23 |
| 264 | Cooper, Garrett | NEW_YOR13 | Curveball | 92 | 28 | 0.221 | 50.6 | 53.7 | 79.3 | 23.8% | 17.2% | 25.0% | 25.0% | 24 |
| 273 | Helt, Robert | LAK_ERI24 | Curveball | 106 | 18 | 0.259 | 50.1 | 52.1 | 81.1 | 40.0% | 38.7% | 27.8% | 16.7% | 25 |

### Changeups

| Rank | Pitcher | Team | Pitch Type | Pitches | BBE | xwOBA | PVS 20-80 | PVS 0-100 | EV | Whiff% | K% | HardHit% | SweetSpot% | Pitch Type Rank |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 4 | Escobar, Anthony | TRO_AIG | Changeup | 82 | 23 | 0.123 | 77.2 | 99.5 | 70.9 | 33.3% | 30.0% | 4.3% | 13.0% | 1 |
| 19 | Peyton, Blake | GAT_GRI | Changeup | 62 | 17 | 0.149 | 71.7 | 96.8 | 71.2 | 31.0% | 15.8% | 5.9% | 23.5% | 2 |
| 20 | Hensey, Rob | SUS_COU1 | Changeup | 141 | 25 | 0.169 | 69.6 | 96.7 | 72.8 | 53.5% | 43.2% | 4.0% | 24.0% | 3 |
| 22 | Willeman, Landon | EVA_OTT | Changeup | 112 | 38 | 0.160 | 68.7 | 96.3 | 74.1 | 24.6% | 12.9% | 7.9% | 15.8% | 4 |
| 27 | Rodriguez, Joe Joe | NEW_JER6 | Changeup | 59 | 11 | 0.132 | 68.3 | 95.4 | 78.9 | 40.0% | 31.2% | 0.0% | 0.0% | 5 |
| 31 | Maietta, Dante | WIN_CIT29 | Changeup | 112 | 19 | 0.151 | 67.3 | 94.7 | 75.7 | 50.9% | 44.1% | 0.0% | 21.1% | 6 |
| 34 | Boies, Emiles | QUE_CAP | Changeup | 122 | 38 | 0.170 | 66.8 | 94.2 | 75.2 | 27.1% | 18.5% | 10.5% | 13.2% | 7 |
| 37 | Foster, Kobe | WAS_WIL3 | Changeup | 115 | 31 | 0.192 | 66.1 | 93.7 | 73.1 | 47.2% | 34.1% | 6.5% | 29.0% | 8 |
| 38 | Wiltse, Ryan | EVA_OTT | Changeup | 107 | 32 | 0.187 | 66.0 | 93.5 | 74.6 | 37.5% | 31.2% | 6.2% | 25.0% | 9 |
| 39 | Moreno, Jose | DOW_EAS1 | Changeup | 52 | 12 | 0.174 | 65.5 | 93.3 | 75.8 | 40.9% | 40.0% | 0.0% | 25.0% | 10 |
| 40 | Messina, Chris | FDU_KNI | Changeup | 68 | 16 | 0.252 | 65.3 | 93.1 | 75.3 | 16.7% | 5.9% | 6.2% | 18.8% | 11 |
| 61 | Cooper, Garrett | NEW_YOR13 | Changeup | 109 | 25 | 0.222 | 61.7 | 89.4 | 76.0 | 29.8% | 17.4% | 16.0% | 20.0% | 12 |
| 99 | VanMarter, Luke | LEM_COL | Changeup | 53 | 17 | 0.253 | 58.5 | 82.7 | 75.7 | 9.5% | 0.0% | 11.8% | 35.3% | 13 |
| 112 | Pindel, Buddie | SCH_BOO | Changeup | 88 | 21 | 0.219 | 57.9 | 80.5 | 77.2 | 35.9% | 21.7% | 9.5% | 28.6% | 14 |
| 113 | Rohde, Isaac | NEW_YOR13 | Changeup | 543 | 163 | 0.213 | 57.7 | 80.3 | 76.5 | 21.9% | 18.4% | 11.0% | 30.7% | 15 |
| 121 | Barreto, Brayhans | TRI_VAL | Changeup | 108 | 23 | 0.227 | 57.4 | 78.9 | 76.3 | 39.5% | 13.3% | 8.7% | 34.8% | 16 |
| 132 | Cameron, Zach | WIN_CIT29 | Changeup | 111 | 27 | 0.215 | 56.9 | 76.9 | 78.9 | 36.4% | 13.6% | 18.5% | 14.8% | 17 |
| 144 | Kines, Gunnar | JOL_SLA | Changeup | 176 | 65 | 0.224 | 56.1 | 74.8 | 76.9 | 25.3% | 24.0% | 23.1% | 27.7% | 18 |
| 146 | Balzan, Jackson | SUS_COU1 | Changeup | 198 | 61 | 0.232 | 55.9 | 74.5 | 76.1 | 29.5% | 21.9% | 16.4% | 36.1% | 19 |
| 152 | Plumadore, Carson | WIN_CIT29 | Changeup | 180 | 53 | 0.209 | 55.7 | 73.4 | 78.4 | 28.4% | 18.6% | 11.3% | 26.4% | 20 |
| 157 | Dill, Austin | TRI_VAL | Changeup | 184 | 36 | 0.218 | 55.4 | 72.5 | 78.3 | 42.2% | 27.0% | 19.4% | 22.2% | 21 |
| 178 | Sakurai, Masatoshi | QUE_CAP | Changeup | 103 | 24 | 0.250 | 54.2 | 68.8 | 78.0 | 34.1% | 22.7% | 16.7% | 29.2% | 22 |
| 181 | Roland, Cole | QUE_CAP | Changeup | 71 | 17 | 0.244 | 54.0 | 68.3 | 78.2 | 19.2% | 11.1% | 11.8% | 35.3% | 23 |
| 186 | DeCastro, Justin | LON_ISL22 | Changeup | 122 | 42 | 0.236 | 53.8 | 67.4 | 79.4 | 18.3% | 8.6% | 14.3% | 26.2% | 24 |
| 200 | Thompson, Ross | SCH_BOO | Changeup | 82 | 12 | 0.234 | 53.0 | 65.0 | 80.0 | 50.0% | 47.6% | 16.7% | 25.0% | 25 |

## Standardized Coefficients Used

| Metric | Standardized Coefficient | Score Direction |
|---|---:|---|
| `whiff_pct` | 0.003254 | helps score when lower |
| `csw_pct` | 0.029336 | helps score when lower |
| `putaway_pct` | -0.014520 | helps score when higher |
| `k_pct` | -0.043673 | helps score when higher |
| `avg_exit_velocity` | 0.589000 | helps score when lower |
| `hardhit_pct` | 0.239017 | helps score when lower |
| `barrel_pct` | -0.049151 | helps score when higher |
| `sweetspot_pct` | 0.303807 | helps score when lower |