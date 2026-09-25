# V2R cluster inventory

2026-09-25T06:48:47.991787+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | [] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 318871576576 available bytes; 82.21% used; 112480370 free inodes.

server1 `/home`: 318871576576 available bytes; 82.21% used; 112480370 free inodes.

server1 `/tmp`: 318871576576 available bytes; 82.21% used; 112480370 free inodes.

server1 `/var/tmp`: 318871576576 available bytes; 82.21% used; 112480370 free inodes.

server1 `/mnt/raid5`: 399733428224 available bytes; 98.17% used; 337560552 free inodes.
| server2 | True | [] | [] | reference_compatible=False |

server2 `/`: 22877634560 available bytes; 98.72% used; 110410526 free inodes.

server2 `/home`: 22877634560 available bytes; 98.72% used; 110410526 free inodes.

server2 `/tmp`: 22877634560 available bytes; 98.72% used; 110410526 free inodes.

server2 `/var/tmp`: 22877634560 available bytes; 98.72% used; 110410526 free inodes.

server2 `/mnt/raid5`: 338191745024 available bytes; 97.66% used; 445098644 free inodes.
| server3 | True | [] | [] | reference_compatible=True |

server3 `/`: 84448931840 available bytes; 95.29% used; 114156031 free inodes.

server3 `/home`: 84448931840 available bytes; 95.29% used; 114156031 free inodes.

server3 `/data`: 142526046208 available bytes; 98.03% used; 225813429 free inodes.

server3 `/tmp`: 84448931840 available bytes; 95.29% used; 114156031 free inodes.

server3 `/var/tmp`: 84448931840 available bytes; 95.29% used; 114156031 free inodes.
| server4 | True | ['1', '3'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 105639194624 available bytes; 94.10% used; 114350378 free inodes.

server4 `/home`: 105639194624 available bytes; 94.10% used; 114350378 free inodes.

server4 `/data`: 249510932480 available bytes; 96.55% used; 225018068 free inodes.

server4 `/tmp`: 105639194624 available bytes; 94.10% used; 114350378 free inodes.

server4 `/var/tmp`: 105639194624 available bytes; 94.10% used; 114350378 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
