# V2R cluster inventory

2026-09-25T23:38:19.895527+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | ['4', '6', '7'] | ['/tmp', '/var/tmp'] |

server1 `/`: 318673391616 available bytes; 82.22% used; 112476314 free inodes.

server1 `/home`: 318673391616 available bytes; 82.22% used; 112476314 free inodes.

server1 `/tmp`: 318673391616 available bytes; 82.22% used; 112476314 free inodes.

server1 `/var/tmp`: 318673391616 available bytes; 82.22% used; 112476314 free inodes.

server1 `/mnt/raid5`: 360098910208 available bytes; 98.35% used; 337538614 free inodes.
| server2 | True | ['2'] | [] |

server2 `/`: 22951489536 available bytes; 98.72% used; 110406236 free inodes.

server2 `/home`: 22951489536 available bytes; 98.72% used; 110406236 free inodes.

server2 `/tmp`: 22951489536 available bytes; 98.72% used; 110406236 free inodes.

server2 `/var/tmp`: 22951489536 available bytes; 98.72% used; 110406236 free inodes.

server2 `/mnt/raid5`: 295694622720 available bytes; 97.96% used; 445050614 free inodes.
| server3 | True | [] | [] |

server3 `/`: 84352442368 available bytes; 95.29% used; 114152440 free inodes.

server3 `/home`: 84352442368 available bytes; 95.29% used; 114152440 free inodes.

server3 `/data`: 124803600384 available bytes; 98.28% used; 225811378 free inodes.

server3 `/tmp`: 84352442368 available bytes; 95.29% used; 114152440 free inodes.

server3 `/var/tmp`: 84352442368 available bytes; 95.29% used; 114152440 free inodes.
| server4 | True | ['3', '7'] | ['/tmp', '/var/tmp'] |

server4 `/`: 105082884096 available bytes; 94.14% used; 114346616 free inodes.

server4 `/home`: 105082884096 available bytes; 94.14% used; 114346616 free inodes.

server4 `/data`: 178220392448 available bytes; 97.54% used; 224917594 free inodes.

server4 `/tmp`: 105082884096 available bytes; 94.14% used; 114346616 free inodes.

server4 `/var/tmp`: 105082884096 available bytes; 94.14% used; 114346616 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
