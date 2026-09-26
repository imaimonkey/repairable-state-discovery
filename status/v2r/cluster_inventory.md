# V2R cluster inventory

2026-09-26T16:50:56.573793+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | ['0', '3', '4', '5', '6', '7'] | ['/tmp', '/var/tmp'] |

server1 `/`: 316774973440 available bytes; 82.33% used; 112451696 free inodes.

server1 `/home`: 316774973440 available bytes; 82.33% used; 112451696 free inodes.

server1 `/tmp`: 316774973440 available bytes; 82.33% used; 112451696 free inodes.

server1 `/var/tmp`: 316774973440 available bytes; 82.33% used; 112451696 free inodes.

server1 `/mnt/raid5`: 654089043968 available bytes; 97.00% used; 337531235 free inodes.
| server2 | True | ['2', '7'] | [] |

server2 `/`: 18024759296 available bytes; 98.99% used; 110367561 free inodes.

server2 `/home`: 18024759296 available bytes; 98.99% used; 110367561 free inodes.

server2 `/tmp`: 18024759296 available bytes; 98.99% used; 110367561 free inodes.

server2 `/var/tmp`: 18024759296 available bytes; 98.99% used; 110367561 free inodes.

server2 `/mnt/raid5`: 606592401408 available bytes; 95.81% used; 444970563 free inodes.
| server3 | True | ['0'] | [] |

server3 `/`: 81274155008 available bytes; 95.46% used; 114065353 free inodes.

server3 `/home`: 81274155008 available bytes; 95.46% used; 114065353 free inodes.

server3 `/data`: 1349288497152 available bytes; 81.35% used; 225829477 free inodes.

server3 `/tmp`: 81274155008 available bytes; 95.46% used; 114065353 free inodes.

server3 `/var/tmp`: 81274155008 available bytes; 95.46% used; 114065353 free inodes.
| server4 | True | ['0', '2', '3', '4', '5', '7'] | ['/tmp', '/var/tmp'] |

server4 `/`: 105953054720 available bytes; 94.09% used; 114347873 free inodes.

server4 `/home`: 105953054720 available bytes; 94.09% used; 114347873 free inodes.

server4 `/data`: 410526871552 available bytes; 94.33% used; 224824569 free inodes.

server4 `/tmp`: 105953054720 available bytes; 94.09% used; 114347873 free inodes.

server4 `/var/tmp`: 105953054720 available bytes; 94.09% used; 114347873 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
