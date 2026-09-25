# V2R cluster inventory

2026-09-25T03:41:13.241071+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | ['4'] | ['/tmp', '/var/tmp'] |

server1 `/`: 318939381760 available bytes; 82.21% used; 112480350 free inodes.

server1 `/home`: 318939381760 available bytes; 82.21% used; 112480350 free inodes.

server1 `/tmp`: 318939381760 available bytes; 82.21% used; 112480350 free inodes.

server1 `/var/tmp`: 318939381760 available bytes; 82.21% used; 112480350 free inodes.

server1 `/mnt/raid5`: 416062595072 available bytes; 98.09% used; 337597617 free inodes.
| server2 | True | [] | [] |

server2 `/`: 22975660032 available bytes; 98.72% used; 110410442 free inodes.

server2 `/home`: 22975660032 available bytes; 98.72% used; 110410442 free inodes.

server2 `/tmp`: 22975660032 available bytes; 98.72% used; 110410442 free inodes.

server2 `/var/tmp`: 22975660032 available bytes; 98.72% used; 110410442 free inodes.

server2 `/mnt/raid5`: 464029249536 available bytes; 96.79% used; 445111682 free inodes.
| server3 | True | [] | [] |

server3 `/`: 84340760576 available bytes; 95.29% used; 114156064 free inodes.

server3 `/home`: 84340760576 available bytes; 95.29% used; 114156064 free inodes.

server3 `/data`: 144403357696 available bytes; 98.00% used; 225817255 free inodes.

server3 `/tmp`: 84340760576 available bytes; 95.29% used; 114156064 free inodes.

server3 `/var/tmp`: 84340760576 available bytes; 95.29% used; 114156064 free inodes.
| server4 | True | ['6', '7'] | ['/tmp', '/var/tmp'] |

server4 `/`: 105683513344 available bytes; 94.10% used; 114350897 free inodes.

server4 `/home`: 105683513344 available bytes; 94.10% used; 114350897 free inodes.

server4 `/data`: 39157239808 available bytes; 99.46% used; 224965679 free inodes.

server4 `/tmp`: 105683513344 available bytes; 94.10% used; 114350897 free inodes.

server4 `/var/tmp`: 105683513344 available bytes; 94.10% used; 114350897 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
