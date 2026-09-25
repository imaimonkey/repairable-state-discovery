# V2R cluster inventory

2026-09-25T22:32:35.783684+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | ['4', '6', '7'] | ['/tmp', '/var/tmp'] |

server1 `/`: 318694174720 available bytes; 82.22% used; 112476313 free inodes.

server1 `/home`: 318694174720 available bytes; 82.22% used; 112476313 free inodes.

server1 `/tmp`: 318694174720 available bytes; 82.22% used; 112476313 free inodes.

server1 `/var/tmp`: 318694174720 available bytes; 82.22% used; 112476313 free inodes.

server1 `/mnt/raid5`: 360239042560 available bytes; 98.35% used; 337538930 free inodes.
| server2 | True | ['2'] | [] |

server2 `/`: 22953455616 available bytes; 98.72% used; 110406238 free inodes.

server2 `/home`: 22953455616 available bytes; 98.72% used; 110406238 free inodes.

server2 `/tmp`: 22953455616 available bytes; 98.72% used; 110406238 free inodes.

server2 `/var/tmp`: 22953455616 available bytes; 98.72% used; 110406238 free inodes.

server2 `/mnt/raid5`: 298877353984 available bytes; 97.93% used; 445052742 free inodes.
| server3 | True | [] | [] |

server3 `/`: 84356517888 available bytes; 95.29% used; 114152430 free inodes.

server3 `/home`: 84356517888 available bytes; 95.29% used; 114152430 free inodes.

server3 `/data`: 124825694208 available bytes; 98.27% used; 225805891 free inodes.

server3 `/tmp`: 84356517888 available bytes; 95.29% used; 114152430 free inodes.

server3 `/var/tmp`: 84356517888 available bytes; 95.29% used; 114152430 free inodes.
| server4 | True | ['3', '7'] | ['/tmp', '/var/tmp'] |

server4 `/`: 105244356608 available bytes; 94.13% used; 114346966 free inodes.

server4 `/home`: 105244356608 available bytes; 94.13% used; 114346966 free inodes.

server4 `/data`: 192241725440 available bytes; 97.34% used; 224917713 free inodes.

server4 `/tmp`: 105244356608 available bytes; 94.13% used; 114346966 free inodes.

server4 `/var/tmp`: 105244356608 available bytes; 94.13% used; 114346966 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
