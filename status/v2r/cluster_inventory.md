# V2R cluster inventory

2026-09-26T00:01:14.658762+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | ['4', '5', '6', '7'] | ['/tmp', '/var/tmp'] |

server1 `/`: 318672478208 available bytes; 82.22% used; 112476311 free inodes.

server1 `/home`: 318672478208 available bytes; 82.22% used; 112476311 free inodes.

server1 `/tmp`: 318672478208 available bytes; 82.22% used; 112476311 free inodes.

server1 `/var/tmp`: 318672478208 available bytes; 82.22% used; 112476311 free inodes.

server1 `/mnt/raid5`: 360007155712 available bytes; 98.35% used; 337538494 free inodes.
| server2 | True | ['2'] | [] |

server2 `/`: 22944735232 available bytes; 98.72% used; 110406238 free inodes.

server2 `/home`: 22944735232 available bytes; 98.72% used; 110406238 free inodes.

server2 `/tmp`: 22944735232 available bytes; 98.72% used; 110406238 free inodes.

server2 `/var/tmp`: 22944735232 available bytes; 98.72% used; 110406238 free inodes.

server2 `/mnt/raid5`: 296184147968 available bytes; 97.95% used; 445050019 free inodes.
| server3 | True | [] | [] |

server3 `/`: 84347691008 available bytes; 95.29% used; 114152430 free inodes.

server3 `/home`: 84347691008 available bytes; 95.29% used; 114152430 free inodes.

server3 `/data`: 124801306624 available bytes; 98.28% used; 225810913 free inodes.

server3 `/tmp`: 84347691008 available bytes; 95.29% used; 114152430 free inodes.

server3 `/var/tmp`: 84347691008 available bytes; 95.29% used; 114152430 free inodes.
| server4 | True | ['2', '3', '6', '7'] | ['/tmp', '/var/tmp'] |

server4 `/`: 105454100480 available bytes; 94.12% used; 114348398 free inodes.

server4 `/home`: 105454100480 available bytes; 94.12% used; 114348398 free inodes.

server4 `/data`: 178053607424 available bytes; 97.54% used; 224917568 free inodes.

server4 `/tmp`: 105454100480 available bytes; 94.12% used; 114348398 free inodes.

server4 `/var/tmp`: 105454100480 available bytes; 94.12% used; 114348398 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
