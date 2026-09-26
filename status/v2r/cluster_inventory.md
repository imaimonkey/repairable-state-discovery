# V2R cluster inventory

2026-09-26T06:53:56.376626+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | ['1', '4', '5', '6', '7'] | ['/tmp', '/var/tmp'] |

server1 `/`: 318770192384 available bytes; 82.22% used; 112476293 free inodes.

server1 `/home`: 318770192384 available bytes; 82.22% used; 112476293 free inodes.

server1 `/tmp`: 318770192384 available bytes; 82.22% used; 112476293 free inodes.

server1 `/var/tmp`: 318770192384 available bytes; 82.22% used; 112476293 free inodes.

server1 `/mnt/raid5`: 219314941952 available bytes; 98.99% used; 337539610 free inodes.
| server2 | True | [] | [] |

server2 `/`: 22321696768 available bytes; 98.75% used; 110403874 free inodes.

server2 `/home`: 22321696768 available bytes; 98.75% used; 110403874 free inodes.

server2 `/tmp`: 22321696768 available bytes; 98.75% used; 110403874 free inodes.

server2 `/var/tmp`: 22321696768 available bytes; 98.75% used; 110403874 free inodes.

server2 `/mnt/raid5`: 272347025408 available bytes; 98.12% used; 445028399 free inodes.
| server3 | True | [] | [] |

server3 `/`: 82566225920 available bytes; 95.39% used; 114110898 free inodes.

server3 `/home`: 82566225920 available bytes; 95.39% used; 114110898 free inodes.

server3 `/data`: 123992993792 available bytes; 98.29% used; 225821883 free inodes.

server3 `/tmp`: 82566225920 available bytes; 95.39% used; 114110898 free inodes.

server3 `/var/tmp`: 82566225920 available bytes; 95.39% used; 114110898 free inodes.
| server4 | True | ['2', '3', '6', '7'] | ['/tmp', '/var/tmp'] |

server4 `/`: 106075570176 available bytes; 94.08% used; 114348174 free inodes.

server4 `/home`: 106075570176 available bytes; 94.08% used; 114348174 free inodes.

server4 `/data`: 105906073600 available bytes; 98.54% used; 224923070 free inodes.

server4 `/tmp`: 106075570176 available bytes; 94.08% used; 114348174 free inodes.

server4 `/var/tmp`: 106075570176 available bytes; 94.08% used; 114348174 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
