# V2R cluster inventory

2026-09-25T10:36:23.021728+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | [] | ['/tmp', '/var/tmp'] |

server1 `/`: 318991441920 available bytes; 82.20% used; 112479392 free inodes.

server1 `/home`: 318991441920 available bytes; 82.20% used; 112479392 free inodes.

server1 `/tmp`: 318991441920 available bytes; 82.20% used; 112479392 free inodes.

server1 `/var/tmp`: 318991441920 available bytes; 82.20% used; 112479392 free inodes.

server1 `/mnt/raid5`: 368811114496 available bytes; 98.31% used; 337555343 free inodes.
| server2 | True | ['0', '3', '5', '6'] | [] |

server2 `/`: 22826033152 available bytes; 98.73% used; 110410494 free inodes.

server2 `/home`: 22826033152 available bytes; 98.73% used; 110410494 free inodes.

server2 `/tmp`: 22826033152 available bytes; 98.73% used; 110410494 free inodes.

server2 `/var/tmp`: 22826033152 available bytes; 98.73% used; 110410494 free inodes.

server2 `/mnt/raid5`: 316026871808 available bytes; 97.82% used; 445089707 free inodes.
| server3 | True | [] | [] |

server3 `/`: 84418703360 available bytes; 95.29% used; 114156037 free inodes.

server3 `/home`: 84418703360 available bytes; 95.29% used; 114156037 free inodes.

server3 `/data`: 142009737216 available bytes; 98.04% used; 225815632 free inodes.

server3 `/tmp`: 84418703360 available bytes; 95.29% used; 114156037 free inodes.

server3 `/var/tmp`: 84418703360 available bytes; 95.29% used; 114156037 free inodes.
| server4 | True | [] | ['/tmp', '/var/tmp'] |

server4 `/`: 105613172736 available bytes; 94.11% used; 114350251 free inodes.

server4 `/home`: 105613172736 available bytes; 94.11% used; 114350251 free inodes.

server4 `/data`: 238513655808 available bytes; 96.70% used; 224986495 free inodes.

server4 `/tmp`: 105613172736 available bytes; 94.11% used; 114350251 free inodes.

server4 `/var/tmp`: 105613172736 available bytes; 94.11% used; 114350251 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
