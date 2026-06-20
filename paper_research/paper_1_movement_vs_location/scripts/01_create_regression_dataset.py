from __future__ import annotations

import numpy as np
import pandas as pd

from paper_utils import (
    DATA_DIR,
    DEPENDENTS,
    ENRICHED_PITCH_PATH,
    REGRESSION_COLUMNS,
    REPORT_DIR,
    add_join_keys,
    ensure_dirs,
    find_master_table,
    is_batted_ball_dependent,
    markdown_table,
)


OUTPUT_PATH = DATA_DIR / "regression_dataset.csv"
SUMMARY_PATH = REPORT_DIR / "regression_dataset_summary.md"
MIN_PITCHES = 25
MIN_BATTED_BALLS = 10


def closest_column(columns: list[str], canonical: str) -> str | None:
    if canonical in columns:
        return canonical
    compact = canonical.replace("_", "").lower()
    candidates = []
    for column in columns:
        low = column.lower()
        score = 0
        if compact in low.replace("_", ""):
            score += 3
        for token in canonical.lower().split("_"):
            if token in low:
                score += 1
        if score:
            candidates.append((score, column))
    return sorted(candidates, reverse=True)[0][1] if candidates else None


def pitch_outcomes_from_parquet() -> pd.DataFrame:
    if not ENRICHED_PITCH_PATH.exists():
        return pd.DataFrame()
    required = [
        "pitcher_name",
        "pitcher_id",
        "pitcher_team",
        "pitch_type",
        "batter_side_canonical",
        "pitch_call",
        "xwoba_frontier",
        "woba_value",
        "hit_launch_exit_speed_y",
    ]
    df = pd.read_parquet(ENRICHED_PITCH_PATH, columns=required)
    df = add_join_keys(df)
    pitch_call = df["pitch_call"].astype("string")
    swing = pitch_call.isin(
        ["Strike Swinging", "Foul Ball Not Fieldable", "Foul Ball Fieldable", "In Play"]
    ).fillna(False)
    whiff = pitch_call.eq("Strike Swinging").fillna(False)
    batted_ball = df["xwoba_frontier"].notna()
    hardhit = pd.to_numeric(df["hit_launch_exit_speed_y"], errors="coerce").ge(95)
    df["pitch_count_actual"] = 1
    df["batted_ball_count_actual"] = batted_ball.astype(int)
    df["swing_count"] = swing.astype(int)
    df["whiff_count"] = whiff.astype(int)
    df["hardhit_count"] = (hardhit & batted_ball).astype(int)
    grouped = (
        df.groupby(
            ["pitcher_name", "pitcher_id_key", "pitcher_team", "pitch_type", "batter_side"],
            dropna=False,
        )
        .agg(
            pitch_count_actual=("pitch_count_actual", "sum"),
            batted_ball_count_actual=("batted_ball_count_actual", "sum"),
            xwoba_frontier=("xwoba_frontier", "mean"),
            woba_value=("woba_value", "mean"),
            swing_count=("swing_count", "sum"),
            whiff_count=("whiff_count", "sum"),
            hardhit_count=("hardhit_count", "sum"),
        )
        .reset_index()
    )
    grouped["whiff_pct"] = grouped["whiff_count"] / grouped["swing_count"].replace(0, np.nan)
    grouped["hardhit_pct"] = grouped["hardhit_count"] / grouped["batted_ball_count_actual"].replace(0, np.nan)
    return grouped


def main() -> None:
    ensure_dirs()
    master_path = find_master_table()
    master = add_join_keys(pd.read_csv(master_path))
    before_rows = len(master)
    columns = list(master.columns)
    mappings: dict[str, str | None] = {}

    for canonical in DEPENDENTS:
        match = closest_column(columns, canonical)
        mappings[canonical] = match
        if match and match != canonical:
            master[canonical] = master[match]

    outcomes = pitch_outcomes_from_parquet()
    if not outcomes.empty:
        merge_keys = ["pitcher_name", "pitcher_id_key", "pitcher_team", "pitch_type", "batter_side"]
        outcome_cols = [
            "pitch_count_actual",
            "batted_ball_count_actual",
            "xwoba_frontier",
            "woba_value",
            "whiff_pct",
            "hardhit_pct",
        ]
        master = master.merge(
            outcomes[merge_keys + outcome_cols],
            on=merge_keys,
            how="left",
            suffixes=("", "_from_pitch_data"),
        )
        for column in DEPENDENTS:
            from_col = f"{column}_from_pitch_data"
            if from_col in master.columns:
                if column in master.columns:
                    master[column] = master[column].fillna(master[from_col])
                else:
                    master[column] = master[from_col]
                mappings[column] = mappings.get(column) or f"pitch-level aggregate: {column}"
            elif column in master.columns and mappings.get(column) is None:
                mappings[column] = f"pitch-level aggregate: {column}"
        for count_col, from_col in [
            ("pitch_count", "pitch_count_actual"),
            ("batted_ball_count", "batted_ball_count_actual"),
        ]:
            if from_col in master.columns:
                master[count_col] = pd.to_numeric(master[count_col], errors="coerce").fillna(master[from_col])

    for column in REGRESSION_COLUMNS:
        if column not in master.columns:
            master[column] = np.nan

    keep = master[REGRESSION_COLUMNS].drop_duplicates(
        ["pitcher_name", "pitcher_id", "pitcher_team", "pitch_type", "batter_side"]
    )
    missing_before = keep[REGRESSION_COLUMNS].isna().sum().reset_index()
    missing_before.columns = ["column", "missing_rows"]

    filtered = keep.copy()
    for column in ["pitch_count", "batted_ball_count", "movement_quality_20_80", "location_score_20_80", *DEPENDENTS]:
        filtered[column] = pd.to_numeric(filtered[column], errors="coerce")
    filtered = filtered.loc[
        filtered["pitch_count"].ge(MIN_PITCHES)
        & filtered["movement_quality_20_80"].notna()
        & filtered["location_score_20_80"].notna()
    ].copy()
    # Keep a common regression dataset, but leave dependent-variable-specific batted-ball
    # filters to later scripts so whiff models retain all valid rows.
    after_rows = len(filtered)
    filtered.to_csv(OUTPUT_PATH, index=False)

    desc_cols = [
        "pitch_count",
        "batted_ball_count",
        *DEPENDENTS,
        "movement_quality_20_80",
        "location_score_20_80",
    ]
    desc = filtered[desc_cols].describe().T.reset_index().rename(columns={"index": "variable"})
    pitch_counts = filtered["pitch_type"].value_counts().reset_index()
    pitch_counts.columns = ["pitch_type", "rows"]
    side_counts = filtered["batter_side"].value_counts(dropna=False).reset_index()
    side_counts.columns = ["batter_side", "rows"]

    lines = [
        "# Regression Dataset Summary",
        "",
        f"- Master input: `{master_path}`",
        f"- Output dataset: `{OUTPUT_PATH}`",
        f"- Rows before filtering: {before_rows:,}",
        f"- Rows after filtering: {after_rows:,}",
        f"- Minimum pitch count: {MIN_PITCHES}",
        "",
        "## Outcome Column Mapping",
        "",
        "| Canonical variable | Source column |",
        "|---|---|",
    ]
    for canonical, source in mappings.items():
        lines.append(f"| `{canonical}` | `{source or '<missing>'}` |")
    lines.extend(["", "## Pitch Type Counts", "", *markdown_table(pitch_counts)])
    lines.extend(["", "## Batter Side Counts", "", *markdown_table(side_counts)])
    lines.extend(["", "## Missing Value Table Before Filtering", "", *markdown_table(missing_before)])
    lines.extend(["", "## Descriptive Statistics", "", *markdown_table(desc)])
    lines.extend(["", "## Dependent-Specific Filters", ""])
    for dep in DEPENDENTS:
        dep_df = filtered.dropna(subset=[dep])
        if is_batted_ball_dependent(dep):
            dep_df = dep_df.loc[dep_df["batted_ball_count"].ge(MIN_BATTED_BALLS)]
        lines.append(f"- `{dep}` usable rows: {len(dep_df):,}")
    SUMMARY_PATH.write_text("\n".join(lines), encoding="utf-8")

    print(f"Wrote regression dataset: {OUTPUT_PATH}")
    print(f"Wrote summary: {SUMMARY_PATH}")
    print(f"Rows before filtering: {before_rows:,}")
    print(f"Rows after filtering: {after_rows:,}")


if __name__ == "__main__":
    main()
