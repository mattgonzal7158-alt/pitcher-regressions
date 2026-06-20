# Paper 1: Movement vs Location Regression

This standalone paper module compares movement quality and location quality as explanations for pitch outcomes.

It is organized as its own mini-project:

- `scripts/` - reproducible paper workflow.
- `data/` - paper-specific regression datasets and CSV model outputs.
- `reports/` - paper summaries, regression tables, diagnostics, and robustness checks.
- `plots/` - paper figures and diagnostic plots.

The workflow uses existing project outputs only. It does not rebuild Frontier xwOBA, Pitch Value Score, Location Value, movement archetypes, Stuff+, Execution+, or scouting leaderboards.

## Run

From the project root:

```powershell
uv run python paper_research/paper_1_movement_vs_location/scripts/run_all_paper_1.py
```

## Start Here

1. `reports/paper_results_summary.md`
2. `reports/paper_tables_and_figures.md`
3. `scripts/run_all_paper_1.py`
