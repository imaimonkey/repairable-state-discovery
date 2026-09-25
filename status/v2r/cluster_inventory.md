# V2R cluster inventory

2026-09-25T20:42:34.778350+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | ['4', '6', '7'] | ['/tmp', '/var/tmp'] |

server1 `/`: 318710009856 available bytes; 82.22% used; 112476326 free inodes.

server1 `/home`: 318710009856 available bytes; 82.22% used; 112476326 free inodes.

server1 `/tmp`: 318710009856 available bytes; 82.22% used; 112476326 free inodes.

server1 `/var/tmp`: 318710009856 available bytes; 82.22% used; 112476326 free inodes.

server1 `/mnt/raid5`: 368663715840 available bytes; 98.31% used; 337539865 free inodes.
| server2 | True | ['4', '5', '6'] | [] |

server2 `/`: 22953934848 available bytes; 98.72% used; 110406242 free inodes.

server2 `/home`: 22953934848 available bytes; 98.72% used; 110406242 free inodes.

server2 `/tmp`: 22953934848 available bytes; 98.72% used; 110406242 free inodes.

server2 `/var/tmp`: 22953934848 available bytes; 98.72% used; 110406242 free inodes.

server2 `/mnt/raid5`: 302931963904 available bytes; 97.91% used; 445056867 free inodes.
| server3 | True | [] | [] |

server3 `/`: 84381544448 available bytes; 95.29% used; 114152622 free inodes.

server3 `/home`: 84381544448 available bytes; 95.29% used; 114152622 free inodes.

server3 `/data`: 127168389120 available bytes; 98.24% used; 225807835 free inodes.

server3 `/tmp`: 84381544448 available bytes; 95.29% used; 114152622 free inodes.

server3 `/var/tmp`: 84381544448 available bytes; 95.29% used; 114152622 free inodes.
| server4 | True | ['2', '3', '6', '7'] | ['/tmp', '/var/tmp'] |

server4 `/`: 105655713792 available bytes; 94.10% used; 114349549 free inodes.

server4 `/home`: 105655713792 available bytes; 94.10% used; 114349549 free inodes.

server4 `/data`: 228184551424 available bytes; 96.85% used; 224928306 free inodes.

server4 `/tmp`: 105655713792 available bytes; 94.10% used; 114349549 free inodes.

server4 `/var/tmp`: 105655713792 available bytes; 94.10% used; 114349549 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
