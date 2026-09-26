"""Generation 3 task adapters backed by verified source-native V2R helpers.

The adapter deliberately delegates prompt, dataset, and evaluator semantics to
the pinned-byte loader in ``repairable_diffusion.src.v2r.reference_sources``.
Generation 3 adds an explicit namespace and confirmatory-population guard so a
MATH-500 bridge cannot be mistaken for the source-native OpenCompass MATH bank.
"""
from __future__ import annotations

import json
from pathlib import Path
from typing import Any

from repairable_diffusion.src.v2r.reference_sources import (
    OfficialEvaluator,
    ensure_sources,
    load_records,
    native_messages,
)


GENERATION_ID = "rsd_ref_v3"
ROOT = Path(__file__).resolve().parents[3]
RECIPE_ROOT = ROOT / "results/v2r_reference/reference_recipes"

TASKS: dict[str, dict[str, Any]] = {
    "llada_math": {
        "recipe": RECIPE_ROOT / "llada.json",
        "recipe_task": "math500",
        "mode": "native",
        "population": "source_native_opencompass_math",
        "count": 5000,
        "calibration_only": False,
    },
    "llada_gsm8k": {
        "recipe": RECIPE_ROOT / "llada.json",
        "recipe_task": "gsm8k",
        "mode": "native",
        "population": "source_native_opencompass_gsm8k",
        "count": 1319,
        "calibration_only": False,
    },
    "llada_math_calibration": {
        "recipe": RECIPE_ROOT / "llada.json",
        "recipe_task": "math500",
        "mode": "bridge",
        "population": "HuggingFaceH4/MATH-500",
        "count": 500,
        "calibration_only": True,
    },
}


def task_definition(task_id: str) -> dict[str, Any]:
    try:
        definition = dict(TASKS[task_id])
    except KeyError as exc:
        raise ValueError(f"unknown RSD Generation 3 task: {task_id}") from exc
    if definition["population"] == "HuggingFaceH4/MATH-500" and not definition["calibration_only"]:
        raise ValueError("MATH-500 bridge cannot be a Generation 3 confirmatory population")
    return definition


def load_recipe(task_id: str) -> dict[str, Any]:
    definition = task_definition(task_id)
    return json.loads(Path(definition["recipe"]).read_text(encoding="utf-8"))


def load_source_task(task_id: str, cache: Path) -> tuple[dict[str, Any], dict[str, Path], list[dict[str, Any]]]:
    """Load a frozen source-native task and assert its population count."""

    definition = task_definition(task_id)
    recipe = load_recipe(task_id)
    sources = ensure_sources(recipe, cache)
    rows = load_records(recipe, definition["recipe_task"], definition["mode"], cache)
    if len(rows) != definition["count"]:
        raise ValueError(f"{task_id} count mismatch: {len(rows)} != {definition['count']}")
    return recipe, sources, rows


def native_prompt(task_id: str, question: str, sources: dict[str, Path]) -> list[dict[str, str]]:
    definition = task_definition(task_id)
    recipe = load_recipe(task_id)
    return native_messages(recipe["backbone"], definition["recipe_task"], question, sources)


def evaluator(task_id: str, sources: dict[str, Path]) -> OfficialEvaluator:
    definition = task_definition(task_id)
    recipe = load_recipe(task_id)
    return OfficialEvaluator(recipe["backbone"], definition["recipe_task"], sources)
