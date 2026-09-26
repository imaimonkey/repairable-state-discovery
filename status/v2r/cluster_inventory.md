# V2R cluster inventory

2026-09-26T13:35:43.239312+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | ['1', '2', '3', '4', '5', '6', '7'] | ['/tmp', '/var/tmp'] |

server1 `/`: 318155538432 available bytes; 82.25% used; 112474413 free inodes.

server1 `/home`: 318155538432 available bytes; 82.25% used; 112474413 free inodes.

server1 `/tmp`: 318155538432 available bytes; 82.25% used; 112474413 free inodes.

server1 `/var/tmp`: 318155538432 available bytes; 82.25% used; 112474413 free inodes.

server1 `/mnt/raid5`: 674755289088 available bytes; 96.90% used; 337535772 free inodes.
| server2 | True | ['2', '7'] | [] |

server2 `/`: 19072679936 available bytes; 98.94% used; 110378920 free inodes.

server2 `/home`: 19072679936 available bytes; 98.94% used; 110378920 free inodes.

server2 `/tmp`: 19072679936 available bytes; 98.94% used; 110378920 free inodes.

server2 `/var/tmp`: 19072679936 available bytes; 98.94% used; 110378920 free inodes.

server2 `/mnt/raid5`: 636400562176 available bytes; 95.60% used; 444976356 free inodes.
| server3 | True | [] | [] |

server3 `/`: 82641113088 available bytes; 95.39% used; 114110801 free inodes.

server3 `/home`: 82641113088 available bytes; 95.39% used; 114110801 free inodes.

server3 `/data`: 1347497111552 available bytes; 81.38% used; 225822948 free inodes.

server3 `/tmp`: 82641113088 available bytes; 95.39% used; 114110801 free inodes.

server3 `/var/tmp`: 82641113088 available bytes; 95.39% used; 114110801 free inodes.
| server4 | True | ['0', '3', '5', '7'] | ['/tmp', '/var/tmp'] |

server4 `/`: 105898401792 available bytes; 94.09% used; 114347938 free inodes.

server4 `/home`: 105898401792 available bytes; 94.09% used; 114347938 free inodes.

server4 `/data`: 411550642176 available bytes; 94.31% used; 224827598 free inodes.

server4 `/tmp`: 105898401792 available bytes; 94.09% used; 114347938 free inodes.

server4 `/var/tmp`: 105898401792 available bytes; 94.09% used; 114347938 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
