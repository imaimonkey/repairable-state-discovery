# V2R cluster inventory

2026-09-24T13:04:40.689106+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | [] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 324041347072 available bytes; 81.92% used; 112481558 free inodes.

server1 `/home`: 324041347072 available bytes; 81.92% used; 112481558 free inodes.

server1 `/tmp`: 324041347072 available bytes; 81.92% used; 112481558 free inodes.

server1 `/var/tmp`: 324041347072 available bytes; 81.92% used; 112481558 free inodes.

server1 `/mnt/raid5`: 417078292480 available bytes; 98.09% used; 337678191 free inodes.
| server2 | True | ['7'] | [] | reference_compatible=False |

server2 `/`: 57555902464 available bytes; 96.79% used; 110428987 free inodes.

server2 `/home`: 57555902464 available bytes; 96.79% used; 110428987 free inodes.

server2 `/tmp`: 57555902464 available bytes; 96.79% used; 110428987 free inodes.

server2 `/var/tmp`: 57555902464 available bytes; 96.79% used; 110428987 free inodes.

server2 `/mnt/raid5`: 507415863296 available bytes; 96.49% used; 445170744 free inodes.
| server3 | True | [] | [] | reference_compatible=True |

server3 `/`: 85199036416 available bytes; 95.25% used; 114167247 free inodes.

server3 `/home`: 85199036416 available bytes; 95.25% used; 114167247 free inodes.

server3 `/data`: 162985545728 available bytes; 97.75% used; 225813672 free inodes.

server3 `/tmp`: 85199036416 available bytes; 95.25% used; 114167247 free inodes.

server3 `/var/tmp`: 85199036416 available bytes; 95.25% used; 114167247 free inodes.
| server4 | True | [] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 105779179520 available bytes; 94.10% used; 114348761 free inodes.

server4 `/home`: 105779179520 available bytes; 94.10% used; 114348761 free inodes.

server4 `/data`: 90039070720 available bytes; 98.76% used; 225257179 free inodes.

server4 `/tmp`: 105779179520 available bytes; 94.10% used; 114348761 free inodes.

server4 `/var/tmp`: 105779179520 available bytes; 94.10% used; 114348761 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
