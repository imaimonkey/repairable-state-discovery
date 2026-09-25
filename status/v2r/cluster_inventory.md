# V2R cluster inventory

2026-09-25T22:28:00.849884+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | ['4', '6', '7'] | ['/tmp', '/var/tmp'] |

server1 `/`: 318695464960 available bytes; 82.22% used; 112476307 free inodes.

server1 `/home`: 318695464960 available bytes; 82.22% used; 112476307 free inodes.

server1 `/tmp`: 318695464960 available bytes; 82.22% used; 112476307 free inodes.

server1 `/var/tmp`: 318695464960 available bytes; 82.22% used; 112476307 free inodes.

server1 `/mnt/raid5`: 360251072512 available bytes; 98.35% used; 337538955 free inodes.
| server2 | True | ['2'] | [] |

server2 `/`: 22955548672 available bytes; 98.72% used; 110406238 free inodes.

server2 `/home`: 22955548672 available bytes; 98.72% used; 110406238 free inodes.

server2 `/tmp`: 22955548672 available bytes; 98.72% used; 110406238 free inodes.

server2 `/var/tmp`: 22955548672 available bytes; 98.72% used; 110406238 free inodes.

server2 `/mnt/raid5`: 299042426880 available bytes; 97.93% used; 445052980 free inodes.
| server3 | True | [] | [] |

server3 `/`: 84354637824 available bytes; 95.29% used; 114152442 free inodes.

server3 `/home`: 84354637824 available bytes; 95.29% used; 114152442 free inodes.

server3 `/data`: 124827648000 available bytes; 98.27% used; 225805983 free inodes.

server3 `/tmp`: 84354637824 available bytes; 95.29% used; 114152442 free inodes.

server3 `/var/tmp`: 84354637824 available bytes; 95.29% used; 114152442 free inodes.
| server4 | True | ['3', '7'] | ['/tmp', '/var/tmp'] |

server4 `/`: 105244520448 available bytes; 94.13% used; 114346967 free inodes.

server4 `/home`: 105244520448 available bytes; 94.13% used; 114346967 free inodes.

server4 `/data`: 192842678272 available bytes; 97.33% used; 224917741 free inodes.

server4 `/tmp`: 105244520448 available bytes; 94.13% used; 114346967 free inodes.

server4 `/var/tmp`: 105244520448 available bytes; 94.13% used; 114346967 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
