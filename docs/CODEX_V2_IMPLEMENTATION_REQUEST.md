# Codex V2 Implementation Request

Implement the frozen V2 scientific contract in `docs/v2_scientific_contract.md` without changing the research question or silently relaxing any readiness gate. The existing V1 pipeline must continue to run unchanged and existing V1 outputs must never be overwritten.

## Source of truth

1. `docs/v2_scientific_contract.md`
2. `repairable_diffusion/configs/v2/measurement_contract.yaml`
3. `scripts/audit_v2_design.py`

If existing V1 code conflicts with the V2 contract, preserve V1 and add an isolated V2 path. Do not retrofit V1 artifacts and label them V2.

## Required implementation work

### P0-1. Task adapters

Create `repairable_diffusion/src/v2/task_adapters.py` with a common interface:

- `load_records(cfg)`
- `build_prompt(item, tokenizer)`
- `extract_prediction(text)`
- `evaluate(prediction, gold)`
- `canonicalize(prediction)`
- `evaluator_id` / `evaluator_version`

Required first adapters:
- MATH-500 using a symbolic-equivalence-capable evaluator or benchmark-standard equivalent;
- GSM8K numeric answer evaluation;
- a predeclared exact-answer BBH structured-reasoning adapter;
- MBPP with sandboxed executable evaluation. Never execute generated code in the orchestration process without isolation/time/resource limits.

### P0-2. Faithful decoder state

Create `repairable_diffusion/src/v2/backends.py` (or an equivalent isolated package) with a V2 backend protocol:

- `generate_trajectory_v2(...)`
- `continue_from_snapshot(...)`
- `intervene_snapshot(...)`
- `continue_intervened_snapshot(...)`
- compute counters (`nfe`, forward calls)

Snapshots must contain all decoder state required for phase-faithful replay.

For LLaDA, preserve:
- block index;
- within-block step;
- current transfer schedule/remaining plan or another exactly equivalent decoder state;
- current token sequence and confidence metadata;
- generation hyperparameters needed by the transition kernel.

For Dream, preserve every state variable used by native future transitions, including first-unmask confidence/history state and any phase-dependent decoding values. A V2 no-op continuation must use the native Dream transition logic, including any native penalty/remasking behavior.

### P0-3. Fixed stochastic replicates

V2 repair branches must have one fixed operator specification. Branches differ only by the deterministic stage-separated seed from `v2.contracts.deterministic_branch_seed`.

For every branch call `seed_everything(branch_seed)` before future stochastic model operations.

Do not average different temperatures or remask fractions into one `q_R` estimate.

### P0-4. Operators and controls

Implement required operator ids from the V2 contract:

- `native_continuation`
- `matched_stochastic_continuation`
- `random_position_remask`
- `low_confidence_remask_v2`
- `fresh_sampling_compute_control`
- `core`

Random remask must modify exactly the same number of eligible positions as the paired targeted operator at the same checkpoint.

CoRe must be integrated as an external operator without changing its scientific semantics. Record source revision/version in provenance.

DecoCal is optional and must not block Tier A.

### P0-5. Localization / confirmation split

Create a probe bank keyed by:

`dataset, item_id, trajectory_id, step_index, operator_id, stage, branch_index, branch_seed`

Run `B_loc` branches over eligible checkpoints, choose candidate locations, then estimate the chosen location using disjoint `B_eval` seeds. Preserve both raw branch outcomes and aggregated estimates.

Never report the finite-sample maximum from localization branches as the confirmed oracle estimate.

### P0-6. Observed correctness and decomposition

For every saved checkpoint compute/store:

- provisional answer;
- `o_t`;
- `q_C`;
- `q_R`;
- `delta_R`;
- normalized refinement time;
- block/phase information;
- mask/commitment ratio;
- state-local confidence and entropy features.

Classify/report repairable-but-never-correct trajectories separately from trajectories that were transiently correct.

### P0-7. Learned localization

Replace the V1 headline predictor path for V2 with grouped OOF state-value estimation. Reuse `repairable_diffusion/src/v2/oof.py` where appropriate.

Requirements:
- group by item id;
- every headline score is OOF;
- primary targets are continuous `q_R` or `delta_R`;
- never create positive labels for all-zero/non-repairable trajectories merely because a top-k ranking exists;
- state-local features and multi-trajectory disagreement features are separate variants.

### P0-8. Prospective policy evaluation

Produce two distinct outputs:

1. retrospective diagnostic recovery on known failed trajectories;
2. prospective policy value where intervention can also harm originally successful trajectories.

Main net policy gain must use the second definition. Use branch-level simulation for item pass@k instead of multiplying marginal trajectory probabilities when raw branch outcomes are available.

### P0-9. Actual compute control

Decode actual fresh samples under a matched additional compute budget. Record NFE/forward calls for base generation, native continuation, repair operators, and fresh sampling.

The V1 analytic extra-sampling approximation may remain for historical comparison but cannot be a V2 main result.

### P0-10. Scientific provenance

Every V2 artifact must carry a scientific fingerprint. On cache reuse, compare the stored fingerprint to the current run and fail closed on mismatch.

Use `repairable_diffusion/src/v2/provenance.py` and include all required fields from the measurement contract.

## Required tests

Implement and unskip these tests before full-scale execution:

- `test_snapshot_native_replay`
- `test_branch_seed_reproducibility`
- `test_branch_seed_independence`
- `test_fixed_operator_across_branches`
- `test_zero_repair_no_positive_label`
- `test_grouped_oof_no_item_leakage`
- `test_policy_negative_repair_accounting`
- `test_artifact_fingerprint_invalidation`
- `test_task_adapter_evaluator`
- `test_operator_nfe_accounting`

Add backend-specific replay tests for both LLaDA and Dream. Replay tests must compare transition semantics/state, not only the final decoded answer.

## V2 run namespace

Use only new V2 directories, e.g.:

- `repairable_diffusion/outputs/v2_measurement/...`
- `results/v2_measurement/...`
- `paper/v2_generated/...` until final manuscript promotion

Do not reuse V1 `run_name` values.

## Execution sequence

1. `python scripts/audit_v2_design.py --mode design`
2. implement P0 items above
3. run unit/integration tests
4. `python scripts/audit_v2_design.py --mode execution`
5. run a correctness-only pilot on a predeclared small subset; do not tune the scientific contract to maximize the observed effect
6. freeze git SHA/config/manifest
7. Tier A: LLaDA × MATH-500/GSM8K full deep analysis
8. Tier B mechanism controls on paired states
9. Tier C BBH/MBPP thin validation
10. Tier D Dream transfer
11. aggregate main tables/figures exactly as specified in `docs/v2_paper_structure.md`

## Acceptance criteria

The implementation is not complete merely because jobs launch. It is complete only when:

- V1 behavior/artifacts remain isolated and intact;
- all V2 readiness tests pass;
- no-op continuation semantics are demonstrated for both backbones;
- localization and confirmation seed sets are disjoint;
- operator replicates hold all non-seed hyperparameters fixed;
- actual compute controls exist;
- learned headline scores are grouped OOF;
- prospective policy accounting includes harm to successes;
- the V2 manifest can reproduce the exact scientific fingerprint for every main result.

Do not start the full V2 GPU matrix before these acceptance criteria are satisfied.
