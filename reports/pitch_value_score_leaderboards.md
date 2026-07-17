# Frontier League Pitch Value Score

- Input file: `data\processed\pitcher_pitch_type_xwoba_metrics.csv`
- Output file: `data\processed\pitch_value_scores.csv`
- Qualified pitcher-pitch types scored: 853
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
| GroundBall% | Share of tracked batted balls launched below 10 degrees. | Higher is better in the Ground Ball component score. |
| LineDrive% | Share of tracked batted balls launched from 10 to 25 degrees. | Lower is better in the Line Drive Suppression component score. |
| FlyBall% | Share of tracked batted balls launched above 25 degrees. | Lower is better in the Fly Ball Suppression component score. |

## Score Method

The score uses frozen standardized weights on the miss and contact metrics. Those weights encode how strongly each metric is associated with expected damage in the scoring system.

Each metric is standardized across qualified pitcher-pitch type rows. The standardized score weight is applied to estimate xwOBA pressure, then the sign is reversed so lower-xwOBA traits score higher.

`pitch_value_raw = -sum(standardized_weight * metric_z)`

- `pitch_value_20_80`: scouting-style scale, mean 50 and 10 points per standard deviation, clipped from 20 to 80.
- `pitch_value_0_100`: percentile rank of `pitch_value_raw` among qualified pitcher-pitch types.
- `overall_rank`: rank across all qualified pitcher-pitch types.
- `pitch_type_rank`: rank within that exact pitch type label.

Because the sign is reversed, a metric with a positive damage weight hurts the Pitch Value Score when it is high. A metric with a negative damage weight helps the score when it is high.

## Component Scores

The output also includes standalone component scores for ground-ball tendency, strikeout ability, line-drive suppression, and fly-ball suppression. Each component has a raw score, a 20-80 score, a percentile, an overall rank, and a pitch-type rank.

| Component | Metric | Direction |
|---|---|---|
| `groundball_score` | `groundball_pct` | higher metric scores better |
| `strikeout_score` | `k_pct` | higher metric scores better |
| `line_drive_score` | `line_drive_pct` | lower metric scores better |
| `flyball_score` | `flyball_pct` | lower metric scores better |

A component score of `50` is league average among qualified pitcher-pitch types; `60` is one standard deviation better. Component ranks sort highest score first.

## Methodology Notes

- The scoring model is descriptive. It identifies which observed pitch-level outcomes were associated with lower expected damage in this dataset.
- Contact quality carries much of the weight because average exit velocity, SweetSpot%, and HardHit% are the strongest damage signals in the current score.
- Miss metrics still matter for baseball evaluation, but in this multivariate score they receive less weight when contact quality already captures most of the damage signal.
- Small samples can still move the leaderboards. The qualification filter helps, but the score should be read with pitch count and batted-ball count nearby.
- The score does not directly include command, sequencing, handedness splits, game context, injury risk, or scouting grades.

## Top 25 Pitches in the League

| Rank | Pitcher | Team | Pitch Type | Pitches | BBE | xwOBA | PVS 20-80 | PVS 0-100 | EV | Whiff% | K% | HardHit% | SweetSpot% | GB Score | K Score | LD Supp | FB Supp | Pitch Type Rank |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | Grounds, Jackson | DOW_EAS1 | Curveball | 82 | 10 | 0.108 | 80.0 | 100.0 | 64.6 | 42.1% | 41.2% | 0.0% | 0.0% | 58.9 | 67.5 | 76.0 | 43.2 | 1 |
| 2 | Carroll, Jake | JOL_SLA | Slider | 68 | 12 | 0.190 | 80.0 | 99.9 | 68.3 | 26.9% | 28.6% | 0.0% | 16.7% | 52.4 | 57.2 | 54.2 | 49.9 | 1 |
| 3 | Morgan, Cooper | QUE_CAP | Curveball | 72 | 22 | 0.146 | 80.0 | 99.8 | 64.0 | 40.0% | 44.4% | 9.1% | 45.5% | 41.3 | 70.2 | 52.2 | 39.4 | 2 |
| 4 | Ryan, Dillon | NEW_ENG23 | Slider | 125 | 25 | 0.144 | 79.9 | 99.6 | 69.9 | 35.3% | 34.5% | 0.0% | 20.0% | 60.4 | 62.0 | 60.3 | 54.6 | 2 |
| 5 | Leduc, Zachary | TRO_AIG | Slider | 78 | 14 | 0.092 | 79.2 | 99.5 | 68.7 | 46.7% | 38.9% | 7.1% | 21.4% | 58.9 | 65.6 | 57.3 | 54.8 | 3 |
| 6 | Zentko, Dylan | EVA_OTT | Changeup | 67 | 13 | 0.155 | 78.6 | 99.4 | 70.2 | 44.8% | 35.7% | 7.7% | 15.4% | 67.8 | 63.0 | 55.9 | 65.1 | 1 |
| 7 | Lawson, Nathan | FLO_Y'A | Changeup | 60 | 17 | 0.166 | 78.2 | 99.3 | 72.9 | 27.6% | 37.5% | 5.9% | 5.9% | 52.0 | 64.5 | 76.0 | 36.0 | 2 |
| 8 | Vecerka, Boris | QUE_CAP | Slider | 74 | 14 | 0.129 | 77.6 | 99.2 | 71.2 | 31.8% | 41.2% | 7.1% | 14.3% | 53.3 | 67.5 | 57.3 | 49.0 | 4 |
| 9 | Peyton, Blake | GAT_GRI | Changeup | 93 | 20 | 0.141 | 77.3 | 99.1 | 70.1 | 37.5% | 15.4% | 5.0% | 20.0% | 70.4 | 46.4 | 56.4 | 67.6 | 3 |
| 10 | Alpern, Liam | FLO_Y'A | Slider | 78 | 16 | 0.113 | 76.4 | 98.9 | 69.9 | 14.3% | 35.7% | 12.5% | 18.8% | 54.0 | 63.0 | 67.8 | 43.2 | 5 |
| 11 | Serrano, Elio | NEW_JER6 | Changeup | 63 | 15 | 0.148 | 75.9 | 98.8 | 70.0 | 35.1% | 21.4% | 6.7% | 26.7% | 51.1 | 51.3 | 58.6 | 45.9 | 4 |
| 12 | Jones, Logan | TRI_VAL | Slider | 65 | 17 | 0.191 | 74.7 | 98.7 | 68.2 | 23.1% | 25.0% | 11.8% | 35.3% | 52.0 | 54.2 | 45.2 | 55.1 | 6 |
| 13 | Grounds, Jackson | DOW_EAS1 | Four-Seam | 107 | 27 | 0.159 | 74.4 | 98.6 | 69.9 | 25.5% | 21.7% | 11.1% | 25.9% | 37.4 | 51.6 | 51.8 | 35.6 | 1 |
| 14 | Davis, Tyler | WIN_CIT29 | Four-Seam | 76 | 19 | 0.111 | 74.4 | 98.5 | 75.6 | 23.1% | 19.0% | 5.3% | 0.0% | 44.6 | 49.4 | 76.0 | 28.1 | 2 |
| 15 | Debban, Caleb | NEW_JER6 | Four-Seam | 57 | 13 | 0.174 | 73.8 | 98.4 | 70.6 | 20.0% | 6.2% | 7.7% | 23.1% | 49.9 | 38.9 | 65.9 | 40.0 | 3 |
| 16 | Garcia, Hector | WAS_WIL3 | Splitter | 62 | 13 | 0.185 | 73.6 | 98.2 | 71.1 | 45.7% | 40.0% | 7.7% | 23.1% | 55.9 | 66.5 | 55.9 | 52.6 | 1 |
| 17 | Bargo, Casey | NEW_ENG23 | Slider | 56 | 16 | 0.176 | 73.6 | 98.1 | 74.6 | 28.0% | 40.0% | 0.0% | 12.5% | 68.5 | 66.5 | 59.6 | 63.5 | 7 |
| 18 | Hickey, Matt | GAT_GRI | Slider | 86 | 25 | 0.191 | 73.5 | 98.0 | 71.4 | 24.3% | 13.0% | 12.0% | 16.0% | 66.6 | 44.4 | 65.5 | 57.8 | 8 |
| 19 | Escobar, Anthony | TRO_AIG | Changeup | 147 | 38 | 0.156 | 72.7 | 97.9 | 73.0 | 40.3% | 25.6% | 10.5% | 13.2% | 52.8 | 54.8 | 62.2 | 45.3 | 5 |
| 20 | Harper, Scott | NEW_YOR13 | Slider | 212 | 33 | 0.155 | 72.6 | 97.8 | 72.9 | 50.0% | 45.3% | 6.1% | 18.2% | 39.0 | 70.8 | 64.1 | 29.6 | 9 |
| 21 | Lockhart, Gauge | LAK_ERI24 | Cutter | 95 | 27 | 0.160 | 72.5 | 97.7 | 72.7 | 29.2% | 36.4% | 7.4% | 18.5% | 48.8 | 63.5 | 66.3 | 38.6 | 1 |
| 22 | Bohnert, Matthew | WIN_CIT29 | Curveball | 97 | 12 | 0.143 | 71.9 | 97.5 | 75.1 | 46.2% | 47.4% | 8.3% | 8.3% | 65.3 | 72.5 | 76.0 | 49.9 | 3 |
| 23 | Kirby, Zach | WAS_WIL3 | Slider | 127 | 42 | 0.156 | 71.7 | 97.4 | 73.3 | 21.1% | 13.8% | 2.4% | 21.4% | 40.5 | 45.1 | 57.3 | 35.4 | 10 |
| 24 | Cameron, Zach | WIN_CIT29 | Four-Seam | 115 | 42 | 0.201 | 71.7 | 97.3 | 73.1 | 20.0% | 25.0% | 11.9% | 14.3% | 49.7 | 54.2 | 63.5 | 41.2 | 4 |
| 25 | Moore, Kyle | SCH_BOO | Slider | 53 | 20 | 0.177 | 71.2 | 97.2 | 73.5 | 20.7% | 12.5% | 10.0% | 15.0% | 35.7 | 44.0 | 56.4 | 30.9 | 11 |

## Leaderboards by Pitch Family

### Four-Seams

| Rank | Pitcher | Team | Pitch Type | Pitches | BBE | xwOBA | PVS 20-80 | PVS 0-100 | EV | Whiff% | K% | HardHit% | SweetSpot% | GB Score | K Score | LD Supp | FB Supp | Pitch Type Rank |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 13 | Grounds, Jackson | DOW_EAS1 | Four-Seam | 107 | 27 | 0.159 | 74.4 | 98.6 | 69.9 | 25.5% | 21.7% | 11.1% | 25.9% | 37.4 | 51.6 | 51.8 | 35.6 | 1 |
| 14 | Davis, Tyler | WIN_CIT29 | Four-Seam | 76 | 19 | 0.111 | 74.4 | 98.5 | 75.6 | 23.1% | 19.0% | 5.3% | 0.0% | 44.6 | 49.4 | 76.0 | 28.1 | 2 |
| 15 | Debban, Caleb | NEW_JER6 | Four-Seam | 57 | 13 | 0.174 | 73.8 | 98.4 | 70.6 | 20.0% | 6.2% | 7.7% | 23.1% | 49.9 | 38.9 | 65.9 | 40.0 | 3 |
| 24 | Cameron, Zach | WIN_CIT29 | Four-Seam | 115 | 42 | 0.201 | 71.7 | 97.3 | 73.1 | 20.0% | 25.0% | 11.9% | 14.3% | 49.7 | 54.2 | 63.5 | 41.2 | 4 |
| 39 | Grounds, Jackson | TRO_AIG | Four-Seam | 62 | 15 | 0.148 | 67.9 | 95.5 | 71.8 | 25.0% | 14.3% | 0.0% | 40.0% | 35.7 | 45.5 | 49.8 | 35.0 | 5 |
| 44 | Correa, Nelvin | QUE_CAP | Four-Seam | 86 | 29 | 0.192 | 67.2 | 95.0 | 74.9 | 10.8% | 0.0% | 6.9% | 17.2% | 49.5 | 33.8 | 67.0 | 38.9 | 6 |
| 54 | Foy, Corbin | LAK_ERI24 | Four-Seam | 96 | 19 | 0.177 | 65.8 | 93.8 | 72.9 | 18.5% | 25.0% | 5.3% | 36.8% | 40.6 | 54.2 | 48.4 | 41.0 | 7 |
| 71 | Gregory, Ben | GAT_GRI | Four-Seam | 93 | 18 | 0.186 | 64.1 | 91.8 | 77.0 | 26.7% | 9.5% | 5.6% | 16.7% | 54.6 | 41.6 | 61.5 | 47.7 | 8 |
| 80 | Garbrick, Alex | LAK_ERI24 | Four-Seam | 82 | 32 | 0.224 | 63.4 | 90.7 | 76.7 | 16.3% | 11.5% | 15.6% | 12.5% | 58.9 | 43.2 | 63.7 | 50.8 | 9 |
| 90 | Brown, Ethan | WAS_WIL3 | Four-Seam | 67 | 25 | 0.217 | 62.2 | 89.6 | 74.2 | 10.0% | 12.5% | 16.0% | 28.0% | 41.9 | 44.0 | 39.3 | 48.0 | 10 |
| 91 | Hensey, Rob | SUS_COU1 | Four-Seam | 220 | 60 | 0.187 | 62.2 | 89.4 | 75.2 | 33.0% | 31.1% | 8.3% | 31.7% | 47.3 | 59.2 | 56.4 | 43.2 | 11 |
| 93 | Morgan, Cooper | QUE_CAP | Four-Seam | 65 | 19 | 0.208 | 61.9 | 89.2 | 75.6 | 35.1% | 38.9% | 0.0% | 36.8% | 52.8 | 65.6 | 55.3 | 49.6 | 12 |
| 100 | Cartwright, Eli | GAT_GRI | Four-Seam | 207 | 46 | 0.194 | 61.5 | 88.4 | 76.4 | 31.1% | 25.0% | 8.7% | 26.1% | 35.4 | 54.2 | 53.2 | 32.5 | 13 |
| 107 | Anderson, Colt | WAS_WIL3 | Four-Seam | 258 | 92 | 0.215 | 61.0 | 87.6 | 74.7 | 14.9% | 13.7% | 12.0% | 33.7% | 53.0 | 45.0 | 43.3 | 57.3 | 14 |
| 110 | Mercado, Nelson | OTT_TIT | Four-Seam | 81 | 27 | 0.169 | 60.8 | 87.2 | 76.2 | 17.9% | 5.9% | 11.1% | 25.9% | 34.6 | 38.6 | 51.8 | 32.6 | 15 |
| 112 | Shears, Tanner | SCH_BOO | Four-Seam | 219 | 39 | 0.190 | 60.6 | 87.0 | 75.6 | 35.7% | 29.5% | 7.7% | 33.3% | 40.0 | 58.0 | 49.2 | 40.0 | 16 |
| 118 | Zaffiro, Cole | SCH_BOO | Four-Seam | 289 | 78 | 0.195 | 60.1 | 86.3 | 76.2 | 28.8% | 25.7% | 6.4% | 33.3% | 40.0 | 54.8 | 59.2 | 33.7 | 17 |
| 120 | Wehrle, Tyler | WIN_CIT29 | Four-Seam | 236 | 50 | 0.189 | 59.8 | 86.0 | 76.4 | 33.0% | 30.6% | 10.0% | 30.0% | 34.1 | 58.8 | 49.8 | 33.4 | 18 |
| 127 | Kaminer, Brandon | DOW_EAS1 | Four-Seam | 185 | 57 | 0.227 | 59.5 | 85.2 | 76.5 | 12.7% | 14.5% | 8.8% | 31.6% | 46.0 | 45.7 | 46.1 | 48.2 | 19 |
| 129 | Ortiz, Julio | GAT_GRI | Four-Seam | 330 | 78 | 0.199 | 59.4 | 85.0 | 77.5 | 33.1% | 27.4% | 6.4% | 28.2% | 39.1 | 56.2 | 52.5 | 36.9 | 20 |
| 130 | Dima, Josh | GAT_GRI | Four-Seam | 238 | 57 | 0.205 | 59.3 | 84.9 | 76.7 | 31.9% | 31.4% | 8.8% | 29.8% | 44.6 | 59.4 | 48.4 | 45.3 | 21 |
| 137 | Langhorne, Miles | SUS_COU1 | Four-Seam | 70 | 21 | 0.246 | 59.1 | 84.1 | 76.0 | 10.0% | 6.7% | 9.5% | 33.3% | 53.3 | 39.2 | 32.4 | 64.5 | 22 |
| 141 | MacMillan, Blake | TRO_AIG | Four-Seam | 148 | 48 | 0.201 | 59.0 | 83.6 | 76.6 | 36.7% | 39.4% | 12.5% | 29.2% | 34.7 | 66.0 | 46.0 | 36.4 | 23 |
| 148 | Foster, Kobe | WAS_WIL3 | Four-Seam | 442 | 159 | 0.194 | 58.7 | 82.8 | 76.9 | 23.7% | 22.7% | 11.3% | 28.9% | 27.1 | 52.4 | 47.2 | 27.5 | 24 |
| 149 | Garcia, Brett | OTT_TIT | Four-Seam | 258 | 77 | 0.203 | 58.7 | 82.6 | 76.8 | 35.9% | 33.8% | 7.8% | 33.8% | 41.3 | 61.5 | 52.2 | 39.4 | 25 |

### Sinkers

| Rank | Pitcher | Team | Pitch Type | Pitches | BBE | xwOBA | PVS 20-80 | PVS 0-100 | EV | Whiff% | K% | HardHit% | SweetSpot% | GB Score | K Score | LD Supp | FB Supp | Pitch Type Rank |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 31 | Riedel, Caleb | SCH_BOO | Sinker | 77 | 22 | 0.141 | 70.0 | 96.5 | 72.5 | 25.0% | 27.8% | 9.1% | 22.7% | 44.8 | 56.5 | 58.2 | 39.4 | 1 |
| 33 | Still, Stephen | TRI_VAL | Sinker | 61 | 18 | 0.212 | 69.5 | 96.2 | 74.7 | 25.8% | 36.4% | 11.1% | 16.7% | 41.7 | 63.5 | 68.7 | 29.6 | 2 |
| 37 | Glickstein, Aaron | SCH_BOO | Sinker | 101 | 34 | 0.180 | 68.3 | 95.8 | 73.4 | 16.3% | 7.7% | 5.9% | 23.5% | 47.5 | 40.1 | 56.8 | 43.2 | 3 |
| 62 | Colon, Jeffrey | TRO_AIG | Sinker | 56 | 17 | 0.170 | 64.9 | 92.8 | 73.9 | 18.5% | 13.3% | 23.5% | 17.6% | 52.0 | 44.7 | 68.3 | 40.8 | 4 |
| 76 | Widener, Jacob | SUS_COU1 | Sinker | 139 | 42 | 0.189 | 63.7 | 91.2 | 73.7 | 30.9% | 9.4% | 11.9% | 28.6% | 53.3 | 41.4 | 48.0 | 54.8 | 5 |
| 83 | Mannering, Shawn | DOW_EAS1 | Sinker | 59 | 15 | 0.258 | 63.3 | 90.4 | 74.8 | 22.2% | 6.7% | 13.3% | 26.7% | 35.7 | 39.2 | 49.8 | 35.0 | 6 |
| 87 | Garcia, Andrew | EVA_OTT | Sinker | 52 | 12 | 0.239 | 62.9 | 89.9 | 75.8 | 13.6% | 0.0% | 16.7% | 16.7% | 78.2 | 33.8 | 76.0 | 63.5 | 7 |
| 113 | Petschke, Ben | EVA_OTT | Sinker | 54 | 13 | 0.206 | 60.6 | 86.9 | 75.6 | 8.0% | 8.3% | 23.1% | 23.1% | 55.9 | 40.6 | 55.9 | 52.6 | 8 |
| 116 | Lovell, Justin | WIN_CIT29 | Sinker | 129 | 36 | 0.175 | 60.5 | 86.5 | 74.6 | 24.1% | 6.9% | 13.9% | 33.3% | 48.1 | 39.4 | 43.3 | 52.2 | 9 |
| 121 | Hungate, Chase | NEW_JER6 | Sinker | 66 | 24 | 0.202 | 59.7 | 85.9 | 75.0 | 21.6% | 35.7% | 16.7% | 33.3% | 58.9 | 63.0 | 54.2 | 56.7 | 10 |
| 124 | Harley, Tristan | SUS_COU1 | Sinker | 97 | 36 | 0.188 | 59.6 | 85.6 | 76.3 | 10.9% | 4.3% | 13.9% | 25.0% | 46.0 | 37.3 | 61.5 | 38.6 | 11 |
| 125 | Sabatine, Gino | TRI_VAL | Sinker | 54 | 19 | 0.194 | 59.6 | 85.5 | 76.2 | 13.0% | 7.1% | 10.5% | 31.6% | 48.7 | 39.6 | 55.3 | 45.3 | 12 |
| 145 | Cerda, Junior | EVA_OTT | Sinker | 114 | 42 | 0.211 | 58.9 | 83.1 | 75.7 | 9.6% | 12.5% | 0.0% | 42.9% | 47.8 | 44.0 | 38.6 | 54.8 | 13 |
| 164 | Morgan, Marcus | JOL_SLA | Sinker | 96 | 23 | 0.227 | 58.1 | 80.9 | 77.7 | 27.8% | 34.8% | 13.0% | 26.1% | 53.8 | 62.2 | 53.2 | 52.0 | 14 |
| 185 | Grounds, Jackson | DOW_EAS1 | Sinker | 116 | 26 | 0.215 | 57.2 | 78.4 | 76.8 | 22.9% | 7.7% | 11.5% | 30.8% | 47.0 | 40.1 | 35.7 | 55.7 | 15 |
| 195 | Turner, Eric | JOL_SLA | Sinker | 91 | 34 | 0.213 | 56.8 | 77.3 | 76.4 | 17.4% | 9.7% | 17.6% | 29.4% | 45.2 | 41.7 | 45.2 | 47.9 | 16 |
| 196 | McCartney, Seth | MIS_MUD | Sinker | 120 | 39 | 0.238 | 56.7 | 77.1 | 78.3 | 8.3% | 5.3% | 20.5% | 17.9% | 61.8 | 38.1 | 55.9 | 58.8 | 17 |
| 197 | Henderson, Drew | DOW_EAS1 | Sinker | 115 | 29 | 0.213 | 56.7 | 77.0 | 76.9 | 13.3% | 19.2% | 13.8% | 31.0% | 52.2 | 49.5 | 62.5 | 44.6 | 18 |
| 199 | Lawson, Nathan | FLO_Y'A | Sinker | 186 | 64 | 0.211 | 56.7 | 76.8 | 78.0 | 11.8% | 8.7% | 9.4% | 29.7% | 51.6 | 40.9 | 53.5 | 49.5 | 19 |
| 215 | Long, Maddox | WAS_WIL3 | Sinker | 285 | 84 | 0.234 | 56.0 | 74.9 | 78.6 | 15.4% | 17.8% | 15.5% | 23.8% | 64.4 | 48.3 | 57.3 | 60.6 | 20 |
| 222 | Fritz, AJ | MIS_MUD | Sinker | 55 | 21 | 0.239 | 55.6 | 74.1 | 78.5 | 28.1% | 16.7% | 9.5% | 33.3% | 49.7 | 47.4 | 44.8 | 52.9 | 21 |
| 237 | Odonnell, Brendan | NEW_ENG23 | Sinker | 91 | 14 | 0.238 | 55.0 | 72.3 | 81.7 | 29.0% | 7.7% | 7.1% | 14.3% | 80.0 | 40.1 | 66.7 | 78.1 | 22 |
| 247 | Plumadore, Carson | WIN_CIT29 | Sinker | 127 | 38 | 0.199 | 54.8 | 71.2 | 76.8 | 17.9% | 40.7% | 10.5% | 42.1% | 30.4 | 67.1 | 34.7 | 38.9 | 23 |
| 254 | Kelly, Colin | SUS_COU1 | Sinker | 96 | 29 | 0.189 | 54.5 | 70.3 | 77.5 | 25.0% | 11.1% | 17.2% | 31.0% | 52.2 | 42.9 | 53.4 | 50.2 | 24 |
| 261 | Aldeano, Austin | TRO_AIG | Sinker | 70 | 24 | 0.218 | 54.3 | 69.5 | 77.2 | 22.2% | 18.8% | 16.7% | 33.3% | 36.3 | 49.1 | 43.3 | 39.8 | 25 |

### Sliders

| Rank | Pitcher | Team | Pitch Type | Pitches | BBE | xwOBA | PVS 20-80 | PVS 0-100 | EV | Whiff% | K% | HardHit% | SweetSpot% | GB Score | K Score | LD Supp | FB Supp | Pitch Type Rank |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 2 | Carroll, Jake | JOL_SLA | Slider | 68 | 12 | 0.190 | 80.0 | 99.9 | 68.3 | 26.9% | 28.6% | 0.0% | 16.7% | 52.4 | 57.2 | 54.2 | 49.9 | 1 |
| 4 | Ryan, Dillon | NEW_ENG23 | Slider | 125 | 25 | 0.144 | 79.9 | 99.6 | 69.9 | 35.3% | 34.5% | 0.0% | 20.0% | 60.4 | 62.0 | 60.3 | 54.6 | 2 |
| 5 | Leduc, Zachary | TRO_AIG | Slider | 78 | 14 | 0.092 | 79.2 | 99.5 | 68.7 | 46.7% | 38.9% | 7.1% | 21.4% | 58.9 | 65.6 | 57.3 | 54.8 | 3 |
| 8 | Vecerka, Boris | QUE_CAP | Slider | 74 | 14 | 0.129 | 77.6 | 99.2 | 71.2 | 31.8% | 41.2% | 7.1% | 14.3% | 53.3 | 67.5 | 57.3 | 49.0 | 4 |
| 10 | Alpern, Liam | FLO_Y'A | Slider | 78 | 16 | 0.113 | 76.4 | 98.9 | 69.9 | 14.3% | 35.7% | 12.5% | 18.8% | 54.0 | 63.0 | 67.8 | 43.2 | 5 |
| 12 | Jones, Logan | TRI_VAL | Slider | 65 | 17 | 0.191 | 74.7 | 98.7 | 68.2 | 23.1% | 25.0% | 11.8% | 35.3% | 52.0 | 54.2 | 45.2 | 55.1 | 6 |
| 17 | Bargo, Casey | NEW_ENG23 | Slider | 56 | 16 | 0.176 | 73.6 | 98.1 | 74.6 | 28.0% | 40.0% | 0.0% | 12.5% | 68.5 | 66.5 | 59.6 | 63.5 | 7 |
| 18 | Hickey, Matt | GAT_GRI | Slider | 86 | 25 | 0.191 | 73.5 | 98.0 | 71.4 | 24.3% | 13.0% | 12.0% | 16.0% | 66.6 | 44.4 | 65.5 | 57.8 | 8 |
| 20 | Harper, Scott | NEW_YOR13 | Slider | 212 | 33 | 0.155 | 72.6 | 97.8 | 72.9 | 50.0% | 45.3% | 6.1% | 18.2% | 39.0 | 70.8 | 64.1 | 29.6 | 9 |
| 23 | Kirby, Zach | WAS_WIL3 | Slider | 127 | 42 | 0.156 | 71.7 | 97.4 | 73.3 | 21.1% | 13.8% | 2.4% | 21.4% | 40.5 | 45.1 | 57.3 | 35.4 | 10 |
| 25 | Moore, Kyle | SCH_BOO | Slider | 53 | 20 | 0.177 | 71.2 | 97.2 | 73.5 | 20.7% | 12.5% | 10.0% | 15.0% | 35.7 | 44.0 | 56.4 | 30.9 | 11 |
| 28 | Nakata, Yuto | QUE_CAP | Slider | 97 | 22 | 0.155 | 70.5 | 96.8 | 74.2 | 35.9% | 32.0% | 0.0% | 22.7% | 55.3 | 60.0 | 58.2 | 50.6 | 12 |
| 29 | McEvoy, Aidan | FLO_Y'A | Slider | 107 | 27 | 0.157 | 70.5 | 96.7 | 74.1 | 39.6% | 32.4% | 7.4% | 18.5% | 40.3 | 60.3 | 56.6 | 35.6 | 13 |
| 30 | Donnan, Blake | FLO_Y'A | Slider | 65 | 10 | 0.186 | 70.1 | 96.6 | 71.5 | 51.7% | 52.9% | 10.0% | 30.0% | 43.4 | 77.1 | 49.8 | 43.2 | 14 |
| 36 | Jones, Logan | FLO_Y'A | Slider | 51 | 10 | 0.179 | 68.5 | 95.9 | 75.7 | 46.4% | 30.8% | 0.0% | 20.0% | 51.1 | 59.0 | 49.8 | 51.3 | 15 |
| 45 | Vega, Lucas | TRO_AIG | Slider | 134 | 36 | 0.156 | 66.7 | 94.8 | 75.6 | 26.8% | 28.6% | 5.6% | 19.4% | 39.6 | 57.2 | 54.2 | 36.4 | 16 |
| 48 | Balzan, Jackson | SUS_COU1 | Slider | 91 | 26 | 0.187 | 66.5 | 94.5 | 74.8 | 34.1% | 28.6% | 7.7% | 23.1% | 52.9 | 57.2 | 60.9 | 46.3 | 17 |
| 53 | Morin, Jacob | QUE_CAP | Slider | 85 | 20 | 0.207 | 65.8 | 93.9 | 73.4 | 30.6% | 30.4% | 10.0% | 30.0% | 47.3 | 58.7 | 56.4 | 43.2 | 18 |
| 66 | Petschke, Ben | EVA_OTT | Slider | 144 | 42 | 0.186 | 64.6 | 92.4 | 75.2 | 18.5% | 25.7% | 9.5% | 23.8% | 57.0 | 54.8 | 54.2 | 54.8 | 19 |
| 70 | Perozzi, John | SUS_COU1 | Slider | 126 | 30 | 0.179 | 64.1 | 91.9 | 74.4 | 44.4% | 41.2% | 13.3% | 26.7% | 43.4 | 67.5 | 49.8 | 43.2 | 20 |
| 72 | MacMillan, Blake | TRO_AIG | Slider | 106 | 13 | 0.211 | 64.1 | 91.7 | 73.9 | 56.1% | 63.6% | 23.1% | 23.1% | 61.8 | 80.0 | 45.8 | 65.1 | 21 |
| 77 | Foster, Kobe | WAS_WIL3 | Slider | 144 | 37 | 0.184 | 63.6 | 91.1 | 74.3 | 32.2% | 29.7% | 13.5% | 27.0% | 43.2 | 58.1 | 54.8 | 39.8 | 22 |
| 79 | Barraza, Chris | MIS_MUD | Slider | 57 | 21 | 0.194 | 63.4 | 90.9 | 75.1 | 21.9% | 43.8% | 4.8% | 33.3% | 53.3 | 69.6 | 51.1 | 52.9 | 23 |
| 85 | Plumadore, Carson | WIN_CIT29 | Slider | 115 | 32 | 0.174 | 62.9 | 90.2 | 76.6 | 28.6% | 25.0% | 3.1% | 25.0% | 34.7 | 54.2 | 59.6 | 27.9 | 24 |
| 86 | Vail, Tyler | NEW_YOR13 | Slider | 197 | 31 | 0.237 | 62.9 | 90.0 | 75.2 | 35.2% | 30.4% | 6.5% | 32.3% | 52.6 | 58.7 | 42.2 | 57.6 | 25 |

### Curveballs

| Rank | Pitcher | Team | Pitch Type | Pitches | BBE | xwOBA | PVS 20-80 | PVS 0-100 | EV | Whiff% | K% | HardHit% | SweetSpot% | GB Score | K Score | LD Supp | FB Supp | Pitch Type Rank |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | Grounds, Jackson | DOW_EAS1 | Curveball | 82 | 10 | 0.108 | 80.0 | 100.0 | 64.6 | 42.1% | 41.2% | 0.0% | 0.0% | 58.9 | 67.5 | 76.0 | 43.2 | 1 |
| 3 | Morgan, Cooper | QUE_CAP | Curveball | 72 | 22 | 0.146 | 80.0 | 99.8 | 64.0 | 40.0% | 44.4% | 9.1% | 45.5% | 41.3 | 70.2 | 52.2 | 39.4 | 2 |
| 22 | Bohnert, Matthew | WIN_CIT29 | Curveball | 97 | 12 | 0.143 | 71.9 | 97.5 | 75.1 | 46.2% | 47.4% | 8.3% | 8.3% | 65.3 | 72.5 | 76.0 | 49.9 | 3 |
| 34 | Townes, Holland | SCH_BOO | Curveball | 82 | 11 | 0.189 | 68.7 | 96.1 | 73.2 | 51.9% | 60.0% | 18.2% | 18.2% | 62.4 | 80.0 | 52.2 | 61.7 | 4 |
| 38 | Jones, Breyln | NEW_JER6 | Curveball | 54 | 12 | 0.186 | 68.0 | 95.7 | 76.4 | 22.7% | 26.7% | 0.0% | 16.7% | 58.9 | 55.6 | 76.0 | 43.2 | 5 |
| 43 | Garcia, Brett | OTT_TIT | Curveball | 115 | 20 | 0.175 | 67.4 | 95.1 | 76.6 | 34.1% | 50.0% | 10.0% | 10.0% | 62.7 | 74.7 | 69.5 | 51.3 | 6 |
| 46 | Gregory, Ben | GAT_GRI | Curveball | 53 | 14 | 0.227 | 66.7 | 94.7 | 72.6 | 25.0% | 22.2% | 14.3% | 28.6% | 75.4 | 52.0 | 48.0 | 78.1 | 7 |
| 49 | Salata, Derek | SCH_BOO | Curveball | 122 | 25 | 0.196 | 66.5 | 94.4 | 73.9 | 37.3% | 43.8% | 8.0% | 28.0% | 54.2 | 69.6 | 49.8 | 54.6 | 8 |
| 50 | Binns, Malik | NEW_JER6 | Curveball | 55 | 13 | 0.185 | 66.3 | 94.3 | 73.8 | 27.3% | 13.3% | 7.7% | 30.8% | 61.8 | 44.7 | 55.9 | 58.8 | 9 |
| 51 | Heredia-Bustos, Rolando | DOW_EAS1 | Curveball | 75 | 18 | 0.177 | 66.3 | 94.1 | 73.1 | 33.3% | 23.1% | 16.7% | 22.2% | 46.0 | 52.7 | 46.9 | 47.7 | 10 |
| 52 | Hill, Kaleb | OTT_TIT | Curveball | 222 | 51 | 0.198 | 66.1 | 94.0 | 73.7 | 27.8% | 17.5% | 9.8% | 25.5% | 64.2 | 48.1 | 52.9 | 63.1 | 11 |
| 58 | Hickey, Matt | GAT_GRI | Curveball | 62 | 13 | 0.190 | 65.5 | 93.3 | 76.5 | 26.1% | 30.8% | 7.7% | 15.4% | 67.8 | 59.0 | 55.9 | 65.1 | 12 |
| 60 | Hohenstein, Liam | WIN_CIT29 | Curveball | 103 | 19 | 0.168 | 65.2 | 93.1 | 73.5 | 29.0% | 11.1% | 0.0% | 36.8% | 40.6 | 42.9 | 48.4 | 41.0 | 13 |
| 63 | Eisenbarger, Jack | QUE_CAP | Curveball | 93 | 13 | 0.212 | 64.8 | 92.7 | 72.2 | 28.6% | 33.3% | 15.4% | 38.5% | 49.9 | 61.1 | 45.8 | 52.6 | 14 |
| 75 | Cook, Cole | SCH_BOO | Curveball | 114 | 22 | 0.197 | 63.8 | 91.3 | 75.1 | 40.0% | 44.8% | 18.2% | 22.7% | 58.9 | 70.5 | 58.2 | 54.3 | 15 |
| 78 | Boies, Emiles | QUE_CAP | Curveball | 80 | 20 | 0.172 | 63.5 | 91.0 | 74.8 | 29.0% | 14.3% | 20.0% | 20.0% | 62.7 | 45.5 | 56.4 | 59.5 | 16 |
| 84 | Majick, Eli | NEW_ENG23 | Curveball | 52 | 14 | 0.186 | 63.1 | 90.3 | 76.6 | 14.3% | 23.1% | 0.0% | 28.6% | 53.3 | 52.7 | 48.0 | 54.8 | 17 |
| 95 | Harris, Ben | GAT_GRI | Curveball | 242 | 22 | 0.234 | 61.8 | 89.0 | 76.7 | 36.2% | 55.0% | 13.6% | 22.7% | 58.9 | 78.8 | 46.3 | 61.7 | 18 |
| 98 | Wiltse, Ryan | EVA_OTT | Curveball | 131 | 17 | 0.217 | 61.6 | 88.6 | 78.0 | 35.5% | 33.3% | 17.6% | 11.8% | 74.8 | 61.1 | 60.6 | 69.5 | 19 |
| 101 | Scafidi, Christian | LAK_ERI24 | Curveball | 59 | 12 | 0.194 | 61.3 | 88.3 | 75.7 | 22.2% | 46.2% | 8.3% | 33.3% | 71.7 | 71.6 | 43.3 | 77.1 | 20 |
| 102 | Hampton, Ky | OTT_TIT | Curveball | 52 | 15 | 0.177 | 61.3 | 88.2 | 73.2 | 15.0% | 28.6% | 13.3% | 40.0% | 56.3 | 57.2 | 41.1 | 62.2 | 21 |
| 105 | Maryniak, Connor | NEW_JER6 | Curveball | 180 | 46 | 0.214 | 61.1 | 87.8 | 78.2 | 36.1% | 38.9% | 8.7% | 17.4% | 77.3 | 65.6 | 61.8 | 71.5 | 22 |
| 135 | Sechrist, Zander | WAS_WIL3 | Curveball | 92 | 28 | 0.205 | 59.1 | 84.3 | 74.4 | 15.0% | 12.5% | 14.3% | 35.7% | 34.0 | 44.0 | 38.6 | 40.2 | 23 |
| 147 | Lefebvre, Charles | TRO_AIG | Curveball | 99 | 24 | 0.247 | 58.7 | 82.9 | 76.7 | 32.5% | 42.3% | 4.2% | 37.5% | 52.4 | 68.4 | 48.7 | 53.3 | 24 |
| 154 | Vail, Tyler | NEW_YOR13 | Curveball | 183 | 22 | 0.215 | 58.5 | 82.1 | 80.0 | 36.0% | 28.6% | 4.5% | 22.7% | 69.4 | 57.2 | 52.2 | 69.1 | 25 |

### Changeups

| Rank | Pitcher | Team | Pitch Type | Pitches | BBE | xwOBA | PVS 20-80 | PVS 0-100 | EV | Whiff% | K% | HardHit% | SweetSpot% | GB Score | K Score | LD Supp | FB Supp | Pitch Type Rank |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 6 | Zentko, Dylan | EVA_OTT | Changeup | 67 | 13 | 0.155 | 78.6 | 99.4 | 70.2 | 44.8% | 35.7% | 7.7% | 15.4% | 67.8 | 63.0 | 55.9 | 65.1 | 1 |
| 7 | Lawson, Nathan | FLO_Y'A | Changeup | 60 | 17 | 0.166 | 78.2 | 99.3 | 72.9 | 27.6% | 37.5% | 5.9% | 5.9% | 52.0 | 64.5 | 76.0 | 36.0 | 2 |
| 9 | Peyton, Blake | GAT_GRI | Changeup | 93 | 20 | 0.141 | 77.3 | 99.1 | 70.1 | 37.5% | 15.4% | 5.0% | 20.0% | 70.4 | 46.4 | 56.4 | 67.6 | 3 |
| 11 | Serrano, Elio | NEW_JER6 | Changeup | 63 | 15 | 0.148 | 75.9 | 98.8 | 70.0 | 35.1% | 21.4% | 6.7% | 26.7% | 51.1 | 51.3 | 58.6 | 45.9 | 4 |
| 19 | Escobar, Anthony | TRO_AIG | Changeup | 147 | 38 | 0.156 | 72.7 | 97.9 | 73.0 | 40.3% | 25.6% | 10.5% | 13.2% | 52.8 | 54.8 | 62.2 | 45.3 | 5 |
| 27 | Rodriguez, Joe Joe | NEW_JER6 | Changeup | 125 | 19 | 0.155 | 70.6 | 97.0 | 76.3 | 53.3% | 34.6% | 0.0% | 10.5% | 56.8 | 62.1 | 69.1 | 45.3 | 6 |
| 32 | Harris, Everette | TRI_VAL | Changeup | 96 | 27 | 0.168 | 69.7 | 96.4 | 74.3 | 15.9% | 7.1% | 7.4% | 14.8% | 66.0 | 39.6 | 56.6 | 62.8 | 7 |
| 35 | Parsons, Billy | SUS_COU1 | Changeup | 61 | 17 | 0.234 | 68.5 | 96.0 | 74.2 | 28.1% | 41.2% | 5.9% | 23.5% | 80.0 | 67.5 | 68.3 | 74.3 | 8 |
| 42 | Smith, Ben | NEW_ENG23 | Changeup | 56 | 15 | 0.152 | 67.6 | 95.2 | 77.2 | 20.8% | 7.1% | 6.7% | 6.7% | 61.4 | 39.6 | 76.0 | 45.9 | 9 |
| 47 | Messina, Chris | FDU_KNI | Changeup | 68 | 16 | 0.254 | 66.5 | 94.6 | 75.3 | 16.7% | 5.9% | 6.2% | 18.8% | 68.5 | 38.6 | 67.8 | 58.4 | 10 |
| 55 | Wiltse, Ryan | EVA_OTT | Changeup | 150 | 45 | 0.203 | 65.8 | 93.7 | 74.4 | 34.9% | 28.3% | 6.7% | 28.9% | 59.7 | 56.9 | 49.8 | 60.4 | 11 |
| 56 | Morgan, Cooper | QUE_CAP | Changeup | 74 | 20 | 0.190 | 65.6 | 93.6 | 73.2 | 32.4% | 29.4% | 5.0% | 35.0% | 39.6 | 57.8 | 49.8 | 39.1 | 12 |
| 64 | Drakeford, Dosie | NEW_JER6 | Changeup | 84 | 15 | 0.159 | 64.7 | 92.6 | 73.9 | 56.8% | 54.2% | 0.0% | 40.0% | 46.0 | 78.1 | 32.4 | 56.7 | 13 |
| 68 | Tokar, Heitor | OTT_TIT | Changeup | 70 | 25 | 0.198 | 64.6 | 92.1 | 74.9 | 17.6% | 10.0% | 12.0% | 24.0% | 54.2 | 41.9 | 60.3 | 48.0 | 14 |
| 69 | Sesar, Jorden | SUS_COU1 | Changeup | 75 | 22 | 0.181 | 64.3 | 92.0 | 75.5 | 28.2% | 27.8% | 9.1% | 27.3% | 48.3 | 56.5 | 46.3 | 50.6 | 15 |
| 73 | Leak, Anthony | NEW_YOR13 | Changeup | 75 | 17 | 0.199 | 64.0 | 91.6 | 77.7 | 26.7% | 6.2% | 0.0% | 17.6% | 61.1 | 38.9 | 68.3 | 50.3 | 16 |
| 81 | Maietta, Dante | WIN_CIT29 | Changeup | 259 | 52 | 0.186 | 63.3 | 90.6 | 77.3 | 41.6% | 32.8% | 3.8% | 21.2% | 49.9 | 60.6 | 58.4 | 44.7 | 17 |
| 82 | Miner, Jace | DOW_EAS1 | Changeup | 156 | 36 | 0.219 | 63.3 | 90.5 | 74.6 | 28.8% | 17.6% | 11.1% | 27.8% | 52.4 | 48.2 | 54.2 | 49.9 | 18 |
| 103 | Willeman, Landon | EVA_OTT | Changeup | 179 | 57 | 0.202 | 61.2 | 88.0 | 76.5 | 25.0% | 16.7% | 14.0% | 22.8% | 60.9 | 47.4 | 57.6 | 56.7 | 19 |
| 108 | Campbell, Tyler | MIS_MUD | Changeup | 97 | 30 | 0.220 | 60.9 | 87.5 | 77.4 | 28.9% | 20.0% | 6.7% | 23.3% | 38.3 | 50.1 | 58.6 | 32.3 | 20 |
| 114 | Hensey, Rob | SUS_COU1 | Changeup | 277 | 63 | 0.212 | 60.5 | 86.8 | 77.4 | 44.2% | 41.0% | 12.7% | 20.6% | 71.7 | 67.3 | 57.3 | 68.4 | 21 |
| 115 | Plumadore, Carson | WIN_CIT29 | Changeup | 269 | 76 | 0.196 | 60.5 | 86.6 | 75.8 | 28.7% | 19.0% | 9.2% | 30.3% | 44.6 | 49.4 | 60.5 | 37.8 | 22 |
| 128 | Hocom, Quinn | TRI_VAL | Changeup | 101 | 22 | 0.221 | 59.4 | 85.1 | 76.5 | 28.9% | 19.2% | 22.7% | 22.7% | 65.9 | 49.5 | 52.2 | 65.4 | 23 |
| 133 | Gartland, Chad | TRI_VAL | Changeup | 52 | 23 | 0.206 | 59.2 | 84.5 | 76.5 | 13.8% | 5.3% | 8.7% | 30.4% | 53.8 | 38.1 | 53.2 | 52.0 | 24 |
| 134 | VanMarter, Luke | LEM_COL | Changeup | 53 | 17 | 0.256 | 59.2 | 84.4 | 75.7 | 9.5% | 0.0% | 11.8% | 35.3% | 43.0 | 33.8 | 52.9 | 40.8 | 25 |

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