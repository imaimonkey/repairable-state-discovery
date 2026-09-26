# V2R cluster inventory

2026-09-26T01:52:45.581928+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | ['1', '4', '5', '6', '7'] | ['/tmp', '/var/tmp'] |

server1 `/`: 318527983616 available bytes; 82.23% used; 112476294 free inodes.

server1 `/home`: 318527983616 available bytes; 82.23% used; 112476294 free inodes.

server1 `/tmp`: 318527983616 available bytes; 82.23% used; 112476294 free inodes.

server1 `/var/tmp`: 318527983616 available bytes; 82.23% used; 112476294 free inodes.

server1 `/mnt/raid5`: 345241890816 available bytes; 98.42% used; 337546335 free inodes.
| server2 | True | [] | [] |

server2 `/`: 22931542016 available bytes; 98.72% used; 110406216 free inodes.

server2 `/home`: 22931542016 available bytes; 98.72% used; 110406216 free inodes.

server2 `/tmp`: 22931542016 available bytes; 98.72% used; 110406216 free inodes.

server2 `/var/tmp`: 22931542016 available bytes; 98.72% used; 110406216 free inodes.

server2 `/mnt/raid5`: 290061062144 available bytes; 98.00% used; 445055212 free inodes.
| server3 | True | [] | [] |

server3 `/`: 84326711296 available bytes; 95.29% used; 114152366 free inodes.

server3 `/home`: 84326711296 available bytes; 95.29% used; 114152366 free inodes.

server3 `/data`: 124797059072 available bytes; 98.28% used; 225817640 free inodes.

server3 `/tmp`: 84326711296 available bytes; 95.29% used; 114152366 free inodes.

server3 `/var/tmp`: 84326711296 available bytes; 95.29% used; 114152366 free inodes.
| server4 | True | ['2', '3', '6', '7'] | ['/tmp', '/var/tmp'] |

server4 `/`: 105433964544 available bytes; 94.12% used; 114348357 free inodes.

server4 `/home`: 105433964544 available bytes; 94.12% used; 114348357 free inodes.

server4 `/data`: 130909110272 available bytes; 98.19% used; 224915772 free inodes.

server4 `/tmp`: 105433964544 available bytes; 94.12% used; 114348357 free inodes.

server4 `/var/tmp`: 105433964544 available bytes; 94.12% used; 114348357 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
