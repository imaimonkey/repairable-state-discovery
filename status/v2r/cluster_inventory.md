# V2R cluster inventory

2026-09-25T03:42:45.298147+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | [] | ['/tmp', '/var/tmp'] |

server1 `/`: 318939029504 available bytes; 82.21% used; 112480350 free inodes.

server1 `/home`: 318939029504 available bytes; 82.21% used; 112480350 free inodes.

server1 `/tmp`: 318939029504 available bytes; 82.21% used; 112480350 free inodes.

server1 `/var/tmp`: 318939029504 available bytes; 82.21% used; 112480350 free inodes.

server1 `/mnt/raid5`: 416010825728 available bytes; 98.09% used; 337597396 free inodes.
| server2 | True | [] | [] |

server2 `/`: 22974476288 available bytes; 98.72% used; 110410442 free inodes.

server2 `/home`: 22974476288 available bytes; 98.72% used; 110410442 free inodes.

server2 `/tmp`: 22974476288 available bytes; 98.72% used; 110410442 free inodes.

server2 `/var/tmp`: 22974476288 available bytes; 98.72% used; 110410442 free inodes.

server2 `/mnt/raid5`: 464508448768 available bytes; 96.79% used; 445111520 free inodes.
| server3 | True | [] | [] |

server3 `/`: 84340748288 available bytes; 95.29% used; 114156064 free inodes.

server3 `/home`: 84340748288 available bytes; 95.29% used; 114156064 free inodes.

server3 `/data`: 144378470400 available bytes; 98.00% used; 225817228 free inodes.

server3 `/tmp`: 84340748288 available bytes; 95.29% used; 114156064 free inodes.

server3 `/var/tmp`: 84340748288 available bytes; 95.29% used; 114156064 free inodes.
| server4 | True | ['6', '7'] | ['/tmp', '/var/tmp'] |

server4 `/`: 105683472384 available bytes; 94.10% used; 114350897 free inodes.

server4 `/home`: 105683472384 available bytes; 94.10% used; 114350897 free inodes.

server4 `/data`: 39154475008 available bytes; 99.46% used; 224965609 free inodes.

server4 `/tmp`: 105683472384 available bytes; 94.10% used; 114350897 free inodes.

server4 `/var/tmp`: 105683472384 available bytes; 94.10% used; 114350897 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
