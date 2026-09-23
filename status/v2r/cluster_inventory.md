# V2R cluster inventory

2026-09-23T23:19:52.331101+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | ['6', '7'] | ['/tmp', '/var/tmp', '/mnt/raid5'] |

server1 `/`: 325663494144 available bytes; 81.83% used; 112501611 free inodes.

server1 `/home`: 325663494144 available bytes; 81.83% used; 112501611 free inodes.

server1 `/tmp`: 325663494144 available bytes; 81.83% used; 112501611 free inodes.

server1 `/var/tmp`: 325663494144 available bytes; 81.83% used; 112501611 free inodes.

server1 `/mnt/raid5`: 1381817114624 available bytes; 93.66% used; 337739788 free inodes.
| server2 | True | [] | [] |

server2 `/`: 41048801280 available bytes; 97.71% used; 110432604 free inodes.

server2 `/home`: 41048801280 available bytes; 97.71% used; 110432604 free inodes.

server2 `/tmp`: 41048801280 available bytes; 97.71% used; 110432604 free inodes.

server2 `/var/tmp`: 41048801280 available bytes; 97.71% used; 110432604 free inodes.

server2 `/mnt/raid5`: 534822952960 available bytes; 96.30% used; 445205918 free inodes.
| server3 | True | ['3'] | ['/tmp', '/var/tmp'] |

server3 `/`: 292246396928 available bytes; 83.69% used; 114171233 free inodes.

server3 `/home`: 292246396928 available bytes; 83.69% used; 114171233 free inodes.

server3 `/data`: 82323120128 available bytes; 98.86% used; 225845965 free inodes.

server3 `/tmp`: 292246396928 available bytes; 83.69% used; 114171233 free inodes.

server3 `/var/tmp`: 292246396928 available bytes; 83.69% used; 114171233 free inodes.
| server4 | True | ['3', '6', '7'] | ['/tmp', '/var/tmp'] |

server4 `/`: 106252111872 available bytes; 94.07% used; 114352728 free inodes.

server4 `/home`: 106252111872 available bytes; 94.07% used; 114352728 free inodes.

server4 `/data`: 294276034560 available bytes; 95.93% used; 225426979 free inodes.

server4 `/tmp`: 106252111872 available bytes; 94.07% used; 114352728 free inodes.

server4 `/var/tmp`: 106252111872 available bytes; 94.07% used; 114352728 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
