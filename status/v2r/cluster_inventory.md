# V2R cluster inventory

2026-09-26T05:01:25.576894+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | ['1', '4', '5', '6', '7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 318398468096 available bytes; 82.24% used; 112476278 free inodes.

server1 `/home`: 318398468096 available bytes; 82.24% used; 112476278 free inodes.

server1 `/tmp`: 318398468096 available bytes; 82.24% used; 112476278 free inodes.

server1 `/var/tmp`: 318398468096 available bytes; 82.24% used; 112476278 free inodes.

server1 `/mnt/raid5`: 329920053248 available bytes; 98.49% used; 337544718 free inodes.
| server2 | True | [] | [] | reference_compatible=False |

server2 `/`: 22929879040 available bytes; 98.72% used; 110406196 free inodes.

server2 `/home`: 22929879040 available bytes; 98.72% used; 110406196 free inodes.

server2 `/tmp`: 22929879040 available bytes; 98.72% used; 110406196 free inodes.

server2 `/var/tmp`: 22929879040 available bytes; 98.72% used; 110406196 free inodes.

server2 `/mnt/raid5`: 284593451008 available bytes; 98.03% used; 445049912 free inodes.
| server3 | True | [] | [] | reference_compatible=True |

server3 `/`: 83810779136 available bytes; 95.32% used; 114139098 free inodes.

server3 `/home`: 83810779136 available bytes; 95.32% used; 114139098 free inodes.

server3 `/data`: 124620574720 available bytes; 98.28% used; 225825639 free inodes.

server3 `/tmp`: 83810779136 available bytes; 95.32% used; 114139098 free inodes.

server3 `/var/tmp`: 83810779136 available bytes; 95.32% used; 114139098 free inodes.
| server4 | True | ['2', '3', '6', '7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 105993138176 available bytes; 94.09% used; 114348206 free inodes.

server4 `/home`: 105993138176 available bytes; 94.09% used; 114348206 free inodes.

server4 `/data`: 107000156160 available bytes; 98.52% used; 224929219 free inodes.

server4 `/tmp`: 105993138176 available bytes; 94.09% used; 114348206 free inodes.

server4 `/var/tmp`: 105993138176 available bytes; 94.09% used; 114348206 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
