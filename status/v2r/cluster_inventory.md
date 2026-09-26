# V2R cluster inventory

2026-09-26T16:00:37.534947+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | ['3', '4', '5', '6', '7'] | ['/tmp', '/var/tmp'] |

server1 `/`: 318138998784 available bytes; 82.25% used; 112473911 free inodes.

server1 `/home`: 318138998784 available bytes; 82.25% used; 112473911 free inodes.

server1 `/tmp`: 318138998784 available bytes; 82.25% used; 112473911 free inodes.

server1 `/var/tmp`: 318138998784 available bytes; 82.25% used; 112473911 free inodes.

server1 `/mnt/raid5`: 654092812288 available bytes; 97.00% used; 337531404 free inodes.
| server2 | True | ['2', '7'] | [] |

server2 `/`: 18031001600 available bytes; 98.99% used; 110367516 free inodes.

server2 `/home`: 18031001600 available bytes; 98.99% used; 110367516 free inodes.

server2 `/tmp`: 18031001600 available bytes; 98.99% used; 110367516 free inodes.

server2 `/var/tmp`: 18031001600 available bytes; 98.99% used; 110367516 free inodes.

server2 `/mnt/raid5`: 608534421504 available bytes; 95.80% used; 444971958 free inodes.
| server3 | True | [] | [] |

server3 `/`: 82289119232 available bytes; 95.41% used; 114114001 free inodes.

server3 `/home`: 82289119232 available bytes; 95.41% used; 114114001 free inodes.

server3 `/data`: 1349411753984 available bytes; 81.35% used; 225831581 free inodes.

server3 `/tmp`: 82289119232 available bytes; 95.41% used; 114114001 free inodes.

server3 `/var/tmp`: 82289119232 available bytes; 95.41% used; 114114001 free inodes.
| server4 | True | ['0', '3', '5', '7'] | ['/tmp', '/var/tmp'] |

server4 `/`: 105954156544 available bytes; 94.09% used; 114347852 free inodes.

server4 `/home`: 105954156544 available bytes; 94.09% used; 114347852 free inodes.

server4 `/data`: 410716344320 available bytes; 94.32% used; 224825369 free inodes.

server4 `/tmp`: 105954156544 available bytes; 94.09% used; 114347852 free inodes.

server4 `/var/tmp`: 105954156544 available bytes; 94.09% used; 114347852 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
