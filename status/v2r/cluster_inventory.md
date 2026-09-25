# V2R cluster inventory

2026-09-25T02:59:39.485830+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | [] | ['/tmp', '/var/tmp'] |

server1 `/`: 318941401088 available bytes; 82.21% used; 112480390 free inodes.

server1 `/home`: 318941401088 available bytes; 82.21% used; 112480390 free inodes.

server1 `/tmp`: 318941401088 available bytes; 82.21% used; 112480390 free inodes.

server1 `/var/tmp`: 318941401088 available bytes; 82.21% used; 112480390 free inodes.

server1 `/mnt/raid5`: 416147488768 available bytes; 98.09% used; 337602474 free inodes.
| server2 | True | [] | [] |

server2 `/`: 22998470656 available bytes; 98.72% used; 110410443 free inodes.

server2 `/home`: 22998470656 available bytes; 98.72% used; 110410443 free inodes.

server2 `/tmp`: 22998470656 available bytes; 98.72% used; 110410443 free inodes.

server2 `/var/tmp`: 22998470656 available bytes; 98.72% used; 110410443 free inodes.

server2 `/mnt/raid5`: 466133340160 available bytes; 96.78% used; 445112938 free inodes.
| server3 | True | [] | [] |

server3 `/`: 84346109952 available bytes; 95.29% used; 114156075 free inodes.

server3 `/home`: 84346109952 available bytes; 95.29% used; 114156075 free inodes.

server3 `/data`: 145021124608 available bytes; 98.00% used; 225810471 free inodes.

server3 `/tmp`: 84346109952 available bytes; 95.29% used; 114156075 free inodes.

server3 `/var/tmp`: 84346109952 available bytes; 95.29% used; 114156075 free inodes.
| server4 | True | ['2', '3', '6', '7'] | ['/tmp', '/var/tmp'] |

server4 `/`: 105693290496 available bytes; 94.10% used; 114350903 free inodes.

server4 `/home`: 105693290496 available bytes; 94.10% used; 114350903 free inodes.

server4 `/data`: 51875041280 available bytes; 99.28% used; 224967464 free inodes.

server4 `/tmp`: 105693290496 available bytes; 94.10% used; 114350903 free inodes.

server4 `/var/tmp`: 105693290496 available bytes; 94.10% used; 114350903 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
