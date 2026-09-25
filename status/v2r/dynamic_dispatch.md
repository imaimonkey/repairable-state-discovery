# ICLR 2027 V2R dynamic dispatch

Updated: `2026-09-25T23:13:54.725098+00:00`; next inventory interval: `90s`.

This is a read-only placement decision. It does not cancel, preempt, or delete jobs/artifacts.

| Server | Observed | Idle GPUs | Safe FS | Reference compatible | Eligible | Reasons |
|---|---:|---|---|---:|---:|---|
| server1 | True | ['4', '6', '7'] | ['/tmp', '/var/tmp'] | False | False | exact_native_replay_failed |
| server2 | True | ['2'] | [] | False | False | no_safe_filesystem, exact_native_replay_failed;_safe_scratch_is_non_authoritative |
| server3 | True | [] | [] | True | False | no_idle_gpu_candidate, no_safe_filesystem |
| server4 | True | ['3', '7'] | ['/tmp', '/var/tmp'] | False | False | exact_native_replay_failed;_reference_torch_2_1_2_is_sm120_incompatible |

**Next batch:** `WAIT_WITH_INTERVAL_REPLAN` — No server currently passes the combined observation, storage, GPU, and reference-runtime gates.

Running reference jobs: `0`; pending/configuring: `7`.
