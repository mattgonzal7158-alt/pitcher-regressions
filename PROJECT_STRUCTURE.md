# Project Structure

## Folders

| Folder | Contents |
|---|---|
| `data/raw/` | Original source parquet files. |
| `data/processed/` | Generated parquet and CSV analysis outputs. |
| `reports/` | Markdown reports and methodology notes. |
| `plots/` | Generated figures, grouped by analysis step. |
| `scripts/` | Reproducible Python scripts for each analysis step. |
| `paper_research/` | Standalone paper modules, each with its own scripts, data, reports, and plots. |
| `paper_research/paper_1_movement_vs_location/` | Self-contained paper regression workflow comparing movement quality and location value. |
| `archive/duplicates/` | Older duplicate outputs kept for reference instead of deleting. |
| `archive/cache/` | Moved generated Python cache files. |

## Paper Research Modules

Paper-specific work is grouped under matching subfolders so it is easy to find without mixing it into the main scoring pipeline.

| Paper module | Scripts | Data outputs | Reports | Plots |
|---|---|---|---|---|
| Paper 1: Movement vs Location Regression | `paper_research/paper_1_movement_vs_location/scripts/` | `paper_research/paper_1_movement_vs_location/data/` | `paper_research/paper_1_movement_vs_location/reports/` | `paper_research/paper_1_movement_vs_location/plots/` |

Start here for Paper 1:

- `paper_research/paper_1_movement_vs_location/README.md`
- `paper_research/paper_1_movement_vs_location/scripts/run_all_paper_1.py`
- `paper_research/paper_1_movement_vs_location/reports/paper_results_summary.md`

## Main Reports

| Report | Purpose |
|---|---|
| `reports/FRONTIER_PITCH_VALUE_METHODOLOGY.md` | Full methodology and interpretation guide. |
| `reports/pitch_value_score_leaderboards.md` | Pitch Value Score leaderboards. |
| `reports/pitch_value_movement_report.md` | Movement regression and correlation results. |
| `reports/pitch_movement_archetype_report.md` | Movement archetypes, undervalued pitches, and scouting notes. |
| `reports/location_score_report.md` | Location Score leaderboards by pitcher, pitch type, and batter side. |
| `reports/pitch_leaderboard_splits.md` | Handedness-specific final pitch leaderboards blending Pitch Value and Location Score. |
| `reports/platoon_weapon_report.md` | Platoon gap analysis identifying one-sided and balanced pitch weapons. |
| `reports/master_pitch_evaluation_table_report.md` | Master table inventory, warnings, and top final pitch score summaries. |
| `reports/stuff_plus_report.md` | Movement/release-only Stuff+ model summaries, importance tables, and leaderboards. |
| `reports/execution_plus_report.md` | Execution+ quadrants comparing actual final scores to movement-based expectations. |
| `reports/master_pitch_evaluation_table_v2_report.md` | Master v2 join report after adding Stuff+ and Execution+ fields. |
| `reports/final_scouting_leaderboards.md` | Final scouting leaderboards across overall, split, Stuff+, Execution+, location, and weapon categories. |

## Canonical Data Outputs

| File | Purpose |
|---|---|
| `data/processed/2026-data-with-woba-xwoba.parquet` | Main enriched pitch-level dataset with `woba_value` and `xwoba_frontier`. |
| `data/processed/pitcher_pitch_type_xwoba_metrics.csv` | Pitcher + pitch type metrics used for scoring. |
| `data/processed/pitch_value_scores_with_type_rank.csv` | Current normalized Pitch Value Score table. |
| `data/processed/pitch_value_scores.csv` | Canonical filename; may be stale if open/locked during regeneration. |
| `data/processed/pitch_value_movement_model_data.csv` | Pitch Value Score joined to movement traits. |
| `data/processed/pitch_movement_archetypes.csv` | Clustered movement archetype table. |
| `data/processed/location_value_grid.csv` | Location Value grid by pitch type, batter side, and 0.25 ft plate-location bin. |
| `data/processed/location_scores.csv` | Pitcher + pitch type + batter side Location Scores. |
| `data/processed/pitch_leaderboard_splits.csv` | Handedness-specific final pitch leaderboard table. |
| `data/processed/platoon_weapon_scores.csv` | Pitcher + pitch type platoon gaps comparing final scores vs RHH and LHH. |
| `data/processed/master_pitch_evaluation_table.csv` | Consolidated pitch evaluation table at pitcher + pitch type + batter side level. |
| `data/processed/stuff_plus_scores.csv` | Movement/release-only Stuff+ predictions and rankings. |
| `data/processed/execution_plus_scores.csv` | Execution+ scores and quadrant labels comparing final score to Stuff+ expectation. |
| `data/processed/master_pitch_evaluation_table_v2.csv` | Master pitch table with Stuff+ and Execution+ fields added. |
| `data/processed/final_scouting_leaderboards.csv` | Long-form export of the final scouting leaderboard sections. |
| `paper_research/paper_1_movement_vs_location/data/regression_dataset.csv` | Paper regression analysis dataset at pitcher + pitch type + batter side level. |
| `paper_research/paper_1_movement_vs_location/data/main_regression_results.csv` | Main regression coefficients and model statistics. |
| `paper_research/paper_1_movement_vs_location/data/diagnostic_tests.csv` | Regression diagnostic test results by dependent variable. |
| `paper_research/paper_1_movement_vs_location/data/robustness_results.csv` | Robustness regression coefficients and model statistics. |

## Pitch Value Score Inputs

Pitch Value Score is created by `scripts/create_pitch_value_score.py` from `data/processed/pitcher_pitch_type_xwoba_metrics.csv`. Each scored row is one pitcher + normalized pitch type combination, filtered to at least 50 pitches and at least 10 tracked batted balls.

The score uses these standardized pitcher-pitch type metrics:

| Metric | Role in score |
|---|---|
| `whiff_pct` | Miss bat outcome metric. |
| `csw_pct` | Called-strike plus whiff outcome metric. |
| `putaway_pct` | Two-strike finishing metric. |
| `k_pct` | Plate-appearance finishing metric. |
| `avg_exit_velocity` | Contact-quality damage metric. |
| `hardhit_pct` | Contact-quality damage metric. |
| `barrel_pct` | Contact-quality damage metric. |
| `sweetspot_pct` | Productive-launch contact metric. |

Each metric is z-scored across qualified pitcher-pitch type rows, multiplied by its standardized coefficient from the `xwoba_frontier` regression, then sign-flipped so lower expected damage produces a higher score:

```text
pitch_value_raw = -sum(standardized_coefficient * metric_z)
```

The raw score is then scaled into `pitch_value_20_80` and percentile-ranked as `pitch_value_0_100`. The full explanation and coefficient table live in `reports/FRONTIER_PITCH_VALUE_METHODOLOGY.md` and `reports/pitch_value_score_leaderboards.md`.

## Location Value

Location Value is created by `scripts/create_location_value.py` from the existing enriched pitch-level dataset. It does not rebuild xwOBA or Pitch Value Score.

The analysis builds separate 0.25 foot location grids for each normalized `pitch_type` and `batter_side` combination. Each cell stores:

| Column | Meaning |
|---|---|
| `cell_count` | Number of pitches in that pitch type + batter side + location bin. |
| `xwoba_observation_count` | Number of cell pitches with non-null `xwoba_frontier`. |
| `cell_avg_xwoba` | Raw average `xwoba_frontier` in the cell, ignoring missing xwOBA values. |
| `pitch_type_batter_side_avg` | League average `xwoba_frontier` for the exact pitch type and batter side. |
| `smoothed_xwoba` | Empirical Bayes blend of the cell average and pitch type + batter side average, with weight 100. |
| `location_value` | `pitch_type_batter_side_avg - smoothed_xwoba`; positive means the location is better than average for that pitch type and batter side. |
| `location_value_per_100` | Same value scaled by 100 for easier heatmap reading. |

Outputs:

- `data/processed/location_value_grid.csv`
- `plots/location_value/`

## Location Score

Location Score is created by `scripts/create_location_score.py` from the existing enriched pitch-level dataset and `data/processed/location_value_grid.csv`. It assigns each pitch to its matching Location Value grid cell, then aggregates by pitcher, normalized pitch type, and batter side.

The pitch-level value is:

```text
location_advantage = league_average_pitch_type_side_xwoba - grid_xwoba
```

Positive values mean the pitch was thrown to a better-than-average location for that exact pitch type and batter side. Rows are scored with a minimum of 25 assigned pitches.

Outputs:

- `data/processed/location_scores.csv`
- `reports/location_score_report.md`

## Split Pitch Leaderboards

Split pitch leaderboards are created by `scripts/create_split_pitch_leaderboards.py` from `data/processed/pitch_value_scores_with_type_rank.csv` and `data/processed/location_scores.csv`.

The final score blends overall pitch quality with handedness-specific location quality:

```text
final_pitch_score = 0.70 * pitch_value_20_80 + 0.30 * location_score_20_80
```

Pitch Value is pitcher + pitch type level, while Location Score supplies the batter-side split. The output includes overall rank, pitch type rank, and pitch type + batter side rank.

Outputs:

- `data/processed/pitch_leaderboard_splits.csv`
- `reports/pitch_leaderboard_splits.md`

## Platoon Weapons

Platoon weapon analysis is created by `scripts/analyze_platoon_weapons.py` from `data/processed/pitch_leaderboard_splits.csv`. It compares each pitcher + pitch type final score against RHH and LHH.

The platoon gap is:

```text
platoon_gap = final_pitch_score_vs_rhh - final_pitch_score_vs_lhh
```

Positive gaps point to better performance versus RHH; negative gaps point to better performance versus LHH. Categories include Balanced Weapon, Right-Handed Killer, Left-Handed Killer, and Reverse Split Weapon.

Outputs:

- `data/processed/platoon_weapon_scores.csv`
- `reports/platoon_weapon_report.md`

## Master Pitch Evaluation Table

The master table is created by `scripts/create_master_pitch_evaluation_table.py` from existing processed outputs only. It uses `data/processed/pitch_leaderboard_splits.csv` as the pitcher + pitch type + batter side spine when available, then joins Pitch Value, Location Score, Platoon Weapon, movement, and archetype fields.

Outputs:

- `data/processed/master_pitch_evaluation_table.csv`
- `reports/master_pitch_evaluation_table_report.md`

## Stuff+ Model

Stuff+ is created by `scripts/create_stuff_plus_model.py` from `data/processed/master_pitch_evaluation_table.csv`. It predicts `final_pitch_score_20_80` using only movement and release traits:

- IVB
- HB
- velocity
- spin rate
- extension
- release height
- release side

Pitch types with at least 30 pitcher + pitch type + batter side rows receive pitch-type-specific models. Smaller pitch types use a fallback pooled model with pitch type fixed effects. Predictors are standardized before modeling.

Outputs:

- `data/processed/stuff_plus_scores.csv`
- `reports/stuff_plus_report.md`

## Execution+

Execution+ is created by `scripts/create_execution_plus.py` from `data/processed/master_pitch_evaluation_table.csv` and `data/processed/stuff_plus_scores.csv`.

It compares actual final pitch quality against movement/release-only expected quality:

```text
execution_raw = final_pitch_score_20_80 - stuff_plus_raw
```

Quadrants:

- Elite Weapon: high Stuff+, high Execution+
- Development Target: high Stuff+, low Execution+
- Command/Deception Weapon: low Stuff+, high Execution+
- Low Priority: low Stuff+, low Execution+

Outputs:

- `data/processed/execution_plus_scores.csv`
- `reports/execution_plus_report.md`

## Master Pitch Evaluation Table v2

The v2 master table is created by `scripts/update_master_with_stuff_execution.py` from the original master table, Stuff+ scores, and Execution+ scores. It preserves the original master table and writes a new version with:

- `stuff_plus_raw`
- `stuff_plus_20_80`
- `stuff_plus_0_100`
- `execution_raw`
- `execution_plus_20_80`
- `execution_plus_0_100`
- `quadrant_label`

Outputs:

- `data/processed/master_pitch_evaluation_table_v2.csv`
- `reports/master_pitch_evaluation_table_v2_report.md`

## Final Scouting Leaderboards

Final scouting leaderboards are created by `scripts/create_final_scouting_leaderboards.py` from `data/processed/master_pitch_evaluation_table_v2.csv`. They collect best overall pitches, Stuff+, Execution+, location, handedness splits, development targets, balanced weapons, and one-side weapons.

Outputs:

- `data/processed/final_scouting_leaderboards.csv`
- `reports/final_scouting_leaderboards.md`

## Paper 1: Movement vs Location Regression

The first paper regression section is self-contained in `paper_research/paper_1_movement_vs_location/`. It uses existing project outputs only and does not rebuild the Frontier xwOBA model, Pitch Value Score, Location Value grids, movement archetypes, Stuff+, Execution+, or scouting leaderboards.

The analysis asks how much pitch movement quality and location score explain pitch outcomes at the pitcher + pitch type + batter side level. Dependent variables are:

- `xwoba_frontier`
- `woba_value`
- `whiff_pct`
- `hardhit_pct`

Core predictors are:

- `movement_quality_20_80`
- `location_score_20_80`

Controls and fixed effects include pitch count, batted-ball count, pitch type, and batter side where specified. The workflow also produces regression diagnostics, robustness checks, publication-style tables, and figures.

Scripts:

- `paper_research/paper_1_movement_vs_location/scripts/01_create_regression_dataset.py`
- `paper_research/paper_1_movement_vs_location/scripts/02_run_main_regressions.py`
- `paper_research/paper_1_movement_vs_location/scripts/03_regression_diagnostics.py`
- `paper_research/paper_1_movement_vs_location/scripts/04_robustness_checks.py`
- `paper_research/paper_1_movement_vs_location/scripts/05_create_tables_and_figures.py`
- `paper_research/paper_1_movement_vs_location/scripts/06_create_paper_results_summary.py`
- `paper_research/paper_1_movement_vs_location/scripts/run_all_paper_1.py`

Outputs:

- `paper_research/paper_1_movement_vs_location/data/regression_dataset.csv`
- `paper_research/paper_1_movement_vs_location/data/main_regression_results.csv`
- `paper_research/paper_1_movement_vs_location/data/diagnostic_tests.csv`
- `paper_research/paper_1_movement_vs_location/data/robustness_results.csv`
- `paper_research/paper_1_movement_vs_location/reports/regression_dataset_summary.md`
- `paper_research/paper_1_movement_vs_location/reports/main_regression_results.md`
- `paper_research/paper_1_movement_vs_location/reports/regression_diagnostics.md`
- `paper_research/paper_1_movement_vs_location/reports/robustness_checks.md`
- `paper_research/paper_1_movement_vs_location/reports/paper_tables_and_figures.md`
- `paper_research/paper_1_movement_vs_location/reports/paper_results_summary.md`
- `paper_research/paper_1_movement_vs_location/plots/`
- `paper_research/paper_1_movement_vs_location/plots/diagnostics/`

## Reproduction Order

Run from the project root:

```powershell
uv run python scripts/create_woba_value.py
uv run python scripts/build_frontier_xwoba.py
uv run python scripts/analyze_xwoba_pitch_metrics.py
uv run python scripts/create_pitch_value_score.py
uv run python scripts/analyze_pitch_value_movement.py
uv run python scripts/cluster_pitch_archetypes.py
```

Location Value is a downstream add-on. Run it separately after the enriched pitch-level dataset exists:

```powershell
uv run python scripts/create_location_value.py
uv run python scripts/create_location_score.py
uv run python scripts/create_split_pitch_leaderboards.py
uv run python scripts/analyze_platoon_weapons.py
uv run python scripts/create_master_pitch_evaluation_table.py
uv run python scripts/create_stuff_plus_model.py
uv run python scripts/create_execution_plus.py
uv run python scripts/update_master_with_stuff_execution.py
uv run python scripts/create_final_scouting_leaderboards.py
```

Paper 1 is a downstream research module. Run it after `master_pitch_evaluation_table_v2.csv` exists:

```powershell
uv run python paper_research/paper_1_movement_vs_location/scripts/run_all_paper_1.py
```
