# V2R cluster inventory

2026-09-26T14:56:34.558888+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | ['3', '4', '5', '6', '7'] | ['/tmp', '/var/tmp'] |

server1 `/`: 318112677888 available bytes; 82.25% used; 112474326 free inodes.

server1 `/home`: 318112677888 available bytes; 82.25% used; 112474326 free inodes.

server1 `/tmp`: 318112677888 available bytes; 82.25% used; 112474326 free inodes.

server1 `/var/tmp`: 318112677888 available bytes; 82.25% used; 112474326 free inodes.

server1 `/mnt/raid5`: 657639948288 available bytes; 96.98% used; 337531877 free inodes.
| server2 | True | ['7'] | [] |

server2 `/`: 7765135360 available bytes; 99.57% used; 110367487 free inodes.

server2 `/home`: 7765135360 available bytes; 99.57% used; 110367487 free inodes.

server2 `/tmp`: 7765135360 available bytes; 99.57% used; 110367487 free inodes.

server2 `/var/tmp`: 7765135360 available bytes; 99.57% used; 110367487 free inodes.

server2 `/mnt/raid5`: 629834915840 available bytes; 95.65% used; 444973705 free inodes.
| server3 | True | [] | [] |

server3 `/`: 82632486912 available bytes; 95.39% used; 114110773 free inodes.

server3 `/home`: 82632486912 available bytes; 95.39% used; 114110773 free inodes.

server3 `/data`: 1346840526848 available bytes; 81.39% used; 225804898 free inodes.

server3 `/tmp`: 82632486912 available bytes; 95.39% used; 114110773 free inodes.

server3 `/var/tmp`: 82632486912 available bytes; 95.39% used; 114110773 free inodes.
| server4 | True | ['3', '5', '7'] | ['/tmp', '/var/tmp'] |

server4 `/`: 105886359552 available bytes; 94.09% used; 114347840 free inodes.

server4 `/home`: 105886359552 available bytes; 94.09% used; 114347840 free inodes.

server4 `/data`: 410830348288 available bytes; 94.32% used; 224826256 free inodes.

server4 `/tmp`: 105886359552 available bytes; 94.09% used; 114347840 free inodes.

server4 `/var/tmp`: 105886359552 available bytes; 94.09% used; 114347840 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
