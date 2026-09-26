# V2R cluster inventory

2026-09-26T13:52:30.102223+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | ['1', '2', '3', '4', '5', '6', '7'] | ['/tmp', '/var/tmp'] |

server1 `/`: 318152720384 available bytes; 82.25% used; 112474422 free inodes.

server1 `/home`: 318152720384 available bytes; 82.25% used; 112474422 free inodes.

server1 `/tmp`: 318152720384 available bytes; 82.25% used; 112474422 free inodes.

server1 `/var/tmp`: 318152720384 available bytes; 82.25% used; 112474422 free inodes.

server1 `/mnt/raid5`: 674753531904 available bytes; 96.90% used; 337535768 free inodes.
| server2 | True | ['2', '7'] | [] |

server2 `/`: 19076636672 available bytes; 98.94% used; 110378924 free inodes.

server2 `/home`: 19076636672 available bytes; 98.94% used; 110378924 free inodes.

server2 `/tmp`: 19076636672 available bytes; 98.94% used; 110378924 free inodes.

server2 `/var/tmp`: 19076636672 available bytes; 98.94% used; 110378924 free inodes.

server2 `/mnt/raid5`: 635399991296 available bytes; 95.61% used; 444975668 free inodes.
| server3 | True | [] | [] |

server3 `/`: 82640232448 available bytes; 95.39% used; 114110809 free inodes.

server3 `/home`: 82640232448 available bytes; 95.39% used; 114110809 free inodes.

server3 `/data`: 1347434897408 available bytes; 81.38% used; 225822742 free inodes.

server3 `/tmp`: 82640232448 available bytes; 95.39% used; 114110809 free inodes.

server3 `/var/tmp`: 82640232448 available bytes; 95.39% used; 114110809 free inodes.
| server4 | True | ['0', '3', '5', '7'] | ['/tmp', '/var/tmp'] |

server4 `/`: 105898102784 available bytes; 94.09% used; 114347938 free inodes.

server4 `/home`: 105898102784 available bytes; 94.09% used; 114347938 free inodes.

server4 `/data`: 411441041408 available bytes; 94.31% used; 224827551 free inodes.

server4 `/tmp`: 105898102784 available bytes; 94.09% used; 114347938 free inodes.

server4 `/var/tmp`: 105898102784 available bytes; 94.09% used; 114347938 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
