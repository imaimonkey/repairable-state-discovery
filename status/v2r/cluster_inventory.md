# V2R cluster inventory

2026-09-24T00:30:56.662973+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | [] | ['/tmp', '/var/tmp', '/mnt/raid5'] |

server1 `/`: 325550833664 available bytes; 81.84% used; 112500585 free inodes.

server1 `/home`: 325550833664 available bytes; 81.84% used; 112500585 free inodes.

server1 `/tmp`: 325550833664 available bytes; 81.84% used; 112500585 free inodes.

server1 `/var/tmp`: 325550833664 available bytes; 81.84% used; 112500585 free inodes.

server1 `/mnt/raid5`: 1140329713664 available bytes; 94.77% used; 337735147 free inodes.
| server2 | True | [] | [] |

server2 `/`: 40994988032 available bytes; 97.71% used; 110432336 free inodes.

server2 `/home`: 40994988032 available bytes; 97.71% used; 110432336 free inodes.

server2 `/tmp`: 40994988032 available bytes; 97.71% used; 110432336 free inodes.

server2 `/var/tmp`: 40994988032 available bytes; 97.71% used; 110432336 free inodes.

server2 `/mnt/raid5`: 532749672448 available bytes; 96.32% used; 445203426 free inodes.
| server3 | True | [] | ['/tmp', '/var/tmp'] |

server3 `/`: 292196110336 available bytes; 83.69% used; 114186382 free inodes.

server3 `/home`: 292196110336 available bytes; 83.69% used; 114186382 free inodes.

server3 `/data`: 82237214720 available bytes; 98.86% used; 225844211 free inodes.

server3 `/tmp`: 292196110336 available bytes; 83.69% used; 114186382 free inodes.

server3 `/var/tmp`: 292196110336 available bytes; 83.69% used; 114186382 free inodes.
| server4 | True | ['1', '3', '6', '7'] | ['/tmp', '/var/tmp'] |

server4 `/`: 106078638080 available bytes; 94.08% used; 114350327 free inodes.

server4 `/home`: 106078638080 available bytes; 94.08% used; 114350327 free inodes.

server4 `/data`: 292922523648 available bytes; 95.95% used; 225414579 free inodes.

server4 `/tmp`: 106078638080 available bytes; 94.08% used; 114350327 free inodes.

server4 `/var/tmp`: 106078638080 available bytes; 94.08% used; 114350327 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
