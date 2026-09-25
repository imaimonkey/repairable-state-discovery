# V2R cluster inventory

2026-09-25T23:56:39.751576+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | ['4', '5', '6', '7'] | ['/tmp', '/var/tmp'] |

server1 `/`: 318672551936 available bytes; 82.22% used; 112476308 free inodes.

server1 `/home`: 318672551936 available bytes; 82.22% used; 112476308 free inodes.

server1 `/tmp`: 318672551936 available bytes; 82.22% used; 112476308 free inodes.

server1 `/var/tmp`: 318672551936 available bytes; 82.22% used; 112476308 free inodes.

server1 `/mnt/raid5`: 360041889792 available bytes; 98.35% used; 337538523 free inodes.
| server2 | True | ['2'] | [] |

server2 `/`: 22943477760 available bytes; 98.72% used; 110406234 free inodes.

server2 `/home`: 22943477760 available bytes; 98.72% used; 110406234 free inodes.

server2 `/tmp`: 22943477760 available bytes; 98.72% used; 110406234 free inodes.

server2 `/var/tmp`: 22943477760 available bytes; 98.72% used; 110406234 free inodes.

server2 `/mnt/raid5`: 296241967104 available bytes; 97.95% used; 445049992 free inodes.
| server3 | True | [] | [] |

server3 `/`: 84346658816 available bytes; 95.29% used; 114152430 free inodes.

server3 `/home`: 84346658816 available bytes; 95.29% used; 114152430 free inodes.

server3 `/data`: 124804067328 available bytes; 98.28% used; 225810990 free inodes.

server3 `/tmp`: 84346658816 available bytes; 95.29% used; 114152430 free inodes.

server3 `/var/tmp`: 84346658816 available bytes; 95.29% used; 114152430 free inodes.
| server4 | True | ['3', '7'] | ['/tmp', '/var/tmp'] |

server4 `/`: 105082318848 available bytes; 94.14% used; 114346616 free inodes.

server4 `/home`: 105082318848 available bytes; 94.14% used; 114346616 free inodes.

server4 `/data`: 178215735296 available bytes; 97.54% used; 224917578 free inodes.

server4 `/tmp`: 105082318848 available bytes; 94.14% used; 114346616 free inodes.

server4 `/var/tmp`: 105082318848 available bytes; 94.14% used; 114346616 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
