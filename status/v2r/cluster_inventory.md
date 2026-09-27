# V2R cluster inventory

2026-09-27T03:17:33.177718+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | ['2', '3', '4', '5', '6', '7'] | ['/tmp', '/var/tmp'] |

server1 `/`: 315086569472 available bytes; 82.42% used; 112443053 free inodes.

server1 `/home`: 315086569472 available bytes; 82.42% used; 112443053 free inodes.

server1 `/tmp`: 315086569472 available bytes; 82.42% used; 112443053 free inodes.

server1 `/var/tmp`: 315086569472 available bytes; 82.42% used; 112443053 free inodes.

server1 `/mnt/raid5`: 636794654720 available bytes; 97.08% used; 337401379 free inodes.
| server2 | True | [] | [] |

server2 `/`: 17624518656 available bytes; 99.02% used; 110365007 free inodes.

server2 `/home`: 17624518656 available bytes; 99.02% used; 110365007 free inodes.

server2 `/tmp`: 17624518656 available bytes; 99.02% used; 110365007 free inodes.

server2 `/var/tmp`: 17624518656 available bytes; 99.02% used; 110365007 free inodes.

server2 `/mnt/raid5`: 579599585280 available bytes; 96.00% used; 444883269 free inodes.
| server3 | True | [] | [] |

server3 `/`: 78711054336 available bytes; 95.61% used; 114062956 free inodes.

server3 `/home`: 78711054336 available bytes; 95.61% used; 114062956 free inodes.

server3 `/data`: 1336532996096 available bytes; 81.53% used; 225761629 free inodes.

server3 `/tmp`: 78711054336 available bytes; 95.61% used; 114062956 free inodes.

server3 `/var/tmp`: 78711054336 available bytes; 95.61% used; 114062956 free inodes.
| server4 | True | ['3', '7'] | ['/tmp', '/var/tmp'] |

server4 `/`: 111028547584 available bytes; 93.80% used; 114372980 free inodes.

server4 `/home`: 111028547584 available bytes; 93.80% used; 114372980 free inodes.

server4 `/data`: 393625378816 available bytes; 94.56% used; 224780984 free inodes.

server4 `/tmp`: 111028547584 available bytes; 93.80% used; 114372980 free inodes.

server4 `/var/tmp`: 111028547584 available bytes; 93.80% used; 114372980 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
