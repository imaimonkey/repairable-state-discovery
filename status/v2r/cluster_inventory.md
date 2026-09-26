# V2R cluster inventory

2026-09-26T06:50:53.005938+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | ['1', '4', '5', '6', '7'] | ['/tmp', '/var/tmp'] |

server1 `/`: 318770724864 available bytes; 82.22% used; 112476295 free inodes.

server1 `/home`: 318770724864 available bytes; 82.22% used; 112476295 free inodes.

server1 `/tmp`: 318770724864 available bytes; 82.22% used; 112476295 free inodes.

server1 `/var/tmp`: 318770724864 available bytes; 82.22% used; 112476295 free inodes.

server1 `/mnt/raid5`: 219322363904 available bytes; 98.99% used; 337539626 free inodes.
| server2 | True | [] | [] |

server2 `/`: 22320451584 available bytes; 98.75% used; 110403874 free inodes.

server2 `/home`: 22320451584 available bytes; 98.75% used; 110403874 free inodes.

server2 `/tmp`: 22320451584 available bytes; 98.75% used; 110403874 free inodes.

server2 `/var/tmp`: 22320451584 available bytes; 98.75% used; 110403874 free inodes.

server2 `/mnt/raid5`: 272423436288 available bytes; 98.12% used; 445028257 free inodes.
| server3 | True | [] | [] |

server3 `/`: 82566967296 available bytes; 95.39% used; 114110893 free inodes.

server3 `/home`: 82566967296 available bytes; 95.39% used; 114110893 free inodes.

server3 `/data`: 123990523904 available bytes; 98.29% used; 225821934 free inodes.

server3 `/tmp`: 82566967296 available bytes; 95.39% used; 114110893 free inodes.

server3 `/var/tmp`: 82566967296 available bytes; 95.39% used; 114110893 free inodes.
| server4 | True | ['2', '3', '6', '7'] | ['/tmp', '/var/tmp'] |

server4 `/`: 106075660288 available bytes; 94.08% used; 114348174 free inodes.

server4 `/home`: 106075660288 available bytes; 94.08% used; 114348174 free inodes.

server4 `/data`: 105904984064 available bytes; 98.54% used; 224923084 free inodes.

server4 `/tmp`: 106075660288 available bytes; 94.08% used; 114348174 free inodes.

server4 `/var/tmp`: 106075660288 available bytes; 94.08% used; 114348174 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
