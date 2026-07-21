# Frontier League Pitch Value Score

- Input file: `data\processed\pitcher_pitch_type_xwoba_metrics.csv`
- Output file: `data\processed\pitch_value_scores.csv`
- Qualified pitcher-pitch types scored: 889
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
| 1 | Grounds, Jackson | DOW_EAS1 | Curveball | 82 | 10 | 0.107 | 80.0 | 100.0 | 64.6 | 42.1% | 41.2% | 0.0% | 0.0% | 59.0 | 67.6 | 76.2 | 43.1 | 1 |
| 2 | Vecerka, Boris | QUE_CAP | Slider | 83 | 18 | 0.123 | 80.0 | 99.9 | 69.1 | 25.9% | 38.9% | 5.6% | 16.7% | 59.0 | 65.7 | 54.3 | 56.8 | 1 |
| 3 | Carroll, Jake | JOL_SLA | Slider | 74 | 15 | 0.177 | 80.0 | 99.8 | 69.4 | 24.1% | 23.5% | 0.0% | 20.0% | 61.6 | 53.2 | 58.7 | 56.8 | 2 |
| 4 | Ryan, Dillon | NEW_ENG23 | Slider | 125 | 25 | 0.144 | 79.9 | 99.7 | 69.9 | 35.3% | 34.5% | 0.0% | 20.0% | 60.5 | 62.1 | 60.4 | 54.6 | 3 |
| 5 | Zentko, Dylan | EVA_OTT | Changeup | 67 | 13 | 0.155 | 78.5 | 99.6 | 70.2 | 44.8% | 35.7% | 7.7% | 15.4% | 68.0 | 63.1 | 56.0 | 65.2 | 1 |
| 6 | Morgan, Cooper | QUE_CAP | Curveball | 85 | 26 | 0.149 | 78.0 | 99.4 | 65.8 | 35.4% | 42.9% | 7.7% | 42.3% | 44.0 | 69.0 | 56.0 | 39.9 | 2 |
| 7 | Peyton, Blake | GAT_GRI | Changeup | 93 | 20 | 0.140 | 77.2 | 99.3 | 70.1 | 37.5% | 15.4% | 5.0% | 20.0% | 70.7 | 46.5 | 56.5 | 67.7 | 2 |
| 8 | Alpern, Liam | FLO_Y'A | Slider | 78 | 16 | 0.112 | 76.3 | 99.2 | 69.9 | 14.3% | 35.7% | 12.5% | 18.8% | 54.1 | 63.1 | 68.0 | 43.1 | 4 |
| 9 | Serrano, Elio | NEW_JER6 | Changeup | 63 | 15 | 0.148 | 75.9 | 99.1 | 70.0 | 35.1% | 21.4% | 6.7% | 26.7% | 51.2 | 51.4 | 58.7 | 45.8 | 3 |
| 10 | Jones, Logan | TRI_VAL | Slider | 65 | 17 | 0.191 | 74.7 | 99.0 | 68.2 | 23.1% | 25.0% | 11.8% | 35.3% | 52.1 | 54.4 | 45.3 | 55.2 | 5 |
| 11 | Bauer, Patrick | QUE_CAP | Slider | 51 | 11 | 0.170 | 74.4 | 98.9 | 73.0 | 12.5% | 25.0% | 9.1% | 9.1% | 34.2 | 54.4 | 64.3 | 24.4 | 6 |
| 12 | Grounds, Jackson | DOW_EAS1 | Four-Seam | 107 | 27 | 0.158 | 74.3 | 98.8 | 69.9 | 25.5% | 21.7% | 11.1% | 25.9% | 37.3 | 51.7 | 51.9 | 35.5 | 1 |
| 13 | Davis, Tyler | WIN_CIT29 | Four-Seam | 76 | 19 | 0.111 | 74.3 | 98.7 | 75.6 | 23.1% | 19.0% | 5.3% | 0.0% | 44.6 | 49.5 | 76.2 | 28.0 | 2 |
| 14 | Debban, Caleb | NEW_JER6 | Four-Seam | 57 | 13 | 0.173 | 73.7 | 98.5 | 70.6 | 20.0% | 6.2% | 7.7% | 23.1% | 50.0 | 39.0 | 66.1 | 39.9 | 3 |
| 15 | Harper, Scott | NEW_YOR13 | Slider | 217 | 34 | 0.150 | 73.6 | 98.4 | 72.5 | 49.4% | 45.3% | 5.9% | 17.6% | 38.3 | 70.9 | 64.6 | 28.6 | 7 |
| 16 | Garcia, Hector | WAS_WIL3 | Splitter | 62 | 13 | 0.184 | 73.6 | 98.3 | 71.1 | 45.7% | 40.0% | 7.7% | 23.1% | 56.0 | 66.6 | 56.0 | 52.6 | 1 |
| 17 | Bargo, Casey | NEW_ENG23 | Slider | 56 | 16 | 0.176 | 73.5 | 98.2 | 74.6 | 28.0% | 40.0% | 0.0% | 12.5% | 68.7 | 66.6 | 59.8 | 63.6 | 8 |
| 18 | McEvoy, Aidan | FLO_Y'A | Slider | 119 | 30 | 0.153 | 72.5 | 98.1 | 72.8 | 40.7% | 34.2% | 6.7% | 20.0% | 40.8 | 61.9 | 58.7 | 34.9 | 9 |
| 19 | Lawson, Nathan | FLO_Y'A | Changeup | 68 | 22 | 0.194 | 72.4 | 98.0 | 73.5 | 23.5% | 30.0% | 4.5% | 18.2% | 48.3 | 58.5 | 64.3 | 39.4 | 4 |
| 20 | Cameron, Zach | WIN_CIT29 | Four-Seam | 120 | 43 | 0.195 | 71.9 | 97.9 | 73.0 | 19.0% | 24.2% | 11.6% | 14.0% | 49.0 | 53.7 | 64.0 | 40.2 | 4 |
| 21 | Bohnert, Matthew | WIN_CIT29 | Curveball | 98 | 12 | 0.143 | 71.8 | 97.8 | 75.1 | 46.2% | 47.4% | 8.3% | 8.3% | 65.5 | 72.7 | 76.2 | 49.9 | 3 |
| 22 | Leduc, Zachary | TRO_AIG | Slider | 87 | 15 | 0.128 | 71.7 | 97.6 | 71.0 | 45.5% | 36.8% | 13.3% | 26.7% | 56.4 | 64.0 | 58.7 | 51.3 | 10 |
| 23 | Kirby, Zach | WAS_WIL3 | Slider | 127 | 42 | 0.156 | 71.6 | 97.5 | 73.3 | 21.1% | 13.8% | 2.4% | 21.4% | 40.4 | 45.2 | 57.4 | 35.3 | 11 |
| 24 | Soto, Carlos | JOL_SLA | Splitter | 54 | 11 | 0.173 | 71.0 | 97.4 | 73.5 | 34.5% | 43.8% | 9.1% | 18.2% | 69.6 | 69.7 | 64.3 | 61.7 | 2 |
| 25 | Hickey, Matt | GAT_GRI | Slider | 89 | 26 | 0.206 | 70.5 | 97.3 | 72.3 | 23.1% | 12.5% | 11.5% | 19.2% | 65.0 | 44.1 | 61.0 | 58.9 | 12 |

## Leaderboards by Pitch Family

### Four-Seams

| Rank | Pitcher | Team | Pitch Type | Pitches | BBE | xwOBA | PVS 20-80 | PVS 0-100 | EV | Whiff% | K% | HardHit% | SweetSpot% | GB Score | K Score | LD Supp | FB Supp | Pitch Type Rank |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 12 | Grounds, Jackson | DOW_EAS1 | Four-Seam | 107 | 27 | 0.158 | 74.3 | 98.8 | 69.9 | 25.5% | 21.7% | 11.1% | 25.9% | 37.3 | 51.7 | 51.9 | 35.5 | 1 |
| 13 | Davis, Tyler | WIN_CIT29 | Four-Seam | 76 | 19 | 0.111 | 74.3 | 98.7 | 75.6 | 23.1% | 19.0% | 5.3% | 0.0% | 44.6 | 49.5 | 76.2 | 28.0 | 2 |
| 14 | Debban, Caleb | NEW_JER6 | Four-Seam | 57 | 13 | 0.173 | 73.7 | 98.5 | 70.6 | 20.0% | 6.2% | 7.7% | 23.1% | 50.0 | 39.0 | 66.1 | 39.9 | 3 |
| 20 | Cameron, Zach | WIN_CIT29 | Four-Seam | 120 | 43 | 0.195 | 71.9 | 97.9 | 73.0 | 19.0% | 24.2% | 11.6% | 14.0% | 49.0 | 53.7 | 64.0 | 40.2 | 4 |
| 34 | Campbell, Tyler | MIS_MUD | Four-Seam | 60 | 20 | 0.179 | 68.7 | 96.3 | 72.1 | 7.4% | 0.0% | 10.0% | 25.0% | 62.9 | 33.9 | 56.5 | 59.5 | 5 |
| 44 | Correa, Nelvin | QUE_CAP | Four-Seam | 96 | 29 | 0.191 | 67.3 | 95.2 | 74.9 | 13.2% | 3.7% | 6.9% | 17.2% | 49.6 | 37.0 | 67.2 | 38.8 | 6 |
| 47 | Grounds, Jackson | TRO_AIG | Four-Seam | 79 | 19 | 0.149 | 66.9 | 94.8 | 71.9 | 34.4% | 16.7% | 5.3% | 36.8% | 40.5 | 47.6 | 55.5 | 36.6 | 7 |
| 61 | Foy, Corbin | LAK_ERI24 | Four-Seam | 96 | 19 | 0.176 | 65.7 | 93.3 | 72.9 | 18.5% | 25.0% | 5.3% | 36.8% | 40.5 | 54.4 | 48.5 | 40.9 | 8 |
| 63 | Earwood, Micah | SUS_COU1 | Four-Seam | 96 | 12 | 0.228 | 65.5 | 93.0 | 73.1 | 0.0% | 0.0% | 8.3% | 33.3% | 59.0 | 33.9 | 43.3 | 63.6 | 9 |
| 75 | Gregory, Ben | GAT_GRI | Four-Seam | 93 | 18 | 0.186 | 64.0 | 91.7 | 77.0 | 26.7% | 9.5% | 5.6% | 16.7% | 54.6 | 41.7 | 61.6 | 47.6 | 10 |
| 87 | Garbrick, Alex | LAK_ERI24 | Four-Seam | 82 | 32 | 0.223 | 63.2 | 90.3 | 76.7 | 16.3% | 11.5% | 15.6% | 12.5% | 59.0 | 43.4 | 63.9 | 50.8 | 11 |
| 92 | Shears, Tanner | SCH_BOO | Four-Seam | 240 | 43 | 0.189 | 62.8 | 89.8 | 74.3 | 35.5% | 31.2% | 7.0% | 34.9% | 39.9 | 59.5 | 45.6 | 42.1 | 12 |
| 99 | Hensey, Rob | SUS_COU1 | Four-Seam | 220 | 60 | 0.186 | 62.1 | 89.0 | 75.2 | 33.0% | 31.1% | 8.3% | 31.7% | 47.3 | 59.4 | 56.5 | 43.1 | 13 |
| 101 | Brown, Ethan | WAS_WIL3 | Four-Seam | 67 | 25 | 0.217 | 62.0 | 88.8 | 74.2 | 10.0% | 12.5% | 16.0% | 28.0% | 41.8 | 44.1 | 39.4 | 48.0 | 14 |
| 106 | Morgan, Cooper | QUE_CAP | Four-Seam | 85 | 22 | 0.198 | 61.6 | 88.2 | 75.1 | 38.6% | 43.5% | 0.0% | 40.9% | 48.3 | 69.5 | 46.3 | 50.6 | 15 |
| 108 | Cartwright, Eli | GAT_GRI | Four-Seam | 207 | 46 | 0.193 | 61.4 | 88.0 | 76.4 | 31.1% | 25.0% | 8.7% | 26.1% | 35.3 | 54.4 | 53.3 | 32.4 | 16 |
| 115 | Lyons, Kendall | QUE_CAP | Four-Seam | 71 | 28 | 0.181 | 60.9 | 87.2 | 77.1 | 25.6% | 26.3% | 7.1% | 25.0% | 42.3 | 55.4 | 57.4 | 37.2 | 17 |
| 119 | Mercado, Nelson | OTT_TIT | Four-Seam | 81 | 27 | 0.169 | 60.6 | 86.7 | 76.2 | 17.9% | 5.9% | 11.1% | 25.9% | 34.4 | 38.7 | 51.9 | 32.4 | 18 |
| 129 | Anderson, Colt | WAS_WIL3 | Four-Seam | 266 | 94 | 0.216 | 60.3 | 85.6 | 75.0 | 16.7% | 14.7% | 12.8% | 33.0% | 53.2 | 45.9 | 44.0 | 57.1 | 19 |
| 131 | Harley, Tristan | SUS_COU1 | Four-Seam | 68 | 28 | 0.224 | 60.0 | 85.4 | 76.7 | 13.9% | 0.0% | 10.7% | 25.0% | 39.5 | 33.9 | 57.4 | 34.3 | 20 |
| 133 | Wehrle, Tyler | WIN_CIT29 | Four-Seam | 236 | 50 | 0.188 | 59.6 | 85.2 | 76.4 | 33.0% | 30.6% | 10.0% | 30.0% | 34.0 | 59.0 | 49.9 | 33.2 | 21 |
| 139 | Kaminer, Brandon | DOW_EAS1 | Four-Seam | 185 | 57 | 0.226 | 59.4 | 84.5 | 76.5 | 12.7% | 14.5% | 8.8% | 31.6% | 46.0 | 45.8 | 46.2 | 48.1 | 22 |
| 141 | Dima, Josh | GAT_GRI | Four-Seam | 238 | 57 | 0.204 | 59.2 | 84.3 | 76.7 | 31.9% | 31.4% | 8.8% | 29.8% | 44.6 | 59.6 | 48.5 | 45.2 | 23 |
| 146 | Zaffiro, Cole | SCH_BOO | Four-Seam | 335 | 92 | 0.198 | 59.0 | 83.7 | 76.7 | 28.1% | 25.3% | 6.5% | 32.6% | 39.5 | 54.6 | 59.1 | 33.3 | 24 |
| 148 | Langhorne, Miles | SUS_COU1 | Four-Seam | 70 | 21 | 0.245 | 58.9 | 83.5 | 76.0 | 10.0% | 6.7% | 9.5% | 33.3% | 53.4 | 39.4 | 32.4 | 64.6 | 25 |

### Sinkers

| Rank | Pitcher | Team | Pitch Type | Pitches | BBE | xwOBA | PVS 20-80 | PVS 0-100 | EV | Whiff% | K% | HardHit% | SweetSpot% | GB Score | K Score | LD Supp | FB Supp | Pitch Type Rank |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 27 | Riedel, Caleb | SCH_BOO | Sinker | 81 | 22 | 0.140 | 70.0 | 97.1 | 72.5 | 27.0% | 31.6% | 9.1% | 22.7% | 44.8 | 59.7 | 58.3 | 39.4 | 1 |
| 30 | Still, Stephen | TRI_VAL | Sinker | 61 | 18 | 0.211 | 69.4 | 96.7 | 74.7 | 25.8% | 36.4% | 11.1% | 16.7% | 41.7 | 63.7 | 68.9 | 29.4 | 2 |
| 55 | Glickstein, Aaron | SCH_BOO | Sinker | 105 | 35 | 0.184 | 66.2 | 93.9 | 74.0 | 16.0% | 7.4% | 8.6% | 22.9% | 49.0 | 40.0 | 57.4 | 44.3 | 3 |
| 59 | Odonnell, Brendan | NEW_ENG23 | Sinker | 109 | 21 | 0.203 | 65.9 | 93.5 | 76.5 | 23.8% | 5.6% | 4.8% | 14.3% | 72.0 | 38.5 | 63.7 | 64.6 | 4 |
| 69 | Colon, Jeffrey | TRO_AIG | Sinker | 56 | 17 | 0.169 | 64.7 | 92.4 | 73.9 | 18.5% | 13.3% | 23.5% | 17.6% | 52.1 | 44.8 | 68.5 | 40.7 | 5 |
| 80 | Widener, Jacob | SUS_COU1 | Sinker | 139 | 42 | 0.188 | 63.6 | 91.1 | 73.7 | 30.9% | 9.4% | 11.9% | 28.6% | 53.4 | 41.6 | 48.0 | 54.8 | 6 |
| 89 | Mannering, Shawn | DOW_EAS1 | Sinker | 59 | 15 | 0.256 | 63.1 | 90.1 | 74.8 | 22.2% | 6.7% | 13.3% | 26.7% | 35.6 | 39.4 | 49.9 | 34.9 | 7 |
| 95 | Garcia, Andrew | EVA_OTT | Sinker | 52 | 12 | 0.237 | 62.7 | 89.4 | 75.8 | 13.6% | 0.0% | 16.7% | 16.7% | 78.4 | 33.9 | 76.2 | 63.6 | 8 |
| 127 | Petschke, Ben | EVA_OTT | Sinker | 54 | 13 | 0.205 | 60.4 | 85.8 | 75.6 | 8.0% | 8.3% | 23.1% | 23.1% | 56.0 | 40.7 | 56.0 | 52.6 | 9 |
| 136 | Sabatine, Gino | TRI_VAL | Sinker | 54 | 19 | 0.193 | 59.5 | 84.8 | 76.2 | 13.0% | 7.1% | 10.5% | 31.6% | 48.7 | 39.8 | 55.5 | 45.2 | 10 |
| 137 | Harley, Tristan | SUS_COU1 | Sinker | 97 | 36 | 0.187 | 59.4 | 84.7 | 76.3 | 10.9% | 4.3% | 13.9% | 25.0% | 46.0 | 37.5 | 61.6 | 38.5 | 11 |
| 158 | Lovell, Justin | WIN_CIT29 | Sinker | 136 | 37 | 0.180 | 58.5 | 82.3 | 75.3 | 27.1% | 9.7% | 16.2% | 32.4% | 49.5 | 41.8 | 44.2 | 53.1 | 12 |
| 161 | Plumadore, Carson | WIN_CIT29 | Sinker | 138 | 42 | 0.187 | 58.4 | 82.0 | 75.8 | 16.4% | 37.9% | 9.5% | 38.1% | 29.3 | 64.9 | 38.6 | 35.3 | 13 |
| 170 | Hungate, Chase | NEW_JER6 | Sinker | 83 | 29 | 0.210 | 58.1 | 81.0 | 76.5 | 18.6% | 27.8% | 13.8% | 31.0% | 60.3 | 56.6 | 58.1 | 55.8 | 14 |
| 176 | Morgan, Marcus | JOL_SLA | Sinker | 96 | 23 | 0.226 | 57.9 | 80.3 | 77.7 | 27.8% | 34.8% | 13.0% | 26.1% | 53.9 | 62.4 | 53.3 | 52.0 | 15 |
| 197 | Grounds, Jackson | DOW_EAS1 | Sinker | 116 | 26 | 0.214 | 57.0 | 78.0 | 76.8 | 22.9% | 7.7% | 11.5% | 30.8% | 47.0 | 40.2 | 35.7 | 55.7 | 16 |
| 200 | Henderson, Drew | DOW_EAS1 | Sinker | 129 | 35 | 0.214 | 56.9 | 77.6 | 76.6 | 12.0% | 16.7% | 17.1% | 28.6% | 51.2 | 47.6 | 61.2 | 44.3 | 17 |
| 211 | McCartney, Seth | MIS_MUD | Sinker | 120 | 39 | 0.237 | 56.5 | 76.4 | 78.3 | 8.3% | 5.3% | 20.5% | 17.9% | 62.0 | 38.2 | 56.0 | 58.9 | 18 |
| 227 | Lawson, Nathan | FLO_Y'A | Sinker | 218 | 81 | 0.213 | 56.1 | 74.6 | 77.3 | 9.9% | 6.8% | 11.1% | 32.1% | 52.7 | 39.5 | 51.9 | 51.7 | 19 |
| 231 | Long, Maddox | WAS_WIL3 | Sinker | 285 | 84 | 0.233 | 55.8 | 74.1 | 78.6 | 15.4% | 17.8% | 15.5% | 23.8% | 64.5 | 48.5 | 57.4 | 60.7 | 20 |
| 236 | Fuenmayor, Liu | OTT_TIT | Sinker | 81 | 27 | 0.212 | 55.7 | 73.6 | 75.4 | 15.8% | 12.5% | 14.8% | 40.7% | 54.6 | 44.1 | 47.0 | 56.8 | 21 |
| 237 | Fritz, AJ | MIS_MUD | Sinker | 55 | 21 | 0.238 | 55.5 | 73.5 | 78.5 | 28.1% | 16.7% | 9.5% | 33.3% | 49.7 | 47.6 | 44.9 | 52.9 | 22 |
| 238 | Turner, Eric | JOL_SLA | Sinker | 113 | 39 | 0.210 | 55.5 | 73.3 | 77.1 | 15.4% | 8.8% | 17.9% | 28.2% | 46.0 | 41.1 | 49.2 | 46.2 | 23 |
| 264 | Milburn, Isaac | FLO_Y'A | Sinker | 109 | 38 | 0.231 | 54.6 | 70.4 | 77.6 | 15.1% | 3.0% | 23.7% | 23.7% | 61.0 | 36.4 | 55.5 | 58.2 | 24 |
| 270 | Kelly, Colin | SUS_COU1 | Sinker | 96 | 29 | 0.188 | 54.3 | 69.7 | 77.5 | 25.0% | 11.1% | 17.2% | 31.0% | 52.3 | 43.0 | 53.5 | 50.2 | 25 |

### Sliders

| Rank | Pitcher | Team | Pitch Type | Pitches | BBE | xwOBA | PVS 20-80 | PVS 0-100 | EV | Whiff% | K% | HardHit% | SweetSpot% | GB Score | K Score | LD Supp | FB Supp | Pitch Type Rank |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 2 | Vecerka, Boris | QUE_CAP | Slider | 83 | 18 | 0.123 | 80.0 | 99.9 | 69.1 | 25.9% | 38.9% | 5.6% | 16.7% | 59.0 | 65.7 | 54.3 | 56.8 | 1 |
| 3 | Carroll, Jake | JOL_SLA | Slider | 74 | 15 | 0.177 | 80.0 | 99.8 | 69.4 | 24.1% | 23.5% | 0.0% | 20.0% | 61.6 | 53.2 | 58.7 | 56.8 | 2 |
| 4 | Ryan, Dillon | NEW_ENG23 | Slider | 125 | 25 | 0.144 | 79.9 | 99.7 | 69.9 | 35.3% | 34.5% | 0.0% | 20.0% | 60.5 | 62.1 | 60.4 | 54.6 | 3 |
| 8 | Alpern, Liam | FLO_Y'A | Slider | 78 | 16 | 0.112 | 76.3 | 99.2 | 69.9 | 14.3% | 35.7% | 12.5% | 18.8% | 54.1 | 63.1 | 68.0 | 43.1 | 4 |
| 10 | Jones, Logan | TRI_VAL | Slider | 65 | 17 | 0.191 | 74.7 | 99.0 | 68.2 | 23.1% | 25.0% | 11.8% | 35.3% | 52.1 | 54.4 | 45.3 | 55.2 | 5 |
| 11 | Bauer, Patrick | QUE_CAP | Slider | 51 | 11 | 0.170 | 74.4 | 98.9 | 73.0 | 12.5% | 25.0% | 9.1% | 9.1% | 34.2 | 54.4 | 64.3 | 24.4 | 6 |
| 15 | Harper, Scott | NEW_YOR13 | Slider | 217 | 34 | 0.150 | 73.6 | 98.4 | 72.5 | 49.4% | 45.3% | 5.9% | 17.6% | 38.3 | 70.9 | 64.6 | 28.6 | 7 |
| 17 | Bargo, Casey | NEW_ENG23 | Slider | 56 | 16 | 0.176 | 73.5 | 98.2 | 74.6 | 28.0% | 40.0% | 0.0% | 12.5% | 68.7 | 66.6 | 59.8 | 63.6 | 8 |
| 18 | McEvoy, Aidan | FLO_Y'A | Slider | 119 | 30 | 0.153 | 72.5 | 98.1 | 72.8 | 40.7% | 34.2% | 6.7% | 20.0% | 40.8 | 61.9 | 58.7 | 34.9 | 9 |
| 22 | Leduc, Zachary | TRO_AIG | Slider | 87 | 15 | 0.128 | 71.7 | 97.6 | 71.0 | 45.5% | 36.8% | 13.3% | 26.7% | 56.4 | 64.0 | 58.7 | 51.3 | 10 |
| 23 | Kirby, Zach | WAS_WIL3 | Slider | 127 | 42 | 0.156 | 71.6 | 97.5 | 73.3 | 21.1% | 13.8% | 2.4% | 21.4% | 40.4 | 45.2 | 57.4 | 35.3 | 11 |
| 25 | Hickey, Matt | GAT_GRI | Slider | 89 | 26 | 0.206 | 70.5 | 97.3 | 72.3 | 23.1% | 12.5% | 11.5% | 19.2% | 65.0 | 44.1 | 61.0 | 58.9 | 12 |
| 28 | Donnan, Blake | FLO_Y'A | Slider | 65 | 10 | 0.186 | 70.0 | 97.0 | 71.5 | 51.7% | 52.9% | 10.0% | 30.0% | 43.4 | 77.2 | 49.9 | 43.1 | 13 |
| 32 | Nakata, Yuto | QUE_CAP | Slider | 107 | 24 | 0.161 | 68.9 | 96.5 | 75.2 | 34.1% | 29.6% | 0.0% | 20.8% | 59.0 | 58.2 | 59.8 | 53.4 | 14 |
| 33 | Duncan, Tanner | DOW_EAS1 | Slider | 64 | 10 | 0.174 | 68.9 | 96.4 | 77.4 | 50.0% | 27.8% | 10.0% | 0.0% | 80.0 | 56.6 | 76.2 | 67.7 | 15 |
| 43 | Balzan, Jackson | SUS_COU1 | Slider | 93 | 27 | 0.180 | 67.3 | 95.3 | 74.6 | 33.3% | 28.6% | 7.4% | 22.2% | 51.8 | 57.3 | 61.6 | 44.6 | 16 |
| 48 | Vega, Lucas | TRO_AIG | Slider | 134 | 36 | 0.156 | 66.6 | 94.7 | 75.6 | 26.8% | 28.6% | 5.6% | 19.4% | 39.5 | 57.3 | 54.3 | 36.2 | 17 |
| 49 | Jones, Logan | FLO_Y'A | Slider | 56 | 11 | 0.190 | 66.5 | 94.6 | 76.9 | 44.8% | 28.6% | 0.0% | 18.2% | 55.4 | 57.3 | 52.3 | 54.3 | 18 |
| 60 | Earwood, Micah | SUS_COU1 | Slider | 108 | 18 | 0.193 | 65.8 | 93.4 | 71.6 | 33.3% | 25.0% | 11.1% | 38.9% | 50.3 | 54.4 | 39.7 | 56.8 | 19 |
| 62 | Morin, Jacob | QUE_CAP | Slider | 85 | 20 | 0.207 | 65.7 | 93.1 | 73.4 | 30.6% | 30.4% | 10.0% | 30.0% | 47.3 | 58.8 | 56.5 | 43.1 | 20 |
| 68 | Perozzi, John | SUS_COU1 | Slider | 129 | 31 | 0.174 | 64.7 | 92.5 | 74.2 | 43.9% | 40.0% | 12.9% | 25.8% | 42.6 | 66.6 | 50.8 | 41.8 | 21 |
| 70 | Petschke, Ben | EVA_OTT | Slider | 144 | 42 | 0.185 | 64.5 | 92.2 | 75.2 | 18.5% | 25.7% | 9.5% | 23.8% | 57.1 | 54.9 | 54.3 | 54.8 | 22 |
| 76 | MacMillan, Blake | TRO_AIG | Slider | 106 | 13 | 0.210 | 63.9 | 91.6 | 73.9 | 56.1% | 63.6% | 23.1% | 23.1% | 62.0 | 80.0 | 45.9 | 65.2 | 23 |
| 82 | Moore, Kyle | SCH_BOO | Slider | 58 | 22 | 0.208 | 63.5 | 90.9 | 75.1 | 19.4% | 12.5% | 13.6% | 22.7% | 34.2 | 44.1 | 46.3 | 35.6 | 24 |
| 83 | Foster, Kobe | WAS_WIL3 | Slider | 144 | 37 | 0.184 | 63.4 | 90.8 | 74.3 | 32.2% | 29.7% | 13.5% | 27.0% | 43.2 | 58.2 | 54.9 | 39.8 | 25 |

### Curveballs

| Rank | Pitcher | Team | Pitch Type | Pitches | BBE | xwOBA | PVS 20-80 | PVS 0-100 | EV | Whiff% | K% | HardHit% | SweetSpot% | GB Score | K Score | LD Supp | FB Supp | Pitch Type Rank |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | Grounds, Jackson | DOW_EAS1 | Curveball | 82 | 10 | 0.107 | 80.0 | 100.0 | 64.6 | 42.1% | 41.2% | 0.0% | 0.0% | 59.0 | 67.6 | 76.2 | 43.1 | 1 |
| 6 | Morgan, Cooper | QUE_CAP | Curveball | 85 | 26 | 0.149 | 78.0 | 99.4 | 65.8 | 35.4% | 42.9% | 7.7% | 42.3% | 44.0 | 69.0 | 56.0 | 39.9 | 2 |
| 21 | Bohnert, Matthew | WIN_CIT29 | Curveball | 98 | 12 | 0.143 | 71.8 | 97.8 | 75.1 | 46.2% | 47.4% | 8.3% | 8.3% | 65.5 | 72.7 | 76.2 | 49.9 | 3 |
| 36 | Jones, Breyln | NEW_JER6 | Curveball | 60 | 12 | 0.186 | 68.4 | 96.1 | 76.4 | 29.2% | 38.9% | 0.0% | 16.7% | 59.0 | 65.7 | 76.2 | 43.1 | 4 |
| 39 | Hickey, Matt | GAT_GRI | Curveball | 65 | 15 | 0.179 | 68.1 | 95.7 | 75.7 | 24.0% | 28.6% | 6.7% | 13.3% | 66.8 | 57.3 | 58.7 | 62.2 | 5 |
| 45 | Garcia, Brett | OTT_TIT | Curveball | 121 | 20 | 0.174 | 67.2 | 95.1 | 76.6 | 34.1% | 48.1% | 10.0% | 10.0% | 62.9 | 73.3 | 69.7 | 51.3 | 6 |
| 46 | Hohenstein, Liam | WIN_CIT29 | Curveball | 106 | 20 | 0.160 | 67.1 | 94.9 | 72.9 | 28.1% | 10.5% | 0.0% | 35.0% | 39.5 | 42.5 | 49.9 | 39.0 | 7 |
| 50 | Gregory, Ben | GAT_GRI | Curveball | 53 | 14 | 0.226 | 66.5 | 94.5 | 72.6 | 25.0% | 22.2% | 14.3% | 28.6% | 75.7 | 52.1 | 48.0 | 78.3 | 8 |
| 52 | Salata, Derek | SCH_BOO | Curveball | 122 | 25 | 0.195 | 66.3 | 94.3 | 73.9 | 37.3% | 43.8% | 8.0% | 28.0% | 54.3 | 69.7 | 49.9 | 54.6 | 9 |
| 54 | Binns, Malik | NEW_JER6 | Curveball | 55 | 13 | 0.185 | 66.2 | 94.0 | 73.8 | 27.3% | 13.3% | 7.7% | 30.8% | 62.0 | 44.8 | 56.0 | 58.9 | 10 |
| 56 | Heredia-Bustos, Rolando | DOW_EAS1 | Curveball | 75 | 18 | 0.177 | 66.2 | 93.8 | 73.1 | 33.3% | 23.1% | 16.7% | 22.2% | 46.0 | 52.8 | 47.0 | 47.6 | 11 |
| 67 | Eisenbarger, Jack | QUE_CAP | Curveball | 93 | 13 | 0.212 | 64.7 | 92.6 | 72.2 | 28.6% | 33.3% | 15.4% | 38.5% | 50.0 | 61.2 | 45.9 | 52.6 | 12 |
| 72 | Townes, Holland | SCH_BOO | Curveball | 90 | 13 | 0.211 | 64.1 | 92.0 | 75.0 | 48.3% | 56.5% | 15.4% | 23.1% | 56.0 | 80.0 | 45.9 | 58.9 | 13 |
| 73 | Harris, Ben | GAT_GRI | Curveball | 278 | 26 | 0.215 | 64.1 | 91.9 | 76.6 | 37.3% | 58.3% | 11.5% | 19.2% | 59.0 | 80.0 | 50.9 | 58.9 | 14 |
| 79 | Cook, Cole | SCH_BOO | Curveball | 116 | 22 | 0.196 | 63.6 | 91.2 | 75.1 | 40.0% | 44.8% | 18.2% | 22.7% | 59.0 | 70.6 | 58.3 | 54.3 | 15 |
| 90 | Majick, Eli | NEW_ENG23 | Curveball | 52 | 14 | 0.185 | 63.0 | 90.0 | 76.6 | 14.3% | 23.1% | 0.0% | 28.6% | 53.4 | 52.8 | 48.0 | 54.8 | 16 |
| 97 | Hill, Kaleb | OTT_TIT | Curveball | 247 | 58 | 0.206 | 62.6 | 89.2 | 74.7 | 28.0% | 18.0% | 12.1% | 27.6% | 63.0 | 48.7 | 49.0 | 64.3 | 17 |
| 104 | Wiltse, Ryan | EVA_OTT | Curveball | 146 | 17 | 0.217 | 61.6 | 88.4 | 78.0 | 35.5% | 36.4% | 17.6% | 11.8% | 75.0 | 63.7 | 60.7 | 69.6 | 18 |
| 110 | Scafidi, Christian | LAK_ERI24 | Curveball | 59 | 12 | 0.193 | 61.2 | 87.7 | 75.7 | 22.2% | 46.2% | 8.3% | 33.3% | 72.0 | 71.7 | 43.3 | 77.3 | 19 |
| 111 | Hampton, Ky | OTT_TIT | Curveball | 52 | 15 | 0.176 | 61.1 | 87.6 | 73.2 | 15.0% | 28.6% | 13.3% | 40.0% | 56.4 | 57.3 | 41.1 | 62.2 | 20 |
| 120 | Earwood, Micah | SUS_COU1 | Curveball | 218 | 38 | 0.235 | 60.5 | 86.6 | 75.6 | 35.6% | 34.5% | 15.8% | 28.9% | 59.0 | 62.1 | 48.5 | 60.4 | 21 |
| 156 | Lefebvre, Charles | TRO_AIG | Curveball | 99 | 24 | 0.246 | 58.6 | 82.6 | 76.7 | 32.5% | 42.3% | 4.2% | 37.5% | 52.5 | 68.5 | 48.8 | 53.4 | 22 |
| 171 | Vail, Tyler | NEW_YOR13 | Curveball | 186 | 23 | 0.220 | 58.1 | 80.9 | 80.4 | 34.6% | 31.2% | 4.3% | 21.7% | 67.4 | 59.5 | 53.3 | 66.3 | 23 |
| 173 | Gollert, Harley | TRO_AIG | Curveball | 86 | 21 | 0.224 | 58.0 | 80.7 | 78.8 | 32.4% | 10.0% | 4.8% | 23.8% | 64.5 | 42.1 | 51.2 | 64.6 | 24 |
| 174 | Boies, Emiles | QUE_CAP | Curveball | 91 | 22 | 0.187 | 58.0 | 80.5 | 76.3 | 33.3% | 11.8% | 22.7% | 22.7% | 62.5 | 43.5 | 58.3 | 58.0 | 25 |

### Changeups

| Rank | Pitcher | Team | Pitch Type | Pitches | BBE | xwOBA | PVS 20-80 | PVS 0-100 | EV | Whiff% | K% | HardHit% | SweetSpot% | GB Score | K Score | LD Supp | FB Supp | Pitch Type Rank |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 5 | Zentko, Dylan | EVA_OTT | Changeup | 67 | 13 | 0.155 | 78.5 | 99.6 | 70.2 | 44.8% | 35.7% | 7.7% | 15.4% | 68.0 | 63.1 | 56.0 | 65.2 | 1 |
| 7 | Peyton, Blake | GAT_GRI | Changeup | 93 | 20 | 0.140 | 77.2 | 99.3 | 70.1 | 37.5% | 15.4% | 5.0% | 20.0% | 70.7 | 46.5 | 56.5 | 67.7 | 2 |
| 9 | Serrano, Elio | NEW_JER6 | Changeup | 63 | 15 | 0.148 | 75.9 | 99.1 | 70.0 | 35.1% | 21.4% | 6.7% | 26.7% | 51.2 | 51.4 | 58.7 | 45.8 | 3 |
| 19 | Lawson, Nathan | FLO_Y'A | Changeup | 68 | 22 | 0.194 | 72.4 | 98.0 | 73.5 | 23.5% | 30.0% | 4.5% | 18.2% | 48.3 | 58.5 | 64.3 | 39.4 | 4 |
| 29 | Harris, Everette | TRI_VAL | Changeup | 96 | 27 | 0.168 | 69.6 | 96.9 | 74.3 | 15.9% | 7.1% | 7.4% | 14.8% | 66.2 | 39.8 | 56.7 | 62.9 | 5 |
| 31 | Escobar, Anthony | TRO_AIG | Changeup | 162 | 41 | 0.165 | 69.2 | 96.6 | 74.4 | 41.8% | 27.3% | 12.2% | 14.6% | 50.4 | 56.2 | 63.4 | 42.1 | 6 |
| 35 | Parsons, Billy | SUS_COU1 | Changeup | 61 | 17 | 0.234 | 68.4 | 96.2 | 74.2 | 28.1% | 41.2% | 5.9% | 23.5% | 80.0 | 67.6 | 68.5 | 74.5 | 7 |
| 37 | Rodriguez, Joe Joe | NEW_JER6 | Changeup | 144 | 22 | 0.167 | 68.2 | 96.0 | 76.0 | 52.8% | 38.7% | 0.0% | 18.2% | 55.4 | 65.6 | 64.3 | 46.8 | 8 |
| 38 | Wiltse, Ryan | EVA_OTT | Changeup | 165 | 48 | 0.195 | 68.1 | 95.8 | 73.2 | 35.2% | 29.4% | 6.2% | 29.2% | 60.6 | 58.0 | 48.8 | 61.9 | 9 |
| 42 | Smith, Ben | NEW_ENG23 | Changeup | 56 | 15 | 0.151 | 67.4 | 95.4 | 77.2 | 20.8% | 7.1% | 6.7% | 6.7% | 61.6 | 39.8 | 76.2 | 45.8 | 10 |
| 53 | Messina, Chris | FDU_KNI | Changeup | 68 | 16 | 0.253 | 66.3 | 94.2 | 75.3 | 16.7% | 5.9% | 6.2% | 18.8% | 68.7 | 38.7 | 68.0 | 58.5 | 11 |
| 58 | Leak, Anthony | NEW_YOR13 | Changeup | 77 | 18 | 0.192 | 66.0 | 93.6 | 76.8 | 28.1% | 6.2% | 0.0% | 16.7% | 59.0 | 39.0 | 68.9 | 47.6 | 12 |
| 66 | Drakeford, Dosie | NEW_JER6 | Changeup | 84 | 15 | 0.158 | 64.7 | 92.7 | 73.9 | 56.8% | 54.2% | 0.0% | 40.0% | 46.0 | 78.2 | 32.4 | 56.8 | 13 |
| 78 | Earwood, Micah | SUS_COU1 | Changeup | 211 | 29 | 0.185 | 63.7 | 91.3 | 73.2 | 20.0% | 0.0% | 6.9% | 37.9% | 60.3 | 33.9 | 58.1 | 55.8 | 14 |
| 81 | Campbell, Tyler | MIS_MUD | Changeup | 115 | 33 | 0.205 | 63.6 | 91.0 | 76.6 | 29.4% | 21.4% | 6.1% | 21.2% | 36.5 | 51.4 | 60.3 | 29.4 | 15 |
| 84 | Tokar, Heitor | OTT_TIT | Changeup | 74 | 26 | 0.206 | 63.3 | 90.7 | 75.0 | 16.7% | 9.5% | 11.5% | 26.9% | 53.0 | 41.7 | 56.0 | 49.4 | 16 |
| 86 | Sesar, Jorden | SUS_COU1 | Changeup | 80 | 26 | 0.167 | 63.2 | 90.4 | 74.7 | 25.6% | 26.3% | 7.7% | 34.6% | 44.0 | 55.4 | 45.9 | 46.2 | 17 |
| 88 | Miner, Jace | DOW_EAS1 | Changeup | 156 | 36 | 0.217 | 63.2 | 90.2 | 74.6 | 28.8% | 17.6% | 11.1% | 27.8% | 52.5 | 48.4 | 54.3 | 49.9 | 18 |
| 94 | Morgan, Cooper | QUE_CAP | Changeup | 86 | 24 | 0.199 | 62.8 | 89.5 | 75.0 | 30.8% | 25.0% | 4.2% | 33.3% | 46.0 | 54.4 | 54.3 | 43.1 | 19 |
| 100 | Maietta, Dante | WIN_CIT29 | Changeup | 283 | 54 | 0.191 | 62.1 | 88.9 | 77.4 | 40.7% | 33.3% | 5.6% | 22.2% | 50.3 | 61.2 | 56.7 | 46.1 | 20 |
| 113 | Willeman, Landon | EVA_OTT | Changeup | 179 | 57 | 0.202 | 61.0 | 87.4 | 76.5 | 25.0% | 16.7% | 14.0% | 22.8% | 61.0 | 47.6 | 57.8 | 56.8 | 21 |
| 116 | Barreto, Brayhans | TRI_VAL | Changeup | 122 | 26 | 0.224 | 60.8 | 87.1 | 75.8 | 38.6% | 15.2% | 7.7% | 30.8% | 53.0 | 46.3 | 50.9 | 52.6 | 22 |
| 123 | Pardinho, Eric | OTT_TIT | Changeup | 141 | 25 | 0.219 | 60.5 | 86.3 | 73.8 | 47.9% | 53.7% | 16.0% | 40.0% | 63.6 | 77.8 | 44.6 | 67.7 | 23 |
| 125 | Plumadore, Carson | WIN_CIT29 | Changeup | 272 | 76 | 0.196 | 60.5 | 86.1 | 75.8 | 29.0% | 20.3% | 9.2% | 30.3% | 44.6 | 50.5 | 60.6 | 37.7 | 24 |
| 126 | Hensey, Rob | SUS_COU1 | Changeup | 277 | 63 | 0.212 | 60.4 | 85.9 | 77.4 | 44.2% | 41.0% | 12.7% | 20.6% | 72.0 | 67.4 | 57.4 | 68.5 | 25 |

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