from __future__ import annotations

import datetime as dt
import json
import pickle
from pathlib import Path
from typing import Any

import yaml


def ensure_dir(path: str | Path) -> Path:
    out = Path(path)
    out.mkdir(parents=True, exist_ok=True)
    return out


def now_tag() -> str:
    return dt.datetime.now().strftime("%Y%m%d_%H%M%S")


def load_yaml(path: str | Path) -> dict[str, Any]:
    with open(path, "r", encoding="utf-8") as fh:
        return yaml.safe_load(fh)


def load_json(path: str | Path) -> Any:
    with open(path, "r", encoding="utf-8") as fh:
        return json.load(fh)


def save_json(path: str | Path, payload: Any) -> None:
    path = Path(path)
    ensure_dir(path.parent)
    with open(path, "w", encoding="utf-8") as fh:
        json.dump(payload, fh, indent=2, ensure_ascii=False)


def save_yaml(path: str | Path, payload: Any) -> None:
    path = Path(path)
    ensure_dir(path.parent)
    with open(path, "w", encoding="utf-8") as fh:
        yaml.safe_dump(payload, fh, sort_keys=False, allow_unicode=True)


def save_jsonl(path: str | Path, rows: list[dict[str, Any]]) -> None:
    path = Path(path)
    ensure_dir(path.parent)
    with open(path, "w", encoding="utf-8") as fh:
        for row in rows:
            fh.write(json.dumps(row, ensure_ascii=False) + "\n")


def save_pickle(path: str | Path, payload: Any) -> None:
    path = Path(path)
    ensure_dir(path.parent)
    with open(path, "wb") as fh:
        pickle.dump(payload, fh)


def load_pickle(path: str | Path) -> Any:
    with open(path, "rb") as fh:
        return pickle.load(fh)


def init_run_dir(cfg: dict[str, Any]) -> Path:
    outputs_root = ensure_dir(cfg["paths"]["outputs_root"])
    run_name = cfg["paths"].get("run_name") or "auto"
    if run_name == "auto":
        run_name = now_tag()
    run_dir = outputs_root / run_name
    ensure_dir(run_dir)
    return run_dir
