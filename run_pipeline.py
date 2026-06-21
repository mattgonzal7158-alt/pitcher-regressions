from __future__ import annotations

import argparse
import shutil
import subprocess
import sys
from datetime import datetime
from pathlib import Path

import pandas as pd


ROOT = Path(__file__).resolve().parent
RAW_DIR = ROOT / "data" / "raw"
CANONICAL_RAW = RAW_DIR / "2026-data.parquet"
RUN_REPORT = ROOT / "reports" / "current_pitch_value_run_summary.md"

PIPELINE_STEPS = [
    ("Audit raw TrackMan file", "scripts/audit_trackman_parquet.py"),
    ("Add wOBA values", "scripts/create_woba_value.py"),
    ("Build xwOBA values", "scripts/build_frontier_xwoba.py"),
    ("Create pitcher-pitch metrics", "scripts/create_pitch_type_metrics.py"),
    ("Create Pitch Value Scores", "scripts/create_pitch_value_score.py"),
    ("Create movement score inputs", "scripts/create_movement_score_inputs.py"),
    ("Cluster movement archetypes", "scripts/cluster_pitch_archetypes.py"),
    ("Create location value grid", "scripts/create_location_value.py"),
    ("Create location scores", "scripts/create_location_score.py"),
    ("Create handedness split leaderboards", "scripts/create_split_pitch_leaderboards.py"),
    ("Analyze platoon weapons", "scripts/analyze_platoon_weapons.py"),
    ("Create master pitch table", "scripts/create_master_pitch_evaluation_table.py"),
    ("Create Stuff+ scores", "scripts/create_stuff_plus_model.py"),
    ("Create Execution+ scores", "scripts/create_execution_plus.py"),
    ("Update master table with Stuff+/Execution+", "scripts/update_master_with_stuff_execution.py"),
    ("Create final scouting leaderboards", "scripts/create_final_scouting_leaderboards.py"),
]


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description=(
            "Front-door rebuild for the pitch-value repo. Drop a new parquet in data/raw, "
            "then run this file to refresh all score outputs."
        )
    )
    parser.add_argument(
        "--raw-file",
        type=Path,
        default=None,
        help="Optional raw parquet to use. If omitted, the newest .parquet in data/raw is used.",
    )
    parser.add_argument(
        "--skip-raw-copy",
        action="store_true",
        help="Use data/raw/2026-data.parquet as-is.",
    )
    parser.add_argument(
        "--only-summary",
        action="store_true",
        help="Skip rebuild steps and regenerate only the quick-review exports and run summary.",
    )
    return parser.parse_args()


def newest_raw_file() -> Path:
    candidates = sorted(RAW_DIR.glob("*.parquet"), key=lambda path: path.stat().st_mtime, reverse=True)
    if not candidates:
        raise FileNotFoundError(
            f"No parquet files found in {RAW_DIR}. Add the latest TrackMan parquet there first."
        )
    return candidates[0]


def prepare_raw_file(args: argparse.Namespace) -> Path:
    RAW_DIR.mkdir(parents=True, exist_ok=True)
    if args.skip_raw_copy:
        if not CANONICAL_RAW.exists():
            raise FileNotFoundError(f"Missing canonical raw file: {CANONICAL_RAW}")
        return CANONICAL_RAW

    source = args.raw_file.resolve() if args.raw_file else newest_raw_file().resolve()
    if source.suffix.lower() != ".parquet":
        raise ValueError(f"Raw input must be a parquet file, got: {source}")
    if not source.exists():
        raise FileNotFoundError(f"Raw input not found: {source}")

    canonical = CANONICAL_RAW.resolve()
    if source != canonical:
        shutil.copy2(source, canonical)
        print(f"Copied raw input to {CANONICAL_RAW}")
    else:
        print(f"Using raw input {CANONICAL_RAW}")
    return CANONICAL_RAW


def run_step(label: str, script: str) -> None:
    print(f"\n=== {label} ===")
    command = [sys.executable, script]
    subprocess.run(command, cwd=ROOT, check=True)


def write_quick_exports() -> dict[str, Path]:
    output_dir = ROOT / "data" / "processed"
    reports_dir = ROOT / "reports"
    output_dir.mkdir(parents=True, exist_ok=True)
    reports_dir.mkdir(parents=True, exist_ok=True)

    exports: dict[str, Path] = {}

    pitch_values = pd.read_csv(output_dir / "pitch_value_scores.csv")
    top_pitch_value = pitch_values.sort_values("overall_rank").head(100)
    exports["Top 100 raw Pitch Value Scores"] = output_dir / "current_top_pitch_value_scores.csv"
    top_pitch_value.to_csv(exports["Top 100 raw Pitch Value Scores"], index=False)

    best_by_type = (
        pitch_values.sort_values(["pitch_type", "pitch_type_rank"])
        .groupby("pitch_type", dropna=False)
        .head(25)
        .reset_index(drop=True)
    )
    exports["Top 25 raw Pitch Value Scores by pitch type"] = output_dir / "current_top_pitch_value_by_type.csv"
    best_by_type.to_csv(exports["Top 25 raw Pitch Value Scores by pitch type"], index=False)

    final = pd.read_csv(output_dir / "final_scouting_leaderboards.csv")
    best_overall = final.loc[final["leaderboard"].eq("Best Overall Pitches")].copy()
    exports["Best overall final pitch scores"] = output_dir / "current_best_overall_pitches.csv"
    best_overall.to_csv(exports["Best overall final pitch scores"], index=False)

    master = pd.read_csv(output_dir / "master_pitch_evaluation_table_v2.csv")
    best_pitcher_pitch = (
        master.dropna(subset=["final_pitch_score_20_80"])
        .sort_values("final_pitch_score_20_80", ascending=False)
        .drop_duplicates(["pitcher_name", "pitcher_team", "pitch_type"])
        .head(150)
    )
    exports["Best pitcher-pitch rows"] = output_dir / "current_best_pitcher_pitches.csv"
    best_pitcher_pitch.to_csv(exports["Best pitcher-pitch rows"], index=False)

    return exports


def markdown_table(df: pd.DataFrame, columns: list[str], rows: int = 20) -> list[str]:
    lines = ["| " + " | ".join(columns) + " |", "|" + "|".join(["---"] * len(columns)) + "|"]
    for row in df.head(rows).itertuples(index=False):
        values = []
        for column in columns:
            value = getattr(row, column)
            if pd.isna(value):
                values.append("")
            elif isinstance(value, float):
                values.append(f"{value:.1f}" if "score" in column or column.endswith("_80") else f"{value:.3f}")
            else:
                values.append(str(value))
        lines.append("| " + " | ".join(values) + " |")
    return lines


def write_run_summary(raw_file: Path, exports: dict[str, Path]) -> None:
    processed_dir = ROOT / "data" / "processed"
    final = pd.read_csv(processed_dir / "final_scouting_leaderboards.csv")
    best_overall = final.loc[final["leaderboard"].eq("Best Overall Pitches")].copy()

    pitch_values = pd.read_csv(processed_dir / "pitch_value_scores.csv")
    pitch_type_counts = pitch_values["pitch_type"].value_counts().sort_index()

    lines = [
        "# Current Pitch Value Run Summary",
        "",
        f"- Run time: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}",
        f"- Raw input: `{raw_file.relative_to(ROOT)}`",
        f"- Qualified raw Pitch Value rows: {len(pitch_values):,}",
        f"- Final scouting leaderboard rows: {len(final):,}",
        "",
        "## Start Here",
        "",
        "- `reports/final_scouting_leaderboards.md`",
        "- `data/processed/current_best_overall_pitches.csv`",
        "- `data/processed/current_top_pitch_value_scores.csv`",
        "- `data/processed/master_pitch_evaluation_table_v2.csv`",
        "",
        "## Quick Exports",
        "",
    ]
    lines.extend(f"- {label}: `{path.relative_to(ROOT)}`" for label, path in exports.items())

    lines.extend(["", "## Top 20 Overall Pitches", ""])
    summary_columns = [
        "leaderboard_rank",
        "pitcher_name",
        "pitcher_team",
        "pitch_type",
        "batter_side",
        "pitch_count",
        "final_pitch_score_20_80",
        "raw_pitch_score_20_80",
        "location_score_20_80",
        "stuff_plus_20_80",
        "execution_plus_20_80",
    ]
    lines.extend(markdown_table(best_overall[summary_columns], summary_columns, rows=20))

    lines.extend(["", "## Qualified Pitch Value Rows by Pitch Type", "", "| Pitch Type | Rows |", "|---|---:|"])
    lines.extend(f"| `{pitch_type}` | {count:,} |" for pitch_type, count in pitch_type_counts.items())

    RUN_REPORT.parent.mkdir(parents=True, exist_ok=True)
    RUN_REPORT.write_text("\n".join(lines), encoding="utf-8")
    print(f"\nWrote run summary: {RUN_REPORT}")


def main() -> None:
    args = parse_args()
    if args.only_summary:
        raw_file = CANONICAL_RAW if CANONICAL_RAW.exists() else ROOT / "data" / "processed" / "2026-data-with-woba-xwoba.parquet"
    else:
        raw_file = prepare_raw_file(args)

    if not args.only_summary:
        for label, script in PIPELINE_STEPS:
            run_step(label, script)

    exports = write_quick_exports()
    write_run_summary(raw_file, exports)

    print("\nDone. Open reports/current_pitch_value_run_summary.md first.")


if __name__ == "__main__":
    main()
