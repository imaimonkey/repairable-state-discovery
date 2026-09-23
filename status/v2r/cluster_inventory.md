# V2R cluster inventory

2026-09-23T21:50:31.410595+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | ['6', '7'] | ['/tmp', '/var/tmp', '/mnt/raid5'] |

server1 `/`: 325714104320 available bytes; 81.83% used; 112501403 free inodes.

server1 `/home`: 325714104320 available bytes; 81.83% used; 112501403 free inodes.

server1 `/tmp`: 325714104320 available bytes; 81.83% used; 112501403 free inodes.

server1 `/var/tmp`: 325714104320 available bytes; 81.83% used; 112501403 free inodes.

server1 `/mnt/raid5`: 1388122382336 available bytes; 93.63% used; 337739914 free inodes.
| server2 | True | [] | [] |

server2 `/`: 41105371136 available bytes; 97.71% used; 110432649 free inodes.

server2 `/home`: 41105371136 available bytes; 97.71% used; 110432649 free inodes.

server2 `/tmp`: 41105371136 available bytes; 97.71% used; 110432649 free inodes.

server2 `/var/tmp`: 41105371136 available bytes; 97.71% used; 110432649 free inodes.

server2 `/mnt/raid5`: 537894060032 available bytes; 96.28% used; 445208098 free inodes.
| server3 | True | [] | ['/tmp', '/var/tmp'] |

server3 `/`: 293052690432 available bytes; 83.65% used; 114223999 free inodes.

server3 `/home`: 293052690432 available bytes; 83.65% used; 114223999 free inodes.

server3 `/data`: 82469904384 available bytes; 98.86% used; 225848050 free inodes.

server3 `/tmp`: 293052690432 available bytes; 83.65% used; 114223999 free inodes.

server3 `/var/tmp`: 293052690432 available bytes; 83.65% used; 114223999 free inodes.
| server4 | True | ['3', '5', '6', '7'] | ['/tmp', '/var/tmp'] |

server4 `/`: 106463715328 available bytes; 94.06% used; 114355823 free inodes.

server4 `/home`: 106463715328 available bytes; 94.06% used; 114355823 free inodes.

server4 `/data`: 300234149888 available bytes; 95.85% used; 225446947 free inodes.

server4 `/tmp`: 106463715328 available bytes; 94.06% used; 114355823 free inodes.

server4 `/var/tmp`: 106463715328 available bytes; 94.06% used; 114355823 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
