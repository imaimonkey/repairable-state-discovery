# V2R cluster inventory

2026-09-26T15:54:31.597998+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | ['3', '4', '5', '6', '7'] | ['/tmp', '/var/tmp'] |

server1 `/`: 318137876480 available bytes; 82.25% used; 112473919 free inodes.

server1 `/home`: 318137876480 available bytes; 82.25% used; 112473919 free inodes.

server1 `/tmp`: 318137876480 available bytes; 82.25% used; 112473919 free inodes.

server1 `/var/tmp`: 318137876480 available bytes; 82.25% used; 112473919 free inodes.

server1 `/mnt/raid5`: 654093545472 available bytes; 97.00% used; 337531404 free inodes.
| server2 | True | ['2', '7'] | [] |

server2 `/`: 18028486656 available bytes; 98.99% used; 110367508 free inodes.

server2 `/home`: 18028486656 available bytes; 98.99% used; 110367508 free inodes.

server2 `/tmp`: 18028486656 available bytes; 98.99% used; 110367508 free inodes.

server2 `/var/tmp`: 18028486656 available bytes; 98.99% used; 110367508 free inodes.

server2 `/mnt/raid5`: 608722153472 available bytes; 95.79% used; 444972109 free inodes.
| server3 | True | [] | [] |

server3 `/`: 82151251968 available bytes; 95.42% used; 114093399 free inodes.

server3 `/home`: 82151251968 available bytes; 95.42% used; 114093399 free inodes.

server3 `/data`: 1349440565248 available bytes; 81.35% used; 225832114 free inodes.

server3 `/tmp`: 82151251968 available bytes; 95.42% used; 114093399 free inodes.

server3 `/var/tmp`: 82151251968 available bytes; 95.42% used; 114093399 free inodes.
| server4 | True | ['0', '3', '5', '7'] | ['/tmp', '/var/tmp'] |

server4 `/`: 105954299904 available bytes; 94.09% used; 114347852 free inodes.

server4 `/home`: 105954299904 available bytes; 94.09% used; 114347852 free inodes.

server4 `/data`: 410716098560 available bytes; 94.32% used; 224825367 free inodes.

server4 `/tmp`: 105954299904 available bytes; 94.09% used; 114347852 free inodes.

server4 `/var/tmp`: 105954299904 available bytes; 94.09% used; 114347852 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
