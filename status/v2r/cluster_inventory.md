# V2R cluster inventory

2026-09-26T14:39:47.261841+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | ['3', '4', '5', '6', '7'] | ['/tmp', '/var/tmp'] |

server1 `/`: 318126325760 available bytes; 82.25% used; 112474359 free inodes.

server1 `/home`: 318126325760 available bytes; 82.25% used; 112474359 free inodes.

server1 `/tmp`: 318126325760 available bytes; 82.25% used; 112474359 free inodes.

server1 `/var/tmp`: 318126325760 available bytes; 82.25% used; 112474359 free inodes.

server1 `/mnt/raid5`: 674022498304 available bytes; 96.91% used; 337531925 free inodes.
| server2 | True | ['7'] | [] |

server2 `/`: 14737252352 available bytes; 99.18% used; 110378814 free inodes.

server2 `/home`: 14737252352 available bytes; 99.18% used; 110378814 free inodes.

server2 `/tmp`: 14737252352 available bytes; 99.18% used; 110378814 free inodes.

server2 `/var/tmp`: 14737252352 available bytes; 99.18% used; 110378814 free inodes.

server2 `/mnt/raid5`: 634662232064 available bytes; 95.61% used; 444974452 free inodes.
| server3 | True | [] | [] |

server3 `/`: 82629185536 available bytes; 95.39% used; 114110777 free inodes.

server3 `/home`: 82629185536 available bytes; 95.39% used; 114110777 free inodes.

server3 `/data`: 1346880241664 available bytes; 81.39% used; 225805110 free inodes.

server3 `/tmp`: 82629185536 available bytes; 95.39% used; 114110777 free inodes.

server3 `/var/tmp`: 82629185536 available bytes; 95.39% used; 114110777 free inodes.
| server4 | True | ['3', '5', '7'] | ['/tmp', '/var/tmp'] |

server4 `/`: 105886691328 available bytes; 94.09% used; 114347840 free inodes.

server4 `/home`: 105886691328 available bytes; 94.09% used; 114347840 free inodes.

server4 `/data`: 411004243968 available bytes; 94.32% used; 224826650 free inodes.

server4 `/tmp`: 105886691328 available bytes; 94.09% used; 114347840 free inodes.

server4 `/var/tmp`: 105886691328 available bytes; 94.09% used; 114347840 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
