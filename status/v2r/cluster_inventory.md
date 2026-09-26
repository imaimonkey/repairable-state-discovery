# V2R cluster inventory

2026-09-26T21:11:40.129999+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | ['0', '3', '4', '5', '6', '7'] | ['/tmp', '/var/tmp'] |

server1 `/`: 315481272320 available bytes; 82.40% used; 112445685 free inodes.

server1 `/home`: 315481272320 available bytes; 82.40% used; 112445685 free inodes.

server1 `/tmp`: 315481272320 available bytes; 82.40% used; 112445685 free inodes.

server1 `/var/tmp`: 315481272320 available bytes; 82.40% used; 112445685 free inodes.

server1 `/mnt/raid5`: 645854441472 available bytes; 97.04% used; 337467123 free inodes.
| server2 | True | ['2', '7'] | [] |

server2 `/`: 17933668352 available bytes; 99.00% used; 110367527 free inodes.

server2 `/home`: 17933668352 available bytes; 99.00% used; 110367527 free inodes.

server2 `/tmp`: 17933668352 available bytes; 99.00% used; 110367527 free inodes.

server2 `/var/tmp`: 17933668352 available bytes; 99.00% used; 110367527 free inodes.

server2 `/mnt/raid5`: 599221669888 available bytes; 95.86% used; 444963389 free inodes.
| server3 | True | [] | [] |

server3 `/`: 81266274304 available bytes; 95.47% used; 114065308 free inodes.

server3 `/home`: 81266274304 available bytes; 95.47% used; 114065308 free inodes.

server3 `/data`: 1351141838848 available bytes; 81.33% used; 225831896 free inodes.

server3 `/tmp`: 81266274304 available bytes; 95.47% used; 114065308 free inodes.

server3 `/var/tmp`: 81266274304 available bytes; 95.47% used; 114065308 free inodes.
| server4 | True | ['5', '7'] | ['/tmp', '/var/tmp'] |

server4 `/`: 105917968384 available bytes; 94.09% used; 114347843 free inodes.

server4 `/home`: 105917968384 available bytes; 94.09% used; 114347843 free inodes.

server4 `/data`: 409914273792 available bytes; 94.33% used; 224823843 free inodes.

server4 `/tmp`: 105917968384 available bytes; 94.09% used; 114347843 free inodes.

server4 `/var/tmp`: 105917968384 available bytes; 94.09% used; 114347843 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
