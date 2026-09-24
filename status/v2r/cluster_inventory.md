# V2R cluster inventory

2026-09-24T21:59:13.494966+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | [] | ['/tmp', '/var/tmp'] |

server1 `/`: 323951591424 available bytes; 81.93% used; 112481415 free inodes.

server1 `/home`: 323951591424 available bytes; 81.93% used; 112481415 free inodes.

server1 `/tmp`: 323951591424 available bytes; 81.93% used; 112481415 free inodes.

server1 `/var/tmp`: 323951591424 available bytes; 81.93% used; 112481415 free inodes.

server1 `/mnt/raid5`: 415432568832 available bytes; 98.09% used; 337623934 free inodes.
| server2 | True | [] | [] |

server2 `/`: 30124322816 available bytes; 98.32% used; 110411302 free inodes.

server2 `/home`: 30124322816 available bytes; 98.32% used; 110411302 free inodes.

server2 `/tmp`: 30124322816 available bytes; 98.32% used; 110411302 free inodes.

server2 `/var/tmp`: 30124322816 available bytes; 98.32% used; 110411302 free inodes.

server2 `/mnt/raid5`: 489512239104 available bytes; 96.62% used; 445154097 free inodes.
| server3 | True | [] | [] |

server3 `/`: 84380098560 available bytes; 95.29% used; 114156085 free inodes.

server3 `/home`: 84380098560 available bytes; 95.29% used; 114156085 free inodes.

server3 `/data`: 149804306432 available bytes; 97.93% used; 225802647 free inodes.

server3 `/tmp`: 84380098560 available bytes; 95.29% used; 114156085 free inodes.

server3 `/var/tmp`: 84380098560 available bytes; 95.29% used; 114156085 free inodes.
| server4 | True | ['1', '4', '5'] | ['/tmp', '/var/tmp'] |

server4 `/`: 105819619328 available bytes; 94.09% used; 114348340 free inodes.

server4 `/home`: 105819619328 available bytes; 94.09% used; 114348340 free inodes.

server4 `/data`: 77700050944 available bytes; 98.93% used; 225243412 free inodes.

server4 `/tmp`: 105819619328 available bytes; 94.09% used; 114348340 free inodes.

server4 `/var/tmp`: 105819619328 available bytes; 94.09% used; 114348340 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
