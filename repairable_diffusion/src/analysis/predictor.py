from __future__ import annotations

from collections import Counter, defaultdict
from typing import Any

import numpy as np
from sklearn.compose import ColumnTransformer
from sklearn.impute import SimpleImputer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, roc_auc_score
from sklearn.model_selection import GroupKFold
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


def _make_model(*, feature_count: int, max_iter: int, random_state: int) -> Pipeline:
    return Pipeline(
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
                            list(range(feature_count)),
                        )
                    ]
                ),
            ),
            (
                "clf",
                LogisticRegression(
                    max_iter=max_iter,
                    random_state=random_state,
                ),
            ),
        ]
    )


def fit_crossfit_predictor_scores(
    train_rows: list[dict[str, Any]],
    inference_rows: list[dict[str, Any]],
    feature_keys: list[str],
    *,
    requested_folds: int,
    random_state: int,
    max_iter: int,
) -> tuple[list[dict[str, Any]], dict[str, Any], Pipeline]:
    """Fit item-grouped cross-fit models and return leakage-free inference scores.

    Every item that contributes supervision is scored only by the fold model that
    excluded that item.  Items that never contribute a supervised failed-state row
    are scored by the final model trained on all supervised items; these items are
    still genuinely unseen by that final fit.  The final all-data model is saved for
    deployment only and is not used to score supervised training items.
    """

    if not train_rows:
        raise ValueError("cross-fit predictor requires at least one supervised row")

    groups = np.asarray([int(row["item_id"]) for row in train_rows])
    unique_groups = np.unique(groups)
    if len(unique_groups) < 2:
        raise ValueError("cross-fit predictor requires at least two supervised item groups")

    n_splits = min(max(2, int(requested_folds)), len(unique_groups))
    X = np.asarray([[row[key] for key in feature_keys] for row in train_rows], dtype=np.float32)
    y = np.asarray([int(row["label"]) for row in train_rows], dtype=np.int64)
    X_infer = np.asarray(
        [[row[key] for key in feature_keys] for row in inference_rows],
        dtype=np.float32,
    )

    oof_proba = np.full(len(train_rows), np.nan, dtype=np.float64)
    inference_scores: dict[tuple[int, int, int], tuple[float, str, int | None]] = {}
    fold_summaries: list[dict[str, Any]] = []
    splitter = GroupKFold(n_splits=n_splits)

    for fold_index, (train_idx, test_idx) in enumerate(splitter.split(X, y, groups=groups)):
        model = _make_model(
            feature_count=len(feature_keys),
            max_iter=max_iter,
            random_state=random_state + fold_index,
        )
        model.fit(X[train_idx], y[train_idx])
        fold_test_proba = model.predict_proba(X[test_idx])[:, 1]
        oof_proba[test_idx] = fold_test_proba

        heldout_items = {int(item_id) for item_id in groups[test_idx]}
        infer_idx = [
            index
            for index, row in enumerate(inference_rows)
            if int(row["item_id"]) in heldout_items
        ]
        if infer_idx:
            fold_infer_proba = model.predict_proba(X_infer[infer_idx])[:, 1]
            for row_index, score in zip(infer_idx, fold_infer_proba, strict=True):
                row = inference_rows[row_index]
                key = (
                    int(row["item_id"]),
                    int(row["trajectory_id"]),
                    int(row["step_index"]),
                )
                inference_scores[key] = (float(score), "crossfit_oof", fold_index)

        fold_summaries.append(
            {
                "fold": fold_index,
                "train_items": len({int(item_id) for item_id in groups[train_idx]}),
                "test_items": len(heldout_items),
                "train_rows": int(len(train_idx)),
                "test_rows": int(len(test_idx)),
            }
        )

    if np.isnan(oof_proba).any():
        raise RuntimeError("cross-fit predictor left supervised rows without OOF scores")

    final_model = _make_model(
        feature_count=len(feature_keys),
        max_iter=max_iter,
        random_state=random_state,
    )
    final_model.fit(X, y)

    missing_infer_idx = []
    for index, row in enumerate(inference_rows):
        key = (
            int(row["item_id"]),
            int(row["trajectory_id"]),
            int(row["step_index"]),
        )
        if key not in inference_scores:
            missing_infer_idx.append(index)
    if missing_infer_idx:
        final_proba = final_model.predict_proba(X_infer[missing_infer_idx])[:, 1]
        supervised_items = {int(item_id) for item_id in groups}
        for row_index, score in zip(missing_infer_idx, final_proba, strict=True):
            row = inference_rows[row_index]
            item_id = int(row["item_id"])
            if item_id in supervised_items:
                raise RuntimeError(
                    "supervised item reached full-fit inference path; cross-fit coverage is incomplete"
                )
            key = (item_id, int(row["trajectory_id"]), int(row["step_index"]))
            inference_scores[key] = (float(score), "full_fit_unseen_item", None)

    pred_label = (oof_proba >= 0.5).astype(np.int64)
    metrics = {
        "evaluation_protocol": "item_grouped_crossfit_oof",
        "crossfit_folds": n_splits,
        "supervised_items": int(len(unique_groups)),
        "train_rows": int(len(train_rows)),
        "test_rows": int(len(train_rows)),
        "positive_rate_train": float(y.mean()) if len(y) else 0.0,
        "positive_rate_test": float(y.mean()) if len(y) else 0.0,
        "accuracy": float(accuracy_score(y, pred_label)) if len(y) else 0.0,
        "roc_auc": float(roc_auc_score(y, oof_proba)) if len(np.unique(y)) > 1 else None,
        "folds": fold_summaries,
    }

    score_rows = []
    score_source_counts: Counter[str] = Counter()
    for row in inference_rows:
        key = (
            int(row["item_id"]),
            int(row["trajectory_id"]),
            int(row["step_index"]),
        )
        score, source, fold_index = inference_scores[key]
        score_source_counts[source] += 1
        score_rows.append(
            {
                "item_id": row["item_id"],
                "trajectory_id": row["trajectory_id"],
                "step_index": row["step_index"],
                "score": score,
                "score_source": source,
                "crossfit_fold": fold_index,
                "base_correct": row.get("base_correct"),
                "correction_rate": row.get("correction_rate"),
                "label": row.get("label"),
            }
        )
    metrics["score_source_counts"] = dict(score_source_counts)
    return score_rows, metrics, final_model


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
                "base_correct": bool(record["correct"]),
            }
            prev_answer = candidate
            oracle_step = oracle_lookup.get(
                (record["item_id"], record["trajectory_id"], step["step_index"])
            )
            if oracle_step is not None:
                row["correction_rate"] = oracle_step["correction_rate"]
                row["label"] = int(
                    step["step_index"]
                    in top_steps[(record["item_id"], record["trajectory_id"])]
                )
            inference_rows.append(dict(row))
            if not record["correct"] and oracle_step is not None:
                rows.append(dict(row))

    if not rows:
        payload = {"enabled": False, "reason": "no training rows"}
        save_json(run_dir / "repair_predictor.json", payload)
        return payload

    unique_items = {int(row["item_id"]) for row in rows}
    if len(unique_items) < 2:
        payload = {
            "enabled": False,
            "reason": "insufficient item groups for leakage-free cross-fit evaluation",
        }
        save_json(run_dir / "repair_predictor.json", payload)
        return payload

    score_rows, metrics, final_model = fit_crossfit_predictor_scores(
        rows,
        inference_rows,
        list(FEATURE_KEYS),
        requested_folds=int(cfg["predictor"].get("crossfit_folds", 5)),
        random_state=int(cfg["predictor"].get("random_state", 7)),
        max_iter=int(cfg["predictor"].get("max_iter", 1000)),
    )

    payload = {
        "enabled": True,
        "feature_keys": FEATURE_KEYS,
        "metrics": metrics,
        "scores": score_rows,
        "deployment_model_note": (
            "repair_predictor.pkl is fit on all supervised items for deployment only; "
            "reported selector scores for supervised items are cross-fit OOF scores"
        ),
    }
    save_pickle(run_dir / "repair_predictor.pkl", final_model)
    save_json(run_dir / "repair_predictor.json", payload)
    return payload
