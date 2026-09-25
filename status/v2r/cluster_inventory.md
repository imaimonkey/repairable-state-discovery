# V2R cluster inventory

2026-09-25T03:50:28.091129+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | [] | ['/tmp', '/var/tmp'] |

server1 `/`: 318928424960 available bytes; 82.21% used; 112480352 free inodes.

server1 `/home`: 318928424960 available bytes; 82.21% used; 112480352 free inodes.

server1 `/tmp`: 318928424960 available bytes; 82.21% used; 112480352 free inodes.

server1 `/var/tmp`: 318928424960 available bytes; 82.21% used; 112480352 free inodes.

server1 `/mnt/raid5`: 415730462720 available bytes; 98.09% used; 337596464 free inodes.
| server2 | True | [] | [] |

server2 `/`: 22973063168 available bytes; 98.72% used; 110410440 free inodes.

server2 `/home`: 22973063168 available bytes; 98.72% used; 110410440 free inodes.

server2 `/tmp`: 22973063168 available bytes; 98.72% used; 110410440 free inodes.

server2 `/var/tmp`: 22973063168 available bytes; 98.72% used; 110410440 free inodes.

server2 `/mnt/raid5`: 464268754944 available bytes; 96.79% used; 445111158 free inodes.
| server3 | True | [] | [] |

server3 `/`: 84340924416 available bytes; 95.29% used; 114156062 free inodes.

server3 `/home`: 84340924416 available bytes; 95.29% used; 114156062 free inodes.

server3 `/data`: 144246341632 available bytes; 98.01% used; 225816998 free inodes.

server3 `/tmp`: 84340924416 available bytes; 95.29% used; 114156062 free inodes.

server3 `/var/tmp`: 84340924416 available bytes; 95.29% used; 114156062 free inodes.
| server4 | True | ['6', '7'] | ['/tmp', '/var/tmp'] |

server4 `/`: 105683202048 available bytes; 94.10% used; 114350901 free inodes.

server4 `/home`: 105683202048 available bytes; 94.10% used; 114350901 free inodes.

server4 `/data`: 38558490624 available bytes; 99.47% used; 224965082 free inodes.

server4 `/tmp`: 105683202048 available bytes; 94.10% used; 114350901 free inodes.

server4 `/var/tmp`: 105683202048 available bytes; 94.10% used; 114350901 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
