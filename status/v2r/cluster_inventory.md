# V2R cluster inventory

2026-09-26T03:44:21.086794+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | ['1', '4', '5', '6', '7'] | ['/tmp', '/var/tmp'] |

server1 `/`: 318417772544 available bytes; 82.24% used; 112476273 free inodes.

server1 `/home`: 318417772544 available bytes; 82.24% used; 112476273 free inodes.

server1 `/tmp`: 318417772544 available bytes; 82.24% used; 112476273 free inodes.

server1 `/var/tmp`: 318417772544 available bytes; 82.24% used; 112476273 free inodes.

server1 `/mnt/raid5`: 330988679168 available bytes; 98.48% used; 337545738 free inodes.
| server2 | True | [] | [] |

server2 `/`: 22938996736 available bytes; 98.72% used; 110406214 free inodes.

server2 `/home`: 22938996736 available bytes; 98.72% used; 110406214 free inodes.

server2 `/tmp`: 22938996736 available bytes; 98.72% used; 110406214 free inodes.

server2 `/var/tmp`: 22938996736 available bytes; 98.72% used; 110406214 free inodes.

server2 `/mnt/raid5`: 286820126720 available bytes; 98.02% used; 445052000 free inodes.
| server3 | True | [] | [] |

server3 `/`: 84313485312 available bytes; 95.29% used; 114152362 free inodes.

server3 `/home`: 84313485312 available bytes; 95.29% used; 114152362 free inodes.

server3 `/data`: 125358129152 available bytes; 98.27% used; 225830353 free inodes.

server3 `/tmp`: 84313485312 available bytes; 95.29% used; 114152362 free inodes.

server3 `/var/tmp`: 84313485312 available bytes; 95.29% used; 114152362 free inodes.
| server4 | True | ['3', '7'] | ['/tmp', '/var/tmp'] |

server4 `/`: 105766260736 available bytes; 94.10% used; 114346784 free inodes.

server4 `/home`: 105766260736 available bytes; 94.10% used; 114346784 free inodes.

server4 `/data`: 108864286720 available bytes; 98.50% used; 224914701 free inodes.

server4 `/tmp`: 105766260736 available bytes; 94.10% used; 114346784 free inodes.

server4 `/var/tmp`: 105766260736 available bytes; 94.10% used; 114346784 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
