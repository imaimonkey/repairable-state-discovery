# V2R cluster inventory

2026-09-26T06:11:09.590582+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | ['1', '4', '5', '6', '7'] | ['/tmp', '/var/tmp'] |

server1 `/`: 318779453440 available bytes; 82.22% used; 112476279 free inodes.

server1 `/home`: 318779453440 available bytes; 82.22% used; 112476279 free inodes.

server1 `/tmp`: 318779453440 available bytes; 82.22% used; 112476279 free inodes.

server1 `/var/tmp`: 318779453440 available bytes; 82.22% used; 112476279 free inodes.

server1 `/mnt/raid5`: 222282481664 available bytes; 98.98% used; 337539905 free inodes.
| server2 | True | [] | [] |

server2 `/`: 20781838336 available bytes; 98.84% used; 110404637 free inodes.

server2 `/home`: 20781838336 available bytes; 98.84% used; 110404637 free inodes.

server2 `/tmp`: 20781838336 available bytes; 98.84% used; 110404637 free inodes.

server2 `/var/tmp`: 20781838336 available bytes; 98.84% used; 110404637 free inodes.

server2 `/mnt/raid5`: 274250969088 available bytes; 98.10% used; 445033238 free inodes.
| server3 | True | [] | [] |

server3 `/`: 82430357504 available bytes; 95.40% used; 114110905 free inodes.

server3 `/home`: 82430357504 available bytes; 95.40% used; 114110905 free inodes.

server3 `/data`: 123993276416 available bytes; 98.29% used; 225822599 free inodes.

server3 `/tmp`: 82430357504 available bytes; 95.40% used; 114110905 free inodes.

server3 `/var/tmp`: 82430357504 available bytes; 95.40% used; 114110905 free inodes.
| server4 | True | ['3', '7'] | ['/tmp', '/var/tmp'] |

server4 `/`: 105990262784 available bytes; 94.09% used; 114347063 free inodes.

server4 `/home`: 105990262784 available bytes; 94.09% used; 114347063 free inodes.

server4 `/data`: 106912632832 available bytes; 98.52% used; 224929091 free inodes.

server4 `/tmp`: 105990262784 available bytes; 94.09% used; 114347063 free inodes.

server4 `/var/tmp`: 105990262784 available bytes; 94.09% used; 114347063 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
