from pathlib import Path

import pandas as pd


INPUT_PATH = Path("data/raw/2026-data.parquet")
OUTPUT_PATH = Path("data/processed/2026-data-with-woba.parquet")
REPORT_PATH = Path("reports/woba_value_validation.md")

EVENT_COLUMNS = {
    "plate_appearance_result": "play_result",
    "walk_strikeout_result": "kor_bb",
    "pitch_result": "pitch_call",
    "pitch_type": "pitch_type",
}

WOBA_WEIGHTS = {
    "BB": 0.701,
    "HBP": 0.732,
    "1B": 0.893,
    "2B": 1.265,
    "3B": 1.601,
    "HR": 2.056,
}


def derive_woba_event(df: pd.DataFrame) -> pd.Series:
    play_result = df[EVENT_COLUMNS["plate_appearance_result"]].astype("string")
    kor_bb = df[EVENT_COLUMNS["walk_strikeout_result"]].astype("string")
    pitch_call = df[EVENT_COLUMNS["pitch_result"]].astype("string")

    event = pd.Series("OTHER_ZERO", index=df.index, dtype="string")

    event.loc[play_result.eq("Single")] = "1B"
    event.loc[play_result.eq("Double")] = "2B"
    event.loc[play_result.eq("Triple")] = "3B"
    event.loc[play_result.eq("Home Run")] = "HR"
    event.loc[kor_bb.eq("Walk")] = "BB"
    event.loc[pitch_call.eq("Hit By Pitch")] = "HBP"

    out_mask = (
        kor_bb.eq("Strikeout")
        | play_result.isin(["Out", "Fielder's Choice", "Sacrifice", "Caught Stealing"])
    )
    event.loc[out_mask] = "OUT"

    # Positive events win if a row has overlapping labels.
    event.loc[play_result.eq("Single")] = "1B"
    event.loc[play_result.eq("Double")] = "2B"
    event.loc[play_result.eq("Triple")] = "3B"
    event.loc[play_result.eq("Home Run")] = "HR"
    event.loc[kor_bb.eq("Walk")] = "BB"
    event.loc[pitch_call.eq("Hit By Pitch")] = "HBP"

    return event


def write_report(df: pd.DataFrame, woba_event: pd.Series) -> None:
    event_counts = woba_event.value_counts(dropna=False).rename_axis("event").reset_index(name="count")
    stats = df["woba_value"].describe()
    by_pitch_type = (
        df.groupby(EVENT_COLUMNS["pitch_type"], dropna=False)["woba_value"]
        .agg(count="size", mean="mean", sum="sum")
        .sort_values(["mean", "count"], ascending=[False, False])
        .reset_index()
    )

    lines = [
        "# woba_value Validation Report",
        "",
        f"- Input file: `{INPUT_PATH}`",
        f"- Output file: `{OUTPUT_PATH}`",
        f"- Rows saved: {len(df):,}",
        f"- Columns saved: {len(df.columns):,}",
        "",
        "## Event/Result Columns Identified",
        "",
        "| Role | Actual Column Name | Why Used |",
        "|---|---|---|",
        "| Plate appearance / batted-ball result | `play_result` | Contains `Single`, `Double`, `Triple`, `Home Run`, and in-play zero-value results. |",
        "| Walk / strikeout result | `kor_bb` | Contains `Walk` and `Strikeout`. |",
        "| Pitch result | `pitch_call` | Contains `Hit By Pitch`. |",
        "| Pitch type | `pitch_type` | Clean pitch-type column used for the pitch-type average. |",
        "",
        "## Assumptions",
        "",
        "- `play_result` is used for hit events because it contains the actual canonical hit result names.",
        "- `kor_bb == Walk` is mapped to `BB`.",
        "- `pitch_call == Hit By Pitch` is mapped to `HBP`.",
        "- `kor_bb == Strikeout` plus `play_result` values `Out`, `Fielder's Choice`, `Sacrifice`, and `Caught Stealing` are treated as outs and assigned `0.0`.",
        "- Rows that do not match a provided positive weight or the listed out labels are assigned `0.0` and counted as `OTHER_ZERO`; this includes non-terminal pitches and events outside the provided weights, such as `Error` or `Stolen Base`.",
        "- If a row has overlapping labels, positive weighted outcomes are applied after zero-value out labels.",
        "",
        "## Weights Applied",
        "",
        "| Event | Weight |",
        "|---|---:|",
    ]
    for event, weight in WOBA_WEIGHTS.items():
        lines.append(f"| `{event}` | {weight:.3f} |")

    lines.extend(["", "## Derived Event Counts", "", "| Event | Count |", "|---|---:|"])
    for row in event_counts.itertuples(index=False):
        lines.append(f"| `{row.event}` | {row.count:,} |")

    lines.extend(["", "## Raw Event Column Counts", ""])
    for column in [
        EVENT_COLUMNS["plate_appearance_result"],
        EVENT_COLUMNS["walk_strikeout_result"],
        EVENT_COLUMNS["pitch_result"],
    ]:
        lines.extend([f"### `{column}`", "", "| Value | Count |", "|---|---:|"])
        counts = df[column].astype("string").fillna("<NA>").value_counts(dropna=False)
        for value, count in counts.items():
            lines.append(f"| `{value}` | {count:,} |")
        lines.append("")

    lines.extend(
        [
            "## woba_value Summary Statistics",
            "",
            "| Statistic | Value |",
            "|---|---:|",
        ]
    )
    for stat, value in stats.items():
        lines.append(f"| `{stat}` | {value:.6f} |")

    lines.extend(
        [
            "",
            "## Average woba_value by Pitch Type",
            "",
            "| Pitch Type | Count | Average woba_value | Sum woba_value |",
            "|---|---:|---:|---:|",
        ]
    )
    for row in by_pitch_type.itertuples(index=False):
        pitch_type = "<NA>" if pd.isna(row.pitch_type) else row.pitch_type
        lines.append(f"| `{pitch_type}` | {row.count:,} | {row.mean:.6f} | {row.sum:.6f} |")

    REPORT_PATH.write_text("\n".join(lines), encoding="utf-8")


def main() -> None:
    df = pd.read_parquet(INPUT_PATH)

    required = set(EVENT_COLUMNS.values())
    missing = sorted(required.difference(df.columns))
    if missing:
        raise ValueError(f"Missing required columns: {missing}")

    woba_event = derive_woba_event(df)
    df["woba_value"] = woba_event.map(WOBA_WEIGHTS).fillna(0.0).astype("float64")

    df.to_parquet(OUTPUT_PATH, index=False)
    write_report(df, woba_event)

    print(f"Identified event/result columns: {EVENT_COLUMNS}")
    print(f"Wrote updated dataframe: {OUTPUT_PATH}")
    print(f"Wrote validation report: {REPORT_PATH}")
    print("\nDerived event counts:")
    print(woba_event.value_counts(dropna=False).to_string())
    print("\nwoba_value summary:")
    print(df["woba_value"].describe().to_string())
    print("\nAverage woba_value by pitch_type:")
    print(
        df.groupby(EVENT_COLUMNS["pitch_type"], dropna=False)["woba_value"]
        .agg(count="size", mean="mean")
        .sort_values(["mean", "count"], ascending=[False, False])
        .to_string()
    )


if __name__ == "__main__":
    main()
