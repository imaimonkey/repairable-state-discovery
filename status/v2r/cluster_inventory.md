# V2R cluster inventory

2026-09-25T22:12:44.334595+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | ['4', '6', '7'] | ['/tmp', '/var/tmp'] |

server1 `/`: 318692646912 available bytes; 82.22% used; 112476301 free inodes.

server1 `/home`: 318692646912 available bytes; 82.22% used; 112476301 free inodes.

server1 `/tmp`: 318692646912 available bytes; 82.22% used; 112476301 free inodes.

server1 `/var/tmp`: 318692646912 available bytes; 82.22% used; 112476301 free inodes.

server1 `/mnt/raid5`: 360285667328 available bytes; 98.35% used; 337539033 free inodes.
| server2 | True | ['2'] | [] |

server2 `/`: 22948089856 available bytes; 98.72% used; 110406244 free inodes.

server2 `/home`: 22948089856 available bytes; 98.72% used; 110406244 free inodes.

server2 `/tmp`: 22948089856 available bytes; 98.72% used; 110406244 free inodes.

server2 `/var/tmp`: 22948089856 available bytes; 98.72% used; 110406244 free inodes.

server2 `/mnt/raid5`: 299817930752 available bytes; 97.93% used; 445053502 free inodes.
| server3 | True | [] | [] |

server3 `/`: 84358209536 available bytes; 95.29% used; 114152630 free inodes.

server3 `/home`: 84358209536 available bytes; 95.29% used; 114152630 free inodes.

server3 `/data`: 125875388416 available bytes; 98.26% used; 225806275 free inodes.

server3 `/tmp`: 84358209536 available bytes; 95.29% used; 114152630 free inodes.

server3 `/var/tmp`: 84358209536 available bytes; 95.29% used; 114152630 free inodes.
| server4 | True | ['3', '7'] | ['/tmp', '/var/tmp'] |

server4 `/`: 105312165888 available bytes; 94.12% used; 114347146 free inodes.

server4 `/home`: 105312165888 available bytes; 94.12% used; 114347146 free inodes.

server4 `/data`: 208638394368 available bytes; 97.12% used; 224919030 free inodes.

server4 `/tmp`: 105312165888 available bytes; 94.12% used; 114347146 free inodes.

server4 `/var/tmp`: 105312165888 available bytes; 94.12% used; 114347146 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
