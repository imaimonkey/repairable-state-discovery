# 50924 Seed-Collision Forensic Feasibility

- Frozen execution SHA: `8b1361d3d8d60a58e28847ac35af8dfc2b023d2d`
- Job: `50924` / `v2_gsm8k_dream`
- No branch rerun, metric recomputation, report overwrite, or seal bypass was performed.

## Formal finding

`deterministic_branch_seed()` includes `stage` in the SHA-256 payload, but reduces the first 64 digest bits modulo `2**31 - 1`. Different stage payloads therefore share the same finite integer namespace. The frozen `require_disjoint_seed_sets: true` gate is formally violated by five localization/confirmation seed intersections.

All five are `CROSS_CONTEXT_OR_ITEM_COLLISION`: no overlap maps to the same `(item_id, trajectory_id, step_index, branch_index)` context. The same integer seed is nevertheless reused across unrelated contexts, so this is not evidence of direct candidate-state reuse.

## Minimum correction feasibility

A collision-only correction is technically feasible in a separate namespace:

- Saved `trajectories.pkl` contains snapshots for all five affected confirmation contexts.
- Affected confirmation contexts: `5`.
- Affected confirmation rows: `10` (two paired operators per context).
- Current affected-row NFE: `272` total; forward calls: `272`.
- Full confirmation rows: `178560`. Candidate replacement fraction: `0.00560036%`.
- Localization results can remain unchanged.
- A replacement seed can be selected deterministically from the context key and collision set only, while preserving the same replacement seed across the two paired operators.
- Selection is outcome-independent if based only on seed identity/context and the predeclared collision set.

Derived artifacts would still need deterministic materialization in a new corrected namespace: `probe_branches.jsonl`, `selector_confirmation.csv`, `existence.csv`, `report.json`, manifest hash, and a new provenance record. This has not been performed.

## Cost interpretation

The compute scope is about ten operator branch calls, not a four-day full rerun, but corrected aggregation and a new provenance/audit chain would still be required. The small compute fraction does not by itself establish interchangeability with the original artifact.

## Decision boundary

The correction target is mechanically selected by seed identity, not correctness, q-values, thresholds, or headline outcome. Whether this is accepted as protocol-compliant remains a scientific/provenance decision because the existing artifact violates the frozen disjointness gate.

## Code references

- `repairable_diffusion/src/v2/contracts.py:54-76`: stage-tagged hash followed by 31-bit modulo.
- `repairable_diffusion/src/v2/contracts.py:79-82`: strict cross-stage disjointness assertion.
- `repairable_diffusion/src/v2/run_measurement.py:331-343`: localization seeds; paired operators share a seed.
- `repairable_diffusion/src/v2/run_measurement.py:460-472`: confirmation seeds; paired operators share a seed.
- `scripts/seal_v2_runs.py:69-72`: sealing gate that rejected `50924`.

No seed implementation change is included in this forensic branch.

## Implementation alternatives (not applied)

| Option | Guaranteed disjointness | Reproducibility | Seed-library compatibility | Paired-operator semantics | Preserve existing non-colliding branches | Rerun scope |
|---|---|---|---|---|---|---|
| A. Stage-specific non-overlapping ranges | Yes, if ranges are fixed and capacity-checked | Yes | Good for Python/NumPy/PyTorch integer seeds | Yes, both paired operators receive the same stage-scoped seed | No, changing the mapping changes all affected stage seeds | Broadest; generally requires rerunning all branches whose seed mapping changes |
| B. Encode stage tag in high bits | Yes only if the encoded integer width and downstream seed handling preserve the tag | Yes | Conditional; some libraries or signed/int32 paths may truncate bits | Yes | Usually no if the integer seed is changed for every stage | Broad; same concern about changed existing seeds |
| C. Collision detection plus deterministic rehash | Yes for the realized finite branch set, if collision checks run before execution and rehash is deterministic | Yes | Good with ordinary integer seeds | Yes, rehash is applied at the paired context level | Best; non-colliding existing seeds can remain unchanged | Narrow for realized collisions, but requires a pre-execution collision manifest and corrected reruns |

For the current `50924` evidence, Option C is the smallest operational correction candidate because the target set can be selected solely from seed identity before looking at outcomes. It is not approved here: the frozen protocol and provenance policy must first decide whether a post hoc collision-only correction is admissible. Option A or B is more suitable for a future protocol revision, but would normally invalidate more existing branch seeds and therefore require a new execution generation.
