from __future__ import annotations

import ast
import math
import os
import re
import resource
import subprocess
import sys
import tempfile
from dataclasses import dataclass
from decimal import Decimal, InvalidOperation
from pathlib import Path
from typing import Any, Protocol

import numpy as np
from datasets import load_dataset

from repairable_diffusion.src.utils.math_eval import extract_boxed_answer, normalize_math_answer


TASK_ADAPTER_VERSION = "v2.1"


def _deterministic_indices(length: int, cfg: dict[str, Any]) -> list[int]:
    """Return a predeclared deterministic subset without V1's prefix-slice bias."""

    if length <= 0:
        return []
    explicit = cfg.get("indices")
    if explicit is not None:
        values = [int(x) for x in explicit]
        if len(values) != len(set(values)):
            raise ValueError("dataset.indices contains duplicates")
        if any(x < 0 or x >= length for x in values):
            raise ValueError("dataset.indices contains out-of-range index")
        return values
    limit = cfg.get("limit")
    if limit is None:
        return list(range(length))
    limit = min(int(limit), length)
    rng = np.random.default_rng(int(cfg.get("sample_seed", 1729)))
    # Sort only to make artifact diffs stable; selection itself is randomized.
    return sorted(int(x) for x in rng.choice(length, size=limit, replace=False).tolist())


def _last_number(text: str) -> str | None:
    matches = re.findall(r"[-+]?\d[\d,]*(?:\.\d+)?(?:[eE][-+]?\d+)?", text or "")
    return matches[-1].replace(",", "") if matches else None


def _extract_fenced_code(text: str) -> str:
    blocks = re.findall(r"```(?:python)?\s*(.*?)```", text or "", flags=re.IGNORECASE | re.DOTALL)
    if blocks:
        return blocks[-1].strip()
    return (text or "").strip()


def _basic_latex_to_sympy(text: str) -> str:
    out = normalize_math_answer(text)
    out = out.replace("\\cdot", "*").replace("\\times", "*").replace("\\pi", "pi")
    out = out.replace("^", "**")
    # Resolve simple nested-free fractions/square roots repeatedly. This is not a
    # general LaTeX parser, but covers the short MATH-500 answer forms used here.
    frac = re.compile(r"\\frac\{([^{}]+)\}\{([^{}]+)\}")
    sqrt = re.compile(r"\\sqrt\{([^{}]+)\}")
    previous = None
    while previous != out:
        previous = out
        out = frac.sub(r"((\1)/(\2))", out)
        out = sqrt.sub(r"sqrt(\1)", out)
    out = out.replace("{", "(").replace("}", ")")
    out = out.replace("\\", "")
    return out


def math_equivalent(prediction: str | None, gold: str | None) -> bool:
    if prediction is None or gold is None:
        return False
    pred = normalize_math_answer(prediction)
    target = normalize_math_answer(extract_boxed_answer(gold) or gold)
    if not pred or not target:
        return False
    if pred == target:
        return True
    try:
        from sympy import simplify, sympify

        p_expr = sympify(_basic_latex_to_sympy(pred), evaluate=True)
        g_expr = sympify(_basic_latex_to_sympy(target), evaluate=True)
        return bool(simplify(p_expr - g_expr) == 0)
    except Exception:
        pass
    try:
        return math.isclose(float(pred), float(target), rel_tol=1e-9, abs_tol=1e-9)
    except Exception:
        return False


class TaskAdapter(Protocol):
    evaluator_id: str
    evaluator_version: str

    def load_records(self, cfg: dict[str, Any]) -> list[dict[str, Any]]: ...

    def build_prompt(self, item: dict[str, Any], tokenizer: Any) -> tuple[str, str]: ...

    def extract_prediction(self, text: str) -> str | None: ...

    def canonicalize(self, prediction: str | None) -> str: ...

    def evaluate(self, prediction: str | None, gold: Any, *, item: dict[str, Any] | None = None) -> bool: ...


@dataclass
class BaseAdapter:
    evaluator_id: str
    evaluator_version: str = TASK_ADAPTER_VERSION

    def build_prompt(self, item: dict[str, Any], tokenizer: Any) -> tuple[str, str]:
        user_content = str(item["question"])
        if hasattr(tokenizer, "apply_chat_template"):
            prompt = tokenizer.apply_chat_template(
                [{"role": "user", "content": user_content}],
                add_generation_prompt=True,
                tokenize=False,
            )
        else:
            prompt = f"User: {user_content}\nAssistant:"
        return user_content, prompt

    def canonicalize(self, prediction: str | None) -> str:
        return (prediction or "").strip()


class Math500Adapter(BaseAdapter):
    def __init__(self) -> None:
        super().__init__("math500_symbolic_equivalence")

    def load_records(self, cfg: dict[str, Any]) -> list[dict[str, Any]]:
        ds = load_dataset(cfg.get("path", "HuggingFaceH4/MATH-500"), split=cfg.get("split", "test"))
        rows: list[dict[str, Any]] = []
        for idx in _deterministic_indices(len(ds), cfg):
            raw = dict(ds[int(idx)])
            question = str(raw.get("problem") or raw.get("question") or "").strip()
            gold = raw.get("answer") or raw.get("solution") or raw.get("final_answer")
            if not question or gold is None:
                raise ValueError(f"invalid MATH-500 row index={idx}")
            rows.append({"item_id": int(idx), "question": question, "answer": str(gold), "raw": raw})
        return rows

    def build_prompt(self, item: dict[str, Any], tokenizer: Any) -> tuple[str, str]:
        user_content = f"{item['question']}\nPlease reason step by step, and put your final answer within \\boxed{{}}."
        prompt = tokenizer.apply_chat_template(
            [{"role": "user", "content": user_content}], add_generation_prompt=True, tokenize=False
        )
        return user_content, prompt

    def extract_prediction(self, text: str) -> str | None:
        return extract_boxed_answer(text) or _last_number(text)

    def canonicalize(self, prediction: str | None) -> str:
        return normalize_math_answer(prediction)

    def evaluate(self, prediction: str | None, gold: Any, *, item: dict[str, Any] | None = None) -> bool:
        return math_equivalent(prediction, str(gold))


class GSM8KAdapter(BaseAdapter):
    def __init__(self) -> None:
        super().__init__("gsm8k_numeric")

    def load_records(self, cfg: dict[str, Any]) -> list[dict[str, Any]]:
        ds = load_dataset(
            cfg.get("path", "openai/gsm8k"), cfg.get("config_name", "main"), split=cfg.get("split", "test")
        )
        rows = []
        for idx in _deterministic_indices(len(ds), cfg):
            raw = dict(ds[int(idx)])
            gold = str(raw["answer"])
            if "####" in gold:
                gold = gold.split("####")[-1].strip()
            gold_num = _last_number(gold) or gold.replace(",", "").strip()
            rows.append({"item_id": int(idx), "question": str(raw["question"]).strip(), "answer": gold_num, "raw": raw})
        return rows

    def build_prompt(self, item: dict[str, Any], tokenizer: Any) -> tuple[str, str]:
        user_content = f"{item['question']}\nReason step by step. Put the final numeric answer within \\boxed{{}}."
        prompt = tokenizer.apply_chat_template(
            [{"role": "user", "content": user_content}], add_generation_prompt=True, tokenize=False
        )
        return user_content, prompt

    def extract_prediction(self, text: str) -> str | None:
        boxed = extract_boxed_answer(text)
        return _last_number(boxed) if boxed else _last_number(text)

    def canonicalize(self, prediction: str | None) -> str:
        if prediction is None:
            return ""
        value = _last_number(prediction) or prediction.replace(",", "").strip()
        try:
            return str(Decimal(value).normalize())
        except InvalidOperation:
            return value

    def evaluate(self, prediction: str | None, gold: Any, *, item: dict[str, Any] | None = None) -> bool:
        return bool(self.canonicalize(prediction)) and self.canonicalize(prediction) == self.canonicalize(str(gold))


class BBHLogicalDeductionAdapter(BaseAdapter):
    ALLOWED_TASKS = {
        "logical_deduction_three_objects",
        "logical_deduction_five_objects",
        "logical_deduction_seven_objects",
    }

    def __init__(self) -> None:
        super().__init__("bbh_exact_choice")

    def load_records(self, cfg: dict[str, Any]) -> list[dict[str, Any]]:
        task = str(cfg.get("config_name") or cfg.get("task") or "")
        if task not in self.ALLOWED_TASKS:
            raise ValueError(f"BBH task is not frozen/allowed: {task}")
        path = cfg.get("path", "maveriq/bigbenchhard")
        ds = load_dataset(path, task, split=cfg.get("split", "train"))
        rows = []
        for idx in _deterministic_indices(len(ds), cfg):
            raw = dict(ds[int(idx)])
            question = str(raw.get("input") or raw.get("question") or raw.get("prompt") or "").strip()
            gold = str(raw.get("target") or raw.get("answer") or "").strip()
            if not question or not gold:
                raise ValueError(f"invalid BBH row {task}:{idx}")
            rows.append({"item_id": int(idx), "question": question, "answer": gold, "raw": raw, "task": task})
        return rows

    def build_prompt(self, item: dict[str, Any], tokenizer: Any) -> tuple[str, str]:
        user_content = (
            f"{item['question']}\nReason carefully. On the final line output only the answer choice, for example (A)."
        )
        prompt = tokenizer.apply_chat_template(
            [{"role": "user", "content": user_content}], add_generation_prompt=True, tokenize=False
        )
        return user_content, prompt

    def extract_prediction(self, text: str) -> str | None:
        matches = re.findall(r"\(([A-Z])\)", text or "", flags=re.IGNORECASE)
        if matches:
            return f"({matches[-1].upper()})"
        tail = (text or "").strip().splitlines()
        return tail[-1].strip() if tail else None

    def canonicalize(self, prediction: str | None) -> str:
        if not prediction:
            return ""
        m = re.search(r"\(?\b([A-Z])\b\)?", prediction.strip(), flags=re.IGNORECASE)
        return f"({m.group(1).upper()})" if m else prediction.strip().lower()

    def evaluate(self, prediction: str | None, gold: Any, *, item: dict[str, Any] | None = None) -> bool:
        return bool(self.canonicalize(prediction)) and self.canonicalize(prediction) == self.canonicalize(str(gold))


_ALLOWED_IMPORTS = {
    "math",
    "itertools",
    "functools",
    "collections",
    "heapq",
    "bisect",
    "re",
    "statistics",
    "string",
    "typing",
}
_FORBIDDEN_CALLS = {"open", "eval", "exec", "compile", "__import__", "input", "breakpoint"}


def _validate_untrusted_python(source: str) -> None:
    tree = ast.parse(source)
    for node in ast.walk(tree):
        if isinstance(node, ast.Import):
            for alias in node.names:
                if alias.name.split(".")[0] not in _ALLOWED_IMPORTS:
                    raise ValueError(f"forbidden import: {alias.name}")
        elif isinstance(node, ast.ImportFrom):
            module = (node.module or "").split(".")[0]
            if module not in _ALLOWED_IMPORTS:
                raise ValueError(f"forbidden import-from: {node.module}")
        elif isinstance(node, ast.Call) and isinstance(node.func, ast.Name) and node.func.id in _FORBIDDEN_CALLS:
            raise ValueError(f"forbidden call: {node.func.id}")
        elif isinstance(node, ast.Attribute) and node.attr.startswith("__"):
            raise ValueError(f"forbidden dunder attribute: {node.attr}")


def _sandbox_limits() -> None:
    # Linux worker limits. Do not weaken these in Codex runs without human approval.
    resource.setrlimit(resource.RLIMIT_CPU, (3, 3))
    resource.setrlimit(resource.RLIMIT_AS, (768 * 1024 * 1024, 768 * 1024 * 1024))
    resource.setrlimit(resource.RLIMIT_FSIZE, (1024 * 1024, 1024 * 1024))
    resource.setrlimit(resource.RLIMIT_NOFILE, (32, 32))
    try:
        resource.setrlimit(resource.RLIMIT_NPROC, (0, 0))
    except (ValueError, OSError):
        pass


class RestrictedPythonEvaluator:
    evaluator_id = "mbpp_restricted_subprocess"
    evaluator_version = TASK_ADAPTER_VERSION

    def evaluate(self, code: str, tests: list[str], *, timeout_seconds: float = 5.0) -> bool:
        _validate_untrusted_python(code)
        for test in tests:
            _validate_untrusted_python(test)
        source = code.rstrip() + "\n\n" + "\n".join(tests) + "\n"
        with tempfile.TemporaryDirectory(prefix="mbpp_v2_") as tmp:
            path = Path(tmp) / "candidate.py"
            path.write_text(source, encoding="utf-8")
            env = {"PYTHONHASHSEED": "0", "PYTHONNOUSERSITE": "1", "PATH": os.environ.get("PATH", "")}
            try:
                proc = subprocess.run(
                    [sys.executable, "-I", str(path)],
                    cwd=tmp,
                    env=env,
                    stdout=subprocess.DEVNULL,
                    stderr=subprocess.DEVNULL,
                    timeout=timeout_seconds,
                    preexec_fn=_sandbox_limits if os.name == "posix" else None,
                    check=False,
                )
            except subprocess.TimeoutExpired:
                return False
            return proc.returncode == 0

    def self_test(self) -> None:
        if not self.evaluate("def add(a, b):\n    return a + b", ["assert add(2, 3) == 5"]):
            raise RuntimeError("MBPP sandbox self-test failed for valid program")
        try:
            self.evaluate("import os\ndef f():\n    return 1", ["assert f() == 1"])
        except ValueError:
            return
        raise RuntimeError("MBPP sandbox self-test failed to reject forbidden import")


class MBPPAdapter(BaseAdapter):
    def __init__(self) -> None:
        super().__init__("mbpp_restricted_execution")
        self.executor = RestrictedPythonEvaluator()

    def load_records(self, cfg: dict[str, Any]) -> list[dict[str, Any]]:
        ds = load_dataset(
            cfg.get("path", "google-research-datasets/mbpp"),
            cfg.get("config_name", "sanitized"),
            split=cfg.get("split", "test"),
        )
        rows = []
        for idx in _deterministic_indices(len(ds), cfg):
            raw = dict(ds[int(idx)])
            question = str(raw.get("prompt") or raw.get("text") or "").strip()
            tests = list(raw.get("test_list") or []) + list(raw.get("challenge_test_list") or [])
            if not question or not tests:
                raise ValueError(f"invalid MBPP row index={idx}")
            rows.append(
                {
                    "item_id": int(idx),
                    "question": question,
                    "answer": str(raw.get("code") or ""),
                    "tests": tests,
                    "raw": raw,
                }
            )
        return rows

    def build_prompt(self, item: dict[str, Any], tokenizer: Any) -> tuple[str, str]:
        tests = "\n".join(str(x) for x in item.get("tests", [])[:3])
        user_content = (
            f"Write a Python function that solves the following task. Return executable Python code only.\n\n"
            f"Task:\n{item['question']}\n\nTests:\n{tests}"
        )
        prompt = tokenizer.apply_chat_template(
            [{"role": "user", "content": user_content}], add_generation_prompt=True, tokenize=False
        )
        return user_content, prompt

    def extract_prediction(self, text: str) -> str | None:
        code = _extract_fenced_code(text)
        return code if code else None

    def canonicalize(self, prediction: str | None) -> str:
        return (prediction or "").strip()

    def evaluate(self, prediction: str | None, gold: Any, *, item: dict[str, Any] | None = None) -> bool:
        if not prediction or item is None:
            return False
        tests = list(item.get("tests") or item.get("raw", {}).get("test_list") or [])
        if item.get("raw", {}).get("challenge_test_list"):
            tests += list(item["raw"]["challenge_test_list"])
        try:
            return self.executor.evaluate(prediction, tests)
        except (SyntaxError, ValueError):
            return False


def create_task_adapter(cfg: dict[str, Any]) -> TaskAdapter:
    name = str(cfg.get("name", "")).lower()
    if name == "math500":
        return Math500Adapter()
    if name == "gsm8k":
        return GSM8KAdapter()
    if name in {"bbh", "bbh_predeclared_structured"}:
        return BBHLogicalDeductionAdapter()
    if name == "mbpp":
        return MBPPAdapter()
    raise ValueError(f"Unsupported V2 dataset.name: {cfg.get('name')}")
