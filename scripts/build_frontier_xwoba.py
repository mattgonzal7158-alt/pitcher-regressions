from __future__ import annotations

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from sklearn.compose import ColumnTransformer
from sklearn.impute import SimpleImputer
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder


INPUT_PATH = Path("data/processed/2026-data-with-woba.parquet")
OUTPUT_PATH = Path("data/processed/2026-data-with-woba-xwoba.parquet")
REPORT_PATH = Path("reports/frontier_xwoba_model_report.md")
PLOTS_DIR = Path("plots/frontier_xwoba")

TARGET_COLUMN = "woba_value"
PREDICTION_COLUMN = "xwoba_frontier"

COLUMNS = {
    "exit_velocity": "hit_launch_exit_speed_y",
    "launch_angle": "hit_launch_angle_y",
    "spray_angle": "hit_launch_direction_y",
    "batted_ball_type": "hit_type",
}

RANDOM_STATE = 42
TEST_SIZE = 0.20


def root_mean_squared_error(y_true: pd.Series, y_pred: np.ndarray) -> float:
    return float(np.sqrt(mean_squared_error(y_true, y_pred)))


def require_columns(df: pd.DataFrame) -> None:
    required = [TARGET_COLUMN, *COLUMNS.values()]
    missing = sorted(set(required).difference(df.columns))
    if missing:
        raise ValueError(f"Missing required columns: {missing}")


def build_modeling_frame(df: pd.DataFrame) -> pd.DataFrame:
    model_df = pd.DataFrame(
        {
            "exit_velocity": pd.to_numeric(df[COLUMNS["exit_velocity"]], errors="coerce"),
            "launch_angle": pd.to_numeric(df[COLUMNS["launch_angle"]], errors="coerce"),
            "spray_angle": pd.to_numeric(df[COLUMNS["spray_angle"]], errors="coerce"),
            "batted_ball_type": df[COLUMNS["batted_ball_type"]]
            .astype("string")
            .fillna("Unknown"),
            TARGET_COLUMN: pd.to_numeric(df[TARGET_COLUMN], errors="coerce"),
        },
        index=df.index,
    )

    batted_ball_mask = model_df[["exit_velocity", "launch_angle"]].notna().all(axis=1)
    model_df = model_df.loc[batted_ball_mask].copy()
    model_df = model_df.dropna(subset=[TARGET_COLUMN])
    model_df["launch_angle_squared"] = model_df["launch_angle"] ** 2
    return model_df


def make_preprocessor(numeric_features: list[str], categorical_features: list[str]) -> ColumnTransformer:
    numeric_transformer = Pipeline(
        steps=[
            ("imputer", SimpleImputer(strategy="median")),
        ]
    )
    categorical_transformer = Pipeline(
        steps=[
            ("imputer", SimpleImputer(strategy="constant", fill_value="Unknown")),
            ("onehot", OneHotEncoder(handle_unknown="ignore")),
        ]
    )

    return ColumnTransformer(
        transformers=[
            ("numeric", numeric_transformer, numeric_features),
            ("categorical", categorical_transformer, categorical_features),
        ]
    )


def make_model_configs() -> dict[str, Pipeline]:
    linear_features = ["exit_velocity", "launch_angle"]
    quadratic_features = ["exit_velocity", "launch_angle", "launch_angle_squared"]
    spray_features = ["exit_velocity", "launch_angle", "spray_angle"]
    categorical_features = ["batted_ball_type"]

    linear_model = Pipeline(
        steps=[
            ("preprocess", make_preprocessor(linear_features, categorical_features)),
            ("model", LinearRegression()),
        ]
    )

    quadratic_model = Pipeline(
        steps=[
            ("preprocess", make_preprocessor(quadratic_features, categorical_features)),
            ("model", LinearRegression()),
        ]
    )

    spray_model = Pipeline(
        steps=[
            ("preprocess", make_preprocessor(spray_features, categorical_features)),
            ("model", LinearRegression()),
        ]
    )

    return {
        "linear_ev_la_batted_type": linear_model,
        "linear_ev_la_la2_batted_type": quadratic_model,
        "linear_ev_la_spray_batted_type": spray_model,
    }


def evaluate_models(model_df: pd.DataFrame) -> tuple[pd.DataFrame, str, dict[str, Pipeline]]:
    features = ["exit_velocity", "launch_angle", "spray_angle", "batted_ball_type"]
    if "launch_angle_squared" in model_df.columns:
        features.append("launch_angle_squared")
    x_train, x_test, y_train, y_test = train_test_split(
        model_df[features],
        model_df[TARGET_COLUMN],
        test_size=TEST_SIZE,
        random_state=RANDOM_STATE,
    )

    rows = []
    models = make_model_configs()
    for name, model in models.items():
        model.fit(x_train, y_train)
        train_pred = np.clip(model.predict(x_train), 0.0, None)
        test_pred = np.clip(model.predict(x_test), 0.0, None)
        rows.append(
            {
                "model": name,
                "train_r_squared": r2_score(y_train, train_pred),
                "train_rmse": root_mean_squared_error(y_train, train_pred),
                "test_r_squared": r2_score(y_test, test_pred),
                "test_rmse": root_mean_squared_error(y_test, test_pred),
            }
        )

    results = pd.DataFrame(rows).sort_values(
        ["test_rmse", "test_r_squared"], ascending=[True, False]
    )
    best_model_name = str(results.iloc[0]["model"])
    return results, best_model_name, models


def save_plots(model_df: pd.DataFrame) -> None:
    PLOTS_DIR.mkdir(exist_ok=True)
    plot_df = model_df.copy()

    fig, ax = plt.subplots(figsize=(9, 6))
    hb = ax.hexbin(
        plot_df["exit_velocity"],
        plot_df[TARGET_COLUMN],
        gridsize=45,
        mincnt=1,
        cmap="viridis",
    )
    ax.set_title("wOBA Value by Exit Velocity")
    ax.set_xlabel("Exit Velocity")
    ax.set_ylabel("woba_value")
    fig.colorbar(hb, ax=ax, label="Batted balls")
    fig.tight_layout()
    fig.savefig(PLOTS_DIR / "woba_by_exit_velocity.png", dpi=160)
    plt.close(fig)

    fig, ax = plt.subplots(figsize=(9, 6))
    hb = ax.hexbin(
        plot_df["launch_angle"],
        plot_df[TARGET_COLUMN],
        gridsize=45,
        mincnt=1,
        cmap="magma",
    )
    ax.set_title("wOBA Value by Launch Angle")
    ax.set_xlabel("Launch Angle")
    ax.set_ylabel("woba_value")
    fig.colorbar(hb, ax=ax, label="Batted balls")
    fig.tight_layout()
    fig.savefig(PLOTS_DIR / "woba_by_launch_angle.png", dpi=160)
    plt.close(fig)

    fig, ax = plt.subplots(figsize=(9, 6))
    hb = ax.hexbin(
        plot_df["spray_angle"],
        plot_df[TARGET_COLUMN],
        gridsize=45,
        mincnt=1,
        cmap="cividis",
    )
    ax.set_title("wOBA Value by Spray Angle")
    ax.set_xlabel("Spray Angle")
    ax.set_ylabel("woba_value")
    fig.colorbar(hb, ax=ax, label="Batted balls")
    fig.tight_layout()
    fig.savefig(PLOTS_DIR / "woba_by_spray_angle.png", dpi=160)
    plt.close(fig)

    by_type = (
        plot_df.groupby("batted_ball_type", dropna=False)[TARGET_COLUMN]
        .agg(count="size", mean="mean")
        .sort_values("mean", ascending=False)
    )
    fig, ax = plt.subplots(figsize=(9, 6))
    by_type["mean"].plot(kind="bar", ax=ax, color="#4c78a8")
    ax.set_title("Average wOBA Value by Batted Ball Type")
    ax.set_xlabel("Batted Ball Type")
    ax.set_ylabel("Average woba_value")
    for index, (_, row) in enumerate(by_type.iterrows()):
        ax.text(index, row["mean"], f"n={int(row['count']):,}", ha="center", va="bottom", fontsize=8)
    fig.tight_layout()
    fig.savefig(PLOTS_DIR / "woba_by_batted_ball_type.png", dpi=160)
    plt.close(fig)

    fig, ax = plt.subplots(figsize=(9, 7))
    scatter = ax.scatter(
        plot_df["exit_velocity"],
        plot_df["launch_angle"],
        c=plot_df[TARGET_COLUMN],
        s=8,
        alpha=0.45,
        cmap="plasma",
        linewidths=0,
    )
    ax.set_title("Batted Ball wOBA by Exit Velocity and Launch Angle")
    ax.set_xlabel("Exit Velocity")
    ax.set_ylabel("Launch Angle")
    fig.colorbar(scatter, ax=ax, label="woba_value")
    fig.tight_layout()
    fig.savefig(PLOTS_DIR / "woba_ev_launch_scatter.png", dpi=160)
    plt.close(fig)


def write_report(
    df: pd.DataFrame,
    model_df: pd.DataFrame,
    results: pd.DataFrame,
    best_model_name: str,
) -> None:
    selected = results.loc[results["model"].eq(best_model_name)].iloc[0]
    by_type = (
        model_df.groupby("batted_ball_type", dropna=False)[TARGET_COLUMN]
        .agg(count="size", mean="mean")
        .sort_values(["mean", "count"], ascending=[False, False])
        .reset_index()
    )

    lines = [
        "# Frontier League xwOBA Model Report",
        "",
        f"- Input file: `{INPUT_PATH}`",
        f"- Output file: `{OUTPUT_PATH}`",
        f"- Rows in source dataframe: {len(df):,}",
        f"- Batted balls modeled: {len(model_df):,}",
        f"- Prediction column: `{PREDICTION_COLUMN}`",
        f"- Selected model: `{best_model_name}`",
        "",
        "## Columns Identified",
        "",
        "| Feature | Column Used | Note |",
        "|---|---|---|",
        f"| Exit Velocity | `{COLUMNS['exit_velocity']}` | Populated launch-tracking column; `_x` counterpart is empty in this file. |",
        f"| Launch Angle | `{COLUMNS['launch_angle']}` | Populated launch-tracking column; `_x` counterpart is empty in this file. |",
        f"| Spray Angle | `{COLUMNS['spray_angle']}` | Populated launch direction column. |",
        f"| Batted Ball Type | `{COLUMNS['batted_ball_type']}` | Normalized tagged/auto hit type; missing values are modeled as `Unknown`. |",
        f"| Target | `{TARGET_COLUMN}` | Previously created Frontier League wOBA value. |",
        "",
        "## Model Performance",
        "",
        "| Model | Train R-squared | Train RMSE | Test R-squared | Test RMSE |",
        "|---|---:|---:|---:|---:|",
    ]

    for row in results.itertuples(index=False):
        lines.append(
            f"| `{row.model}` | {row.train_r_squared:.6f} | {row.train_rmse:.6f} | "
            f"{row.test_r_squared:.6f} | {row.test_rmse:.6f} |"
        )

    lines.extend(
        [
            "",
            "## Why This Model Was Selected",
            "",
            (
                f"`{best_model_name}` was selected because it had the lowest holdout RMSE "
                f"({selected.test_rmse:.6f}) and the highest/competitive holdout R-squared "
                f"({selected.test_r_squared:.6f}) among the candidate models. RMSE was used "
                "as the primary criterion because the prediction task is to assign calibrated "
                "expected wOBA values to individual batted balls; lower prediction error is more "
                "directly useful than a slightly more complex specification with no error gain."
            ),
            "",
            "## Batted Ball Type Summary",
            "",
            "| Batted Ball Type | Count | Average woba_value |",
            "|---|---:|---:|",
        ]
    )
    for row in by_type.itertuples(index=False):
        lines.append(f"| `{row.batted_ball_type}` | {row.count:,} | {row.mean:.6f} |")

    lines.extend(
        [
            "",
            "## Exploratory Plots",
            "",
            f"- `{PLOTS_DIR / 'woba_by_exit_velocity.png'}`",
            f"- `{PLOTS_DIR / 'woba_by_launch_angle.png'}`",
            f"- `{PLOTS_DIR / 'woba_by_spray_angle.png'}`",
            f"- `{PLOTS_DIR / 'woba_by_batted_ball_type.png'}`",
            f"- `{PLOTS_DIR / 'woba_ev_launch_scatter.png'}`",
        ]
    )

    REPORT_PATH.write_text("\n".join(lines), encoding="utf-8")


def main() -> None:
    df = pd.read_parquet(INPUT_PATH)
    require_columns(df)

    model_df = build_modeling_frame(df)
    save_plots(model_df)
    results, best_model_name, models = evaluate_models(model_df)

    best_model = models[best_model_name]
    feature_columns = [
        "exit_velocity",
        "launch_angle",
        "launch_angle_squared",
        "spray_angle",
        "batted_ball_type",
    ]
    best_model.fit(model_df[feature_columns], model_df[TARGET_COLUMN])

    df[PREDICTION_COLUMN] = np.nan
    predictions = np.clip(best_model.predict(model_df[feature_columns]), 0.0, None)
    df.loc[model_df.index, PREDICTION_COLUMN] = predictions

    df.to_parquet(OUTPUT_PATH, index=False)
    write_report(df, model_df, results, best_model_name)

    print(f"Identified columns: {COLUMNS}")
    print(f"Batted balls modeled: {len(model_df):,}")
    print(f"Selected model: {best_model_name}")
    print(results.to_string(index=False))
    print(f"Wrote updated dataframe: {OUTPUT_PATH}")
    print(f"Wrote report: {REPORT_PATH}")
    print(f"Wrote plots to: {PLOTS_DIR}")


if __name__ == "__main__":
    main()
