# V2R cluster inventory

2026-09-25T00:21:03.863083+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | [] | ['/tmp', '/var/tmp'] |

server1 `/`: 319088513024 available bytes; 82.20% used; 112480793 free inodes.

server1 `/home`: 319088513024 available bytes; 82.20% used; 112480793 free inodes.

server1 `/tmp`: 319088513024 available bytes; 82.20% used; 112480793 free inodes.

server1 `/var/tmp`: 319088513024 available bytes; 82.20% used; 112480793 free inodes.

server1 `/mnt/raid5`: 416871333888 available bytes; 98.09% used; 337620925 free inodes.
| server2 | True | [] | [] |

server2 `/`: 23083298816 available bytes; 98.71% used; 110410783 free inodes.

server2 `/home`: 23083298816 available bytes; 98.71% used; 110410783 free inodes.

server2 `/tmp`: 23083298816 available bytes; 98.71% used; 110410783 free inodes.

server2 `/var/tmp`: 23083298816 available bytes; 98.71% used; 110410783 free inodes.

server2 `/mnt/raid5`: 502122975232 available bytes; 96.53% used; 445163374 free inodes.
| server3 | True | [] | [] |

server3 `/`: 84355334144 available bytes; 95.29% used; 114156084 free inodes.

server3 `/home`: 84355334144 available bytes; 95.29% used; 114156084 free inodes.

server3 `/data`: 149037768704 available bytes; 97.94% used; 225813597 free inodes.

server3 `/tmp`: 84355334144 available bytes; 95.29% used; 114156084 free inodes.

server3 `/var/tmp`: 84355334144 available bytes; 95.29% used; 114156084 free inodes.
| server4 | True | ['0', '5', '7'] | ['/tmp', '/var/tmp'] |

server4 `/`: 105789202432 available bytes; 94.10% used; 114348296 free inodes.

server4 `/home`: 105789202432 available bytes; 94.10% used; 114348296 free inodes.

server4 `/data`: 56782364672 available bytes; 99.22% used; 225070517 free inodes.

server4 `/tmp`: 105789202432 available bytes; 94.10% used; 114348296 free inodes.

server4 `/var/tmp`: 105789202432 available bytes; 94.10% used; 114348296 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
