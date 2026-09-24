# V2R cluster inventory

2026-09-24T02:03:56.046283+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | ['4', '6', '7'] | ['/tmp', '/var/tmp'] |

server1 `/`: 325447098368 available bytes; 81.84% used; 112499283 free inodes.

server1 `/home`: 325447098368 available bytes; 81.84% used; 112499283 free inodes.

server1 `/tmp`: 325447098368 available bytes; 81.84% used; 112499283 free inodes.

server1 `/var/tmp`: 325447098368 available bytes; 81.84% used; 112499283 free inodes.

server1 `/mnt/raid5`: 758608740352 available bytes; 96.52% used; 337733591 free inodes.
| server2 | True | [] | [] |

server2 `/`: 40912297984 available bytes; 97.72% used; 110431724 free inodes.

server2 `/home`: 40912297984 available bytes; 97.72% used; 110431724 free inodes.

server2 `/tmp`: 40912297984 available bytes; 97.72% used; 110431724 free inodes.

server2 `/var/tmp`: 40912297984 available bytes; 97.72% used; 110431724 free inodes.

server2 `/mnt/raid5`: 529280634880 available bytes; 96.34% used; 445200297 free inodes.
| server3 | True | [] | ['/tmp', '/var/tmp'] |

server3 `/`: 292714700800 available bytes; 83.67% used; 114211273 free inodes.

server3 `/home`: 292714700800 available bytes; 83.67% used; 114211273 free inodes.

server3 `/data`: 60193738752 available bytes; 99.17% used; 225841585 free inodes.

server3 `/tmp`: 292714700800 available bytes; 83.67% used; 114211273 free inodes.

server3 `/var/tmp`: 292714700800 available bytes; 83.67% used; 114211273 free inodes.
| server4 | True | ['2', '3', '6', '7'] | ['/tmp', '/var/tmp'] |

server4 `/`: 105938173952 available bytes; 94.09% used; 114348463 free inodes.

server4 `/home`: 105938173952 available bytes; 94.09% used; 114348463 free inodes.

server4 `/data`: 289776582656 available bytes; 96.00% used; 225388486 free inodes.

server4 `/tmp`: 105938173952 available bytes; 94.09% used; 114348463 free inodes.

server4 `/var/tmp`: 105938173952 available bytes; 94.09% used; 114348463 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
