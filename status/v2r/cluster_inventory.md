# V2R cluster inventory

2026-09-25T00:31:27.915246+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | [] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 319087214592 available bytes; 82.20% used; 112480776 free inodes.

server1 `/home`: 319087214592 available bytes; 82.20% used; 112480776 free inodes.

server1 `/tmp`: 319087214592 available bytes; 82.20% used; 112480776 free inodes.

server1 `/var/tmp`: 319087214592 available bytes; 82.20% used; 112480776 free inodes.

server1 `/mnt/raid5`: 416852451328 available bytes; 98.09% used; 337619723 free inodes.
| server2 | True | [] | [] | reference_compatible=False |

server2 `/`: 23080804352 available bytes; 98.71% used; 110410771 free inodes.

server2 `/home`: 23080804352 available bytes; 98.71% used; 110410771 free inodes.

server2 `/tmp`: 23080804352 available bytes; 98.71% used; 110410771 free inodes.

server2 `/var/tmp`: 23080804352 available bytes; 98.71% used; 110410771 free inodes.

server2 `/mnt/raid5`: 501772111872 available bytes; 96.53% used; 445162907 free inodes.
| server3 | True | [] | [] | reference_compatible=True |

server3 `/`: 84349833216 available bytes; 95.29% used; 114156084 free inodes.

server3 `/home`: 84349833216 available bytes; 95.29% used; 114156084 free inodes.

server3 `/data`: 148867284992 available bytes; 97.94% used; 225813422 free inodes.

server3 `/tmp`: 84349833216 available bytes; 95.29% used; 114156084 free inodes.

server3 `/var/tmp`: 84349833216 available bytes; 95.29% used; 114156084 free inodes.
| server4 | True | ['0', '5', '7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 105788911616 available bytes; 94.10% used; 114348296 free inodes.

server4 `/home`: 105788911616 available bytes; 94.10% used; 114348296 free inodes.

server4 `/data`: 56628117504 available bytes; 99.22% used; 225056327 free inodes.

server4 `/tmp`: 105788911616 available bytes; 94.10% used; 114348296 free inodes.

server4 `/var/tmp`: 105788911616 available bytes; 94.10% used; 114348296 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
