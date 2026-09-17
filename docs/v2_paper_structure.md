# V2 Paper Structure

This outline is subordinate to `docs/v2_scientific_contract.md` and exists to keep experiments, analysis, and manuscript structure aligned.

## Title

**When Does Diffusion Reasoning Become Irrecoverable? Repairable States in Diffusion Language Models**

## Abstract logic

1. Final failure is only an endpoint observation.
2. DLMs expose intermediate refinement states.
3. Define state-level recoverability operationally through native continuation and controlled intervention.
4. Separate transient correctness, native recoverability, and intervention-conditioned recoverability.
5. Evaluate existence, source, non-oracle localization, harm, compute, and generalization.
6. State conclusions only at the operator/checkpoint/budget scope supported by V2.

Do not claim a universal intrinsic point of irrecoverability.

## Section 1 — Introduction

Hook: final failure tells where a trajectory ended, not whether failure was inevitable.

Motivate the distinction:
- observed intermediate correctness
- native continuation recoverability
- intervention-enabled recoverability

Contributions:
1. formalization of counterfactual state-level recoverability;
2. controlled measurement protocol separating continuation from intervention;
3. empirical localization/generalization with harm and compute accounting.

## Section 2 — Related Work

Organize by scientific adjacency rather than model chronology:
- diffusion language models and iterative decoding;
- remasking/revision and inference-time correction;
- temporal dynamics and intermediate-state analysis;
- intermediate-state reuse/test-time reasoning.

The novelty sentence should emphasize ultimately failed trajectories, counterfactual state-level measurement, native-continuation controls, and non-oracle localization rather than simply using intermediate states.

## Section 3 — Formalizing State-Level Recoverability

Define:
- `o_t`
- `q_C(x_t)`
- `q_R(x_t)`
- `Delta_R(x_t)`
- `T_last^R`

State clearly that recoverability is operator/checkpoint/budget/evaluator relative.

## Section 4 — Measurement Protocol

Describe:
- canonical trajectory bank;
- faithful decoder-state snapshots;
- native continuation;
- fixed-operator stochastic replicates;
- localization/confirmation branch split;
- negative intervention on successful trajectories;
- OOF state-value estimation;
- prospective policy evaluation;
- NFE accounting and fresh-sampling control.

## Section 5 — Experimental Setup

Deep anchor:
- LLaDA × MATH-500
- LLaDA × GSM8K

Thin validation:
- LLaDA × predeclared BBH structured reasoning
- LLaDA × MBPP
- Dream × MATH-500/GSM8K

Direct operator controls:
- native continuation
- matched stochastic continuation
- random-position remask
- canonical low-confidence remask
- CoRe
- optional DecoCal

Compute control:
- actual fresh sampling

## Section 6 — Results

### 6.1 Does recoverability exist beyond transient correctness?
Main Table 1 + recoverability landscape.

### 6.2 What creates recovery?
Main Table 2. Compare `q_C`, `q_R`, `Delta_R`, harm, modified tokens, and NFE.

### 6.3 Can recoverability be localized without oracle outcomes at inference time?
Main Table 3. Simple temporal/state selectors vs grouped-OOF state-value estimator vs independently evaluated oracle.

### 6.4 Does the phenomenon generalize?
Cross-domain/backbone summary; preserve negative/inconsistent cases.

## Section 7 — Analysis

- non-monotonic recoverability and last-repairable survival;
- block/decoder-phase effects;
- overlap between operators;
- repairable-but-never-correct trajectories;
- recovery/harm/compute frontier;
- qualitative state transitions.

## Section 8 — Limitations

Expected remaining limitations:
- finite operator family;
- finite branch estimates;
- discrete checkpoint resolution;
- two diffusion model families;
- operational, not causal, interpretation of reasoning state.

## Main-paper artifacts

Only three main tables and three main figures unless an additional artifact is necessary to resolve a headline claim.

Appendix by default:
- AR reference rows;
- seed/stride/branch-count robustness;
- feature ablations;
- operator hyperparameter sensitivity;
- extended qualitative examples;
- implementation/reproducibility detail.
