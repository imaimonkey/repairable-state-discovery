# V2R cluster inventory

2026-09-25T21:39:07.617524+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | ['4', '6', '7'] | ['/tmp', '/var/tmp'] |

server1 `/`: 318701252608 available bytes; 82.22% used; 112476319 free inodes.

server1 `/home`: 318701252608 available bytes; 82.22% used; 112476319 free inodes.

server1 `/tmp`: 318701252608 available bytes; 82.22% used; 112476319 free inodes.

server1 `/var/tmp`: 318701252608 available bytes; 82.22% used; 112476319 free inodes.

server1 `/mnt/raid5`: 360507908096 available bytes; 98.35% used; 337539233 free inodes.
| server2 | True | [] | [] |

server2 `/`: 22899683328 available bytes; 98.72% used; 110405686 free inodes.

server2 `/home`: 22899683328 available bytes; 98.72% used; 110405686 free inodes.

server2 `/tmp`: 22899683328 available bytes; 98.72% used; 110405686 free inodes.

server2 `/var/tmp`: 22899683328 available bytes; 98.72% used; 110405686 free inodes.

server2 `/mnt/raid5`: 300450430976 available bytes; 97.92% used; 445054328 free inodes.
| server3 | True | [] | [] |

server3 `/`: 84366872576 available bytes; 95.29% used; 114152626 free inodes.

server3 `/home`: 84366872576 available bytes; 95.29% used; 114152626 free inodes.

server3 `/data`: 125889413120 available bytes; 98.26% used; 225806832 free inodes.

server3 `/tmp`: 84366872576 available bytes; 95.29% used; 114152626 free inodes.

server3 `/var/tmp`: 84366872576 available bytes; 95.29% used; 114152626 free inodes.
| server4 | True | ['3', '7'] | ['/tmp', '/var/tmp'] |

server4 `/`: 105388761088 available bytes; 94.12% used; 114347330 free inodes.

server4 `/home`: 105388761088 available bytes; 94.12% used; 114347330 free inodes.

server4 `/data`: 216675778560 available bytes; 97.01% used; 224919898 free inodes.

server4 `/tmp`: 105388761088 available bytes; 94.12% used; 114347330 free inodes.

server4 `/var/tmp`: 105388761088 available bytes; 94.12% used; 114347330 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
