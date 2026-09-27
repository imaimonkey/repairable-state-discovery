# V2R cluster inventory

2026-09-27T01:53:41.857931+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | ['1', '2', '3', '4', '5', '6', '7'] | ['/tmp', '/var/tmp'] |

server1 `/`: 315159343104 available bytes; 82.42% used; 112443366 free inodes.

server1 `/home`: 315159343104 available bytes; 82.42% used; 112443366 free inodes.

server1 `/tmp`: 315159343104 available bytes; 82.42% used; 112443366 free inodes.

server1 `/var/tmp`: 315159343104 available bytes; 82.42% used; 112443366 free inodes.

server1 `/mnt/raid5`: 637480640512 available bytes; 97.08% used; 337405470 free inodes.
| server2 | True | [] | [] |

server2 `/`: 17635586048 available bytes; 99.02% used; 110364996 free inodes.

server2 `/home`: 17635586048 available bytes; 99.02% used; 110364996 free inodes.

server2 `/tmp`: 17635586048 available bytes; 99.02% used; 110364996 free inodes.

server2 `/var/tmp`: 17635586048 available bytes; 99.02% used; 110364996 free inodes.

server2 `/mnt/raid5`: 582031257600 available bytes; 95.98% used; 444885982 free inodes.
| server3 | True | [] | [] |

server3 `/`: 78717014016 available bytes; 95.61% used; 114062953 free inodes.

server3 `/home`: 78717014016 available bytes; 95.61% used; 114062953 free inodes.

server3 `/data`: 1338786566144 available bytes; 81.50% used; 225762825 free inodes.

server3 `/tmp`: 78717014016 available bytes; 95.61% used; 114062953 free inodes.

server3 `/var/tmp`: 78717014016 available bytes; 95.61% used; 114062953 free inodes.
| server4 | True | ['3', '6', '7'] | ['/tmp', '/var/tmp'] |

server4 `/`: 105868763136 available bytes; 94.09% used; 114347816 free inodes.

server4 `/home`: 105868763136 available bytes; 94.09% used; 114347816 free inodes.

server4 `/data`: 406909599744 available bytes; 94.38% used; 224782888 free inodes.

server4 `/tmp`: 105868763136 available bytes; 94.09% used; 114347816 free inodes.

server4 `/var/tmp`: 105868763136 available bytes; 94.09% used; 114347816 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
