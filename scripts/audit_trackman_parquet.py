from pathlib import Path

import pandas as pd


PARQUET_PATH = Path("data/raw/2026-data.parquet")
REPORT_PATH = Path("reports/frontier_trackman_data_audit.md")


FIELD_MATCHES = {
    "Exit Velocity": [
        "exit_speed",
        "exit_velocity",
        "hit_launch_exit_speed",
    ],
    "Launch Angle": [
        "launch_angle",
        "hit_launch_angle",
    ],
    "Spray Angle": [
        "spray_angle",
        "launch_direction",
        "hit_launch_direction",
        "flat_bearing",
        "hit_landing_flat_bearing",
    ],
    "Pitch Type": [
        "pitch_type",
        "tagged_pitch_type",
        "auto_pitch_type",
    ],
    "Pitcher Name": [
        "pitcher_name",
    ],
    "Batter Name": [
        "batter_name",
        "hitter_name",
    ],
    "Plate Appearance Result": [
        "kor_bb",
        "pa_result",
        "plate_appearance_result",
        "play_result",
    ],
    "Pitch Result": [
        "pitch_call",
        "pitch_result",
    ],
    "IVB": [
        "induced_vert_break",
        "induced_vertical_break",
        "ivb",
        "pfxz",
    ],
    "HB": [
        "horz_break",
        "horizontal_break",
        "hb",
        "pfxx",
    ],
    "Spin Rate": [
        "spin_rate",
    ],
    "Velocity": [
        "rel_speed",
        "release_speed",
        "effective_velo",
        "velocity",
        "velo",
    ],
}


def compact(value: str) -> str:
    return "".join(ch.lower() for ch in value if ch.isalnum())


def spaced(value: str) -> str:
    return value.lower().replace("_", " ").replace("-", " ")


def identify_candidates(columns: list[str]) -> dict[str, list[str]]:
    candidates = {}
    for label, keywords in FIELD_MATCHES.items():
        hits = []
        for column in columns:
            column_compact = compact(column)
            for keyword in keywords:
                keyword_compact = compact(keyword)
                if keyword_compact and keyword_compact in column_compact:
                    hits.append(column)
                    break
        candidates[label] = hits
    return candidates


def identify_pitch_type_columns(columns: list[str]) -> list[str]:
    terms = ["pitch_type", "tagged_pitch_type", "auto_pitch_type"]
    return [column for column in columns if any(compact(term) in compact(column) for term in terms)]


def identify_event_columns(columns: list[str]) -> list[str]:
    terms = [
        "kor_bb",
        "pitch_call",
        "pitch_result",
        "play_result",
        "pa_result",
        "plate_appearance_result",
        "strike_zone_decision",
        "hit_type",
    ]
    compact_terms = [compact(term) for term in terms]
    return [column for column in columns if any(term in compact(column) for term in compact_terms)]


def unique_section(df: pd.DataFrame, columns: list[str], dtypes: pd.Series, max_values: int = 250) -> list[str]:
    lines = []
    for column in columns:
        series = df[column]
        values = series.dropna().astype("string").unique().tolist()
        values = sorted(values, key=str)
        lines.append(f"### {column}")
        lines.append(
            f"dtype: `{dtypes[column]}` | missing: {int(series.isna().sum())} | "
            f"non-null unique values: {len(values)}"
        )
        if values:
            for value in values[:max_values]:
                lines.append(f"- `{value}`")
            if len(values) > max_values:
                lines.append(f"- ... {len(values) - max_values} more values not shown")
        else:
            lines.append("- No non-null values")
        lines.append("")
    return lines


def main() -> None:
    df = pd.read_parquet(PARQUET_PATH)
    columns = list(df.columns)
    dtypes = df.dtypes.astype(str)
    missing = df.isna().sum()
    candidates = identify_candidates(columns)
    pitch_type_columns = identify_pitch_type_columns(columns)
    event_columns = identify_event_columns(columns)

    lines = [
        "# Frontier League TrackMan Parquet Data Audit",
        "",
        f"- File: `{PARQUET_PATH}`",
        f"- Rows: {len(df):,}",
        f"- Columns: {len(columns):,}",
        f"- Memory usage in pandas: {df.memory_usage(deep=True).sum() / (1024**2):,.2f} MB",
        "",
        "## 1. All Column Names",
    ]

    for index, column in enumerate(columns, 1):
        lines.append(f"{index}. `{column}`")

    lines.extend(["", "## 2. Data Types", "| Column | Data Type |", "|---|---|"])
    for column in columns:
        lines.append(f"| `{column}` | `{dtypes[column]}` |")

    lines.extend(["", "## 3. Missing Values", "| Column | Missing Count | Missing % |", "|---|---:|---:|"])
    for column in columns:
        miss = int(missing[column])
        pct = miss / len(df) * 100 if len(df) else 0
        lines.append(f"| `{column}` | {miss:,} | {pct:.2f}% |")

    lines.extend(["", "## 4. Unique Values for Pitch Type Columns"])
    if pitch_type_columns:
        lines.extend(unique_section(df, pitch_type_columns, dtypes))
    else:
        lines.append("No pitch type columns were identified by name search.")

    lines.extend(["", "## 5. Unique Values for Event/Outcome Columns"])
    if event_columns:
        lines.extend(unique_section(df, event_columns, dtypes))
    else:
        lines.append("No event/outcome columns were identified by name search.")

    lines.extend(
        [
            "",
            "## 6. Candidate Columns by Requested Field",
            "These are name-based candidate matches using actual column names. They are not assumed canonical mappings.",
            "",
            "| Requested Field | Candidate Column Names |",
            "|---|---|",
        ]
    )
    for label, hits in candidates.items():
        value = ", ".join(f"`{hit}`" for hit in hits) if hits else "None found by name search"
        lines.append(f"| {label} | {value} |")

    lines.extend(
        [
            "",
            "## 7. Dataset Structure Summary",
            f"The parquet file contains {len(df):,} rows and {len(columns):,} columns. "
            "Column data types are distributed as follows:",
        ]
    )
    for dtype_name, count in dtypes.value_counts().sort_index().items():
        lines.append(f"- `{dtype_name}`: {count} columns")

    lines.extend(["", "Columns with no missing values:"])
    none_missing = [column for column in columns if int(missing[column]) == 0]
    lines.append(", ".join(f"`{column}`" for column in none_missing) if none_missing else "None")

    lines.extend(["", "Columns with all values missing:"])
    all_missing = [column for column in columns if int(missing[column]) == len(df)]
    lines.append(", ".join(f"`{column}`" for column in all_missing) if all_missing else "None")

    lines.extend(["", "Highest-missing columns:"])
    for column, miss in missing.sort_values(ascending=False).head(20).items():
        pct = miss / len(df) * 100 if len(df) else 0
        lines.append(f"- `{column}`: {int(miss):,} missing ({pct:.2f}%)")

    lines.extend(["", "Lowest-missing columns:"])
    for column, miss in missing.sort_values(ascending=True).head(20).items():
        pct = miss / len(df) * 100 if len(df) else 0
        lines.append(f"- `{column}`: {int(miss):,} missing ({pct:.2f}%)")

    numeric_count = len(df.select_dtypes(include="number").columns)
    lines.extend(
        [
            "",
            f"Numeric column count: {numeric_count}",
            f"Non-numeric column count: {len(columns) - numeric_count}",
        ]
    )

    REPORT_PATH.write_text("\n".join(lines), encoding="utf-8")

    print(f"Wrote {REPORT_PATH}")
    print(f"Rows: {len(df):,}")
    print(f"Columns: {len(columns):,}")
    print("Column names:")
    for column in columns:
        print(f"- {column}")
    print("\nCandidate fields:")
    for label, hits in candidates.items():
        print(f"{label}: {hits if hits else 'None found'}")
    print(f"\nPitch type columns: {pitch_type_columns if pitch_type_columns else 'None found'}")
    print(f"Event/outcome columns: {event_columns if event_columns else 'None found'}")


if __name__ == "__main__":
    main()
