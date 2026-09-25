# V2R cluster inventory

2026-09-25T10:13:58.216647+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | [] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 318834704384 available bytes; 82.21% used; 112480387 free inodes.

server1 `/home`: 318834704384 available bytes; 82.21% used; 112480387 free inodes.

server1 `/tmp`: 318834704384 available bytes; 82.21% used; 112480387 free inodes.

server1 `/var/tmp`: 318834704384 available bytes; 82.21% used; 112480387 free inodes.

server1 `/mnt/raid5`: 364866502656 available bytes; 98.33% used; 337556387 free inodes.
| server2 | True | ['3', '6'] | [] | reference_compatible=False |

server2 `/`: 22835236864 available bytes; 98.73% used; 110410480 free inodes.

server2 `/home`: 22835236864 available bytes; 98.73% used; 110410480 free inodes.

server2 `/tmp`: 22835236864 available bytes; 98.73% used; 110410480 free inodes.

server2 `/var/tmp`: 22835236864 available bytes; 98.73% used; 110410480 free inodes.

server2 `/mnt/raid5`: 316646776832 available bytes; 97.81% used; 445091132 free inodes.
| server3 | True | [] | [] | reference_compatible=True |

server3 `/`: 84417409024 available bytes; 95.29% used; 114156045 free inodes.

server3 `/home`: 84417409024 available bytes; 95.29% used; 114156045 free inodes.

server3 `/data`: 142025216000 available bytes; 98.04% used; 225816172 free inodes.

server3 `/tmp`: 84417409024 available bytes; 95.29% used; 114156045 free inodes.

server3 `/var/tmp`: 84417409024 available bytes; 95.29% used; 114156045 free inodes.
| server4 | True | [] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 105613979648 available bytes; 94.11% used; 114350276 free inodes.

server4 `/home`: 105613979648 available bytes; 94.11% used; 114350276 free inodes.

server4 `/data`: 240068243456 available bytes; 96.68% used; 224989519 free inodes.

server4 `/tmp`: 105613979648 available bytes; 94.11% used; 114350276 free inodes.

server4 `/var/tmp`: 105613979648 available bytes; 94.11% used; 114350276 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
