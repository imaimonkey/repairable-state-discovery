# Reference-primary protocol — 72-hour reset, generation 2

Frozen before any R0 GPU or R3 outcome. This document supersedes the priority, size, cancellation and reproduction-scope clauses of `V2R_REFERENCE_DESIGN_20260923.md` under the user's latest `V2R_REFERENCE_PRIMARY_FULL_RESET_20260923.md` and accompanying hard-critical-path instruction. All unmodified source pins, task prompts, evaluator identity, operator semantics, phase-valid checkpoint mapping, RNG separation, provenance and evidence restrictions in that design remain binding. Generation-1 freeze88127ca is historical, not overwritten.

## Hard critical path

**LLaDA-MATH deep reference evidence > LLaDA-GSM8K replication > Dream-MATH replication > Dream-GSM8K.** Dream must never delay LLaDA completion, sealing or paper integration. At T−24h, integrate the strongest completed SEALED reference evidence rather than wait for the full matrix. Minimum scientific scope for a core reference claim is LLaDA MATH full500, failed64 core, temporal32; GSM is the next task replication. The author determines whether available evidence warrants submission and claim strength. Missing Dream does not block a completed LLaDA artifact's seal.

## Authorized legacy reset

50668 and50669 are explicitly authorized for cancellation after read-only Slurm/artifact snapshots. Status is CANCELLED_FOR_REFERENCE_PRIMARY_RESET. Original artifacts/worktrees remain untouched. 50753/50754/50923 and all old V2 artifacts are LEGACY_MEASUREMENT_DECODER_EVIDENCE, never fill missing reference cells. 50924 forensic is outside the critical path. Existing live monitor remains running.

## Models, tasks and recipes

Source pins in unchanged `results/v2r_reference/reference_recipes/llada.json` and `dream.json` remain binding. One trajectory_id0 per item. LLaDA MATH-500 test500 first; GSM8K main test1319 second. Dream MATH same500 third; Dream GSM optional. Exact source-native prompts retained (including LLaDA GSM four fixed demonstrations) so paper adapter exposes those prompts instead of silently replacing them. Source-native evaluator and the existing paper evaluator both score the same output; differences are recorded. No score-matching search.

R0 now means source-native16-item smoke plus recipe fidelity, not a prerequisite full5000-item official benchmark rerun. R1 bridges to exact paper datasets and tests evaluators. R2 is32 fixed items per backbone/task and two deterministic seed scenarios, exact final token/text/answer/correctness/schedule/NFE/RNG equivalence. Passing source-native smoke is not a claim of full official benchmark reproduction. Next, full paper-task bank is the reference baseline and receives reproduction sanity assessment. Full-MATH and MATH-500 are NOT_DIRECTLY_COMPARABLE; do not run separate full5000 solely to delay paper anchors. R2-passing LLaDA may proceed while Dream remains pending, under the explicit hard-critical-path instruction.

## Frozen sampling and compute

Design seed20260923. Full baseline bank is generated once with validated snapshots and reused for R3. Hash-ranked failed pool requires that task's full bank to finish; we choose this cleaner rule, not an early first-fail prefix. Parallelize that bank's shards to minimize the wait, then start its repairability while other task baselines run. No waiting for all four task banks.

Core sizes: LLaDA target64/min32 per task; Dream target32/min32 per task (no automatic64 expansion in this 72-hour generation). LLaDA temporal32 and mechanism32 each; if fewer than32 failures exist, record shortage and NEEDS_REVIEW rather than silently redefining primary evidence. Timing/resource-only rule chooses LLaDA32–64; target64 preferred. Dream deep mechanisms are out of scope. Successful harm subset: deterministic hash-ranked32 successes per LLaDA task, explicit coverage; if fewer, all successes and report count. Subsets depend only on base final correctness and design hash, never repairability.

Rank core failed trajectories by canonical JSON hash `[20260923,backbone,task,item_id,0]`. Temporal/mechanism/policy_success include their purpose tag before item_id; each has its own frozen selection manifest. Bank SHA binds every selected trajectory.

Use the seven normalized target checkpoints from the previous design. LLaDA nearest scheduled open-block state, ties earlier; no reopening finished blocks. Stage1 at seven checkpoints uses B_loc4 paired qC/qR continuations. Stage2 confirms only the localization oracle candidate with highest localization qR (ties earliest actual checkpoint) using B_eval8 disjoint contexts; observable selectors are separately frozen and share confirmation only when selecting that exact same checkpoint. Confirm qC and qR at the same candidate; canonical tau0.25, sensitivity0.125/0.25/0.5. Report selection protocol, never localization maximum as confirmation. Temporal32 alone receives dense independent B_eval8 confirmation at all seven checkpoints. Core state-observed correctness is on that seven-state grid, not every unrecorded refinement step. Primary T_last/survival comes only from dense temporal confirmation.

Official LLaDA temp0 is retained. Repeated seeds need not produce distinct outcomes; no claim of independent Bernoulli information from identical deterministic repeats. Dream source temperature0.1 and source sampling remain unchanged. Controls retain phase-faithful exact replay, matched continuation, canonical low-confidence remask, matched-count random remask, CoRe-snapshot and actual fresh compute where budget allows. NFE/harm/coverage always explicit. Frozen OOF estimator and prospective successful harm remain required before a localization claim, and cannot be replaced posthoc.

Shard target2–4h; planned upper bound6h; no multi-day job. Runtime safety factor1.25 and storage requirement2×projected bytes+50GiB on <95%-used filesystem. Budget freezes before R3 with measured8–16-item timing data, remaining exclusive GPU slots, deadline, selected N and registry hashes. T−24 no new optional scope; T−12 no scientific code/protocol changes or long GPU jobs and integrate only SEALED; T−6 submission evidence frozen and package work only.

## Metric and provenance contract

Primary quantities: reference_trajectory_accuracy, sampled_trajectory_count, sampled_failed_trajectory_count, items_with_at_least_one_failed_trajectory, confirmed_repairable_failed_trajectory_rate, repairable_but_never_correct_failed_trajectory_rate, native_recoverable_failed_trajectory_rate, mean qC/qR/Delta, temporal-subset T_last and survival. Measurement trajectory accuracy/pass@k/all-k-failed rate remain separate names. `failed_items_probed` and `base_pass_at_k` prohibited.

Complete expected seed contexts audited before submission, including all stage registries across the execution generation; intentional matched future-noise pairs only. Immutable clean execution SHA after tests and R2, exact same scientific implementation for R3. Single-writer all-shard verified merge and stage-aware seals allow LLaDA core/temporal completion to be imported without waiting for optional mechanism/localization/Dream. Unsupported bundle components are explicitly NOT_APPLICABLE_TO_THIS_STAGE and never numeric substitutes.

Latest author-level title, claim strength, interpretation and final Abstract/Conclusion remain reserved. A technical PDF build PASS is distinct from scientific submission readiness. Freeze record points to this protocol and unchanged recipes, records no R3 results seen, supersedes generation1, and is committed before GPU-heavy probes.
