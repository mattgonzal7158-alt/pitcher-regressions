# Current Pitch Value Run Summary

- Run time: 2026-07-05 13:24:27
- Raw input: `data\raw\2026-data.parquet`
- Qualified raw Pitch Value rows: 744
- Final scouting leaderboard rows: 13,372

## Start Here

- `reports/final_scouting_leaderboards.md`
- `data/processed/current_best_overall_pitches.csv`
- `data/processed/current_top_pitch_value_scores.csv`
- `data/processed/master_pitch_evaluation_table_v2.csv`

## Quick Exports

- Top 100 raw Pitch Value Scores: `data\processed\current_top_pitch_value_scores.csv`
- Top 25 raw Pitch Value Scores by pitch type: `data\processed\current_top_pitch_value_by_type.csv`
- Best overall final pitch scores: `data\processed\current_best_overall_pitches.csv`
- Best pitcher-pitch rows: `data\processed\current_best_pitcher_pitches.csv`

## Top 20 Overall Pitches

| leaderboard_rank | pitcher_name | pitcher_team | pitch_type | batter_side | pitch_count | final_pitch_score_20_80 | raw_pitch_score_20_80 | location_score_20_80 | stuff_plus_20_80 | execution_plus_20_80 |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | Vecerka, Boris | QUE_CAP | Slider | R | 48 | 75.1 | 80.0 | 63.7 | 67.9 | 78.6 |
| 2 | Ryan, Dillon | NEW_ENG23 | Slider | R | 54 | 74.4 | 79.2 | 63.0 | 62.6 | 79.8 |
| 3 | Harper, Scott | NEW_YOR13 | Slider | R | 143 | 74.0 | 76.7 | 67.5 | 80.0 | 70.7 |
| 4 | Kirby, Zach | WAS_WIL3 | Slider | R | 126 | 73.6 | 70.9 | 80.0 | 72.6 | 74.4 |
| 5 | Bargo, Casey | NEW_ENG23 | Slider | R | 29 | 73.0 | 72.8 | 73.7 | 59.4 | 79.3 |
| 6 | Moore, Kyle | SCH_BOO | Slider | R | 31 | 72.5 | 70.4 | 77.5 | 42.2 | 80.0 |
| 7 | Grounds, Jackson | DOW_EAS1 | Curveball | R | 43 | 72.5 | 80.0 | 54.8 | 53.4 | 80.0 |
| 8 | Grounds, Jackson | DOW_EAS1 | Four-Seam | R | 48 | 72.2 | 73.5 | 69.3 | 49.0 | 80.0 |
| 9 | Lawson, Nathan | FLO_Y'A | Changeup | L | 33 | 72.0 | 77.0 | 60.6 | 58.4 | 78.3 |
| 10 | Morgan, Cooper | QUE_CAP | Curveball | L | 44 | 72.0 | 80.0 | 53.3 | 50.0 | 80.0 |
| 11 | Alpern, Liam | FLO_Y'A | Slider | L | 38 | 71.4 | 75.5 | 61.8 | 64.5 | 74.7 |
| 12 | Carroll, Jake | JOL_SLA | Slider | L | 46 | 70.9 | 80.0 | 49.8 | 68.0 | 72.5 |
| 13 | Davis, Tyler | WIN_CIT29 | Four-Seam | R | 33 | 70.8 | 73.6 | 64.2 | 53.5 | 78.6 |
| 14 | Ryan, Dillon | NEW_ENG23 | Slider | L | 59 | 70.0 | 79.2 | 48.5 | 62.6 | 73.6 |
| 15 | Cameron, Zach | WIN_CIT29 | Four-Seam | R | 50 | 69.8 | 70.9 | 67.1 | 43.9 | 80.0 |
| 16 | Rodriguez, Joe Joe | NEW_JER6 | Changeup | L | 59 | 69.8 | 74.8 | 58.1 | 53.7 | 77.1 |
| 17 | Grounds, Jackson | DOW_EAS1 | Curveball | L | 39 | 69.5 | 80.0 | 45.0 | 53.4 | 76.8 |
| 18 | Peyton, Blake | GAT_GRI | Changeup | R | 84 | 69.2 | 76.4 | 52.7 | 47.6 | 79.0 |
| 19 | Escobar, Anthony | TRO_AIG | Changeup | L | 100 | 69.0 | 72.0 | 61.9 | 62.2 | 72.3 |
| 20 | Harper, Scott | NEW_YOR13 | Slider | L | 31 | 69.0 | 76.7 | 50.9 | 80.0 | 63.6 |

## Qualified Pitch Value Rows by Pitch Type

| Pitch Type | Rows |
|---|---:|
| `Changeup` | 111 |
| `Curveball` | 72 |
| `Cutter` | 31 |
| `Four-Seam` | 241 |
| `Sinker` | 121 |
| `Slider` | 156 |
| `Splitter` | 12 |