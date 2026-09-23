# V2R cluster inventory

2026-09-23T22:56:45.582961+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | ['6', '7'] | ['/tmp', '/var/tmp', '/mnt/raid5'] |

server1 `/`: 325747490816 available bytes; 81.83% used; 112501733 free inodes.

server1 `/home`: 325747490816 available bytes; 81.83% used; 112501733 free inodes.

server1 `/tmp`: 325747490816 available bytes; 81.83% used; 112501733 free inodes.

server1 `/var/tmp`: 325747490816 available bytes; 81.83% used; 112501733 free inodes.

server1 `/mnt/raid5`: 1388005851136 available bytes; 93.63% used; 337739805 free inodes.
| server2 | True | [] | [] |

server2 `/`: 41062604800 available bytes; 97.71% used; 110432613 free inodes.

server2 `/home`: 41062604800 available bytes; 97.71% used; 110432613 free inodes.

server2 `/tmp`: 41062604800 available bytes; 97.71% used; 110432613 free inodes.

server2 `/var/tmp`: 41062604800 available bytes; 97.71% used; 110432613 free inodes.

server2 `/mnt/raid5`: 535514988544 available bytes; 96.30% used; 445206123 free inodes.
| server3 | True | ['3'] | ['/tmp', '/var/tmp'] |

server3 `/`: 292537344000 available bytes; 83.68% used; 114192882 free inodes.

server3 `/home`: 292537344000 available bytes; 83.68% used; 114192882 free inodes.

server3 `/data`: 82352041984 available bytes; 98.86% used; 225846725 free inodes.

server3 `/tmp`: 292537344000 available bytes; 83.68% used; 114192882 free inodes.

server3 `/var/tmp`: 292537344000 available bytes; 83.68% used; 114192882 free inodes.
| server4 | True | ['3', '6', '7'] | ['/tmp', '/var/tmp'] |

server4 `/`: 106304348160 available bytes; 94.07% used; 114353567 free inodes.

server4 `/home`: 106304348160 available bytes; 94.07% used; 114353567 free inodes.

server4 `/data`: 300084977664 available bytes; 95.85% used; 225432676 free inodes.

server4 `/tmp`: 106304348160 available bytes; 94.07% used; 114353567 free inodes.

server4 `/var/tmp`: 106304348160 available bytes; 94.07% used; 114353567 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
