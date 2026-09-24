# V2R cluster inventory

2026-09-24T01:37:30.346689+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | ['4', '6', '7'] | ['/tmp', '/var/tmp'] |

server1 `/`: 325460733952 available bytes; 81.84% used; 112499473 free inodes.

server1 `/home`: 325460733952 available bytes; 81.84% used; 112499473 free inodes.

server1 `/tmp`: 325460733952 available bytes; 81.84% used; 112499473 free inodes.

server1 `/var/tmp`: 325460733952 available bytes; 81.84% used; 112499473 free inodes.

server1 `/mnt/raid5`: 866942603264 available bytes; 96.02% used; 337733909 free inodes.
| server2 | True | [] | [] |

server2 `/`: 40937947136 available bytes; 97.72% used; 110431935 free inodes.

server2 `/home`: 40937947136 available bytes; 97.72% used; 110431935 free inodes.

server2 `/tmp`: 40937947136 available bytes; 97.72% used; 110431935 free inodes.

server2 `/var/tmp`: 40937947136 available bytes; 97.72% used; 110431935 free inodes.

server2 `/mnt/raid5`: 530571481088 available bytes; 96.33% used; 445201366 free inodes.
| server3 | True | [] | ['/tmp', '/var/tmp'] |

server3 `/`: 292723642368 available bytes; 83.66% used; 114211255 free inodes.

server3 `/home`: 292723642368 available bytes; 83.66% used; 114211255 free inodes.

server3 `/data`: 71598563328 available bytes; 99.01% used; 225842119 free inodes.

server3 `/tmp`: 292723642368 available bytes; 83.66% used; 114211255 free inodes.

server3 `/var/tmp`: 292723642368 available bytes; 83.66% used; 114211255 free inodes.
| server4 | True | ['2', '3', '6', '7'] | ['/tmp', '/var/tmp'] |

server4 `/`: 105958420480 available bytes; 94.09% used; 114348692 free inodes.

server4 `/home`: 105958420480 available bytes; 94.09% used; 114348692 free inodes.

server4 `/data`: 290804645888 available bytes; 95.98% used; 225396932 free inodes.

server4 `/tmp`: 105958420480 available bytes; 94.09% used; 114348692 free inodes.

server4 `/var/tmp`: 105958420480 available bytes; 94.09% used; 114348692 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
