# V2R cluster inventory

2026-09-26T15:28:36.433709+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | ['3', '4', '5', '6', '7'] | ['/tmp', '/var/tmp'] |

server1 `/`: 318160457728 available bytes; 82.25% used; 112473939 free inodes.

server1 `/home`: 318160457728 available bytes; 82.25% used; 112473939 free inodes.

server1 `/tmp`: 318160457728 available bytes; 82.25% used; 112473939 free inodes.

server1 `/var/tmp`: 318160457728 available bytes; 82.25% used; 112473939 free inodes.

server1 `/mnt/raid5`: 654122954752 available bytes; 97.00% used; 337531530 free inodes.
| server2 | True | ['2', '7'] | [] |

server2 `/`: 18030895104 available bytes; 98.99% used; 110367504 free inodes.

server2 `/home`: 18030895104 available bytes; 98.99% used; 110367504 free inodes.

server2 `/tmp`: 18030895104 available bytes; 98.99% used; 110367504 free inodes.

server2 `/var/tmp`: 18030895104 available bytes; 98.99% used; 110367504 free inodes.

server2 `/mnt/raid5`: 609465548800 available bytes; 95.79% used; 444972983 free inodes.
| server3 | True | [] | [] |

server3 `/`: 82446090240 available bytes; 95.40% used; 114101914 free inodes.

server3 `/home`: 82446090240 available bytes; 95.40% used; 114101914 free inodes.

server3 `/data`: 1347184394240 available bytes; 81.38% used; 225809791 free inodes.

server3 `/tmp`: 82446090240 available bytes; 95.40% used; 114101914 free inodes.

server3 `/var/tmp`: 82446090240 available bytes; 95.40% used; 114101914 free inodes.
| server4 | True | ['3', '5', '7'] | ['/tmp', '/var/tmp'] |

server4 `/`: 105954754560 available bytes; 94.09% used; 114347840 free inodes.

server4 `/home`: 105954754560 available bytes; 94.09% used; 114347840 free inodes.

server4 `/data`: 410802130944 available bytes; 94.32% used; 224825966 free inodes.

server4 `/tmp`: 105954754560 available bytes; 94.09% used; 114347840 free inodes.

server4 `/var/tmp`: 105954754560 available bytes; 94.09% used; 114347840 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
