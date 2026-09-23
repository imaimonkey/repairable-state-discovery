# V2R cluster inventory

2026-09-23T21:39:45.090764+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | ['6', '7'] | ['/tmp', '/var/tmp', '/mnt/raid5'] |

server1 `/`: 325714362368 available bytes; 81.83% used; 112501433 free inodes.

server1 `/home`: 325714362368 available bytes; 81.83% used; 112501433 free inodes.

server1 `/tmp`: 325714362368 available bytes; 81.83% used; 112501433 free inodes.

server1 `/var/tmp`: 325714362368 available bytes; 81.83% used; 112501433 free inodes.

server1 `/mnt/raid5`: 1388131704832 available bytes; 93.63% used; 337739936 free inodes.
| server2 | True | [] | [] |

server2 `/`: 41117622272 available bytes; 97.71% used; 110432676 free inodes.

server2 `/home`: 41117622272 available bytes; 97.71% used; 110432676 free inodes.

server2 `/tmp`: 41117622272 available bytes; 97.71% used; 110432676 free inodes.

server2 `/var/tmp`: 41117622272 available bytes; 97.71% used; 110432676 free inodes.

server2 `/mnt/raid5`: 538222145536 available bytes; 96.28% used; 445208419 free inodes.
| server3 | True | [] | ['/tmp', '/var/tmp'] |

server3 `/`: 292940697600 available bytes; 83.65% used; 114208253 free inodes.

server3 `/home`: 292940697600 available bytes; 83.65% used; 114208253 free inodes.

server3 `/data`: 52268388352 available bytes; 99.28% used; 225848590 free inodes.

server3 `/tmp`: 292940697600 available bytes; 83.65% used; 114208253 free inodes.

server3 `/var/tmp`: 292940697600 available bytes; 83.65% used; 114208253 free inodes.
| server4 | True | ['0', '2', '3', '5', '6', '7'] | ['/tmp', '/var/tmp'] |

server4 `/`: 106474860544 available bytes; 94.06% used; 114355988 free inodes.

server4 `/home`: 106474860544 available bytes; 94.06% used; 114355988 free inodes.

server4 `/data`: 300263440384 available bytes; 95.85% used; 225449015 free inodes.

server4 `/tmp`: 106474860544 available bytes; 94.06% used; 114355988 free inodes.

server4 `/var/tmp`: 106474860544 available bytes; 94.06% used; 114355988 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
