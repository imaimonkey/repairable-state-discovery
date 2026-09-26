# V2R cluster inventory

2026-09-26T00:10:24.673585+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | ['4', '5', '6', '7'] | ['/tmp', '/var/tmp'] |

server1 `/`: 318670708736 available bytes; 82.22% used; 112476313 free inodes.

server1 `/home`: 318670708736 available bytes; 82.22% used; 112476313 free inodes.

server1 `/tmp`: 318670708736 available bytes; 82.22% used; 112476313 free inodes.

server1 `/var/tmp`: 318670708736 available bytes; 82.22% used; 112476313 free inodes.

server1 `/mnt/raid5`: 359576408064 available bytes; 98.35% used; 337547073 free inodes.
| server2 | True | ['2'] | [] |

server2 `/`: 22950879232 available bytes; 98.72% used; 110406226 free inodes.

server2 `/home`: 22950879232 available bytes; 98.72% used; 110406226 free inodes.

server2 `/tmp`: 22950879232 available bytes; 98.72% used; 110406226 free inodes.

server2 `/var/tmp`: 22950879232 available bytes; 98.72% used; 110406226 free inodes.

server2 `/mnt/raid5`: 296062640128 available bytes; 97.95% used; 445058132 free inodes.
| server3 | True | [] | [] |

server3 `/`: 84342599680 available bytes; 95.29% used; 114152433 free inodes.

server3 `/home`: 84342599680 available bytes; 95.29% used; 114152433 free inodes.

server3 `/data`: 124946186240 available bytes; 98.27% used; 225819382 free inodes.

server3 `/tmp`: 84342599680 available bytes; 95.29% used; 114152433 free inodes.

server3 `/var/tmp`: 84342599680 available bytes; 95.29% used; 114152433 free inodes.
| server4 | True | ['2', '3', '6', '7'] | ['/tmp', '/var/tmp'] |

server4 `/`: 105453846528 available bytes; 94.12% used; 114348398 free inodes.

server4 `/home`: 105453846528 available bytes; 94.12% used; 114348398 free inodes.

server4 `/data`: 178052837376 available bytes; 97.54% used; 224917556 free inodes.

server4 `/tmp`: 105453846528 available bytes; 94.12% used; 114348398 free inodes.

server4 `/var/tmp`: 105453846528 available bytes; 94.12% used; 114348398 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
