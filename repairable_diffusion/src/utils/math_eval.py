from __future__ import annotations

import re
from typing import Any


def last_boxed_only_string(text: str) -> str | None:
    idx = text.rfind("\\boxed")
    if idx < 0:
        return None
    i = idx
    depth = 0
    end = None
    while i < len(text):
        if text[i] == "{":
            depth += 1
        elif text[i] == "}":
            depth -= 1
            if depth == 0:
                end = i
                break
        i += 1
    if end is None:
        return None
    return text[idx : end + 1]


def remove_boxed(text: str) -> str | None:
    prefix = "\\boxed{"
    if text.startswith(prefix) and text.endswith("}"):
        return text[len(prefix) : -1]
    return None


def extract_boxed_answer(text: str) -> str | None:
    boxed = last_boxed_only_string(text)
    if boxed is None:
        return None
    return remove_boxed(boxed)


def normalize_math_answer(text: str | None) -> str:
    if not text:
        return ""
    out = text.strip()
    substitutions = [
        (" ", ""),
        ("\n", ""),
        ("\\left", ""),
        ("\\right", ""),
        ("\\!", ""),
        ("\\%", ""),
        ("$", ""),
        ("tfrac", "frac"),
        ("dfrac", "frac"),
    ]
    for before, after in substitutions:
        out = out.replace(before, after)
    out = re.sub(r"(\\text\{)(.*?)(\})", r"\2", out)
    if out.replace(",", "").isdigit():
        out = out.replace(",", "")
    if "/" in out and len(out.split("/")) == 2:
        a, b = out.split("/", 1)
        if a.isdigit() and b.isdigit():
            out = f"\\frac{{{a}}}{{{b}}}"
    return out


def answers_match(prediction: str | None, gold: str | None) -> bool:
    pred = normalize_math_answer(prediction)
    tgt = normalize_math_answer(extract_boxed_answer(gold) or gold)
    return bool(pred) and pred == tgt


def build_diffusion_math_prompt(question: str, tokenizer: Any) -> tuple[str, str]:
    user_content = f"{question}\nPlease reason step by step, and put your final answer within \\boxed{{}}."
    messages = [{"role": "user", "content": user_content}]
    prompt = tokenizer.apply_chat_template(messages, add_generation_prompt=True, tokenize=False)
    return user_content, prompt


def build_ar_math_prompt(question: str, tokenizer: Any) -> tuple[str, str]:
    user_content = (
        f"{question}\nSolve it step by step. End with your final answer in \\boxed{{}}."
    )
    if hasattr(tokenizer, "apply_chat_template"):
        messages = [{"role": "user", "content": user_content}]
        prompt = tokenizer.apply_chat_template(messages, add_generation_prompt=True, tokenize=False)
    else:
        prompt = f"Question: {question}\nAnswer step by step and end with \\boxed{{}}.\nAnswer:"
    return user_content, prompt
