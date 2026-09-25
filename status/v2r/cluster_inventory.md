# V2R cluster inventory

2026-09-25T02:56:33.223013+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | [] | ['/tmp', '/var/tmp'] |

server1 `/`: 318952509440 available bytes; 82.21% used; 112480426 free inodes.

server1 `/home`: 318952509440 available bytes; 82.21% used; 112480426 free inodes.

server1 `/tmp`: 318952509440 available bytes; 82.21% used; 112480426 free inodes.

server1 `/var/tmp`: 318952509440 available bytes; 82.21% used; 112480426 free inodes.

server1 `/mnt/raid5`: 416156209152 available bytes; 98.09% used; 337602843 free inodes.
| server2 | True | [] | [] |

server2 `/`: 22998155264 available bytes; 98.72% used; 110410441 free inodes.

server2 `/home`: 22998155264 available bytes; 98.72% used; 110410441 free inodes.

server2 `/tmp`: 22998155264 available bytes; 98.72% used; 110410441 free inodes.

server2 `/var/tmp`: 22998155264 available bytes; 98.72% used; 110410441 free inodes.

server2 `/mnt/raid5`: 466235039744 available bytes; 96.78% used; 445113074 free inodes.
| server3 | True | [] | [] |

server3 `/`: 84346114048 available bytes; 95.29% used; 114156075 free inodes.

server3 `/home`: 84346114048 available bytes; 95.29% used; 114156075 free inodes.

server3 `/data`: 145079668736 available bytes; 97.99% used; 225810529 free inodes.

server3 `/tmp`: 84346114048 available bytes; 95.29% used; 114156075 free inodes.

server3 `/var/tmp`: 84346114048 available bytes; 95.29% used; 114156075 free inodes.
| server4 | True | ['2', '3', '4', '6', '7'] | ['/tmp', '/var/tmp'] |

server4 `/`: 105693483008 available bytes; 94.10% used; 114350922 free inodes.

server4 `/home`: 105693483008 available bytes; 94.10% used; 114350922 free inodes.

server4 `/data`: 52705759232 available bytes; 99.27% used; 224967491 free inodes.

server4 `/tmp`: 105693483008 available bytes; 94.10% used; 114350922 free inodes.

server4 `/var/tmp`: 105693483008 available bytes; 94.10% used; 114350922 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
