# V2R cluster inventory

2026-09-23T23:06:00.883068+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | ['6', '7'] | ['/tmp', '/var/tmp', '/mnt/raid5'] |

server1 `/`: 325739888640 available bytes; 81.83% used; 112501691 free inodes.

server1 `/home`: 325739888640 available bytes; 81.83% used; 112501691 free inodes.

server1 `/tmp`: 325739888640 available bytes; 81.83% used; 112501691 free inodes.

server1 `/var/tmp`: 325739888640 available bytes; 81.83% used; 112501691 free inodes.

server1 `/mnt/raid5`: 1387998609408 available bytes; 93.63% used; 337739788 free inodes.
| server2 | True | [] | [] |

server2 `/`: 41059303424 available bytes; 97.71% used; 110432612 free inodes.

server2 `/home`: 41059303424 available bytes; 97.71% used; 110432612 free inodes.

server2 `/tmp`: 41059303424 available bytes; 97.71% used; 110432612 free inodes.

server2 `/var/tmp`: 41059303424 available bytes; 97.71% used; 110432612 free inodes.

server2 `/mnt/raid5`: 535213477888 available bytes; 96.30% used; 445205801 free inodes.
| server3 | True | ['3'] | ['/tmp', '/var/tmp'] |

server3 `/`: 292863864832 available bytes; 83.66% used; 114210987 free inodes.

server3 `/home`: 292863864832 available bytes; 83.66% used; 114210987 free inodes.

server3 `/data`: 82347294720 available bytes; 98.86% used; 225846543 free inodes.

server3 `/tmp`: 292863864832 available bytes; 83.66% used; 114210987 free inodes.

server3 `/var/tmp`: 292863864832 available bytes; 83.66% used; 114210987 free inodes.
| server4 | True | ['3', '6', '7'] | ['/tmp', '/var/tmp'] |

server4 `/`: 106283597824 available bytes; 94.07% used; 114353235 free inodes.

server4 `/home`: 106283597824 available bytes; 94.07% used; 114353235 free inodes.

server4 `/data`: 300060237824 available bytes; 95.85% used; 225430986 free inodes.

server4 `/tmp`: 106283597824 available bytes; 94.07% used; 114353235 free inodes.

server4 `/var/tmp`: 106283597824 available bytes; 94.07% used; 114353235 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
