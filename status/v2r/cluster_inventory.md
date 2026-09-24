# V2R cluster inventory

2026-09-24T00:41:46.182567+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | [] | ['/tmp', '/var/tmp', '/mnt/raid5'] |

server1 `/`: 325540663296 available bytes; 81.84% used; 112500466 free inodes.

server1 `/home`: 325540663296 available bytes; 81.84% used; 112500466 free inodes.

server1 `/tmp`: 325540663296 available bytes; 81.84% used; 112500466 free inodes.

server1 `/var/tmp`: 325540663296 available bytes; 81.84% used; 112500466 free inodes.

server1 `/mnt/raid5`: 1094865461248 available bytes; 94.98% used; 337735013 free inodes.
| server2 | True | [] | [] |

server2 `/`: 40984100864 available bytes; 97.71% used; 110432297 free inodes.

server2 `/home`: 40984100864 available bytes; 97.71% used; 110432297 free inodes.

server2 `/tmp`: 40984100864 available bytes; 97.71% used; 110432297 free inodes.

server2 `/var/tmp`: 40984100864 available bytes; 97.71% used; 110432297 free inodes.

server2 `/mnt/raid5`: 532423819264 available bytes; 96.32% used; 445202959 free inodes.
| server3 | True | [] | ['/tmp', '/var/tmp'] |

server3 `/`: 292085338112 available bytes; 83.70% used; 114182020 free inodes.

server3 `/home`: 292085338112 available bytes; 83.70% used; 114182020 free inodes.

server3 `/data`: 82229788672 available bytes; 98.86% used; 225843931 free inodes.

server3 `/tmp`: 292085338112 available bytes; 83.70% used; 114182020 free inodes.

server3 `/var/tmp`: 292085338112 available bytes; 83.70% used; 114182020 free inodes.
| server4 | True | ['1', '3', '6', '7'] | ['/tmp', '/var/tmp'] |

server4 `/`: 106059931648 available bytes; 94.08% used; 114350034 free inodes.

server4 `/home`: 106059931648 available bytes; 94.08% used; 114350034 free inodes.

server4 `/data`: 292918190080 available bytes; 95.95% used; 225414580 free inodes.

server4 `/tmp`: 106059931648 available bytes; 94.08% used; 114350034 free inodes.

server4 `/var/tmp`: 106059931648 available bytes; 94.08% used; 114350034 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
