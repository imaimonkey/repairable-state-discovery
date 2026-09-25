# V2R cluster inventory

2026-09-25T23:32:12.945944+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | ['4', '6', '7'] | ['/tmp', '/var/tmp'] |

server1 `/`: 318674956288 available bytes; 82.22% used; 112476314 free inodes.

server1 `/home`: 318674956288 available bytes; 82.22% used; 112476314 free inodes.

server1 `/tmp`: 318674956288 available bytes; 82.22% used; 112476314 free inodes.

server1 `/var/tmp`: 318674956288 available bytes; 82.22% used; 112476314 free inodes.

server1 `/mnt/raid5`: 360110907392 available bytes; 98.35% used; 337538642 free inodes.
| server2 | True | ['2'] | [] |

server2 `/`: 22945099776 available bytes; 98.72% used; 110406234 free inodes.

server2 `/home`: 22945099776 available bytes; 98.72% used; 110406234 free inodes.

server2 `/tmp`: 22945099776 available bytes; 98.72% used; 110406234 free inodes.

server2 `/var/tmp`: 22945099776 available bytes; 98.72% used; 110406234 free inodes.

server2 `/mnt/raid5`: 297212112896 available bytes; 97.95% used; 445050836 free inodes.
| server3 | True | [] | [] |

server3 `/`: 84349014016 available bytes; 95.29% used; 114152442 free inodes.

server3 `/home`: 84349014016 available bytes; 95.29% used; 114152442 free inodes.

server3 `/data`: 124820221952 available bytes; 98.27% used; 225811544 free inodes.

server3 `/tmp`: 84349014016 available bytes; 95.29% used; 114152442 free inodes.

server3 `/var/tmp`: 84349014016 available bytes; 95.29% used; 114152442 free inodes.
| server4 | True | ['3', '7'] | ['/tmp', '/var/tmp'] |

server4 `/`: 105083052032 available bytes; 94.14% used; 114346616 free inodes.

server4 `/home`: 105083052032 available bytes; 94.14% used; 114346616 free inodes.

server4 `/data`: 178221207552 available bytes; 97.54% used; 224917599 free inodes.

server4 `/tmp`: 105083052032 available bytes; 94.14% used; 114346616 free inodes.

server4 `/var/tmp`: 105083052032 available bytes; 94.14% used; 114346616 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
