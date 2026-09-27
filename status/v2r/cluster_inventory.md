# V2R cluster inventory

2026-09-27T00:19:10.398284+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | ['1', '2', '3', '4', '5', '6', '7'] | ['/tmp', '/var/tmp'] |

server1 `/`: 315166502912 available bytes; 82.42% used; 112443556 free inodes.

server1 `/home`: 315166502912 available bytes; 82.42% used; 112443556 free inodes.

server1 `/tmp`: 315166502912 available bytes; 82.42% used; 112443556 free inodes.

server1 `/var/tmp`: 315166502912 available bytes; 82.42% used; 112443556 free inodes.

server1 `/mnt/raid5`: 637714051072 available bytes; 97.07% used; 337408001 free inodes.
| server2 | True | [] | [] |

server2 `/`: 17726193664 available bytes; 99.01% used; 110365963 free inodes.

server2 `/home`: 17726193664 available bytes; 99.01% used; 110365963 free inodes.

server2 `/tmp`: 17726193664 available bytes; 99.01% used; 110365963 free inodes.

server2 `/var/tmp`: 17726193664 available bytes; 99.01% used; 110365963 free inodes.

server2 `/mnt/raid5`: 592988962816 available bytes; 95.90% used; 444957522 free inodes.
| server3 | True | ['3'] | [] |

server3 `/`: 77747757056 available bytes; 95.66% used; 114068740 free inodes.

server3 `/home`: 77747752960 available bytes; 95.66% used; 114068740 free inodes.

server3 `/data`: 1349111504896 available bytes; 81.35% used; 225825748 free inodes.

server3 `/tmp`: 77747748864 available bytes; 95.66% used; 114068740 free inodes.

server3 `/var/tmp`: 77747744768 available bytes; 95.66% used; 114068740 free inodes.
| server4 | True | ['3', '6', '7'] | ['/tmp', '/var/tmp'] |

server4 `/`: 105879629824 available bytes; 94.09% used; 114347843 free inodes.

server4 `/home`: 105879629824 available bytes; 94.09% used; 114347843 free inodes.

server4 `/data`: 409334771712 available bytes; 94.34% used; 224821783 free inodes.

server4 `/tmp`: 105879629824 available bytes; 94.09% used; 114347843 free inodes.

server4 `/var/tmp`: 105879629824 available bytes; 94.09% used; 114347843 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
