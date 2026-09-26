# V2R cluster inventory

2026-09-26T00:31:48.286391+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | ['1', '4', '5', '6', '7'] | ['/tmp', '/var/tmp'] |

server1 `/`: 318652420096 available bytes; 82.22% used; 112476294 free inodes.

server1 `/home`: 318652420096 available bytes; 82.22% used; 112476294 free inodes.

server1 `/tmp`: 318652420096 available bytes; 82.22% used; 112476294 free inodes.

server1 `/var/tmp`: 318652420096 available bytes; 82.22% used; 112476294 free inodes.

server1 `/mnt/raid5`: 318103801856 available bytes; 98.54% used; 337546848 free inodes.
| server2 | True | [] | [] |

server2 `/`: 22940647424 available bytes; 98.72% used; 110406214 free inodes.

server2 `/home`: 22940647424 available bytes; 98.72% used; 110406214 free inodes.

server2 `/tmp`: 22940647424 available bytes; 98.72% used; 110406214 free inodes.

server2 `/var/tmp`: 22940647424 available bytes; 98.72% used; 110406214 free inodes.

server2 `/mnt/raid5`: 295039623168 available bytes; 97.96% used; 445057857 free inodes.
| server3 | True | [] | [] |

server3 `/`: 84340518912 available bytes; 95.29% used; 114152443 free inodes.

server3 `/home`: 84340518912 available bytes; 95.29% used; 114152443 free inodes.

server3 `/data`: 124944490496 available bytes; 98.27% used; 225819004 free inodes.

server3 `/tmp`: 84340518912 available bytes; 95.29% used; 114152443 free inodes.

server3 `/var/tmp`: 84340518912 available bytes; 95.29% used; 114152443 free inodes.
| server4 | True | ['2', '3', '6', '7'] | ['/tmp', '/var/tmp'] |

server4 `/`: 105453109248 available bytes; 94.12% used; 114348367 free inodes.

server4 `/home`: 105453109248 available bytes; 94.12% used; 114348367 free inodes.

server4 `/data`: 169382715392 available bytes; 97.66% used; 224917438 free inodes.

server4 `/tmp`: 105453109248 available bytes; 94.12% used; 114348367 free inodes.

server4 `/var/tmp`: 105453109248 available bytes; 94.12% used; 114348367 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
