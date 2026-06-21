from __future__ import annotations

from pathlib import Path

import pandas as pd


PITCH_DATA_PATH = Path("data/processed/2026-data-with-woba-xwoba.parquet")
SCORE_PATH = Path("data/processed/pitch_value_scores.csv")
OUTPUT_PATH = Path("data/processed/movement_score_inputs.csv")

MOVEMENT_COLUMNS = {
    "ivb": "pitch_movement_induced_vert_break_x",
    "hb": "pitch_movement_horz_break_x",
    "spin_rate": "pitch_release_spin_rate_x",
    "velocity": "pitch_release_rel_speed_x",
    "extension": "pitch_release_extension_x",
    "release_height": "pitch_release_rel_height_x",
    "release_side": "pitch_release_rel_side_x",
}
PREDICTORS = list(MOVEMENT_COLUMNS)
PITCH_TYPE_NORMALIZATION = {
    "Fastball": "Four-Seam",
    "Two-Seam": "Sinker",
}


def normalize_pitch_type(series: pd.Series) -> pd.Series:
    return series.astype("string").replace(PITCH_TYPE_NORMALIZATION)


def pitcher_id_key(series: pd.Series) -> pd.Series:
    numeric = pd.to_numeric(series, errors="coerce")
    key = numeric.round().astype("Int64").astype("string")
    return key.fillna("<MISSING>")


def main() -> None:
    pitch_cols = [
        "pitcher_name",
        "pitcher_id",
        "pitcher_team",
        "pitch_type",
        *MOVEMENT_COLUMNS.values(),
    ]
    pitch_df = pd.read_parquet(PITCH_DATA_PATH, columns=pitch_cols)
    pitch_df["pitch_type"] = normalize_pitch_type(pitch_df["pitch_type"])
    pitch_df["pitcher_id_key"] = pitcher_id_key(pitch_df["pitcher_id"])
    for output_name, source_name in MOVEMENT_COLUMNS.items():
        pitch_df[output_name] = pd.to_numeric(pitch_df[source_name], errors="coerce")

    movement = (
        pitch_df.groupby(["pitcher_name", "pitcher_id_key", "pitcher_team", "pitch_type"], dropna=False)
        [PREDICTORS]
        .mean()
        .reset_index()
    )

    scores = pd.read_csv(SCORE_PATH)
    scores["pitcher_id_key"] = pitcher_id_key(scores["pitcher_id"])
    merge_keys = ["pitcher_name", "pitcher_id_key", "pitcher_team", "pitch_type"]
    merged = scores.merge(movement, on=merge_keys, how="left", validate="one_to_one")
    merged = merged.dropna(subset=["pitch_value_20_80", *PREDICTORS]).copy()

    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    merged.to_csv(OUTPUT_PATH, index=False)
    print(f"Wrote movement score inputs: {OUTPUT_PATH}")
    print(f"Rows with movement traits: {len(merged):,}")


if __name__ == "__main__":
    main()
