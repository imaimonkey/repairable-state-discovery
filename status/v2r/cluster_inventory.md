# V2R cluster inventory

2026-09-24T00:15:29.208827+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | [] | ['/tmp', '/var/tmp', '/mnt/raid5'] |

server1 `/`: 325560418304 available bytes; 81.84% used; 112500751 free inodes.

server1 `/home`: 325560418304 available bytes; 81.84% used; 112500751 free inodes.

server1 `/tmp`: 325560418304 available bytes; 81.84% used; 112500751 free inodes.

server1 `/var/tmp`: 325560418304 available bytes; 81.84% used; 112500751 free inodes.

server1 `/mnt/raid5`: 1203064430592 available bytes; 94.48% used; 337735225 free inodes.
| server2 | True | [] | [] |

server2 `/`: 41009299456 available bytes; 97.71% used; 110432399 free inodes.

server2 `/home`: 41009299456 available bytes; 97.71% used; 110432399 free inodes.

server2 `/tmp`: 41009299456 available bytes; 97.71% used; 110432399 free inodes.

server2 `/var/tmp`: 41009299456 available bytes; 97.71% used; 110432399 free inodes.

server2 `/mnt/raid5`: 532707168256 available bytes; 96.32% used; 445204005 free inodes.
| server3 | True | [] | ['/tmp', '/var/tmp'] |

server3 `/`: 292595146752 available bytes; 83.67% used; 114206621 free inodes.

server3 `/home`: 292595146752 available bytes; 83.67% used; 114206621 free inodes.

server3 `/data`: 82252713984 available bytes; 98.86% used; 225844490 free inodes.

server3 `/tmp`: 292595146752 available bytes; 83.67% used; 114206621 free inodes.

server3 `/var/tmp`: 292595146752 available bytes; 83.67% used; 114206621 free inodes.
| server4 | True | ['1', '3', '6', '7'] | ['/tmp', '/var/tmp'] |

server4 `/`: 106104754176 available bytes; 94.08% used; 114350731 free inodes.

server4 `/home`: 106104754176 available bytes; 94.08% used; 114350731 free inodes.

server4 `/data`: 292912439296 available bytes; 95.95% used; 225414568 free inodes.

server4 `/tmp`: 106104754176 available bytes; 94.08% used; 114350731 free inodes.

server4 `/var/tmp`: 106104754176 available bytes; 94.08% used; 114350731 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
