# V2R cluster inventory

2026-09-25T01:18:04.494047+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | [] | ['/tmp', '/var/tmp'] |

server1 `/`: 319078547456 available bytes; 82.20% used; 112480770 free inodes.

server1 `/home`: 319078547456 available bytes; 82.20% used; 112480770 free inodes.

server1 `/tmp`: 319078547456 available bytes; 82.20% used; 112480770 free inodes.

server1 `/var/tmp`: 319078547456 available bytes; 82.20% used; 112480770 free inodes.

server1 `/mnt/raid5`: 416511102976 available bytes; 98.09% used; 337614354 free inodes.
| server2 | True | ['2'] | [] |

server2 `/`: 23058771968 available bytes; 98.71% used; 110410770 free inodes.

server2 `/home`: 23058771968 available bytes; 98.71% used; 110410770 free inodes.

server2 `/tmp`: 23058771968 available bytes; 98.71% used; 110410770 free inodes.

server2 `/var/tmp`: 23058771968 available bytes; 98.71% used; 110410770 free inodes.

server2 `/mnt/raid5`: 497411186688 available bytes; 96.56% used; 445162025 free inodes.
| server3 | True | [] | [] |

server3 `/`: 84357951488 available bytes; 95.29% used; 114156087 free inodes.

server3 `/home`: 84357951488 available bytes; 95.29% used; 114156087 free inodes.

server3 `/data`: 146895867904 available bytes; 97.97% used; 225812537 free inodes.

server3 `/tmp`: 84357951488 available bytes; 95.29% used; 114156087 free inodes.

server3 `/var/tmp`: 84357951488 available bytes; 95.29% used; 114156087 free inodes.
| server4 | True | ['0', '1', '4', '5', '7'] | ['/tmp', '/var/tmp'] |

server4 `/`: 105779253248 available bytes; 94.10% used; 114348295 free inodes.

server4 `/home`: 105779253248 available bytes; 94.10% used; 114348295 free inodes.

server4 `/data`: 53324353536 available bytes; 99.26% used; 225030748 free inodes.

server4 `/tmp`: 105779253248 available bytes; 94.10% used; 114348295 free inodes.

server4 `/var/tmp`: 105779253248 available bytes; 94.10% used; 114348295 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
