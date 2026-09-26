# V2R cluster inventory

2026-09-26T19:55:26.447086+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | ['0', '3', '4', '5', '6', '7'] | ['/tmp', '/var/tmp'] |

server1 `/`: 315539779584 available bytes; 82.40% used; 112445150 free inodes.

server1 `/home`: 315539779584 available bytes; 82.40% used; 112445150 free inodes.

server1 `/tmp`: 315539779584 available bytes; 82.40% used; 112445150 free inodes.

server1 `/var/tmp`: 315539779584 available bytes; 82.40% used; 112445150 free inodes.

server1 `/mnt/raid5`: 645852725248 available bytes; 97.04% used; 337467120 free inodes.
| server2 | True | ['2', '7'] | [] |

server2 `/`: 18029961216 available bytes; 98.99% used; 110367557 free inodes.

server2 `/home`: 18029961216 available bytes; 98.99% used; 110367557 free inodes.

server2 `/tmp`: 18029961216 available bytes; 98.99% used; 110367557 free inodes.

server2 `/var/tmp`: 18029961216 available bytes; 98.99% used; 110367557 free inodes.

server2 `/mnt/raid5`: 601667842048 available bytes; 95.84% used; 444965481 free inodes.
| server3 | True | [] | [] |

server3 `/`: 81264889856 available bytes; 95.47% used; 114065302 free inodes.

server3 `/home`: 81264889856 available bytes; 95.47% used; 114065302 free inodes.

server3 `/data`: 1348739117056 available bytes; 81.36% used; 225833200 free inodes.

server3 `/tmp`: 81264889856 available bytes; 95.47% used; 114065302 free inodes.

server3 `/var/tmp`: 81264889856 available bytes; 95.47% used; 114065302 free inodes.
| server4 | True | [] | ['/tmp', '/var/tmp'] |

server4 `/`: 105919893504 available bytes; 94.09% used; 114347834 free inodes.

server4 `/home`: 105919893504 available bytes; 94.09% used; 114347834 free inodes.

server4 `/data`: 410279895040 available bytes; 94.33% used; 224824175 free inodes.

server4 `/tmp`: 105919893504 available bytes; 94.09% used; 114347834 free inodes.

server4 `/var/tmp`: 105919893504 available bytes; 94.09% used; 114347834 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
