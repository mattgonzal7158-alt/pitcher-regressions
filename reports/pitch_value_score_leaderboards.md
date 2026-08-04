# Frontier League Pitch Value Score

- Input file: `data\processed\pitcher_pitch_type_xwoba_metrics.csv`
- Output file: `data\processed\pitch_value_scores.csv`
- Qualified pitcher-pitch types scored: 1,002
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
| 1 | Grounds, Jackson | DOW_EAS1 | Curveball | 82 | 10 | 0.109 | 80.0 | 100.0 | 64.6 | 42.1% | 41.2% | 0.0% | 0.0% | 59.5 | 67.0 | 75.9 | 43.4 | 1 |
| 2 | Morrissey, Joe | EVA_OTT | Cutter | 62 | 18 | 0.113 | 80.0 | 99.9 | 68.3 | 33.3% | 40.0% | 0.0% | 16.7% | 41.9 | 66.1 | 61.6 | 34.3 | 1 |
| 3 | Vecerka, Boris | QUE_CAP | Slider | 83 | 18 | 0.123 | 80.0 | 99.8 | 69.1 | 25.9% | 38.9% | 5.6% | 16.7% | 59.5 | 65.2 | 54.4 | 57.0 | 1 |
| 4 | Carroll, Jake | JOL_SLA | Slider | 74 | 15 | 0.178 | 80.0 | 99.7 | 69.4 | 24.1% | 23.5% | 0.0% | 20.0% | 62.1 | 52.9 | 58.7 | 57.0 | 2 |
| 5 | Flontek, Zac | DOW_EAS1 | Slider | 76 | 12 | 0.089 | 80.0 | 99.6 | 70.5 | 40.9% | 45.5% | 8.3% | 8.3% | 52.9 | 70.4 | 65.1 | 43.4 | 3 |
| 6 | Ryan, Dillon | NEW_ENG23 | Slider | 149 | 29 | 0.145 | 79.6 | 99.5 | 70.4 | 38.7% | 35.3% | 0.0% | 17.2% | 60.9 | 62.3 | 62.5 | 53.3 | 4 |
| 7 | Morgan, Cooper | QUE_CAP | Curveball | 99 | 30 | 0.148 | 78.8 | 99.4 | 65.7 | 33.3% | 40.0% | 6.7% | 40.0% | 43.7 | 66.1 | 54.4 | 40.6 | 2 |
| 8 | Harley, Tristan | SUS_COU1 | Slider | 74 | 16 | 0.112 | 77.0 | 99.3 | 69.0 | 35.5% | 31.2% | 6.2% | 25.0% | 54.6 | 59.1 | 51.7 | 53.6 | 5 |
| 9 | Sanders, Brayden | MIS_MUD | Slider | 66 | 11 | 0.160 | 76.6 | 99.2 | 70.6 | 45.8% | 46.7% | 9.1% | 18.2% | 63.1 | 71.4 | 75.9 | 47.1 | 6 |
| 10 | Bauer, Patrick | QUE_CAP | Slider | 71 | 14 | 0.151 | 76.5 | 99.1 | 72.4 | 22.7% | 20.0% | 7.1% | 7.1% | 36.9 | 50.1 | 66.7 | 25.8 | 7 |
| 11 | Alpern, Liam | FLO_Y'A | Slider | 78 | 16 | 0.113 | 76.1 | 99.0 | 69.9 | 14.3% | 35.7% | 12.5% | 18.8% | 54.6 | 62.7 | 67.8 | 43.4 | 8 |
| 12 | Sparks, Alec | GAT_GRI | Curveball | 89 | 12 | 0.160 | 76.0 | 98.9 | 70.8 | 39.3% | 41.2% | 0.0% | 25.0% | 52.9 | 67.0 | 54.4 | 50.2 | 3 |
| 13 | Heintz, Danny | FLO_Y'A | Four-Seam | 60 | 12 | 0.092 | 75.8 | 98.8 | 72.5 | 55.6% | 46.7% | 0.0% | 16.7% | 46.3 | 71.4 | 75.9 | 29.7 | 1 |
| 14 | Kramer, Cameron | TRO_AIG | Slider | 63 | 10 | 0.176 | 75.7 | 98.7 | 69.1 | 53.6% | 42.9% | 10.0% | 30.0% | 59.5 | 68.4 | 50.1 | 59.8 | 9 |
| 15 | Scafidi, Christian | LAK_ERI24 | Cutter | 52 | 14 | 0.147 | 74.4 | 98.6 | 72.3 | 10.5% | 14.3% | 0.0% | 21.4% | 59.5 | 45.5 | 57.5 | 55.1 | 2 |
| 16 | Davis, Tyler | WIN_CIT29 | Four-Seam | 76 | 19 | 0.111 | 74.4 | 98.5 | 75.6 | 23.1% | 19.0% | 5.3% | 0.0% | 44.9 | 49.3 | 75.9 | 28.3 | 2 |
| 17 | Jones, Logan | TRI_VAL | Slider | 65 | 17 | 0.190 | 74.3 | 98.4 | 68.2 | 23.1% | 25.0% | 11.8% | 35.3% | 52.5 | 54.1 | 45.6 | 55.4 | 10 |
| 18 | Grounds, Jackson | DOW_EAS1 | Four-Seam | 107 | 27 | 0.159 | 74.1 | 98.3 | 69.9 | 25.5% | 21.7% | 11.1% | 25.9% | 37.5 | 51.5 | 52.0 | 35.8 | 3 |
| 19 | Bargo, Casey | NEW_ENG23 | Slider | 56 | 16 | 0.176 | 73.6 | 98.2 | 74.6 | 28.0% | 40.0% | 0.0% | 12.5% | 69.4 | 66.1 | 59.8 | 63.9 | 11 |
| 20 | Debban, Caleb | NEW_JER6 | Four-Seam | 57 | 13 | 0.176 | 73.5 | 98.1 | 70.6 | 20.0% | 6.2% | 7.7% | 23.1% | 50.4 | 39.1 | 66.0 | 40.2 | 4 |
| 21 | Garcia, Hector | WAS_WIL3 | Splitter | 62 | 13 | 0.184 | 73.4 | 98.0 | 71.1 | 45.7% | 40.0% | 7.7% | 23.1% | 56.5 | 66.1 | 56.1 | 52.8 | 1 |
| 22 | Earwood, Micah | SUS_COU1 | Four-Seam | 98 | 13 | 0.231 | 73.3 | 97.9 | 69.7 | 0.0% | 0.0% | 7.7% | 30.8% | 62.6 | 34.1 | 46.1 | 65.4 | 5 |
| 23 | Harper, Scott | NEW_YOR13 | Slider | 243 | 40 | 0.153 | 72.8 | 97.8 | 71.5 | 47.7% | 44.1% | 5.0% | 25.0% | 39.7 | 69.3 | 59.8 | 33.1 | 12 |
| 24 | Barreto, Brayhans | TRI_VAL | Cutter | 51 | 16 | 0.163 | 72.4 | 97.7 | 70.8 | 17.9% | 0.0% | 6.2% | 25.0% | 59.5 | 34.1 | 51.7 | 58.7 | 3 |
| 25 | McEvoy, Aidan | FLO_Y'A | Slider | 135 | 33 | 0.159 | 71.9 | 97.6 | 73.0 | 43.5% | 38.1% | 6.1% | 21.2% | 41.5 | 64.6 | 56.4 | 37.2 | 13 |

## Leaderboards by Pitch Family

### Four-Seams

| Rank | Pitcher | Team | Pitch Type | Pitches | BBE | xwOBA | PVS 20-80 | PVS 0-100 | EV | Whiff% | K% | HardHit% | SweetSpot% | GB Score | K Score | LD Supp | FB Supp | Pitch Type Rank |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 13 | Heintz, Danny | FLO_Y'A | Four-Seam | 60 | 12 | 0.092 | 75.8 | 98.8 | 72.5 | 55.6% | 46.7% | 0.0% | 16.7% | 46.3 | 71.4 | 75.9 | 29.7 | 1 |
| 16 | Davis, Tyler | WIN_CIT29 | Four-Seam | 76 | 19 | 0.111 | 74.4 | 98.5 | 75.6 | 23.1% | 19.0% | 5.3% | 0.0% | 44.9 | 49.3 | 75.9 | 28.3 | 2 |
| 18 | Grounds, Jackson | DOW_EAS1 | Four-Seam | 107 | 27 | 0.159 | 74.1 | 98.3 | 69.9 | 25.5% | 21.7% | 11.1% | 25.9% | 37.5 | 51.5 | 52.0 | 35.8 | 3 |
| 20 | Debban, Caleb | NEW_JER6 | Four-Seam | 57 | 13 | 0.176 | 73.5 | 98.1 | 70.6 | 20.0% | 6.2% | 7.7% | 23.1% | 50.4 | 39.1 | 66.0 | 40.2 | 4 |
| 22 | Earwood, Micah | SUS_COU1 | Four-Seam | 98 | 13 | 0.231 | 73.3 | 97.9 | 69.7 | 0.0% | 0.0% | 7.7% | 30.8% | 62.6 | 34.1 | 46.1 | 65.4 | 5 |
| 41 | Cameron, Zach | WIN_CIT29 | Four-Seam | 144 | 54 | 0.198 | 68.7 | 96.0 | 74.3 | 17.6% | 25.0% | 13.0% | 14.8% | 46.3 | 54.1 | 66.3 | 35.8 | 6 |
| 43 | Campbell, Tyler | MIS_MUD | Four-Seam | 60 | 20 | 0.178 | 68.6 | 95.8 | 72.1 | 7.4% | 0.0% | 10.0% | 25.0% | 63.5 | 34.1 | 56.5 | 59.8 | 7 |
| 51 | Correa, Nelvin | QUE_CAP | Four-Seam | 108 | 34 | 0.182 | 67.7 | 95.0 | 75.3 | 11.9% | 3.3% | 5.9% | 14.7% | 47.8 | 36.8 | 68.3 | 36.1 | 8 |
| 70 | Foy, Corbin | LAK_ERI24 | Four-Seam | 96 | 19 | 0.175 | 65.5 | 93.1 | 72.9 | 18.5% | 25.0% | 5.3% | 36.8% | 40.7 | 54.1 | 48.8 | 41.2 | 9 |
| 95 | Hensey, Rob | SUS_COU1 | Four-Seam | 244 | 68 | 0.180 | 63.0 | 90.6 | 75.2 | 33.0% | 30.0% | 7.4% | 29.4% | 46.7 | 58.1 | 58.8 | 41.0 | 10 |
| 103 | Brown, Ethan | WAS_WIL3 | Four-Seam | 67 | 25 | 0.216 | 61.9 | 89.8 | 74.2 | 10.0% | 12.5% | 16.0% | 28.0% | 42.1 | 44.1 | 39.8 | 48.3 | 11 |
| 107 | Morgan, Cooper | QUE_CAP | Four-Seam | 87 | 23 | 0.196 | 61.9 | 89.4 | 75.3 | 39.1% | 45.8% | 0.0% | 39.1% | 50.9 | 70.7 | 47.9 | 52.3 | 12 |
| 117 | Lyons, Kendall | QUE_CAP | Four-Seam | 79 | 29 | 0.180 | 61.4 | 88.4 | 77.1 | 26.2% | 25.0% | 6.9% | 24.1% | 41.7 | 54.1 | 58.1 | 36.3 | 13 |
| 118 | Cartwright, Eli | GAT_GRI | Four-Seam | 207 | 46 | 0.193 | 61.4 | 88.3 | 76.4 | 31.1% | 25.0% | 8.7% | 26.1% | 35.4 | 54.1 | 53.5 | 32.7 | 14 |
| 127 | Gregory, Ben | GAT_GRI | Four-Seam | 149 | 43 | 0.201 | 60.9 | 87.4 | 75.2 | 18.3% | 10.5% | 9.3% | 32.6% | 45.7 | 42.5 | 42.9 | 50.0 | 15 |
| 132 | Mercado, Nelson | OTT_TIT | Four-Seam | 81 | 27 | 0.169 | 60.6 | 86.9 | 76.2 | 17.9% | 5.9% | 11.1% | 25.9% | 34.5 | 38.8 | 52.0 | 32.7 | 16 |
| 144 | Anderson, Colt | WAS_WIL3 | Four-Seam | 315 | 110 | 0.219 | 59.8 | 85.7 | 75.2 | 18.4% | 16.7% | 11.8% | 33.6% | 53.7 | 47.4 | 45.4 | 56.8 | 17 |
| 152 | Shears, Tanner | SCH_BOO | Four-Seam | 285 | 55 | 0.198 | 59.4 | 84.9 | 74.8 | 33.0% | 28.6% | 7.3% | 40.0% | 40.0 | 57.0 | 43.1 | 44.1 | 18 |
| 155 | Kaminer, Brandon | DOW_EAS1 | Four-Seam | 185 | 57 | 0.226 | 59.4 | 84.6 | 76.5 | 12.7% | 14.5% | 8.8% | 31.6% | 46.3 | 45.8 | 46.5 | 48.4 | 19 |
| 156 | Boies, Emiles | QUE_CAP | Four-Seam | 147 | 57 | 0.202 | 59.2 | 84.5 | 75.5 | 22.5% | 20.0% | 10.5% | 33.3% | 37.9 | 50.1 | 48.8 | 38.3 | 20 |
| 161 | Langhorne, Miles | SUS_COU1 | Four-Seam | 70 | 21 | 0.245 | 58.9 | 84.0 | 76.0 | 10.0% | 6.7% | 9.5% | 33.3% | 53.8 | 39.5 | 32.9 | 64.8 | 21 |
| 168 | MacMillan, Blake | TRO_AIG | Four-Seam | 152 | 48 | 0.200 | 58.7 | 83.3 | 76.6 | 37.5% | 39.4% | 12.5% | 29.2% | 34.7 | 65.6 | 46.4 | 36.5 | 22 |
| 177 | Ortiz, Julio | GAT_GRI | Four-Seam | 389 | 93 | 0.200 | 58.5 | 82.4 | 78.2 | 32.6% | 25.8% | 7.5% | 25.8% | 38.6 | 54.8 | 55.1 | 35.0 | 23 |
| 182 | Foster, Kobe | WAS_WIL3 | Four-Seam | 478 | 171 | 0.194 | 58.4 | 81.9 | 77.2 | 24.0% | 23.5% | 11.1% | 28.1% | 27.3 | 52.9 | 48.8 | 27.3 | 24 |
| 183 | Kelly, Colin | SUS_COU1 | Four-Seam | 82 | 30 | 0.213 | 58.4 | 81.8 | 78.7 | 15.4% | 8.0% | 10.0% | 20.0% | 48.9 | 40.5 | 58.7 | 43.4 | 25 |

### Sinkers

| Rank | Pitcher | Team | Pitch Type | Pitches | BBE | xwOBA | PVS 20-80 | PVS 0-100 | EV | Whiff% | K% | HardHit% | SweetSpot% | GB Score | K Score | LD Supp | FB Supp | Pitch Type Rank |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 30 | Riedel, Caleb | SCH_BOO | Sinker | 91 | 26 | 0.125 | 70.6 | 97.1 | 71.7 | 26.2% | 35.0% | 7.7% | 26.9% | 41.2 | 62.1 | 61.0 | 33.9 | 1 |
| 35 | Still, Stephen | TRI_VAL | Sinker | 61 | 18 | 0.212 | 69.4 | 96.6 | 74.7 | 25.8% | 36.4% | 11.1% | 16.7% | 41.9 | 63.2 | 68.7 | 29.7 | 2 |
| 60 | Glickstein, Aaron | SCH_BOO | Sinker | 125 | 38 | 0.185 | 66.6 | 94.1 | 73.8 | 16.4% | 10.0% | 7.9% | 23.7% | 49.1 | 42.1 | 55.5 | 45.5 | 3 |
| 75 | Colon, Jeffrey | TRO_AIG | Sinker | 56 | 17 | 0.170 | 64.6 | 92.6 | 73.9 | 18.5% | 13.3% | 23.5% | 17.6% | 52.5 | 44.8 | 68.3 | 41.0 | 4 |
| 84 | Widener, Jacob | SUS_COU1 | Sinker | 192 | 53 | 0.191 | 64.0 | 91.7 | 73.5 | 30.1% | 15.2% | 15.1% | 26.4% | 52.8 | 46.3 | 51.6 | 51.9 | 5 |
| 91 | Odonnell, Brendan | NEW_ENG23 | Sinker | 135 | 27 | 0.210 | 63.1 | 91.0 | 76.8 | 23.5% | 9.1% | 7.4% | 18.5% | 72.7 | 41.4 | 61.6 | 66.1 | 6 |
| 93 | Mannering, Shawn | DOW_EAS1 | Sinker | 59 | 15 | 0.258 | 63.1 | 90.8 | 74.8 | 22.2% | 6.7% | 13.3% | 26.7% | 35.7 | 39.5 | 50.1 | 35.2 | 7 |
| 97 | Garcia, Andrew | EVA_OTT | Sinker | 52 | 12 | 0.240 | 62.7 | 90.4 | 75.8 | 13.6% | 0.0% | 16.7% | 16.7% | 79.3 | 34.1 | 75.9 | 63.9 | 8 |
| 110 | Lovell, Justin | WIN_CIT29 | Sinker | 183 | 49 | 0.187 | 61.8 | 89.1 | 74.8 | 28.4% | 15.0% | 16.3% | 26.5% | 53.8 | 46.1 | 52.2 | 52.6 | 9 |
| 115 | Grills, Evan | OTT_TIT | Sinker | 55 | 18 | 0.206 | 61.4 | 88.6 | 77.2 | 17.4% | 26.7% | 11.1% | 22.2% | 37.5 | 55.4 | 61.6 | 29.7 | 10 |
| 116 | Plumadore, Carson | WIN_CIT29 | Sinker | 162 | 48 | 0.174 | 61.4 | 88.5 | 75.4 | 20.3% | 39.4% | 8.3% | 33.3% | 31.4 | 65.6 | 43.7 | 34.8 | 11 |
| 133 | Petschke, Ben | EVA_OTT | Sinker | 59 | 13 | 0.206 | 60.6 | 86.8 | 75.6 | 14.8% | 15.4% | 23.1% | 23.1% | 56.5 | 46.4 | 56.1 | 52.8 | 12 |
| 153 | Sabatine, Gino | TRI_VAL | Sinker | 54 | 19 | 0.193 | 59.4 | 84.8 | 76.2 | 13.0% | 7.1% | 10.5% | 31.6% | 49.1 | 39.8 | 55.5 | 45.5 | 13 |
| 195 | Morgan, Marcus | JOL_SLA | Sinker | 96 | 23 | 0.227 | 57.9 | 80.6 | 77.7 | 27.8% | 34.8% | 13.0% | 26.1% | 54.3 | 61.9 | 53.5 | 52.3 | 14 |
| 207 | Lawson, Nathan | FLO_Y'A | Sinker | 276 | 110 | 0.210 | 57.3 | 79.4 | 77.3 | 9.0% | 6.4% | 9.1% | 30.9% | 53.7 | 39.3 | 54.8 | 50.8 | 15 |
| 215 | Grounds, Jackson | DOW_EAS1 | Sinker | 116 | 26 | 0.215 | 57.0 | 78.6 | 76.8 | 22.9% | 7.7% | 11.5% | 30.8% | 47.3 | 40.3 | 36.2 | 56.0 | 16 |
| 228 | McCartney, Seth | MIS_MUD | Sinker | 120 | 39 | 0.238 | 56.6 | 77.3 | 78.3 | 8.3% | 5.3% | 20.5% | 17.9% | 62.6 | 38.3 | 56.1 | 59.1 | 17 |
| 249 | Lodes, Jett | FLO_Y'A | Sinker | 96 | 30 | 0.218 | 55.9 | 75.2 | 77.9 | 11.9% | 12.5% | 6.7% | 33.3% | 56.9 | 44.1 | 58.7 | 51.6 | 18 |
| 251 | Long, Maddox | WAS_WIL3 | Sinker | 285 | 84 | 0.233 | 55.9 | 75.0 | 78.6 | 15.4% | 17.8% | 15.5% | 23.8% | 65.2 | 48.4 | 57.5 | 60.9 | 19 |
| 252 | Fauci, Sonny | NEW_JER6 | Sinker | 122 | 39 | 0.219 | 55.8 | 75.0 | 78.0 | 11.8% | 10.8% | 15.4% | 25.6% | 52.4 | 42.8 | 49.4 | 52.8 | 20 |
| 262 | Milburn, Isaac | FLO_Y'A | Sinker | 137 | 50 | 0.233 | 55.6 | 74.0 | 78.5 | 13.4% | 4.7% | 18.0% | 22.0% | 62.7 | 37.9 | 57.8 | 58.1 | 21 |
| 264 | Fritz, AJ | MIS_MUD | Sinker | 55 | 21 | 0.237 | 55.6 | 73.8 | 78.5 | 28.1% | 16.7% | 9.5% | 33.3% | 50.1 | 47.4 | 45.2 | 53.1 | 22 |
| 266 | Turner, Eric | JOL_SLA | Sinker | 113 | 39 | 0.209 | 55.5 | 73.6 | 77.1 | 15.4% | 8.8% | 17.9% | 28.2% | 46.3 | 41.2 | 49.4 | 46.5 | 23 |
| 272 | Leak, Anthony | NEW_YOR13 | Sinker | 154 | 40 | 0.230 | 55.3 | 73.0 | 76.3 | 13.6% | 12.1% | 17.5% | 32.5% | 57.5 | 43.8 | 46.9 | 59.8 | 24 |
| 274 | Barrett, Gabriel | NEW_YOR13 | Sinker | 60 | 21 | 0.209 | 55.3 | 72.8 | 75.1 | 17.2% | 21.4% | 14.3% | 42.9% | 50.1 | 51.2 | 39.1 | 57.0 | 25 |

### Sliders

| Rank | Pitcher | Team | Pitch Type | Pitches | BBE | xwOBA | PVS 20-80 | PVS 0-100 | EV | Whiff% | K% | HardHit% | SweetSpot% | GB Score | K Score | LD Supp | FB Supp | Pitch Type Rank |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 3 | Vecerka, Boris | QUE_CAP | Slider | 83 | 18 | 0.123 | 80.0 | 99.8 | 69.1 | 25.9% | 38.9% | 5.6% | 16.7% | 59.5 | 65.2 | 54.4 | 57.0 | 1 |
| 4 | Carroll, Jake | JOL_SLA | Slider | 74 | 15 | 0.178 | 80.0 | 99.7 | 69.4 | 24.1% | 23.5% | 0.0% | 20.0% | 62.1 | 52.9 | 58.7 | 57.0 | 2 |
| 5 | Flontek, Zac | DOW_EAS1 | Slider | 76 | 12 | 0.089 | 80.0 | 99.6 | 70.5 | 40.9% | 45.5% | 8.3% | 8.3% | 52.9 | 70.4 | 65.1 | 43.4 | 3 |
| 6 | Ryan, Dillon | NEW_ENG23 | Slider | 149 | 29 | 0.145 | 79.6 | 99.5 | 70.4 | 38.7% | 35.3% | 0.0% | 17.2% | 60.9 | 62.3 | 62.5 | 53.3 | 4 |
| 8 | Harley, Tristan | SUS_COU1 | Slider | 74 | 16 | 0.112 | 77.0 | 99.3 | 69.0 | 35.5% | 31.2% | 6.2% | 25.0% | 54.6 | 59.1 | 51.7 | 53.6 | 5 |
| 9 | Sanders, Brayden | MIS_MUD | Slider | 66 | 11 | 0.160 | 76.6 | 99.2 | 70.6 | 45.8% | 46.7% | 9.1% | 18.2% | 63.1 | 71.4 | 75.9 | 47.1 | 6 |
| 10 | Bauer, Patrick | QUE_CAP | Slider | 71 | 14 | 0.151 | 76.5 | 99.1 | 72.4 | 22.7% | 20.0% | 7.1% | 7.1% | 36.9 | 50.1 | 66.7 | 25.8 | 7 |
| 11 | Alpern, Liam | FLO_Y'A | Slider | 78 | 16 | 0.113 | 76.1 | 99.0 | 69.9 | 14.3% | 35.7% | 12.5% | 18.8% | 54.6 | 62.7 | 67.8 | 43.4 | 8 |
| 14 | Kramer, Cameron | TRO_AIG | Slider | 63 | 10 | 0.176 | 75.7 | 98.7 | 69.1 | 53.6% | 42.9% | 10.0% | 30.0% | 59.5 | 68.4 | 50.1 | 59.8 | 9 |
| 17 | Jones, Logan | TRI_VAL | Slider | 65 | 17 | 0.190 | 74.3 | 98.4 | 68.2 | 23.1% | 25.0% | 11.8% | 35.3% | 52.5 | 54.1 | 45.6 | 55.4 | 10 |
| 19 | Bargo, Casey | NEW_ENG23 | Slider | 56 | 16 | 0.176 | 73.6 | 98.2 | 74.6 | 28.0% | 40.0% | 0.0% | 12.5% | 69.4 | 66.1 | 59.8 | 63.9 | 11 |
| 23 | Harper, Scott | NEW_YOR13 | Slider | 243 | 40 | 0.153 | 72.8 | 97.8 | 71.5 | 47.7% | 44.1% | 5.0% | 25.0% | 39.7 | 69.3 | 59.8 | 33.1 | 12 |
| 25 | McEvoy, Aidan | FLO_Y'A | Slider | 135 | 33 | 0.159 | 71.9 | 97.6 | 73.0 | 43.5% | 38.1% | 6.1% | 21.2% | 41.5 | 64.6 | 56.4 | 37.2 | 13 |
| 26 | Kirby, Zach | WAS_WIL3 | Slider | 127 | 42 | 0.156 | 71.6 | 97.5 | 73.3 | 21.1% | 13.8% | 2.4% | 21.4% | 40.6 | 45.2 | 57.5 | 35.6 | 14 |
| 34 | Donnan, Blake | FLO_Y'A | Slider | 65 | 10 | 0.184 | 69.7 | 96.7 | 71.5 | 51.7% | 52.9% | 10.0% | 30.0% | 43.7 | 76.4 | 50.1 | 43.4 | 15 |
| 39 | Nakata, Yuto | QUE_CAP | Slider | 107 | 24 | 0.162 | 69.0 | 96.2 | 75.2 | 34.1% | 29.6% | 0.0% | 20.8% | 59.5 | 57.8 | 59.8 | 53.6 | 16 |
| 46 | Townes, Holland | SCH_BOO | Slider | 55 | 14 | 0.191 | 68.4 | 95.5 | 74.3 | 25.0% | 10.0% | 14.3% | 14.3% | 48.2 | 42.1 | 57.5 | 43.4 | 17 |
| 47 | MacMillan, Blake | TRO_AIG | Slider | 108 | 14 | 0.196 | 68.1 | 95.4 | 72.2 | 53.5% | 60.9% | 21.4% | 21.4% | 65.2 | 80.0 | 48.3 | 66.8 | 18 |
| 48 | Hickey, Matt | GAT_GRI | Slider | 112 | 33 | 0.204 | 67.9 | 95.3 | 74.2 | 24.0% | 13.3% | 12.1% | 15.2% | 60.7 | 44.8 | 64.2 | 52.1 | 19 |
| 49 | Duncan, Tanner | DOW_EAS1 | Slider | 88 | 14 | 0.162 | 67.9 | 95.2 | 77.2 | 50.0% | 30.4% | 7.1% | 7.1% | 70.8 | 58.4 | 75.9 | 55.1 | 20 |
| 55 | Balzan, Jackson | SUS_COU1 | Slider | 93 | 27 | 0.179 | 67.3 | 94.6 | 74.6 | 33.3% | 28.6% | 7.4% | 22.2% | 52.2 | 57.0 | 61.6 | 44.9 | 21 |
| 57 | Jones, Logan | FLO_Y'A | Slider | 82 | 15 | 0.176 | 66.7 | 94.4 | 76.6 | 51.2% | 42.9% | 0.0% | 20.0% | 56.9 | 68.4 | 50.1 | 57.0 | 22 |
| 58 | Marynczak, Arlo | TRI_VAL | Slider | 57 | 12 | 0.170 | 66.7 | 94.3 | 73.8 | 26.1% | 11.1% | 8.3% | 25.0% | 39.7 | 43.0 | 54.4 | 36.5 | 23 |
| 59 | Vega, Lucas | TRO_AIG | Slider | 134 | 36 | 0.155 | 66.7 | 94.2 | 75.6 | 26.8% | 28.6% | 5.6% | 19.4% | 39.7 | 57.0 | 54.4 | 36.5 | 24 |
| 62 | Tomczak, Anthony | EVA_OTT | Slider | 74 | 19 | 0.149 | 66.4 | 93.9 | 75.4 | 26.7% | 26.7% | 0.0% | 26.3% | 53.2 | 55.4 | 62.3 | 45.5 | 25 |

### Curveballs

| Rank | Pitcher | Team | Pitch Type | Pitches | BBE | xwOBA | PVS 20-80 | PVS 0-100 | EV | Whiff% | K% | HardHit% | SweetSpot% | GB Score | K Score | LD Supp | FB Supp | Pitch Type Rank |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | Grounds, Jackson | DOW_EAS1 | Curveball | 82 | 10 | 0.109 | 80.0 | 100.0 | 64.6 | 42.1% | 41.2% | 0.0% | 0.0% | 59.5 | 67.0 | 75.9 | 43.4 | 1 |
| 7 | Morgan, Cooper | QUE_CAP | Curveball | 99 | 30 | 0.148 | 78.8 | 99.4 | 65.7 | 33.3% | 40.0% | 6.7% | 40.0% | 43.7 | 66.1 | 54.4 | 40.6 | 2 |
| 12 | Sparks, Alec | GAT_GRI | Curveball | 89 | 12 | 0.160 | 76.0 | 98.9 | 70.8 | 39.3% | 41.2% | 0.0% | 25.0% | 52.9 | 67.0 | 54.4 | 50.2 | 3 |
| 32 | Rodriguez, Ramon | WIN_CIT29 | Curveball | 119 | 22 | 0.173 | 69.9 | 96.9 | 74.1 | 26.3% | 26.3% | 4.5% | 18.2% | 45.1 | 55.2 | 70.0 | 32.2 | 4 |
| 33 | Bohnert, Matthew | WIN_CIT29 | Curveball | 124 | 14 | 0.163 | 69.9 | 96.8 | 75.1 | 46.8% | 45.8% | 7.1% | 14.3% | 59.5 | 70.7 | 66.7 | 49.2 | 5 |
| 36 | Pierson, Kenny | LAK_ERI24 | Curveball | 91 | 12 | 0.204 | 69.3 | 96.5 | 72.9 | 32.1% | 35.3% | 8.3% | 25.0% | 33.1 | 62.3 | 65.1 | 22.9 | 6 |
| 44 | Jones, Breyln | NEW_JER6 | Curveball | 60 | 12 | 0.186 | 68.5 | 95.7 | 76.4 | 29.2% | 38.9% | 0.0% | 16.7% | 59.5 | 65.2 | 75.9 | 43.4 | 7 |
| 56 | Hohenstein, Liam | WIN_CIT29 | Curveball | 109 | 20 | 0.160 | 67.0 | 94.5 | 72.9 | 27.3% | 10.5% | 0.0% | 35.0% | 39.7 | 42.5 | 50.1 | 39.3 | 8 |
| 65 | Binns, Malik | NEW_JER6 | Curveball | 55 | 13 | 0.184 | 66.2 | 93.6 | 73.8 | 27.3% | 13.3% | 7.7% | 30.8% | 62.6 | 44.8 | 56.1 | 59.1 | 9 |
| 67 | Heredia-Bustos, Rolando | DOW_EAS1 | Curveball | 75 | 18 | 0.177 | 66.0 | 93.4 | 73.1 | 33.3% | 23.1% | 16.7% | 22.2% | 46.3 | 52.6 | 47.2 | 47.9 | 10 |
| 73 | Hickey, Matt | GAT_GRI | Curveball | 84 | 18 | 0.200 | 65.0 | 92.8 | 75.9 | 25.0% | 35.3% | 5.6% | 22.2% | 63.9 | 62.3 | 61.6 | 57.0 | 11 |
| 82 | Conklin, MacCallan | TRO_AIG | Curveball | 55 | 13 | 0.197 | 64.2 | 91.9 | 77.3 | 21.1% | 20.0% | 15.4% | 7.7% | 62.6 | 50.1 | 66.0 | 52.8 | 12 |
| 85 | Eisenbarger, Jack | QUE_CAP | Curveball | 98 | 14 | 0.232 | 63.9 | 91.6 | 73.0 | 27.3% | 28.6% | 14.3% | 35.7% | 53.8 | 57.0 | 48.3 | 55.1 | 13 |
| 92 | Salata, Derek | SCH_BOO | Curveball | 187 | 31 | 0.213 | 63.1 | 90.9 | 75.3 | 41.3% | 48.8% | 9.7% | 29.0% | 58.2 | 73.1 | 46.8 | 60.6 | 14 |
| 94 | Harris, Ben | GAT_GRI | Curveball | 324 | 33 | 0.215 | 63.1 | 90.7 | 77.8 | 33.8% | 58.9% | 12.1% | 15.2% | 60.7 | 80.0 | 56.4 | 57.0 | 15 |
| 101 | Garcia, Brett | OTT_TIT | Curveball | 153 | 26 | 0.193 | 62.1 | 90.0 | 77.1 | 32.0% | 47.1% | 11.5% | 19.2% | 56.5 | 71.7 | 66.0 | 46.5 | 16 |
| 119 | Hampton, Ky | OTT_TIT | Curveball | 76 | 20 | 0.176 | 61.3 | 88.2 | 72.6 | 21.4% | 31.2% | 15.0% | 40.0% | 55.5 | 59.1 | 43.7 | 59.8 | 17 |
| 120 | Boies, Emiles | QUE_CAP | Curveball | 118 | 28 | 0.173 | 61.2 | 88.1 | 75.9 | 34.7% | 25.0% | 17.9% | 21.4% | 59.5 | 54.1 | 62.1 | 52.1 | 18 |
| 122 | Hill, Kaleb | OTT_TIT | Curveball | 269 | 68 | 0.204 | 61.2 | 87.9 | 75.3 | 27.2% | 17.1% | 11.8% | 29.4% | 59.5 | 47.8 | 47.5 | 61.4 | 19 |
| 123 | Scafidi, Christian | LAK_ERI24 | Curveball | 61 | 12 | 0.193 | 61.2 | 87.8 | 75.7 | 26.3% | 50.0% | 8.3% | 33.3% | 72.7 | 74.1 | 43.7 | 77.5 | 20 |
| 129 | Kostura, Brit | WAS_WIL3 | Curveball | 87 | 38 | 0.209 | 60.8 | 87.2 | 75.3 | 16.7% | 14.3% | 13.2% | 28.9% | 55.3 | 45.5 | 42.0 | 60.6 | 21 |
| 139 | Cook, Cole | SCH_BOO | Curveball | 132 | 27 | 0.224 | 60.1 | 86.2 | 76.6 | 35.3% | 39.4% | 14.8% | 25.9% | 58.0 | 65.6 | 56.8 | 54.0 | 22 |
| 145 | Hocom, Quinn | TRI_VAL | Curveball | 120 | 27 | 0.228 | 59.8 | 85.6 | 75.7 | 14.3% | 4.8% | 22.2% | 18.5% | 72.7 | 37.9 | 56.8 | 69.2 | 23 |
| 148 | Campbell, AJ | WIN_CIT29 | Curveball | 80 | 15 | 0.191 | 59.8 | 85.3 | 78.4 | 5.0% | 7.1% | 6.7% | 20.0% | 41.0 | 39.8 | 58.7 | 35.2 | 24 |
| 150 | Zaffiro, Cole | SCH_BOO | Curveball | 66 | 13 | 0.212 | 59.5 | 85.1 | 77.9 | 15.8% | 6.7% | 15.4% | 15.4% | 80.0 | 39.5 | 66.0 | 78.0 | 25 |

### Changeups

| Rank | Pitcher | Team | Pitch Type | Pitches | BBE | xwOBA | PVS 20-80 | PVS 0-100 | EV | Whiff% | K% | HardHit% | SweetSpot% | GB Score | K Score | LD Supp | FB Supp | Pitch Type Rank |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 27 | Peyton, Blake | GAT_GRI | Changeup | 108 | 21 | 0.159 | 70.8 | 97.4 | 71.7 | 38.1% | 14.8% | 9.5% | 23.8% | 68.9 | 46.0 | 51.3 | 68.7 | 1 |
| 29 | Good, Ty | GAT_GRI | Changeup | 73 | 10 | 0.244 | 70.7 | 97.2 | 75.0 | 54.2% | 60.0% | 0.0% | 20.0% | 67.4 | 80.0 | 63.0 | 59.8 | 2 |
| 37 | Perdomo, Rafael | QUE_CAP | Changeup | 55 | 14 | 0.186 | 69.1 | 96.4 | 70.2 | 33.3% | 16.7% | 21.4% | 28.6% | 48.2 | 47.4 | 57.5 | 43.4 | 3 |
| 38 | Rodriguez, Joe Joe | NEW_JER6 | Changeup | 187 | 31 | 0.169 | 69.1 | 96.3 | 74.7 | 54.3% | 43.9% | 6.5% | 19.4% | 63.3 | 69.2 | 63.4 | 55.3 | 4 |
| 40 | Lawson, Nathan | FLO_Y'A | Changeup | 107 | 31 | 0.196 | 68.9 | 96.1 | 74.5 | 29.4% | 31.2% | 6.5% | 19.4% | 55.7 | 59.1 | 63.4 | 47.3 | 5 |
| 45 | Parsons, Billy | SUS_COU1 | Changeup | 62 | 17 | 0.233 | 68.4 | 95.6 | 74.2 | 28.1% | 41.2% | 5.9% | 23.5% | 80.0 | 67.0 | 68.3 | 74.7 | 6 |
| 52 | Escobar, Anthony | TRO_AIG | Changeup | 195 | 46 | 0.169 | 67.6 | 94.9 | 75.0 | 43.5% | 31.5% | 13.0% | 15.2% | 52.6 | 59.3 | 64.7 | 43.4 | 7 |
| 54 | Wiltse, Ryan | EVA_OTT | Changeup | 202 | 56 | 0.190 | 67.4 | 94.7 | 73.4 | 34.6% | 29.3% | 5.4% | 30.4% | 58.1 | 57.5 | 48.3 | 59.5 | 8 |
| 61 | O'Hanlon, Michael | WAS_WIL3 | Changeup | 66 | 11 | 0.174 | 66.4 | 94.0 | 72.4 | 57.1% | 57.9% | 18.2% | 27.3% | 48.7 | 80.0 | 52.5 | 47.1 | 9 |
| 63 | Messina, Chris | FDU_KNI | Changeup | 68 | 16 | 0.253 | 66.4 | 93.8 | 75.3 | 16.7% | 5.9% | 6.2% | 18.8% | 69.4 | 38.8 | 67.8 | 58.7 | 10 |
| 64 | Harris, Everette | TRI_VAL | Changeup | 118 | 32 | 0.181 | 66.3 | 93.7 | 75.5 | 13.5% | 5.7% | 9.4% | 15.6% | 69.4 | 38.7 | 59.8 | 63.9 | 11 |
| 68 | Campbell, Tyler | MIS_MUD | Changeup | 138 | 37 | 0.194 | 65.6 | 93.3 | 76.2 | 33.3% | 25.7% | 5.4% | 18.9% | 37.0 | 54.7 | 61.9 | 29.0 | 12 |
| 77 | Drakeford, Dosie | NEW_JER6 | Changeup | 84 | 15 | 0.158 | 64.5 | 92.4 | 73.9 | 56.8% | 54.2% | 0.0% | 40.0% | 46.3 | 77.4 | 32.9 | 57.0 | 13 |
| 79 | Leak, Anthony | NEW_YOR13 | Changeup | 91 | 22 | 0.190 | 64.3 | 92.2 | 77.6 | 25.0% | 5.0% | 4.5% | 13.6% | 59.5 | 38.1 | 70.0 | 47.1 | 14 |
| 86 | Tokar, Heitor | OTT_TIT | Changeup | 80 | 28 | 0.203 | 63.9 | 91.5 | 75.2 | 20.0% | 12.5% | 10.7% | 25.0% | 53.8 | 44.1 | 57.5 | 49.2 | 15 |
| 90 | Earwood, Micah | SUS_COU1 | Changeup | 216 | 30 | 0.187 | 63.3 | 91.1 | 73.7 | 18.2% | 0.0% | 6.7% | 36.7% | 62.1 | 34.1 | 58.7 | 57.0 | 16 |
| 96 | Smith, Ben | NEW_ENG23 | Changeup | 73 | 22 | 0.186 | 62.9 | 90.5 | 78.6 | 18.2% | 5.3% | 4.5% | 13.6% | 66.7 | 38.3 | 70.0 | 54.5 | 17 |
| 99 | Sesar, Jorden | SUS_COU1 | Changeup | 99 | 29 | 0.173 | 62.5 | 90.2 | 75.2 | 26.5% | 26.1% | 10.3% | 31.0% | 49.9 | 55.0 | 49.2 | 50.4 | 18 |
| 104 | Morgan, Cooper | QUE_CAP | Changeup | 92 | 27 | 0.196 | 61.9 | 89.7 | 75.6 | 30.2% | 24.0% | 7.4% | 29.6% | 52.2 | 53.3 | 56.8 | 47.9 | 19 |
| 108 | Serrano, Elio | NEW_JER6 | Changeup | 101 | 24 | 0.191 | 61.8 | 89.3 | 76.3 | 34.5% | 29.2% | 16.7% | 20.8% | 49.6 | 57.4 | 59.8 | 43.4 | 20 |
| 112 | Zentko, Dylan | EVA_OTT | Changeup | 110 | 26 | 0.223 | 61.6 | 88.9 | 75.0 | 33.3% | 28.0% | 11.5% | 30.8% | 47.3 | 56.5 | 41.2 | 52.8 | 21 |
| 113 | Maietta, Dante | WIN_CIT29 | Changeup | 330 | 70 | 0.189 | 61.5 | 88.8 | 77.0 | 39.6% | 31.7% | 10.0% | 22.9% | 49.3 | 59.5 | 57.5 | 44.5 | 22 |
| 126 | Barreto, Brayhans | TRI_VAL | Changeup | 130 | 27 | 0.220 | 60.9 | 87.5 | 75.4 | 38.8% | 19.4% | 7.4% | 33.3% | 52.2 | 49.7 | 52.0 | 51.0 | 23 |
| 134 | Hagan, Jack | DOW_EAS1 | Changeup | 52 | 15 | 0.188 | 60.6 | 86.7 | 77.6 | 10.5% | 11.1% | 6.7% | 26.7% | 56.9 | 43.0 | 58.7 | 51.6 | 24 |
| 135 | Eisenbarger, Jack | QUE_CAP | Changeup | 227 | 41 | 0.192 | 60.5 | 86.6 | 75.6 | 50.9% | 35.5% | 17.1% | 26.8% | 48.9 | 62.5 | 60.2 | 42.4 | 25 |

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