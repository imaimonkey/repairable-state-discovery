# V2R cluster inventory

2026-09-26T14:59:37.577007+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | ['3', '4', '5', '6', '7'] | ['/tmp', '/var/tmp'] |

server1 `/`: 318111862784 available bytes; 82.25% used; 112474061 free inodes.

server1 `/home`: 318111862784 available bytes; 82.25% used; 112474061 free inodes.

server1 `/tmp`: 318111862784 available bytes; 82.25% used; 112474061 free inodes.

server1 `/var/tmp`: 318111862784 available bytes; 82.25% used; 112474061 free inodes.

server1 `/mnt/raid5`: 656145780736 available bytes; 96.99% used; 337531877 free inodes.
| server2 | True | ['7'] | [] |

server2 `/`: 1791070208 available bytes; 99.90% used; 110367165 free inodes.

server2 `/home`: 1791070208 available bytes; 99.90% used; 110367165 free inodes.

server2 `/tmp`: 1791070208 available bytes; 99.90% used; 110367165 free inodes.

server2 `/var/tmp`: 1791070208 available bytes; 99.90% used; 110367165 free inodes.

server2 `/mnt/raid5`: 625079930880 available bytes; 95.68% used; 444973568 free inodes.
| server3 | True | [] | [] |

server3 `/`: 82628796416 available bytes; 95.39% used; 114110773 free inodes.

server3 `/home`: 82628796416 available bytes; 95.39% used; 114110773 free inodes.

server3 `/data`: 1346840584192 available bytes; 81.39% used; 225804873 free inodes.

server3 `/tmp`: 82628796416 available bytes; 95.39% used; 114110773 free inodes.

server3 `/var/tmp`: 82628796416 available bytes; 95.39% used; 114110773 free inodes.
| server4 | True | ['3', '5', '7'] | ['/tmp', '/var/tmp'] |

server4 `/`: 105877905408 available bytes; 94.09% used; 114347840 free inodes.

server4 `/home`: 105877905408 available bytes; 94.09% used; 114347840 free inodes.

server4 `/data`: 410822070272 available bytes; 94.32% used; 224826215 free inodes.

server4 `/tmp`: 105877905408 available bytes; 94.09% used; 114347840 free inodes.

server4 `/var/tmp`: 105877905408 available bytes; 94.09% used; 114347840 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
