# V2R cluster inventory

2026-09-27T07:07:47.433783+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | ['2', '3', '4', '5', '6', '7'] | ['/tmp', '/var/tmp'] |

server1 `/`: 314481672192 available bytes; 82.46% used; 112440814 free inodes.

server1 `/home`: 314481672192 available bytes; 82.46% used; 112440814 free inodes.

server1 `/tmp`: 314481672192 available bytes; 82.46% used; 112440814 free inodes.

server1 `/var/tmp`: 314481672192 available bytes; 82.46% used; 112440814 free inodes.

server1 `/mnt/raid5`: 634669359104 available bytes; 97.09% used; 337400006 free inodes.
| server2 | True | [] | [] |

server2 `/`: 17615720448 available bytes; 99.02% used; 110365005 free inodes.

server2 `/home`: 17615720448 available bytes; 99.02% used; 110365005 free inodes.

server2 `/tmp`: 17615720448 available bytes; 99.02% used; 110365005 free inodes.

server2 `/var/tmp`: 17615720448 available bytes; 99.02% used; 110365005 free inodes.

server2 `/mnt/raid5`: 572027801600 available bytes; 96.05% used; 444874579 free inodes.
| server3 | True | [] | [] |

server3 `/`: 78573809664 available bytes; 95.62% used; 114062886 free inodes.

server3 `/home`: 78573809664 available bytes; 95.62% used; 114062886 free inodes.

server3 `/data`: 1333230063616 available bytes; 81.57% used; 225764510 free inodes.

server3 `/tmp`: 78573809664 available bytes; 95.62% used; 114062886 free inodes.

server3 `/var/tmp`: 78573809664 available bytes; 95.62% used; 114062886 free inodes.
| server4 | True | ['5'] | ['/tmp', '/var/tmp'] |

server4 `/`: 111071088640 available bytes; 93.80% used; 114372892 free inodes.

server4 `/home`: 111071088640 available bytes; 93.80% used; 114372892 free inodes.

server4 `/data`: 374397153280 available bytes; 94.83% used; 224771412 free inodes.

server4 `/tmp`: 111071088640 available bytes; 93.80% used; 114372892 free inodes.

server4 `/var/tmp`: 111071088640 available bytes; 93.80% used; 114372892 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
