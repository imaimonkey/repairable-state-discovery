# V2R cluster inventory

2026-09-25T06:41:28.566333+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | [] | ['/tmp', '/var/tmp'] |

server1 `/`: 318873346048 available bytes; 82.21% used; 112480357 free inodes.

server1 `/home`: 318873346048 available bytes; 82.21% used; 112480357 free inodes.

server1 `/tmp`: 318873346048 available bytes; 82.21% used; 112480357 free inodes.

server1 `/var/tmp`: 318873346048 available bytes; 82.21% used; 112480357 free inodes.

server1 `/mnt/raid5`: 399788666880 available bytes; 98.17% used; 337561374 free inodes.
| server2 | True | [] | [] |

server2 `/`: 22885789696 available bytes; 98.72% used; 110410542 free inodes.

server2 `/home`: 22885789696 available bytes; 98.72% used; 110410542 free inodes.

server2 `/tmp`: 22885789696 available bytes; 98.72% used; 110410542 free inodes.

server2 `/var/tmp`: 22885789696 available bytes; 98.72% used; 110410542 free inodes.

server2 `/mnt/raid5`: 355548332032 available bytes; 97.54% used; 445099116 free inodes.
| server3 | True | [] | [] |

server3 `/`: 84449935360 available bytes; 95.29% used; 114156029 free inodes.

server3 `/home`: 84449935360 available bytes; 95.29% used; 114156029 free inodes.

server3 `/data`: 142530818048 available bytes; 98.03% used; 225813567 free inodes.

server3 `/tmp`: 84449935360 available bytes; 95.29% used; 114156029 free inodes.

server3 `/var/tmp`: 84449935360 available bytes; 95.29% used; 114156029 free inodes.
| server4 | True | ['3'] | ['/tmp', '/var/tmp'] |

server4 `/`: 105639432192 available bytes; 94.10% used; 114350384 free inodes.

server4 `/home`: 105639432192 available bytes; 94.10% used; 114350384 free inodes.

server4 `/data`: 251128168448 available bytes; 96.53% used; 225018926 free inodes.

server4 `/tmp`: 105639432192 available bytes; 94.10% used; 114350384 free inodes.

server4 `/var/tmp`: 105639432192 available bytes; 94.10% used; 114350384 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
