# V2R cluster inventory

2026-09-26T02:30:57.945989+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | ['1', '4', '5', '6', '7'] | ['/tmp', '/var/tmp'] |

server1 `/`: 318418472960 available bytes; 82.24% used; 112476279 free inodes.

server1 `/home`: 318418472960 available bytes; 82.24% used; 112476279 free inodes.

server1 `/tmp`: 318418472960 available bytes; 82.24% used; 112476279 free inodes.

server1 `/var/tmp`: 318418472960 available bytes; 82.24% used; 112476279 free inodes.

server1 `/mnt/raid5`: 344963833856 available bytes; 98.42% used; 337546144 free inodes.
| server2 | True | [] | [] |

server2 `/`: 22942203904 available bytes; 98.72% used; 110406220 free inodes.

server2 `/home`: 22942203904 available bytes; 98.72% used; 110406220 free inodes.

server2 `/tmp`: 22942203904 available bytes; 98.72% used; 110406220 free inodes.

server2 `/var/tmp`: 22942203904 available bytes; 98.72% used; 110406220 free inodes.

server2 `/mnt/raid5`: 288943181824 available bytes; 98.00% used; 445054457 free inodes.
| server3 | True | [] | [] |

server3 `/`: 84317503488 available bytes; 95.29% used; 114152372 free inodes.

server3 `/home`: 84317503488 available bytes; 95.29% used; 114152372 free inodes.

server3 `/data`: 124788686848 available bytes; 98.28% used; 225816988 free inodes.

server3 `/tmp`: 84317503488 available bytes; 95.29% used; 114152372 free inodes.

server3 `/var/tmp`: 84317503488 available bytes; 95.29% used; 114152372 free inodes.
| server4 | True | ['2', '3', '6', '7'] | ['/tmp', '/var/tmp'] |

server4 `/`: 106126647296 available bytes; 94.08% used; 114349422 free inodes.

server4 `/home`: 106126647296 available bytes; 94.08% used; 114349422 free inodes.

server4 `/data`: 130850959360 available bytes; 98.19% used; 224915694 free inodes.

server4 `/tmp`: 106126647296 available bytes; 94.08% used; 114349422 free inodes.

server4 `/var/tmp`: 106126647296 available bytes; 94.08% used; 114349422 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
