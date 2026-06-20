from __future__ import annotations

import subprocess
import sys
from pathlib import Path


SCRIPT_DIR = Path(__file__).resolve().parent
SCRIPTS = [
    "01_create_regression_dataset.py",
    "02_run_main_regressions.py",
    "03_regression_diagnostics.py",
    "04_robustness_checks.py",
    "05_create_tables_and_figures.py",
    "06_create_paper_results_summary.py",
]


def main() -> None:
    for script in SCRIPTS:
        path = SCRIPT_DIR / script
        print(f"Running {path}")
        subprocess.run([sys.executable, str(path)], check=True)


if __name__ == "__main__":
    main()
