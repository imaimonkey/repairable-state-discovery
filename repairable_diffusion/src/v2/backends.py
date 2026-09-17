from __future__ import annotations

import math
from dataclasses import dataclass, asdict
from typing import Any

import numpy as np
import torch
import torch.nn.functional as F

from repairable_diffusion.src.backends.dream import DreamBackend
from repairable_diffusion.src.backends.rfba_llada import RFBALLADABackend, add_gumbel_noise, get_num_transfer_tokens
from repairable_diffusion.src.utils.seed import seed_everything
from repairable_diffusion.src.v2.task_adapters import TaskAdapter


V2_BACKEND_VERSION = "v2.2"
CORE_SOURCE_REPOSITORY = "UCF-CRCV/CoRe"
CORE_SOURCE_REVISION = "524e01e11a8751afb67b81a2c930f938faf9a70e"


def _rng_snapshot() -> dict[str, Any]:
    payload: dict[str, Any] = {"torch_cpu": torch.get_rng_state().cpu().tolist()}
    if torch.cuda.is_available():
        payload["torch_cuda"] = [state.cpu().tolist() for state in torch.cuda.get_rng_state_all()]
    else:
        payload["torch_cuda"] = []
    return payload


def _restore_rng(payload: dict[str, Any]) -> None:
    torch.set_rng_state(torch.tensor(payload["torch_cpu"], dtype=torch.uint8))
    cuda_states = payload.get("torch_cuda") or []
    if cuda_states and torch.cuda.is_available():
        torch.cuda.set_rng_state_all([torch.tensor(state, dtype=torch.uint8) for state in cuda_states])


@dataclass
class ComputeCounter:
    forward_calls: int = 0
    nfe: int = 0

    def add_forward(self, count: int = 1) -> None:
        self.forward_calls += int(count)
        self.nfe += int(count)

    def to_dict(self) -> dict[str, int]:
        return {"forward_calls": self.forward_calls, "nfe": self.nfe}


@dataclass
class V2Snapshot:
    backend_type: str
    schema_version: str
    step_index: int
    total_steps: int
    prompt_len: int
    full_token_ids: list[int]
    token_confidences: list[float | None]
    masked_ratio: float
    commitment_ratio: float
    block_index: int | None
    step_in_block: int | None
    active_plan: list[int] | None
    first_conf: list[float | None] | None
    rng_state: dict[str, Any]
    backend_state: dict[str, Any]

    def to_dict(self) -> dict[str, Any]:
        return asdict(self)


@dataclass
class InterventionResult:
    snapshot: dict[str, Any]
    operator_id: str
    applicable: bool
    modified_positions: list[int]
    metadata: dict[str, Any]
    compute: dict[str, int]


class V2BackendMixin:
    backend_type: str

    def __init_v2__(self, adapter: TaskAdapter) -> None:
        self.adapter = adapter

    def _adapter_prompt_ids(self, item: dict[str, Any]) -> tuple[str, str, torch.Tensor]:
        self.load()
        prompt_text, prompt = self.adapter.build_prompt(item, self.tokenizer)
        prompt_ids = self.tokenizer(prompt, return_tensors="pt").input_ids
        if torch.cuda.is_available() and next(self.model.parameters()).is_cuda:
            prompt_ids = prompt_ids.cuda()
        return prompt_text, prompt, prompt_ids

    def _adapter_prediction(self, token_ids: torch.Tensor, prompt_len: int) -> str | None:
        text = self.tokenizer.decode(token_ids[0, prompt_len:], skip_special_tokens=True)
        return self.adapter.extract_prediction(text)

    def _adapter_correct(self, prediction: str | None, item: dict[str, Any]) -> bool:
        return self.adapter.evaluate(prediction, item["answer"], item=item)


class V2LLADABackend(V2BackendMixin, RFBALLADABackend):
    backend_type = "rfba_llada_v2"

    def __init__(self, cfg: dict[str, Any], adapter: TaskAdapter):
        RFBALLADABackend.__init__(self, cfg)
        self.__init_v2__(adapter)

    def _forward(self, x: torch.Tensor, counter: ComputeCounter) -> torch.Tensor:
        counter.add_forward()
        return self.model(x).logits

    def generate_trajectory_v2(
        self, item: dict[str, Any], trajectory_id: int, generation_cfg: dict[str, Any]
    ) -> dict[str, Any]:
        seed = int(generation_cfg["base_seed"]) + int(trajectory_id) + int(item["item_id"]) * 10000
        seed_everything(seed)
        prompt_text, prompt, prompt_ids = self._adapter_prompt_ids(item)

        steps = int(generation_cfg["steps"])
        gen_length = int(generation_cfg["gen_length"])
        block_length = int(generation_cfg["block_length"])
        temperature = float(generation_cfg["temperature"])
        cfg_scale = float(generation_cfg.get("cfg_scale", 0.0))
        remasking = str(generation_cfg.get("remasking", "low_confidence"))
        mask_id = int(generation_cfg["mask_id"])
        checkpoint_stride = int(generation_cfg["checkpoint_stride"])
        if cfg_scale != 0.0:
            raise NotImplementedError("V2 LLaDA currently requires cfg_scale=0 for replay equivalence")
        if gen_length % block_length != 0:
            raise ValueError("gen_length must be divisible by block_length")
        num_blocks = gen_length // block_length
        if steps % num_blocks != 0:
            raise ValueError("steps must be divisible by num_blocks")
        steps_per_block = steps // num_blocks

        x = torch.full(
            (1, prompt_ids.shape[1] + gen_length), mask_id, dtype=torch.long, device=prompt_ids.device
        )
        x[:, : prompt_ids.shape[1]] = prompt_ids.clone()
        prompt_len = int(prompt_ids.shape[1])
        counter = ComputeCounter()
        rows: list[dict[str, Any]] = []
        active_plan: torch.Tensor | None = None

        for step_index in range(1, steps + 1):
            block_index = (step_index - 1) // steps_per_block
            local_step = (step_index - 1) % steps_per_block
            block_start = prompt_len + block_index * block_length
            block_end = prompt_len + (block_index + 1) * block_length
            mask_index = x == mask_id
            if local_step == 0:
                active_plan = get_num_transfer_tokens(mask_index[:, block_start:block_end], steps_per_block)
            assert active_plan is not None

            with torch.no_grad():
                logits = self._forward(x, counter)
                probs = F.softmax(logits.to(torch.float32), dim=-1)
                x0 = torch.argmax(add_gumbel_noise(logits, temperature), dim=-1)
                if remasking == "low_confidence":
                    x0_p = self._probs_for_tokens(probs, x0)
                elif remasking == "random":
                    x0_p = torch.rand((x0.shape[0], x0.shape[1]), device=x0.device)
                else:
                    raise NotImplementedError(remasking)

            x0[:, block_end:] = mask_id
            x0 = torch.where(mask_index, x0, x)
            confidence = torch.where(mask_index, x0_p, torch.full_like(x0_p, float("-inf")))
            confidence[:, :prompt_len] = float("-inf")
            confidence[:, block_end:] = float("-inf")
            k = int(active_plan[0, local_step].item())
            transfer_index = torch.zeros_like(x, dtype=torch.bool)
            if k > 0:
                finite = torch.isfinite(confidence[0])
                k = min(k, int(finite.sum().item()))
                if k > 0:
                    _, selected = torch.topk(confidence[0], k=k)
                    transfer_index[0, selected] = True
            next_x = x.clone()
            next_x[transfer_index] = x0[transfer_index]

            gen_mask = next_x[0, prompt_len:] == mask_id
            chosen_probs = self._probs_for_tokens(probs[:, prompt_len:, :], next_x[:, prompt_len:])
            conf_values = chosen_probs[0].detach().cpu().tolist()
            token_confidences = [
                None if bool(gen_mask[pos].item()) else float(conf_values[pos]) for pos in range(gen_length)
            ]
            masked_probs = probs[0, prompt_len:][gen_mask]
            if masked_probs.numel() > 0:
                entropy = -(masked_probs * torch.log(masked_probs.clamp(min=1e-12))).sum(dim=-1)
                entropy_mean = float(entropy.mean().item())
                entropy_max = float(entropy.max().item())
            else:
                entropy_mean = entropy_max = 0.0
            provisional = self._adapter_prediction(next_x, prompt_len)
            row: dict[str, Any] = {
                "step_index": step_index,
                "total_steps": steps,
                "normalized_step": step_index / steps,
                "block_index": block_index,
                "step_in_block": local_step + 1,
                "masked_ratio": float(gen_mask.float().mean().item()),
                "commitment_ratio": float((~gen_mask).float().mean().item()),
                "state_token_conf_mean": float(np.mean([v for v in token_confidences if v is not None])) if any(v is not None for v in token_confidences) else 0.0,
                "state_token_conf_min": float(np.min([v for v in token_confidences if v is not None])) if any(v is not None for v in token_confidences) else 0.0,
                "masked_entropy_mean": entropy_mean,
                "masked_entropy_max": entropy_max,
                "answer_candidate": provisional,
                "observed_correct": self._adapter_correct(provisional, item) if provisional is not None else False,
                "snapshot": None,
            }
            if step_index % checkpoint_stride == 0 or step_index == steps:
                row["snapshot"] = V2Snapshot(
                    backend_type=self.backend_type,
                    schema_version=V2_BACKEND_VERSION,
                    step_index=step_index,
                    total_steps=steps,
                    prompt_len=prompt_len,
                    full_token_ids=next_x[0].detach().cpu().tolist(),
                    token_confidences=token_confidences,
                    masked_ratio=row["masked_ratio"],
                    commitment_ratio=row["commitment_ratio"],
                    block_index=block_index,
                    step_in_block=local_step + 1,
                    active_plan=active_plan[0].detach().cpu().tolist(),
                    first_conf=None,
                    rng_state=_rng_snapshot(),
                    backend_state={"steps_per_block": steps_per_block, "block_length": block_length},
                ).to_dict()
            rows.append(row)
            x = next_x

        if bool((x[:, prompt_len:] == mask_id).any().item()):
            raise RuntimeError("V2 LLaDA base generation ended with masked tokens")
        final_text = self.tokenizer.decode(x[0, prompt_len:], skip_special_tokens=True)
        final_answer = self.adapter.extract_prediction(final_text)
        return {
            "item_id": int(item["item_id"]),
            "trajectory_id": int(trajectory_id),
            "seed": seed,
            "question": item["question"],
            "gold_answer": item["answer"],
            "prompt_text": prompt_text,
            "prompt": prompt,
            "final_text": final_text,
            "final_answer": final_answer,
            "correct": self._adapter_correct(final_answer, item),
            "steps": rows,
            "compute": counter.to_dict(),
            "backend_version": V2_BACKEND_VERSION,
        }

    def _active_bounds(self, snapshot: dict[str, Any], generation_cfg: dict[str, Any]) -> tuple[int, int, int, int]:
        prompt_len = int(snapshot["prompt_len"])
        block_length = int(generation_cfg["block_length"])
        steps = int(generation_cfg["steps"])
        gen_length = int(generation_cfg["gen_length"])
        num_blocks = gen_length // block_length
        steps_per_block = steps // num_blocks
        block_index = int(snapshot["block_index"])
        start = prompt_len + block_index * block_length
        end = prompt_len + (block_index + 1) * block_length
        return start, end, steps_per_block, block_index

    def canonical_remask_positions(self, snapshot: dict[str, Any], operator_cfg: dict[str, Any], generation_cfg: dict[str, Any]) -> list[int]:
        start, end, steps_per_block, _ = self._active_bounds(snapshot, generation_cfg)
        if int(snapshot["step_in_block"]) >= steps_per_block:
            return []
        prompt_len = int(snapshot["prompt_len"])
        confs = list(snapshot["token_confidences"])
        anchor = float(operator_cfg.get("anchor_confidence_threshold", 0.80))
        eligible: list[tuple[int, float]] = []
        for absolute in range(start, end):
            rel = absolute - prompt_len
            conf = confs[rel]
            if conf is not None:
                eligible.append((rel, float(conf)))
        if not eligible:
            return []
        low = [row for row in eligible if row[1] < anchor] or eligible
        low.sort(key=lambda row: row[1])
        fraction = float(operator_cfg["remask_fraction"])
        target = max(int(math.ceil(len(low) * fraction)), int(operator_cfg["min_remask_positions"]))
        target = min(target, len(low))
        return sorted(rel for rel, _ in low[:target])

    def intervene_snapshot(
        self,
        snapshot: dict[str, Any],
        *,
        operator_id: str,
        operator_cfg: dict[str, Any],
        generation_cfg: dict[str, Any],
        branch_seed: int,
        paired_modified_count: int | None = None,
    ) -> InterventionResult:
        self.load()
        snap = dict(snapshot)
        snap["full_token_ids"] = list(snapshot["full_token_ids"])
        snap["token_confidences"] = list(snapshot["token_confidences"])
        counter = ComputeCounter()
        prompt_len = int(snap["prompt_len"])
        mask_id = int(generation_cfg["mask_id"])
        start, end, steps_per_block, _ = self._active_bounds(snap, generation_cfg)
        if int(snap["step_in_block"]) >= steps_per_block:
            return InterventionResult(snap, operator_id, False, [], {"reason": "block_boundary"}, counter.to_dict())

        targeted = self.canonical_remask_positions(snap, operator_cfg, generation_cfg)
        positions: list[int]
        metadata: dict[str, Any] = {}
        if operator_id == "low_confidence_remask_v2":
            positions = targeted
        elif operator_id == "random_position_remask":
            count = int(paired_modified_count if paired_modified_count is not None else len(targeted))
            committed = []
            for absolute in range(start, end):
                rel = absolute - prompt_len
                if snap["token_confidences"][rel] is not None:
                    committed.append(rel)
            if count <= 0 or not committed:
                positions = []
            else:
                rng = np.random.default_rng(int(branch_seed))
                count = min(count, len(committed))
                positions = sorted(int(x) for x in rng.choice(committed, size=count, replace=False).tolist())
        elif operator_id == "core":
            device = next(self.model.parameters()).device
            x = torch.tensor(snap["full_token_ids"], dtype=torch.long, device=device).unsqueeze(0)
            with torch.no_grad():
                logits = self._forward(x, counter)
                probs = F.softmax(logits.to(torch.float32), dim=-1)
            committed_abs = [a for a in range(start, end) if int(x[0, a].item()) != mask_id]
            if not committed_abs:
                positions = []
            else:
                top2, _ = probs[0, committed_abs].topk(2, dim=-1)
                margins = top2[:, 0] - top2[:, 1]
                candidate_m = min(int(operator_cfg.get("core_candidate_m", 32)), len(committed_abs))
                _, idx = torch.topk(-margins, k=candidate_m)
                verify_abs = [committed_abs[int(i)] for i in idx.detach().cpu().tolist()]
                x_ver = x.clone()
                x_ver[0, verify_abs] = mask_id
                with torch.no_grad():
                    logits_ver = self._forward(x_ver, counter)
                    p_ver = F.softmax(logits_ver.to(torch.float32), dim=-1)
                old_tokens = x[0, verify_abs]
                tok_prob = p_ver[0, verify_abs].gather(-1, old_tokens.unsqueeze(-1)).squeeze(-1)
                pll = torch.log(tok_prob + 1e-10)
                replacement = torch.argmax(logits_ver[0, verify_abs], dim=-1)
                replacement_prob = p_ver[0, verify_abs].gather(-1, replacement.unsqueeze(-1)).squeeze(-1)
                valid = (replacement != old_tokens) & (replacement_prob >= float(operator_cfg.get("core_replacement_confidence", 0.30)))
                valid_indices = torch.where(valid)[0]
                desired = int(paired_modified_count if paired_modified_count is not None else len(targeted))
                desired = max(0, desired)
                if valid_indices.numel() == 0 or desired == 0:
                    positions = []
                else:
                    scores = -pll[valid_indices]
                    k = min(desired, int(valid_indices.numel()))
                    _, chosen_local = torch.topk(scores, k=k)
                    selected_verify = valid_indices[chosen_local]
                    positions = sorted(verify_abs[int(i)] - prompt_len for i in selected_verify.detach().cpu().tolist())
                metadata.update(
                    {
                        "core_source_repository": CORE_SOURCE_REPOSITORY,
                        "core_source_revision": CORE_SOURCE_REVISION,
                        "core_candidate_m": candidate_m,
                        "core_verified": len(verify_abs),
                        "label": "CoRe-snapshot",
                    }
                )
        else:
            raise ValueError(f"unsupported V2 intervention: {operator_id}")

        if not positions:
            return InterventionResult(snap, operator_id, False, [], {**metadata, "reason": "no_eligible_positions"}, counter.to_dict())
        for rel in positions:
            snap["full_token_ids"][prompt_len + int(rel)] = mask_id
            snap["token_confidences"][int(rel)] = None
        snap.setdefault("backend_state", {})
        snap["backend_state"] = dict(snap["backend_state"])
        snap["backend_state"]["recompute_active_plan"] = True
        metadata["paired_target_count"] = len(targeted)
        return InterventionResult(snap, operator_id, True, positions, metadata, counter.to_dict())

    def continue_from_snapshot(
        self,
        item: dict[str, Any],
        snapshot: dict[str, Any],
        generation_cfg: dict[str, Any],
        *,
        branch_seed: int | None,
        restore_native_rng: bool = False,
    ) -> dict[str, Any]:
        self.load()
        if restore_native_rng:
            _restore_rng(snapshot["rng_state"])
        elif branch_seed is not None:
            seed_everything(int(branch_seed))
        else:
            raise ValueError("continuation requires branch_seed or restore_native_rng=True")

        device = next(self.model.parameters()).device
        x = torch.tensor(snapshot["full_token_ids"], dtype=torch.long, device=device).unsqueeze(0)
        prompt_len = int(snapshot["prompt_len"])
        steps = int(generation_cfg["steps"])
        gen_length = int(generation_cfg["gen_length"])
        block_length = int(generation_cfg["block_length"])
        temperature = float(generation_cfg["temperature"])
        mask_id = int(generation_cfg["mask_id"])
        remasking = str(generation_cfg.get("remasking", "low_confidence"))
        num_blocks = gen_length // block_length
        steps_per_block = steps // num_blocks
        counter = ComputeCounter()

        current_plan = list(snapshot.get("active_plan") or [])
        snapshot_block = int(snapshot["block_index"])
        recompute_active = bool(snapshot.get("backend_state", {}).get("recompute_active_plan", False))
        start_step = int(snapshot["step_index"]) + 1
        recomputed_plan: list[int] | None = None
        recompute_start_local: int | None = None

        if recompute_active and start_step <= steps:
            block_index = (start_step - 1) // steps_per_block
            if block_index == snapshot_block:
                local_completed = int(snapshot["step_in_block"])
                remaining_local = steps_per_block - local_completed
                if remaining_local > 0:
                    block_start = prompt_len + block_index * block_length
                    block_end = prompt_len + (block_index + 1) * block_length
                    plan_tensor = get_num_transfer_tokens(x[:, block_start:block_end] == mask_id, remaining_local)
                    recomputed_plan = plan_tensor[0].detach().cpu().tolist()
                    recompute_start_local = local_completed

        for step_index in range(start_step, steps + 1):
            block_index = (step_index - 1) // steps_per_block
            local_step = (step_index - 1) % steps_per_block
            block_start = prompt_len + block_index * block_length
            block_end = prompt_len + (block_index + 1) * block_length
            mask_index = x == mask_id
            if not bool(mask_index[:, prompt_len:].any().item()):
                break
            if local_step == 0:
                plan_tensor = get_num_transfer_tokens(mask_index[:, block_start:block_end], steps_per_block)
                current_plan = plan_tensor[0].detach().cpu().tolist()
                recomputed_plan = None
                recompute_start_local = None

            with torch.no_grad():
                logits = self._forward(x, counter)
                probs = F.softmax(logits.to(torch.float32), dim=-1)
                x0 = torch.argmax(add_gumbel_noise(logits, temperature), dim=-1)
                if remasking == "low_confidence":
                    x0_p = self._probs_for_tokens(probs, x0)
                elif remasking == "random":
                    x0_p = torch.rand((x0.shape[0], x0.shape[1]), device=x0.device)
                else:
                    raise NotImplementedError(remasking)
            x0[:, block_end:] = mask_id
            x0 = torch.where(mask_index, x0, x)
            confidence = torch.where(mask_index, x0_p, torch.full_like(x0_p, float("-inf")))
            confidence[:, :prompt_len] = float("-inf")
            confidence[:, block_end:] = float("-inf")

            if recomputed_plan is not None and recompute_start_local is not None and block_index == snapshot_block:
                idx = local_step - recompute_start_local
                k = int(recomputed_plan[idx]) if 0 <= idx < len(recomputed_plan) else 0
            else:
                k = int(current_plan[local_step]) if local_step < len(current_plan) else 0
            finite = torch.isfinite(confidence[0])
            k = min(k, int(finite.sum().item()))
            if k > 0:
                _, selected = torch.topk(confidence[0], k=k)
                x[0, selected] = x0[0, selected]

        remaining = int((x[:, prompt_len:] == mask_id).sum().item())
        if remaining:
            raise RuntimeError(
                f"V2 LLaDA continuation exhausted fixed schedule with {remaining} masks; refusing extra post-hoc steps"
            )
        final_text = self.tokenizer.decode(x[0, prompt_len:], skip_special_tokens=True)
        prediction = self.adapter.extract_prediction(final_text)
        return {
            "final_text": final_text,
            "final_answer": prediction,
            "correct": self._adapter_correct(prediction, item),
            "compute": counter.to_dict(),
        }

    def run_operator_branch(
        self,
        item: dict[str, Any],
        snapshot: dict[str, Any],
        generation_cfg: dict[str, Any],
        operator_cfg: dict[str, Any],
        *,
        operator_id: str,
        branch_seed: int,
        paired_modified_count: int | None = None,
    ) -> dict[str, Any]:
        if operator_id == "native_continuation":
            result = self.continue_from_snapshot(
                item, snapshot, generation_cfg, branch_seed=None, restore_native_rng=True
            )
            return {**result, "operator_id": operator_id, "modified_positions": [], "intervention_compute": {"nfe": 0, "forward_calls": 0}}
        if operator_id == "matched_stochastic_continuation":
            result = self.continue_from_snapshot(
                item, snapshot, generation_cfg, branch_seed=branch_seed, restore_native_rng=False
            )
            return {**result, "operator_id": operator_id, "modified_positions": [], "intervention_compute": {"nfe": 0, "forward_calls": 0}}
        intervention = self.intervene_snapshot(
            snapshot,
            operator_id=operator_id,
            operator_cfg=operator_cfg,
            generation_cfg=generation_cfg,
            branch_seed=branch_seed,
            paired_modified_count=paired_modified_count,
        )
        if not intervention.applicable:
            return {
                "operator_id": operator_id,
                "applicable": False,
                "correct": None,
                "final_answer": None,
                "modified_positions": [],
                "metadata": intervention.metadata,
                "compute": intervention.compute,
                "intervention_compute": intervention.compute,
            }
        result = self.continue_from_snapshot(
            item, intervention.snapshot, generation_cfg, branch_seed=branch_seed, restore_native_rng=False
        )
        compute = {
            "nfe": int(result["compute"]["nfe"]) + int(intervention.compute["nfe"]),
            "forward_calls": int(result["compute"]["forward_calls"]) + int(intervention.compute["forward_calls"]),
        }
        return {
            **result,
            "operator_id": operator_id,
            "applicable": True,
            "modified_positions": intervention.modified_positions,
            "metadata": intervention.metadata,
            "compute": compute,
            "intervention_compute": intervention.compute,
        }


class V2DreamBackend(V2BackendMixin, DreamBackend):
    backend_type = "dream_v2"

    def __init__(self, cfg: dict[str, Any], adapter: TaskAdapter):
        DreamBackend.__init__(self, cfg)
        self.__init_v2__(adapter)

    def _forward(self, x: torch.Tensor, counter: ComputeCounter) -> torch.Tensor:
        counter.add_forward()
        logits = self.model(x, "full", None).logits
        return torch.cat([logits[:, :1], logits[:, :-1]], dim=1)

    @staticmethod
    def _first_conf_to_list(first_conf: torch.Tensor) -> list[float | None]:
        values = first_conf[0].detach().cpu().tolist()
        return [None if math.isnan(float(v)) else float(v) for v in values]

    @staticmethod
    def _first_conf_from_list(values: list[float | None], device: torch.device) -> torch.Tensor:
        return torch.tensor(
            [[float("nan") if v is None else float(v) for v in values]], dtype=torch.float32, device=device
        )

    def _dream_step(
        self,
        x: torch.Tensor,
        first_conf: torch.Tensor,
        is_prompt_mask: torch.Tensor,
        *,
        step_id: int,
        total_steps: int,
        generation_cfg: dict[str, Any],
        counter: ComputeCounter,
    ) -> tuple[torch.Tensor, torch.Tensor, torch.Tensor, list[int], list[float]]:
        mask_token_id = self._mask_token_id(generation_cfg)
        pad_token_id = self._pad_token_id()
        temperature = float(generation_cfg["temperature"])
        top_p = float(self.cfg.get("top_p", 0.95))
        top_k = self.cfg.get("top_k")
        eos_penalty = float(self.cfg.get("eos_penalty", 0.0))
        mask_index = x == mask_token_id
        logits = self._forward(x, counter)
        mask_logits = logits[mask_index]
        if mask_logits.numel() > 0:
            mask_logits = mask_logits.clone()
            if pad_token_id is not None and pad_token_id < mask_logits.shape[-1]:
                t = 1.0 - (step_id / max(1, total_steps))
                mask_logits[:, pad_token_id] += eos_penalty * math.log(max(1e-6, 1 - t + 1e-3))
            _, x0, zero_temp_confidence = self.sample_tokens(
                mask_logits, temperature=temperature, top_p=top_p, top_k=top_k
            )
            confidence = zero_temp_confidence
        else:
            confidence = torch.tensor([], device=x.device, dtype=torch.float32)
            x0 = torch.tensor([], device=x.device, dtype=torch.long)

        confidence_full = torch.full(x.shape, float("-inf"), device=x.device, dtype=torch.float32)
        candidate_tokens = torch.full(x.shape, mask_token_id, device=x.device, dtype=torch.long)
        if confidence.numel() > 0:
            confidence_full[mask_index] = confidence
            candidate_tokens[mask_index] = x0
        selected_mask = torch.zeros_like(mask_index, dtype=torch.bool)
        new_positions: list[int] = []
        new_conf: list[float] = []
        prompt_len = int(is_prompt_mask.sum().item())
        for b in range(x.shape[0]):
            mask_pos = torch.where(mask_index[b] & ~is_prompt_mask[b])[0]
            prev_first = first_conf[b][~torch.isnan(first_conf[b])]
            threshold = float(prev_first.mean().item()) if prev_first.numel() > 0 else 1.0
            if mask_pos.numel() == 0:
                continue
            confidences_b = confidence_full[b, mask_pos]
            sel_indices = mask_pos[confidences_b > threshold]
            if sel_indices.numel() < 2:
                k = min(2, int(mask_pos.numel()))
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
            first_conf[need_record] = confidence_full[need_record].to(dtype=first_conf.dtype)

        current_unmasked = x != mask_token_id
        current_token_probs = self._confidence_of_current_tokens(logits, x)
        remask_mask = torch.zeros_like(current_unmasked, dtype=torch.bool)
        for b in range(x.shape[0]):
            positions = torch.where(current_unmasked[b] & ~is_prompt_mask[b])[0]
            count = int(positions.numel())
            if count <= 1:
                continue
            num_remask = int(max(1, min(count - 1, math.ceil(int(new_unmask_counts[b].item()) / 8))))
            cur_conf = current_token_probs[b, positions]
            _, smallest_idx = torch.topk(-cur_conf, k=num_remask)
            remask_mask[b, positions[smallest_idx]] = True
        if remask_mask.any():
            x[remask_mask] = mask_token_id
        return x, first_conf, logits, new_positions, new_conf

    def generate_trajectory_v2(
        self, item: dict[str, Any], trajectory_id: int, generation_cfg: dict[str, Any]
    ) -> dict[str, Any]:
        seed = int(generation_cfg["base_seed"]) + int(trajectory_id) + int(item["item_id"]) * 10000
        seed_everything(seed)
        prompt_text, prompt, prompt_ids = self._adapter_prompt_ids(item)
        steps = int(generation_cfg["steps"])
        gen_length = int(generation_cfg["gen_length"])
        checkpoint_stride = int(generation_cfg["checkpoint_stride"])
        mask_id = self._mask_token_id(generation_cfg)
        x = F.pad(prompt_ids, (0, gen_length), value=mask_id)
        prompt_len = int(prompt_ids.shape[1])
        is_prompt_mask = torch.zeros_like(x, dtype=torch.bool)
        is_prompt_mask[:, :prompt_len] = True
        first_conf = torch.full(x.shape, float("nan"), device=x.device, dtype=torch.float32)
        counter = ComputeCounter()
        rows: list[dict[str, Any]] = []

        step_id = 0
        while bool((x == mask_id).any().item()) and step_id < steps:
            x, first_conf, logits, new_positions, new_conf = self._dream_step(
                x, first_conf, is_prompt_mask, step_id=step_id, total_steps=steps, generation_cfg=generation_cfg, counter=counter
            )
            gen_mask = x[0, prompt_len:] == mask_id
            current_probs = self._confidence_of_current_tokens(logits, x)[0, prompt_len:].detach().cpu().tolist()
            token_confidences = [
                None if bool(gen_mask[pos].item()) else float(current_probs[pos]) for pos in range(gen_length)
            ]
            if bool(gen_mask.any().item()):
                masked_probs = F.softmax(logits[0, prompt_len:][gen_mask].to(torch.float32), dim=-1)
                entropy = -(masked_probs * torch.log(masked_probs.clamp(min=1e-12))).sum(dim=-1)
                entropy_mean, entropy_max = float(entropy.mean().item()), float(entropy.max().item())
            else:
                entropy_mean = entropy_max = 0.0
            provisional = self._adapter_prediction(x, prompt_len)
            row: dict[str, Any] = {
                "step_index": step_id + 1,
                "total_steps": steps,
                "normalized_step": (step_id + 1) / steps,
                "block_index": None,
                "step_in_block": None,
                "masked_ratio": float(gen_mask.float().mean().item()),
                "commitment_ratio": float((~gen_mask).float().mean().item()),
                "state_token_conf_mean": float(np.mean([v for v in token_confidences if v is not None])) if any(v is not None for v in token_confidences) else 0.0,
                "state_token_conf_min": float(np.min([v for v in token_confidences if v is not None])) if any(v is not None for v in token_confidences) else 0.0,
                "masked_entropy_mean": entropy_mean,
                "masked_entropy_max": entropy_max,
                "answer_candidate": provisional,
                "observed_correct": self._adapter_correct(provisional, item) if provisional is not None else False,
                "snapshot": None,
            }
            if (step_id + 1) % checkpoint_stride == 0 or not bool((x == mask_id).any().item()) or step_id + 1 == steps:
                row["snapshot"] = V2Snapshot(
                    backend_type=self.backend_type,
                    schema_version=V2_BACKEND_VERSION,
                    step_index=step_id + 1,
                    total_steps=steps,
                    prompt_len=prompt_len,
                    full_token_ids=x[0].detach().cpu().tolist(),
                    token_confidences=token_confidences,
                    masked_ratio=row["masked_ratio"],
                    commitment_ratio=row["commitment_ratio"],
                    block_index=None,
                    step_in_block=None,
                    active_plan=None,
                    first_conf=self._first_conf_to_list(first_conf),
                    rng_state=_rng_snapshot(),
                    backend_state={},
                ).to_dict()
            rows.append(row)
            step_id += 1

        if bool((x[:, prompt_len:] == mask_id).any().item()):
            raise RuntimeError("V2 Dream base generation exhausted fixed step budget with masks remaining")
        final_text = self.tokenizer.decode(x[0, prompt_len:], skip_special_tokens=True)
        prediction = self.adapter.extract_prediction(final_text)
        return {
            "item_id": int(item["item_id"]),
            "trajectory_id": int(trajectory_id),
            "seed": seed,
            "question": item["question"],
            "gold_answer": item["answer"],
            "prompt_text": prompt_text,
            "prompt": prompt,
            "final_text": final_text,
            "final_answer": prediction,
            "correct": self._adapter_correct(prediction, item),
            "steps": rows,
            "compute": counter.to_dict(),
            "backend_version": V2_BACKEND_VERSION,
        }

    def canonical_remask_positions(self, snapshot: dict[str, Any], operator_cfg: dict[str, Any], generation_cfg: dict[str, Any]) -> list[int]:
        confs = list(snapshot["token_confidences"])
        eligible = [(idx, float(conf)) for idx, conf in enumerate(confs) if conf is not None]
        if not eligible:
            return []
        anchor = float(operator_cfg.get("anchor_confidence_threshold", 0.80))
        low = [row for row in eligible if row[1] < anchor] or eligible
        low.sort(key=lambda row: row[1])
        target = max(int(math.ceil(len(low) * float(operator_cfg["remask_fraction"]))), int(operator_cfg["min_remask_positions"]))
        target = min(target, len(low))
        return sorted(idx for idx, _ in low[:target])

    def intervene_snapshot(
        self,
        snapshot: dict[str, Any],
        *,
        operator_id: str,
        operator_cfg: dict[str, Any],
        generation_cfg: dict[str, Any],
        branch_seed: int,
        paired_modified_count: int | None = None,
    ) -> InterventionResult:
        if operator_id == "core":
            raise ValueError("CoRe-snapshot is a Tier-B LLaDA-only control in the frozen contract")
        snap = dict(snapshot)
        snap["full_token_ids"] = list(snapshot["full_token_ids"])
        snap["token_confidences"] = list(snapshot["token_confidences"])
        snap["first_conf"] = list(snapshot.get("first_conf") or [])
        targeted = self.canonical_remask_positions(snap, operator_cfg, generation_cfg)
        if operator_id == "low_confidence_remask_v2":
            positions = targeted
        elif operator_id == "random_position_remask":
            count = int(paired_modified_count if paired_modified_count is not None else len(targeted))
            eligible = [idx for idx, conf in enumerate(snap["token_confidences"]) if conf is not None]
            if count <= 0 or not eligible:
                positions = []
            else:
                rng = np.random.default_rng(int(branch_seed))
                positions = sorted(int(x) for x in rng.choice(eligible, size=min(count, len(eligible)), replace=False).tolist())
        else:
            raise ValueError(f"unsupported Dream intervention: {operator_id}")
        if not positions:
            return InterventionResult(snap, operator_id, False, [], {"reason": "no_eligible_positions"}, {"nfe": 0, "forward_calls": 0})
        prompt_len = int(snap["prompt_len"])
        mask_id = self._mask_token_id(generation_cfg)
        for rel in positions:
            snap["full_token_ids"][prompt_len + rel] = mask_id
            snap["token_confidences"][rel] = None
            if snap["first_conf"]:
                snap["first_conf"][prompt_len + rel] = None
        return InterventionResult(
            snap, operator_id, True, positions, {"paired_target_count": len(targeted)}, {"nfe": 0, "forward_calls": 0}
        )

    def continue_from_snapshot(
        self,
        item: dict[str, Any],
        snapshot: dict[str, Any],
        generation_cfg: dict[str, Any],
        *,
        branch_seed: int | None,
        restore_native_rng: bool = False,
    ) -> dict[str, Any]:
        self.load()
        if restore_native_rng:
            _restore_rng(snapshot["rng_state"])
        elif branch_seed is not None:
            seed_everything(int(branch_seed))
        else:
            raise ValueError("continuation requires branch_seed or restore_native_rng=True")
        device = next(self.model.parameters()).device
        x = torch.tensor(snapshot["full_token_ids"], dtype=torch.long, device=device).unsqueeze(0)
        prompt_len = int(snapshot["prompt_len"])
        first_conf = self._first_conf_from_list(list(snapshot["first_conf"]), device)
        is_prompt_mask = torch.zeros_like(x, dtype=torch.bool)
        is_prompt_mask[:, :prompt_len] = True
        total_steps = int(generation_cfg["steps"])
        mask_id = self._mask_token_id(generation_cfg)
        counter = ComputeCounter()
        step_id = int(snapshot["step_index"])
        while bool((x == mask_id).any().item()) and step_id < total_steps:
            x, first_conf, _, _, _ = self._dream_step(
                x, first_conf, is_prompt_mask, step_id=step_id, total_steps=total_steps, generation_cfg=generation_cfg, counter=counter
            )
            step_id += 1
        remaining = int((x[:, prompt_len:] == mask_id).sum().item())
        if remaining:
            raise RuntimeError(
                f"V2 Dream continuation exhausted fixed schedule with {remaining} masks; refusing extra steps"
            )
        final_text = self.tokenizer.decode(x[0, prompt_len:], skip_special_tokens=True)
        prediction = self.adapter.extract_prediction(final_text)
        return {
            "final_text": final_text,
            "final_answer": prediction,
            "correct": self._adapter_correct(prediction, item),
            "compute": counter.to_dict(),
        }

    def run_operator_branch(
        self,
        item: dict[str, Any],
        snapshot: dict[str, Any],
        generation_cfg: dict[str, Any],
        operator_cfg: dict[str, Any],
        *,
        operator_id: str,
        branch_seed: int,
        paired_modified_count: int | None = None,
    ) -> dict[str, Any]:
        if operator_id == "native_continuation":
            result = self.continue_from_snapshot(item, snapshot, generation_cfg, branch_seed=None, restore_native_rng=True)
            return {**result, "operator_id": operator_id, "modified_positions": [], "intervention_compute": {"nfe": 0, "forward_calls": 0}}
        if operator_id == "matched_stochastic_continuation":
            result = self.continue_from_snapshot(item, snapshot, generation_cfg, branch_seed=branch_seed, restore_native_rng=False)
            return {**result, "operator_id": operator_id, "modified_positions": [], "intervention_compute": {"nfe": 0, "forward_calls": 0}}
        intervention = self.intervene_snapshot(
            snapshot,
            operator_id=operator_id,
            operator_cfg=operator_cfg,
            generation_cfg=generation_cfg,
            branch_seed=branch_seed,
            paired_modified_count=paired_modified_count,
        )
        if not intervention.applicable:
            return {
                "operator_id": operator_id,
                "applicable": False,
                "correct": None,
                "final_answer": None,
                "modified_positions": [],
                "metadata": intervention.metadata,
                "compute": intervention.compute,
                "intervention_compute": intervention.compute,
            }
        result = self.continue_from_snapshot(item, intervention.snapshot, generation_cfg, branch_seed=branch_seed, restore_native_rng=False)
        return {
            **result,
            "operator_id": operator_id,
            "applicable": True,
            "modified_positions": intervention.modified_positions,
            "metadata": intervention.metadata,
            "intervention_compute": intervention.compute,
        }


def create_v2_backend(backend_cfg: dict[str, Any], adapter: TaskAdapter):
    backend_type = str(backend_cfg["type"])
    if backend_type == "rfba_llada":
        return V2LLADABackend(backend_cfg, adapter)
    if backend_type == "dream":
        return V2DreamBackend(backend_cfg, adapter)
    raise ValueError(f"V2 requires a diffusion backend, got backend.type={backend_type}")
