# Paper 1: Movement vs Location Regression

This folder contains the self-contained paper workflow for the movement quality vs location quality regression section.

It uses existing project outputs only. It does not rebuild Frontier xwOBA, Pitch Value Score, Location Value, movement archetypes, Stuff+, Execution+, or scouting leaderboards.

## Run

From the project root:

```powershell
uv run python paper_research/paper_1_movement_vs_location/scripts/run_all_paper_1.py
```

## Script Order

1. `01_create_regression_dataset.py`
2. `02_run_main_regressions.py`
3. `03_regression_diagnostics.py`
4. `04_robustness_checks.py`
5. `05_create_tables_and_figures.py`
6. `06_create_paper_results_summary.py`

## Outputs

- Data: `paper_research/paper_1_movement_vs_location/data/`
- Reports: `paper_research/paper_1_movement_vs_location/reports/`
- Figures: `paper_research/paper_1_movement_vs_location/plots/`
- Diagnostics: `paper_research/paper_1_movement_vs_location/plots/diagnostics/`
