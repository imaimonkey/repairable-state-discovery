# ICLR 2027 V2R dynamic dispatch

Updated: `2026-09-23T19:29:41.015599+00:00`; next inventory interval: `90s`.

This is a read-only placement decision. It does not cancel, preempt, or delete jobs/artifacts.

| Server | Observed | Idle GPUs | Safe FS | Reference compatible | Eligible | Reasons |
|---|---:|---|---|---:|---:|---|
| server1 | True | ['4', '7'] | ['/tmp', '/var/tmp', '/mnt/raid5'] | False | False | exact_native_replay_failed |
| server2 | True | ['6', '7'] | [] | False | False | no_safe_filesystem |
| server3 | True | [] | ['/tmp', '/var/tmp'] | True | False | no_idle_gpu_candidate |
| server4 | True | ['0', '1', '2', '3', '4', '5', '6'] | ['/tmp', '/var/tmp'] | False | False | exact_native_replay_failed;_reference_torch_2_1_2_is_sm120_incompatible |

**Next batch:** `WAIT_WITH_INTERVAL_REPLAN` — No server currently passes the combined observation, storage, GPU, and reference-runtime gates.

Running reference jobs: `2`; pending/configuring: `6`.
