# V2R cluster inventory

2026-09-26T00:27:13.422135+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | ['1', '4', '5', '6', '7'] | ['/tmp', '/var/tmp'] |

server1 `/`: 318653698048 available bytes; 82.22% used; 112476264 free inodes.

server1 `/home`: 318653698048 available bytes; 82.22% used; 112476264 free inodes.

server1 `/tmp`: 318653698048 available bytes; 82.22% used; 112476264 free inodes.

server1 `/var/tmp`: 318653698048 available bytes; 82.22% used; 112476264 free inodes.

server1 `/mnt/raid5`: 359402475520 available bytes; 98.35% used; 337546906 free inodes.
| server2 | True | [] | [] |

server2 `/`: 22942535680 available bytes; 98.72% used; 110406214 free inodes.

server2 `/home`: 22942535680 available bytes; 98.72% used; 110406214 free inodes.

server2 `/tmp`: 22942535680 available bytes; 98.72% used; 110406214 free inodes.

server2 `/var/tmp`: 22942535680 available bytes; 98.72% used; 110406214 free inodes.

server2 `/mnt/raid5`: 295180984320 available bytes; 97.96% used; 445057854 free inodes.
| server3 | True | [] | [] |

server3 `/`: 84339036160 available bytes; 95.29% used; 114152441 free inodes.

server3 `/home`: 84339036160 available bytes; 95.29% used; 114152441 free inodes.

server3 `/data`: 124948381696 available bytes; 98.27% used; 225819100 free inodes.

server3 `/tmp`: 84339036160 available bytes; 95.29% used; 114152441 free inodes.

server3 `/var/tmp`: 84339036160 available bytes; 95.29% used; 114152441 free inodes.
| server4 | True | ['3', '7'] | ['/tmp', '/var/tmp'] |

server4 `/`: 105453264896 available bytes; 94.12% used; 114348365 free inodes.

server4 `/home`: 105453264896 available bytes; 94.12% used; 114348365 free inodes.

server4 `/data`: 177807646720 available bytes; 97.54% used; 224917510 free inodes.

server4 `/tmp`: 105453264896 available bytes; 94.12% used; 114348365 free inodes.

server4 `/var/tmp`: 105453264896 available bytes; 94.12% used; 114348365 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
