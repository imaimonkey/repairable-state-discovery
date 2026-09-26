# V2R cluster inventory

2026-09-26T15:53:00.083471+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | ['3', '4', '5', '6', '7'] | ['/tmp', '/var/tmp'] |

server1 `/`: 318138466304 available bytes; 82.25% used; 112473919 free inodes.

server1 `/home`: 318138466304 available bytes; 82.25% used; 112473919 free inodes.

server1 `/tmp`: 318138466304 available bytes; 82.25% used; 112473919 free inodes.

server1 `/var/tmp`: 318138466304 available bytes; 82.25% used; 112473919 free inodes.

server1 `/mnt/raid5`: 654095695872 available bytes; 97.00% used; 337531400 free inodes.
| server2 | True | ['2', '7'] | [] |

server2 `/`: 18029125632 available bytes; 98.99% used; 110367508 free inodes.

server2 `/home`: 18029125632 available bytes; 98.99% used; 110367508 free inodes.

server2 `/tmp`: 18029125632 available bytes; 98.99% used; 110367508 free inodes.

server2 `/var/tmp`: 18029125632 available bytes; 98.99% used; 110367508 free inodes.

server2 `/mnt/raid5`: 608771633152 available bytes; 95.79% used; 444972180 free inodes.
| server3 | True | [] | [] |

server3 `/`: 82151698432 available bytes; 95.42% used; 114093401 free inodes.

server3 `/home`: 82151698432 available bytes; 95.42% used; 114093401 free inodes.

server3 `/data`: 1349440856064 available bytes; 81.35% used; 225832157 free inodes.

server3 `/tmp`: 82151698432 available bytes; 95.42% used; 114093401 free inodes.

server3 `/var/tmp`: 82151698432 available bytes; 95.42% used; 114093401 free inodes.
| server4 | True | ['0', '3', '5', '7'] | ['/tmp', '/var/tmp'] |

server4 `/`: 105954312192 available bytes; 94.09% used; 114347852 free inodes.

server4 `/home`: 105954312192 available bytes; 94.09% used; 114347852 free inodes.

server4 `/data`: 410717196288 available bytes; 94.32% used; 224825367 free inodes.

server4 `/tmp`: 105954312192 available bytes; 94.09% used; 114347852 free inodes.

server4 `/var/tmp`: 105954312192 available bytes; 94.09% used; 114347852 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
