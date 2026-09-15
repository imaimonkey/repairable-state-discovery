# Predictor Method

The predictor is an approximate selector for repairable intermediate states. It is not trained to solve the original reasoning problem. It is trained to imitate the oracle localization signal produced by the repair probe.

## Supervision

For each failed trajectory, oracle repair probes every eligible checkpoint. A checkpoint receives a correction rate:

```text
r(i, t, s) = correct_repair_branches(i, t, s) / total_repair_branches
```

where `i` is the item, `t` is the trajectory, and `s` is the checkpoint step.

For each failed trajectory `(i, t)`, checkpoints are sorted by `r(i, t, s)`. The top `top_k_label` checkpoints are labeled positive:

```text
y(i, t, s) = 1 if s is among the top-k oracle repair checkpoints for trajectory (i, t)
y(i, t, s) = 0 otherwise
```

The current final configs use `top_k_label: 2`.

## Features

Each checkpoint is represented by state-level features computed before repair:

| Feature | Meaning |
| --- | --- |
| `step_norm` | checkpoint step divided by total refinement steps |
| `masked_ratio` | fraction of tokens still masked |
| `commitment_ratio` | fraction of tokens already committed/unmasked |
| `state_token_conf_mean` | mean confidence over state tokens |
| `state_token_conf_min` | minimum state-token confidence |
| `masked_entropy_mean` | mean entropy over masked-token predictions |
| `masked_entropy_max` | maximum masked-token entropy |
| `answer_disagreement` | disagreement among answer candidates at the same item and step |
| `candidate_change_rate` | whether the answer candidate changed from the previous checkpoint |

These features intentionally avoid using oracle branch outcomes at inference time.

## Model

The predictor is logistic regression with median imputation and standard scaling:

```text
p(y=1 | x) = sigmoid(w^T z(x) + b)
```

where `x` is the raw checkpoint feature vector and `z(x)` is the imputed, standardized feature vector.

## Leakage-free evaluation

Claim-bearing selector scores use **item-grouped cross-fitting** rather than scoring the same supervised item with a model that was trained on it.

For each fold, all checkpoints from held-out item IDs are excluded from that fold's fit. Every supervised item is scored only by the model for the fold in which that item is held out:

```text
train_items(fold) intersect test_items(fold) = empty
```

The cross-fit out-of-fold scores are the scores used by the selector evaluation. A separate final logistic-regression model is fit on all supervised items and stored in `repair_predictor.pkl` only as the deployment artifact; it is not used to report performance on items that contributed supervision.

Items that contain no supervised failed-state rows are genuinely unseen by the final fit and may be scored by that final deployment model. The predictor JSON records `score_source` for every checkpoint so this distinction is auditable.

Reported predictor accuracy and ROC-AUC are computed over the concatenated out-of-fold supervised rows.

## Inference

For each trajectory, the predictor scores all eligible checkpoints and selects the highest-scoring checkpoint:

```text
s_hat(i, t) = argmax_s p(y=1 | x(i, t, s))
```

Threshold/abstention variants repair only when:

```text
max_s p(y=1 | x(i, t, s)) >= threshold
```

This produces the `predictor@0.50`, `predictor@0.70`, and `predictor@0.90` rows in extended analysis.

## Net policy evaluation

A recovery-only metric can overstate a deployable repair policy because it counts newly repaired failures while treating already-correct trajectories as permanently correct. The main evaluation therefore separates:

- `recovery_only_expected_item_pass_at_k`: historical recovery-only metric;
- `negative_repair_rate`: probability that selected repair damages an originally correct trajectory;
- `net_expected_item_pass_at_k`: expected item pass@k after applying the same selector to both failed and originally correct trajectories;
- `net_policy_gain_over_base_pass_at_k`: net expected pass@k minus base pass@k.

For a trajectory selected for repair, failed trajectories use the selected checkpoint's correction rate and originally correct trajectories use its preservation rate. Item-level pass@k is then recomputed across all trajectories.

`net_expected_item_pass_at_k` is reported only when the oracle artifact contains repair probes for **all** originally successful trajectories as well as all failed trajectories. Slice runs with capped negative-repair probing remain useful for diagnosis but are not allowed to masquerade as complete net-policy evaluation.

## Interpretation

The predictor approximates oracle checkpoint localization from cheap state signals. A high ROC-AUC means the features separate oracle-top checkpoints from other checkpoints under the top-k label. It does not guarantee maximal repaired pass@k because the final metric is item-level expected recovery under selected repair, and it is affected by repair branch stochasticity, abstention, and negative repair on already-correct trajectories.

The paper-level selector claim should therefore use cross-fit scores and net policy metrics. Recovery-only results remain measurement evidence for state repairability, not sufficient evidence for a safe deployable selector.
