# Frontier League Pitch Value Score

- Input file: `data\processed\pitcher_pitch_type_xwoba_metrics.csv`
- Output file: `data\processed\pitch_value_scores.csv`
- Qualified pitcher-pitch types scored: 744
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
| 1 | Grounds, Jackson | DOW_EAS1 | Curveball | 82 | 10 | 0.110 | 80.0 | 100.0 | 64.6 | 42.1% | 41.2% | 0.0% | 0.0% | 1 |
| 2 | Morgan, Cooper | QUE_CAP | Curveball | 51 | 15 | 0.119 | 80.0 | 99.9 | 61.1 | 30.8% | 41.7% | 6.7% | 40.0% | 2 |
| 3 | Vecerka, Boris | QUE_CAP | Slider | 61 | 10 | 0.109 | 80.0 | 99.7 | 67.8 | 35.3% | 46.2% | 0.0% | 20.0% | 1 |
| 4 | Carroll, Jake | JOL_SLA | Slider | 62 | 11 | 0.208 | 80.0 | 99.6 | 68.7 | 25.0% | 28.6% | 0.0% | 18.2% | 2 |
| 5 | Ryan, Dillon | NEW_ENG23 | Slider | 113 | 22 | 0.149 | 79.2 | 99.5 | 70.2 | 34.8% | 38.5% | 0.0% | 18.2% | 3 |
| 6 | Lawson, Nathan | FLO_Y'A | Changeup | 51 | 17 | 0.168 | 77.0 | 99.3 | 72.9 | 20.0% | 23.1% | 5.9% | 5.9% | 1 |
| 7 | Harper, Scott | NEW_YOR13 | Slider | 174 | 28 | 0.146 | 76.7 | 99.2 | 71.5 | 48.4% | 45.2% | 3.6% | 14.3% | 4 |
| 8 | Peyton, Blake | GAT_GRI | Changeup | 87 | 20 | 0.142 | 76.4 | 99.1 | 70.1 | 36.8% | 16.0% | 5.0% | 20.0% | 2 |
| 9 | Alpern, Liam | FLO_Y'A | Slider | 78 | 16 | 0.115 | 75.5 | 98.9 | 69.9 | 14.3% | 35.7% | 12.5% | 18.8% | 5 |
| 10 | Rodriguez, Joe Joe | NEW_JER6 | Changeup | 82 | 15 | 0.120 | 74.8 | 98.8 | 75.7 | 46.5% | 28.6% | 0.0% | 0.0% | 3 |
| 11 | Serrano, Elio | NEW_JER6 | Changeup | 55 | 13 | 0.162 | 74.3 | 98.7 | 69.5 | 35.3% | 25.0% | 7.7% | 30.8% | 4 |
| 12 | Jones, Logan | TRI_VAL | Slider | 65 | 17 | 0.191 | 73.7 | 98.5 | 68.2 | 23.1% | 25.0% | 11.8% | 35.3% | 6 |
| 13 | Davis, Tyler | WIN_CIT29 | Four-Seam | 76 | 19 | 0.113 | 73.6 | 98.4 | 75.6 | 23.1% | 19.0% | 5.3% | 0.0% | 1 |
| 14 | Grounds, Jackson | DOW_EAS1 | Four-Seam | 107 | 27 | 0.161 | 73.5 | 98.3 | 69.9 | 25.5% | 21.7% | 11.1% | 25.9% | 2 |
| 15 | Webster, Evan | FLO_Y'A | Cutter | 108 | 26 | 0.147 | 73.5 | 98.1 | 72.6 | 29.8% | 25.0% | 11.5% | 11.5% | 1 |
| 16 | Bargo, Casey | NEW_ENG23 | Slider | 56 | 16 | 0.178 | 72.8 | 98.0 | 74.6 | 28.0% | 40.0% | 0.0% | 12.5% | 7 |
| 17 | Garcia, Hector | WAS_WIL3 | Splitter | 62 | 13 | 0.187 | 72.7 | 97.8 | 71.1 | 45.7% | 40.0% | 7.7% | 23.1% | 1 |
| 18 | Lovell, Justin | WIN_CIT29 | Sinker | 89 | 25 | 0.127 | 72.2 | 97.7 | 71.2 | 12.1% | 5.3% | 8.0% | 24.0% | 1 |
| 19 | Escobar, Anthony | TRO_AIG | Changeup | 104 | 30 | 0.150 | 72.0 | 97.6 | 73.1 | 32.7% | 24.1% | 6.7% | 16.7% | 5 |
| 20 | McEvoy, Aidan | FLO_Y'A | Slider | 100 | 25 | 0.146 | 71.7 | 97.4 | 73.5 | 38.6% | 31.2% | 8.0% | 16.0% | 8 |
| 21 | Correa, Nelvin | QUE_CAP | Cutter | 88 | 24 | 0.140 | 71.5 | 97.3 | 71.9 | 27.3% | 19.0% | 8.3% | 20.8% | 2 |
| 22 | Cameron, Zach | WIN_CIT29 | Four-Seam | 98 | 39 | 0.206 | 70.9 | 97.2 | 72.7 | 14.9% | 21.4% | 12.8% | 15.4% | 3 |
| 23 | Kirby, Zach | WAS_WIL3 | Slider | 127 | 42 | 0.158 | 70.9 | 97.0 | 73.3 | 21.1% | 13.8% | 2.4% | 21.4% | 9 |
| 24 | Moore, Kyle | SCH_BOO | Slider | 53 | 20 | 0.178 | 70.4 | 96.9 | 73.5 | 20.7% | 12.5% | 10.0% | 15.0% | 10 |
| 25 | Nakata, Yuto | QUE_CAP | Slider | 90 | 21 | 0.162 | 69.8 | 96.8 | 74.8 | 36.1% | 29.2% | 0.0% | 19.0% | 11 |

## Leaderboards by Pitch Family

### Four-Seams

| Rank | Pitcher | Team | Pitch Type | Pitches | BBE | xwOBA | PVS 20-80 | PVS 0-100 | EV | Whiff% | K% | HardHit% | SweetSpot% | Pitch Type Rank |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 13 | Davis, Tyler | WIN_CIT29 | Four-Seam | 76 | 19 | 0.113 | 73.6 | 98.4 | 75.6 | 23.1% | 19.0% | 5.3% | 0.0% | 1 |
| 14 | Grounds, Jackson | DOW_EAS1 | Four-Seam | 107 | 27 | 0.161 | 73.5 | 98.3 | 69.9 | 25.5% | 21.7% | 11.1% | 25.9% | 2 |
| 22 | Cameron, Zach | WIN_CIT29 | Four-Seam | 98 | 39 | 0.206 | 70.9 | 97.2 | 72.7 | 14.9% | 21.4% | 12.8% | 15.4% | 3 |
| 40 | Correa, Nelvin | QUE_CAP | Four-Seam | 75 | 23 | 0.185 | 66.5 | 94.8 | 75.4 | 13.3% | 0.0% | 8.7% | 13.0% | 4 |
| 54 | Foy, Corbin | LAK_ERI24 | Four-Seam | 96 | 19 | 0.179 | 65.0 | 92.9 | 72.9 | 18.5% | 25.0% | 5.3% | 36.8% | 5 |
| 67 | Gregory, Ben | GAT_GRI | Four-Seam | 90 | 18 | 0.188 | 63.6 | 91.1 | 77.0 | 24.1% | 9.5% | 5.6% | 16.7% | 6 |
| 70 | Rodriguez, Joe Joe | NEW_JER6 | Four-Seam | 67 | 22 | 0.184 | 63.2 | 90.7 | 77.9 | 22.9% | 20.0% | 4.5% | 18.2% | 7 |
| 76 | MacMillan, Blake | TRO_AIG | Four-Seam | 129 | 40 | 0.191 | 62.6 | 89.9 | 75.4 | 37.3% | 42.3% | 12.5% | 25.0% | 8 |
| 78 | Shears, Tanner | SCH_BOO | Four-Seam | 205 | 35 | 0.188 | 62.4 | 89.7 | 74.5 | 38.5% | 31.7% | 5.7% | 34.3% | 9 |
| 87 | Brown, Ethan | WAS_WIL3 | Four-Seam | 67 | 25 | 0.220 | 61.6 | 88.4 | 74.2 | 10.0% | 12.5% | 16.0% | 28.0% | 10 |
| 88 | Riedel, Caleb | SCH_BOO | Four-Seam | 153 | 42 | 0.252 | 61.5 | 88.3 | 73.7 | 35.2% | 42.9% | 11.9% | 38.1% | 11 |
| 90 | Anderson, Colt | WAS_WIL3 | Four-Seam | 227 | 83 | 0.219 | 61.4 | 88.0 | 73.8 | 14.7% | 15.2% | 12.0% | 36.1% | 12 |
| 92 | Foster, Kobe | WAS_WIL3 | Four-Seam | 354 | 124 | 0.187 | 61.3 | 87.8 | 75.9 | 27.2% | 25.0% | 8.9% | 27.4% | 13 |
| 97 | Brouwer, Adam | LAK_ERI24 | Four-Seam | 96 | 40 | 0.184 | 60.6 | 87.1 | 76.6 | 23.2% | 25.0% | 7.5% | 27.5% | 14 |
| 98 | Hensey, Rob | SUS_COU1 | Four-Seam | 192 | 54 | 0.191 | 60.5 | 87.0 | 75.3 | 32.6% | 32.5% | 9.3% | 33.3% | 15 |
| 104 | Mercado, Nelson | OTT_TIT | Four-Seam | 81 | 27 | 0.172 | 60.3 | 86.2 | 76.2 | 17.9% | 5.9% | 11.1% | 25.9% | 16 |
| 105 | Cartwright, Eli | GAT_GRI | Four-Seam | 165 | 41 | 0.195 | 60.2 | 86.0 | 76.4 | 33.3% | 25.7% | 9.8% | 26.8% | 17 |
| 113 | Ortiz, Julio | GAT_GRI | Four-Seam | 311 | 73 | 0.199 | 59.6 | 84.9 | 77.4 | 32.1% | 26.5% | 5.5% | 27.4% | 18 |
| 116 | Wehrle, Tyler | WIN_CIT29 | Four-Seam | 236 | 50 | 0.191 | 59.2 | 84.5 | 76.4 | 33.0% | 30.6% | 10.0% | 30.0% | 19 |
| 124 | Kaminer, Brandon | DOW_EAS1 | Four-Seam | 185 | 57 | 0.229 | 59.0 | 83.5 | 76.5 | 12.7% | 14.5% | 8.8% | 31.6% | 20 |
| 126 | Garcia, Brett | OTT_TIT | Four-Seam | 229 | 67 | 0.203 | 58.9 | 83.2 | 76.2 | 37.0% | 35.5% | 9.0% | 34.3% | 21 |
| 133 | Langhorne, Miles | SUS_COU1 | Four-Seam | 70 | 21 | 0.248 | 58.6 | 82.3 | 76.0 | 10.0% | 6.7% | 9.5% | 33.3% | 22 |
| 138 | Zaffiro, Cole | SCH_BOO | Four-Seam | 210 | 51 | 0.195 | 58.4 | 81.6 | 76.9 | 32.5% | 26.5% | 5.9% | 33.3% | 23 |
| 141 | Vilchez, Michael | OTT_TIT | Four-Seam | 79 | 23 | 0.221 | 58.3 | 81.2 | 77.7 | 28.9% | 27.3% | 13.0% | 26.1% | 24 |
| 147 | Kelly, Colin | SUS_COU1 | Four-Seam | 82 | 30 | 0.216 | 58.0 | 80.4 | 78.7 | 15.4% | 8.0% | 10.0% | 20.0% | 25 |

### Sinkers

| Rank | Pitcher | Team | Pitch Type | Pitches | BBE | xwOBA | PVS 20-80 | PVS 0-100 | EV | Whiff% | K% | HardHit% | SweetSpot% | Pitch Type Rank |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 18 | Lovell, Justin | WIN_CIT29 | Sinker | 89 | 25 | 0.127 | 72.2 | 97.7 | 71.2 | 12.1% | 5.3% | 8.0% | 24.0% | 1 |
| 30 | Still, Stephen | TRI_VAL | Sinker | 61 | 18 | 0.216 | 68.8 | 96.1 | 74.7 | 25.8% | 36.4% | 11.1% | 16.7% | 2 |
| 56 | Riedel, Caleb | SCH_BOO | Sinker | 64 | 19 | 0.158 | 64.9 | 92.6 | 73.6 | 28.1% | 25.0% | 10.5% | 26.3% | 3 |
| 58 | Colon, Jeffrey | TRO_AIG | Sinker | 56 | 17 | 0.173 | 64.3 | 92.3 | 73.9 | 18.5% | 13.3% | 23.5% | 17.6% | 4 |
| 68 | Glickstein, Aaron | SCH_BOO | Sinker | 85 | 30 | 0.186 | 63.5 | 91.0 | 74.8 | 11.9% | 9.5% | 6.7% | 26.7% | 5 |
| 75 | Mannering, Shawn | DOW_EAS1 | Sinker | 59 | 15 | 0.261 | 62.7 | 90.1 | 74.8 | 22.2% | 6.7% | 13.3% | 26.7% | 6 |
| 79 | Lawson, Nathan | FLO_Y'A | Sinker | 145 | 51 | 0.191 | 62.4 | 89.5 | 76.1 | 11.3% | 8.1% | 5.9% | 25.5% | 7 |
| 91 | Widener, Jacob | SUS_COU1 | Sinker | 114 | 34 | 0.181 | 61.3 | 87.9 | 74.5 | 30.9% | 11.5% | 11.8% | 29.4% | 8 |
| 96 | Cerda, Junior | EVA_OTT | Sinker | 78 | 30 | 0.200 | 60.8 | 87.2 | 75.0 | 11.1% | 10.5% | 0.0% | 40.0% | 9 |
| 122 | Sabatine, Gino | TRI_VAL | Sinker | 54 | 19 | 0.195 | 59.1 | 83.7 | 76.2 | 13.0% | 7.1% | 10.5% | 31.6% | 10 |
| 130 | Morgan, Marcus | JOL_SLA | Sinker | 83 | 18 | 0.223 | 58.7 | 82.7 | 76.1 | 33.3% | 36.8% | 11.1% | 33.3% | 11 |
| 168 | Grounds, Jackson | DOW_EAS1 | Sinker | 116 | 26 | 0.217 | 56.7 | 77.6 | 76.8 | 22.9% | 7.7% | 11.5% | 30.8% | 12 |
| 173 | McCartney, Seth | MIS_MUD | Sinker | 120 | 39 | 0.240 | 56.4 | 76.9 | 78.3 | 8.3% | 5.3% | 20.5% | 17.9% | 13 |
| 174 | Turner, Eric | JOL_SLA | Sinker | 89 | 34 | 0.214 | 56.4 | 76.7 | 76.4 | 17.4% | 9.7% | 17.6% | 29.4% | 14 |
| 179 | Henderson, Drew | DOW_EAS1 | Sinker | 106 | 29 | 0.215 | 56.2 | 76.1 | 76.9 | 14.3% | 16.0% | 13.8% | 31.0% | 15 |
| 191 | Cook, Cole | SCH_BOO | Sinker | 84 | 25 | 0.217 | 55.8 | 74.5 | 75.2 | 20.0% | 10.5% | 12.0% | 40.0% | 16 |
| 198 | Hensey, Rob | SUS_COU1 | Sinker | 373 | 139 | 0.229 | 55.6 | 73.5 | 77.0 | 17.3% | 17.7% | 15.1% | 31.7% | 17 |
| 199 | Long, Maddox | WAS_WIL3 | Sinker | 285 | 84 | 0.236 | 55.6 | 73.4 | 78.6 | 15.4% | 17.8% | 15.5% | 23.8% | 18 |
| 202 | Plumadore, Carson | WIN_CIT29 | Sinker | 113 | 36 | 0.200 | 55.6 | 73.0 | 76.1 | 16.0% | 41.7% | 8.3% | 44.4% | 19 |
| 207 | Fritz, AJ | MIS_MUD | Sinker | 55 | 21 | 0.240 | 55.2 | 72.3 | 78.5 | 28.1% | 16.7% | 9.5% | 33.3% | 20 |
| 215 | Martzolf, Max | JOL_SLA | Sinker | 169 | 44 | 0.242 | 54.8 | 71.2 | 77.3 | 15.0% | 11.4% | 18.2% | 29.5% | 21 |
| 220 | Joven, Art | MIS_MUD | Sinker | 275 | 74 | 0.236 | 54.6 | 70.6 | 78.4 | 8.8% | 7.6% | 17.6% | 24.3% | 22 |
| 224 | Pierson, Kenny | LAK_ERI24 | Sinker | 192 | 57 | 0.227 | 54.3 | 70.0 | 79.1 | 0.0% | 2.1% | 15.8% | 21.1% | 23 |
| 231 | Kelly, Colin | SUS_COU1 | Sinker | 96 | 29 | 0.191 | 54.1 | 69.1 | 77.5 | 25.0% | 11.1% | 17.2% | 31.0% | 24 |
| 232 | Peyton, Blake | GAT_GRI | Sinker | 73 | 25 | 0.179 | 54.0 | 69.0 | 78.8 | 26.5% | 18.8% | 12.0% | 28.0% | 25 |

### Sliders

| Rank | Pitcher | Team | Pitch Type | Pitches | BBE | xwOBA | PVS 20-80 | PVS 0-100 | EV | Whiff% | K% | HardHit% | SweetSpot% | Pitch Type Rank |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 3 | Vecerka, Boris | QUE_CAP | Slider | 61 | 10 | 0.109 | 80.0 | 99.7 | 67.8 | 35.3% | 46.2% | 0.0% | 20.0% | 1 |
| 4 | Carroll, Jake | JOL_SLA | Slider | 62 | 11 | 0.208 | 80.0 | 99.6 | 68.7 | 25.0% | 28.6% | 0.0% | 18.2% | 2 |
| 5 | Ryan, Dillon | NEW_ENG23 | Slider | 113 | 22 | 0.149 | 79.2 | 99.5 | 70.2 | 34.8% | 38.5% | 0.0% | 18.2% | 3 |
| 7 | Harper, Scott | NEW_YOR13 | Slider | 174 | 28 | 0.146 | 76.7 | 99.2 | 71.5 | 48.4% | 45.2% | 3.6% | 14.3% | 4 |
| 9 | Alpern, Liam | FLO_Y'A | Slider | 78 | 16 | 0.115 | 75.5 | 98.9 | 69.9 | 14.3% | 35.7% | 12.5% | 18.8% | 5 |
| 12 | Jones, Logan | TRI_VAL | Slider | 65 | 17 | 0.191 | 73.7 | 98.5 | 68.2 | 23.1% | 25.0% | 11.8% | 35.3% | 6 |
| 16 | Bargo, Casey | NEW_ENG23 | Slider | 56 | 16 | 0.178 | 72.8 | 98.0 | 74.6 | 28.0% | 40.0% | 0.0% | 12.5% | 7 |
| 20 | McEvoy, Aidan | FLO_Y'A | Slider | 100 | 25 | 0.146 | 71.7 | 97.4 | 73.5 | 38.6% | 31.2% | 8.0% | 16.0% | 8 |
| 23 | Kirby, Zach | WAS_WIL3 | Slider | 127 | 42 | 0.158 | 70.9 | 97.0 | 73.3 | 21.1% | 13.8% | 2.4% | 21.4% | 9 |
| 24 | Moore, Kyle | SCH_BOO | Slider | 53 | 20 | 0.178 | 70.4 | 96.9 | 73.5 | 20.7% | 12.5% | 10.0% | 15.0% | 10 |
| 25 | Nakata, Yuto | QUE_CAP | Slider | 90 | 21 | 0.162 | 69.8 | 96.8 | 74.8 | 36.1% | 29.2% | 0.0% | 19.0% | 11 |
| 26 | Toribio, Noe | TRO_AIG | Slider | 107 | 29 | 0.154 | 69.7 | 96.6 | 72.5 | 22.2% | 20.0% | 6.9% | 24.1% | 12 |
| 27 | Donnan, Blake | FLO_Y'A | Slider | 65 | 10 | 0.187 | 69.2 | 96.5 | 71.5 | 51.7% | 52.9% | 10.0% | 30.0% | 13 |
| 31 | Sechrist, Zander | WAS_WIL3 | Slider | 60 | 17 | 0.183 | 68.5 | 96.0 | 71.8 | 25.0% | 12.5% | 5.9% | 29.4% | 14 |
| 35 | Hickey, Matt | GAT_GRI | Slider | 75 | 21 | 0.194 | 67.6 | 95.4 | 73.1 | 25.8% | 15.8% | 14.3% | 19.0% | 15 |
| 39 | Balzan, Jackson | SUS_COU1 | Slider | 65 | 18 | 0.189 | 66.6 | 94.9 | 73.1 | 40.0% | 35.0% | 11.1% | 27.8% | 16 |
| 45 | Vega, Lucas | TRO_AIG | Slider | 117 | 33 | 0.153 | 66.0 | 94.1 | 75.8 | 26.0% | 27.3% | 6.1% | 18.2% | 17 |
| 47 | Smith, Jackson | MIS_MUD | Slider | 106 | 32 | 0.199 | 65.9 | 93.8 | 75.0 | 24.5% | 42.9% | 9.4% | 21.9% | 18 |
| 53 | Morin, Jacob | QUE_CAP | Slider | 85 | 20 | 0.208 | 65.1 | 93.0 | 73.4 | 30.6% | 30.4% | 10.0% | 30.0% | 19 |
| 55 | Harajli, Ahmad | FLO_Y'A | Slider | 69 | 19 | 0.169 | 65.0 | 92.7 | 76.0 | 38.7% | 35.3% | 5.3% | 21.1% | 20 |
| 59 | Perozzi, John | SUS_COU1 | Slider | 123 | 29 | 0.176 | 64.1 | 92.2 | 73.8 | 45.2% | 42.4% | 13.8% | 27.6% | 21 |
| 63 | Petschke, Ben | EVA_OTT | Slider | 138 | 40 | 0.184 | 63.9 | 91.7 | 75.3 | 19.0% | 24.2% | 10.0% | 22.5% | 22 |
| 72 | Fauci, Sonny | NEW_JER6 | Slider | 87 | 15 | 0.229 | 62.8 | 90.5 | 77.0 | 54.3% | 42.9% | 6.7% | 20.0% | 23 |
| 73 | Ronne, Andrew | GAT_GRI | Slider | 122 | 19 | 0.179 | 62.8 | 90.3 | 75.9 | 43.2% | 38.1% | 5.3% | 26.3% | 24 |
| 77 | Foster, Kobe | WAS_WIL3 | Slider | 118 | 33 | 0.187 | 62.6 | 89.8 | 73.5 | 30.8% | 32.3% | 15.2% | 30.3% | 25 |

### Curveballs

| Rank | Pitcher | Team | Pitch Type | Pitches | BBE | xwOBA | PVS 20-80 | PVS 0-100 | EV | Whiff% | K% | HardHit% | SweetSpot% | Pitch Type Rank |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | Grounds, Jackson | DOW_EAS1 | Curveball | 82 | 10 | 0.110 | 80.0 | 100.0 | 64.6 | 42.1% | 41.2% | 0.0% | 0.0% | 1 |
| 2 | Morgan, Cooper | QUE_CAP | Curveball | 51 | 15 | 0.119 | 80.0 | 99.9 | 61.1 | 30.8% | 41.7% | 6.7% | 40.0% | 2 |
| 34 | Sechrist, Zander | WAS_WIL3 | Curveball | 70 | 21 | 0.187 | 67.7 | 95.6 | 71.0 | 15.6% | 11.8% | 9.5% | 33.3% | 3 |
| 41 | Eisenbarger, Jack | QUE_CAP | Curveball | 71 | 10 | 0.214 | 66.4 | 94.6 | 69.9 | 29.4% | 33.3% | 10.0% | 50.0% | 4 |
| 42 | Garcia, Brett | OTT_TIT | Curveball | 104 | 19 | 0.177 | 66.1 | 94.5 | 76.7 | 33.3% | 47.8% | 10.5% | 10.5% | 5 |
| 43 | Salata, Derek | SCH_BOO | Curveball | 83 | 19 | 0.205 | 66.0 | 94.4 | 73.6 | 38.5% | 47.8% | 5.3% | 31.6% | 6 |
| 51 | Harris, Ben | GAT_GRI | Curveball | 205 | 21 | 0.218 | 65.7 | 93.3 | 75.8 | 35.6% | 54.3% | 9.5% | 19.0% | 7 |
| 52 | Binns, Malik | NEW_JER6 | Curveball | 55 | 13 | 0.187 | 65.6 | 93.1 | 73.8 | 27.3% | 13.3% | 7.7% | 30.8% | 8 |
| 61 | Bohnert, Matthew | WIN_CIT29 | Curveball | 83 | 10 | 0.170 | 64.0 | 91.9 | 78.2 | 44.1% | 50.0% | 10.0% | 10.0% | 9 |
| 69 | Hill, Kaleb | OTT_TIT | Curveball | 201 | 47 | 0.211 | 63.4 | 90.9 | 74.2 | 29.3% | 18.9% | 10.6% | 27.7% | 10 |
| 74 | Heredia-Bustos, Rolando | DOW_EAS1 | Curveball | 53 | 17 | 0.190 | 62.7 | 90.2 | 74.3 | 28.6% | 25.0% | 17.6% | 23.5% | 11 |
| 80 | Simpson, Garret | EVA_OTT | Curveball | 94 | 20 | 0.203 | 62.3 | 89.4 | 78.7 | 29.4% | 25.9% | 10.0% | 10.0% | 12 |
| 84 | Maryniak, Connor | NEW_JER6 | Curveball | 121 | 29 | 0.225 | 61.8 | 88.8 | 78.0 | 42.6% | 45.2% | 6.9% | 17.2% | 13 |
| 99 | Petery, Dylan | WIN_CIT29 | Curveball | 56 | 12 | 0.217 | 60.5 | 86.8 | 77.9 | 22.7% | 16.7% | 0.0% | 25.0% | 14 |
| 100 | Scafidi, Christian | LAK_ERI24 | Curveball | 55 | 12 | 0.195 | 60.5 | 86.7 | 75.7 | 22.2% | 41.7% | 8.3% | 33.3% | 15 |
| 107 | Earwood, Micah | SUS_COU1 | Curveball | 82 | 12 | 0.204 | 60.1 | 85.8 | 76.9 | 37.9% | 35.0% | 33.3% | 8.3% | 16 |
| 110 | Gollert, Harley | TRO_AIG | Curveball | 52 | 10 | 0.240 | 59.8 | 85.3 | 77.3 | 43.5% | 15.4% | 0.0% | 30.0% | 17 |
| 114 | Wiltse, Ryan | EVA_OTT | Curveball | 116 | 16 | 0.233 | 59.4 | 84.8 | 78.5 | 32.1% | 30.0% | 18.8% | 12.5% | 18 |
| 135 | Anibal, Trevor | NEW_ENG23 | Curveball | 99 | 18 | 0.236 | 58.6 | 82.0 | 74.3 | 42.1% | 50.0% | 16.7% | 38.9% | 19 |
| 143 | Vail, Tyler | NEW_YOR13 | Curveball | 182 | 22 | 0.217 | 58.1 | 80.9 | 80.0 | 36.0% | 28.6% | 4.5% | 22.7% | 20 |
| 152 | De Los Santos, Enmanuel | NEW_ENG23 | Curveball | 87 | 11 | 0.220 | 57.8 | 79.7 | 77.4 | 38.1% | 40.0% | 18.2% | 27.3% | 21 |
| 164 | Lefebvre, Charles | TRO_AIG | Curveball | 89 | 22 | 0.255 | 56.9 | 78.1 | 76.7 | 34.2% | 45.8% | 4.5% | 40.9% | 22 |
| 171 | Peters, Garrett | NEW_YOR13 | Curveball | 118 | 32 | 0.230 | 56.5 | 77.2 | 78.5 | 24.5% | 16.7% | 12.5% | 25.0% | 23 |
| 178 | Petschke, Ben | EVA_OTT | Curveball | 164 | 40 | 0.235 | 56.3 | 76.2 | 79.8 | 22.6% | 11.6% | 12.5% | 17.5% | 24 |
| 182 | Balzan, Jackson | SUS_COU1 | Curveball | 69 | 14 | 0.218 | 56.1 | 75.7 | 78.9 | 34.6% | 33.3% | 14.3% | 21.4% | 25 |

### Changeups

| Rank | Pitcher | Team | Pitch Type | Pitches | BBE | xwOBA | PVS 20-80 | PVS 0-100 | EV | Whiff% | K% | HardHit% | SweetSpot% | Pitch Type Rank |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 6 | Lawson, Nathan | FLO_Y'A | Changeup | 51 | 17 | 0.168 | 77.0 | 99.3 | 72.9 | 20.0% | 23.1% | 5.9% | 5.9% | 1 |
| 8 | Peyton, Blake | GAT_GRI | Changeup | 87 | 20 | 0.142 | 76.4 | 99.1 | 70.1 | 36.8% | 16.0% | 5.0% | 20.0% | 2 |
| 10 | Rodriguez, Joe Joe | NEW_JER6 | Changeup | 82 | 15 | 0.120 | 74.8 | 98.8 | 75.7 | 46.5% | 28.6% | 0.0% | 0.0% | 3 |
| 11 | Serrano, Elio | NEW_JER6 | Changeup | 55 | 13 | 0.162 | 74.3 | 98.7 | 69.5 | 35.3% | 25.0% | 7.7% | 30.8% | 4 |
| 19 | Escobar, Anthony | TRO_AIG | Changeup | 104 | 30 | 0.150 | 72.0 | 97.6 | 73.1 | 32.7% | 24.1% | 6.7% | 16.7% | 5 |
| 28 | Sesar, Jorden | SUS_COU1 | Changeup | 64 | 15 | 0.150 | 69.1 | 96.4 | 74.8 | 31.0% | 33.3% | 6.7% | 20.0% | 6 |
| 29 | Harris, Everette | TRI_VAL | Changeup | 96 | 27 | 0.171 | 69.0 | 96.2 | 74.3 | 15.9% | 7.1% | 7.4% | 14.8% | 7 |
| 33 | Parsons, Billy | SUS_COU1 | Changeup | 61 | 17 | 0.235 | 67.8 | 95.7 | 74.2 | 28.1% | 41.2% | 5.9% | 23.5% | 8 |
| 38 | Tokar, Heitor | OTT_TIT | Changeup | 63 | 21 | 0.189 | 66.7 | 95.0 | 74.0 | 20.7% | 11.8% | 9.5% | 23.8% | 9 |
| 44 | Hocom, Quinn | TRI_VAL | Changeup | 73 | 18 | 0.186 | 66.0 | 94.2 | 74.3 | 24.1% | 20.0% | 22.2% | 16.7% | 10 |
| 46 | Drakeford, Dosie | NEW_JER6 | Changeup | 71 | 14 | 0.143 | 66.0 | 94.0 | 73.7 | 53.1% | 50.0% | 0.0% | 35.7% | 11 |
| 48 | Morgan, Cooper | QUE_CAP | Changeup | 66 | 18 | 0.183 | 65.9 | 93.7 | 72.9 | 32.3% | 28.6% | 5.6% | 33.3% | 12 |
| 49 | Messina, Chris | FDU_KNI | Changeup | 68 | 16 | 0.257 | 65.8 | 93.5 | 75.3 | 16.7% | 5.9% | 6.2% | 18.8% | 13 |
| 50 | Miner, Jace | DOW_EAS1 | Changeup | 78 | 22 | 0.240 | 65.7 | 93.4 | 72.9 | 21.2% | 18.8% | 13.6% | 27.3% | 14 |
| 64 | Cooper, Garrett | NEW_YOR13 | Changeup | 198 | 49 | 0.202 | 63.8 | 91.5 | 75.9 | 32.3% | 26.7% | 10.2% | 20.4% | 15 |
| 65 | Maietta, Dante | WIN_CIT29 | Changeup | 191 | 34 | 0.180 | 63.8 | 91.4 | 77.7 | 45.0% | 33.3% | 2.9% | 17.6% | 16 |
| 66 | Wiltse, Ryan | EVA_OTT | Changeup | 120 | 37 | 0.204 | 63.7 | 91.3 | 75.2 | 34.8% | 28.6% | 8.1% | 27.0% | 17 |
| 71 | Leak, Anthony | NEW_YOR13 | Changeup | 60 | 15 | 0.203 | 62.9 | 90.6 | 77.5 | 26.9% | 6.7% | 0.0% | 20.0% | 18 |
| 94 | Willeman, Landon | EVA_OTT | Changeup | 154 | 49 | 0.200 | 61.0 | 87.5 | 76.5 | 27.1% | 17.8% | 12.2% | 22.4% | 19 |
| 118 | Hensey, Rob | SUS_COU1 | Changeup | 226 | 49 | 0.210 | 59.1 | 84.3 | 76.9 | 43.1% | 39.1% | 14.3% | 24.5% | 20 |
| 120 | Foster, Kobe | WAS_WIL3 | Changeup | 149 | 46 | 0.232 | 59.1 | 84.0 | 75.9 | 43.2% | 25.9% | 8.7% | 32.6% | 21 |
| 121 | Henderson, Drew | DOW_EAS1 | Changeup | 126 | 34 | 0.212 | 59.1 | 83.9 | 75.1 | 29.5% | 20.6% | 14.7% | 32.4% | 22 |
| 123 | Rohde, Isaac | NEW_YOR13 | Changeup | 709 | 207 | 0.213 | 59.0 | 83.6 | 75.8 | 23.5% | 18.5% | 11.6% | 30.9% | 23 |
| 131 | VanMarter, Luke | LEM_COL | Changeup | 53 | 17 | 0.260 | 58.6 | 82.5 | 75.7 | 9.5% | 0.0% | 11.8% | 35.3% | 24 |
| 149 | Plumadore, Carson | WIN_CIT29 | Changeup | 209 | 59 | 0.208 | 57.8 | 80.1 | 77.3 | 31.2% | 20.0% | 10.2% | 27.1% | 25 |

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