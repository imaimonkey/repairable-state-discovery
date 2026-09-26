# V2R cluster inventory

2026-09-26T03:33:39.613510+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | ['1', '4', '5', '6', '7'] | ['/tmp', '/var/tmp'] |

server1 `/`: 318416633856 available bytes; 82.24% used; 112476264 free inodes.

server1 `/home`: 318416633856 available bytes; 82.24% used; 112476264 free inodes.

server1 `/tmp`: 318416633856 available bytes; 82.24% used; 112476264 free inodes.

server1 `/var/tmp`: 318416633856 available bytes; 82.24% used; 112476264 free inodes.

server1 `/mnt/raid5`: 331014426624 available bytes; 98.48% used; 337545810 free inodes.
| server2 | True | [] | [] |

server2 `/`: 22940913664 available bytes; 98.72% used; 110406216 free inodes.

server2 `/home`: 22940913664 available bytes; 98.72% used; 110406216 free inodes.

server2 `/tmp`: 22940913664 available bytes; 98.72% used; 110406216 free inodes.

server2 `/var/tmp`: 22940913664 available bytes; 98.72% used; 110406216 free inodes.

server2 `/mnt/raid5`: 287140261888 available bytes; 98.02% used; 445052567 free inodes.
| server3 | True | [] | [] |

server3 `/`: 84311105536 available bytes; 95.30% used; 114152362 free inodes.

server3 `/home`: 84311105536 available bytes; 95.30% used; 114152362 free inodes.

server3 `/data`: 125425012736 available bytes; 98.27% used; 225830547 free inodes.

server3 `/tmp`: 84311105536 available bytes; 95.30% used; 114152362 free inodes.

server3 `/var/tmp`: 84311105536 available bytes; 95.30% used; 114152362 free inodes.
| server4 | True | ['3', '7'] | ['/tmp', '/var/tmp'] |

server4 `/`: 105800155136 available bytes; 94.10% used; 114346872 free inodes.

server4 `/home`: 105800155136 available bytes; 94.10% used; 114346872 free inodes.

server4 `/data`: 108925739008 available bytes; 98.49% used; 224914757 free inodes.

server4 `/tmp`: 105800155136 available bytes; 94.10% used; 114346872 free inodes.

server4 `/var/tmp`: 105800155136 available bytes; 94.10% used; 114346872 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
