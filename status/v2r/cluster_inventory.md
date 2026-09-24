# V2R cluster inventory

2026-09-24T22:59:19.458266+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | [] | ['/tmp', '/var/tmp'] |

server1 `/`: 321865003008 available bytes; 82.04% used; 112480936 free inodes.

server1 `/home`: 321865003008 available bytes; 82.04% used; 112480936 free inodes.

server1 `/tmp`: 321865003008 available bytes; 82.04% used; 112480936 free inodes.

server1 `/var/tmp`: 321865003008 available bytes; 82.04% used; 112480936 free inodes.

server1 `/mnt/raid5`: 415297921024 available bytes; 98.09% used; 337616861 free inodes.
| server2 | True | [] | [] |

server2 `/`: 23133409280 available bytes; 98.71% used; 110410859 free inodes.

server2 `/home`: 23133409280 available bytes; 98.71% used; 110410859 free inodes.

server2 `/tmp`: 23133409280 available bytes; 98.71% used; 110410859 free inodes.

server2 `/var/tmp`: 23133409280 available bytes; 98.71% used; 110410859 free inodes.

server2 `/mnt/raid5`: 487645970432 available bytes; 96.63% used; 445152260 free inodes.
| server3 | True | [] | [] |

server3 `/`: 84370554880 available bytes; 95.29% used; 114156077 free inodes.

server3 `/home`: 84370554880 available bytes; 95.29% used; 114156077 free inodes.

server3 `/data`: 148799479808 available bytes; 97.94% used; 225801527 free inodes.

server3 `/tmp`: 84370554880 available bytes; 95.29% used; 114156077 free inodes.

server3 `/var/tmp`: 84370554880 available bytes; 95.29% used; 114156077 free inodes.
| server4 | True | ['0', '7'] | ['/tmp', '/var/tmp'] |

server4 `/`: 105800880128 available bytes; 94.10% used; 114348316 free inodes.

server4 `/home`: 105800880128 available bytes; 94.10% used; 114348316 free inodes.

server4 `/data`: 62037557248 available bytes; 99.14% used; 225193063 free inodes.

server4 `/tmp`: 105800880128 available bytes; 94.10% used; 114348316 free inodes.

server4 `/var/tmp`: 105800880128 available bytes; 94.10% used; 114348316 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
