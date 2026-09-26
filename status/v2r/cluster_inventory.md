# V2R cluster inventory

2026-09-26T05:16:00.163432+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | ['1', '4', '5', '6', '7'] | ['/tmp', '/var/tmp'] |

server1 `/`: 318398488576 available bytes; 82.24% used; 112476279 free inodes.

server1 `/home`: 318398488576 available bytes; 82.24% used; 112476279 free inodes.

server1 `/tmp`: 318398488576 available bytes; 82.24% used; 112476279 free inodes.

server1 `/var/tmp`: 318398488576 available bytes; 82.24% used; 112476279 free inodes.

server1 `/mnt/raid5`: 307464638464 available bytes; 98.59% used; 337542811 free inodes.
| server2 | True | [] | [] |

server2 `/`: 22921633792 available bytes; 98.72% used; 110406197 free inodes.

server2 `/home`: 22921633792 available bytes; 98.72% used; 110406197 free inodes.

server2 `/tmp`: 22921633792 available bytes; 98.72% used; 110406197 free inodes.

server2 `/var/tmp`: 22921633792 available bytes; 98.72% used; 110406197 free inodes.

server2 `/mnt/raid5`: 263435743232 available bytes; 98.18% used; 445048971 free inodes.
| server3 | True | ['3'] | [] |

server3 `/`: 84087816192 available bytes; 95.31% used; 114166106 free inodes.

server3 `/home`: 84087816192 available bytes; 95.31% used; 114166106 free inodes.

server3 `/data`: 124489015296 available bytes; 98.28% used; 225825041 free inodes.

server3 `/tmp`: 84087816192 available bytes; 95.31% used; 114166106 free inodes.

server3 `/var/tmp`: 84087816192 available bytes; 95.31% used; 114166106 free inodes.
| server4 | True | ['2', '3', '6', '7'] | ['/tmp', '/var/tmp'] |

server4 `/`: 106095341568 available bytes; 94.08% used; 114348204 free inodes.

server4 `/home`: 106095341568 available bytes; 94.08% used; 114348204 free inodes.

server4 `/data`: 106995253248 available bytes; 98.52% used; 224929206 free inodes.

server4 `/tmp`: 106095341568 available bytes; 94.08% used; 114348204 free inodes.

server4 `/var/tmp`: 106095341568 available bytes; 94.08% used; 114348204 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
