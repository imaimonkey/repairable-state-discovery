# V2R cluster inventory

2026-09-25T22:20:22.641631+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | ['4', '6', '7'] | ['/tmp', '/var/tmp'] |

server1 `/`: 318697492480 available bytes; 82.22% used; 112476303 free inodes.

server1 `/home`: 318697492480 available bytes; 82.22% used; 112476303 free inodes.

server1 `/tmp`: 318697492480 available bytes; 82.22% used; 112476303 free inodes.

server1 `/var/tmp`: 318697492480 available bytes; 82.22% used; 112476303 free inodes.

server1 `/mnt/raid5`: 360260661248 available bytes; 98.35% used; 337538981 free inodes.
| server2 | True | ['2'] | [] |

server2 `/`: 22947606528 available bytes; 98.72% used; 110406236 free inodes.

server2 `/home`: 22947606528 available bytes; 98.72% used; 110406236 free inodes.

server2 `/tmp`: 22947606528 available bytes; 98.72% used; 110406236 free inodes.

server2 `/var/tmp`: 22947606528 available bytes; 98.72% used; 110406236 free inodes.

server2 `/mnt/raid5`: 299254013952 available bytes; 97.93% used; 445053147 free inodes.
| server3 | True | [] | [] |

server3 `/`: 84356915200 available bytes; 95.29% used; 114152554 free inodes.

server3 `/home`: 84356915200 available bytes; 95.29% used; 114152554 free inodes.

server3 `/data`: 124825513984 available bytes; 98.27% used; 225806134 free inodes.

server3 `/tmp`: 84356915200 available bytes; 95.29% used; 114152554 free inodes.

server3 `/var/tmp`: 84356915200 available bytes; 95.29% used; 114152554 free inodes.
| server4 | True | ['3', '7'] | ['/tmp', '/var/tmp'] |

server4 `/`: 105311911936 available bytes; 94.12% used; 114347141 free inodes.

server4 `/home`: 105311911936 available bytes; 94.12% used; 114347141 free inodes.

server4 `/data`: 204905721856 available bytes; 97.17% used; 224917883 free inodes.

server4 `/tmp`: 105311911936 available bytes; 94.12% used; 114347141 free inodes.

server4 `/var/tmp`: 105311911936 available bytes; 94.12% used; 114347141 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
