from __future__ import annotations

from typing import Any

import torch
import torch.nn.functional as F

from repairable_diffusion.src.backends.rfba_llada import add_gumbel_noise, get_num_transfer_tokens
from repairable_diffusion.src.v2.backends import ComputeCounter, V2DreamBackend, V2LLADABackend, _restore_rng


def replay_llada_next_state(
    backend: V2LLADABackend,
    snapshot: dict[str, Any],
    generation_cfg: dict[str, Any],
) -> dict[str, Any]:
    """Replay exactly one native LLaDA transition from a saved snapshot."""

    backend.load()
    _restore_rng(snapshot["rng_state"])
    device = next(backend.model.parameters()).device
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
    step_index = int(snapshot["step_index"]) + 1
    if step_index > steps:
        raise ValueError("snapshot has no next transition")
    block_index = (step_index - 1) // steps_per_block
    local_step = (step_index - 1) % steps_per_block
    block_start = prompt_len + block_index * block_length
    block_end = prompt_len + (block_index + 1) * block_length
    mask_index = x == mask_id

    if local_step == 0:
        plan = get_num_transfer_tokens(mask_index[:, block_start:block_end], steps_per_block)[0].detach().cpu().tolist()
    else:
        if int(snapshot["block_index"]) != block_index:
            raise AssertionError("snapshot block state inconsistent with next transition")
        plan = list(snapshot["active_plan"])

    counter = ComputeCounter()
    with torch.no_grad():
        logits = backend._forward(x, counter)
        probs = F.softmax(logits.to(torch.float32), dim=-1)
        x0 = torch.argmax(add_gumbel_noise(logits, temperature), dim=-1)
        if remasking == "low_confidence":
            x0_p = backend._probs_for_tokens(probs, x0)
        elif remasking == "random":
            x0_p = torch.rand((x0.shape[0], x0.shape[1]), device=x0.device)
        else:
            raise NotImplementedError(remasking)
    x0[:, block_end:] = mask_id
    x0 = torch.where(mask_index, x0, x)
    confidence = torch.where(mask_index, x0_p, torch.full_like(x0_p, float("-inf")))
    confidence[:, :prompt_len] = float("-inf")
    confidence[:, block_end:] = float("-inf")
    k = int(plan[local_step])
    finite = torch.isfinite(confidence[0])
    k = min(k, int(finite.sum().item()))
    if k > 0:
        _, selected = torch.topk(confidence[0], k=k)
        x[0, selected] = x0[0, selected]
    return {
        "full_token_ids": x[0].detach().cpu().tolist(),
        "step_index": step_index,
        "block_index": block_index,
        "step_in_block": local_step + 1,
        "compute": counter.to_dict(),
    }


def replay_dream_next_state(
    backend: V2DreamBackend,
    snapshot: dict[str, Any],
    generation_cfg: dict[str, Any],
) -> dict[str, Any]:
    """Replay exactly one native Dream transition, including first-unmask state."""

    backend.load()
    _restore_rng(snapshot["rng_state"])
    device = next(backend.model.parameters()).device
    x = torch.tensor(snapshot["full_token_ids"], dtype=torch.long, device=device).unsqueeze(0)
    prompt_len = int(snapshot["prompt_len"])
    first_conf = backend._first_conf_from_list(list(snapshot["first_conf"]), device)
    is_prompt_mask = torch.zeros_like(x, dtype=torch.bool)
    is_prompt_mask[:, :prompt_len] = True
    step_id = int(snapshot["step_index"])
    total_steps = int(generation_cfg["steps"])
    if step_id >= total_steps:
        raise ValueError("snapshot has no next transition")
    counter = ComputeCounter()
    x, first_conf, _, _, _ = backend._dream_step(
        x,
        first_conf,
        is_prompt_mask,
        step_id=step_id,
        total_steps=total_steps,
        generation_cfg=generation_cfg,
        counter=counter,
    )
    return {
        "full_token_ids": x[0].detach().cpu().tolist(),
        "first_conf": backend._first_conf_to_list(first_conf),
        "step_index": step_id + 1,
        "compute": counter.to_dict(),
    }
