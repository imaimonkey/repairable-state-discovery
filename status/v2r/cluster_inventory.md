# V2R cluster inventory

2026-09-25T05:56:45.895141+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | [] | ['/tmp', '/var/tmp'] |

server1 `/`: 318869164032 available bytes; 82.21% used; 112480336 free inodes.

server1 `/home`: 318869164032 available bytes; 82.21% used; 112480336 free inodes.

server1 `/tmp`: 318869164032 available bytes; 82.21% used; 112480336 free inodes.

server1 `/var/tmp`: 318869164032 available bytes; 82.21% used; 112480336 free inodes.

server1 `/mnt/raid5`: 408419569664 available bytes; 98.13% used; 337565097 free inodes.
| server2 | True | [] | [] |

server2 `/`: 22905610240 available bytes; 98.72% used; 110410355 free inodes.

server2 `/home`: 22905610240 available bytes; 98.72% used; 110410355 free inodes.

server2 `/tmp`: 22905610240 available bytes; 98.72% used; 110410355 free inodes.

server2 `/var/tmp`: 22905610240 available bytes; 98.72% used; 110410355 free inodes.

server2 `/mnt/raid5`: 393350819840 available bytes; 97.28% used; 445101226 free inodes.
| server3 | True | [] | [] |

server3 `/`: 84315017216 available bytes; 95.29% used; 114156039 free inodes.

server3 `/home`: 84315017216 available bytes; 95.29% used; 114156039 free inodes.

server3 `/data`: 142772793344 available bytes; 98.03% used; 225814362 free inodes.

server3 `/tmp`: 84315017216 available bytes; 95.29% used; 114156039 free inodes.

server3 `/var/tmp`: 84315017216 available bytes; 95.29% used; 114156039 free inodes.
| server4 | True | ['3'] | ['/tmp', '/var/tmp'] |

server4 `/`: 105649201152 available bytes; 94.10% used; 114350386 free inodes.

server4 `/home`: 105649201152 available bytes; 94.10% used; 114350386 free inodes.

server4 `/data`: 256293609472 available bytes; 96.46% used; 225026283 free inodes.

server4 `/tmp`: 105649201152 available bytes; 94.10% used; 114350386 free inodes.

server4 `/var/tmp`: 105649201152 available bytes; 94.10% used; 114350386 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
