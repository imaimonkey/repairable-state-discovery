# V2R cluster inventory

2026-09-24T18:36:59.815757+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | ['0', '7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 324004843520 available bytes; 81.92% used; 112481447 free inodes.

server1 `/home`: 324004843520 available bytes; 81.92% used; 112481447 free inodes.

server1 `/tmp`: 324004843520 available bytes; 81.92% used; 112481447 free inodes.

server1 `/var/tmp`: 324004843520 available bytes; 81.92% used; 112481447 free inodes.

server1 `/mnt/raid5`: 416310652928 available bytes; 98.09% used; 337638588 free inodes.
| server2 | True | ['7'] | [] | reference_compatible=False |

server2 `/`: 54482984960 available bytes; 96.96% used; 110411950 free inodes.

server2 `/home`: 54482984960 available bytes; 96.96% used; 110411950 free inodes.

server2 `/tmp`: 54482984960 available bytes; 96.96% used; 110411950 free inodes.

server2 `/var/tmp`: 54482984960 available bytes; 96.96% used; 110411950 free inodes.

server2 `/mnt/raid5`: 496510365696 available bytes; 96.57% used; 445160364 free inodes.
| server3 | True | ['1'] | [] | reference_compatible=True |

server3 `/`: 84407660544 available bytes; 95.29% used; 114156143 free inodes.

server3 `/home`: 84407660544 available bytes; 95.29% used; 114156143 free inodes.

server3 `/data`: 152813174784 available bytes; 97.89% used; 225800432 free inodes.

server3 `/tmp`: 84407660544 available bytes; 95.29% used; 114156143 free inodes.

server3 `/var/tmp`: 84407660544 available bytes; 95.29% used; 114156143 free inodes.
| server4 | True | [] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 105662050304 available bytes; 94.10% used; 114348505 free inodes.

server4 `/home`: 105662050304 available bytes; 94.10% used; 114348505 free inodes.

server4 `/data`: 90042109952 available bytes; 98.76% used; 225267864 free inodes.

server4 `/tmp`: 105662050304 available bytes; 94.10% used; 114348505 free inodes.

server4 `/var/tmp`: 105662050304 available bytes; 94.10% used; 114348505 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
