# V2R cluster inventory

2026-09-24T23:39:25.933683+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | [] | ['/tmp', '/var/tmp'] |

server1 `/`: 319013195776 available bytes; 82.20% used; 112480783 free inodes.

server1 `/home`: 319013195776 available bytes; 82.20% used; 112480783 free inodes.

server1 `/tmp`: 319013195776 available bytes; 82.20% used; 112480783 free inodes.

server1 `/var/tmp`: 319013195776 available bytes; 82.20% used; 112480783 free inodes.

server1 `/mnt/raid5`: 394567172096 available bytes; 98.19% used; 337612138 free inodes.
| server2 | True | [] | [] |

server2 `/`: 23111716864 available bytes; 98.71% used; 110410810 free inodes.

server2 `/home`: 23111716864 available bytes; 98.71% used; 110410810 free inodes.

server2 `/tmp`: 23111716864 available bytes; 98.71% used; 110410810 free inodes.

server2 `/var/tmp`: 23111716864 available bytes; 98.71% used; 110410810 free inodes.

server2 `/mnt/raid5`: 486108422144 available bytes; 96.64% used; 445150759 free inodes.
| server3 | True | [] | [] |

server3 `/`: 84361375744 available bytes; 95.29% used; 114156081 free inodes.

server3 `/home`: 84361375744 available bytes; 95.29% used; 114156081 free inodes.

server3 `/data`: 148047126528 available bytes; 97.95% used; 225800742 free inodes.

server3 `/tmp`: 84361375744 available bytes; 95.29% used; 114156081 free inodes.

server3 `/var/tmp`: 84361375744 available bytes; 95.29% used; 114156081 free inodes.
| server4 | True | ['7'] | ['/tmp', '/var/tmp'] |

server4 `/`: 105799315456 available bytes; 94.10% used; 114348296 free inodes.

server4 `/home`: 105799315456 available bytes; 94.10% used; 114348296 free inodes.

server4 `/data`: 61103677440 available bytes; 99.16% used; 225133763 free inodes.

server4 `/tmp`: 105799315456 available bytes; 94.10% used; 114348296 free inodes.

server4 `/var/tmp`: 105799315456 available bytes; 94.10% used; 114348296 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
