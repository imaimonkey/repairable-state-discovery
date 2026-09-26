# V2R cluster inventory

2026-09-26T09:49:57.491061+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | ['1', '4', '5', '6', '7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 318616666112 available bytes; 82.23% used; 112475080 free inodes.

server1 `/home`: 318616666112 available bytes; 82.23% used; 112475080 free inodes.

server1 `/tmp`: 318616666112 available bytes; 82.23% used; 112475080 free inodes.

server1 `/var/tmp`: 318616666112 available bytes; 82.23% used; 112475080 free inodes.

server1 `/mnt/raid5`: 218925293568 available bytes; 99.00% used; 337538559 free inodes.
| server2 | True | [] | [] | reference_compatible=False |

server2 `/`: 22306578432 available bytes; 98.76% used; 110402882 free inodes.

server2 `/home`: 22306578432 available bytes; 98.76% used; 110402882 free inodes.

server2 `/tmp`: 22306578432 available bytes; 98.76% used; 110402882 free inodes.

server2 `/var/tmp`: 22306578432 available bytes; 98.76% used; 110402882 free inodes.

server2 `/mnt/raid5`: 252849684480 available bytes; 98.25% used; 445022416 free inodes.
| server3 | True | [] | [] | reference_compatible=True |

server3 `/`: 82659180544 available bytes; 95.39% used; 114110803 free inodes.

server3 `/home`: 82659180544 available bytes; 95.39% used; 114110803 free inodes.

server3 `/data`: 123594473472 available bytes; 98.29% used; 225827477 free inodes.

server3 `/tmp`: 82659180544 available bytes; 95.39% used; 114110803 free inodes.

server3 `/var/tmp`: 82659180544 available bytes; 95.39% used; 114110803 free inodes.
| server4 | True | ['3', '7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 105931542528 available bytes; 94.09% used; 114348027 free inodes.

server4 `/home`: 105931542528 available bytes; 94.09% used; 114348027 free inodes.

server4 `/data`: 89249746944 available bytes; 98.77% used; 224882309 free inodes.

server4 `/tmp`: 105931542528 available bytes; 94.09% used; 114348027 free inodes.

server4 `/var/tmp`: 105931542528 available bytes; 94.09% used; 114348027 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
