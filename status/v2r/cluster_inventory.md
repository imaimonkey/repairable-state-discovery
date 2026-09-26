# V2R cluster inventory

2026-09-26T14:48:56.777951+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | ['3', '4', '5', '6', '7'] | ['/tmp', '/var/tmp'] |

server1 `/`: 318121984000 available bytes; 82.25% used; 112474343 free inodes.

server1 `/home`: 318121984000 available bytes; 82.25% used; 112474343 free inodes.

server1 `/tmp`: 318121984000 available bytes; 82.25% used; 112474343 free inodes.

server1 `/var/tmp`: 318121984000 available bytes; 82.25% used; 112474343 free inodes.

server1 `/mnt/raid5`: 666930388992 available bytes; 96.94% used; 337531894 free inodes.
| server2 | True | ['7'] | [] |

server2 `/`: 13713485824 available bytes; 99.23% used; 110378793 free inodes.

server2 `/home`: 13713485824 available bytes; 99.23% used; 110378793 free inodes.

server2 `/tmp`: 13713485824 available bytes; 99.23% used; 110378793 free inodes.

server2 `/var/tmp`: 13713485824 available bytes; 99.23% used; 110378793 free inodes.

server2 `/mnt/raid5`: 634395009024 available bytes; 95.62% used; 444973972 free inodes.
| server3 | True | [] | [] |

server3 `/`: 82627133440 available bytes; 95.39% used; 114110765 free inodes.

server3 `/home`: 82627133440 available bytes; 95.39% used; 114110765 free inodes.

server3 `/data`: 1346872582144 available bytes; 81.39% used; 225805006 free inodes.

server3 `/tmp`: 82627133440 available bytes; 95.39% used; 114110765 free inodes.

server3 `/var/tmp`: 82627133440 available bytes; 95.39% used; 114110765 free inodes.
| server4 | True | ['3', '5', '7'] | ['/tmp', '/var/tmp'] |

server4 `/`: 105886498816 available bytes; 94.09% used; 114347840 free inodes.

server4 `/home`: 105886498816 available bytes; 94.09% used; 114347840 free inodes.

server4 `/data`: 410988773376 available bytes; 94.32% used; 224826395 free inodes.

server4 `/tmp`: 105886498816 available bytes; 94.09% used; 114347840 free inodes.

server4 `/var/tmp`: 105886498816 available bytes; 94.09% used; 114347840 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
