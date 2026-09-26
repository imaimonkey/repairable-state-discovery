# RSD Generation 3 Scientific Contract

Status: **FROZEN DESIGN BEFORE CONFIRMATORY OUTCOMES**

Generation id: `rsd_ref_v3`

This contract defines the new source-faithful confirmatory generation. It does not modify or reinterpret V1 artifacts, the frozen prior V2 generation, the V2R calibration evidence, or legacy jobs. The authoritative implementation namespace is `repairable_diffusion/configs/rsd_ref_v3/`; the authoritative execution handoff is `docs/RSD_REF_V3_EXECUTION.md`.

## Scientific question

Under source-faithful reference diffusion decoding, do ultimately failed trajectories contain intermediate states from which a controlled local intervention can recover the correct answer?

The primary claim boundary is:

> Final failure is an endpoint observation and does not necessarily imply that every intermediate diffusion state is already irrecoverable.

The following claims are not pre-registered as positive outcomes and must not be asserted without separate evidence: a universal irrecoverability point, a monotonic temporal law, causal reasoning recovery, reliable prospective localization, decoding superiority, or efficiency superiority.

## Generation and provenance boundary

- `rsd_ref_v3` is a new scientific generation; it is not a continuation of V2's generic 64-step measurement decoder.
- Canonical source parent: `227cbcc99c7edfac83de7f34c452db7defd5bdcb`.
- Server1 runtime qualification evidence: `b1e8ab7e3b7c4b9f93995e437da3615bff910390`.
- The server1 MATH-500 R0/R1/R2 calibration is runtime/replay qualification only. It is not a Generation 3 confirmatory result or denominator.
- Existing pilot and legacy results are planning, compute, debugging, or historical evidence only; no confirmatory estimate may pool them.
- Generation 3 artifacts may be written only under `outputs/rsd_ref_v3/`, `results/rsd_ref_v3/`, and `status/rsd_ref_v3/`.

## Reference populations and baselines

Generation 3 primary reference banks use exactly one source-native trajectory per item:

| Task | Source-native population | Split/count | Prompt | Evaluator | Generation recipe |
|---|---|---:|---|---|---|
| LLaDA MATH | pinned OpenCompass MATH archive | test/5000 | official zero-shot chat rendering | pinned OpenCompass `MATHEvaluator(version=v2)` and `math_postprocess_v2` | 512 steps, length 512, block 64, temperature 0, CFG 0, low-confidence remasking |
| LLaDA GSM8K | pinned OpenCompass GSM8K archive | test/1319 | official four-shot chat rendering | pinned OpenCompass `Gsm8kEvaluator` and postprocessors | 256 steps, length 256, block 8, temperature 0, CFG 0, low-confidence remasking |

The pinned source files, archive hashes, model/tokenizer revision, prompt policy, evaluator identity, and reported upstream values are frozen in [RSD Generation 3 task specification](RSD_REF_V3_TASK_SPEC.md). HuggingFace MATH-500 is retained as calibration/pilot only and is explicitly not treated as the source-native OpenCompass MATH population.

Dream MATH/GSM8K are secondary replication configurations. Dream does not block the LLaDA Tier A path and is never silently substituted for the LLaDA primary.

## Base trajectory and failed pool

The base bank is `one source-native reference trajectory / item`, equivalent to a reference `pass@1` observation. The prior V2 `8 trajectories/item` denominator is not reused. Counterfactual branches are estimator/control budget and are never relabeled as base pass@k.

The full source-native bank is generated before confirmatory selection. The failed pool is defined only by final base correctness. Within that failed pool, deterministic hash-ranked subsets are selected without using repairability outcomes. A shortage below a frozen target is recorded as `NEEDS_REVIEW`; it is not silently replaced by an easier population.

Selection key:

```text
SHA256(generation | design_seed | backbone | task | purpose | item_id | trajectory_id)
```

The Generation 3 design seed is `314159265`. The exact selection policy and subset manifests are tracked under `status/rsd_ref_v3/`.

## Intervention and control semantics

The minimum primary comparison contains:

1. exact native replay/fidelity control;
2. source-native continuation `q_C` where the decoder regime gives a meaningful stochastic continuation;
3. canonical targeted repair `q_R` using `low_confidence_remask_v2`;
4. matched-count random-position remask control.

For LLaDA, interventions modify only eligible positions in the current active block/phase and never reopen completed blocks. The random control changes exactly the same number of eligible positions as the paired targeted repair. `CoRe-snapshot` and actual fresh-sampling compute control are predeclared mechanism-tier controls and do not block the primary existence test.

Because the source-native LLaDA recipes use temperature 0, repeated nominal seed branches may be identical. Such repetitions are deterministic confirmation, not independent Bernoulli trials. The contract distinguishes deterministic exact confirmation from stochastic estimation; statistical units remain item/trajectory level.

## Temporal and branch design

The predeclared normalized checkpoint grid is:

```text
0.125, 0.250, 0.375, 0.500, 0.625, 0.750, 0.875
```

`T_last^R` is an operational last-confirmed-repairable statistic. No monotonicity or universal point-of-no-return assumption is made. Localization and confirmation use disjoint seed namespaces when stochastic branches are meaningful; default branch budgets are `B_loc=4` and `B_eval=8`, with exact deterministic duplicate handling recorded rather than counted as independent evidence.

## Frozen estimands

- transient correctness: `o_t`;
- native recoverability: `q_C(x_t)`;
- intervention recoverability: `q_R(x_t)`;
- intervention lift: `Delta_R(x_t) = q_R(x_t) - q_C(x_t)`;
- confirmed repairability prevalence;
- operational `T_last^R` and temporal survival;
- intervention harm on originally correct source-native trajectories;
- exact NFE/forward-call accounting.

Primary analyses report raw counts and denominators, Wilson or exact binomial intervals where applicable, paired intervention/control differences, and item-level bootstrap intervals where appropriate. Pilot and confirmatory denominators are never pooled. Learned localization scores must be grouped out-of-fold by `item_id`; retrospective oracle selection is not prospective deployment.

## Frozen sample targets

Before confirmatory outcomes are observed, the resource-only targets are:

- core: 256 failed trajectories per primary task;
- temporal: 128 failed trajectories per primary task;
- mechanism: 128 failed trajectories per primary task;
- successful-trajectory harm control: 128 trajectories per primary task.

These targets are subject to measured resource feasibility and the explicit shortage rule above. The complete resource calculation is in `docs/rsd_ref_v3_sample_size_plan.md`.

## Readiness gate

Single-server primary execution requires all of:

```text
canonical source/config SHA match
server1 SCIENTIFIC_EXECUTION_QUALIFIED
server1 STORAGE_READY
CONFIRMATORY_PROTOCOL_FROZEN
```

Cross-server equivalence is an additional requirement only when multi-server shard pooling is selected. Phase 3A freezes design and storage; it does not start a full reference bank or any confirmatory scientific run.
