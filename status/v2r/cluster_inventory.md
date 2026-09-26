# V2R cluster inventory

2026-09-26T23:57:49.825958+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | ['0', '1', '2', '3', '4', '5', '6', '7'] | ['/tmp', '/var/tmp'] |

server1 `/`: 315444219904 available bytes; 82.40% used; 112445729 free inodes.

server1 `/home`: 315444219904 available bytes; 82.40% used; 112445729 free inodes.

server1 `/tmp`: 315444219904 available bytes; 82.40% used; 112445729 free inodes.

server1 `/var/tmp`: 315444219904 available bytes; 82.40% used; 112445729 free inodes.

server1 `/mnt/raid5`: 637714493440 available bytes; 97.07% used; 337408340 free inodes.
| server2 | True | ['7'] | [] |

server2 `/`: 17946247168 available bytes; 99.00% used; 110367450 free inodes.

server2 `/home`: 17946247168 available bytes; 99.00% used; 110367450 free inodes.

server2 `/tmp`: 17946247168 available bytes; 99.00% used; 110367450 free inodes.

server2 `/var/tmp`: 17946247168 available bytes; 99.00% used; 110367450 free inodes.

server2 `/mnt/raid5`: 594301677568 available bytes; 95.89% used; 444959016 free inodes.
| server3 | True | ['2', '3'] | [] |

server3 `/`: 81081176064 available bytes; 95.48% used; 114069884 free inodes.

server3 `/home`: 81081176064 available bytes; 95.48% used; 114069884 free inodes.

server3 `/data`: 1349116260352 available bytes; 81.35% used; 225826097 free inodes.

server3 `/tmp`: 81081176064 available bytes; 95.48% used; 114069884 free inodes.

server3 `/var/tmp`: 81081176064 available bytes; 95.48% used; 114069884 free inodes.
| server4 | True | ['2', '3', '6', '7'] | ['/tmp', '/var/tmp'] |

server4 `/`: 105880219648 available bytes; 94.09% used; 114347853 free inodes.

server4 `/home`: 105880219648 available bytes; 94.09% used; 114347853 free inodes.

server4 `/data`: 409580646400 available bytes; 94.34% used; 224823790 free inodes.

server4 `/tmp`: 105880219648 available bytes; 94.09% used; 114347853 free inodes.

server4 `/var/tmp`: 105880219648 available bytes; 94.09% used; 114347853 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
