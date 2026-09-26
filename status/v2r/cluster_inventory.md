# V2R cluster inventory

2026-09-26T06:42:15.474957+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | ['1', '4', '5', '6', '7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 318769500160 available bytes; 82.22% used; 112476293 free inodes.

server1 `/home`: 318769500160 available bytes; 82.22% used; 112476293 free inodes.

server1 `/tmp`: 318769500160 available bytes; 82.22% used; 112476293 free inodes.

server1 `/var/tmp`: 318769500160 available bytes; 82.22% used; 112476293 free inodes.

server1 `/mnt/raid5`: 219341381632 available bytes; 98.99% used; 337539663 free inodes.
| server2 | True | [] | [] | reference_compatible=False |

server2 `/`: 22321688576 available bytes; 98.75% used; 110403843 free inodes.

server2 `/home`: 22321688576 available bytes; 98.75% used; 110403843 free inodes.

server2 `/tmp`: 22321688576 available bytes; 98.75% used; 110403843 free inodes.

server2 `/var/tmp`: 22321688576 available bytes; 98.75% used; 110403843 free inodes.

server2 `/mnt/raid5`: 272669716480 available bytes; 98.12% used; 445028608 free inodes.
| server3 | True | [] | [] | reference_compatible=True |

server3 `/`: 82563309568 available bytes; 95.39% used; 114110888 free inodes.

server3 `/home`: 82563309568 available bytes; 95.39% used; 114110888 free inodes.

server3 `/data`: 123994812416 available bytes; 98.29% used; 225822079 free inodes.

server3 `/tmp`: 82563309568 available bytes; 95.39% used; 114110888 free inodes.

server3 `/var/tmp`: 82563309568 available bytes; 95.39% used; 114110888 free inodes.
| server4 | True | ['2', '3', '6', '7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 106075910144 available bytes; 94.08% used; 114348174 free inodes.

server4 `/home`: 106075910144 available bytes; 94.08% used; 114348174 free inodes.

server4 `/data`: 105908838400 available bytes; 98.54% used; 224923194 free inodes.

server4 `/tmp`: 106075910144 available bytes; 94.08% used; 114348174 free inodes.

server4 `/var/tmp`: 106075910144 available bytes; 94.08% used; 114348174 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
