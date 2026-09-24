# V2R cluster inventory

2026-09-24T20:34:09.848479+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | [] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 323982315520 available bytes; 81.93% used; 112481433 free inodes.

server1 `/home`: 323982315520 available bytes; 81.93% used; 112481433 free inodes.

server1 `/tmp`: 323982315520 available bytes; 81.93% used; 112481433 free inodes.

server1 `/var/tmp`: 323982315520 available bytes; 81.93% used; 112481433 free inodes.

server1 `/mnt/raid5`: 415614070784 available bytes; 98.09% used; 337633978 free inodes.
| server2 | True | ['7'] | [] | reference_compatible=False |

server2 `/`: 30152798208 available bytes; 98.32% used; 110411376 free inodes.

server2 `/home`: 30152798208 available bytes; 98.32% used; 110411376 free inodes.

server2 `/tmp`: 30152798208 available bytes; 98.32% used; 110411376 free inodes.

server2 `/var/tmp`: 30152798208 available bytes; 98.32% used; 110411376 free inodes.

server2 `/mnt/raid5`: 492153454592 available bytes; 96.60% used; 445156972 free inodes.
| server3 | True | [] | [] | reference_compatible=True |

server3 `/`: 84396843008 available bytes; 95.29% used; 114156106 free inodes.

server3 `/home`: 84396843008 available bytes; 95.29% used; 114156106 free inodes.

server3 `/data`: 151401652224 available bytes; 97.91% used; 225804308 free inodes.

server3 `/tmp`: 84396843008 available bytes; 95.29% used; 114156106 free inodes.

server3 `/var/tmp`: 84396843008 available bytes; 95.29% used; 114156106 free inodes.
| server4 | True | [] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 105640071168 available bytes; 94.10% used; 114348380 free inodes.

server4 `/home`: 105640071168 available bytes; 94.10% used; 114348380 free inodes.

server4 `/data`: 85464616960 available bytes; 98.82% used; 225257649 free inodes.

server4 `/tmp`: 105640071168 available bytes; 94.10% used; 114348380 free inodes.

server4 `/var/tmp`: 105640071168 available bytes; 94.10% used; 114348380 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
