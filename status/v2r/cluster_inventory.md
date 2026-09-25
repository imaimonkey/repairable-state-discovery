# V2R cluster inventory

2026-09-25T02:57:33.236145+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | [] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 318941761536 available bytes; 82.21% used; 112480390 free inodes.

server1 `/home`: 318941761536 available bytes; 82.21% used; 112480390 free inodes.

server1 `/tmp`: 318941761536 available bytes; 82.21% used; 112480390 free inodes.

server1 `/var/tmp`: 318941761536 available bytes; 82.21% used; 112480390 free inodes.

server1 `/mnt/raid5`: 416154066944 available bytes; 98.09% used; 337602725 free inodes.
| server2 | True | [] | [] | reference_compatible=False |

server2 `/`: 22997741568 available bytes; 98.72% used; 110410441 free inodes.

server2 `/home`: 22997741568 available bytes; 98.72% used; 110410441 free inodes.

server2 `/tmp`: 22997741568 available bytes; 98.72% used; 110410441 free inodes.

server2 `/var/tmp`: 22997741568 available bytes; 98.72% used; 110410441 free inodes.

server2 `/mnt/raid5`: 466208796672 available bytes; 96.78% used; 445113136 free inodes.
| server3 | True | [] | [] | reference_compatible=True |

server3 `/`: 84345937920 available bytes; 95.29% used; 114156075 free inodes.

server3 `/home`: 84345937920 available bytes; 95.29% used; 114156075 free inodes.

server3 `/data`: 145065406464 available bytes; 98.00% used; 225810508 free inodes.

server3 `/tmp`: 84345937920 available bytes; 95.29% used; 114156075 free inodes.

server3 `/var/tmp`: 84345937920 available bytes; 95.29% used; 114156075 free inodes.
| server4 | True | ['2', '3', '4', '6', '7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 105693401088 available bytes; 94.10% used; 114350910 free inodes.

server4 `/home`: 105693401088 available bytes; 94.10% used; 114350910 free inodes.

server4 `/data`: 52371124224 available bytes; 99.28% used; 224967486 free inodes.

server4 `/tmp`: 105693401088 available bytes; 94.10% used; 114350910 free inodes.

server4 `/var/tmp`: 105693401088 available bytes; 94.10% used; 114350910 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
