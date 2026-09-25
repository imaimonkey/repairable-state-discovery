# V2R cluster inventory

2026-09-25T23:47:29.710967+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | ['4', '6', '7'] | ['/tmp', '/var/tmp'] |

server1 `/`: 318672764928 available bytes; 82.22% used; 112476305 free inodes.

server1 `/home`: 318672764928 available bytes; 82.22% used; 112476305 free inodes.

server1 `/tmp`: 318672764928 available bytes; 82.22% used; 112476305 free inodes.

server1 `/var/tmp`: 318672764928 available bytes; 82.22% used; 112476305 free inodes.

server1 `/mnt/raid5`: 360073158656 available bytes; 98.35% used; 337538560 free inodes.
| server2 | True | ['2'] | [] |

server2 `/`: 22949343232 available bytes; 98.72% used; 110406238 free inodes.

server2 `/home`: 22949343232 available bytes; 98.72% used; 110406238 free inodes.

server2 `/tmp`: 22949343232 available bytes; 98.72% used; 110406238 free inodes.

server2 `/var/tmp`: 22949343232 available bytes; 98.72% used; 110406238 free inodes.

server2 `/mnt/raid5`: 296513593344 available bytes; 97.95% used; 445050470 free inodes.
| server3 | True | [] | [] |

server3 `/`: 84350595072 available bytes; 95.29% used; 114152446 free inodes.

server3 `/home`: 84350595072 available bytes; 95.29% used; 114152446 free inodes.

server3 `/data`: 124801597440 available bytes; 98.28% used; 225811161 free inodes.

server3 `/tmp`: 84350595072 available bytes; 95.29% used; 114152446 free inodes.

server3 `/var/tmp`: 84350595072 available bytes; 95.29% used; 114152446 free inodes.
| server4 | True | ['3', '7'] | ['/tmp', '/var/tmp'] |

server4 `/`: 105082621952 available bytes; 94.14% used; 114346616 free inodes.

server4 `/home`: 105082621952 available bytes; 94.14% used; 114346616 free inodes.

server4 `/data`: 178219196416 available bytes; 97.54% used; 224917595 free inodes.

server4 `/tmp`: 105082621952 available bytes; 94.14% used; 114346616 free inodes.

server4 `/var/tmp`: 105082621952 available bytes; 94.14% used; 114346616 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
