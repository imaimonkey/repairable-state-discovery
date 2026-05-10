from __future__ import annotations

from collections import Counter, defaultdict
from typing import Any

import numpy as np
from sklearn.compose import ColumnTransformer
from sklearn.impute import SimpleImputer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, roc_auc_score
from sklearn.model_selection import GroupShuffleSplit
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler

from repairable_diffusion.src.utils.io import save_json, save_pickle


FEATURE_KEYS = [
    "step_norm",
    "masked_ratio",
    "commitment_ratio",
    "state_token_conf_mean",
    "state_token_conf_min",
    "masked_entropy_mean",
    "masked_entropy_max",
    "answer_disagreement",
    "candidate_change_rate",
]


def _oracle_map(oracle_payload: dict[str, Any]) -> dict[tuple[int, int, int], dict[str, Any]]:
    out = {}
    for result in oracle_payload["results"]:
        for step in result["step_results"]:
            out[(result["item_id"], result["trajectory_id"], step["step_index"])] = step
    return out


def _build_disagreement(records: list[dict[str, Any]]) -> dict[tuple[int, int], float]:
    buckets: dict[tuple[int, int], list[str]] = defaultdict(list)
    for record in records:
        for step in record["steps"]:
            candidate = step.get("answer_candidate") or ""
            buckets[(record["item_id"], step["step_index"])].append(candidate)

    out = {}
    for key, answers in buckets.items():
        counts = Counter(answers)
        top = counts.most_common(1)[0][1] if counts else 0
        out[key] = 1.0 - (top / max(1, len(answers)))
    return out


def train_repair_predictor(
    cfg: dict[str, Any],
    run_dir,
    trajectory_payload: dict[str, Any],
    oracle_payload: dict[str, Any],
) -> dict[str, Any]:
    oracle_lookup = _oracle_map(oracle_payload)
    disagreement = _build_disagreement(trajectory_payload["records"])
    top_k = int(cfg["predictor"].get("top_k_label", 1))

    rows = []
    by_traj: dict[tuple[int, int], list[dict[str, Any]]] = defaultdict(list)
    for result in oracle_payload["results"]:
        for step in result["step_results"]:
            by_traj[(result["item_id"], result["trajectory_id"])].append(step)

    top_steps = {
        traj_id: {
            step["step_index"]
            for step in sorted(steps, key=lambda x: x["correction_rate"], reverse=True)[:top_k]
        }
        for traj_id, steps in by_traj.items()
    }

    inference_rows = []
    for record in trajectory_payload["records"]:
        prev_answer = None
        for step in record["steps"]:
            snapshot = step.get("snapshot")
            if snapshot is None:
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
            if not record["correct"]:
                oracle_step = oracle_lookup.get((record["item_id"], record["trajectory_id"], step["step_index"]))
                if oracle_step is None:
                    continue
                train_row = dict(row)
                train_row["correction_rate"] = oracle_step["correction_rate"]
                train_row["label"] = int(step["step_index"] in top_steps[(record["item_id"], record["trajectory_id"])])
                rows.append(train_row)

    if not rows:
        payload = {"enabled": False, "reason": "no training rows"}
        save_json(run_dir / "repair_predictor.json", payload)
        return payload

    groups = np.asarray([row["item_id"] for row in rows])
    X = np.asarray([[row[key] for key in FEATURE_KEYS] for row in rows], dtype=np.float32)
    y = np.asarray([row["label"] for row in rows], dtype=np.int64)

    splitter = GroupShuffleSplit(
        n_splits=1,
        test_size=float(cfg["predictor"].get("test_size", 0.2)),
        random_state=int(cfg["predictor"].get("random_state", 7)),
    )
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
                            list(range(len(FEATURE_KEYS))),
                        )
                    ]
                ),
            ),
            (
                "clf",
                LogisticRegression(
                    max_iter=int(cfg["predictor"].get("max_iter", 1000)),
                    random_state=int(cfg["predictor"].get("random_state", 7)),
                ),
            ),
        ]
    )
    model.fit(X[train_idx], y[train_idx])
    pred_proba = model.predict_proba(X[test_idx])[:, 1]
    pred_label = (pred_proba >= 0.5).astype(np.int64)

    metrics = {
        "train_rows": int(len(train_idx)),
        "test_rows": int(len(test_idx)),
        "positive_rate_train": float(y[train_idx].mean()) if len(train_idx) else 0.0,
        "positive_rate_test": float(y[test_idx].mean()) if len(test_idx) else 0.0,
        "accuracy": float(accuracy_score(y[test_idx], pred_label)) if len(test_idx) else 0.0,
        "roc_auc": float(roc_auc_score(y[test_idx], pred_proba)) if len(np.unique(y[test_idx])) > 1 else None,
    }

    score_rows = []
    for row in inference_rows:
        score = float(model.predict_proba(np.asarray([[row[key] for key in FEATURE_KEYS]], dtype=np.float32))[0, 1])
        score_rows.append(
            {
                "item_id": row["item_id"],
                "trajectory_id": row["trajectory_id"],
                "step_index": row["step_index"],
                "score": score,
                "correction_rate": row.get("correction_rate"),
                "label": row.get("label"),
            }
        )

    payload = {
        "enabled": True,
        "feature_keys": FEATURE_KEYS,
        "metrics": metrics,
        "scores": score_rows,
    }
    save_pickle(run_dir / "repair_predictor.pkl", model)
    save_json(run_dir / "repair_predictor.json", payload)
    return payload
