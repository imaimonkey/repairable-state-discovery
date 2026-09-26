# V2R cluster inventory

2026-09-26T01:16:05.466096+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | ['1', '4', '5', '6', '7'] | ['/tmp', '/var/tmp'] |

server1 `/`: 318657556480 available bytes; 82.22% used; 112476296 free inodes.

server1 `/home`: 318657556480 available bytes; 82.22% used; 112476296 free inodes.

server1 `/tmp`: 318657556480 available bytes; 82.22% used; 112476296 free inodes.

server1 `/var/tmp`: 318657556480 available bytes; 82.22% used; 112476296 free inodes.

server1 `/mnt/raid5`: 345531555840 available bytes; 98.41% used; 337546622 free inodes.
| server2 | True | [] | [] |

server2 `/`: 22938431488 available bytes; 98.72% used; 110406204 free inodes.

server2 `/home`: 22938431488 available bytes; 98.72% used; 110406204 free inodes.

server2 `/tmp`: 22938431488 available bytes; 98.72% used; 110406204 free inodes.

server2 `/var/tmp`: 22938431488 available bytes; 98.72% used; 110406204 free inodes.

server2 `/mnt/raid5`: 291117924352 available bytes; 97.99% used; 445056107 free inodes.
| server3 | True | [] | [] |

server3 `/`: 84341424128 available bytes; 95.29% used; 114152430 free inodes.

server3 `/home`: 84341424128 available bytes; 95.29% used; 114152430 free inodes.

server3 `/data`: 124933472256 available bytes; 98.27% used; 225818268 free inodes.

server3 `/tmp`: 84341424128 available bytes; 95.29% used; 114152430 free inodes.

server3 `/var/tmp`: 84341424128 available bytes; 95.29% used; 114152430 free inodes.
| server4 | True | ['3', '7'] | ['/tmp', '/var/tmp'] |

server4 `/`: 105281314816 available bytes; 94.12% used; 114347079 free inodes.

server4 `/home`: 105281314816 available bytes; 94.12% used; 114347079 free inodes.

server4 `/data`: 141690421248 available bytes; 98.04% used; 224917311 free inodes.

server4 `/tmp`: 105281314816 available bytes; 94.12% used; 114347079 free inodes.

server4 `/var/tmp`: 105281314816 available bytes; 94.12% used; 114347079 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
