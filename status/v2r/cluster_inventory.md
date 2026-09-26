# V2R cluster inventory

2026-09-26T16:09:46.685126+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | ['0', '3', '4', '5', '6', '7'] | ['/tmp', '/var/tmp'] |

server1 `/`: 318128230400 available bytes; 82.25% used; 112473902 free inodes.

server1 `/home`: 318128230400 available bytes; 82.25% used; 112473902 free inodes.

server1 `/tmp`: 318128230400 available bytes; 82.25% used; 112473902 free inodes.

server1 `/var/tmp`: 318128230400 available bytes; 82.25% used; 112473902 free inodes.

server1 `/mnt/raid5`: 654094032896 available bytes; 97.00% used; 337531404 free inodes.
| server2 | True | ['2', '7'] | [] |

server2 `/`: 18025119744 available bytes; 98.99% used; 110367512 free inodes.

server2 `/home`: 18025119744 available bytes; 98.99% used; 110367512 free inodes.

server2 `/tmp`: 18025119744 available bytes; 98.99% used; 110367512 free inodes.

server2 `/var/tmp`: 18025119744 available bytes; 98.99% used; 110367512 free inodes.

server2 `/mnt/raid5`: 608284934144 available bytes; 95.80% used; 444971671 free inodes.
| server3 | True | [] | [] |

server3 `/`: 81583026176 available bytes; 95.45% used; 114077158 free inodes.

server3 `/home`: 81583026176 available bytes; 95.45% used; 114077158 free inodes.

server3 `/data`: 1349386240000 available bytes; 81.35% used; 225830999 free inodes.

server3 `/tmp`: 81583026176 available bytes; 95.45% used; 114077158 free inodes.

server3 `/var/tmp`: 81583026176 available bytes; 95.45% used; 114077158 free inodes.
| server4 | True | ['0', '3', '5', '7'] | ['/tmp', '/var/tmp'] |

server4 `/`: 105953951744 available bytes; 94.09% used; 114347852 free inodes.

server4 `/home`: 105953951744 available bytes; 94.09% used; 114347852 free inodes.

server4 `/data`: 410716565504 available bytes; 94.32% used; 224825369 free inodes.

server4 `/tmp`: 105953951744 available bytes; 94.09% used; 114347852 free inodes.

server4 `/var/tmp`: 105953951744 available bytes; 94.09% used; 114347852 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
