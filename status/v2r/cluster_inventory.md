# V2R cluster inventory

2026-09-26T20:39:38.954778+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | ['0', '3', '4', '5', '6', '7'] | ['/tmp', '/var/tmp'] |

server1 `/`: 315482574848 available bytes; 82.40% used; 112444688 free inodes.

server1 `/home`: 315482574848 available bytes; 82.40% used; 112444688 free inodes.

server1 `/tmp`: 315482574848 available bytes; 82.40% used; 112444688 free inodes.

server1 `/var/tmp`: 315482574848 available bytes; 82.40% used; 112444688 free inodes.

server1 `/mnt/raid5`: 645855846400 available bytes; 97.04% used; 337467123 free inodes.
| server2 | True | ['2', '7'] | [] |

server2 `/`: 17975320576 available bytes; 99.00% used; 110367099 free inodes.

server2 `/home`: 17975320576 available bytes; 99.00% used; 110367099 free inodes.

server2 `/tmp`: 17975320576 available bytes; 99.00% used; 110367099 free inodes.

server2 `/var/tmp`: 17975320576 available bytes; 99.00% used; 110367099 free inodes.

server2 `/mnt/raid5`: 600412983296 available bytes; 95.85% used; 444964401 free inodes.
| server3 | True | [] | [] |

server3 `/`: 81263775744 available bytes; 95.47% used; 114065289 free inodes.

server3 `/home`: 81263775744 available bytes; 95.47% used; 114065289 free inodes.

server3 `/data`: 1348607410176 available bytes; 81.36% used; 225831578 free inodes.

server3 `/tmp`: 81263775744 available bytes; 95.47% used; 114065289 free inodes.

server3 `/var/tmp`: 81263775744 available bytes; 95.47% used; 114065289 free inodes.
| server4 | True | ['5'] | ['/tmp', '/var/tmp'] |

server4 `/`: 105918840832 available bytes; 94.09% used; 114347838 free inodes.

server4 `/home`: 105918840832 available bytes; 94.09% used; 114347838 free inodes.

server4 `/data`: 410088849408 available bytes; 94.33% used; 224823711 free inodes.

server4 `/tmp`: 105918840832 available bytes; 94.09% used; 114347838 free inodes.

server4 `/var/tmp`: 105918840832 available bytes; 94.09% used; 114347838 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
