# V2R cluster inventory

2026-09-26T03:26:01.202104+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | ['1', '4', '5', '6', '7'] | ['/tmp', '/var/tmp'] |

server1 `/`: 318416302080 available bytes; 82.24% used; 112476260 free inodes.

server1 `/home`: 318416302080 available bytes; 82.24% used; 112476260 free inodes.

server1 `/tmp`: 318416302080 available bytes; 82.24% used; 112476260 free inodes.

server1 `/var/tmp`: 318416302080 available bytes; 82.24% used; 112476260 free inodes.

server1 `/mnt/raid5`: 331027275776 available bytes; 98.48% used; 337545837 free inodes.
| server2 | True | [] | [] |

server2 `/`: 22933794816 available bytes; 98.72% used; 110406212 free inodes.

server2 `/home`: 22933794816 available bytes; 98.72% used; 110406212 free inodes.

server2 `/tmp`: 22933794816 available bytes; 98.72% used; 110406212 free inodes.

server2 `/var/tmp`: 22933794816 available bytes; 98.72% used; 110406212 free inodes.

server2 `/mnt/raid5`: 286840266752 available bytes; 98.02% used; 445052923 free inodes.
| server3 | True | [] | [] |

server3 `/`: 84309143552 available bytes; 95.30% used; 114152362 free inodes.

server3 `/home`: 84309143552 available bytes; 95.30% used; 114152362 free inodes.

server3 `/data`: 125429649408 available bytes; 98.27% used; 225830689 free inodes.

server3 `/tmp`: 84309143552 available bytes; 95.30% used; 114152362 free inodes.

server3 `/var/tmp`: 84309143552 available bytes; 95.30% used; 114152362 free inodes.
| server4 | True | ['3', '7'] | ['/tmp', '/var/tmp'] |

server4 `/`: 105842393088 available bytes; 94.09% used; 114346959 free inodes.

server4 `/home`: 105842393088 available bytes; 94.09% used; 114346959 free inodes.

server4 `/data`: 108955672576 available bytes; 98.49% used; 224914809 free inodes.

server4 `/tmp`: 105842393088 available bytes; 94.09% used; 114346959 free inodes.

server4 `/var/tmp`: 105842393088 available bytes; 94.09% used; 114346959 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
