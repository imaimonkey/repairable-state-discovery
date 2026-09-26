# V2R cluster inventory

2026-09-26T13:14:21.734962+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | ['1', '2', '3', '4', '5', '6', '7'] | ['/tmp', '/var/tmp'] |

server1 `/`: 318153351168 available bytes; 82.25% used; 112474441 free inodes.

server1 `/home`: 318153351168 available bytes; 82.25% used; 112474441 free inodes.

server1 `/tmp`: 318153351168 available bytes; 82.25% used; 112474441 free inodes.

server1 `/var/tmp`: 318153351168 available bytes; 82.25% used; 112474441 free inodes.

server1 `/mnt/raid5`: 674746744832 available bytes; 96.90% used; 337535819 free inodes.
| server2 | True | ['2', '7'] | [] |

server2 `/`: 19077959680 available bytes; 98.94% used; 110378934 free inodes.

server2 `/home`: 19077959680 available bytes; 98.94% used; 110378934 free inodes.

server2 `/tmp`: 19077959680 available bytes; 98.94% used; 110378934 free inodes.

server2 `/var/tmp`: 19077959680 available bytes; 98.94% used; 110378934 free inodes.

server2 `/mnt/raid5`: 637020889088 available bytes; 95.60% used; 444976862 free inodes.
| server3 | True | [] | [] |

server3 `/`: 82639056896 available bytes; 95.39% used; 114110813 free inodes.

server3 `/home`: 82639056896 available bytes; 95.39% used; 114110813 free inodes.

server3 `/data`: 1347561230336 available bytes; 81.38% used; 225823152 free inodes.

server3 `/tmp`: 82639056896 available bytes; 95.39% used; 114110813 free inodes.

server3 `/var/tmp`: 82639056896 available bytes; 95.39% used; 114110813 free inodes.
| server4 | True | ['0', '3', '5', '7'] | ['/tmp', '/var/tmp'] |

server4 `/`: 105898811392 available bytes; 94.09% used; 114347938 free inodes.

server4 `/home`: 105898811392 available bytes; 94.09% used; 114347938 free inodes.

server4 `/data`: 413220139008 available bytes; 94.29% used; 224833810 free inodes.

server4 `/tmp`: 105898811392 available bytes; 94.09% used; 114347938 free inodes.

server4 `/var/tmp`: 105898811392 available bytes; 94.09% used; 114347938 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
