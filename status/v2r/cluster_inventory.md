# V2R cluster inventory

2026-09-25T05:52:08.540329+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | [] | ['/tmp', '/var/tmp'] |

server1 `/`: 318870163456 available bytes; 82.21% used; 112480335 free inodes.

server1 `/home`: 318870163456 available bytes; 82.21% used; 112480335 free inodes.

server1 `/tmp`: 318870163456 available bytes; 82.21% used; 112480335 free inodes.

server1 `/var/tmp`: 318870163456 available bytes; 82.21% used; 112480335 free inodes.

server1 `/mnt/raid5`: 408434761728 available bytes; 98.13% used; 337565646 free inodes.
| server2 | True | [] | [] |

server2 `/`: 22911569920 available bytes; 98.72% used; 110410371 free inodes.

server2 `/home`: 22911569920 available bytes; 98.72% used; 110410371 free inodes.

server2 `/tmp`: 22911569920 available bytes; 98.72% used; 110410371 free inodes.

server2 `/var/tmp`: 22911569920 available bytes; 98.72% used; 110410371 free inodes.

server2 `/mnt/raid5`: 407578062848 available bytes; 97.18% used; 445101661 free inodes.
| server3 | True | [] | [] |

server3 `/`: 84312694784 available bytes; 95.30% used; 114156039 free inodes.

server3 `/home`: 84312694784 available bytes; 95.30% used; 114156039 free inodes.

server3 `/data`: 142774284288 available bytes; 98.03% used; 225814426 free inodes.

server3 `/tmp`: 84312694784 available bytes; 95.30% used; 114156039 free inodes.

server3 `/var/tmp`: 84312694784 available bytes; 95.30% used; 114156039 free inodes.
| server4 | True | ['3'] | ['/tmp', '/var/tmp'] |

server4 `/`: 105649340416 available bytes; 94.10% used; 114350387 free inodes.

server4 `/home`: 105649340416 available bytes; 94.10% used; 114350387 free inodes.

server4 `/data`: 256304906240 available bytes; 96.46% used; 225027029 free inodes.

server4 `/tmp`: 105649340416 available bytes; 94.10% used; 114350387 free inodes.

server4 `/var/tmp`: 105649340416 available bytes; 94.10% used; 114350387 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
