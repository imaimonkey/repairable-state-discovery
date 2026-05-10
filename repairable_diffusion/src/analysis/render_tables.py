from __future__ import annotations

import argparse
from pathlib import Path
from typing import Any

from repairable_diffusion.src.utils.io import ensure_dir


def _read_json(path: str | Path) -> dict[str, Any]:
    import json

    with open(path, "r", encoding="utf-8") as fh:
        return json.load(fh)


def _fmt(value: Any) -> str:
    if value is None:
        return "-"
    if isinstance(value, float):
        return f"{value:.4f}"
    return str(value)


def _markdown_table(headers: list[str], rows: list[list[Any]]) -> str:
    lines = [
        "| " + " | ".join(headers) + " |",
        "| " + " | ".join(["---"] * len(headers)) + " |",
    ]
    for row in rows:
        lines.append("| " + " | ".join(_fmt(value) for value in row) + " |")
    return "\n".join(lines) + "\n"


def _latex_table(headers: list[str], rows: list[list[Any]], caption: str, label: str) -> str:
    spec = "l" * len(headers)
    lines = [
        "\\begin{table}[t]",
        "\\centering",
        f"\\caption{{{caption}}}",
        f"\\label{{{label}}}",
        f"\\begin{{tabular}}{{{spec}}}",
        "\\hline",
        " & ".join(headers) + " \\\\",
        "\\hline",
    ]
    for row in rows:
        lines.append(" & ".join(_fmt(value) for value in row) + " \\\\")
    lines.extend(["\\hline", "\\end{tabular}", "\\end{table}", ""])
    return "\n".join(lines)


def render_tables(aggregate_report_path: str | Path, output_dir: str | Path) -> dict[str, str]:
    payload = _read_json(aggregate_report_path)
    out_dir = ensure_dir(output_dir)

    diffusion_headers = [
        "dataset",
        "model",
        "pass@1",
        "pass@k",
        "pred repaired pass@k",
        "pred gain",
        "oracle-pred gap",
        "peak step",
        "repairable failed rate",
        "neg repair",
    ]
    diffusion_rows = [
        [
            row.get("dataset_name"),
            row.get("model_profile"),
            row.get("item_pass_at_1"),
            row.get("item_pass_at_k"),
            row.get("predictor_expected_pass_at_k"),
            row.get("predictor_gain_over_base_pass_at_k"),
            row.get("oracle_minus_predictor_expected_pass_at_k"),
            row.get("peak_step_index"),
            row.get("repairable_failed_rate"),
            row.get("predictor_negative_repair_rate"),
        ]
        for row in payload.get("diffusion_rows", [])
    ]

    ar_headers = ["dataset", "model", "pass@1", "pass@k"]
    ar_rows = [
        [
            row.get("dataset_name"),
            row.get("model_profile"),
            row.get("pass_at_1"),
            row.get("pass_at_k"),
        ]
        for row in payload.get("ar_rows", [])
    ]

    diffusion_md = _markdown_table(diffusion_headers, diffusion_rows)
    ar_md = _markdown_table(ar_headers, ar_rows)
    diffusion_tex = _latex_table(diffusion_headers, diffusion_rows, "Diffusion repairability summary.", "tab:diffusion-repairability")
    ar_tex = _latex_table(ar_headers, ar_rows, "Autoregressive baseline summary.", "tab:ar-baselines")

    outputs = {
        "diffusion_markdown": diffusion_md,
        "ar_markdown": ar_md,
        "diffusion_latex": diffusion_tex,
        "ar_latex": ar_tex,
    }

    for name, content in outputs.items():
        suffix = ".tex" if "latex" in name else ".md"
        path = out_dir / f"{name}{suffix}"
        with open(path, "w", encoding="utf-8") as fh:
            fh.write(content)
    return {key: str((out_dir / f"{key}{'.tex' if 'latex' in key else '.md'}")) for key in outputs}


def parse_args() -> argparse.Namespace:
    ap = argparse.ArgumentParser()
    ap.add_argument("--aggregate-report", required=True)
    ap.add_argument("--output-dir", required=True)
    return ap.parse_args()


def main() -> None:
    args = parse_args()
    outputs = render_tables(args.aggregate_report, args.output_dir)
    for name, path in outputs.items():
        print(f"[render] {name}: {path}")


if __name__ == "__main__":
    main()
