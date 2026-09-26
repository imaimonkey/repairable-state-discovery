# Phase 2B storage reservation report

Storage was measured directly with `df -h`, `df -i`, and artifact-level `du`; no blind 200 GiB rule was applied. The observed legacy V2 execution root is approximately 2.0 GiB and the reference root approximately 606 MiB. The largest observed 250-item run is 264,097,041 bytes, giving an observed upper-bound unit of about 1.056 MiB/item including its current probe/report files.

Extrapolating only the known MATH-500 (500), GSM8K (1319), and three BBH logical tasks (750) gives about 2.71 GB for one measured-format bank and about 8.13 GB for a three-copy temporary/counterfactual high-water estimate. MBPP, Dream, model caches, and any larger raw format are explicitly not included; a provisional reservation should therefore be at least 15 GB above current usage and must be revisited after those measurements.

| Server | Candidate free space | Reservation | Gate |
|---|---:|---|---|
| server1 | `/` 297G; `/mnt/raid5` 204G, both 83/99% used | none | FAIL |
| server2 | `/` 19G; `/mnt/raid5` 224G, both 99% used | none | FAIL |
| server3 | `/` 77G; `/data` 115G, 96/99% used | none | FAIL |
| server4 | `/` 99G; `/data` 83G, 95/99% used | none | FAIL |

No cleanup candidate was deleted. Candidate metadata, ownership, source SHA, artifact status, references, recoverability, and recommendations are in `status/rsd/storage_status.json`.

The small server1 GPU calibration was stored separately in its canonical calibration worktree and completed at approximately 18 MiB for 64 item evidence files plus the gate report. This calibration artifact is retained as qualification evidence and does not count as a full-run reservation. Full scientific execution remains independently blocked at `STORAGE_NOT_RESERVED`; no large raw or confirmatory execution is authorized.

The Phase 2A runtime safety gate still requires an approved reservation with at least 200 GiB free and 10% inode margin before raw execution. The measured projection above is the empirical planning estimate; it does not override that safety gate. Therefore no server is marked `STORAGE_PASS` in this phase.
