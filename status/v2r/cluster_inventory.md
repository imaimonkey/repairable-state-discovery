# V2R cluster inventory

2026-09-26T23:09:02.882147+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | ['0', '1', '2', '3', '4', '5', '6', '7'] | ['/tmp', '/var/tmp'] |

server1 `/`: 315468013568 available bytes; 82.40% used; 112445703 free inodes.

server1 `/home`: 315468013568 available bytes; 82.40% used; 112445703 free inodes.

server1 `/tmp`: 315468013568 available bytes; 82.40% used; 112445703 free inodes.

server1 `/var/tmp`: 315468013568 available bytes; 82.40% used; 112445703 free inodes.

server1 `/mnt/raid5`: 645834592256 available bytes; 97.04% used; 337467222 free inodes.
| server2 | True | ['2', '7'] | [] |

server2 `/`: 17940066304 available bytes; 99.00% used; 110367500 free inodes.

server2 `/home`: 17940066304 available bytes; 99.00% used; 110367500 free inodes.

server2 `/tmp`: 17940066304 available bytes; 99.00% used; 110367500 free inodes.

server2 `/var/tmp`: 17940066304 available bytes; 99.00% used; 110367500 free inodes.

server2 `/mnt/raid5`: 595148275712 available bytes; 95.89% used; 444960293 free inodes.
| server3 | True | ['2'] | [] |

server3 `/`: 81084588032 available bytes; 95.48% used; 114069881 free inodes.

server3 `/home`: 81084588032 available bytes; 95.48% used; 114069881 free inodes.

server3 `/data`: 1349236174848 available bytes; 81.35% used; 225826628 free inodes.

server3 `/tmp`: 81084588032 available bytes; 95.48% used; 114069881 free inodes.

server3 `/var/tmp`: 81084588032 available bytes; 95.48% used; 114069881 free inodes.
| server4 | True | ['2', '3', '6', '7'] | ['/tmp', '/var/tmp'] |

server4 `/`: 105898221568 available bytes; 94.09% used; 114347853 free inodes.

server4 `/home`: 105898221568 available bytes; 94.09% used; 114347853 free inodes.

server4 `/data`: 409610424320 available bytes; 94.34% used; 224823808 free inodes.

server4 `/tmp`: 105898221568 available bytes; 94.09% used; 114347853 free inodes.

server4 `/var/tmp`: 105898221568 available bytes; 94.09% used; 114347853 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
