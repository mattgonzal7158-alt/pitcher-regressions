# Current Pitch Value Run Summary

- Run time: 2026-07-14 15:24:48
- Raw input: `data\raw\2026-data.parquet`
- Qualified raw Pitch Value rows: 853
- Final scouting leaderboard rows: 15,486

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
| 1 | Ryan, Dillon | NEW_ENG23 | Slider | R | 61 | 76.7 | 79.9 | 69.2 | 65.2 | 80.0 |
| 2 | Kirby, Zach | WAS_WIL3 | Slider | R | 126 | 74.2 | 71.7 | 80.0 | 70.9 | 76.3 |
| 3 | Bargo, Casey | NEW_ENG23 | Slider | R | 29 | 74.1 | 73.6 | 75.5 | 60.9 | 80.0 |
| 4 | Grounds, Jackson | DOW_EAS1 | Curveball | R | 43 | 73.3 | 80.0 | 57.6 | 59.8 | 79.2 |
| 5 | Moore, Kyle | SCH_BOO | Slider | R | 31 | 72.8 | 71.2 | 76.5 | 46.5 | 80.0 |
| 6 | Grounds, Jackson | DOW_EAS1 | Four-Seam | R | 48 | 72.6 | 74.4 | 68.5 | 49.8 | 80.0 |
| 7 | Vecerka, Boris | QUE_CAP | Slider | R | 53 | 72.5 | 77.6 | 60.8 | 69.8 | 74.3 |
| 8 | Lawson, Nathan | FLO_Y'A | Changeup | L | 40 | 72.5 | 78.2 | 59.1 | 58.9 | 78.4 |
| 9 | Alpern, Liam | FLO_Y'A | Slider | L | 38 | 72.0 | 76.4 | 61.5 | 60.2 | 77.2 |
| 10 | Zentko, Dylan | EVA_OTT | Changeup | R | 57 | 71.8 | 78.6 | 56.1 | 56.7 | 78.4 |
| 11 | Hickey, Matt | GAT_GRI | Slider | R | 71 | 71.7 | 73.5 | 67.5 | 63.2 | 75.7 |
| 12 | Harper, Scott | NEW_YOR13 | Slider | R | 166 | 71.5 | 72.6 | 69.1 | 80.0 | 68.5 |
| 13 | Leduc, Zachary | TRO_AIG | Slider | R | 46 | 71.5 | 79.2 | 53.6 | 64.1 | 75.1 |
| 14 | Davis, Tyler | WIN_CIT29 | Four-Seam | R | 33 | 71.5 | 74.4 | 64.7 | 53.7 | 79.0 |
| 15 | Ryan, Dillon | NEW_ENG23 | Slider | L | 64 | 71.3 | 79.9 | 51.3 | 65.2 | 74.5 |
| 16 | Morgan, Cooper | QUE_CAP | Curveball | L | 56 | 71.2 | 80.0 | 50.8 | 45.8 | 80.0 |
| 17 | Leduc, Zachary | TRO_AIG | Slider | L | 32 | 71.0 | 79.2 | 52.0 | 64.1 | 74.4 |
| 18 | Peyton, Blake | GAT_GRI | Changeup | R | 90 | 70.8 | 77.3 | 55.5 | 47.5 | 80.0 |
| 19 | Escobar, Anthony | TRO_AIG | Changeup | L | 142 | 70.4 | 72.7 | 65.0 | 63.1 | 73.9 |
| 20 | Carroll, Jake | JOL_SLA | Slider | L | 50 | 70.3 | 80.0 | 47.8 | 60.9 | 74.7 |

## Qualified Pitch Value Rows by Pitch Type

| Pitch Type | Rows |
|---|---:|
| `Changeup` | 123 |
| `Curveball` | 90 |
| `Cutter` | 38 |
| `Four-Seam` | 262 |
| `Sinker` | 141 |
| `Slider` | 185 |
| `Splitter` | 14 |