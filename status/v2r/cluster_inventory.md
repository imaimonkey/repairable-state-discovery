# V2R cluster inventory

2026-09-27T00:11:33.150696+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | ['1', '2', '3', '4', '5', '6', '7'] | ['/tmp', '/var/tmp'] |

server1 `/`: 315086229504 available bytes; 82.42% used; 112443702 free inodes.

server1 `/home`: 315086229504 available bytes; 82.42% used; 112443702 free inodes.

server1 `/tmp`: 315086229504 available bytes; 82.42% used; 112443702 free inodes.

server1 `/var/tmp`: 315086229504 available bytes; 82.42% used; 112443702 free inodes.

server1 `/mnt/raid5`: 637712486400 available bytes; 97.07% used; 337408130 free inodes.
| server2 | True | ['7'] | [] |

server2 `/`: 17937555456 available bytes; 99.00% used; 110367424 free inodes.

server2 `/home`: 17937555456 available bytes; 99.00% used; 110367424 free inodes.

server2 `/tmp`: 17937555456 available bytes; 99.00% used; 110367424 free inodes.

server2 `/var/tmp`: 17937555456 available bytes; 99.00% used; 110367424 free inodes.

server2 `/mnt/raid5`: 593634316288 available bytes; 95.90% used; 444957704 free inodes.
| server3 | True | ['3'] | [] |

server3 `/`: 79774281728 available bytes; 95.55% used; 114068847 free inodes.

server3 `/home`: 79774277632 available bytes; 95.55% used; 114068847 free inodes.

server3 `/data`: 1349112709120 available bytes; 81.35% used; 225825902 free inodes.

server3 `/tmp`: 79774277632 available bytes; 95.55% used; 114068847 free inodes.

server3 `/var/tmp`: 79774277632 available bytes; 95.55% used; 114068847 free inodes.
| server4 | True | ['2', '3', '6', '7'] | ['/tmp', '/var/tmp'] |

server4 `/`: 105879842816 available bytes; 94.09% used; 114347853 free inodes.

server4 `/home`: 105879842816 available bytes; 94.09% used; 114347853 free inodes.

server4 `/data`: 409573462016 available bytes; 94.34% used; 224823737 free inodes.

server4 `/tmp`: 105879842816 available bytes; 94.09% used; 114347853 free inodes.

server4 `/var/tmp`: 105879842816 available bytes; 94.09% used; 114347853 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
