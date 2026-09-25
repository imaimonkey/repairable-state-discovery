# V2R cluster inventory

2026-09-25T03:52:00.083258+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | [] | ['/tmp', '/var/tmp'] |

server1 `/`: 318928236544 available bytes; 82.21% used; 112480352 free inodes.

server1 `/home`: 318928236544 available bytes; 82.21% used; 112480352 free inodes.

server1 `/tmp`: 318928236544 available bytes; 82.21% used; 112480352 free inodes.

server1 `/var/tmp`: 318928236544 available bytes; 82.21% used; 112480352 free inodes.

server1 `/mnt/raid5`: 415725154304 available bytes; 98.09% used; 337596280 free inodes.
| server2 | True | [] | [] |

server2 `/`: 22972198912 available bytes; 98.72% used; 110410440 free inodes.

server2 `/home`: 22972198912 available bytes; 98.72% used; 110410440 free inodes.

server2 `/tmp`: 22972198912 available bytes; 98.72% used; 110410440 free inodes.

server2 `/var/tmp`: 22972198912 available bytes; 98.72% used; 110410440 free inodes.

server2 `/mnt/raid5`: 464219414528 available bytes; 96.79% used; 445111089 free inodes.
| server3 | True | [] | [] |

server3 `/`: 84340785152 available bytes; 95.29% used; 114156062 free inodes.

server3 `/home`: 84340785152 available bytes; 95.29% used; 114156062 free inodes.

server3 `/data`: 144221458432 available bytes; 98.01% used; 225816944 free inodes.

server3 `/tmp`: 84340785152 available bytes; 95.29% used; 114156062 free inodes.

server3 `/var/tmp`: 84340785152 available bytes; 95.29% used; 114156062 free inodes.
| server4 | True | ['6', '7'] | ['/tmp', '/var/tmp'] |

server4 `/`: 105683165184 available bytes; 94.10% used; 114350901 free inodes.

server4 `/home`: 105683165184 available bytes; 94.10% used; 114350901 free inodes.

server4 `/data`: 38555820032 available bytes; 99.47% used; 224965023 free inodes.

server4 `/tmp`: 105683165184 available bytes; 94.10% used; 114350901 free inodes.

server4 `/var/tmp`: 105683165184 available bytes; 94.10% used; 114350901 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
