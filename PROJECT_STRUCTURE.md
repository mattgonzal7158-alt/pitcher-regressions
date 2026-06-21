# Project Structure

This repo is for reviewing which pitches are most valuable right now.

## Folders

| Folder | Contents |
|---|---|
| `data/raw/` | Original source files, when available. |
| `data/processed/` | Generated parquet and CSV pitch-value outputs. |
| `reports/` | Markdown leaderboards, methodology notes, and scouting summaries. |
| `plots/` | Generated pitch-value, location-value, and movement-archetype figures. |
| `scripts/` | Reproducible Python scripts for building the score tables. |
| `run_pipeline.py` | Front-door runner that rebuilds every score output from a new raw parquet. |
| `archive/duplicates/` | Older duplicate outputs kept for reference. |
| `archive/cache/` | Older generated cache files kept out of the active workflow. |

## Main Reports

| Report | Purpose |
|---|---|
| `reports/pitch_value_score_leaderboards.md` | Main Pitch Value Score leaderboards. |
| `reports/pitch_leaderboard_splits.md` | Handedness-specific final pitch leaderboards. |
| `reports/final_scouting_leaderboards.md` | Best current pitches across overall, splits, Stuff+, Execution+, location, and weapon categories. |
| `reports/master_pitch_evaluation_table_v2_report.md` | Master pitch table with Stuff+ and Execution+ fields. |
| `reports/pitch_movement_archetype_report.md` | Movement archetypes, highest-performing movement groups, and undervalued pitches. |
| `reports/location_score_report.md` | Location Score leaderboards by pitcher, pitch type, and batter side. |
| `reports/platoon_weapon_report.md` | Platoon gap analysis identifying one-sided and balanced pitch weapons. |
| `reports/stuff_plus_report.md` | Movement/release-only Stuff+ score summaries and leaderboards. |
| `reports/execution_plus_report.md` | Execution+ summaries comparing actual final scores to movement-based expectations. |
| `reports/FRONTIER_PITCH_VALUE_METHODOLOGY.md` | Methodology and interpretation guide. |

## Canonical Data Outputs

| File | Purpose |
|---|---|
| `data/processed/pitch_value_scores_with_type_rank.csv` | Current normalized Pitch Value Score table. |
| `data/processed/pitch_value_scores.csv` | Canonical Pitch Value Score filename. |
| `data/processed/pitch_leaderboard_splits.csv` | Handedness-specific final pitch leaderboard table. |
| `data/processed/final_scouting_leaderboards.csv` | Long-form export of the final scouting leaderboard sections. |
| `data/processed/master_pitch_evaluation_table_v2.csv` | Master pitch table with Pitch Value, Location Score, Stuff+, and Execution+. |
| `data/processed/movement_score_inputs.csv` | Pitch Value joined to movement and release traits for movement archetypes and master tables. |
| `data/processed/pitch_movement_archetypes.csv` | Clustered movement archetype table. |
| `data/processed/highest_performing_archetype_pitches.csv` | Pitches in the best-performing movement archetypes. |
| `data/processed/undervalued_movement_pitches.csv` | Strong movement profiles with average-or-worse current Pitch Value. |
| `data/processed/location_scores.csv` | Pitcher + pitch type + batter side Location Scores. |
| `data/processed/stuff_plus_scores.csv` | Movement/release-only Stuff+ scores and rankings. |
| `data/processed/execution_plus_scores.csv` | Execution+ scores and quadrant labels. |
| `data/processed/platoon_weapon_scores.csv` | Pitcher + pitch type platoon gap scores. |
| `data/processed/2026-data-with-woba-xwoba.parquet` | Enriched pitch-level dataset used by the score builders. |

## What Goes Into Scoring

### Raw Input

The pipeline starts from a TrackMan-style parquet in `data/raw/`. `run_pipeline.py` copies the newest raw parquet to:

- `data/raw/2026-data.parquet`

The raw file must include pitch context, pitch outcomes, batted-ball tracking, pitch movement, release traits, pitcher IDs/names/teams, batter side, pitch type, and plate location fields.

Key raw columns used:

| Ingredient | Columns |
|---|---|
| Pitcher identity | `pitcher_name`, `pitcher_id`, `pitcher_team` |
| Pitch type | `pitch_type` |
| Batter side | `batter_side`, `batter_side_canonical` |
| Pitch result | `pitch_call`, `kor_bb`, `play_result` |
| Count context | `game_state_strikes` |
| Batted-ball contact | `hit_launch_exit_speed_y`, `hit_launch_angle_y`, `hit_launch_direction_y`, `hit_type` |
| Pitch movement | `pitch_movement_induced_vert_break_x`, `pitch_movement_horz_break_x` |
| Release/stuff traits | `pitch_release_rel_speed_x`, `pitch_release_spin_rate_x`, `pitch_release_extension_x`, `pitch_release_rel_height_x`, `pitch_release_rel_side_x` |
| Location | `pitch_location_plate_loc_height_x`, `pitch_location_plate_loc_side_x` |

### Pitch Value Score

Pitch Value Score grades one pitcher + pitch type. It is the main current pitch-quality score.

Inputs come from `data/processed/pitcher_pitch_type_xwoba_metrics.csv`, created by `scripts/create_pitch_type_metrics.py`.

Qualification:

- At least 50 pitches
- At least 10 tracked batted balls
- Non-null scoring metrics

Metrics used:

| Metric | Meaning | Direction |
|---|---|---|
| `whiff_pct` | Swinging strikes / swings | Higher generally helps |
| `csw_pct` | Called strikes + whiffs / pitches | Higher generally helps |
| `putaway_pct` | Strikeouts / two-strike pitches | Higher generally helps |
| `k_pct` | Strikeouts / terminal PA-ending pitches | Higher generally helps |
| `avg_exit_velocity` | Mean EV on tracked batted balls | Lower helps |
| `hardhit_pct` | Share of tracked batted balls at least 95 mph | Lower helps |
| `barrel_pct` | Approximate barrel-zone share | Lower usually helps |
| `sweetspot_pct` | Launch angle 8 to 32 degrees share | Lower helps |

Formula shape:

```text
metric_z = standardized metric across qualified pitcher-pitch type rows
pitch_value_raw = -sum(frozen_standardized_weight * metric_z)
pitch_value_20_80 = 50 + 10 * z(pitch_value_raw), clipped from 20 to 80
pitch_value_0_100 = percentile rank of pitch_value_raw
```

Outputs:

- `data/processed/pitch_value_scores.csv`
- `data/processed/pitch_value_scores_with_type_rank.csv`
- `reports/pitch_value_score_leaderboards.md`

### Location Score

Location Score grades where a pitcher locates a pitch type against each batter side.

It starts with `scripts/create_location_value.py`, which builds location-value grids by:

- Pitch type
- Batter side
- 0.25-foot plate-location bins

Each grid cell compares smoothed cell xwOBA to that pitch type + batter side average.

Then `scripts/create_location_score.py` assigns pitches to those grid cells and aggregates by pitcher + pitch type + batter side.

Qualification:

- At least 25 assigned pitches

Formula shape:

```text
location_advantage = pitch_type_batter_side_avg_xwoba - grid_xwoba
location_score_raw = average location_advantage
location_score_20_80 = 50 + 10 * z(location_score_raw), clipped from 20 to 80
location_score_0_100 = percentile rank of location_score_raw
```

Outputs:

- `data/processed/location_value_grid.csv`
- `data/processed/location_scores.csv`
- `reports/location_score_report.md`

### Final Pitch Score

Final Pitch Score is the main handedness-specific score. It blends overall pitch quality with split-specific location quality.

Created by `scripts/create_split_pitch_leaderboards.py`.

Join level:

- Pitch Value: pitcher + pitch type
- Location Score: pitcher + pitch type + batter side

Formula:

```text
final_pitch_score = 0.70 * pitch_value_20_80 + 0.30 * location_score_20_80
final_pitch_score_0_100 = percentile rank of final_pitch_score
```

Outputs:

- `data/processed/pitch_leaderboard_splits.csv`
- `reports/pitch_leaderboard_splits.md`
- Feeds `data/processed/master_pitch_evaluation_table.csv`

### Movement Archetypes and Movement Quality

Movement archetypes group pitches by shape and release traits, not by outcome alone.

Created by:

- `scripts/create_movement_score_inputs.py`
- `scripts/cluster_pitch_archetypes.py`

Inputs:

| Trait | Source |
|---|---|
| `ivb` | `pitch_movement_induced_vert_break_x` |
| `hb` | `pitch_movement_horz_break_x` |
| `spin_rate` | `pitch_release_spin_rate_x` |
| `velocity` | `pitch_release_rel_speed_x` |
| `extension` | `pitch_release_extension_x` |
| `release_height` | `pitch_release_rel_height_x` |
| `release_side` | `pitch_release_rel_side_x` |

The clustering itself uses:

- `ivb`
- `hb`
- `spin_rate`
- `velocity`
- `extension`

Movement quality is a movement-only proxy that blends movement-predicted Pitch Value with the average Pitch Value of the pitch's archetype.

Outputs:

- `data/processed/movement_score_inputs.csv`
- `data/processed/pitch_movement_archetypes.csv`
- `data/processed/pitch_movement_archetype_summary.csv`
- `data/processed/highest_performing_archetype_pitches.csv`
- `data/processed/undervalued_movement_pitches.csv`
- `reports/pitch_movement_archetype_report.md`

### Stuff+

Stuff+ estimates expected final pitch quality from movement and release traits only.

Created by `scripts/create_stuff_plus_model.py`.

Target:

- `final_pitch_score_20_80`

Predictors:

- `IVB`
- `HB`
- `velocity`
- `spin_rate`
- `extension`
- `release_height`
- `release_side`

Modeling approach:

- Pitch types with at least 30 rows get pitch-type-specific movement/release models.
- Smaller pitch types use a pooled fallback model with pitch-type fixed effects.

Formula shape:

```text
stuff_plus_raw = movement/release-only predicted final pitch score
stuff_plus_20_80 = 50 + 10 * z(stuff_plus_raw), clipped from 20 to 80
stuff_plus_0_100 = percentile rank of stuff_plus_raw
```

Outputs:

- `data/processed/stuff_plus_scores.csv`
- `reports/stuff_plus_report.md`

### Execution+

Execution+ compares actual final pitch quality to movement-only expected quality.

Created by `scripts/create_execution_plus.py`.

Formula:

```text
execution_raw = final_pitch_score_20_80 - stuff_plus_raw
execution_plus_20_80 = 50 + 10 * z(execution_raw), clipped from 20 to 80
execution_plus_0_100 = percentile rank of execution_raw
```

Quadrants:

| Quadrant | Meaning |
|---|---|
| `Elite Weapon` | High Stuff+, high Execution+ |
| `Development Target` | High Stuff+, low Execution+ |
| `Command/Deception Weapon` | Low Stuff+, high Execution+ |
| `Low Priority` | Low Stuff+, low Execution+ |

Outputs:

- `data/processed/execution_plus_scores.csv`
- `reports/execution_plus_report.md`

### Platoon Weapons

Platoon weapon scores compare each pitch's final score against RHH and LHH.

Created by `scripts/analyze_platoon_weapons.py`.

Formula:

```text
platoon_gap = final_pitch_score_vs_rhh - final_pitch_score_vs_lhh
```

Positive gaps mean the pitch scores better versus RHH. Negative gaps mean it scores better versus LHH.

Outputs:

- `data/processed/platoon_weapon_scores.csv`
- `reports/platoon_weapon_report.md`

### Master and Final Scouting Tables

The master table joins the score layers into one pitcher + pitch type + batter side table:

- Pitch Value
- Location Score
- Final Pitch Score
- Platoon category
- Movement traits
- Movement archetype
- Stuff+
- Execution+

Outputs:

- `data/processed/master_pitch_evaluation_table.csv`
- `data/processed/master_pitch_evaluation_table_v2.csv`
- `data/processed/final_scouting_leaderboards.csv`
- `reports/final_scouting_leaderboards.md`

## Reproduction Order

After adding the newest TrackMan parquet to `data/raw/`, run from the project root:

```powershell
uv run python run_pipeline.py
```

The runner uses the newest `.parquet` in `data/raw/`, copies it to `data/raw/2026-data.parquet`, rebuilds every table, and writes quick-review exports:

| File | Purpose |
|---|---|
| `reports/current_pitch_value_run_summary.md` | First report to open after a rebuild. |
| `data/processed/current_best_overall_pitches.csv` | Best overall final pitch scores. |
| `data/processed/current_top_pitch_value_scores.csv` | Top raw Pitch Value Scores. |
| `data/processed/current_top_pitch_value_by_type.csv` | Top raw Pitch Value Scores by pitch type. |
| `data/processed/current_best_pitcher_pitches.csv` | Best pitcher-pitch rows from the master table. |

You can also pass a specific raw file:

```powershell
uv run python run_pipeline.py --raw-file data/raw/my_new_trackman_file.parquet
```

The underlying step order is:

```powershell
uv run python scripts/create_woba_value.py
uv run python scripts/build_frontier_xwoba.py
uv run python scripts/create_pitch_type_metrics.py
uv run python scripts/create_pitch_value_score.py
uv run python scripts/create_movement_score_inputs.py
uv run python scripts/cluster_pitch_archetypes.py
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
