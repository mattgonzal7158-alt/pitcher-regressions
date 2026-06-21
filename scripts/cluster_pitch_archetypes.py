from __future__ import annotations

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from sklearn.cluster import KMeans
from sklearn.decomposition import PCA
from sklearn.metrics import silhouette_score
from sklearn.preprocessing import StandardScaler


INPUT_PATH = Path("data/processed/movement_score_inputs.csv")
OUTPUT_PATH = Path("data/processed/pitch_movement_archetypes.csv")
CLUSTER_SUMMARY_PATH = Path("data/processed/pitch_movement_archetype_summary.csv")
HIGH_ARCHETYPE_PITCHES_PATH = Path("data/processed/highest_performing_archetype_pitches.csv")
UNDERVALUED_PATH = Path("data/processed/undervalued_movement_pitches.csv")
REPORT_PATH = Path("reports/pitch_movement_archetype_report.md")
PLOTS_DIR = Path("plots/pitch_movement_archetypes")

FEATURES = ["ivb", "hb", "spin_rate", "velocity", "extension"]
SCORE_COLUMN = "pitch_value_20_80"
RANDOM_STATE = 42
MIN_K = 2
MAX_K = 10


def percentile_rank(series: pd.Series) -> pd.Series:
    return series.rank(method="average", pct=True).mul(100)


def write_csv_safely(df: pd.DataFrame, path: Path) -> Path:
    try:
        df.to_csv(path, index=False)
        return path
    except PermissionError:
        fallback = path.with_name(f"{path.stem}_updated{path.suffix}")
        df.to_csv(fallback, index=False)
        return fallback


def choose_cluster_count(x_scaled: np.ndarray) -> tuple[int, pd.DataFrame]:
    rows = []
    for k in range(MIN_K, MAX_K + 1):
        model = KMeans(n_clusters=k, random_state=RANDOM_STATE, n_init=50)
        labels = model.fit_predict(x_scaled)
        rows.append(
            {
                "k": k,
                "inertia": model.inertia_,
                "silhouette": silhouette_score(x_scaled, labels),
            }
        )
    results = pd.DataFrame(rows)
    best_k = int(results.sort_values(["silhouette", "k"], ascending=[False, True]).iloc[0]["k"])
    return best_k, results


def label_cluster(row: pd.Series) -> str:
    pitch_mix = str(row["top_pitch_types"])
    ivb = row["ivb"]
    hb = row["hb"]
    velo = row["velocity"]
    spin = row["spin_rate"]
    ext = row["extension"]
    abs_hb = abs(hb)

    if ivb >= 15 and velo >= 88:
        return "Riding Power Fastballs"
    if ivb >= 13 and velo < 88:
        return "Riding Shape / Lower Velo"
    if ivb <= 1 and abs_hb >= 8 and velo <= 83:
        return "Sweepy Breaking Balls"
    if ivb <= 3 and abs_hb < 8 and spin >= 2200:
        return "Tight High-Spin Breakers"
    if hb >= 10 and velo >= 86:
        return "Arm-Side Run Power"
    if hb <= -8 and velo >= 84:
        return "Glove-Side Power Break"
    if ext >= 6.2 and velo >= 86:
        return "Extension-Driven Power"
    if "Changeup" in pitch_mix or "Splitter" in pitch_mix:
        return "Soft-Speed Separation"
    return "Balanced Movement Mix"


def short_trait_summary(row: pd.Series) -> str:
    traits = []
    if row["ivb"] >= 15:
        traits.append("plus ride")
    elif row["ivb"] <= 3:
        traits.append("low ride/drop")
    if abs(row["hb"]) >= 10:
        traits.append("big horizontal")
    if row["spin_rate"] >= 2300:
        traits.append("high spin")
    if row["velocity"] >= 89:
        traits.append("power velocity")
    elif row["velocity"] <= 81:
        traits.append("soft velo")
    if row["extension"] >= 6.2:
        traits.append("extension")
    return ", ".join(traits) if traits else "average movement blend"


def build_summary(df: pd.DataFrame) -> pd.DataFrame:
    pitch_mix = (
        df.groupby("cluster")["pitch_type"]
        .apply(lambda s: ", ".join(s.value_counts().head(3).index.astype(str)))
        .rename("top_pitch_types")
    )
    summary = (
        df.groupby("cluster")
        .agg(
            pitch_count=("pitch_count", "sum"),
            pitch_instances=("pitch_type", "size"),
            avg_pitch_value=(SCORE_COLUMN, "mean"),
            median_pitch_value=(SCORE_COLUMN, "median"),
            avg_xwoba=("xwoba_frontier", "mean"),
            ivb=("ivb", "mean"),
            hb=("hb", "mean"),
            spin_rate=("spin_rate", "mean"),
            velocity=("velocity", "mean"),
            extension=("extension", "mean"),
        )
        .join(pitch_mix)
        .reset_index()
    )
    summary["archetype"] = summary.apply(label_cluster, axis=1)
    used = {}
    labels = []
    for label in summary["archetype"]:
        count = used.get(label, 0) + 1
        used[label] = count
        labels.append(label if count == 1 else f"{label} {count}")
    summary["archetype"] = labels
    summary["cluster_rank"] = summary["avg_pitch_value"].rank(method="first", ascending=False).astype(int)
    return summary.sort_values("cluster_rank")


def movement_quality_score(df: pd.DataFrame, summary: pd.DataFrame) -> pd.Series:
    cluster_quality = summary.set_index("cluster")["avg_pitch_value"]
    raw = df["movement_predicted_pvs"] * 0.65 + df["cluster"].map(cluster_quality) * 0.35
    return percentile_rank(raw)


def make_plots(scored: pd.DataFrame, summary: pd.DataFrame, k_results: pd.DataFrame) -> None:
    PLOTS_DIR.mkdir(exist_ok=True)

    fig, ax1 = plt.subplots(figsize=(8, 6))
    ax1.plot(k_results["k"], k_results["silhouette"], marker="o", color="#2f6690")
    ax1.set_xlabel("Number of clusters")
    ax1.set_ylabel("Silhouette score")
    ax1.set_title("Cluster Count Selection")
    ax2 = ax1.twinx()
    ax2.plot(k_results["k"], k_results["inertia"], marker="s", color="#b44b35")
    ax2.set_ylabel("Inertia")
    fig.tight_layout()
    fig.savefig(PLOTS_DIR / "cluster_count_selection.png", dpi=160)
    plt.close(fig)

    fig, ax = plt.subplots(figsize=(9, 7))
    scatter = ax.scatter(
        scored["hb"],
        scored["ivb"],
        c=scored["cluster_rank"],
        cmap="viridis_r",
        s=40,
        alpha=0.75,
        linewidths=0,
    )
    ax.axhline(0, color="#666666", linewidth=0.8)
    ax.axvline(0, color="#666666", linewidth=0.8)
    ax.set_title("Pitch Movement Archetypes: HB vs IVB")
    ax.set_xlabel("HB")
    ax.set_ylabel("IVB")
    fig.colorbar(scatter, ax=ax, label="Archetype rank")
    fig.tight_layout()
    fig.savefig(PLOTS_DIR / "archetypes_hb_ivb.png", dpi=160)
    plt.close(fig)

    fig, ax = plt.subplots(figsize=(9, 7))
    scatter = ax.scatter(
        scored["velocity"],
        scored["spin_rate"],
        c=scored["cluster_rank"],
        cmap="viridis_r",
        s=40,
        alpha=0.75,
        linewidths=0,
    )
    ax.set_title("Pitch Movement Archetypes: Velocity vs Spin")
    ax.set_xlabel("Velocity")
    ax.set_ylabel("Spin Rate")
    fig.colorbar(scatter, ax=ax, label="Archetype rank")
    fig.tight_layout()
    fig.savefig(PLOTS_DIR / "archetypes_velocity_spin.png", dpi=160)
    plt.close(fig)

    pca = PCA(n_components=2, random_state=RANDOM_STATE)
    pcs = pca.fit_transform(StandardScaler().fit_transform(scored[FEATURES]))
    fig, ax = plt.subplots(figsize=(9, 7))
    scatter = ax.scatter(
        pcs[:, 0],
        pcs[:, 1],
        c=scored["cluster_rank"],
        cmap="viridis_r",
        s=40,
        alpha=0.75,
        linewidths=0,
    )
    ax.set_title("Movement Archetypes in PCA Space")
    ax.set_xlabel("PC1")
    ax.set_ylabel("PC2")
    fig.colorbar(scatter, ax=ax, label="Archetype rank")
    fig.tight_layout()
    fig.savefig(PLOTS_DIR / "archetypes_pca.png", dpi=160)
    plt.close(fig)

    fig, ax = plt.subplots(figsize=(10, 6))
    plot_summary = summary.sort_values("avg_pitch_value", ascending=True)
    ax.barh(plot_summary["archetype"], plot_summary["avg_pitch_value"], color="#467599")
    ax.axvline(scored[SCORE_COLUMN].mean(), color="#333333", linewidth=1)
    ax.set_title("Average Pitch Value by Movement Archetype")
    ax.set_xlabel("Average Pitch Value Score")
    fig.tight_layout()
    fig.savefig(PLOTS_DIR / "archetype_pitch_value.png", dpi=160)
    plt.close(fig)


def table_lines(df: pd.DataFrame, rows: int, include_archetype: bool = True) -> list[str]:
    cols = [
        "Rank",
        "Pitcher",
        "Team",
        "Pitch",
        "Pitches",
        "PVS",
        "xwOBA",
        "IVB",
        "HB",
        "Spin",
        "Velo",
        "Ext",
    ]
    if include_archetype:
        cols.append("Archetype")
    lines = ["| " + " | ".join(cols) + " |", "|" + "|".join(["---"] * len(cols)) + "|"]
    for i, row in enumerate(df.head(rows).itertuples(index=False), start=1):
        values = [
            str(i),
            str(row.pitcher_name),
            str(row.pitcher_team),
            str(row.pitch_type),
            f"{int(row.pitch_count):,}",
            f"{row.pitch_value_20_80:.1f}",
            f"{row.xwoba_frontier:.3f}",
            f"{row.ivb:.1f}",
            f"{row.hb:.1f}",
            f"{row.spin_rate:.0f}",
            f"{row.velocity:.1f}",
            f"{row.extension:.2f}",
        ]
        if include_archetype:
            values.append(str(row.archetype))
        lines.append("| " + " | ".join(values) + " |")
    return lines


def scouting_report_lines(top20: pd.DataFrame) -> list[str]:
    lines = []
    for i, row in enumerate(top20.itertuples(index=False), start=1):
        strengths = short_trait_summary(pd.Series(row._asdict()))
        result = (
            f"{i}. **{row.pitcher_name}, {row.pitcher_team} {row.pitch_type}** "
            f"({row.archetype}): PVS {row.pitch_value_20_80:.1f}, xwOBA {row.xwoba_frontier:.3f}. "
            f"Shape: IVB {row.ivb:.1f}, HB {row.hb:.1f}, {row.velocity:.1f} mph, "
            f"{row.spin_rate:.0f} rpm, {row.extension:.2f} ft extension. "
            f"Scouting read: {strengths}; current results place it #{int(row.overall_rank)} overall "
            f"and #{int(row.pitch_type_rank)} within its pitch type."
        )
        lines.append(result)
    return lines


def write_report(
    scored: pd.DataFrame,
    summary: pd.DataFrame,
    k_results: pd.DataFrame,
    best_k: int,
    high_archetype_pitches: pd.DataFrame,
    undervalued: pd.DataFrame,
) -> None:
    top20 = scored.sort_values("overall_rank").head(20)
    top_archetypes = summary.sort_values("cluster_rank").head(2)

    lines = [
        "# Frontier League Movement Archetypes",
        "",
        f"- Input file: `{INPUT_PATH}`",
        f"- Scored output: `{OUTPUT_PATH}`",
        f"- Cluster summary: `{CLUSTER_SUMMARY_PATH}`",
        f"- Highest-performing archetype pitch list: `{HIGH_ARCHETYPE_PITCHES_PATH}`",
        f"- Undervalued pitch list: `{UNDERVALUED_PATH}`",
        f"- Qualified pitcher-pitch types clustered: {len(scored):,}",
        f"- Features clustered: IVB, HB, spin rate, velocity, extension",
        f"- Selected cluster count: {best_k}",
        f"- Full methodology write-up: `reports/FRONTIER_PITCH_VALUE_METHODOLOGY.md`",
        "",
        "## How To Read This Report",
        "",
        "Higher Pitch Value Score is better. It means the pitch has the outcome profile associated with lower expected xwOBA damage. Archetypes are movement-shape groups, not direct pitcher grades.",
        "",
        "The cluster labels describe the average movement identity of each group. Average Pitch Value Score by cluster tells us which movement families performed best in this dataset, but individual pitches within a cluster can still vary widely based on command, usage, sequencing, and sample size.",
        "",
        "## Cluster Count Test",
        "",
        "| k | Inertia | Silhouette |",
        "|---:|---:|---:|",
    ]
    for row in k_results.itertuples(index=False):
        selected = " **selected**" if int(row.k) == best_k else ""
        lines.append(f"| {int(row.k)} | {row.inertia:.2f} | {row.silhouette:.4f}{selected} |")

    lines.extend(
        [
            "",
            "## Archetype Summary",
            "",
            "| Rank | Archetype | Pitches | Instances | Avg PVS | Avg xwOBA | IVB | HB | Spin | Velo | Ext | Common Pitch Types |",
            "|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|",
        ]
    )
    for row in summary.sort_values("cluster_rank").itertuples(index=False):
        lines.append(
            f"| {row.cluster_rank} | `{row.archetype}` | {int(row.pitch_count):,} | "
            f"{int(row.pitch_instances):,} | {row.avg_pitch_value:.1f} | {row.avg_xwoba:.3f} | "
            f"{row.ivb:.1f} | {row.hb:.1f} | {row.spin_rate:.0f} | {row.velocity:.1f} | "
            f"{row.extension:.2f} | {row.top_pitch_types} |"
        )

    lines.extend(["", "## Highest-Performing Archetypes", ""])
    for row in top_archetypes.itertuples(index=False):
        lines.append(
            f"- `{row.archetype}`: average PVS {row.avg_pitch_value:.1f}, avg xwOBA {row.avg_xwoba:.3f}, "
            f"typical shape {row.ivb:.1f} IVB / {row.hb:.1f} HB at {row.velocity:.1f} mph."
        )

    lines.extend(
        [
            "",
            "## Pitchers in Highest-Performing Archetypes",
            "",
            *table_lines(high_archetype_pitches.sort_values(["cluster_rank", "overall_rank"]), rows=len(high_archetype_pitches)),
            "",
            "## Undervalued Movement Pitches",
            "",
            "Definition: movement quality percentile at least 75, with Pitch Value Score at or below league average.",
            "",
        ]
    )
    if undervalued.empty:
        lines.append("No pitches met the undervalued definition.")
    else:
        undervalued_display = undervalued.sort_values(
            ["movement_quality_0_100", SCORE_COLUMN], ascending=[False, True]
        )
        lines.extend(table_lines(undervalued_display, rows=min(30, len(undervalued_display))))

    lines.extend(
        [
            "",
            "## Top 20 Scouting Reports",
            "",
            *scouting_report_lines(top20),
            "",
            "## Plots",
            "",
            f"- `{PLOTS_DIR / 'cluster_count_selection.png'}`",
            f"- `{PLOTS_DIR / 'archetypes_hb_ivb.png'}`",
            f"- `{PLOTS_DIR / 'archetypes_velocity_spin.png'}`",
            f"- `{PLOTS_DIR / 'archetypes_pca.png'}`",
            f"- `{PLOTS_DIR / 'archetype_pitch_value.png'}`",
        ]
    )

    REPORT_PATH.write_text("\n".join(lines), encoding="utf-8")


def main() -> None:
    df = pd.read_csv(INPUT_PATH)
    model_df = df.dropna(subset=[*FEATURES, SCORE_COLUMN]).copy()

    scaler = StandardScaler()
    x_scaled = scaler.fit_transform(model_df[FEATURES])
    best_k, k_results = choose_cluster_count(x_scaled)
    model = KMeans(n_clusters=best_k, random_state=RANDOM_STATE, n_init=100)
    model_df["cluster"] = model.fit_predict(x_scaled)

    # Movement-only quality proxy: projection toward the actual PVS direction
    # in standardized movement space.
    z = pd.DataFrame(x_scaled, columns=FEATURES, index=model_df.index)
    movement_weights = np.linalg.lstsq(
        np.column_stack([np.ones(len(z)), z.to_numpy()]),
        model_df[SCORE_COLUMN].to_numpy(),
        rcond=None,
    )[0]
    model_df["movement_predicted_pvs"] = (
        np.column_stack([np.ones(len(z)), z.to_numpy()]) @ movement_weights
    )

    summary = build_summary(model_df)
    model_df = model_df.merge(summary[["cluster", "archetype", "cluster_rank"]], on="cluster", how="left")
    model_df["movement_quality_0_100"] = movement_quality_score(model_df, summary)
    model_df["archetype_pitch_value_rank"] = (
        model_df.groupby("cluster")[SCORE_COLUMN].rank(method="first", ascending=False).astype(int)
    )

    high_clusters = summary.sort_values("cluster_rank").head(2)["cluster"].tolist()
    high_archetype_pitches = model_df.loc[model_df["cluster"].isin(high_clusters)].copy()
    undervalued = model_df.loc[
        model_df["movement_quality_0_100"].ge(75)
        & model_df[SCORE_COLUMN].le(model_df[SCORE_COLUMN].mean())
    ].copy()

    make_plots(model_df, summary, k_results)
    output_path = write_csv_safely(model_df.sort_values("overall_rank"), OUTPUT_PATH)
    summary_path = write_csv_safely(summary, CLUSTER_SUMMARY_PATH)
    high_path = write_csv_safely(
        high_archetype_pitches.sort_values(["cluster_rank", "overall_rank"]),
        HIGH_ARCHETYPE_PITCHES_PATH,
    )
    undervalued_path = write_csv_safely(
        undervalued.sort_values(["movement_quality_0_100", SCORE_COLUMN], ascending=[False, True]),
        UNDERVALUED_PATH,
    )
    write_report(model_df, summary, k_results, best_k, high_archetype_pitches, undervalued)

    print(f"Selected clusters: {best_k}")
    print(f"Wrote clustered pitches: {output_path}")
    print(f"Wrote cluster summary: {summary_path}")
    print(f"Wrote high archetype pitch list: {high_path}")
    print(f"Wrote undervalued pitch list: {undervalued_path}")
    print(f"Wrote report: {REPORT_PATH}")
    print(f"Wrote plots to: {PLOTS_DIR}")
    print("\nArchetype summary:")
    print(
        summary[
            [
                "cluster_rank",
                "archetype",
                "pitch_instances",
                "avg_pitch_value",
                "avg_xwoba",
                "ivb",
                "hb",
                "spin_rate",
                "velocity",
                "extension",
                "top_pitch_types",
            ]
        ].to_string(index=False)
    )


if __name__ == "__main__":
    main()
