# V2R cluster inventory

2026-09-24T01:42:08.702491+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | ['4', '6', '7'] | ['/tmp', '/var/tmp'] |

server1 `/`: 325457776640 available bytes; 81.84% used; 112499485 free inodes.

server1 `/home`: 325457776640 available bytes; 81.84% used; 112499485 free inodes.

server1 `/tmp`: 325457776640 available bytes; 81.84% used; 112499485 free inodes.

server1 `/var/tmp`: 325457776640 available bytes; 81.84% used; 112499485 free inodes.

server1 `/mnt/raid5`: 847376584704 available bytes; 96.11% used; 337733892 free inodes.
| server2 | True | [] | [] |

server2 `/`: 40935911424 available bytes; 97.72% used; 110431901 free inodes.

server2 `/home`: 40935911424 available bytes; 97.72% used; 110431901 free inodes.

server2 `/tmp`: 40935911424 available bytes; 97.72% used; 110431901 free inodes.

server2 `/var/tmp`: 40935911424 available bytes; 97.72% used; 110431901 free inodes.

server2 `/mnt/raid5`: 530426134528 available bytes; 96.33% used; 445201116 free inodes.
| server3 | True | [] | ['/tmp', '/var/tmp'] |

server3 `/`: 292713517056 available bytes; 83.67% used; 114211072 free inodes.

server3 `/home`: 292713517056 available bytes; 83.67% used; 114211072 free inodes.

server3 `/data`: 71401730048 available bytes; 99.01% used; 225842041 free inodes.

server3 `/tmp`: 292713517056 available bytes; 83.67% used; 114211072 free inodes.

server3 `/var/tmp`: 292713517056 available bytes; 83.67% used; 114211072 free inodes.
| server4 | True | ['2', '3', '6', '7'] | ['/tmp', '/var/tmp'] |

server4 `/`: 105954570240 available bytes; 94.09% used; 114348624 free inodes.

server4 `/home`: 105954570240 available bytes; 94.09% used; 114348624 free inodes.

server4 `/data`: 289768325120 available bytes; 96.00% used; 225388486 free inodes.

server4 `/tmp`: 105954570240 available bytes; 94.09% used; 114348624 free inodes.

server4 `/var/tmp`: 105954570240 available bytes; 94.09% used; 114348624 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
