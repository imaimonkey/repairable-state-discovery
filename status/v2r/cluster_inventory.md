# V2R cluster inventory

2026-09-26T02:03:28.202007+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | ['1', '4', '5', '6', '7'] | ['/tmp', '/var/tmp'] |

server1 `/`: 318518595584 available bytes; 82.23% used; 112476290 free inodes.

server1 `/home`: 318518595584 available bytes; 82.23% used; 112476290 free inodes.

server1 `/tmp`: 318518595584 available bytes; 82.23% used; 112476290 free inodes.

server1 `/var/tmp`: 318518595584 available bytes; 82.23% used; 112476290 free inodes.

server1 `/mnt/raid5`: 345222049792 available bytes; 98.42% used; 337546298 free inodes.
| server2 | True | [] | [] |

server2 `/`: 22943481856 available bytes; 98.72% used; 110406218 free inodes.

server2 `/home`: 22943481856 available bytes; 98.72% used; 110406218 free inodes.

server2 `/tmp`: 22943481856 available bytes; 98.72% used; 110406218 free inodes.

server2 `/var/tmp`: 22943481856 available bytes; 98.72% used; 110406218 free inodes.

server2 `/mnt/raid5`: 289728929792 available bytes; 98.00% used; 445054727 free inodes.
| server3 | True | [] | [] |

server3 `/`: 84325425152 available bytes; 95.29% used; 114152368 free inodes.

server3 `/home`: 84325425152 available bytes; 95.29% used; 114152368 free inodes.

server3 `/data`: 124793446400 available bytes; 98.28% used; 225817445 free inodes.

server3 `/tmp`: 84325425152 available bytes; 95.29% used; 114152368 free inodes.

server3 `/var/tmp`: 84325425152 available bytes; 95.29% used; 114152368 free inodes.
| server4 | True | ['2', '3', '6', '7'] | ['/tmp', '/var/tmp'] |

server4 `/`: 105433645056 available bytes; 94.12% used; 114348357 free inodes.

server4 `/home`: 105433645056 available bytes; 94.12% used; 114348357 free inodes.

server4 `/data`: 130904944640 available bytes; 98.19% used; 224915763 free inodes.

server4 `/tmp`: 105433645056 available bytes; 94.12% used; 114348357 free inodes.

server4 `/var/tmp`: 105433645056 available bytes; 94.12% used; 114348357 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
