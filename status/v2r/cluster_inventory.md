# V2R cluster inventory

2026-09-24T01:35:57.853251+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | ['4', '6', '7'] | ['/tmp', '/var/tmp'] |

server1 `/`: 325460430848 available bytes; 81.84% used; 112499505 free inodes.

server1 `/home`: 325460430848 available bytes; 81.84% used; 112499505 free inodes.

server1 `/tmp`: 325460430848 available bytes; 81.84% used; 112499505 free inodes.

server1 `/var/tmp`: 325460430848 available bytes; 81.84% used; 112499505 free inodes.

server1 `/mnt/raid5`: 873517154304 available bytes; 95.99% used; 337733932 free inodes.
| server2 | True | [] | [] |

server2 `/`: 40938954752 available bytes; 97.72% used; 110431947 free inodes.

server2 `/home`: 40938954752 available bytes; 97.72% used; 110431947 free inodes.

server2 `/tmp`: 40938954752 available bytes; 97.72% used; 110431947 free inodes.

server2 `/var/tmp`: 40938954752 available bytes; 97.72% used; 110431947 free inodes.

server2 `/mnt/raid5`: 530614804480 available bytes; 96.33% used; 445201412 free inodes.
| server3 | True | [] | ['/tmp', '/var/tmp'] |

server3 `/`: 292720984064 available bytes; 83.67% used; 114211255 free inodes.

server3 `/home`: 292720984064 available bytes; 83.67% used; 114211255 free inodes.

server3 `/data`: 61159710720 available bytes; 99.15% used; 225842134 free inodes.

server3 `/tmp`: 292720984064 available bytes; 83.67% used; 114211255 free inodes.

server3 `/var/tmp`: 292720984064 available bytes; 83.67% used; 114211255 free inodes.
| server4 | True | ['2', '3', '6', '7'] | ['/tmp', '/var/tmp'] |

server4 `/`: 105960488960 available bytes; 94.09% used; 114348724 free inodes.

server4 `/home`: 105960488960 available bytes; 94.09% used; 114348724 free inodes.

server4 `/data`: 290808213504 available bytes; 95.98% used; 225396963 free inodes.

server4 `/tmp`: 105960488960 available bytes; 94.09% used; 114348724 free inodes.

server4 `/var/tmp`: 105960488960 available bytes; 94.09% used; 114348724 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
