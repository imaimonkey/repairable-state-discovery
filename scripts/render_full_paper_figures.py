from __future__ import annotations

import argparse
import csv
import json
from pathlib import Path
from typing import Any

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch


ROOT = Path(__file__).resolve().parents[1]


def _csv(path: Path) -> list[dict[str, str]]:
    with path.open(newline="", encoding="utf-8") as fh:
        return list(csv.DictReader(fh))


def _save(fig: plt.Figure, path: Path) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    fig.savefig(path.with_suffix(".pdf"), bbox_inches="tight")
    fig.savefig(path.with_suffix(".png"), dpi=220, bbox_inches="tight")
    plt.close(fig)


def render(aggregate_path: Path, figure_data: Path, output_dir: Path) -> None:
    output_dir.mkdir(parents=True, exist_ok=True)
    aggregate = json.loads(aggregate_path.read_text(encoding="utf-8"))

    fig, ax = plt.subplots(figsize=(8, 2.5))
    ax.axis("off")
    labels = ["Question + mask", "Diffusion\ntrajectory", "Checkpoint\nsnapshots", "Repair probes", "Selector +\npass@k"]
    xs = [0.08, 0.28, 0.48, 0.68, 0.88]
    for x, label in zip(xs, labels):
        box = FancyBboxPatch((x - 0.08, 0.35), 0.16, 0.3, boxstyle="round,pad=0.02", linewidth=1.2, facecolor="#e8f0fe", edgecolor="#356ac3")
        ax.add_patch(box)
        ax.text(x, 0.5, label, ha="center", va="center", fontsize=9)
    for left, right in zip(xs[:-1], xs[1:]):
        ax.add_patch(FancyArrowPatch((left + 0.085, 0.5), (right - 0.085, 0.5), arrowstyle="->", mutation_scale=14, linewidth=1.0, color="#555"))
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.set_title("State-level repairability protocol", fontsize=11)
    _save(fig, output_dir / "protocol_overview")

    curves = _csv(figure_data / "repair_gain_curves.csv")
    keep = {"math500_full_llada8b_fast", "gsm8k_full_llada8b_fast", "math500_full_dream_v0_instruct_7b", "gsm8k_full_dream_v0_instruct_7b"}
    fig, ax = plt.subplots(figsize=(5.5, 3.4))
    grouped: dict[str, list[dict[str, str]]] = {}
    for row in curves:
        if row.get("run_name") in keep:
            grouped.setdefault(row["run_name"], []).append(row)
    for name, rows in grouped.items():
        rows.sort(key=lambda r: int(r["step_index"]))
        ax.plot([int(r["step_index"]) for r in rows], [float(r["mean_correction_rate"]) for r in rows], marker="o", ms=2.5, label=name.replace("_llada8b_fast", "").replace("_v0_instruct_7b", "_dream"))
    ax.set_xlabel("Checkpoint step")
    ax.set_ylabel("Mean correction rate")
    ax.set_title("Repairability across refinement")
    ax.legend(fontsize=7)
    ax.grid(alpha=0.25)
    _save(fig, output_dir / "repair_gain_curves")

    hist = _csv(figure_data / "best_step_histograms.csv")
    fig, ax = plt.subplots(figsize=(5.5, 3.4))
    for name in ["math500_full_llada8b_fast", "gsm8k_full_llada8b_fast"]:
        rows = [r for r in hist if r.get("run_name") == name]
        rows.sort(key=lambda r: int(r["step_index"]))
        ax.plot([int(r["step_index"]) for r in rows], [int(r["count"]) for r in rows], marker="o", label=name.split("_full_")[0])
    ax.set_xlabel("Best repair step")
    ax.set_ylabel("Trajectory count")
    ax.set_title("Localization of best repair checkpoints")
    ax.legend(fontsize=8)
    ax.grid(alpha=0.25)
    _save(fig, output_dir / "best_step_histogram")

    fig, ax = plt.subplots(figsize=(5.5, 3.4))
    for row in aggregate.get("diffusion_rows", []):
        if row.get("run_name") in {"math500_full_llada8b_fast", "gsm8k_full_llada8b_fast", "math500_full_dream_v0_instruct_7b", "gsm8k_full_dream_v0_instruct_7b"}:
            x = row.get("predictor_expected_pass_at_k")
            y = row.get("oracle_expected_pass_at_k")
            if x is not None and y is not None:
                ax.scatter(float(x), float(y), s=45)
                ax.annotate(str(row.get("dataset_name")), (float(x), float(y)), fontsize=8, xytext=(4, 4), textcoords="offset points")
    lo, hi = ax.get_xlim()
    ax.plot([lo, hi], [lo, hi], "--", color="#777", linewidth=1)
    ax.set_xlabel("Predictor repaired pass@k")
    ax.set_ylabel("Oracle repaired pass@k")
    ax.set_title("Predictor--oracle relationship")
    ax.grid(alpha=0.25)
    _save(fig, output_dir / "predictor_oracle")

    tradeoff = _csv(figure_data / "gain_negative_repair_tradeoff.csv")
    fig, ax = plt.subplots(figsize=(5.5, 3.4))
    for row in tradeoff:
        if row.get("run_name") in keep:
            x = row.get("predictor_negative_repair_rate")
            y = row.get("predictor_gain_over_base_pass_at_k")
            if x not in {None, ""} and y not in {None, ""}:
                ax.scatter(float(x), float(y), s=45)
                ax.annotate(str(row.get("dataset_name")), (float(x), float(y)), fontsize=8, xytext=(4, 4), textcoords="offset points")
    ax.set_xlabel("Negative repair rate")
    ax.set_ylabel("Predictor gain over base pass@k")
    ax.set_title("Repair utility--safety tradeoff")
    ax.grid(alpha=0.25)
    _save(fig, output_dir / "gain_negative_repair")


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--aggregate-report", default=str(ROOT / "results/benchmark_complete_reports/aggregate_report.json"))
    ap.add_argument("--figure-data", default=str(ROOT / "results/benchmark_complete_reports/figure_data"))
    ap.add_argument("--output-dir", default=str(ROOT / "paper/figures"))
    args = ap.parse_args()
    render(Path(args.aggregate_report), Path(args.figure_data), Path(args.output_dir))
    print(f"[paper-figures] output: {args.output_dir}")


if __name__ == "__main__":
    main()
