# V2R cluster inventory

2026-09-26T05:20:35.239503+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | ['1', '4', '5', '6', '7'] | ['/tmp', '/var/tmp'] |

server1 `/`: 318399660032 available bytes; 82.24% used; 112476279 free inodes.

server1 `/home`: 318399660032 available bytes; 82.24% used; 112476279 free inodes.

server1 `/tmp`: 318399660032 available bytes; 82.24% used; 112476279 free inodes.

server1 `/var/tmp`: 318399660032 available bytes; 82.24% used; 112476279 free inodes.

server1 `/mnt/raid5`: 296940810240 available bytes; 98.64% used; 337542678 free inodes.
| server2 | True | [] | [] |

server2 `/`: 22920486912 available bytes; 98.72% used; 110406203 free inodes.

server2 `/home`: 22920486912 available bytes; 98.72% used; 110406203 free inodes.

server2 `/tmp`: 22920486912 available bytes; 98.72% used; 110406203 free inodes.

server2 `/var/tmp`: 22920486912 available bytes; 98.72% used; 110406203 free inodes.

server2 `/mnt/raid5`: 283953926144 available bytes; 98.04% used; 445048872 free inodes.
| server3 | True | [] | [] |

server3 `/`: 84062887936 available bytes; 95.31% used; 114166019 free inodes.

server3 `/home`: 84062887936 available bytes; 95.31% used; 114166019 free inodes.

server3 `/data`: 124361240576 available bytes; 98.28% used; 225824906 free inodes.

server3 `/tmp`: 84062887936 available bytes; 95.31% used; 114166019 free inodes.

server3 `/var/tmp`: 84062887936 available bytes; 95.31% used; 114166019 free inodes.
| server4 | True | ['2', '3', '6', '7'] | ['/tmp', '/var/tmp'] |

server4 `/`: 106095194112 available bytes; 94.08% used; 114348206 free inodes.

server4 `/home`: 106095194112 available bytes; 94.08% used; 114348206 free inodes.

server4 `/data`: 106995650560 available bytes; 98.52% used; 224929223 free inodes.

server4 `/tmp`: 106095194112 available bytes; 94.08% used; 114348206 free inodes.

server4 `/var/tmp`: 106095194112 available bytes; 94.08% used; 114348206 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
