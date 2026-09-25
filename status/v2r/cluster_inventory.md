# V2R cluster inventory

2026-09-25T12:14:29.125648+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | [] | ['/tmp', '/var/tmp'] |

server1 `/`: 319201812480 available bytes; 82.19% used; 112477788 free inodes.

server1 `/home`: 319201812480 available bytes; 82.19% used; 112477788 free inodes.

server1 `/tmp`: 319201812480 available bytes; 82.19% used; 112477788 free inodes.

server1 `/var/tmp`: 319201812480 available bytes; 82.19% used; 112477788 free inodes.

server1 `/mnt/raid5`: 364324597760 available bytes; 98.33% used; 337548323 free inodes.
| server2 | True | ['2', '3', '4', '5', '6'] | [] |

server2 `/`: 22902095872 available bytes; 98.72% used; 110409955 free inodes.

server2 `/home`: 22902095872 available bytes; 98.72% used; 110409955 free inodes.

server2 `/tmp`: 22902095872 available bytes; 98.72% used; 110409955 free inodes.

server2 `/var/tmp`: 22902095872 available bytes; 98.72% used; 110409955 free inodes.

server2 `/mnt/raid5`: 325412626432 available bytes; 97.75% used; 445080974 free inodes.
| server3 | True | [] | [] |

server3 `/`: 84210458624 available bytes; 95.30% used; 114154982 free inodes.

server3 `/home`: 84210458624 available bytes; 95.30% used; 114154982 free inodes.

server3 `/data`: 142280314880 available bytes; 98.03% used; 225811390 free inodes.

server3 `/tmp`: 84210458624 available bytes; 95.30% used; 114154982 free inodes.

server3 `/var/tmp`: 84210458624 available bytes; 95.30% used; 114154982 free inodes.
| server4 | True | [] | ['/tmp', '/var/tmp'] |

server4 `/`: 105666625536 available bytes; 94.10% used; 114349724 free inodes.

server4 `/home`: 105666625536 available bytes; 94.10% used; 114349724 free inodes.

server4 `/data`: 232050753536 available bytes; 96.79% used; 224966400 free inodes.

server4 `/tmp`: 105666625536 available bytes; 94.10% used; 114349724 free inodes.

server4 `/var/tmp`: 105666625536 available bytes; 94.10% used; 114349724 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
