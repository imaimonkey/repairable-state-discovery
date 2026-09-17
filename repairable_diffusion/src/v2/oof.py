from __future__ import annotations

from typing import Any, Sequence

import numpy as np
from sklearn.compose import ColumnTransformer
from sklearn.impute import SimpleImputer
from sklearn.linear_model import LogisticRegression, Ridge
from sklearn.model_selection import GroupKFold
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler


def _matrix(rows: list[dict[str, Any]], feature_keys: Sequence[str]) -> np.ndarray:
    return np.asarray([[row.get(key, np.nan) for key in feature_keys] for row in rows], dtype=np.float64)


def _preprocessor(n_features: int) -> ColumnTransformer:
    return ColumnTransformer(
        transformers=[
            (
                "numeric",
                Pipeline(
                    steps=[
                        ("imputer", SimpleImputer(strategy="median")),
                        ("scaler", StandardScaler()),
                    ]
                ),
                list(range(n_features)),
            )
        ]
    )


def crossfit_binary_scores(
    rows: list[dict[str, Any]],
    *,
    feature_keys: Sequence[str],
    target_key: str,
    group_key: str = "item_id",
    n_splits: int = 5,
    random_state: int = 7,
) -> list[dict[str, Any]]:
    if not rows:
        return []
    groups = np.asarray([row[group_key] for row in rows])
    unique_groups = np.unique(groups)
    if len(unique_groups) < 2:
        raise ValueError("cross-fitting requires at least two distinct groups")
    splits = min(int(n_splits), len(unique_groups))
    if splits < 2:
        raise ValueError("cross-fitting requires at least two folds")

    X = _matrix(rows, feature_keys)
    y = np.asarray([int(bool(row[target_key])) for row in rows], dtype=np.int64)
    scores = np.full(len(rows), np.nan, dtype=np.float64)
    fold_ids = np.full(len(rows), -1, dtype=np.int64)

    for fold_id, (train_idx, test_idx) in enumerate(GroupKFold(n_splits=splits).split(X, y, groups)):
        if set(groups[train_idx]) & set(groups[test_idx]):
            raise AssertionError("group leakage detected")
        y_train = y[train_idx]
        if len(np.unique(y_train)) < 2:
            # A constant training fold is valid but carries no ranking information.
            scores[test_idx] = float(y_train[0]) if len(y_train) else 0.0
            fold_ids[test_idx] = fold_id
            continue
        model = Pipeline(
            steps=[
                ("preprocess", _preprocessor(len(feature_keys))),
                ("clf", LogisticRegression(max_iter=1000, random_state=random_state + fold_id)),
            ]
        )
        model.fit(X[train_idx], y_train)
        scores[test_idx] = model.predict_proba(X[test_idx])[:, 1]
        fold_ids[test_idx] = fold_id

    if np.isnan(scores).any() or (fold_ids < 0).any():
        raise AssertionError("not every row received an out-of-fold score")

    out = []
    for row, score, fold_id in zip(rows, scores, fold_ids, strict=True):
        result = dict(row)
        result["oof_score"] = float(score)
        result["oof_fold"] = int(fold_id)
        out.append(result)
    return out


def crossfit_value_scores(
    rows: list[dict[str, Any]],
    *,
    feature_keys: Sequence[str],
    target_key: str,
    group_key: str = "item_id",
    n_splits: int = 5,
    alpha: float = 1.0,
) -> list[dict[str, Any]]:
    if not rows:
        return []
    groups = np.asarray([row[group_key] for row in rows])
    unique_groups = np.unique(groups)
    splits = min(int(n_splits), len(unique_groups))
    if splits < 2:
        raise ValueError("cross-fitting requires at least two groups/folds")

    X = _matrix(rows, feature_keys)
    y = np.asarray([float(row[target_key]) for row in rows], dtype=np.float64)
    scores = np.full(len(rows), np.nan, dtype=np.float64)
    fold_ids = np.full(len(rows), -1, dtype=np.int64)

    for fold_id, (train_idx, test_idx) in enumerate(GroupKFold(n_splits=splits).split(X, y, groups)):
        if set(groups[train_idx]) & set(groups[test_idx]):
            raise AssertionError("group leakage detected")
        model = Pipeline(
            steps=[
                ("preprocess", _preprocessor(len(feature_keys))),
                ("reg", Ridge(alpha=float(alpha))),
            ]
        )
        model.fit(X[train_idx], y[train_idx])
        scores[test_idx] = model.predict(X[test_idx])
        fold_ids[test_idx] = fold_id

    if np.isnan(scores).any() or (fold_ids < 0).any():
        raise AssertionError("not every row received an out-of-fold value estimate")

    out = []
    for row, score, fold_id in zip(rows, scores, fold_ids, strict=True):
        result = dict(row)
        result["oof_value"] = float(score)
        result["oof_fold"] = int(fold_id)
        out.append(result)
    return out
