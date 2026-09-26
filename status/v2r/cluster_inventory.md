# V2R cluster inventory

2026-09-26T14:16:54.558496+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | ['3', '4', '5', '6', '7'] | ['/tmp', '/var/tmp'] |

server1 `/`: 318130249728 available bytes; 82.25% used; 112474376 free inodes.

server1 `/home`: 318130249728 available bytes; 82.25% used; 112474376 free inodes.

server1 `/tmp`: 318130249728 available bytes; 82.25% used; 112474376 free inodes.

server1 `/var/tmp`: 318130249728 available bytes; 82.25% used; 112474376 free inodes.

server1 `/mnt/raid5`: 674015571968 available bytes; 96.91% used; 337531972 free inodes.
| server2 | True | ['2', '7'] | [] |

server2 `/`: 19067559936 available bytes; 98.94% used; 110378893 free inodes.

server2 `/home`: 19067559936 available bytes; 98.94% used; 110378893 free inodes.

server2 `/tmp`: 19067559936 available bytes; 98.94% used; 110378893 free inodes.

server2 `/var/tmp`: 19067559936 available bytes; 98.94% used; 110378893 free inodes.

server2 `/mnt/raid5`: 635305967616 available bytes; 95.61% used; 444974995 free inodes.
| server3 | True | [] | [] |

server3 `/`: 82640355328 available bytes; 95.39% used; 114110784 free inodes.

server3 `/home`: 82640355328 available bytes; 95.39% used; 114110784 free inodes.

server3 `/data`: 1346895413248 available bytes; 81.39% used; 225805364 free inodes.

server3 `/tmp`: 82640355328 available bytes; 95.39% used; 114110784 free inodes.

server3 `/var/tmp`: 82640355328 available bytes; 95.39% used; 114110784 free inodes.
| server4 | True | ['3', '5', '7'] | ['/tmp', '/var/tmp'] |

server4 `/`: 105887195136 available bytes; 94.09% used; 114347843 free inodes.

server4 `/home`: 105887195136 available bytes; 94.09% used; 114347843 free inodes.

server4 `/data`: 411025276928 available bytes; 94.32% used; 224826837 free inodes.

server4 `/tmp`: 105887195136 available bytes; 94.09% used; 114347843 free inodes.

server4 `/var/tmp`: 105887195136 available bytes; 94.09% used; 114347843 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
