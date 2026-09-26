# AGENTS.md — Repairable State Discovery Generations

This repository contains three scientific generations. **V1 is historical/exploratory and frozen. V2 is a frozen prior-paper generation. RSD Generation 3 (`rsd_ref_v3`) is the active confirmatory generation.** Generations are isolated by source-of-truth documents, configuration namespaces, output namespaces, manifests, and provenance.

All execution agents (including Codex) must obey this file before launching jobs. **Codex is execution-only for this project: it must not edit, commit, or push repository code. Code changes are made by the research owner through the designated coding assistant before handoff.**

## 1. Source-of-truth order

For RSD Generation 3 (`rsd_ref_v3`), use this authority order and do not mix it with the V2 hierarchy:

1. `AGENTS.md`
2. `docs/rsd_ref_v3_scientific_contract.md`
3. `repairable_diffusion/configs/rsd_ref_v3/measurement_contract.yaml`
4. `docs/RSD_REF_V3_EXECUTION.md`
5. frozen `repairable_diffusion/configs/rsd_ref_v3/runs/` configs and pinned source recipes
6. `scripts/audit_rsd_ref_v3.py`

For the frozen prior V2 generation, use the hierarchy below.

1. `docs/v2_scientific_contract.md`
2. `repairable_diffusion/configs/v2/measurement_contract.yaml`
3. `docs/CODEX_V2_FINAL_EXECUTION.md`
4. `scripts/audit_v2_design.py`
5. V2 run configs under `repairable_diffusion/configs/v2/`

If code conflicts with the contract, **Codex must stop and report the conflict**. Repository code changes are made by the research owner/designated coding assistant, never by Codex. Do not silently edit the contract to make a failing implementation pass.

## 2. Non-negotiable research boundary

The paper studies **counterfactual state-level recoverability in ultimately failed diffusion reasoning trajectories**. The headline quantities are:

- observed transient correctness `o_t`;
- stochastic continuation recoverability `q_C(x_t)`;
- intervention-conditioned recoverability `q_R(x_t)`;
- intervention lift `Delta_R(x_t) = q_R(x_t) - q_C(x_t)`;
- operational last-confirmed-repairable checkpoint `T_last` on the predeclared temporal-confirmation subset.

Do **not** redirect the project toward:

- generic DLM decoding SOTA;
- DLM-vs-AR leaderboard ranking;
- a new learned predictor architecture;
- a new remasking method;
- changing datasets/operators after seeing results;
- maximizing a positive headline number.

Negative, null, or inconsistent results must be retained.

## 3. Generation isolation

Never overwrite, rename, reinterpret, or reuse V1 or V2 outputs as RSD Generation 3 evidence. Existing V2 is `FROZEN_HISTORICAL_GENERATION` for this branch of work; its outputs, configs, manifests, and claims are not Generation 3 denominators.

V2 writes only to:

- `repairable_diffusion/outputs/v2_measurement/`
- `results/v2_measurement/`
- `paper/v2_generated/` until final promotion

A V2 run name must start with `v2_`. If an artifact fingerprint differs, fail closed; never force cache reuse.

RSD Generation 3 writes only to:

- `repairable_diffusion/configs/rsd_ref_v3/`
- `outputs/rsd_ref_v3/`
- `results/rsd_ref_v3/`
- `status/rsd_ref_v3/`

A Generation 3 run name must start with `rsd_ref_v3_`. A Generation 3 artifact must reject stale V1/V2 namespaces and mismatched fingerprints; never force cache reuse.

Generation 3 uses one source-native reference trajectory per item for the base bank. Counterfactual branches are not base pass@k and must not be silently pooled with the base denominator.

## 4. V2-only frozen execution matrix

The matrix in this section applies **only to the frozen V2 generation**. It is
not a requirement for RSD Generation 3 and must not be used to override the
Generation 3 contract.

Deep anchor:

- LLaDA-8B-Instruct × MATH-500
- LLaDA-8B-Instruct × GSM8K

Predeclared BBH breadth:

- `logical_deduction_three_objects`
- `logical_deduction_five_objects`
- `logical_deduction_seven_objects`

Code breadth:

- MBPP sanitized test split

Backbone transfer:

- Dream-v0-Instruct-7B × MATH-500
- Dream-v0-Instruct-7B × GSM8K

Do not substitute another dataset because it is easier or looks better without explicit human approval.

## 5. RSD Generation 3-only scientific matrix

Generation 3 (`rsd_ref_v3`) has a separate source-native primary matrix:

- LLaDA-8B-Instruct × OpenCompass-native MATH test archive, 5,000 items;
- LLaDA-8B-Instruct × OpenCompass-native GSM8K test archive, 1,319 items;
- Dream MATH/GSM are secondary replication tasks and never fill a LLaDA cell;
- MATH-500 is a calibration bridge only and is never a confirmatory denominator;
- the base bank has exactly one source-native reference trajectory per item;
- deep stages are materialized only after the full base bank is sealed and the
  outcome-independent hash-ranked subset is frozen.

Generation 3 task identity, prompts, evaluators, recipes, operators, targets,
and provenance are defined by the Generation 3 source-of-truth documents named
in section 1. Its artifacts must remain under the `rsd_ref_v3` namespace.

## 6. Shared operator semantics

`native_continuation` is an **exact replay/fidelity control**, not the estimator of `q_C`.

`matched_stochastic_continuation` is the estimator of `q_C`: same snapshot and phase-faithful continuation, with future stochasticity resampled by a stage-separated branch seed.

`low_confidence_remask_v2` is the canonical intervention. Its hyperparameters are fixed across stochastic replicates.

`random_position_remask` must modify exactly the same number of eligible positions as the paired low-confidence intervention at the same checkpoint.

For LLaDA, a local intervention is scoped to the **currently active block/phase**. Completed blocks are not silently reopened. Block-boundary snapshots with no active committed positions are inapplicable to local remasking.

`core` is the checkpoint adaptation of the public CoRe context-brittleness scoring rule. In tables/text call it **CoRe-snapshot**. Do not call it an unmodified full-sequence CoRe reproduction. Record the official source revision in provenance.

`fresh_sampling_compute_control` means actually decoded fresh samples. The V1 analytic extra-sampling proxy is appendix/history only.

## 7. Shared statistical boundary

- Localization uses `B_loc` branches.
- Confirmation uses disjoint `B_eval` seeds.
- Never report the finite-sample localization maximum as the confirmed oracle estimate.
- Headline learned scores must be grouped out-of-fold by `item_id`.
- Simple temporal priors are predeclared (`1/4`, `1/2`, `3/4` normalized progress); do not rename a result-selected absolute step as “middle”.
- Retrospective recovery and prospective net policy value are different outputs. Prospective value must count harm to originally successful trajectories.
- Retrospective probe strata may sample one failed and one successful trajectory per item, but **prospective deployment may not use that outcome-selected set**. Prospective policy evaluation is frozen to `probe.policy_trajectory_ids: [0]` for every item regardless of final correctness; all other base trajectories stay unchanged.
- Item pass@k uses branch-level simulation when raw branch outcomes exist; do not multiply marginal trajectory probabilities.

## 8. Shared no-result-contingent redesign rule

After the two frozen pilot runs complete, they are used only to verify execution correctness and resource feasibility.

Do not alter any of the following because the observed effect is weak or inconvenient:

- confirmation threshold;
- checkpoint stride;
- operator fraction/threshold;
- branch count;
- task list;
- selector list;
- temporal subset;
- mechanism subset;
- success/failure trajectory sampling policy.

A change to one of these requires explicit human approval and a new contract version.

## 9. Mandatory gate order by generation

### V2-only gates

Before primary LLaDA submission:

```bash
bash scripts/run_v2_suite.sh preflight
python scripts/validate_v2_backends.py --backend llada
bash scripts/run_v2_suite.sh pilot-primary
python scripts/audit_v2_design.py --mode primary
```

The Dream transfer gate is independent and must not block Tier A:

```bash
python scripts/validate_v2_backends.py --backend dream
python scripts/audit_v2_design.py --mode dream
```

If any command fails, stop the affected tier and report it. Codex does not fix repository code.

### RSD Generation 3 gates

The designated coding assistant must freeze and audit the new generation before
handoff. The design audit is independent of mutable storage/runtime state:

```bash
python scripts/audit_rsd_ref_v3.py --mode design
```

The readiness audit additionally requires the exact canonical execution SHA,
server1 scientific qualification, approved storage reservation, live runtime
health/free-space checks, and protocol freeze. `--mode readiness` is the only
gate that may authorize execution; design freeze remains valid when storage
status later changes from `STORAGE_NOT_RESERVED` to `STORAGE_READY`.

Cross-server equivalence is required only when multi-server shard pooling is selected. A single-server primary execution may proceed without it.

## 10. Job execution by generation

### V2-only job execution

After the primary gate passes:

```bash
python scripts/submit_v2_suite.py --tier primary
```

After the independent Dream gate passes:

```bash
python scripts/submit_v2_suite.py --tier dream
```

LLaDA breadth can be submitted after the primary gate:

```bash
python scripts/submit_v2_suite.py --tier breadth
```

or, on a single machine with enough time:

```bash
bash scripts/run_v2_suite.sh full-local
```

Use `--dry-run` before Slurm submission when adapting cluster flags. Changing Slurm partition/time/memory is allowed; changing scientific config is not.

### RSD Generation 3 job execution

Generation 3 uses the explicit runner and neutral job namespace. These commands
are executable entry points, but all non-dry-run stages fail closed until the
readiness audit passes:

```bash
python scripts/run_rsd_ref_v3.py --stage reference --task llada_math --dry-run
python scripts/run_rsd_ref_v3.py --stage reference --task llada_gsm8k --dry-run
python scripts/run_rsd_ref_v3.py --stage materialize-subsets --dry-run
python scripts/run_rsd_ref_v3.py --stage core --task llada_math --dry-run
python scripts/run_rsd_ref_v3.py --stage temporal --task llada_math --dry-run
python scripts/run_rsd_ref_v3.py --stage mechanism --task llada_math --dry-run
python scripts/run_rsd_ref_v3.py --stage successful-harm --task llada_math --dry-run
python scripts/submit_rsd_ref_v3.py --stage reference --task llada_math --dry-run
```

The fixed execution order is: full source-native reference bank, base seal,
failed/successful pool materialization, subset-manifest seal, core/temporal/
mechanism/successful-harm execution, aggregate, then compact seal. A deep
stage may not manufacture item IDs before its sealed base bank exists.

## 11. Codex execution-only boundary

Codex may **execute** without asking:

- environment activation and environment-variable setup;
- Slurm resource requests and node selection;
- copying/synchronizing the exact committed SHA to execution nodes;
- submitting, monitoring, resuming, and collecting jobs without changing scientific fingerprints;
- logging the exact failure and infrastructure context.

Codex must **not** modify scientific code, YAMLs, tests, contracts, or documentation after a generation is handed off for execution; must not commit; and must not push. This includes deterministic bug fixes and path-portability code changes. The designated coding assistant may create or revise a new generation before handoff, after which the execution-only boundary applies again.

If execution exposes a code bug, path-portability issue that requires a code edit, replay mismatch, evaluator problem, or scientific-gate failure, Codex must stop the affected tier and report the exact traceback/log/state. The research owner will patch and push the repository, after which Codex restarts the relevant gates from the new SHA.

Infrastructure choices that do not modify tracked files (environment variables, Slurm flags, cache locations, node-local clean clones) remain allowed.
## 12. Stop conditions

Stop and report instead of improvising if:

- exact native replay fails for the currently affected backend tier;
- same-seed continuation is not reproducible;
- a required model/dataset cannot be loaded with the frozen revision;
- MBPP restricted evaluation cannot be executed safely on the cluster;
- a stale V1/V2 artifact collision is detected;
- CoRe-snapshot cannot preserve the documented context-brittleness scoring semantics;
- full submission would require changing a scientific parameter.

## 13. Required final deliverables

Codex execution is complete only when `results/v2_measurement/` contains:

- unit-preflight PASS stamp tied to the final git SHA;
- backend validation PASS artifact tied to the same git SHA;
- frozen pilot reports;
- every full run `report.json`;
- actual fresh-sampling controls for Tier A;
- `aggregate_report.json`;
- `table1_existence.csv`;
- `table2_mechanisms.csv`;
- `table3_localization.csv`;
- raw localization/confirmation branch files and provenance sidecars;
- `paper/v2_generated/tables/` with the three generated main-table sources;
- `figure_data/` for recoverability/survival and recovery-harm-compute figures;
- `final_execution_manifest.json` recording git SHA, config hashes, job IDs, and infrastructure-only deviations.

Do not draft stronger claims than these artifacts support.

The V2 deliverables above apply only to the frozen V2 generation.

For RSD Generation 3, the required pre-execution handoff is defined in
`docs/RSD_REF_V3_EXECUTION.md`, `status/rsd_ref_v3/design_freeze.json`, and
the runtime readiness files. Generation 3 confirmatory execution is not
authorized merely because V2 artifacts exist.
