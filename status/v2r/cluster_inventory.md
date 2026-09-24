# V2R cluster inventory

2026-09-24T15:13:51.892683+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | [] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 324045348864 available bytes; 81.92% used; 112481469 free inodes.

server1 `/home`: 324045348864 available bytes; 81.92% used; 112481469 free inodes.

server1 `/tmp`: 324045348864 available bytes; 81.92% used; 112481469 free inodes.

server1 `/var/tmp`: 324045348864 available bytes; 81.92% used; 112481469 free inodes.

server1 `/mnt/raid5`: 416800104448 available bytes; 98.09% used; 337663102 free inodes.
| server2 | True | ['7'] | [] | reference_compatible=False |

server2 `/`: 57408462848 available bytes; 96.80% used; 110427671 free inodes.

server2 `/home`: 57408462848 available bytes; 96.80% used; 110427671 free inodes.

server2 `/tmp`: 57408462848 available bytes; 96.80% used; 110427671 free inodes.

server2 `/var/tmp`: 57408462848 available bytes; 96.80% used; 110427671 free inodes.

server2 `/mnt/raid5`: 503170568192 available bytes; 96.52% used; 445166754 free inodes.
| server3 | True | ['0'] | [] | reference_compatible=True |

server3 `/`: 84867715072 available bytes; 95.26% used; 114183303 free inodes.

server3 `/home`: 84867715072 available bytes; 95.26% used; 114183303 free inodes.

server3 `/data`: 160496889856 available bytes; 97.78% used; 225807263 free inodes.

server3 `/tmp`: 84867715072 available bytes; 95.26% used; 114183303 free inodes.

server3 `/var/tmp`: 84867715072 available bytes; 95.26% used; 114183303 free inodes.
| server4 | True | [] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 105716908032 available bytes; 94.10% used; 114348633 free inodes.

server4 `/home`: 105716908032 available bytes; 94.10% used; 114348633 free inodes.

server4 `/data`: 68785815552 available bytes; 99.05% used; 225256964 free inodes.

server4 `/tmp`: 105716908032 available bytes; 94.10% used; 114348633 free inodes.

server4 `/var/tmp`: 105716908032 available bytes; 94.10% used; 114348633 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
