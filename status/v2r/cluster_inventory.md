# V2R cluster inventory

2026-09-26T05:28:13.930058+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | ['1', '4', '5', '6', '7'] | ['/tmp', '/var/tmp'] |

server1 `/`: 318794022912 available bytes; 82.22% used; 112476281 free inodes.

server1 `/home`: 318794022912 available bytes; 82.22% used; 112476281 free inodes.

server1 `/tmp`: 318794022912 available bytes; 82.22% used; 112476281 free inodes.

server1 `/var/tmp`: 318794022912 available bytes; 82.22% used; 112476281 free inodes.

server1 `/mnt/raid5`: 275072823296 available bytes; 98.74% used; 337541935 free inodes.
| server2 | True | [] | [] |

server2 `/`: 22919888896 available bytes; 98.72% used; 110406213 free inodes.

server2 `/home`: 22919888896 available bytes; 98.72% used; 110406213 free inodes.

server2 `/tmp`: 22919888896 available bytes; 98.72% used; 110406213 free inodes.

server2 `/var/tmp`: 22919888896 available bytes; 98.72% used; 110406213 free inodes.

server2 `/mnt/raid5`: 276076691456 available bytes; 98.09% used; 445048471 free inodes.
| server3 | True | [] | [] |

server3 `/`: 84038590464 available bytes; 95.31% used; 114166025 free inodes.

server3 `/home`: 84038590464 available bytes; 95.31% used; 114166025 free inodes.

server3 `/data`: 124355469312 available bytes; 98.28% used; 225824779 free inodes.

server3 `/tmp`: 84038590464 available bytes; 95.31% used; 114166025 free inodes.

server3 `/var/tmp`: 84038590464 available bytes; 95.31% used; 114166025 free inodes.
| server4 | True | ['2', '3', '6', '7'] | ['/tmp', '/var/tmp'] |

server4 `/`: 106094981120 available bytes; 94.08% used; 114348207 free inodes.

server4 `/home`: 106094981120 available bytes; 94.08% used; 114348207 free inodes.

server4 `/data`: 106991083520 available bytes; 98.52% used; 224929230 free inodes.

server4 `/tmp`: 106094981120 available bytes; 94.08% used; 114348207 free inodes.

server4 `/var/tmp`: 106094981120 available bytes; 94.08% used; 114348207 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
