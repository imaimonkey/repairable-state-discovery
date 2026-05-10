from __future__ import annotations

import argparse
from pathlib import Path
from typing import Any

from repairable_diffusion.src.utils.io import ensure_dir, load_json, load_pickle, save_json


def _record_map(trajectory_payload: dict[str, Any]) -> dict[tuple[int, int], dict[str, Any]]:
    return {
        (int(row["item_id"]), int(row["trajectory_id"])): row
        for row in trajectory_payload.get("records", [])
    }


def _example_row(
    *,
    run_name: str,
    example_type: str,
    result: dict[str, Any],
    step: dict[str, Any],
    record: dict[str, Any],
    rate_name: str,
) -> dict[str, Any]:
    branch = None
    if example_type == "successful_repair":
        branch = next((row for row in step.get("branches", []) if row.get("correct")), None)
    elif example_type == "negative_repair":
        branch = next((row for row in step.get("branches", []) if not row.get("correct")), None)
    if branch is None and step.get("branches"):
        branch = step["branches"][0]
    branch = branch or {}
    return {
        "run_name": run_name,
        "type": example_type,
        "item_id": int(result["item_id"]),
        "trajectory_id": int(result["trajectory_id"]),
        "step_index": int(step["step_index"]),
        "rate": float(step.get(rate_name, 0.0)),
        "question": record.get("question"),
        "base_answer": record.get("final_answer"),
        "repair_answer": branch.get("final_answer"),
        "gold_answer": record.get("gold_answer"),
        "repair_correct": branch.get("correct"),
    }


def extract_examples(run_dir: Path, max_per_type: int) -> list[dict[str, Any]]:
    trajectory_payload = load_pickle(run_dir / "trajectories.pkl")
    oracle_payload = load_json(run_dir / "oracle_repair.json")
    records = _record_map(trajectory_payload)
    examples: list[dict[str, Any]] = []

    counts = {"successful_repair": 0, "unrepaired_failure": 0, "negative_repair": 0}

    for result in oracle_payload.get("results", []):
        if counts["successful_repair"] >= max_per_type:
            break
        steps = result.get("step_results", [])
        if not steps:
            continue
        step = max(steps, key=lambda row: float(row.get("correction_rate", 0.0)))
        if float(step.get("correction_rate", 0.0)) <= 0:
            continue
        record = records.get((int(result["item_id"]), int(result["trajectory_id"])), {})
        examples.append(
            _example_row(
                run_name=run_dir.name,
                example_type="successful_repair",
                result=result,
                step=step,
                record=record,
                rate_name="correction_rate",
            )
        )
        counts["successful_repair"] += 1

    for result in oracle_payload.get("results", []):
        if counts["unrepaired_failure"] >= max_per_type:
            break
        steps = result.get("step_results", [])
        if not steps:
            continue
        step = max(steps, key=lambda row: float(row.get("correction_rate", 0.0)))
        if float(step.get("correction_rate", 0.0)) != 0:
            continue
        record = records.get((int(result["item_id"]), int(result["trajectory_id"])), {})
        examples.append(
            _example_row(
                run_name=run_dir.name,
                example_type="unrepaired_failure",
                result=result,
                step=step,
                record=record,
                rate_name="correction_rate",
            )
        )
        counts["unrepaired_failure"] += 1

    for result in oracle_payload.get("success_results", []):
        if counts["negative_repair"] >= max_per_type:
            break
        steps = result.get("step_results", [])
        if not steps:
            continue
        step = max(steps, key=lambda row: float(row.get("degradation_rate", 0.0)))
        if float(step.get("degradation_rate", 0.0)) <= 0:
            continue
        record = records.get((int(result["item_id"]), int(result["trajectory_id"])), {})
        examples.append(
            _example_row(
                run_name=run_dir.name,
                example_type="negative_repair",
                result=result,
                step=step,
                record=record,
                rate_name="degradation_rate",
            )
        )
        counts["negative_repair"] += 1

    return examples


def _markdown(examples: list[dict[str, Any]]) -> str:
    lines = ["# Qualitative Examples", ""]
    for row in examples:
        lines.append(f"## {row['run_name']} / {row['type']}")
        lines.append("")
        lines.append(f"- item_id: `{row['item_id']}`")
        lines.append(f"- trajectory_id: `{row['trajectory_id']}`")
        lines.append(f"- step_index: `{row['step_index']}`")
        lines.append(f"- rate: `{row['rate']}`")
        lines.append(f"- base_answer: `{row['base_answer']}`")
        lines.append(f"- repair_answer: `{row['repair_answer']}`")
        lines.append(f"- gold_answer: `{row['gold_answer']}`")
        lines.append("")
    return "\n".join(lines)


def parse_args() -> argparse.Namespace:
    ap = argparse.ArgumentParser()
    ap.add_argument("--run-dir", action="append", required=True)
    ap.add_argument("--output-dir", required=True)
    ap.add_argument("--max-per-type", type=int, default=1)
    return ap.parse_args()


def main() -> None:
    args = parse_args()
    examples: list[dict[str, Any]] = []
    for run_dir in args.run_dir:
        examples.extend(extract_examples(Path(run_dir), args.max_per_type))
    out_dir = ensure_dir(args.output_dir)
    save_json(out_dir / "qualitative_examples.json", {"examples": examples})
    (out_dir / "qualitative_examples.md").write_text(_markdown(examples), encoding="utf-8")
    print(f"[examples] rows: {len(examples)}")
    print(f"[examples] output: {out_dir}")


if __name__ == "__main__":
    main()
