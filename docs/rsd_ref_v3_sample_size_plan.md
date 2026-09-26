# RSD Generation 3 Sample-Size and Resource Plan

Status: **FROZEN RESOURCE-ONLY PLAN; NO CONFIRMATORY OUTCOMES OBSERVED**

The prior pilot signal, including the observed roughly 3–5% repairability range, is planning evidence only. It is not pooled into Generation 3 estimates and cannot be used to change the plan after outcomes are observed.

## Frozen targets

| Purpose | Target per primary task | Minimum if resource shortage | Unit |
|---|---:|---:|---|
| Core existence/repairability | 256 | 128 | failed base trajectories |
| Temporal confirmation | 128 | 64 | failed base trajectories |
| Mechanism controls | 128 | 64 | failed base trajectories |
| Successful-trajectory harm | 128 | 64 | source-native correct trajectories |

The target is selected before confirmatory outcomes. If the frozen failed pool is smaller than the target, the run records `NEEDS_REVIEW` and reports the actual denominator; it does not substitute MATH-500, a different task, or an outcome-selected population.

## Precision rationale

For a planning prevalence near 0.05, a two-sided 95% binomial interval with half-width near 0.025 requires roughly 292 independent units under a simple normal approximation. The frozen core target of 256 is therefore a resource/precision compromise, not a promise of a particular interval width. Exact or Wilson intervals are reported from the observed denominator. Paired qC/qR comparisons use item-level paired differences and bootstrap intervals rather than treating deterministic decoder repetitions as independent Bernoulli observations.

## Resource-only selection rule

Before any confirmatory outcome is inspected, measure an 8–16 item server1 timing and artifact pilot for the exact source-native recipe. For each purpose, calculate:

```text
time_capacity = floor(usable_gpu_hours * 3600 / (1.25 * seconds_per_item))
storage_capacity = floor((reserved_bytes - safety_margin_bytes) / (2 * bytes_per_item))
selected_n = min(predeclared_target, failed_pool_size, time_capacity, storage_capacity)
```

The runtime safety factor is 1.25. The storage calculation includes the base bank, counterfactual branch artifacts, temporary merge/seal high-water mark, and retention copy. A filesystem at or above 95% use is ineligible even if its nominal free-byte count is large.

## Branch budget

The base bank uses one trajectory per item. Counterfactual branch budgets are recorded separately:

- `B_loc=4` for localization when stochastic continuation is meaningful;
- `B_eval=8` disjoint confirmation branches;
- deterministic temperature-0 repeats are exact confirmations, not independent trials;
- temporal and mechanism subsets use their own frozen selection-purpose hash namespaces;
- successful harm control uses a deterministic hash-ranked subset independent of intervention outcomes.

## Reporting requirements

Every report must include the raw count, denominator, item/trajectory unit, branch count, source/GPU stratum, interval method, paired difference, NFE, and whether a result is deterministic confirmation or stochastic estimation. No pilot result, legacy V2 result, or MATH-500 calibration result may enter a Generation 3 confirmatory denominator.
