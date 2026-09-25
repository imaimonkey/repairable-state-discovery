# V2R cluster inventory

2026-09-25T00:34:31.893447+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | [] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 319086518272 available bytes; 82.20% used; 112480771 free inodes.

server1 `/home`: 319086518272 available bytes; 82.20% used; 112480771 free inodes.

server1 `/tmp`: 319086518272 available bytes; 82.20% used; 112480771 free inodes.

server1 `/var/tmp`: 319086518272 available bytes; 82.20% used; 112480771 free inodes.

server1 `/mnt/raid5`: 416846233600 available bytes; 98.09% used; 337619364 free inodes.
| server2 | True | [] | [] | reference_compatible=False |

server2 `/`: 23076159488 available bytes; 98.71% used; 110410767 free inodes.

server2 `/home`: 23076159488 available bytes; 98.71% used; 110410767 free inodes.

server2 `/tmp`: 23076159488 available bytes; 98.71% used; 110410767 free inodes.

server2 `/var/tmp`: 23076159488 available bytes; 98.71% used; 110410767 free inodes.

server2 `/mnt/raid5`: 501679648768 available bytes; 96.53% used; 445162692 free inodes.
| server3 | True | [] | [] | reference_compatible=True |

server3 `/`: 84349710336 available bytes; 95.29% used; 114156086 free inodes.

server3 `/home`: 84349710336 available bytes; 95.29% used; 114156086 free inodes.

server3 `/data`: 148816707584 available bytes; 97.94% used; 225813365 free inodes.

server3 `/tmp`: 84349710336 available bytes; 95.29% used; 114156086 free inodes.

server3 `/var/tmp`: 84349710336 available bytes; 95.29% used; 114156086 free inodes.
| server4 | True | ['0', '5', '7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 105788833792 available bytes; 94.10% used; 114348296 free inodes.

server4 `/home`: 105788833792 available bytes; 94.10% used; 114348296 free inodes.

server4 `/data`: 56591564800 available bytes; 99.22% used; 225052697 free inodes.

server4 `/tmp`: 105788833792 available bytes; 94.10% used; 114348296 free inodes.

server4 `/var/tmp`: 105788833792 available bytes; 94.10% used; 114348296 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
