# V2R cluster inventory

2026-09-24T21:03:31.673480+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | [] | ['/tmp', '/var/tmp'] |

server1 `/`: 323981844480 available bytes; 81.93% used; 112481417 free inodes.

server1 `/home`: 323981844480 available bytes; 81.93% used; 112481417 free inodes.

server1 `/tmp`: 323981844480 available bytes; 81.93% used; 112481417 free inodes.

server1 `/var/tmp`: 323981844480 available bytes; 81.93% used; 112481417 free inodes.

server1 `/mnt/raid5`: 415554281472 available bytes; 98.09% used; 337630561 free inodes.
| server2 | True | ['7'] | [] |

server2 `/`: 30141501440 available bytes; 98.32% used; 110411372 free inodes.

server2 `/home`: 30141501440 available bytes; 98.32% used; 110411372 free inodes.

server2 `/tmp`: 30141501440 available bytes; 98.32% used; 110411372 free inodes.

server2 `/var/tmp`: 30141501440 available bytes; 98.32% used; 110411372 free inodes.

server2 `/mnt/raid5`: 490697326592 available bytes; 96.61% used; 445156045 free inodes.
| server3 | True | [] | [] |

server3 `/`: 84385886208 available bytes; 95.29% used; 114156093 free inodes.

server3 `/home`: 84385886208 available bytes; 95.29% used; 114156093 free inodes.

server3 `/data`: 150828871680 available bytes; 97.92% used; 225803693 free inodes.

server3 `/tmp`: 84385886208 available bytes; 95.29% used; 114156093 free inodes.

server3 `/var/tmp`: 84385886208 available bytes; 95.29% used; 114156093 free inodes.
| server4 | True | ['4'] | ['/tmp', '/var/tmp'] |

server4 `/`: 105638793216 available bytes; 94.10% used; 114348364 free inodes.

server4 `/home`: 105638793216 available bytes; 94.10% used; 114348364 free inodes.

server4 `/data`: 75025170432 available bytes; 98.96% used; 225254812 free inodes.

server4 `/tmp`: 105638793216 available bytes; 94.10% used; 114348364 free inodes.

server4 `/var/tmp`: 105638793216 available bytes; 94.10% used; 114348364 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
