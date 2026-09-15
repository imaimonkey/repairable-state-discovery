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

from repairable_diffusion.src.utils.math_eval import (
    answers_match,
    build_diffusion_math_prompt,
    extract_boxed_answer,
)
from repairable_diffusion.src.utils.seed import seed_everything


def _chunked_logsumexp(logits: torch.Tensor, *, chunk_size: int = 4096) -> torch.Tensor:
    """Float32 log-sum-exp over vocabulary without materializing full FP32 logits.

    Dream logits are normally bfloat16 on GPU.  The previous diagnostic path
    converted the complete ``[..., vocab]`` tensor to float32 before softmax,
    temporarily doubling the largest activation-sized tensor.  This streaming
    reduction preserves float32 accumulation while bounding the temporary
    allocation by ``chunk_size`` vocabulary columns.
    """
    if logits.ndim < 1 or logits.shape[-1] <= 0:
        raise ValueError("logits must have a non-empty vocabulary dimension")
    if chunk_size <= 0:
        raise ValueError("chunk_size must be positive")

    vocab = int(logits.shape[-1])
    flat = logits.reshape(-1, vocab)
    running_max = None
    running_sum = None
    for start in range(0, vocab, chunk_size):
        chunk = flat[:, start : start + chunk_size].to(torch.float32)
        chunk_max = chunk.max(dim=-1).values
        if running_max is None:
            running_max = chunk_max
            running_sum = torch.exp(chunk - running_max.unsqueeze(-1)).sum(dim=-1)
        else:
            new_max = torch.maximum(running_max, chunk_max)
            running_sum = (
                running_sum * torch.exp(running_max - new_max)
                + torch.exp(chunk - new_max.unsqueeze(-1)).sum(dim=-1)
            )
            running_max = new_max
    assert running_max is not None and running_sum is not None
    result = running_max + torch.log(running_sum.clamp_min(torch.finfo(torch.float32).tiny))
    return result.reshape(logits.shape[:-1])


def _chunked_token_probabilities(
    logits: torch.Tensor,
    token_ids: torch.Tensor,
    *,
    chunk_size: int = 4096,
) -> torch.Tensor:
    """Probability of one selected token per row with bounded temporary memory."""
    if tuple(logits.shape[:-1]) != tuple(token_ids.shape):
        raise ValueError("token_ids shape must match logits without the vocabulary dimension")
    chosen_logits = logits.gather(-1, token_ids.unsqueeze(-1)).squeeze(-1).to(torch.float32)
    log_norm = _chunked_logsumexp(logits, chunk_size=chunk_size)
    return torch.exp(chosen_logits - log_norm).clamp_(0.0, 1.0)


def _chunked_entropy_from_logits(logits: torch.Tensor, *, chunk_size: int = 4096) -> torch.Tensor:
    """Categorical entropy over vocabulary using a streaming softmax reduction."""
    if logits.ndim < 1 or logits.shape[-1] <= 0:
        raise ValueError("logits must have a non-empty vocabulary dimension")
    if chunk_size <= 0:
        raise ValueError("chunk_size must be positive")

    vocab = int(logits.shape[-1])
    flat = logits.reshape(-1, vocab)
    running_max = None
    running_sum = None
    running_weighted_logits = None
    for start in range(0, vocab, chunk_size):
        chunk = flat[:, start : start + chunk_size].to(torch.float32)
        chunk_max = chunk.max(dim=-1).values
        if running_max is None:
            running_max = chunk_max
            weights = torch.exp(chunk - running_max.unsqueeze(-1))
            running_sum = weights.sum(dim=-1)
            running_weighted_logits = (weights * chunk).sum(dim=-1)
        else:
            new_max = torch.maximum(running_max, chunk_max)
            old_scale = torch.exp(running_max - new_max)
            weights = torch.exp(chunk - new_max.unsqueeze(-1))
            running_sum = running_sum * old_scale + weights.sum(dim=-1)
            running_weighted_logits = (
                running_weighted_logits * old_scale + (weights * chunk).sum(dim=-1)
            )
            running_max = new_max
    assert running_max is not None
    assert running_sum is not None
    assert running_weighted_logits is not None
    safe_sum = running_sum.clamp_min(torch.finfo(torch.float32).tiny)
    log_norm = running_max + torch.log(safe_sum)
    expected_logit = running_weighted_logits / safe_sum
    entropy = (log_norm - expected_logit).clamp_min_(0.0)
    return entropy.reshape(logits.shape[:-1])


def _ensure_dream_on_path(playground_root: str | Path) -> Path:
    root = Path(os.environ.get("DIFFUSION_PLAYGROUND_ROOT", str(playground_root))).expanduser().resolve()
    dream_dir = root / "Dream"
    if not dream_dir.exists():
        raise FileNotFoundError(f"Dream directory not found under: {root}")
    for path in (dream_dir, root):
        path_str = str(path)
        if path_str not in sys.path:
            sys.path.insert(0, path_str)
    return root


@dataclass
class Snapshot:
    step_index: int
    total_steps: int
    prompt_len: int
    full_token_ids: list[int]
    token_confidences: list[float | None]


class DreamBackend:
    def __init__(self, cfg: dict[str, Any]):
        self.cfg = cfg
        self.root = _ensure_dream_on_path(cfg["playground_root"])
        from modeling_dream import DreamModel
        from generation_utils import sample_tokens

        self.model_cls = DreamModel
        self.sample_tokens = sample_tokens
        self.model = None
        self.tokenizer = None

    def load(self) -> None:
        if self.model is not None:
            return
        torch_dtype = getattr(torch, self.cfg.get("torch_dtype", "bfloat16"))
        model_path = self.cfg["model_path"]
        self.model = self.model_cls.from_pretrained(
            model_path,
            torch_dtype=torch_dtype,
            trust_remote_code=bool(self.cfg.get("trust_remote_code", True)),
        )
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
        return extract_boxed_answer(self._decode_text(token_ids, prompt_len))

    def _stats_vocab_chunk_size(self) -> int:
        return max(1, int(self.cfg.get("stats_vocab_chunk_size", 4096)))

    def _confidence_of_current_tokens(
        self,
        logits: torch.Tensor,
        x: torch.Tensor,
        active_mask: torch.Tensor,
    ) -> torch.Tensor:
        """Return float32 token probabilities only where diagnostics actually need them."""
        if active_mask.shape != x.shape:
            raise ValueError("active_mask must match token-id shape")
        result = torch.full(x.shape, float("nan"), device=x.device, dtype=torch.float32)
        if bool(active_mask.any().item()):
            selected_logits = logits[active_mask]
            selected_ids = x[active_mask]
            result[active_mask] = _chunked_token_probabilities(
                selected_logits,
                selected_ids,
                chunk_size=self._stats_vocab_chunk_size(),
            )
        return result

    @staticmethod
    def _optional_int(value: Any) -> int | None:
        if value is None:
            return None
        return int(value)

    def _generation_config_token_id(self, name: str) -> int | None:
        generation_config = getattr(self.model, "generation_config", None)
        return self._optional_int(getattr(generation_config, name, None))

    def _mask_token_id(self, generation_cfg: dict[str, Any]) -> int:
        token_id = self._generation_config_token_id("mask_token_id")
        if token_id is None:
            token_id = self._optional_int(generation_cfg.get("mask_id"))
        if token_id is None:
            token_id = self._optional_int(getattr(self.tokenizer, "mask_token_id", None))
        if token_id is None:
            raise ValueError("Dream mask token id unavailable; set generation.mask_id in the run config.")
        return token_id

    def _pad_token_id(self) -> int | None:
        token_id = self._generation_config_token_id("pad_token_id")
        if token_id is not None:
            return token_id
        token_id = self._optional_int(getattr(self.tokenizer, "pad_token_id", None))
        if token_id is not None:
            return token_id
        return self._optional_int(getattr(self.tokenizer, "eos_token_id", None))

    @torch.inference_mode()
    def generate_trajectory(self, item: dict[str, Any], trajectory_id: int, generation_cfg: dict[str, Any]) -> dict[str, Any]:
        question = item["question"]
        gold = item["answer"]
        seed = int(generation_cfg["base_seed"]) + trajectory_id + int(item["item_id"]) * 10000
        seed_everything(seed)
        prompt_text, prompt, prompt_ids = self._prompt_ids(question)

        steps = int(generation_cfg["steps"])
        gen_length = int(generation_cfg["gen_length"])
        checkpoint_stride = int(generation_cfg["checkpoint_stride"])
        temperature = float(generation_cfg["temperature"])
        top_p = float(self.cfg.get("top_p", 0.95))
        top_k = self.cfg.get("top_k")
        eos_penalty = float(self.cfg.get("eos_penalty", 0.0))

        mask_token_id = self._mask_token_id(generation_cfg)
        pad_token_id = self._pad_token_id()

        x = F.pad(prompt_ids, (0, gen_length), value=mask_token_id)
        prompt_len = prompt_ids.shape[1]
        is_prompt_mask = torch.zeros_like(x, dtype=torch.bool)
        is_prompt_mask[:, :prompt_len] = True
        first_conf = torch.full(x.shape, float("nan"), device=x.device, dtype=torch.float32)

        rows: list[dict[str, Any]] = []
        step_id = 0
        while bool((x == mask_token_id).any().item()) and step_id < steps:
            mask_index = x == mask_token_id
            logits = self.model(x, "full", None).logits
            logits = torch.cat([logits[:, :1], logits[:, :-1]], dim=1)

            mask_logits = logits[mask_index]
            if mask_logits.numel() > 0:
                mask_logits = mask_logits.clone()
                if pad_token_id is not None and pad_token_id < mask_logits.shape[-1]:
                    t = 1.0 - (step_id / max(1, steps))
                    mask_logits[:, pad_token_id] += eos_penalty * math.log(max(1e-6, 1 - t + 1e-3))
                confidence, x0, zero_temp_confidence = self.sample_tokens(
                    mask_logits,
                    temperature=temperature,
                    top_p=top_p,
                    top_k=top_k,
                )
                confidence = zero_temp_confidence
            else:
                confidence = torch.tensor([], device=x.device, dtype=torch.float32)
                x0 = torch.tensor([], device=x.device, dtype=torch.long)
            del mask_logits

            confidence_full = torch.full(x.shape, float("-inf"), device=x.device, dtype=torch.float32)
            candidate_tokens = torch.full(x.shape, mask_token_id, device=x.device, dtype=torch.long)
            if confidence.numel() > 0:
                # Dream inference returns bfloat16 confidence values while the
                # bookkeeping tensor is intentionally float32.  Indexed
                # assignment requires an exact dtype match on the supported
                # torch version, so cast only this bookkeeping value.
                confidence_full[mask_index] = confidence.to(confidence_full.dtype)
                candidate_tokens[mask_index] = x0

            selected_mask = torch.zeros_like(mask_index, dtype=torch.bool)
            new_positions = []
            new_conf = []
            for b in range(x.shape[0]):
                mask_pos = torch.where(mask_index[b] & ~is_prompt_mask[b])[0]
                prev_first = first_conf[b][~torch.isnan(first_conf[b])]
                threshold = float(prev_first.mean().item()) if prev_first.numel() > 0 else 1.0
                if mask_pos.numel() == 0:
                    continue
                confidences_b = confidence_full[b, mask_pos]
                sel_bool = confidences_b > threshold
                sel_indices = mask_pos[sel_bool]
                if sel_indices.numel() < 2:
                    k = min(2, mask_pos.numel())
                    _, topk_idx = torch.topk(confidences_b, k=k)
                    sel_indices = mask_pos[topk_idx]
                selected_mask[b, sel_indices] = True
                new_positions.extend((sel_indices - prompt_len).detach().cpu().tolist())
                new_conf.extend(confidence_full[b, sel_indices].detach().cpu().tolist())

            newly_unmasked = selected_mask & mask_index
            new_unmask_counts = newly_unmasked.sum(dim=1)
            if newly_unmasked.any():
                x[newly_unmasked] = candidate_tokens[newly_unmasked]
                need_record = torch.isnan(first_conf) & newly_unmasked
                if need_record.any():
                    first_conf[need_record] = confidence_full[need_record].to(dtype=first_conf.dtype)

            current_unmasked_mask = x != mask_token_id
            diagnostic_positions = current_unmasked_mask & ~is_prompt_mask
            current_token_probs = self._confidence_of_current_tokens(logits, x, diagnostic_positions)
            remask_mask = torch.zeros_like(current_unmasked_mask, dtype=torch.bool)
            for b in range(x.shape[0]):
                cur_unm_pos = torch.where(diagnostic_positions[b])[0]
                cur_unm_count = cur_unm_pos.numel()
                if cur_unm_count <= 1:
                    continue
                num_remask = int(max(1, min(cur_unm_count - 1, math.ceil(int(new_unmask_counts[b].item()) / 8))))
                cur_conf = current_token_probs[b, cur_unm_pos]
                _, smallest_idx = torch.topk(-cur_conf, k=num_remask)
                remask_positions = cur_unm_pos[smallest_idx]
                remask_mask[b, remask_positions] = True

            if remask_mask.any():
                x[remask_mask] = mask_token_id

            gen_mask = x[0, prompt_len:] == mask_token_id
            conf_values = current_token_probs[0, prompt_len:].detach().cpu().tolist()
            token_confidences: list[float | None] = [
                None if bool(gen_mask[pos].item()) else float(conf_values[pos]) for pos in range(gen_length)
            ]

            if bool(gen_mask.any().item()):
                masked_logits = logits[0, prompt_len:][gen_mask]
                entropy = _chunked_entropy_from_logits(
                    masked_logits,
                    chunk_size=self._stats_vocab_chunk_size(),
                )
                masked_entropy_mean = float(entropy.mean().item())
                masked_entropy_max = float(entropy.max().item())
                del masked_logits, entropy
            else:
                masked_entropy_mean = 0.0
                masked_entropy_max = 0.0

            provisional_answer = self._candidate_from_tokens(x, prompt_len)
            row = {
                "step_index": step_id + 1,
                "total_steps": steps,
                "block_index": None,
                "step_in_block": None,
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
            if (step_id + 1) % checkpoint_stride == 0 or not bool((x == mask_token_id).any().item()) or step_id + 1 == steps:
                row["snapshot"] = Snapshot(
                    step_index=step_id + 1,
                    total_steps=steps,
                    prompt_len=prompt_len,
                    full_token_ids=x[0].detach().cpu().tolist(),
                    token_confidences=token_confidences,
                ).__dict__
            rows.append(row)
            step_id += 1
            del logits, current_token_probs

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

    def _repair_positions(self, snapshot: Snapshot, repair_cfg: dict[str, Any], remask_fraction: float, rng: np.random.Generator) -> list[int]:
        confs = snapshot.token_confidences
        anchor = float(repair_cfg["anchor_confidence_threshold"])
        candidates = [(idx, conf) for idx, conf in enumerate(confs) if conf is not None and conf < anchor]
        if not candidates:
            candidates = [(idx, conf) for idx, conf in enumerate(confs) if conf is not None]
        candidates.sort(key=lambda x: x[1] if x[1] is not None else 1.0)
        target = max(int(math.ceil(len(candidates) * remask_fraction)), int(repair_cfg["min_remask_positions"]))
        target = min(len(candidates), target)
        chosen = [idx for idx, _ in candidates[:target]]
        rng.shuffle(chosen)
        return sorted(chosen[:target])

    @torch.inference_mode()
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
        top_p = float(self.cfg.get("top_p", 0.95))
        top_k = self.cfg.get("top_k")

        mask_token_id = self._mask_token_id(generation_cfg)
        x = torch.tensor(snapshot.full_token_ids, dtype=torch.long, device=device).unsqueeze(0)
        prompt_len = snapshot.prompt_len
        total_steps = int(generation_cfg["steps"])
        first_conf = torch.full(x.shape, float("nan"), device=device, dtype=torch.float32)
        for idx, conf in enumerate(snapshot.token_confidences):
            if conf is not None:
                first_conf[0, prompt_len + idx] = float(conf)

        remask_positions = self._repair_positions(snapshot, repair_cfg, remask_fraction, rng)
        for pos in remask_positions:
            x[0, prompt_len + pos] = mask_token_id
            first_conf[0, prompt_len + pos] = float("nan")

        is_prompt_mask = torch.zeros_like(x, dtype=torch.bool)
        is_prompt_mask[:, :prompt_len] = True

        step_id = snapshot.step_index
        while bool((x == mask_token_id).any().item()) and step_id < total_steps:
            mask_index = x == mask_token_id
            logits = self.model(x, "full", None).logits
            logits = torch.cat([logits[:, :1], logits[:, :-1]], dim=1)
            mask_logits = logits[mask_index]
            if mask_logits.numel() > 0:
                confidence, x0, zero_temp_confidence = self.sample_tokens(
                    mask_logits,
                    temperature=temperature,
                    top_p=top_p,
                    top_k=top_k,
                )
                confidence = zero_temp_confidence
            else:
                confidence = torch.tensor([], device=x.device, dtype=torch.float32)
                x0 = torch.tensor([], device=x.device, dtype=torch.long)
            del mask_logits

            confidence_full = torch.full(x.shape, float("-inf"), device=x.device, dtype=torch.float32)
            candidate_tokens = torch.full(x.shape, mask_token_id, device=x.device, dtype=torch.long)
            if confidence.numel() > 0:
                # Keep the confidence bookkeeping tensor in float32 even when
                # Dream returns bfloat16 probabilities from the model.
                confidence_full[mask_index] = confidence.to(confidence_full.dtype)
                candidate_tokens[mask_index] = x0

            selected_mask = torch.zeros_like(mask_index, dtype=torch.bool)
            for b in range(x.shape[0]):
                mask_pos = torch.where(mask_index[b] & ~is_prompt_mask[b])[0]
                if mask_pos.numel() == 0:
                    continue
                prev_first = first_conf[b][~torch.isnan(first_conf[b])]
                threshold = float(prev_first.mean().item()) if prev_first.numel() > 0 else 1.0
                confidences_b = confidence_full[b, mask_pos]
                sel_bool = confidences_b > threshold
                sel_indices = mask_pos[sel_bool]
                if sel_indices.numel() < 2:
                    k = min(2, mask_pos.numel())
                    _, topk_idx = torch.topk(confidences_b, k=k)
                    sel_indices = mask_pos[topk_idx]
                selected_mask[b, sel_indices] = True

            newly_unmasked = selected_mask & mask_index
            new_unmask_counts = newly_unmasked.sum(dim=1)
            if newly_unmasked.any():
                x[newly_unmasked] = candidate_tokens[newly_unmasked]
                need_record = torch.isnan(first_conf) & newly_unmasked
                if need_record.any():
                    first_conf[need_record] = confidence_full[need_record]

            current_unmasked_mask = x != mask_token_id
            diagnostic_positions = current_unmasked_mask & ~is_prompt_mask
            current_token_probs = self._confidence_of_current_tokens(logits, x, diagnostic_positions)
            remask_mask = torch.zeros_like(current_unmasked_mask, dtype=torch.bool)
            for b in range(x.shape[0]):
                cur_unm_pos = torch.where(diagnostic_positions[b])[0]
                cur_unm_count = cur_unm_pos.numel()
                if cur_unm_count <= 1:
                    continue
                num_remask = int(max(1, min(cur_unm_count - 1, math.ceil(int(new_unmask_counts[b].item()) / 8))))
                cur_conf = current_token_probs[b, cur_unm_pos]
                _, smallest_idx = torch.topk(-cur_conf, k=num_remask)
                remask_positions_step = cur_unm_pos[smallest_idx]
                remask_mask[b, remask_positions_step] = True
            if remask_mask.any():
                x[remask_mask] = mask_token_id
                first_conf[remask_mask] = float("nan")
            step_id += 1
            del logits, current_token_probs

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
