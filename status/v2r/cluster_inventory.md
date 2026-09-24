# V2R cluster inventory

2026-09-24T13:57:39.555485+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | ['1'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 324069134336 available bytes; 81.92% used; 112481671 free inodes.

server1 `/home`: 324069134336 available bytes; 81.92% used; 112481671 free inodes.

server1 `/tmp`: 324069134336 available bytes; 81.92% used; 112481671 free inodes.

server1 `/var/tmp`: 324069134336 available bytes; 81.92% used; 112481671 free inodes.

server1 `/mnt/raid5`: 416971882496 available bytes; 98.09% used; 337671996 free inodes.
| server2 | True | ['7'] | [] | reference_compatible=False |

server2 `/`: 57498595328 available bytes; 96.79% used; 110428435 free inodes.

server2 `/home`: 57498595328 available bytes; 96.79% used; 110428435 free inodes.

server2 `/tmp`: 57498595328 available bytes; 96.79% used; 110428435 free inodes.

server2 `/var/tmp`: 57498595328 available bytes; 96.79% used; 110428435 free inodes.

server2 `/mnt/raid5`: 505795702784 available bytes; 96.51% used; 445168949 free inodes.
| server3 | True | [] | [] | reference_compatible=True |

server3 `/`: 85094318080 available bytes; 95.25% used; 114190440 free inodes.

server3 `/home`: 85094318080 available bytes; 95.25% used; 114190440 free inodes.

server3 `/data`: 161052463104 available bytes; 97.77% used; 225802637 free inodes.

server3 `/tmp`: 85094318080 available bytes; 95.25% used; 114190440 free inodes.

server3 `/var/tmp`: 85094318080 available bytes; 95.25% used; 114190440 free inodes.
| server4 | True | [] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 105760251904 available bytes; 94.10% used; 114348716 free inodes.

server4 `/home`: 105760251904 available bytes; 94.10% used; 114348716 free inodes.

server4 `/data`: 81223577600 available bytes; 98.88% used; 225257160 free inodes.

server4 `/tmp`: 105760251904 available bytes; 94.10% used; 114348716 free inodes.

server4 `/var/tmp`: 105760251904 available bytes; 94.10% used; 114348716 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
