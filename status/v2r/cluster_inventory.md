# V2R cluster inventory

2026-09-26T03:58:52.028199+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | ['1', '4', '5', '6', '7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 318414381056 available bytes; 82.24% used; 112476264 free inodes.

server1 `/home`: 318414381056 available bytes; 82.24% used; 112476264 free inodes.

server1 `/tmp`: 318414381056 available bytes; 82.24% used; 112476264 free inodes.

server1 `/var/tmp`: 318414381056 available bytes; 82.24% used; 112476264 free inodes.

server1 `/mnt/raid5`: 330952327168 available bytes; 98.48% used; 337545661 free inodes.
| server2 | True | [] | [] | reference_compatible=False |

server2 `/`: 22931312640 available bytes; 98.72% used; 110406196 free inodes.

server2 `/home`: 22931312640 available bytes; 98.72% used; 110406196 free inodes.

server2 `/tmp`: 22931312640 available bytes; 98.72% used; 110406196 free inodes.

server2 `/var/tmp`: 22931312640 available bytes; 98.72% used; 110406196 free inodes.

server2 `/mnt/raid5`: 286417358848 available bytes; 98.02% used; 445051676 free inodes.
| server3 | True | [] | [] | reference_compatible=True |

server3 `/`: 84672040960 available bytes; 95.27% used; 114177813 free inodes.

server3 `/home`: 84672040960 available bytes; 95.27% used; 114177813 free inodes.

server3 `/data`: 124601454592 available bytes; 98.28% used; 225820436 free inodes.

server3 `/tmp`: 84672040960 available bytes; 95.27% used; 114177813 free inodes.

server3 `/var/tmp`: 84672040960 available bytes; 95.27% used; 114177813 free inodes.
| server4 | True | ['2', '3', '7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 105851052032 available bytes; 94.09% used; 114347416 free inodes.

server4 `/home`: 105851052032 available bytes; 94.09% used; 114347416 free inodes.

server4 `/data`: 109775282176 available bytes; 98.48% used; 224929551 free inodes.

server4 `/tmp`: 105851052032 available bytes; 94.09% used; 114347416 free inodes.

server4 `/var/tmp`: 105851052032 available bytes; 94.09% used; 114347416 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
