# V2R Reference Design Revision — 2026-09-23

Authority: `V2R_FINAL_MASTER_REQUEST_20260923.md`. This is a new `v2r_reference` scientific generation, not a change to V2 artifacts. Freeze this document and source recipe JSONs in Git before any R3 outcome exists. An implementation correction never retroactively changes an old generation's identity.

## Scientific motivation and object

V2 used a fixed decoder for replayable counterfactual measurement, but official/reference benchmark decoding reproduction was not independently gated before primary experiments. The new question is: **Does counterfactual repairability persist under a reference-quality decoder whose baseline behavior is first independently reproduced?** Baseline reproduction is a validity prerequisite, not a fifth RQ.

The scientific unit is one sampled reference trajectory per item, trajectory_id=0. Primary denominator is sampled trajectories whose final answer is incorrect. It is not the pass@8 failed-item set or an item-level multi-sample oracle. Existing V2 is preserved as measurement-decoder evidence, whose ultimate paper role awaits the reference results and author judgment.

## Frozen task/model/source recipes

Four anchors only: GSAI-ML/LLaDA-8B-Instruct and Dream-org/Dream-v0-Instruct-7B, each on HuggingFaceH4/MATH-500 test (500 items) and openai/gsm8k main test (1319 items). No reference BBH/MBPP full reruns. Dataset/model/tokenizer revisions and source-level prompt/evaluator details are in `results/v2r_reference/reference_recipes/llada.json` and `dream.json`; the freeze commit must include these files. Full-MATH reported numbers and MATH-500 bridge numbers are NOT_DIRECTLY_COMPARABLE.

Source inspection (before R3):

* LLaDA repository ML-GSAI/LLaDA @ 9182493720ed723ef8031210d85959364e51cbe0; model/tokenizer @ 08b83a6feb34df1a6011b80c3c00c7563e963b07. Official OpenCompass recipes: GSM length/steps 256/256 block8; Math 512/512 block64; temperature0, CFG0, low-confidence sampling, EOS switches false. GSM prompt includes four fixed official demonstrations; Math official zero-shot prompt.
* Dream repository DreamLM/Dream @ 31f94a60d187e3fd481fee3bbc2c732eb94a879c; model/tokenizer @ 05334cb9faaf763692dcf9d8737c642be2b2a6ae. Official instruct eval: GSM length/steps256/256; Math512/512; entropy algorithm, temperature0.1, top_p0.9, no top_k, alg_temp0. Official zero-shot task templates.
* Bridge dataset revisions: MATH-500 6e4ed1a2a79af7d8630a6b768ec859cb5af4d3be; GSM8K 740312add88f781978c0658806c59bc2815b9866.

No score-targeting search or temperature adjustment. Official LLaDA temperature0 is deterministic: fresh branch seeds may not change outputs. B_loc/B_eval remain protocol repetitions with disjoint RNG contexts, but repeated deterministic outcomes are not independent Bernoulli observations and must not be used to fabricate binomial precision. Native qC on failed trajectories may be identically zero. Preserve null and inapplicable outcomes. The stochastic Dream regime remains distinct.

## Gate chain and bank identity

R0: source-native model/tokenizer/prompt/sampler/evaluator smoke on 16 deterministic anchor items, one trajectory/item. Verify load, completion format, special-token handling, masks exhausted, NFE, VRAM, elapsed time and bytes. Source-native full benchmark status and exact paper-dataset bridge status are separate. Never label MATH-500 as a full-MATH reproduction. R0 smoke is execution validation, not evidence of benchmark-level accuracy reproduction.

R1: apply upstream and paper evaluators to the same completions when upstream implementation is available. Save every disagreement, extraction/canonicalization and correctness. Test boxed nesting/symbolic equivalence/normalization for MATH and numeric decimal/comma normalization for GSM. Unexplained evaluator mismatches or missing official evaluator produce NEEDS_REVIEW, not PASS by convention.

R2: at least 32 fixed item IDs per task, two fixed seeds [20260923,20260924], comparing uninstrumented pinned source to instrumentation. Required 100% final token, extracted answer and correctness agreement; full update schedule and NFE consistency; checkpoints early/mid/late; RNG state equivalence. Snapshots cannot consume random numbers. Correctness against itself is not an independent upstream comparison. Native snapshot replay fidelity must also pass before continuation probes.

Only R2-passing exact code may produce the full reference bank with snapshots on first generation. Bank cardinalities are 500/1319 per backbone, one trajectory/item; baseline and R3 share the same saved trajectory IDs/token sequences/snapshots. No regeneration of a different bank for R3. Reference trajectory accuracy is pass@1; bank correctness determines failed/success pools. R0 full baseline report must distinguish execution completion from agreement with a directly comparable published result.

## RNG and deterministic selection

Design seed: 20260923. Seed registry encodes generation namespace, backbone/task, stage, item, trajectory, checkpoint, branch and paired_rng_group using an injective bounded scheme or complete collision audit before every job. The registry, its bounds and SHA256 are saved. Do not truncate hashes/modulo and assume safety. Localization, confirmation, fresh sampling, independent controls and operator-choice randomness never share a seed. Matched stochastic qC/canonical qR share future noise only through an explicit paired_rng_group. Native exact replay restores captured RNG state, not a fabricated fresh seed.

Failed pool rank is SHA256 of canonical UTF-8 JSON tuple `[20260923, backbone, task, item_id, trajectory_id]`. Sort by full hash (then IDs for a deterministic tie) and take the pre-budgeted N. Failed correctness selects the denominator; repairability outcomes never enter selection. Mechanism and temporal subsets use separate tags `mechanism` and `temporal` in the tuple and are selected from the failed pool independently of effects. Record all selected IDs and bank hash before probes. Successful-policy subset uses `policy_success`, without inspecting intervention outcomes; prospective item coverage/denominator remains explicit.

## Checkpoint grid and local phase validity

Target normalized progress: 0.125,0.250,0.375,0.500,0.625,0.750,0.875; endpoint stored as metadata. Mapping is deterministic from the source schedule, not correctness, confidence or repairability. Use the closest valid state having an open refinement phase with at least one scheduled committed position and at least one remaining refinement step; ties choose the earlier step. Record target progress, actual integer step and actual normalized progress. Deduplicate any coincident mapped states and report the mapping.

For semi-autoregressive LLaDA, completed blocks cannot be reopened. Exact normalized grid points coincide with completed-block boundaries in the source recipes; therefore the nearest active-phase state is immediately before the boundary (Math63/512 for target0.125, GSM31/256 for target0.125). This pre-result rule avoids silently changing block semantics. The terminal endpoint is never a local-remask checkpoint. Dream valid states follow its pinned native time schedule and terminal handling, with no extra posthoc refinement steps.

## Budget-only sample-size rule and sharding

Measure 8–16 item timing pilot (the 16-item R0/R2 measurements may supply it): seconds/base trajectory, seconds/checkpoint continuation, seconds/branch, output bytes/item, NFE and VRAM. Reserve baseline, R2 and P0 requirements first. Choose largest N up to target that fits measured remaining GPU-hours and completion before T-12, using a 1.25 runtime safety factor and storage reserve; no qR/effect input accepted by the planner. If minimum cannot fit, mark BUDGET_BELOW_MINIMUM and report a concrete resource/priority decision; never silently call a smaller exploratory subset primary.

LLaDA core target128/min64 failed trajectories per task; Dream target64/min32. LLaDA mechanism and temporal target64/min32 each. Selection cardinality is also bounded by available failed pool; shortage is explicitly reported. Freeze measured timing, available slots/hours, chosen N and complete calculation in the run manifest before R3. Do not increase/decrease N after viewing repairability outcomes.

Each shard targets 2–6h, maximum8h. Deterministic contiguous assignment over sorted stable item IDs is allowed; assignment hash, expected IDs and no duplicates/no omissions are required. Shard-local atomic item completion supports resume only for exactly matching fingerprint. Raw snapshots remain on the execution server; central index records server, absolute path, size, SHA256, mtime, execution SHA and config SHA. Compact transfers require hash verification. Git contains no large raw artifacts.

## R3 definitions and controls

At each selected state record observed correctness o_t and local eligibility. Localization B_loc=4 estimates qC and canonical qR; confirmation B_eval=8 uses disjoint contexts. Canonical tau_confirm=0.25; sensitivity0.125/0.25/0.5. Delta_R=qR-qC with paired future noise for stochastic continuations. Operational confirmed state requires confirmation qR≥threshold; no assumption of temporal monotonicity.

Canonical operator retains V2 semantics: low_confidence_remask_v2, remask_fraction0.25, minimum4 bounded by eligible positions, anchor confidence0.80, same base temperature and phase-faithful continuation. Within the active block only, deterministic low-confidence ordering, no hyperparameter changes based on outcomes. Phase-inapplicable states are reported as such and not silently dropped from failed-trajectory denominator. Repaired tokens must be completed within a documented valid native continuation schedule; replay and branch NFE must be explicit.

Core primary metrics: confirmed_repairable_failed_trajectory_rate; repairable_but_never_correct_failed_trajectory_rate; native_recoverable_failed_trajectory_rate; mean q_C, mean q_R, mean Delta_R; T_last^R; repairability survival. Declare whether each estimate uses all-grid confirmation or independently confirmed localization-selected checkpoint; never use a localization maximum as confirmed evidence. Never-correct means no observed-correct state on the saved predeclared observation grid (not an assertion about unobserved continuous states).

Temporal LLaDA subset independently confirms every grid checkpoint, reports T_last, survival, qC(t),qR(t),Delta(t), retaining non-monotonic curves. Mechanism LLaDA subset compares exact native replay, matched stochastic continuation, canonical low-confidence remask, paired-count random-position remask, CoRe-snapshot (official UCF-CRCV/CoRe@524e01e11a8751afb67b81a2c930f938faf9a70e adaptation, not full CoRe reproduction), actual freshly decoded sampling with measured NFE. Report failed recovery, intervention lift, harm, modified positions and NFE. Harm requires separately frozen successful-trajectory controls; failed-only mechanism rows cannot support a harm estimate. Fresh sampling cannot use an analytic proxy.

## RQ3 and prospective policy

Retain frozen V2 observable state-value estimator/features and grouped item-level OOF recipe; do not choose a replacement after observing reference performance. Five item-grouped folds, no held-out item outcome in fitting/selection. Evaluate one base trajectory per item, selected-checkpoint intervention, prospective trajectory accuracy delta including harm on original successes. If successful-policy evaluation uses a deterministic subset, report stratum counts/coverage and a prespecified weighted population estimate with uncertainty; do not present subset accuracy as full-bank accuracy. Oracle/selector gap uses independent confirmation, never localization maxima. A frozen estimator whose artifact/version cannot be recovered blocks RQ3 primary claims.

## Metrics, provenance, priorities and paper

V2R prohibits `base_pass_at_k` and `failed_items_probed`. Distinguish reference_trajectory_accuracy, measurement_trajectory_accuracy, pass_at_k, all_k_failed_item_rate, sampled_trajectory_count, sampled_failed_trajectory_count, items_with_at_least_one_failed_trajectory. NFE includes operator forwards and continuation; native exact replay is a fidelity control distinct from qC.

Single controller merges only after all expected shards DONE with matching start execution SHA, config SHA, model/tokenizer revision, dataset hash, seed registry, counts, unique complete IDs and verified artifact hashes. Any violation is AGGREGATION_BLOCKED. Execution worktree immutable during jobs; finalization SHA is separate. Seals bind gate evidence and provenance. Gate failure is NEEDS_REVIEW and never auto-tuned to a score.

Priority P0: both backbones' R0/R1/R2, LLaDA full MATH/GSM banks, LLaDA core, temporal and basic controls. P1: Dream banks/core, OOF localization, actual fresh controls. P2 breadth/operators/seeds cannot occupy needed P0 slots. At T-24 no new P2; at T-12 no new scientific protocol/code or long GPU jobs; at T-6 submitted evidence freezes. No active job auto-kill. Final deadline Sep26 20:59 KST (official Sep25 23:59 AoE).

Paper integrates only SEALED reference numbers. Prepared tables: reference baseline/existence; LLaDA mechanism; prospective localization. Existing V2 decoder-regime comparison stays distinct. Title retaining “When Does ...” requires SEALED LLaDA temporal evidence; record readiness flag, never change title automatically. Abstract/Conclusion final wording, claim strength, mechanism/decoder/generalization interpretation are author decisions.

## Freeze record

The first Git commit containing this complete document and both pinned recipe JSONs is the design freeze. `status/v2r/design_freeze.json` records that immutable commit, file hashes, freeze time and `r3_results_observed=false`. Code/test commits may follow; any protocol change requires a separately named design/execution generation, never mutation of an active execution tree. Chosen N remains PENDING_TIMING until budget-only evidence exists; R3 submission is blocked until its additional budget/subset manifest is frozen.
