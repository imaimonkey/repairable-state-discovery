# V2R cluster inventory

2026-09-26T11:27:26.846538+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | ['1', '4', '5', '6', '7'] | ['/tmp', '/var/tmp'] |

server1 `/`: 318207684608 available bytes; 82.25% used; 112474813 free inodes.

server1 `/home`: 318207684608 available bytes; 82.25% used; 112474813 free inodes.

server1 `/tmp`: 318207684608 available bytes; 82.25% used; 112474813 free inodes.

server1 `/var/tmp`: 318207684608 available bytes; 82.25% used; 112474813 free inodes.

server1 `/mnt/raid5`: 218701479936 available bytes; 99.00% used; 337538080 free inodes.
| server2 | True | [] | [] |

server2 `/`: 19784384512 available bytes; 98.90% used; 110383617 free inodes.

server2 `/home`: 19784384512 available bytes; 98.90% used; 110383617 free inodes.

server2 `/tmp`: 19784384512 available bytes; 98.90% used; 110383617 free inodes.

server2 `/var/tmp`: 19784384512 available bytes; 98.90% used; 110383617 free inodes.

server2 `/mnt/raid5`: 241516879872 available bytes; 98.33% used; 444978328 free inodes.
| server3 | True | [] | [] |

server3 `/`: 82654052352 available bytes; 95.39% used; 114110825 free inodes.

server3 `/home`: 82654052352 available bytes; 95.39% used; 114110825 free inodes.

server3 `/data`: 123502493696 available bytes; 98.29% used; 225825569 free inodes.

server3 `/tmp`: 82654052352 available bytes; 95.39% used; 114110825 free inodes.

server3 `/var/tmp`: 82654052352 available bytes; 95.39% used; 114110825 free inodes.
| server4 | True | ['0', '3', '5', '7'] | ['/tmp', '/var/tmp'] |

server4 `/`: 105909669888 available bytes; 94.09% used; 114347938 free inodes.

server4 `/home`: 105909669888 available bytes; 94.09% used; 114347938 free inodes.

server4 `/data`: 88781660160 available bytes; 98.77% used; 224880319 free inodes.

server4 `/tmp`: 105909669888 available bytes; 94.09% used; 114347938 free inodes.

server4 `/var/tmp`: 105909669888 available bytes; 94.09% used; 114347938 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
