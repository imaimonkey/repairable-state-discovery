# V2R cluster inventory

2026-09-26T17:21:26.425911+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | ['0', '3', '4', '5', '6', '7'] | ['/tmp', '/var/tmp'] |

server1 `/`: 315620651008 available bytes; 82.39% used; 112445844 free inodes.

server1 `/home`: 315620651008 available bytes; 82.39% used; 112445844 free inodes.

server1 `/tmp`: 315620651008 available bytes; 82.39% used; 112445844 free inodes.

server1 `/var/tmp`: 315620651008 available bytes; 82.39% used; 112445844 free inodes.

server1 `/mnt/raid5`: 645847158784 available bytes; 97.04% used; 337467118 free inodes.
| server2 | True | ['2', '7'] | [] |

server2 `/`: 18024173568 available bytes; 98.99% used; 110367560 free inodes.

server2 `/home`: 18024173568 available bytes; 98.99% used; 110367560 free inodes.

server2 `/tmp`: 18024173568 available bytes; 98.99% used; 110367560 free inodes.

server2 `/var/tmp`: 18024173568 available bytes; 98.99% used; 110367560 free inodes.

server2 `/mnt/raid5`: 605801058304 available bytes; 95.81% used; 444969982 free inodes.
| server3 | True | [] | [] |

server3 `/`: 81274839040 available bytes; 95.46% used; 114065342 free inodes.

server3 `/home`: 81274839040 available bytes; 95.46% used; 114065342 free inodes.

server3 `/data`: 1349219508224 available bytes; 81.35% used; 225836329 free inodes.

server3 `/tmp`: 81274839040 available bytes; 95.46% used; 114065342 free inodes.

server3 `/var/tmp`: 81274839040 available bytes; 95.46% used; 114065342 free inodes.
| server4 | True | ['0', '2', '3', '4', '5', '7'] | ['/tmp', '/var/tmp'] |

server4 `/`: 105952333824 available bytes; 94.09% used; 114347873 free inodes.

server4 `/home`: 105952333824 available bytes; 94.09% used; 114347873 free inodes.

server4 `/data`: 410519068672 available bytes; 94.33% used; 224824484 free inodes.

server4 `/tmp`: 105952333824 available bytes; 94.09% used; 114347873 free inodes.

server4 `/var/tmp`: 105952333824 available bytes; 94.09% used; 114347873 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
