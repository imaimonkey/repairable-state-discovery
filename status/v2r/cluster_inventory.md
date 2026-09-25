# V2R cluster inventory

2026-09-25T00:20:43.882671+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | [] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 319088635904 available bytes; 82.20% used; 112480793 free inodes.

server1 `/home`: 319088635904 available bytes; 82.20% used; 112480793 free inodes.

server1 `/tmp`: 319088635904 available bytes; 82.20% used; 112480793 free inodes.

server1 `/var/tmp`: 319088635904 available bytes; 82.20% used; 112480793 free inodes.

server1 `/mnt/raid5`: 416872308736 available bytes; 98.09% used; 337620963 free inodes.
| server2 | True | [] | [] | reference_compatible=False |

server2 `/`: 23083601920 available bytes; 98.71% used; 110410783 free inodes.

server2 `/home`: 23083601920 available bytes; 98.71% used; 110410783 free inodes.

server2 `/tmp`: 23083601920 available bytes; 98.71% used; 110410783 free inodes.

server2 `/var/tmp`: 23083601920 available bytes; 98.71% used; 110410783 free inodes.

server2 `/mnt/raid5`: 502127734784 available bytes; 96.53% used; 445163185 free inodes.
| server3 | True | [] | [] | reference_compatible=True |

server3 `/`: 84355596288 available bytes; 95.29% used; 114156084 free inodes.

server3 `/home`: 84355596288 available bytes; 95.29% used; 114156084 free inodes.

server3 `/data`: 149044830208 available bytes; 97.94% used; 225813615 free inodes.

server3 `/tmp`: 84355596288 available bytes; 95.29% used; 114156084 free inodes.

server3 `/var/tmp`: 84355596288 available bytes; 95.29% used; 114156084 free inodes.
| server4 | True | ['0', '5', '7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 105789206528 available bytes; 94.10% used; 114348296 free inodes.

server4 `/home`: 105789206528 available bytes; 94.10% used; 114348296 free inodes.

server4 `/data`: 56789458944 available bytes; 99.22% used; 225070993 free inodes.

server4 `/tmp`: 105789206528 available bytes; 94.10% used; 114348296 free inodes.

server4 `/var/tmp`: 105789206528 available bytes; 94.10% used; 114348296 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
