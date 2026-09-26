# V2R cluster inventory

2026-09-26T05:17:31.866264+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | ['1', '4', '5', '6', '7'] | ['/tmp', '/var/tmp'] |

server1 `/`: 318397853696 available bytes; 82.24% used; 112476277 free inodes.

server1 `/home`: 318397853696 available bytes; 82.24% used; 112476277 free inodes.

server1 `/tmp`: 318397853696 available bytes; 82.24% used; 112476277 free inodes.

server1 `/var/tmp`: 318397853696 available bytes; 82.24% used; 112476277 free inodes.

server1 `/mnt/raid5`: 304202600448 available bytes; 98.60% used; 337542788 free inodes.
| server2 | True | [] | [] |

server2 `/`: 22922346496 available bytes; 98.72% used; 110406197 free inodes.

server2 `/home`: 22922346496 available bytes; 98.72% used; 110406197 free inodes.

server2 `/tmp`: 22922346496 available bytes; 98.72% used; 110406197 free inodes.

server2 `/var/tmp`: 22922346496 available bytes; 98.72% used; 110406197 free inodes.

server2 `/mnt/raid5`: 263406108672 available bytes; 98.18% used; 445049203 free inodes.
| server3 | True | [] | [] |

server3 `/`: 84085948416 available bytes; 95.31% used; 114166083 free inodes.

server3 `/home`: 84085948416 available bytes; 95.31% used; 114166083 free inodes.

server3 `/data`: 124362940416 available bytes; 98.28% used; 225824967 free inodes.

server3 `/tmp`: 84085948416 available bytes; 95.31% used; 114166083 free inodes.

server3 `/var/tmp`: 84085948416 available bytes; 95.31% used; 114166083 free inodes.
| server4 | True | ['2', '3', '6', '7'] | ['/tmp', '/var/tmp'] |

server4 `/`: 106095296512 available bytes; 94.08% used; 114348206 free inodes.

server4 `/home`: 106095296512 available bytes; 94.08% used; 114348206 free inodes.

server4 `/data`: 106993811456 available bytes; 98.52% used; 224929205 free inodes.

server4 `/tmp`: 106095296512 available bytes; 94.08% used; 114348206 free inodes.

server4 `/var/tmp`: 106095296512 available bytes; 94.08% used; 114348206 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
