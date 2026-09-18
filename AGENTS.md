# AGENTS.md — Repairable State Discovery V2

This repository contains two scientific generations. **V1 is historical/exploratory and frozen. V2 is the final-paper path.**

All execution agents (including Codex) must obey this file before launching jobs. **Codex is execution-only for this project: it must not edit, commit, or push repository code. Code changes are made by the research owner through the designated coding assistant before handoff.**

## 1. Source-of-truth order

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

## 3. V1 isolation

Never overwrite, rename, reinterpret, or reuse V1 outputs as V2 evidence.

V2 writes only to:

- `repairable_diffusion/outputs/v2_measurement/`
- `results/v2_measurement/`
- `paper/v2_generated/` until final promotion

A V2 run name must start with `v2_`. If an artifact fingerprint differs, fail closed; never force cache reuse.

## 4. Frozen execution matrix

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

## 5. Frozen operator semantics

`native_continuation` is an **exact replay/fidelity control**, not the estimator of `q_C`.

`matched_stochastic_continuation` is the estimator of `q_C`: same snapshot and phase-faithful continuation, with future stochasticity resampled by a stage-separated branch seed.

`low_confidence_remask_v2` is the canonical intervention. Its hyperparameters are fixed across stochastic replicates.

`random_position_remask` must modify exactly the same number of eligible positions as the paired low-confidence intervention at the same checkpoint.

For LLaDA, a local intervention is scoped to the **currently active block/phase**. Completed blocks are not silently reopened. Block-boundary snapshots with no active committed positions are inapplicable to local remasking.

`core` is the checkpoint adaptation of the public CoRe context-brittleness scoring rule. In tables/text call it **CoRe-snapshot**. Do not call it an unmodified full-sequence CoRe reproduction. Record the official source revision in provenance.

`fresh_sampling_compute_control` means actually decoded fresh samples. The V1 analytic extra-sampling proxy is appendix/history only.

## 6. Statistical boundary

- Localization uses `B_loc` branches.
- Confirmation uses disjoint `B_eval` seeds.
- Never report the finite-sample localization maximum as the confirmed oracle estimate.
- Headline learned scores must be grouped out-of-fold by `item_id`.
- Simple temporal priors are predeclared (`1/4`, `1/2`, `3/4` normalized progress); do not rename a result-selected absolute step as “middle”.
- Retrospective recovery and prospective net policy value are different outputs. Prospective value must count harm to originally successful trajectories.
- Retrospective probe strata may sample one failed and one successful trajectory per item, but **prospective deployment may not use that outcome-selected set**. Prospective policy evaluation is frozen to `probe.policy_trajectory_ids: [0]` for every item regardless of final correctness; all other base trajectories stay unchanged.
- Item pass@k uses branch-level simulation when raw branch outcomes exist; do not multiply marginal trajectory probabilities.

## 7. No result-contingent redesign

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

## 8. Mandatory gate order

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

## 9. Job execution

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

## 10. Codex execution-only boundary

Codex may **execute** without asking:

- environment activation and environment-variable setup;
- Slurm resource requests and node selection;
- copying/synchronizing the exact committed SHA to execution nodes;
- submitting, monitoring, resuming, and collecting jobs without changing scientific fingerprints;
- logging the exact failure and infrastructure context.

Codex must **not** modify repository code, YAMLs, tests, contracts, or documentation; must not commit; and must not push. This includes deterministic bug fixes and path-portability code changes.

If execution exposes a code bug, path-portability issue that requires a code edit, replay mismatch, evaluator problem, or scientific-gate failure, Codex must stop the affected tier and report the exact traceback/log/state. The research owner will patch and push the repository, after which Codex restarts the relevant gates from the new SHA.

Infrastructure choices that do not modify tracked files (environment variables, Slurm flags, cache locations, node-local clean clones) remain allowed.
## 11. Stop conditions

Stop and report instead of improvising if:

- exact native replay fails for the currently affected backend tier;
- same-seed continuation is not reproducible;
- a required model/dataset cannot be loaded with the frozen revision;
- MBPP restricted evaluation cannot be executed safely on the cluster;
- a stale V1/V2 artifact collision is detected;
- CoRe-snapshot cannot preserve the documented context-brittleness scoring semantics;
- full submission would require changing a scientific parameter.

## 12. Required final deliverables

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
