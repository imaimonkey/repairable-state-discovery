# V2R cluster inventory

2026-09-23T23:46:03.910791+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | [] | ['/tmp', '/var/tmp', '/mnt/raid5'] |

server1 `/`: 325600993280 available bytes; 81.84% used; 112501091 free inodes.

server1 `/home`: 325600993280 available bytes; 81.84% used; 112501091 free inodes.

server1 `/tmp`: 325600993280 available bytes; 81.84% used; 112501091 free inodes.

server1 `/var/tmp`: 325600993280 available bytes; 81.84% used; 112501091 free inodes.

server1 `/mnt/raid5`: 1326137487360 available bytes; 93.92% used; 337735814 free inodes.
| server2 | True | [] | [] |

server2 `/`: 41033076736 available bytes; 97.71% used; 110432500 free inodes.

server2 `/home`: 41033076736 available bytes; 97.71% used; 110432500 free inodes.

server2 `/tmp`: 41033076736 available bytes; 97.71% used; 110432500 free inodes.

server2 `/var/tmp`: 41033076736 available bytes; 97.71% used; 110432500 free inodes.

server2 `/mnt/raid5`: 533954641920 available bytes; 96.31% used; 445204819 free inodes.
| server3 | True | [] | ['/tmp', '/var/tmp'] |

server3 `/`: 292668854272 available bytes; 83.67% used; 114210312 free inodes.

server3 `/home`: 292668854272 available bytes; 83.67% used; 114210312 free inodes.

server3 `/data`: 82295414784 available bytes; 98.86% used; 225845099 free inodes.

server3 `/tmp`: 292668854272 available bytes; 83.67% used; 114210312 free inodes.

server3 `/var/tmp`: 292668854272 available bytes; 83.67% used; 114210312 free inodes.
| server4 | True | ['3', '6', '7'] | ['/tmp', '/var/tmp'] |

server4 `/`: 106178359296 available bytes; 94.07% used; 114351763 free inodes.

server4 `/home`: 106178359296 available bytes; 94.07% used; 114351763 free inodes.

server4 `/data`: 292979752960 available bytes; 95.95% used; 225419191 free inodes.

server4 `/tmp`: 106178359296 available bytes; 94.07% used; 114351763 free inodes.

server4 `/var/tmp`: 106178359296 available bytes; 94.07% used; 114351763 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
