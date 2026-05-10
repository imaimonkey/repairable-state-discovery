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

Training uses grouped train/test splitting by item id so checkpoints from the same item do not appear in both train and test partitions:

```text
train_items intersect test_items = empty
```

The reported predictor metrics are item-grouped held-out accuracy and ROC-AUC over checkpoint labels.

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

## Interpretation

The predictor approximates oracle checkpoint localization from cheap state signals. A high ROC-AUC means the features separate oracle-top checkpoints from other checkpoints under the top-k label. It does not guarantee maximal repaired pass@k because the final metric is item-level expected recovery under selected repair, and it is affected by repair branch stochasticity, abstention, and negative repair on already-correct trajectories.
