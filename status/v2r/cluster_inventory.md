# V2R cluster inventory

2026-09-26T14:47:25.217497+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | ['3', '4', '5', '6', '7'] | ['/tmp', '/var/tmp'] |

server1 `/`: 318122913792 available bytes; 82.25% used; 112474346 free inodes.

server1 `/home`: 318122913792 available bytes; 82.25% used; 112474346 free inodes.

server1 `/tmp`: 318122913792 available bytes; 82.25% used; 112474346 free inodes.

server1 `/var/tmp`: 318122913792 available bytes; 82.25% used; 112474346 free inodes.

server1 `/mnt/raid5`: 669173342208 available bytes; 96.93% used; 337531899 free inodes.
| server2 | True | ['7'] | [] |

server2 `/`: 14053834752 available bytes; 99.22% used; 110378804 free inodes.

server2 `/home`: 14053834752 available bytes; 99.22% used; 110378804 free inodes.

server2 `/tmp`: 14053834752 available bytes; 99.22% used; 110378804 free inodes.

server2 `/var/tmp`: 14053834752 available bytes; 99.22% used; 110378804 free inodes.

server2 `/mnt/raid5`: 634445705216 available bytes; 95.62% used; 444974114 free inodes.
| server3 | True | [] | [] |

server3 `/`: 82627420160 available bytes; 95.39% used; 114110765 free inodes.

server3 `/home`: 82627420160 available bytes; 95.39% used; 114110765 free inodes.

server3 `/data`: 1346873978880 available bytes; 81.39% used; 225805028 free inodes.

server3 `/tmp`: 82627420160 available bytes; 95.39% used; 114110765 free inodes.

server3 `/var/tmp`: 82627420160 available bytes; 95.39% used; 114110765 free inodes.
| server4 | True | ['3', '5', '7'] | ['/tmp', '/var/tmp'] |

server4 `/`: 105886519296 available bytes; 94.09% used; 114347840 free inodes.

server4 `/home`: 105886519296 available bytes; 94.09% used; 114347840 free inodes.

server4 `/data`: 410989330432 available bytes; 94.32% used; 224826409 free inodes.

server4 `/tmp`: 105886519296 available bytes; 94.09% used; 114347840 free inodes.

server4 `/var/tmp`: 105886519296 available bytes; 94.09% used; 114347840 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
