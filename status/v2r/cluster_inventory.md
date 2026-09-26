# V2R cluster inventory

2026-09-26T02:14:09.585820+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | ['1', '4', '5', '6', '7'] | ['/tmp', '/var/tmp'] |

server1 `/`: 318419083264 available bytes; 82.24% used; 112476284 free inodes.

server1 `/home`: 318419083264 available bytes; 82.24% used; 112476284 free inodes.

server1 `/tmp`: 318419083264 available bytes; 82.24% used; 112476284 free inodes.

server1 `/var/tmp`: 318419083264 available bytes; 82.24% used; 112476284 free inodes.

server1 `/mnt/raid5`: 345199927296 available bytes; 98.42% used; 337546242 free inodes.
| server2 | True | [] | [] |

server2 `/`: 22938554368 available bytes; 98.72% used; 110406216 free inodes.

server2 `/home`: 22938554368 available bytes; 98.72% used; 110406216 free inodes.

server2 `/tmp`: 22938554368 available bytes; 98.72% used; 110406216 free inodes.

server2 `/var/tmp`: 22938554368 available bytes; 98.72% used; 110406216 free inodes.

server2 `/mnt/raid5`: 289426804736 available bytes; 98.00% used; 445054431 free inodes.
| server3 | True | [] | [] |

server3 `/`: 84326739968 available bytes; 95.29% used; 114152370 free inodes.

server3 `/home`: 84326739968 available bytes; 95.29% used; 114152370 free inodes.

server3 `/data`: 124791721984 available bytes; 98.28% used; 225817269 free inodes.

server3 `/tmp`: 84326739968 available bytes; 95.29% used; 114152370 free inodes.

server3 `/var/tmp`: 84326739968 available bytes; 95.29% used; 114152370 free inodes.
| server4 | True | ['2', '3', '6', '7'] | ['/tmp', '/var/tmp'] |

server4 `/`: 105433362432 available bytes; 94.12% used; 114348357 free inodes.

server4 `/home`: 105433362432 available bytes; 94.12% used; 114348357 free inodes.

server4 `/data`: 130905174016 available bytes; 98.19% used; 224915760 free inodes.

server4 `/tmp`: 105433362432 available bytes; 94.12% used; 114348357 free inodes.

server4 `/var/tmp`: 105433362432 available bytes; 94.12% used; 114348357 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
