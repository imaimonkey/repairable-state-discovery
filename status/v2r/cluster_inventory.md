# V2R cluster inventory

2026-09-25T20:37:59.751416+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | ['1', '6', '7'] | ['/tmp', '/var/tmp'] |

server1 `/`: 318707478528 available bytes; 82.22% used; 112476319 free inodes.

server1 `/home`: 318707478528 available bytes; 82.22% used; 112476319 free inodes.

server1 `/tmp`: 318707478528 available bytes; 82.22% used; 112476319 free inodes.

server1 `/var/tmp`: 318707478528 available bytes; 82.22% used; 112476319 free inodes.

server1 `/mnt/raid5`: 369158664192 available bytes; 98.31% used; 337540443 free inodes.
| server2 | True | ['4', '5', '6'] | [] |

server2 `/`: 22999093248 available bytes; 98.72% used; 110406387 free inodes.

server2 `/home`: 22999093248 available bytes; 98.72% used; 110406387 free inodes.

server2 `/tmp`: 22999093248 available bytes; 98.72% used; 110406387 free inodes.

server2 `/var/tmp`: 22999093248 available bytes; 98.72% used; 110406387 free inodes.

server2 `/mnt/raid5`: 303076417536 available bytes; 97.91% used; 445057325 free inodes.
| server3 | True | [] | [] |

server3 `/`: 84380852224 available bytes; 95.29% used; 114152622 free inodes.

server3 `/home`: 84380852224 available bytes; 95.29% used; 114152622 free inodes.

server3 `/data`: 127170670592 available bytes; 98.24% used; 225807906 free inodes.

server3 `/tmp`: 84380852224 available bytes; 95.29% used; 114152622 free inodes.

server3 `/var/tmp`: 84380852224 available bytes; 95.29% used; 114152622 free inodes.
| server4 | True | ['2', '3', '6', '7'] | ['/tmp', '/var/tmp'] |

server4 `/`: 105655853056 available bytes; 94.10% used; 114349549 free inodes.

server4 `/home`: 105655853056 available bytes; 94.10% used; 114349549 free inodes.

server4 `/data`: 228329263104 available bytes; 96.84% used; 224928550 free inodes.

server4 `/tmp`: 105655853056 available bytes; 94.10% used; 114349549 free inodes.

server4 `/var/tmp`: 105655853056 available bytes; 94.10% used; 114349549 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
