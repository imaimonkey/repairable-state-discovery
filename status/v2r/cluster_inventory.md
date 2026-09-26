# V2R cluster inventory

2026-09-26T14:21:29.126196+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | ['3', '4', '5', '6', '7'] | ['/tmp', '/var/tmp'] |

server1 `/`: 318128685056 available bytes; 82.25% used; 112474367 free inodes.

server1 `/home`: 318128685056 available bytes; 82.25% used; 112474367 free inodes.

server1 `/tmp`: 318128685056 available bytes; 82.25% used; 112474367 free inodes.

server1 `/var/tmp`: 318128685056 available bytes; 82.25% used; 112474367 free inodes.

server1 `/mnt/raid5`: 674014552064 available bytes; 96.91% used; 337531924 free inodes.
| server2 | True | [] | [] |

server2 `/`: 4279099392 available bytes; 99.76% used; 110378513 free inodes.

server2 `/home`: 4279099392 available bytes; 99.76% used; 110378513 free inodes.

server2 `/tmp`: 4279099392 available bytes; 99.76% used; 110378513 free inodes.

server2 `/var/tmp`: 4279099392 available bytes; 99.76% used; 110378513 free inodes.

server2 `/mnt/raid5`: 635189927936 available bytes; 95.61% used; 444975095 free inodes.
| server3 | True | [] | [] |

server3 `/`: 82639335424 available bytes; 95.39% used; 114110784 free inodes.

server3 `/home`: 82639335424 available bytes; 95.39% used; 114110784 free inodes.

server3 `/data`: 1346886586368 available bytes; 81.39% used; 225805316 free inodes.

server3 `/tmp`: 82639335424 available bytes; 95.39% used; 114110784 free inodes.

server3 `/var/tmp`: 82639335424 available bytes; 95.39% used; 114110784 free inodes.
| server4 | True | ['3', '5', '7'] | ['/tmp', '/var/tmp'] |

server4 `/`: 105887084544 available bytes; 94.09% used; 114347843 free inodes.

server4 `/home`: 105887084544 available bytes; 94.09% used; 114347843 free inodes.

server4 `/data`: 411021225984 available bytes; 94.32% used; 224826789 free inodes.

server4 `/tmp`: 105887084544 available bytes; 94.09% used; 114347843 free inodes.

server4 `/var/tmp`: 105887084544 available bytes; 94.09% used; 114347843 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
