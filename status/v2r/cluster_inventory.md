# V2R cluster inventory

2026-09-25T05:15:14.097714+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | [] | ['/tmp', '/var/tmp'] |

server1 `/`: 318892216320 available bytes; 82.21% used; 112480265 free inodes.

server1 `/home`: 318892216320 available bytes; 82.21% used; 112480265 free inodes.

server1 `/tmp`: 318892216320 available bytes; 82.21% used; 112480265 free inodes.

server1 `/var/tmp`: 318892216320 available bytes; 82.21% used; 112480265 free inodes.

server1 `/mnt/raid5`: 408545083392 available bytes; 98.13% used; 337570130 free inodes.
| server2 | True | [] | [] |

server2 `/`: 22931111936 available bytes; 98.72% used; 110410428 free inodes.

server2 `/home`: 22931111936 available bytes; 98.72% used; 110410428 free inodes.

server2 `/tmp`: 22931111936 available bytes; 98.72% used; 110410428 free inodes.

server2 `/var/tmp`: 22931111936 available bytes; 98.72% used; 110410428 free inodes.

server2 `/mnt/raid5`: 461638647808 available bytes; 96.81% used; 445108682 free inodes.
| server3 | True | [] | [] |

server3 `/`: 84339044352 available bytes; 95.29% used; 114156053 free inodes.

server3 `/home`: 84339044352 available bytes; 95.29% used; 114156053 free inodes.

server3 `/data`: 142780002304 available bytes; 98.03% used; 225815168 free inodes.

server3 `/tmp`: 84339044352 available bytes; 95.29% used; 114156053 free inodes.

server3 `/var/tmp`: 84339044352 available bytes; 95.29% used; 114156053 free inodes.
| server4 | True | ['6', '7'] | ['/tmp', '/var/tmp'] |

server4 `/`: 105658904576 available bytes; 94.10% used; 114350403 free inodes.

server4 `/home`: 105658904576 available bytes; 94.10% used; 114350403 free inodes.

server4 `/data`: 26304835584 available bytes; 99.64% used; 224960182 free inodes.

server4 `/tmp`: 105658904576 available bytes; 94.10% used; 114350403 free inodes.

server4 `/var/tmp`: 105658904576 available bytes; 94.10% used; 114350403 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
