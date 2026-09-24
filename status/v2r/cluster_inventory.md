# V2R cluster inventory

2026-09-24T00:10:50.402699+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | [] | ['/tmp', '/var/tmp', '/mnt/raid5'] |

server1 `/`: 325573312512 available bytes; 81.84% used; 112500804 free inodes.

server1 `/home`: 325573312512 available bytes; 81.84% used; 112500804 free inodes.

server1 `/tmp`: 325573312512 available bytes; 81.84% used; 112500804 free inodes.

server1 `/var/tmp`: 325573312512 available bytes; 81.84% used; 112500804 free inodes.

server1 `/mnt/raid5`: 1222318780416 available bytes; 94.39% used; 337735302 free inodes.
| server2 | True | [] | [] |

server2 `/`: 41007656960 available bytes; 97.71% used; 110432407 free inodes.

server2 `/home`: 41007656960 available bytes; 97.71% used; 110432407 free inodes.

server2 `/tmp`: 41007656960 available bytes; 97.71% used; 110432407 free inodes.

server2 `/var/tmp`: 41007656960 available bytes; 97.71% used; 110432407 free inodes.

server2 `/mnt/raid5`: 533275729920 available bytes; 96.32% used; 445203782 free inodes.
| server3 | True | [] | ['/tmp', '/var/tmp'] |

server3 `/`: 292606869504 available bytes; 83.67% used; 114209620 free inodes.

server3 `/home`: 292606869504 available bytes; 83.67% used; 114209620 free inodes.

server3 `/data`: 82257977344 available bytes; 98.86% used; 225844563 free inodes.

server3 `/tmp`: 292606869504 available bytes; 83.67% used; 114209620 free inodes.

server3 `/var/tmp`: 292606869504 available bytes; 83.67% used; 114209620 free inodes.
| server4 | True | ['3', '4', '6', '7'] | ['/tmp', '/var/tmp'] |

server4 `/`: 106114772992 available bytes; 94.08% used; 114350895 free inodes.

server4 `/home`: 106114772992 available bytes; 94.08% used; 114350895 free inodes.

server4 `/data`: 292911284224 available bytes; 95.95% used; 225414568 free inodes.

server4 `/tmp`: 106114772992 available bytes; 94.08% used; 114350895 free inodes.

server4 `/var/tmp`: 106114772992 available bytes; 94.08% used; 114350895 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
