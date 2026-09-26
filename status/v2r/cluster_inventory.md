# V2R cluster inventory

2026-09-26T00:02:46.322399+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | ['4', '5', '6', '7'] | ['/tmp', '/var/tmp'] |

server1 `/`: 318672183296 available bytes; 82.22% used; 112476310 free inodes.

server1 `/home`: 318672183296 available bytes; 82.22% used; 112476310 free inodes.

server1 `/tmp`: 318672183296 available bytes; 82.22% used; 112476310 free inodes.

server1 `/var/tmp`: 318672183296 available bytes; 82.22% used; 112476310 free inodes.

server1 `/mnt/raid5`: 359439650816 available bytes; 98.35% used; 337538418 free inodes.
| server2 | True | ['2'] | [] |

server2 `/`: 22944567296 available bytes; 98.72% used; 110406236 free inodes.

server2 `/home`: 22944567296 available bytes; 98.72% used; 110406236 free inodes.

server2 `/tmp`: 22944567296 available bytes; 98.72% used; 110406236 free inodes.

server2 `/var/tmp`: 22944567296 available bytes; 98.72% used; 110406236 free inodes.

server2 `/mnt/raid5`: 296136433664 available bytes; 97.95% used; 445049862 free inodes.
| server3 | True | [] | [] |

server3 `/`: 84347592704 available bytes; 95.29% used; 114152430 free inodes.

server3 `/home`: 84347592704 available bytes; 95.29% used; 114152430 free inodes.

server3 `/data`: 124799438848 available bytes; 98.28% used; 225810841 free inodes.

server3 `/tmp`: 84347592704 available bytes; 95.29% used; 114152430 free inodes.

server3 `/var/tmp`: 84347592704 available bytes; 95.29% used; 114152430 free inodes.
| server4 | True | ['2', '3', '6', '7'] | ['/tmp', '/var/tmp'] |

server4 `/`: 105454051328 available bytes; 94.12% used; 114348398 free inodes.

server4 `/home`: 105454051328 available bytes; 94.12% used; 114348398 free inodes.

server4 `/data`: 178052751360 available bytes; 97.54% used; 224917567 free inodes.

server4 `/tmp`: 105454051328 available bytes; 94.12% used; 114348398 free inodes.

server4 `/var/tmp`: 105454051328 available bytes; 94.12% used; 114348398 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
