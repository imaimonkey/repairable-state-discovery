"""Pinned upstream source, native prompts/datasets and evaluator adapters.

Upstream functions are loaded from verified bytes, not reimplemented. OpenCompass
registry decorators and its unused framework base are removed by AST extraction;
the actual postprocessors and scoring method bodies remain byte-source derived.
"""
from __future__ import annotations

import ast
import hashlib
import importlib.util
import json
import re
import urllib.request
import zipfile
from pathlib import Path
from types import SimpleNamespace
from typing import Any


def sha256_file(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def verified_download(url: str, path: Path, expected: str) -> Path:
    if not path.exists():
        path.parent.mkdir(parents=True, exist_ok=True)
        data = urllib.request.urlopen(url, timeout=120).read()
        if hashlib.sha256(data).hexdigest() != expected:
            raise ValueError(f"upstream download hash mismatch: {url}")
        temporary = path.with_suffix(path.suffix + ".partial")
        temporary.write_bytes(data)
        temporary.replace(path)
    if sha256_file(path) != expected:
        raise ValueError(f"pinned source mismatch: {path}")
    return path


def ensure_sources(recipe: dict, cache: Path) -> dict[str, Path]:
    return {entry["path"]: verified_download(entry["url"], cache / recipe["backbone"] / entry["path"], entry["sha256"])
            for entry in recipe["source_files"]}


def import_file(path: Path, name: str) -> Any:
    spec = importlib.util.spec_from_file_location(name, path)
    module = importlib.util.module_from_spec(spec)
    assert spec and spec.loader
    spec.loader.exec_module(module)
    return module


def source_definitions(path: Path, names: set[str], namespace: dict | None = None) -> SimpleNamespace:
    """Extract exact named upstream function/class bodies; no rewrite of logic."""
    tree = ast.parse(path.read_text())
    definitions = []
    for node in tree.body:
        if isinstance(node, (ast.FunctionDef, ast.ClassDef)) and node.name in names:
            node.decorator_list = []
            definitions.append(node)
    if {node.name for node in definitions} != names:
        raise ValueError(f"missing pinned definitions: {names}")
    env = {"re": re, **(namespace or {})}
    exec(compile(ast.fix_missing_locations(ast.Module(body=definitions, type_ignores=[])), str(path), "exec"), env)
    return SimpleNamespace(**env)


def native_messages(backbone: str, task: str, question: str, sources: dict[str, Path]) -> list[dict]:
    if backbone == "dream":
        content = f"Problem:\n{question}\n\nSolution:" if task == "math500" else f"Q: {question}\nA:"
        return [{"role": "user", "content": content}]
    suffix = "math/math_0shot_gen_11c4b5.py" if task == "math500" else "gsm8k/gsm8k_gen_1d7fe4.py"
    path = sources["opencompass/opencompass/configs/datasets/" + suffix]
    tree = ast.parse(path.read_text())
    # Dict(role=...,prompt=...) nodes inside the exact pinned round list.
    rounds = [kw.value for node in ast.walk(tree) if isinstance(node, ast.Call)
              for kw in node.keywords if kw.arg == "round"]
    if len(rounds) != 1 or not isinstance(rounds[0], ast.List):
        raise ValueError("unsupported upstream prompt layout")
    messages = []
    for node in rounds[0].elts:
        raw = {kw.arg: ast.literal_eval(kw.value) for kw in node.keywords}
        messages.append({"role": {"HUMAN": "user", "BOT": "assistant"}[raw["role"]],
                         "content": raw["prompt"].replace("{question}", question).replace("{problem}", question)})
    return messages


def load_records(recipe: dict, task: str, mode: str, cache: Path) -> list[dict]:
    """Load native full benchmark or exact paper bridge with pinned data revision."""
    from datasets import load_dataset
    cfg = recipe["tasks"][task]["native_dataset" if mode == "native" else "bridge_dataset"]
    rows: list[dict] = []
    if "url" in cfg:
        zpath = verified_download(cfg["url"], cache / "datasets" / (cfg["path"].split("/")[-1] + ".zip"), cfg["sha256"])
        with zipfile.ZipFile(zpath) as archive:
            if task == "math500":
                raw = json.loads(archive.read("math/math.json"))
                raw_rows = [(str(k), v) for k, v in raw.items()]
            else:
                raw_rows = [(str(i), json.loads(line)) for i, line in enumerate(archive.read("gsm8k/test.jsonl").decode().splitlines())]
    else:
        configs = cfg.get("config_names", [cfg.get("config_name")])
        raw_rows = []
        for config in configs:
            ds = load_dataset(cfg["path"], config, split=cfg["split"], revision=cfg["revision"], trust_remote_code=True)
            raw_rows.extend((f"{config}:{i}" if len(configs) > 1 else str(i), dict(row)) for i, row in enumerate(ds))
    for item_id, raw in raw_rows:
        gold = str(raw.get("answer", raw.get("solution", "")))
        question = str(raw.get("problem", raw.get("question", "")))
        if not question or not gold:
            raise ValueError(f"invalid native row {item_id}")
        rows.append({"item_id": item_id, "question": question, "answer": gold, "raw": raw})
    if len(rows) != cfg["count"]:
        raise ValueError(f"dataset count mismatch: {len(rows)} != {cfg['count']}")
    return rows


class _FrameworkBase:
    def __init__(self, **kwargs):
        pass


class OfficialEvaluator:
    def __init__(self, backbone: str, task: str, sources: dict[str, Path]):
        self.backbone, self.task = backbone, task
        if backbone == "llada":
            path = sources[f"opencompass/opencompass/datasets/{'math' if task == 'math500' else 'gsm8k'}.py"]
            names = ({"last_boxed_only_string", "remove_boxed", "extract_boxed_answer", "normalize_final_answer", "math_postprocess_v2", "MATHEvaluator"}
                     if task == "math500" else {"gsm8k_dataset_postprocess", "gsm8k_postprocess", "Gsm8kEvaluator"})
            self.module = source_definitions(path, names, {"BaseEvaluator": _FrameworkBase})
            self.evaluator = self.module.MATHEvaluator(version="v2") if task == "math500" else self.module.Gsm8kEvaluator()
        elif task == "math500":
            self.module = import_file(sources["eval_instruct/lm_eval/tasks/minerva_math/utils.py"], "v2r_dream_math")
        else:
            self.module = source_definitions(sources["eval_instruct/lm_eval/filters/extraction.py"], {"RegexFilter"}, {"Filter": object})

    def evaluate(self, text: str, item: dict) -> dict:
        gold = item["answer"]
        if self.backbone == "llada" and self.task == "math500":
            prediction = self.module.math_postprocess_v2(text)
            target = self.module.extract_boxed_answer(gold) or gold
            return {"answer": prediction, "correct": bool(self.evaluator.is_equiv(prediction, target)), "metric": "OpenCompass_MATHEvaluator_v2"}
        if self.backbone == "llada":
            target = self.module.gsm8k_dataset_postprocess(gold) if "#### " in gold else gold.replace(",", "")
            prediction = self.module.gsm8k_postprocess(text)
            return {"answer": prediction, "correct": bool(self.evaluator.is_equal(prediction, target)), "metric": "OpenCompass_Gsm8kEvaluator"}
        if self.task == "math500":
            boxed = self.module.last_boxed_only_string(gold)
            target = self.module.normalize_final_answer(self.module.remove_boxed(boxed) if boxed else gold)
            scores = self.module.process_results({"answer": target}, [text])
            prediction = self.module.normalize_final_answer(self.module.get_unnormalized_answer(text))
            return {"answer": prediction, "correct": bool(scores["exact_match"]), "metrics": scores, "metric": "Dream_minerva_exact_match"}
        target = gold.split("####")[-1].strip()
        values = {}
        predictions = {}
        for name, pattern, group in [("strict-match", r"The answer is (\-?[0-9\.\,]+).", 0),
                                     ("flexible-extract", r"(-?[$0-9.,]{2,})|(-?[0-9]+)", -1)]:
            prediction = self.module.RegexFilter(regex_pattern=pattern, group_select=group).apply([[text]], [item])[0][0]
            # Exact source YAML regexes_to_ignore and ignore_case normalization.
            def norm(s):
                for pattern in [",", r"\$", r"(?s).*#### ", r"\.$"]:
                    s = re.sub(pattern, "", s)
                return s.lower()
            values[name] = norm(prediction) == norm(target)
            predictions[name] = prediction
        return {"answer": predictions["flexible-extract"], "correct": values["flexible-extract"], "metrics": values, "metric": "Dream_gsm8k_flexible_extract"}


def bridge_evaluate(task: str, text: str, item: dict) -> dict:
    from repairable_diffusion.src.v2.task_adapters import GSM8KAdapter, Math500Adapter
    adapter = Math500Adapter() if task == "math500" else GSM8KAdapter()
    prediction = adapter.extract_prediction(text)
    gold = item["answer"].split("####")[-1].strip() if task == "gsm8k" else item["answer"]
    return {"answer": prediction, "correct": bool(adapter.evaluate(prediction, gold, item=item)), "metric": adapter.evaluator_id}
