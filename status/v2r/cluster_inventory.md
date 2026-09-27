# V2R cluster inventory

2026-09-27T00:31:21.950076+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | ['1', '2', '3', '4', '5', '6', '7'] | ['/tmp', '/var/tmp'] |

server1 `/`: 315154898944 available bytes; 82.42% used; 112443463 free inodes.

server1 `/home`: 315154898944 available bytes; 82.42% used; 112443463 free inodes.

server1 `/tmp`: 315154898944 available bytes; 82.42% used; 112443463 free inodes.

server1 `/var/tmp`: 315154898944 available bytes; 82.42% used; 112443463 free inodes.

server1 `/mnt/raid5`: 637682860032 available bytes; 97.07% used; 337407692 free inodes.
| server2 | True | [] | [] |

server2 `/`: 17631760384 available bytes; 99.02% used; 110365010 free inodes.

server2 `/home`: 17631760384 available bytes; 99.02% used; 110365010 free inodes.

server2 `/tmp`: 17631760384 available bytes; 99.02% used; 110365010 free inodes.

server2 `/var/tmp`: 17631760384 available bytes; 99.02% used; 110365010 free inodes.

server2 `/mnt/raid5`: 593164656640 available bytes; 95.90% used; 444957105 free inodes.
| server3 | True | ['3'] | [] |

server3 `/`: 77987545088 available bytes; 95.65% used; 114068605 free inodes.

server3 `/home`: 77987545088 available bytes; 95.65% used; 114068605 free inodes.

server3 `/data`: 1349107609600 available bytes; 81.35% used; 225825547 free inodes.

server3 `/tmp`: 77987545088 available bytes; 95.65% used; 114068605 free inodes.

server3 `/var/tmp`: 77987545088 available bytes; 95.65% used; 114068605 free inodes.
| server4 | True | ['3', '6', '7'] | ['/tmp', '/var/tmp'] |

server4 `/`: 105877946368 available bytes; 94.09% used; 114347834 free inodes.

server4 `/home`: 105877946368 available bytes; 94.09% used; 114347834 free inodes.

server4 `/data`: 409227464704 available bytes; 94.34% used; 224820637 free inodes.

server4 `/tmp`: 105877946368 available bytes; 94.09% used; 114347834 free inodes.

server4 `/var/tmp`: 105877946368 available bytes; 94.09% used; 114347834 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
