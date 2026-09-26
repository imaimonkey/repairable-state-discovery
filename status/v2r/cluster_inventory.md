# V2R cluster inventory

2026-09-26T05:31:18.510308+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | ['1', '4', '5', '6', '7'] | ['/tmp', '/var/tmp'] |

server1 `/`: 318792503296 available bytes; 82.22% used; 112476275 free inodes.

server1 `/home`: 318792503296 available bytes; 82.22% used; 112476275 free inodes.

server1 `/tmp`: 318792503296 available bytes; 82.22% used; 112476275 free inodes.

server1 `/var/tmp`: 318792503296 available bytes; 82.22% used; 112476275 free inodes.

server1 `/mnt/raid5`: 265486295040 available bytes; 98.78% used; 337541582 free inodes.
| server2 | True | [] | [] |

server2 `/`: 22921723904 available bytes; 98.72% used; 110406217 free inodes.

server2 `/home`: 22921723904 available bytes; 98.72% used; 110406217 free inodes.

server2 `/tmp`: 22921723904 available bytes; 98.72% used; 110406217 free inodes.

server2 `/var/tmp`: 22921723904 available bytes; 98.72% used; 110406217 free inodes.

server2 `/mnt/raid5`: 275924000768 available bytes; 98.09% used; 445048339 free inodes.
| server3 | True | [] | [] |

server3 `/`: 83879460864 available bytes; 95.32% used; 114160875 free inodes.

server3 `/home`: 83879460864 available bytes; 95.32% used; 114160875 free inodes.

server3 `/data`: 124352880640 available bytes; 98.28% used; 225824635 free inodes.

server3 `/tmp`: 83879460864 available bytes; 95.32% used; 114160875 free inodes.

server3 `/var/tmp`: 83879460864 available bytes; 95.32% used; 114160875 free inodes.
| server4 | True | ['2', '3', '6', '7'] | ['/tmp', '/var/tmp'] |

server4 `/`: 106094882816 available bytes; 94.08% used; 114348210 free inodes.

server4 `/home`: 106094882816 available bytes; 94.08% used; 114348210 free inodes.

server4 `/data`: 106991972352 available bytes; 98.52% used; 224929230 free inodes.

server4 `/tmp`: 106094882816 available bytes; 94.08% used; 114348210 free inodes.

server4 `/var/tmp`: 106094882816 available bytes; 94.08% used; 114348210 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
