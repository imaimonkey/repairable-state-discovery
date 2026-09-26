# V2R cluster inventory

2026-09-26T02:32:29.630345+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | ['1', '4', '5', '6', '7'] | ['/tmp', '/var/tmp'] |

server1 `/`: 318419746816 available bytes; 82.24% used; 112476280 free inodes.

server1 `/home`: 318419746816 available bytes; 82.24% used; 112476280 free inodes.

server1 `/tmp`: 318419746816 available bytes; 82.24% used; 112476280 free inodes.

server1 `/var/tmp`: 318419746816 available bytes; 82.24% used; 112476280 free inodes.

server1 `/mnt/raid5`: 344963457024 available bytes; 98.42% used; 337546142 free inodes.
| server2 | True | [] | [] |

server2 `/`: 22942146560 available bytes; 98.72% used; 110406220 free inodes.

server2 `/home`: 22942146560 available bytes; 98.72% used; 110406220 free inodes.

server2 `/tmp`: 22942146560 available bytes; 98.72% used; 110406220 free inodes.

server2 `/var/tmp`: 22942146560 available bytes; 98.72% used; 110406220 free inodes.

server2 `/mnt/raid5`: 288361807872 available bytes; 98.01% used; 445054301 free inodes.
| server3 | True | [] | [] |

server3 `/`: 84317356032 available bytes; 95.29% used; 114152372 free inodes.

server3 `/home`: 84317356032 available bytes; 95.29% used; 114152372 free inodes.

server3 `/data`: 124788260864 available bytes; 98.28% used; 225816974 free inodes.

server3 `/tmp`: 84317356032 available bytes; 95.29% used; 114152372 free inodes.

server3 `/var/tmp`: 84317356032 available bytes; 95.29% used; 114152372 free inodes.
| server4 | True | ['2', '3', '6', '7'] | ['/tmp', '/var/tmp'] |

server4 `/`: 106126594048 available bytes; 94.08% used; 114349421 free inodes.

server4 `/home`: 106126594048 available bytes; 94.08% used; 114349421 free inodes.

server4 `/data`: 128506572800 available bytes; 98.22% used; 224915680 free inodes.

server4 `/tmp`: 106126594048 available bytes; 94.08% used; 114349421 free inodes.

server4 `/var/tmp`: 106126594048 available bytes; 94.08% used; 114349421 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
