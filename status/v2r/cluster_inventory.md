# V2R cluster inventory

2026-09-23T23:13:42.705449+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | ['6', '7'] | ['/tmp', '/var/tmp', '/mnt/raid5'] |

server1 `/`: 325669576704 available bytes; 81.83% used; 112501621 free inodes.

server1 `/home`: 325669576704 available bytes; 81.83% used; 112501621 free inodes.

server1 `/tmp`: 325669576704 available bytes; 81.83% used; 112501621 free inodes.

server1 `/var/tmp`: 325669576704 available bytes; 81.83% used; 112501621 free inodes.

server1 `/mnt/raid5`: 1387934306304 available bytes; 93.63% used; 337739891 free inodes.
| server2 | True | [] | [] |

server2 `/`: 41053339648 available bytes; 97.71% used; 110432611 free inodes.

server2 `/home`: 41053339648 available bytes; 97.71% used; 110432611 free inodes.

server2 `/tmp`: 41053339648 available bytes; 97.71% used; 110432611 free inodes.

server2 `/var/tmp`: 41053339648 available bytes; 97.71% used; 110432611 free inodes.

server2 `/mnt/raid5`: 534998818816 available bytes; 96.30% used; 445206221 free inodes.
| server3 | True | ['3'] | ['/tmp', '/var/tmp'] |

server3 `/`: 292071501824 available bytes; 83.70% used; 114165930 free inodes.

server3 `/home`: 292071501824 available bytes; 83.70% used; 114165930 free inodes.

server3 `/data`: 82329563136 available bytes; 98.86% used; 225846064 free inodes.

server3 `/tmp`: 292071501824 available bytes; 83.70% used; 114165930 free inodes.

server3 `/var/tmp`: 292071501824 available bytes; 83.70% used; 114165930 free inodes.
| server4 | True | ['3', '6', '7'] | ['/tmp', '/var/tmp'] |

server4 `/`: 106266128384 available bytes; 94.07% used; 114352955 free inodes.

server4 `/home`: 106266128384 available bytes; 94.07% used; 114352955 free inodes.

server4 `/data`: 299100004352 available bytes; 95.87% used; 225429146 free inodes.

server4 `/tmp`: 106266128384 available bytes; 94.07% used; 114352955 free inodes.

server4 `/var/tmp`: 106266128384 available bytes; 94.07% used; 114352955 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
