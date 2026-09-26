# V2R cluster inventory

2026-09-26T13:18:56.197914+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | ['1', '2', '3', '4', '5', '6', '7'] | ['/tmp', '/var/tmp'] |

server1 `/`: 318153637888 available bytes; 82.25% used; 112474432 free inodes.

server1 `/home`: 318153637888 available bytes; 82.25% used; 112474432 free inodes.

server1 `/tmp`: 318153637888 available bytes; 82.25% used; 112474432 free inodes.

server1 `/var/tmp`: 318153637888 available bytes; 82.25% used; 112474432 free inodes.

server1 `/mnt/raid5`: 674744197120 available bytes; 96.90% used; 337535808 free inodes.
| server2 | True | ['2', '7'] | [] |

server2 `/`: 19075719168 available bytes; 98.94% used; 110378936 free inodes.

server2 `/home`: 19075719168 available bytes; 98.94% used; 110378936 free inodes.

server2 `/tmp`: 19075719168 available bytes; 98.94% used; 110378936 free inodes.

server2 `/var/tmp`: 19075719168 available bytes; 98.94% used; 110378936 free inodes.

server2 `/mnt/raid5`: 636891848704 available bytes; 95.60% used; 444976857 free inodes.
| server3 | True | [] | [] |

server3 `/`: 82642194432 available bytes; 95.39% used; 114110817 free inodes.

server3 `/home`: 82642194432 available bytes; 95.39% used; 114110817 free inodes.

server3 `/data`: 1347563143168 available bytes; 81.38% used; 225823117 free inodes.

server3 `/tmp`: 82642194432 available bytes; 95.39% used; 114110817 free inodes.

server3 `/var/tmp`: 82642194432 available bytes; 95.39% used; 114110817 free inodes.
| server4 | True | ['0', '3', '5', '7'] | ['/tmp', '/var/tmp'] |

server4 `/`: 105898717184 available bytes; 94.09% used; 114347938 free inodes.

server4 `/home`: 105898717184 available bytes; 94.09% used; 114347938 free inodes.

server4 `/data`: 411564535808 available bytes; 94.31% used; 224827628 free inodes.

server4 `/tmp`: 105898717184 available bytes; 94.09% used; 114347938 free inodes.

server4 `/var/tmp`: 105898717184 available bytes; 94.09% used; 114347938 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
