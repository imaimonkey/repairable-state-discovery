# V2R cluster inventory

2026-09-23T23:20:54.580037+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | ['6', '7'] | ['/tmp', '/var/tmp', '/mnt/raid5'] | reference_compatible=False |

server1 `/`: 325663301632 available bytes; 81.83% used; 112501611 free inodes.

server1 `/home`: 325663301632 available bytes; 81.83% used; 112501611 free inodes.

server1 `/tmp`: 325663301632 available bytes; 81.83% used; 112501611 free inodes.

server1 `/var/tmp`: 325663301632 available bytes; 81.83% used; 112501611 free inodes.

server1 `/mnt/raid5`: 1377630449664 available bytes; 93.68% used; 337739767 free inodes.
| server2 | True | [] | [] | reference_compatible=False |

server2 `/`: 41048559616 available bytes; 97.71% used; 110432604 free inodes.

server2 `/home`: 41048559616 available bytes; 97.71% used; 110432604 free inodes.

server2 `/tmp`: 41048559616 available bytes; 97.71% used; 110432604 free inodes.

server2 `/var/tmp`: 41048559616 available bytes; 97.71% used; 110432604 free inodes.

server2 `/mnt/raid5`: 534775173120 available bytes; 96.30% used; 445205783 free inodes.
| server3 | True | ['3'] | ['/tmp', '/var/tmp'] | reference_compatible=True |

server3 `/`: 292246142976 available bytes; 83.69% used; 114171233 free inodes.

server3 `/home`: 292246142976 available bytes; 83.69% used; 114171233 free inodes.

server3 `/data`: 82320588800 available bytes; 98.86% used; 225845945 free inodes.

server3 `/tmp`: 292246142976 available bytes; 83.69% used; 114171233 free inodes.

server3 `/var/tmp`: 292246142976 available bytes; 83.69% used; 114171233 free inodes.
| server4 | True | ['3', '6', '7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 106249785344 available bytes; 94.07% used; 114352685 free inodes.

server4 `/home`: 106249785344 available bytes; 94.07% used; 114352685 free inodes.

server4 `/data`: 293789827072 available bytes; 95.94% used; 225426622 free inodes.

server4 `/tmp`: 106249785344 available bytes; 94.07% used; 114352685 free inodes.

server4 `/var/tmp`: 106249785344 available bytes; 94.07% used; 114352685 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
