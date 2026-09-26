# V2R cluster inventory

2026-09-26T08:05:45.905406+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | ['1', '4', '5', '6', '7'] | ['/tmp', '/var/tmp'] |

server1 `/`: 318750875648 available bytes; 82.22% used; 112476272 free inodes.

server1 `/home`: 318750875648 available bytes; 82.22% used; 112476272 free inodes.

server1 `/tmp`: 318750875648 available bytes; 82.22% used; 112476272 free inodes.

server1 `/var/tmp`: 318750875648 available bytes; 82.22% used; 112476272 free inodes.

server1 `/mnt/raid5`: 219165720576 available bytes; 98.99% used; 337539078 free inodes.
| server2 | True | [] | [] |

server2 `/`: 22322024448 available bytes; 98.75% used; 110403907 free inodes.

server2 `/home`: 22322024448 available bytes; 98.75% used; 110403907 free inodes.

server2 `/tmp`: 22322024448 available bytes; 98.75% used; 110403907 free inodes.

server2 `/var/tmp`: 22322024448 available bytes; 98.75% used; 110403907 free inodes.

server2 `/mnt/raid5`: 256438804480 available bytes; 98.23% used; 445025760 free inodes.
| server3 | True | [] | [] |

server3 `/`: 82679697408 available bytes; 95.39% used; 114110823 free inodes.

server3 `/home`: 82679697408 available bytes; 95.39% used; 114110823 free inodes.

server3 `/data`: 123887226880 available bytes; 98.29% used; 225820441 free inodes.

server3 `/tmp`: 82679697408 available bytes; 95.39% used; 114110823 free inodes.

server3 `/var/tmp`: 82679697408 available bytes; 95.39% used; 114110823 free inodes.
| server4 | True | ['2', '3', '6', '7'] | ['/tmp', '/var/tmp'] |

server4 `/`: 106064924672 available bytes; 94.08% used; 114348148 free inodes.

server4 `/home`: 106064924672 available bytes; 94.08% used; 114348148 free inodes.

server4 `/data`: 92610854912 available bytes; 98.72% used; 224900926 free inodes.

server4 `/tmp`: 106064924672 available bytes; 94.08% used; 114348148 free inodes.

server4 `/var/tmp`: 106064924672 available bytes; 94.08% used; 114348148 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
