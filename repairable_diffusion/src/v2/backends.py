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


V2_BACKEND_VERSION = "v2.3"
CORE_SOURCE_REPOSITORY = "UCF-CRCV/CoRe"
CORE_SOURCE_REVISION = "524e01e11a8751afb67b81a2c930f938faf9a70e"
DREAM_NATIVE_SOURCE_REPOSITORY = "Dream-org/Dream-v0-Instruct-7B"
DREAM_NATIVE_SOURCE_REVISION = "2f177908857f6f96dbe7b696ad5eac5123535bbd"


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
    """Snapshot-compatible implementation of Dream's official native sampler.

    This mirrors DreamGenerationMixin._sample from the pinned official Dream
    remote-code revision. Decoding follows the native diffusion timestep
    schedule and never adds post-hoc decoding steps.
    """

    backend_type = "dream_v2"

    def __init__(self, cfg: dict[str, Any], adapter: TaskAdapter):
        DreamBackend.__init__(self, cfg)
        self.__init_v2__(adapter)

    def _forward(self, x: torch.Tensor, counter: ComputeCounter) -> torch.Tensor:
        counter.add_forward()
        logits = self.model(x, "full", None).logits
        return torch.cat([logits[:, :1], logits[:, :-1]], dim=1)

    @staticmethod
    def _top_p_logits(logits: torch.Tensor, top_p: float | None) -> torch.Tensor:
        if top_p is None or top_p >= 1:
            return logits
        sorted_logits, sorted_indices = torch.sort(logits, descending=True)
        cumulative_probs = torch.cumsum(F.softmax(sorted_logits, dim=-1), dim=-1)
        sorted_indices_to_remove = cumulative_probs > float(top_p)
        sorted_indices_to_remove[..., 1:] = sorted_indices_to_remove[..., :-1].clone()
        sorted_indices_to_remove[..., 0] = False
        mask = torch.zeros_like(logits, dtype=torch.bool, device=logits.device)
        mask = mask.scatter_(-1, sorted_indices, sorted_indices_to_remove)
        return logits.masked_fill(mask, torch.finfo(logits.dtype).min)

    @staticmethod
    def _top_k_logits(logits: torch.Tensor, top_k: int | None) -> torch.Tensor:
        if top_k is None:
            return logits
        k = min(int(top_k), int(logits.size(-1)))
        if k <= 0:
            return logits
        cutoff = torch.topk(logits, k)[0][..., -1, None]
        return logits.masked_fill(logits < cutoff, torch.finfo(logits.dtype).min)

    def _sample_dream_tokens(
        self,
        logits: torch.Tensor,
        *,
        temperature: float,
        top_p: float | None,
        top_k: int | None,
        margin_confidence: bool = False,
        neg_entropy: bool = False,
    ) -> tuple[torch.Tensor, torch.Tensor]:
        """Mirror official Dream generation_utils.sample_tokens."""
        if temperature > 0:
            logits = logits / float(temperature)
        logits = self._top_p_logits(logits, top_p)
        logits = self._top_k_logits(logits, top_k)
        probs = torch.softmax(logits, dim=-1)
        if temperature > 0:
            try:
                x0 = torch.distributions.Categorical(probs=probs).sample()
                confidence = torch.gather(probs, -1, x0.unsqueeze(-1)).squeeze(-1)
            except Exception:
                confidence, x0 = probs.max(dim=-1)
        else:
            confidence, x0 = probs.max(dim=-1)
        if margin_confidence:
            sorted_probs, _ = torch.sort(probs, dim=-1, descending=True)
            confidence = sorted_probs[..., 0] - sorted_probs[..., 1]
        if neg_entropy:
            confidence = torch.sum(probs * torch.log(probs + 1e-10), dim=-1)
        return confidence, x0

    def _native_params(self, generation_cfg: dict[str, Any]) -> dict[str, Any]:
        alg = str(generation_cfg.get("dream_alg", self.cfg.get("alg", "origin")))
        alg_temp = generation_cfg.get("dream_alg_temp", self.cfg.get("alg_temp"))
        eps = float(generation_cfg.get("dream_eps", self.cfg.get("eps", 1e-3)))
        top_p = generation_cfg.get("top_p", self.cfg.get("top_p", 0.95))
        top_k = generation_cfg.get("top_k", self.cfg.get("top_k"))
        if alg not in {"origin", "maskgit_plus", "topk_margin", "entropy"}:
            raise ValueError(f"unsupported official Dream algorithm: {alg}")
        if alg_temp not in (None, 0, 0.0):
            raise NotImplementedError("V2 Dream supports official alg_temp=None/0 only")
        if not 0.0 < eps < 1.0:
            raise ValueError("Dream eps must lie in (0, 1)")
        return {
            "alg": alg,
            "alg_temp": alg_temp,
            "eps": eps,
            "top_p": None if top_p is None else float(top_p),
            "top_k": None if top_k is None else int(top_k),
        }

    @staticmethod
    def _native_transfer_count(
        num_mask_tokens: int,
        *,
        step_id: int,
        total_steps: int,
        eps: float,
        device: torch.device,
    ) -> int:
        if step_id < 0 or step_id >= total_steps:
            raise ValueError("Dream step_id outside fixed diffusion schedule")
        if step_id == total_steps - 1:
            return int(num_mask_tokens)
        timesteps = torch.linspace(1, eps, total_steps + 1, device=device)
        t = timesteps[step_id]
        s = timesteps[step_id + 1]
        return int(int(num_mask_tokens) * float((1 - s / t).item()))

    def _dream_native_step(
        self,
        x: torch.Tensor,
        *,
        prompt_len: int,
        step_id: int,
        total_steps: int,
        generation_cfg: dict[str, Any],
        counter: ComputeCounter,
    ) -> tuple[torch.Tensor, torch.Tensor, list[int], list[float]]:
        """Execute exactly one transition from Dream's official _sample loop."""
        if x.shape[0] != 1:
            raise NotImplementedError("V2 Dream snapshot instrumentation requires batch size 1")
        mask_token_id = self._mask_token_id(generation_cfg)
        temperature = float(generation_cfg["temperature"])
        params = self._native_params(generation_cfg)
        alg = params["alg"]
        top_p = params["top_p"]
        top_k = params["top_k"]

        mask_index = x == mask_token_id
        with torch.no_grad():
            logits = self._forward(x, counter)
        mask_logits = logits[mask_index]
        if mask_logits.numel() == 0:
            return x, logits, [], []

        mask_abs = torch.where(mask_index[0])[0]
        if alg == "origin":
            timesteps = torch.linspace(1, params["eps"], total_steps + 1, device=x.device)
            t = timesteps[step_id]
            s = timesteps[step_id + 1]
            p_transfer = (1 - s / t) if step_id < total_steps - 1 else torch.tensor(1.0, device=x.device)
            x0 = torch.full_like(x[mask_index], mask_token_id, dtype=torch.long, device=x.device)
            transfer = torch.rand(x0.shape, device=x.device) < p_transfer
            selected_abs = mask_abs[transfer]
            if bool(transfer.any().item()):
                selected_conf, sampled = self._sample_dream_tokens(
                    mask_logits[transfer],
                    temperature=temperature,
                    top_p=top_p,
                    top_k=top_k,
                )
                x0[transfer] = sampled
            else:
                selected_conf = torch.empty(0, device=x.device, dtype=torch.float32)
            x = x.clone()
            x[mask_index] = x0
        else:
            selected_conf_all, x0 = self._sample_dream_tokens(
                mask_logits,
                temperature=temperature,
                top_p=top_p,
                top_k=top_k,
                margin_confidence=(alg == "topk_margin"),
                neg_entropy=(alg == "entropy"),
            )
            number_transfer_tokens = self._native_transfer_count(
                int(mask_index.sum().item() // x.shape[0]),
                step_id=step_id,
                total_steps=total_steps,
                eps=float(params["eps"]),
                device=x.device,
            )
            if number_transfer_tokens <= 0:
                selected_abs = torch.empty(0, device=x.device, dtype=torch.long)
                selected_conf = torch.empty(0, device=x.device, dtype=torch.float32)
            else:
                full_confidence = torch.full(x.shape, -torch.inf, device=x.device, dtype=logits.dtype)
                full_confidence[mask_index] = selected_conf_all.to(dtype=logits.dtype)
                _, transfer_index = torch.topk(full_confidence, number_transfer_tokens, dim=-1)
                x_candidates = torch.full_like(x, mask_token_id, dtype=torch.long, device=x.device)
                x_candidates[mask_index] = x0
                row_indices = torch.arange(x.size(0), device=x.device).unsqueeze(1).expand_as(transfer_index)
                x = x.clone()
                x[row_indices, transfer_index] = x_candidates[row_indices, transfer_index]
                selected_abs = transfer_index[0]
                selected_conf = full_confidence[0, selected_abs].to(torch.float32)

        generated = selected_abs[selected_abs >= prompt_len] - prompt_len
        return (
            x,
            logits,
            [int(v) for v in generated.detach().cpu().tolist()],
            [float(v) for v in selected_conf.detach().cpu().tolist()],
        )

    def _assert_snapshot_sampler(self, snapshot: dict[str, Any], generation_cfg: dict[str, Any]) -> None:
        state = dict(snapshot.get("backend_state") or {})
        current = self._native_params(generation_cfg)
        expected = {
            "dream_alg": current["alg"],
            "dream_alg_temp": current["alg_temp"],
            "dream_eps": current["eps"],
            "sampler_source_revision": DREAM_NATIVE_SOURCE_REVISION,
        }
        for key, value in expected.items():
            if key in state and state[key] != value:
                raise RuntimeError(
                    f"Dream snapshot sampler mismatch for {key}: saved={state[key]!r} current={value!r}"
                )

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
        params = self._native_params(generation_cfg)

        x = F.pad(prompt_ids, (0, gen_length), value=mask_id)
        prompt_len = int(prompt_ids.shape[1])
        counter = ComputeCounter()
        rows: list[dict[str, Any]] = []

        for step_id in range(steps):
            x, logits, new_positions, new_conf = self._dream_native_step(
                x,
                prompt_len=prompt_len,
                step_id=step_id,
                total_steps=steps,
                generation_cfg=generation_cfg,
                counter=counter,
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
                "new_positions": new_positions,
                "new_token_conf_mean": float(np.mean(new_conf)) if new_conf else 0.0,
                "state_token_conf_mean": float(np.mean([v for v in token_confidences if v is not None])) if any(v is not None for v in token_confidences) else 0.0,
                "state_token_conf_min": float(np.min([v for v in token_confidences if v is not None])) if any(v is not None for v in token_confidences) else 0.0,
                "masked_entropy_mean": entropy_mean,
                "masked_entropy_max": entropy_max,
                "answer_candidate": provisional,
                "observed_correct": self._adapter_correct(provisional, item) if provisional is not None else False,
                "snapshot": None,
            }
            if (step_id + 1) % checkpoint_stride == 0 or step_id + 1 == steps:
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
                    first_conf=None,
                    rng_state=_rng_snapshot(),
                    backend_state={
                        "dream_alg": params["alg"],
                        "dream_alg_temp": params["alg_temp"],
                        "dream_eps": params["eps"],
                        "sampler_source_repository": DREAM_NATIVE_SOURCE_REPOSITORY,
                        "sampler_source_revision": DREAM_NATIVE_SOURCE_REVISION,
                    },
                ).to_dict()
            rows.append(row)

        remaining = int((x[:, prompt_len:] == mask_id).sum().item())
        if remaining:
            raise RuntimeError(
                f"official Dream fixed schedule ended with {remaining} masks; native sampler fidelity is broken"
            )
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
            "backend_reference": {
                "sampler_source_repository": DREAM_NATIVE_SOURCE_REPOSITORY,
                "sampler_source_revision": DREAM_NATIVE_SOURCE_REVISION,
                "dream_alg": params["alg"],
                "dream_alg_temp": params["alg_temp"],
                "dream_eps": params["eps"],
            },
        }

    def canonical_remask_positions(
        self,
        snapshot: dict[str, Any],
        operator_cfg: dict[str, Any],
        generation_cfg: dict[str, Any],
    ) -> list[int]:
        confs = list(snapshot["token_confidences"])
        eligible = [(idx, float(conf)) for idx, conf in enumerate(confs) if conf is not None]
        if not eligible:
            return []
        anchor = float(operator_cfg.get("anchor_confidence_threshold", 0.80))
        low = [row for row in eligible if row[1] < anchor] or eligible
        low.sort(key=lambda row: row[1])
        target = max(
            int(math.ceil(len(low) * float(operator_cfg["remask_fraction"]))),
            int(operator_cfg["min_remask_positions"]),
        )
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
        self._assert_snapshot_sampler(snapshot, generation_cfg)
        snap = dict(snapshot)
        snap["full_token_ids"] = list(snapshot["full_token_ids"])
        snap["token_confidences"] = list(snapshot["token_confidences"])
        snap["backend_state"] = dict(snapshot.get("backend_state") or {})
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
                positions = sorted(
                    int(x)
                    for x in rng.choice(eligible, size=min(count, len(eligible)), replace=False).tolist()
                )
        else:
            raise ValueError(f"unsupported Dream intervention: {operator_id}")

        if not positions:
            return InterventionResult(
                snap,
                operator_id,
                False,
                [],
                {"reason": "no_eligible_positions"},
                {"nfe": 0, "forward_calls": 0},
            )
        prompt_len = int(snap["prompt_len"])
        mask_id = self._mask_token_id(generation_cfg)
        for rel in positions:
            snap["full_token_ids"][prompt_len + rel] = mask_id
            snap["token_confidences"][rel] = None
        return InterventionResult(
            snap,
            operator_id,
            True,
            positions,
            {"paired_target_count": len(targeted)},
            {"nfe": 0, "forward_calls": 0},
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
        self._assert_snapshot_sampler(snapshot, generation_cfg)
        if restore_native_rng:
            _restore_rng(snapshot["rng_state"])
        elif branch_seed is not None:
            seed_everything(int(branch_seed))
        else:
            raise ValueError("continuation requires branch_seed or restore_native_rng=True")

        device = next(self.model.parameters()).device
        x = torch.tensor(snapshot["full_token_ids"], dtype=torch.long, device=device).unsqueeze(0)
        prompt_len = int(snapshot["prompt_len"])
        total_steps = int(generation_cfg["steps"])
        mask_id = self._mask_token_id(generation_cfg)
        counter = ComputeCounter()

        for step_id in range(int(snapshot["step_index"]), total_steps):
            x, _, _, _ = self._dream_native_step(
                x,
                prompt_len=prompt_len,
                step_id=step_id,
                total_steps=total_steps,
                generation_cfg=generation_cfg,
                counter=counter,
            )

        remaining = int((x[:, prompt_len:] == mask_id).sum().item())
        if remaining:
            raise RuntimeError(
                f"V2 Dream native continuation exhausted fixed schedule with {remaining} masks"
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
            return {
                **result,
                "operator_id": operator_id,
                "modified_positions": [],
                "intervention_compute": {"nfe": 0, "forward_calls": 0},
            }
        if operator_id == "matched_stochastic_continuation":
            result = self.continue_from_snapshot(
                item, snapshot, generation_cfg, branch_seed=branch_seed, restore_native_rng=False
            )
            return {
                **result,
                "operator_id": operator_id,
                "modified_positions": [],
                "intervention_compute": {"nfe": 0, "forward_calls": 0},
            }
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
            item,
            intervention.snapshot,
            generation_cfg,
            branch_seed=branch_seed,
            restore_native_rng=False,
        )
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
