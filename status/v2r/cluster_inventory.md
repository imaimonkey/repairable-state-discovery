# V2R cluster inventory

2026-09-26T02:38:39.433550+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | ['1', '4', '5', '6', '7'] | ['/tmp', '/var/tmp'] |

server1 `/`: 318418325504 available bytes; 82.24% used; 112476271 free inodes.

server1 `/home`: 318418325504 available bytes; 82.24% used; 112476271 free inodes.

server1 `/tmp`: 318418325504 available bytes; 82.24% used; 112476271 free inodes.

server1 `/var/tmp`: 318418325504 available bytes; 82.24% used; 112476271 free inodes.

server1 `/mnt/raid5`: 331159089152 available bytes; 98.48% used; 337546086 free inodes.
| server2 | True | [] | [] |

server2 `/`: 22941945856 available bytes; 98.72% used; 110406220 free inodes.

server2 `/home`: 22941945856 available bytes; 98.72% used; 110406220 free inodes.

server2 `/tmp`: 22941945856 available bytes; 98.72% used; 110406220 free inodes.

server2 `/var/tmp`: 22941945856 available bytes; 98.72% used; 110406220 free inodes.

server2 `/mnt/raid5`: 288731381760 available bytes; 98.00% used; 445054236 free inodes.
| server3 | True | [] | [] |

server3 `/`: 84318269440 available bytes; 95.29% used; 114152378 free inodes.

server3 `/home`: 84318269440 available bytes; 95.29% used; 114152378 free inodes.

server3 `/data`: 124786302976 available bytes; 98.28% used; 225816842 free inodes.

server3 `/tmp`: 84318269440 available bytes; 95.29% used; 114152378 free inodes.

server3 `/var/tmp`: 84318269440 available bytes; 95.29% used; 114152378 free inodes.
| server4 | True | ['3', '7'] | ['/tmp', '/var/tmp'] |

server4 `/`: 106022936576 available bytes; 94.08% used; 114348272 free inodes.

server4 `/home`: 106022936576 available bytes; 94.08% used; 114348272 free inodes.

server4 `/data`: 109800873984 available bytes; 98.48% used; 224915439 free inodes.

server4 `/tmp`: 106022936576 available bytes; 94.08% used; 114348272 free inodes.

server4 `/var/tmp`: 106022936576 available bytes; 94.08% used; 114348272 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
