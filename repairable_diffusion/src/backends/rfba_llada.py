from __future__ import annotations

import math
import os
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import Any

import numpy as np
import torch
import torch.nn.functional as F
from transformers import AutoTokenizer

from repairable_diffusion.src.utils.seed import seed_everything
from repairable_diffusion.src.utils.math_eval import (
    answers_match,
    build_diffusion_math_prompt,
    extract_boxed_answer,
)


def _ensure_rfba_on_path(rfba_root: str | Path) -> Path:
    root = Path(os.environ.get("RFBA_ROOT", str(rfba_root))).expanduser().resolve()
    if not root.exists():
        raise FileNotFoundError(f"rfba root not found: {root}")
    if str(root) not in sys.path:
        sys.path.insert(0, str(root))
    return root


def add_gumbel_noise(logits: torch.Tensor, temperature: float) -> torch.Tensor:
    if temperature == 0:
        return logits
    logits = logits.to(torch.float64)
    noise = torch.rand_like(logits, dtype=torch.float64)
    gumbel_noise = (-torch.log(noise)) ** temperature
    return logits.exp() / gumbel_noise


def get_num_transfer_tokens(mask_index: torch.Tensor, steps: int) -> torch.Tensor:
    mask_num = mask_index.sum(dim=1, keepdim=True)
    base = mask_num // steps
    remainder = mask_num % steps
    counts = torch.zeros(mask_num.size(0), steps, device=mask_index.device, dtype=torch.int64) + base
    for i in range(mask_num.size(0)):
        counts[i, : remainder[i]] += 1
    return counts


@dataclass
class Snapshot:
    step_index: int
    total_steps: int
    prompt_len: int
    full_token_ids: list[int]
    token_confidences: list[float | None]


class RFBALLADABackend:
    def __init__(self, cfg: dict[str, Any]):
        self.cfg = cfg
        self.root = _ensure_rfba_on_path(cfg["rfba_root"])
        if bool(cfg.get("fast", False)):
            from decoding.llada.modeling_llada_fast import LLaDAModelLM as LLaDAModelLMFast

            self.model_cls = LLaDAModelLMFast
        else:
            from decoding.llada.modeling_llada import LLaDAModelLM

            self.model_cls = LLaDAModelLM
        self.tokenizer = None
        self.model = None

    def load(self) -> None:
        if self.model is not None:
            return
        torch_dtype = getattr(torch, self.cfg.get("torch_dtype", "bfloat16"))
        model_path = self.cfg["model_path"]
        self.model = self.model_cls.from_pretrained(model_path, torch_dtype=torch_dtype)
        if self.cfg.get("device", "cuda") == "cuda" and torch.cuda.is_available():
            self.model = self.model.cuda()
        self.model.eval()
        self.tokenizer = AutoTokenizer.from_pretrained(
            model_path,
            trust_remote_code=bool(self.cfg.get("trust_remote_code", True)),
        )

    def _prompt_ids(self, question: str) -> tuple[str, str, torch.Tensor]:
        self.load()
        prompt_text, prompt = build_diffusion_math_prompt(question, self.tokenizer)
        prompt_ids = self.tokenizer(prompt, return_tensors="pt").input_ids
        if torch.cuda.is_available() and next(self.model.parameters()).is_cuda:
            prompt_ids = prompt_ids.cuda()
        return prompt_text, prompt, prompt_ids

    def _decode_text(self, token_ids: torch.Tensor, prompt_len: int) -> str:
        return self.tokenizer.decode(token_ids[0, prompt_len:], skip_special_tokens=True)

    def _candidate_from_tokens(self, token_ids: torch.Tensor, prompt_len: int) -> str | None:
        text = self._decode_text(token_ids, prompt_len)
        return extract_boxed_answer(text)

    def _probs_for_tokens(self, probs: torch.Tensor, token_ids: torch.Tensor) -> torch.Tensor:
        gathered = torch.gather(probs, dim=-1, index=token_ids.unsqueeze(-1)).squeeze(-1)
        return gathered

    def generate_trajectory(self, item: dict[str, Any], trajectory_id: int, generation_cfg: dict[str, Any]) -> dict[str, Any]:
        question = item["question"]
        gold = item["answer"]
        seed = int(generation_cfg["base_seed"]) + trajectory_id + int(item["item_id"]) * 10000
        seed_everything(seed)
        prompt_text, prompt, prompt_ids = self._prompt_ids(question)

        steps = int(generation_cfg["steps"])
        gen_length = int(generation_cfg["gen_length"])
        block_length = int(generation_cfg["block_length"])
        temperature = float(generation_cfg["temperature"])
        cfg_scale = float(generation_cfg["cfg_scale"])
        remasking = generation_cfg["remasking"]
        mask_id = int(generation_cfg["mask_id"])
        checkpoint_stride = int(generation_cfg["checkpoint_stride"])

        x = torch.full(
            (1, prompt_ids.shape[1] + gen_length),
            mask_id,
            dtype=torch.long,
            device=prompt_ids.device,
        )
        x[:, : prompt_ids.shape[1]] = prompt_ids.clone()
        prompt_len = prompt_ids.shape[1]

        if gen_length % block_length != 0:
            raise ValueError("gen_length must be divisible by block_length")
        num_blocks = gen_length // block_length
        if steps % num_blocks != 0:
            raise ValueError("steps must be divisible by num_blocks")
        steps_per_block = steps // num_blocks

        rows: list[dict[str, Any]] = []
        plan = None

        for step_index in range(1, steps + 1):
            block_index = (step_index - 1) // steps_per_block
            local_step = (step_index - 1) % steps_per_block
            block_start = prompt_len + block_index * block_length
            block_end = prompt_len + (block_index + 1) * block_length
            mask_index = x == mask_id

            if local_step == 0:
                plan = get_num_transfer_tokens(mask_index[:, block_start:block_end], steps_per_block)

            with torch.no_grad():
                if cfg_scale > 0:
                    raise NotImplementedError("cfg_scale > 0 is not implemented in this project")
                logits = self.model(x).logits
                probs = F.softmax(logits.to(torch.float32), dim=-1)
                logits_with_noise = add_gumbel_noise(logits, temperature=temperature)
                x0 = torch.argmax(logits_with_noise, dim=-1)
                if remasking == "low_confidence":
                    x0_p = self._probs_for_tokens(probs, x0)
                elif remasking == "random":
                    x0_p = torch.rand((x0.shape[0], x0.shape[1]), device=x0.device)
                else:
                    raise NotImplementedError(remasking)

            x0[:, block_end:] = mask_id
            x0 = torch.where(mask_index, x0, x)
            confidence = torch.where(mask_index, x0_p, torch.full_like(x0_p, float("-inf")))
            k = int(plan[0, local_step].item())
            transfer_index = torch.zeros_like(x, dtype=torch.bool)
            if k > 0:
                _, selected = torch.topk(confidence[0], k=k)
                transfer_index[0, selected] = True

            next_x = x.clone()
            next_x[transfer_index] = x0[transfer_index]

            gen_mask = next_x[0, prompt_len:] == mask_id
            chosen_probs = self._probs_for_tokens(probs[:, prompt_len:, :], next_x[:, prompt_len:])
            conf_values = chosen_probs[0].detach().cpu().tolist()
            token_confidences: list[float | None] = [
                None if bool(gen_mask[pos].item()) else float(conf_values[pos]) for pos in range(gen_length)
            ]

            masked_probs = probs[0, prompt_len:][gen_mask]
            if masked_probs.numel() > 0:
                entropy = -(masked_probs * torch.log(masked_probs.clamp(min=1e-12))).sum(dim=-1)
                masked_entropy_mean = float(entropy.mean().item())
                masked_entropy_max = float(entropy.max().item())
            else:
                masked_entropy_mean = 0.0
                masked_entropy_max = 0.0

            provisional_answer = self._candidate_from_tokens(next_x, prompt_len)
            new_positions = (transfer_index[0, prompt_len:]).nonzero(as_tuple=False).view(-1).cpu().tolist()
            new_conf = [conf_values[pos] for pos in new_positions] if new_positions else []

            row = {
                "step_index": step_index,
                "total_steps": steps,
                "block_index": block_index,
                "step_in_block": local_step + 1,
                "masked_ratio": float(gen_mask.float().mean().item()),
                "commitment_ratio": float((~gen_mask).float().mean().item()),
                "new_positions": new_positions,
                "new_token_conf_mean": float(np.mean(new_conf)) if new_conf else 0.0,
                "state_token_conf_mean": float(np.mean([v for v in token_confidences if v is not None])) if any(v is not None for v in token_confidences) else 0.0,
                "state_token_conf_min": float(np.min([v for v in token_confidences if v is not None])) if any(v is not None for v in token_confidences) else 0.0,
                "masked_entropy_mean": masked_entropy_mean,
                "masked_entropy_max": masked_entropy_max,
                "answer_candidate": provisional_answer,
                "snapshot": None,
            }

            if step_index % checkpoint_stride == 0 or step_index == steps:
                row["snapshot"] = Snapshot(
                    step_index=step_index,
                    total_steps=steps,
                    prompt_len=prompt_len,
                    full_token_ids=next_x[0].detach().cpu().tolist(),
                    token_confidences=token_confidences,
                ).__dict__

            rows.append(row)
            x = next_x

        final_text = self._decode_text(x, prompt_len)
        final_answer = extract_boxed_answer(final_text)
        return {
            "item_id": item["item_id"],
            "trajectory_id": trajectory_id,
            "seed": seed,
            "question": question,
            "gold_answer": gold,
            "prompt_text": prompt_text,
            "prompt": prompt,
            "final_text": final_text,
            "final_answer": final_answer,
            "correct": answers_match(final_answer, gold),
            "steps": rows,
        }

    def _repair_positions(
        self,
        snapshot: Snapshot,
        repair_cfg: dict[str, Any],
        remask_fraction: float,
        rng: np.random.Generator,
    ) -> list[int]:
        confs = snapshot.token_confidences
        anchor = float(repair_cfg["anchor_confidence_threshold"])
        candidates = [(idx, conf) for idx, conf in enumerate(confs) if conf is not None and conf < anchor]
        if not candidates:
            candidates = [(idx, conf) for idx, conf in enumerate(confs) if conf is not None]
        candidates.sort(key=lambda x: x[1] if x[1] is not None else 1.0)
        target = max(int(math.ceil(len(candidates) * remask_fraction)), int(repair_cfg["min_remask_positions"]))
        target = min(len(candidates), target)
        if target <= 0:
            return []
        chosen = [idx for idx, _ in candidates[:target]]
        rng.shuffle(chosen)
        return sorted(chosen[:target])

    def repair_from_snapshot(
        self,
        item: dict[str, Any],
        snapshot_dict: dict[str, Any],
        repair_cfg: dict[str, Any],
        branch_index: int,
        base_seed: int,
        generation_cfg: dict[str, Any],
    ) -> dict[str, Any]:
        self.load()
        snapshot = Snapshot(**snapshot_dict)
        rng = np.random.default_rng(base_seed + branch_index)
        device = next(self.model.parameters()).device
        temperatures = repair_cfg["branch_temperatures"]
        remask_fractions = repair_cfg["branch_remask_fractions"]
        temperature = float(temperatures[branch_index % len(temperatures)])
        remask_fraction = float(remask_fractions[branch_index % len(remask_fractions)])

        x = torch.tensor(snapshot.full_token_ids, dtype=torch.long, device=device).unsqueeze(0)
        prompt_len = snapshot.prompt_len
        gen_length = int(generation_cfg["gen_length"])
        steps = int(generation_cfg["steps"])
        block_length = int(generation_cfg["block_length"])
        mask_id = int(generation_cfg["mask_id"])
        remasking = generation_cfg["remasking"]
        num_blocks = gen_length // block_length
        steps_per_block = steps // num_blocks

        remask_positions = self._repair_positions(snapshot, repair_cfg, remask_fraction, rng)
        for pos in remask_positions:
            x[0, prompt_len + pos] = mask_id

        for step_index in range(snapshot.step_index + 1, steps + 1):
            block_index = min((step_index - 1) // steps_per_block, num_blocks - 1)
            block_end = prompt_len + (block_index + 1) * block_length
            mask_index = x == mask_id
            if not bool(mask_index[:, prompt_len:].any().item()):
                break

            with torch.no_grad():
                logits = self.model(x).logits
                probs = F.softmax(logits.to(torch.float32), dim=-1)
                logits_with_noise = add_gumbel_noise(logits, temperature=temperature)
                x0 = torch.argmax(logits_with_noise, dim=-1)
                if remasking == "low_confidence":
                    x0_p = self._probs_for_tokens(probs, x0)
                elif remasking == "random":
                    x0_p = torch.rand((x0.shape[0], x0.shape[1]), device=x0.device)
                else:
                    raise NotImplementedError(remasking)

            x0 = torch.where(mask_index, x0, x)
            confidence = torch.where(mask_index, x0_p, torch.full_like(x0_p, float("-inf")))
            confidence[:, block_end:] = float("-inf")
            in_scope = mask_index[:, prompt_len:block_end].sum().item()
            if in_scope <= 0:
                continue
            remaining_steps = steps - step_index + 1
            k = max(1, int(math.ceil(in_scope / max(1, remaining_steps))))
            _, selected = torch.topk(confidence[0], k=k)
            transfer_index = torch.zeros_like(x, dtype=torch.bool)
            transfer_index[0, selected] = True
            x[transfer_index] = x0[transfer_index]

        while bool((x[:, prompt_len:] == mask_id).any().item()):
            with torch.no_grad():
                logits = self.model(x).logits
                probs = F.softmax(logits.to(torch.float32), dim=-1)
                x0 = torch.argmax(logits, dim=-1)
                x0 = torch.where(x == mask_id, x0, x)
                chosen_probs = self._probs_for_tokens(probs, x0)
            mask_index = x == mask_id
            confidence = torch.where(mask_index, chosen_probs, torch.full_like(chosen_probs, float("-inf")))
            remaining = int(mask_index[:, prompt_len:].sum().item())
            k = max(1, min(remaining, 8))
            _, selected = torch.topk(confidence[0], k=k)
            x[0, selected] = x0[0, selected]

        final_text = self._decode_text(x, prompt_len)
        final_answer = extract_boxed_answer(final_text)
        return {
            "branch_index": branch_index,
            "temperature": temperature,
            "remask_fraction": remask_fraction,
            "remasked_positions": remask_positions,
            "final_text": final_text,
            "final_answer": final_answer,
            "correct": answers_match(final_answer, item["answer"]),
        }
