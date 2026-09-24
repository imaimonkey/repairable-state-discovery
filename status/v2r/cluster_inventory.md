# V2R cluster inventory

2026-09-24T21:12:45.746018+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | [] | ['/tmp', '/var/tmp'] |

server1 `/`: 323971743744 available bytes; 81.93% used; 112481421 free inodes.

server1 `/home`: 323971743744 available bytes; 81.93% used; 112481421 free inodes.

server1 `/tmp`: 323971743744 available bytes; 81.93% used; 112481421 free inodes.

server1 `/var/tmp`: 323971743744 available bytes; 81.93% used; 112481421 free inodes.

server1 `/mnt/raid5`: 415540785152 available bytes; 98.09% used; 337629488 free inodes.
| server2 | True | ['7'] | [] |

server2 `/`: 30135431168 available bytes; 98.32% used; 110411372 free inodes.

server2 `/home`: 30135431168 available bytes; 98.32% used; 110411372 free inodes.

server2 `/tmp`: 30135431168 available bytes; 98.32% used; 110411372 free inodes.

server2 `/var/tmp`: 30135431168 available bytes; 98.32% used; 110411372 free inodes.

server2 `/mnt/raid5`: 490942988288 available bytes; 96.61% used; 445155558 free inodes.
| server3 | True | [] | [] |

server3 `/`: 84384415744 available bytes; 95.29% used; 114156095 free inodes.

server3 `/home`: 84384415744 available bytes; 95.29% used; 114156095 free inodes.

server3 `/data`: 150670692352 available bytes; 97.92% used; 225803536 free inodes.

server3 `/tmp`: 84384415744 available bytes; 95.29% used; 114156095 free inodes.

server3 `/var/tmp`: 84384415744 available bytes; 95.29% used; 114156095 free inodes.
| server4 | True | ['4'] | ['/tmp', '/var/tmp'] |

server4 `/`: 105632808960 available bytes; 94.11% used; 114348358 free inodes.

server4 `/home`: 105632808960 available bytes; 94.11% used; 114348358 free inodes.

server4 `/data`: 73123106816 available bytes; 98.99% used; 225253902 free inodes.

server4 `/tmp`: 105632808960 available bytes; 94.11% used; 114348358 free inodes.

server4 `/var/tmp`: 105632808960 available bytes; 94.11% used; 114348358 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
