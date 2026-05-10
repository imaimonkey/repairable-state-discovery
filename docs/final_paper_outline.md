# Final Paper Outline

## Working Title

- `Repairable States in Diffusion Reasoning Trajectories`
- `Localizing Repairable Intermediate States in Diffusion Language Models`
- `A Protocol for Measuring State-Level Repairability in Diffusion Reasoning`

## Core Claim

This paper does not primarily propose a new self-correction method. Its main contribution is a protocol for measuring whether failed diffusion reasoning trajectories contain recoverable intermediate states, where those states occur, and how well a lightweight predictor can select them without oracle intervention.

## Recommended Contribution List

1. We formalize `state-level repairability` as a measurable property of diffusion reasoning trajectories.
2. We introduce an oracle repair protocol that localizes where failed trajectories can be recovered.
3. We evaluate practical step selection with a lightweight predictor and quantify the `predictor-oracle gap`.
4. We show that repair gain must be interpreted jointly with `negative repair`, exposing a nontrivial accuracy-safety tradeoff.

## Paper Structure

### 1. Introduction

- Motivation: diffusion LMs expose rich intermediate states, but existing work mainly studies their existence or exploits them heuristically.
- Gap: prior work rarely measures recoverability of failed trajectories at the state level.
- Thesis: failed diffusion trajectories often contain localized, measurable, and partially predictable repairable states.

### 2. Related Work

- Intermediate-state analysis in diffusion LMs
- Self-correction / remasking methods for diffusion LMs
- Test-time selection / reranking / trajectory stitching

### 3. State-Level Repairability Protocol

- Trajectory collection
- Checkpoint extraction
- Oracle repair from snapshot
- Predictor-based step selection
- Negative repair measurement
- Aggregate metrics

### 4. Experimental Setup

- Models
- Datasets
- Repair operator
- Predictor features
- Evaluation metrics

### 5. Main Results

- GSM8K final
- MATH500 final diffusion result
- MATH500 robustness variants
- AR baseline as reference, not primary object of analysis

### 6. Analysis

- Where repairability concentrates across steps
- How much predictor recovers relative to oracle
- Tradeoff between gain and negative repair
- Case studies

### 7. Discussion

- What current results support
- What they do not yet support
- Why protocol-level measurement matters for future diffusion decoding research

### 8. Limitations

- Incomplete backbone diversity
- Limited dataset breadth
- Predictor still lags oracle on harder settings
- Negative repair remains nontrivial

## Where Current Results Fit

### Already strong enough for draft

- Problem framing
- Method section
- GSM8K final results
- MATH500 diffusion-only result
- MATH500 robustness analysis
- Oracle / predictor / negative repair interpretation

### Still missing for submission-quality final version

- Full `protocol_math500_final` completion
- Aggregate final/submission tables
- Multi-seed confidence intervals
- Stronger ablations
- At least one additional backbone or dataset if possible

## How to Use AR Baselines

- Present AR baselines as a standard performance reference.
- Explicitly say they are not the primary object of analysis.
- Use them to contextualize practical headroom, not to define the main novelty.

Suggested phrasing:

`We include AR baselines as a standard performance reference. Our central question is not whether diffusion currently outperforms strong AR models, but whether failed diffusion trajectories contain measurable and localizable repairable states.`

## Tables To Include

### Table 1. Main diffusion repairability summary

- dataset
- model
- pass@1
- pass@k
- predictor repaired pass@k
- predictor gain
- oracle-predictor gap
- peak step
- repairable failed rate
- negative repair

### Table 2. AR baseline reference

- dataset
- model
- pass@1
- pass@k

### Table 3. Robustness variants

- variant
- base pass@k
- predictor repaired pass@k
- oracle repaired pass@k
- negative repair
- peak step

## Figures To Include

1. Protocol overview diagram
2. Repair gain curve across checkpoint step
3. Best-step histogram
4. Predictor vs oracle repaired pass@k
5. Gain vs negative-repair tradeoff plot

## Immediate Writing Plan

1. Write Introduction, Related Work, and Method now.
2. Draft Results with currently available GSM8K and robustness outputs.
3. Use the regenerated final aggregate for MATH500/GSM8K comparison.
4. Add confidence intervals, ablations, and qualitative examples before submission.

## Immediate Experiment Plan

1. Add seed-repeat runs and bootstrap confidence intervals.
2. Add predictor feature ablations.
3. Add negative-repair mitigation ablations.
4. Add at least one more diffusion backbone or dataset if resources allow.
