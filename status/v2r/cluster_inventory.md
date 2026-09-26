# V2R cluster inventory

2026-09-26T10:29:23.429799+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | ['1', '4', '5', '6', '7'] | ['/tmp', '/var/tmp'] |

server1 `/`: 318227726336 available bytes; 82.25% used; 112474858 free inodes.

server1 `/home`: 318227726336 available bytes; 82.25% used; 112474858 free inodes.

server1 `/tmp`: 318227726336 available bytes; 82.25% used; 112474858 free inodes.

server1 `/var/tmp`: 318227726336 available bytes; 82.25% used; 112474858 free inodes.

server1 `/mnt/raid5`: 198188773376 available bytes; 99.09% used; 337538363 free inodes.
| server2 | True | [] | [] |

server2 `/`: 19851816960 available bytes; 98.89% used; 110384909 free inodes.

server2 `/home`: 19851816960 available bytes; 98.89% used; 110384909 free inodes.

server2 `/tmp`: 19851816960 available bytes; 98.89% used; 110384909 free inodes.

server2 `/var/tmp`: 19851816960 available bytes; 98.89% used; 110384909 free inodes.

server2 `/mnt/raid5`: 222943207424 available bytes; 98.46% used; 444979864 free inodes.
| server3 | True | [] | [] |

server3 `/`: 82662240256 available bytes; 95.39% used; 114110825 free inodes.

server3 `/home`: 82662240256 available bytes; 95.39% used; 114110825 free inodes.

server3 `/data`: 123585650688 available bytes; 98.29% used; 225826823 free inodes.

server3 `/tmp`: 82662240256 available bytes; 95.39% used; 114110825 free inodes.

server3 `/var/tmp`: 82662240256 available bytes; 95.39% used; 114110825 free inodes.
| server4 | True | ['3', '5', '7'] | ['/tmp', '/var/tmp'] |

server4 `/`: 105927593984 available bytes; 94.09% used; 114347976 free inodes.

server4 `/home`: 105927593984 available bytes; 94.09% used; 114347976 free inodes.

server4 `/data`: 89091604480 available bytes; 98.77% used; 224881456 free inodes.

server4 `/tmp`: 105927593984 available bytes; 94.09% used; 114347976 free inodes.

server4 `/var/tmp`: 105927593984 available bytes; 94.09% used; 114347976 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
