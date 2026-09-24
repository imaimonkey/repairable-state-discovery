# V2R cluster inventory

2026-09-24T01:23:33.628933+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | ['4'] | ['/tmp', '/var/tmp'] |

server1 `/`: 325467451392 available bytes; 81.84% used; 112499758 free inodes.

server1 `/home`: 325467451392 available bytes; 81.84% used; 112499758 free inodes.

server1 `/tmp`: 325467451392 available bytes; 81.84% used; 112499758 free inodes.

server1 `/var/tmp`: 325467451392 available bytes; 81.84% used; 112499758 free inodes.

server1 `/mnt/raid5`: 924393373696 available bytes; 95.76% used; 337734015 free inodes.
| server2 | True | [] | [] |

server2 `/`: 40952020992 available bytes; 97.72% used; 110432045 free inodes.

server2 `/home`: 40952020992 available bytes; 97.72% used; 110432045 free inodes.

server2 `/tmp`: 40952020992 available bytes; 97.72% used; 110432045 free inodes.

server2 `/var/tmp`: 40952020992 available bytes; 97.72% used; 110432045 free inodes.

server2 `/mnt/raid5`: 531152855040 available bytes; 96.33% used; 445201801 free inodes.
| server3 | True | [] | ['/tmp', '/var/tmp'] |

server3 `/`: 292346961920 available bytes; 83.69% used; 114187454 free inodes.

server3 `/home`: 292346961920 available bytes; 83.69% used; 114187454 free inodes.

server3 `/data`: 82048454656 available bytes; 98.87% used; 225842407 free inodes.

server3 `/tmp`: 292346961920 available bytes; 83.69% used; 114187454 free inodes.

server3 `/var/tmp`: 292346961920 available bytes; 83.69% used; 114187454 free inodes.
| server4 | True | ['2', '3', '6', '7'] | ['/tmp', '/var/tmp'] |

server4 `/`: 105974640640 available bytes; 94.09% used; 114348944 free inodes.

server4 `/home`: 105974640640 available bytes; 94.09% used; 114348944 free inodes.

server4 `/data`: 290827247616 available bytes; 95.98% used; 225396988 free inodes.

server4 `/tmp`: 105974640640 available bytes; 94.09% used; 114348944 free inodes.

server4 `/var/tmp`: 105974640640 available bytes; 94.09% used; 114348944 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
