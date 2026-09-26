# V2R cluster inventory

2026-09-26T05:23:38.843102+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | ['1', '4', '5', '6', '7'] | ['/tmp', '/var/tmp'] |

server1 `/`: 318400716800 available bytes; 82.24% used; 112476282 free inodes.

server1 `/home`: 318400716800 available bytes; 82.24% used; 112476282 free inodes.

server1 `/tmp`: 318400716800 available bytes; 82.24% used; 112476282 free inodes.

server1 `/var/tmp`: 318400716800 available bytes; 82.24% used; 112476282 free inodes.

server1 `/mnt/raid5`: 289040441344 available bytes; 98.67% used; 337542369 free inodes.
| server2 | True | [] | [] |

server2 `/`: 22920982528 available bytes; 98.72% used; 110406203 free inodes.

server2 `/home`: 22920982528 available bytes; 98.72% used; 110406203 free inodes.

server2 `/tmp`: 22920982528 available bytes; 98.72% used; 110406203 free inodes.

server2 `/var/tmp`: 22920982528 available bytes; 98.72% used; 110406203 free inodes.

server2 `/mnt/raid5`: 276983713792 available bytes; 98.09% used; 445048725 free inodes.
| server3 | True | [] | [] |

server3 `/`: 84088745984 available bytes; 95.31% used; 114166402 free inodes.

server3 `/home`: 84088745984 available bytes; 95.31% used; 114166402 free inodes.

server3 `/data`: 124362412032 available bytes; 98.28% used; 225824852 free inodes.

server3 `/tmp`: 84088745984 available bytes; 95.31% used; 114166402 free inodes.

server3 `/var/tmp`: 84088745984 available bytes; 95.31% used; 114166402 free inodes.
| server4 | True | ['2', '3', '6', '7'] | ['/tmp', '/var/tmp'] |

server4 `/`: 106095112192 available bytes; 94.08% used; 114348206 free inodes.

server4 `/home`: 106095112192 available bytes; 94.08% used; 114348206 free inodes.

server4 `/data`: 106993496064 available bytes; 98.52% used; 224929223 free inodes.

server4 `/tmp`: 106095112192 available bytes; 94.08% used; 114348206 free inodes.

server4 `/var/tmp`: 106095112192 available bytes; 94.08% used; 114348206 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
