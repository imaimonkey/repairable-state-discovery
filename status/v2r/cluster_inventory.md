# V2R cluster inventory

2026-09-26T15:13:21.221390+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | ['3', '4', '5', '6', '7'] | ['/tmp', '/var/tmp'] |

server1 `/`: 318164385792 available bytes; 82.25% used; 112473939 free inodes.

server1 `/home`: 318164385792 available bytes; 82.25% used; 112473939 free inodes.

server1 `/tmp`: 318164385792 available bytes; 82.25% used; 112473939 free inodes.

server1 `/var/tmp`: 318164385792 available bytes; 82.25% used; 112473939 free inodes.

server1 `/mnt/raid5`: 654226190336 available bytes; 97.00% used; 337531815 free inodes.
| server2 | True | ['7'] | [] |

server2 `/`: 7159709696 available bytes; 99.60% used; 110367255 free inodes.

server2 `/home`: 7159709696 available bytes; 99.60% used; 110367255 free inodes.

server2 `/tmp`: 7159709696 available bytes; 99.60% used; 110367255 free inodes.

server2 `/var/tmp`: 7159709696 available bytes; 99.60% used; 110367255 free inodes.

server2 `/mnt/raid5`: 609639739392 available bytes; 95.79% used; 444973622 free inodes.
| server3 | True | [] | [] |

server3 `/`: 82443165696 available bytes; 95.40% used; 114101910 free inodes.

server3 `/home`: 82443165696 available bytes; 95.40% used; 114101910 free inodes.

server3 `/data`: 1346908237824 available bytes; 81.39% used; 225810066 free inodes.

server3 `/tmp`: 82443165696 available bytes; 95.40% used; 114101910 free inodes.

server3 `/var/tmp`: 82443165696 available bytes; 95.40% used; 114101910 free inodes.
| server4 | True | ['3', '5', '7'] | ['/tmp', '/var/tmp'] |

server4 `/`: 105955053568 available bytes; 94.09% used; 114347840 free inodes.

server4 `/home`: 105955053568 available bytes; 94.09% used; 114347840 free inodes.

server4 `/data`: 410809118720 available bytes; 94.32% used; 224826085 free inodes.

server4 `/tmp`: 105955053568 available bytes; 94.09% used; 114347840 free inodes.

server4 `/var/tmp`: 105955053568 available bytes; 94.09% used; 114347840 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
