# V2R cluster inventory

2026-09-23T23:42:58.738184+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | [] | ['/tmp', '/var/tmp', '/mnt/raid5'] |

server1 `/`: 325609684992 available bytes; 81.84% used; 112501182 free inodes.

server1 `/home`: 325609684992 available bytes; 81.84% used; 112501182 free inodes.

server1 `/tmp`: 325609684992 available bytes; 81.84% used; 112501182 free inodes.

server1 `/var/tmp`: 325609684992 available bytes; 81.84% used; 112501182 free inodes.

server1 `/mnt/raid5`: 1339248984064 available bytes; 93.86% used; 337735840 free inodes.
| server2 | True | [] | [] |

server2 `/`: 41034604544 available bytes; 97.71% used; 110432515 free inodes.

server2 `/home`: 41034604544 available bytes; 97.71% used; 110432515 free inodes.

server2 `/tmp`: 41034604544 available bytes; 97.71% used; 110432515 free inodes.

server2 `/var/tmp`: 41034604544 available bytes; 97.71% used; 110432515 free inodes.

server2 `/mnt/raid5`: 534063013888 available bytes; 96.31% used; 445205051 free inodes.
| server3 | True | [] | ['/tmp', '/var/tmp'] |

server3 `/`: 292491636736 available bytes; 83.68% used; 114191260 free inodes.

server3 `/home`: 292491636736 available bytes; 83.68% used; 114191260 free inodes.

server3 `/data`: 82294325248 available bytes; 98.86% used; 225845191 free inodes.

server3 `/tmp`: 292491636736 available bytes; 83.68% used; 114191260 free inodes.

server3 `/var/tmp`: 292491636736 available bytes; 83.68% used; 114191260 free inodes.
| server4 | True | ['3', '6', '7'] | ['/tmp', '/var/tmp'] |

server4 `/`: 106192060416 available bytes; 94.07% used; 114351894 free inodes.

server4 `/home`: 106192060416 available bytes; 94.07% used; 114351894 free inodes.

server4 `/data`: 292990152704 available bytes; 95.95% used; 225420098 free inodes.

server4 `/tmp`: 106192060416 available bytes; 94.07% used; 114351894 free inodes.

server4 `/var/tmp`: 106192060416 available bytes; 94.07% used; 114351894 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
