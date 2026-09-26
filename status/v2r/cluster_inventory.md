# V2R cluster inventory

2026-09-26T13:03:40.475753+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | ['0', '1', '2', '3', '4', '5', '6', '7'] | ['/tmp', '/var/tmp'] |

server1 `/`: 318153150464 available bytes; 82.25% used; 112474488 free inodes.

server1 `/home`: 318153150464 available bytes; 82.25% used; 112474488 free inodes.

server1 `/tmp`: 318153150464 available bytes; 82.25% used; 112474488 free inodes.

server1 `/var/tmp`: 318153150464 available bytes; 82.25% used; 112474488 free inodes.

server1 `/mnt/raid5`: 675297554432 available bytes; 96.90% used; 337535969 free inodes.
| server2 | True | ['2', '7'] | [] |

server2 `/`: 19085033472 available bytes; 98.94% used; 110379530 free inodes.

server2 `/home`: 19085033472 available bytes; 98.94% used; 110379530 free inodes.

server2 `/tmp`: 19085033472 available bytes; 98.94% used; 110379530 free inodes.

server2 `/var/tmp`: 19085033472 available bytes; 98.94% used; 110379530 free inodes.

server2 `/mnt/raid5`: 637600116736 available bytes; 95.59% used; 444977392 free inodes.
| server3 | True | [] | [] |

server3 `/`: 82641719296 available bytes; 95.39% used; 114110817 free inodes.

server3 `/home`: 82641719296 available bytes; 95.39% used; 114110817 free inodes.

server3 `/data`: 1347574898688 available bytes; 81.38% used; 225823301 free inodes.

server3 `/tmp`: 82641719296 available bytes; 95.39% used; 114110817 free inodes.

server3 `/var/tmp`: 82641719296 available bytes; 95.39% used; 114110817 free inodes.
| server4 | True | ['0', '3', '5', '7'] | ['/tmp', '/var/tmp'] |

server4 `/`: 105899016192 available bytes; 94.09% used; 114347938 free inodes.

server4 `/home`: 105899016192 available bytes; 94.09% used; 114347938 free inodes.

server4 `/data`: 413505822720 available bytes; 94.29% used; 224846985 free inodes.

server4 `/tmp`: 105899016192 available bytes; 94.09% used; 114347938 free inodes.

server4 `/var/tmp`: 105899016192 available bytes; 94.09% used; 114347938 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
