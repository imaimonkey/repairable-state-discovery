# V2R cluster inventory

2026-09-26T07:09:12.863472+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | ['1', '4', '5', '6', '7'] | ['/tmp', '/var/tmp'] |

server1 `/`: 318768848896 available bytes; 82.22% used; 112476289 free inodes.

server1 `/home`: 318768848896 available bytes; 82.22% used; 112476289 free inodes.

server1 `/tmp`: 318768848896 available bytes; 82.22% used; 112476289 free inodes.

server1 `/var/tmp`: 318768848896 available bytes; 82.22% used; 112476289 free inodes.

server1 `/mnt/raid5`: 211157053440 available bytes; 99.03% used; 337539345 free inodes.
| server2 | True | [] | [] |

server2 `/`: 22314434560 available bytes; 98.76% used; 110403878 free inodes.

server2 `/home`: 22314434560 available bytes; 98.76% used; 110403878 free inodes.

server2 `/tmp`: 22314434560 available bytes; 98.76% used; 110403878 free inodes.

server2 `/var/tmp`: 22314434560 available bytes; 98.76% used; 110403878 free inodes.

server2 `/mnt/raid5`: 271873810432 available bytes; 98.12% used; 445027919 free inodes.
| server3 | True | [] | [] |

server3 `/`: 82687889408 available bytes; 95.39% used; 114110895 free inodes.

server3 `/home`: 82687889408 available bytes; 95.39% used; 114110895 free inodes.

server3 `/data`: 123983319040 available bytes; 98.29% used; 225821432 free inodes.

server3 `/tmp`: 82687889408 available bytes; 95.39% used; 114110895 free inodes.

server3 `/var/tmp`: 82687889408 available bytes; 95.39% used; 114110895 free inodes.
| server4 | True | ['2', '3', '6', '7'] | ['/tmp', '/var/tmp'] |

server4 `/`: 106075086848 available bytes; 94.08% used; 114348174 free inodes.

server4 `/home`: 106075086848 available bytes; 94.08% used; 114348174 free inodes.

server4 `/data`: 105878052864 available bytes; 98.54% used; 224922786 free inodes.

server4 `/tmp`: 106075086848 available bytes; 94.08% used; 114348174 free inodes.

server4 `/var/tmp`: 106075086848 available bytes; 94.08% used; 114348174 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
