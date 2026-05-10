from __future__ import annotations

import re
from typing import Any

from datasets import load_dataset


def _pick_question(row: dict[str, Any]) -> str:
    for key in ("problem", "question", "prompt"):
        value = row.get(key)
        if isinstance(value, str) and value.strip():
            return value.strip()
    raise KeyError(f"Could not find question field in row keys={list(row.keys())}")


def _pick_answer(row: dict[str, Any]) -> str:
    for key in ("answer", "solution", "final_answer"):
        value = row.get(key)
        if isinstance(value, str) and value.strip():
            return value.strip()
    raise KeyError(f"Could not find answer field in row keys={list(row.keys())}")


def load_math500(cfg: dict[str, Any]) -> list[dict[str, Any]]:
    ds = load_dataset(cfg["path"], split=cfg.get("split", "test"))
    start = int(cfg.get("start_index", 0))
    limit = int(cfg.get("limit", len(ds)))
    end = min(len(ds), start + limit)
    rows = []
    for local_idx, row in enumerate(ds.select(range(start, end))):
        rows.append(
            {
                "item_id": start + local_idx,
                "question": _pick_question(row),
                "answer": _pick_answer(row),
                "raw": dict(row),
            }
        )
    return rows


def _extract_gsm8k_answer(answer: str) -> str:
    text = answer.strip()
    if "####" in text:
        text = text.split("####")[-1].strip()
    text = text.replace(",", "")
    match = re.search(r"-?\d+(?:\.\d+)?", text)
    return match.group(0) if match else text


def load_gsm8k(cfg: dict[str, Any]) -> list[dict[str, Any]]:
    ds = load_dataset(cfg["path"], cfg.get("config_name", "main"), split=cfg.get("split", "test"))
    start = int(cfg.get("start_index", 0))
    limit = int(cfg.get("limit", len(ds)))
    end = min(len(ds), start + limit)
    rows = []
    for local_idx, row in enumerate(ds.select(range(start, end))):
        rows.append(
            {
                "item_id": start + local_idx,
                "question": _pick_question(row),
                "answer": _extract_gsm8k_answer(_pick_answer(row)),
                "raw": dict(row),
            }
        )
    return rows


def load_dataset_records(cfg: dict[str, Any]) -> list[dict[str, Any]]:
    name = cfg.get("name", "").lower()
    if name == "math500":
        return load_math500(cfg)
    if name == "gsm8k":
        return load_gsm8k(cfg)
    raise ValueError(f"Unsupported dataset.name: {cfg.get('name')}")
