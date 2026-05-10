from __future__ import annotations

import argparse
import csv
from collections import defaultdict
from pathlib import Path
from typing import Any, Callable

import numpy as np
from sklearn.compose import ColumnTransformer
from sklearn.impute import SimpleImputer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, roc_auc_score
from sklearn.model_selection import GroupShuffleSplit
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler

from repairable_diffusion.src.analysis.predictor import FEATURE_KEYS
from repairable_diffusion.src.utils.io import ensure_dir, load_json, load_pickle, save_json


Step = dict[str, Any]
Result = dict[str, Any]


def _predictor_scores(payload: dict[str, Any]) -> dict[tuple[int, int, int], float]:
    return {
        (row["item_id"], row["trajectory_id"], row["step_index"]): float(row["score"])
        for row in payload.get("scores", [])
    }


def _oracle_step_lookup(oracle_payload: dict[str, Any]) -> dict[tuple[int, int, int], dict[str, Any]]:
    return {
        (result["item_id"], result["trajectory_id"], step["step_index"]): step
        for result in oracle_payload.get("results", [])
        for step in result.get("step_results", [])
    }


def _answer_disagreement(trajectory_payload: dict[str, Any]) -> dict[tuple[int, int], float]:
    buckets: dict[tuple[int, int], list[str]] = defaultdict(list)
    for record in trajectory_payload["records"]:
        for step in record.get("steps", []):
            buckets[(record["item_id"], step["step_index"])].append(step.get("answer_candidate") or "")
    out = {}
    for key, answers in buckets.items():
        counts: dict[str, int] = defaultdict(int)
        for answer in answers:
            counts[answer] += 1
        top = max(counts.values()) if counts else 0
        out[key] = 1.0 - (top / max(1, len(answers)))
    return out


def _feature_rows(
    trajectory_payload: dict[str, Any],
    oracle_payload: dict[str, Any],
) -> tuple[list[dict[str, Any]], list[dict[str, Any]]]:
    oracle_lookup = _oracle_step_lookup(oracle_payload)
    disagreement = _answer_disagreement(trajectory_payload)
    by_traj: dict[tuple[int, int], list[dict[str, Any]]] = defaultdict(list)
    for result in oracle_payload.get("results", []):
        for step in result.get("step_results", []):
            by_traj[(result["item_id"], result["trajectory_id"])].append(step)
    top_steps = {
        traj_id: {
            step["step_index"]
            for step in sorted(steps, key=lambda row: row["correction_rate"], reverse=True)[:1]
        }
        for traj_id, steps in by_traj.items()
    }

    train_rows = []
    inference_rows = []
    for record in trajectory_payload["records"]:
        prev_answer = None
        for step in record.get("steps", []):
            if step.get("snapshot") is None:
                continue
            candidate = step.get("answer_candidate") or ""
            row = {
                "item_id": record["item_id"],
                "trajectory_id": record["trajectory_id"],
                "step_index": step["step_index"],
                "step_norm": step["step_index"] / max(1, step["total_steps"]),
                "masked_ratio": step["masked_ratio"],
                "commitment_ratio": step["commitment_ratio"],
                "state_token_conf_mean": step["state_token_conf_mean"],
                "state_token_conf_min": step["state_token_conf_min"],
                "masked_entropy_mean": step["masked_entropy_mean"],
                "masked_entropy_max": step["masked_entropy_max"],
                "answer_disagreement": disagreement[(record["item_id"], step["step_index"])],
                "candidate_change_rate": 0.0 if prev_answer is None else float(candidate != prev_answer),
            }
            prev_answer = candidate
            inference_rows.append(dict(row))
            if record["correct"]:
                continue
            oracle_step = oracle_lookup.get((record["item_id"], record["trajectory_id"], step["step_index"]))
            if oracle_step is None:
                continue
            train_row = dict(row)
            train_row["label"] = int(step["step_index"] in top_steps[(record["item_id"], record["trajectory_id"])])
            train_rows.append(train_row)
    return train_rows, inference_rows


def _train_ablation_scores(
    train_rows: list[dict[str, Any]],
    inference_rows: list[dict[str, Any]],
    feature_keys: list[str],
    *,
    random_state: int,
) -> tuple[dict[tuple[int, int, int], float], dict[str, Any]]:
    groups = np.asarray([row["item_id"] for row in train_rows])
    X = np.asarray([[row[key] for key in feature_keys] for row in train_rows], dtype=np.float32)
    y = np.asarray([row["label"] for row in train_rows], dtype=np.int64)
    splitter = GroupShuffleSplit(n_splits=1, test_size=0.2, random_state=random_state)
    train_idx, test_idx = next(splitter.split(X, y, groups=groups))
    model = Pipeline(
        steps=[
            (
                "preprocess",
                ColumnTransformer(
                    transformers=[
                        (
                            "numeric",
                            Pipeline(
                                steps=[
                                    ("imputer", SimpleImputer(strategy="median")),
                                    ("scaler", StandardScaler()),
                                ]
                            ),
                            list(range(len(feature_keys))),
                        )
                    ]
                ),
            ),
            ("clf", LogisticRegression(max_iter=1000, random_state=random_state)),
        ]
    )
    model.fit(X[train_idx], y[train_idx])
    pred_proba = model.predict_proba(X[test_idx])[:, 1]
    pred_label = (pred_proba >= 0.5).astype(np.int64)
    metrics = {
        "feature_keys": feature_keys,
        "test_accuracy": float(accuracy_score(y[test_idx], pred_label)) if len(test_idx) else None,
        "test_roc_auc": float(roc_auc_score(y[test_idx], pred_proba)) if len(np.unique(y[test_idx])) > 1 else None,
    }
    X_infer = np.asarray([[row[key] for key in feature_keys] for row in inference_rows], dtype=np.float32)
    pred_infer = model.predict_proba(X_infer)[:, 1]
    scores = {
        (row["item_id"], row["trajectory_id"], row["step_index"]): float(score)
        for row, score in zip(inference_rows, pred_infer, strict=True)
    }
    return scores, metrics


def _ablation_specs() -> dict[str, list[str]]:
    return {
        "abl_all": list(FEATURE_KEYS),
        "abl_confidence_only": ["state_token_conf_mean", "state_token_conf_min"],
        "abl_mask_only": ["masked_ratio", "masked_entropy_mean", "masked_entropy_max"],
        "abl_step_only": ["step_norm"],
        "abl_no_confidence": [key for key in FEATURE_KEYS if not key.startswith("state_token_conf")],
        "abl_no_mask": [key for key in FEATURE_KEYS if key not in {"masked_ratio", "masked_entropy_mean", "masked_entropy_max"}],
        "abl_no_step": [key for key in FEATURE_KEYS if key != "step_norm"],
    }


def _base_item_maps(trajectory_payload: dict[str, Any]) -> tuple[list[int], dict[int, bool], dict[int, bool]]:
    pass1: dict[int, bool] = defaultdict(bool)
    passk: dict[int, bool] = defaultdict(bool)
    for record in trajectory_payload["records"]:
        item_id = int(record["item_id"])
        if int(record["trajectory_id"]) == 0:
            pass1[item_id] = bool(record["correct"])
        passk[item_id] = passk[item_id] or bool(record["correct"])
    item_ids = sorted(passk)
    return item_ids, pass1, passk


def _score_value(
    strategy: str,
    step: Step,
    result: Result,
    predictor: dict[tuple[int, int, int], float],
) -> float:
    key = (int(result["item_id"]), int(result["trajectory_id"]), int(step["step_index"]))
    if strategy == "predictor":
        return predictor.get(key, -1.0)
    if strategy == "confidence_low":
        return -float(step.get("state_token_conf_mean", 0.0))
    if strategy == "entropy_high":
        return float(step.get("masked_entropy_mean", 0.0))
    if strategy == "masked_ratio_high":
        return float(step.get("masked_ratio", 0.0))
    if strategy == "early_step":
        return -float(step.get("step_index", 0))
    if strategy == "middle_step":
        return -abs(float(step.get("step_index", 0)) - 16.0)
    raise ValueError(f"unsupported strategy: {strategy}")


def _select_step(
    strategy: str,
    result: Result,
    predictor: dict[tuple[int, int, int], float],
    *,
    threshold: float | None = None,
    success: bool = False,
) -> Step | None:
    steps = result.get("step_results", [])
    if not steps:
        return None
    if strategy == "oracle":
        key = "degradation_rate" if success else "correction_rate"
        return min(steps, key=lambda row: float(row[key])) if success else max(steps, key=lambda row: float(row[key]))
    picked = max(steps, key=lambda row: _score_value(strategy, row, result, predictor))
    if threshold is not None:
        score = _score_value(strategy, picked, result, predictor)
        if score < threshold:
            return None
    return picked


def _percentile_ci(values: list[float]) -> dict[str, float | None]:
    if not values:
        return {"mean": None, "ci_low": None, "ci_high": None}
    arr = np.asarray(values, dtype=np.float64)
    return {
        "mean": float(arr.mean()),
        "ci_low": float(np.percentile(arr, 2.5)),
        "ci_high": float(np.percentile(arr, 97.5)),
    }


def _bootstrap_item_ci(
    item_values: dict[int, float],
    base_values: dict[int, float],
    rng: np.random.Generator,
    n_bootstrap: int,
) -> dict[str, dict[str, float | None]]:
    item_ids = sorted(item_values)
    if not item_ids:
        empty = {"mean": None, "ci_low": None, "ci_high": None}
        return {"repaired_pass_at_k": empty, "gain": empty}
    repaired_samples = []
    gain_samples = []
    items = np.asarray(item_ids)
    for _ in range(n_bootstrap):
        sample = rng.choice(items, size=len(items), replace=True)
        repaired = float(np.mean([item_values[int(item)] for item in sample]))
        base = float(np.mean([base_values[int(item)] for item in sample]))
        repaired_samples.append(repaired)
        gain_samples.append(repaired - base)
    return {
        "repaired_pass_at_k": _percentile_ci(repaired_samples),
        "gain": _percentile_ci(gain_samples),
    }


def evaluate_strategy(
    *,
    strategy: str,
    run_name: str,
    trajectory_payload: dict[str, Any],
    oracle_payload: dict[str, Any],
    predictor: dict[tuple[int, int, int], float],
    threshold: float | None,
    n_bootstrap: int,
    rng: np.random.Generator,
) -> dict[str, Any]:
    item_ids, pass1, passk = _base_item_maps(trajectory_payload)
    base_values = {item_id: float(passk[item_id]) for item_id in item_ids}
    repair_probs_by_item: dict[int, list[float]] = defaultdict(list)
    selected_failed = 0

    for result in oracle_payload.get("results", []):
        picked = _select_step(strategy, result, predictor, threshold=threshold, success=False)
        if picked is None:
            continue
        selected_failed += 1
        item_id = int(result["item_id"])
        if not passk[item_id]:
            repair_probs_by_item[item_id].append(float(picked["correction_rate"]))

    repaired_item_values: dict[int, float] = {}
    upper_bound_newly_solved = 0
    for item_id in item_ids:
        if passk[item_id]:
            repaired_item_values[item_id] = 1.0
            continue
        probs = repair_probs_by_item.get(item_id, [])
        repaired_item_values[item_id] = 1.0 - float(np.prod([1.0 - p for p in probs])) if probs else 0.0
        upper_bound_newly_solved += int(any(p > 0.0 for p in probs))

    selected_success = 0
    degradation_values = []
    for result in oracle_payload.get("success_results", []):
        picked = _select_step(strategy, result, predictor, threshold=threshold, success=True)
        if picked is None:
            degradation_values.append(0.0)
            continue
        selected_success += 1
        degradation_values.append(float(picked["degradation_rate"]))

    base_pass_at_1 = float(np.mean([float(pass1[item_id]) for item_id in item_ids])) if item_ids else 0.0
    base_pass_at_k = float(np.mean([base_values[item_id] for item_id in item_ids])) if item_ids else 0.0
    repaired_pass_at_k = float(np.mean([repaired_item_values[item_id] for item_id in item_ids])) if item_ids else 0.0
    ci = _bootstrap_item_ci(repaired_item_values, base_values, rng, n_bootstrap)
    branch_count = int(oracle_payload.get("meta", {}).get("branch_count", 0))

    return {
        "run_name": run_name,
        "strategy": strategy if threshold is None else f"{strategy}@{threshold:.2f}",
        "threshold": threshold,
        "base_pass_at_1": base_pass_at_1,
        "base_pass_at_k": base_pass_at_k,
        "repaired_pass_at_k": repaired_pass_at_k,
        "gain": repaired_pass_at_k - base_pass_at_k,
        "repaired_pass_at_k_ci_low": ci["repaired_pass_at_k"]["ci_low"],
        "repaired_pass_at_k_ci_high": ci["repaired_pass_at_k"]["ci_high"],
        "gain_ci_low": ci["gain"]["ci_low"],
        "gain_ci_high": ci["gain"]["ci_high"],
        "expected_newly_solved_items": sum(
            repaired_item_values[item_id] for item_id in item_ids if not passk[item_id]
        ),
        "upper_bound_newly_solved_items": upper_bound_newly_solved,
        "negative_repair_rate": float(np.mean(degradation_values)) if degradation_values else None,
        "selected_failed_trajectories": selected_failed,
        "selected_success_trajectories": selected_success,
        "repair_branch_count": branch_count,
        "estimated_repair_branch_evals": branch_count * (selected_failed + selected_success),
    }


def _write_csv(path: Path, rows: list[dict[str, Any]]) -> None:
    ensure_dir(path.parent)
    if not rows:
        path.write_text("", encoding="utf-8")
        return
    fieldnames = sorted({key for row in rows for key in row})
    with open(path, "w", encoding="utf-8", newline="") as fh:
        writer = csv.DictWriter(fh, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)


def _markdown_table(rows: list[dict[str, Any]]) -> str:
    headers = [
        "run",
        "strategy",
        "base",
        "repaired",
        "gain",
        "gain_ci",
        "neg",
        "branches",
    ]
    lines = [
        "| " + " | ".join(headers) + " |",
        "| " + " | ".join(["---"] * len(headers)) + " |",
    ]
    for row in rows:
        gain_ci = f"[{row['gain_ci_low']:.4f}, {row['gain_ci_high']:.4f}]"
        lines.append(
            "| "
            + " | ".join(
                [
                    str(row["run_name"]),
                    str(row["strategy"]),
                    f"{row['base_pass_at_k']:.4f}",
                    f"{row['repaired_pass_at_k']:.4f}",
                    f"{row['gain']:.4f}",
                    gain_ci,
                    "-" if row["negative_repair_rate"] is None else f"{row['negative_repair_rate']:.4f}",
                    str(row["estimated_repair_branch_evals"]),
                ]
            )
            + " |"
        )
    return "\n".join(lines) + "\n"


def analyze_run(run_dir: Path, *, n_bootstrap: int, seed: int) -> list[dict[str, Any]]:
    trajectory_payload = load_pickle(run_dir / "trajectories.pkl")
    oracle_payload = load_json(run_dir / "oracle_repair.json")
    predictor_payload = load_json(run_dir / "repair_predictor.json")
    predictor = _predictor_scores(predictor_payload)
    rng = np.random.default_rng(seed)
    strategies: list[tuple[str, float | None]] = [
        ("confidence_low", None),
        ("entropy_high", None),
        ("masked_ratio_high", None),
        ("early_step", None),
        ("middle_step", None),
        ("predictor", None),
        ("predictor", 0.50),
        ("predictor", 0.70),
        ("predictor", 0.90),
        ("oracle", None),
    ]
    rows = [
        evaluate_strategy(
            strategy=strategy,
            run_name=run_dir.name,
            trajectory_payload=trajectory_payload,
            oracle_payload=oracle_payload,
            predictor=predictor,
            threshold=threshold,
            n_bootstrap=n_bootstrap,
            rng=rng,
        )
        for strategy, threshold in strategies
    ]
    train_rows, inference_rows = _feature_rows(trajectory_payload, oracle_payload)
    for name, feature_keys in _ablation_specs().items():
        scores, metrics = _train_ablation_scores(train_rows, inference_rows, feature_keys, random_state=seed)
        row = evaluate_strategy(
            strategy="predictor",
            run_name=run_dir.name,
            trajectory_payload=trajectory_payload,
            oracle_payload=oracle_payload,
            predictor=scores,
            threshold=None,
            n_bootstrap=n_bootstrap,
            rng=rng,
        )
        row["strategy"] = name
        row["ablation_test_accuracy"] = metrics["test_accuracy"]
        row["ablation_test_roc_auc"] = metrics["test_roc_auc"]
        row["ablation_feature_keys"] = ",".join(feature_keys)
        rows.append(row)
    return rows


def parse_args() -> argparse.Namespace:
    ap = argparse.ArgumentParser()
    ap.add_argument("--run-dir", action="append", required=True)
    ap.add_argument("--output-dir", required=True)
    ap.add_argument("--bootstrap", type=int, default=1000)
    ap.add_argument("--seed", type=int, default=7)
    return ap.parse_args()


def main() -> None:
    args = parse_args()
    rows = []
    for run_dir in args.run_dir:
        rows.extend(analyze_run(Path(run_dir), n_bootstrap=args.bootstrap, seed=args.seed))

    out_dir = ensure_dir(args.output_dir)
    save_json(out_dir / "extended_repair_analysis.json", {"rows": rows})
    _write_csv(out_dir / "extended_repair_analysis.csv", rows)
    (out_dir / "extended_repair_analysis.md").write_text(_markdown_table(rows), encoding="utf-8")
    print(f"[extended] runs: {len(args.run_dir)}")
    print(f"[extended] rows: {len(rows)}")
    print(f"[extended] output: {out_dir}")


if __name__ == "__main__":
    main()
