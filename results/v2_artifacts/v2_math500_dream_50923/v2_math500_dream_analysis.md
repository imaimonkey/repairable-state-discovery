# Dream-MATH-500 V2 Result Analysis

## Status

- Run: `v2_math500_dream`
- Seal: `SEALED`
- SHA: `8b1361d3d8d60a58e28847ac35af8dfc2b023d2d`
- Scientific fingerprint: `53add4744716f3c5d0b941deee82a7773ca9bc46988082cfc7790c3d9ebdb7b7`

## Headline

| Metric | Value |
|---|---:|
| Items | 500 |
| Trajectories | 4000 |
| Base pass@k | 0.4000 |
| Prospective selector | `oof_state_value` |
| Prospective policy pass@k | 0.3982 |
| Prospective net gain | -0.0018 |
| Probe branch rows | 106872 |

## Existence

| Measure | Count | Rate |
|---|---:|---:|
| Failed items probed | 497 | 100.0000% |
| Transiently correct | 23 | 4.6278% |
| Confirmed repairable | 105 | 21.1268% |
| Repairable but never correct | 87 | 17.5050% |

## Selector Diagnostics

| Selector | Prospective pass@k | Net gain | Diagnostic recovery | Delta vs native | Harm | Coverage |
|---|---:|---:|---:|---:|---:|---:|
| confidence_low | 0.4002 | 0.0002 | 0.0761 | 0.0227 | 0.3972 | 0.9980 |
| earliest_eligible | 0.4007 | 0.0007 | 0.0811 | 0.0241 | 0.4052 | 1.0000 |
| entropy_high | 0.4007 | 0.0007 | 0.0811 | 0.0244 | 0.4052 | 1.0000 |
| mask_ratio | 0.4007 | 0.0007 | 0.0811 | 0.0241 | 0.4052 | 1.0000 |
| normalized_midpoint | 0.3990 | -0.0010 | 0.0171 | 0.0098 | 0.0887 | 1.0000 |
| normalized_quarter | 0.4002 | 0.0002 | 0.0528 | 0.0156 | 0.2137 | 1.0000 |
| normalized_three_quarter | 0.3997 | -0.0003 | 0.0054 | 0.0053 | 0.0343 | 1.0000 |
| oof_state_value | 0.3982 | -0.0018 | 0.0140 | 0.0045 | 0.0887 | 1.0000 |
| oracle_localization | 0.4238 | 0.0237 | 0.0993 | 0.0420 | 0.0665 | 1.0000 |
| random_checkpoint | 0.4000 | 0.0000 | 0.0269 | 0.0104 | 0.1014 | 0.8680 |

## Operator Summary

| Stage | Operator | Rows | Correct | Recovery on base failures | Harm on base successes | Applicable |
|---|---|---:|---:|---:|---:|---:|
| confirmation | low_confidence_remask_v2 | 28344 | 26.4753% | 4.6721% | 21.7927% | 97.5727% |
| confirmation | matched_stochastic_continuation | 28344 | 26.2701% | 3.2752% | 18.9112% | 100.0000% |
| fidelity | native_continuation | 5576 | 28.6944% | 0.0000% | 0.0000% | 100.0000% |
| localization | low_confidence_remask_v2 | 22304 | 26.1324% | 3.6792% | 18.0714% | 87.5000% |
| localization | matched_stochastic_continuation | 22304 | 26.3540% | 2.3642% | 14.0312% | 100.0000% |

## Interpretation

- The sealed Dream-MATH run is ready for per-run analysis.
- The frozen `oof_state_value` estimate is 0.3982, versus base 0.4000; the observed difference is -0.0018.
- 105 of 497 initially failed items meet the confirmation threshold for repairability.
- These results support a Dream-MATH existence/repairability analysis, but not a final eight-run or cross-backbone claim.
- Fresh compute control is disabled in the frozen configuration, so no independent compute-matched control comparison is available for this run.

## Caveats

- Single Dream-MATH-500 run; not the final eight-run aggregate.
- Prospective policy is estimated from frozen confirmation branches, not a fresh independent test run.
- Fresh compute control is disabled in the frozen Dream configuration.
- Dream uses hotfix SHA 8b1361d; cross-run aggregation must preserve per-run SHA provenance.
