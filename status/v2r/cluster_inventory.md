# V2R cluster inventory

2026-09-24T00:35:35.030179+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | [] | ['/tmp', '/var/tmp', '/mnt/raid5'] |

server1 `/`: 325546311680 available bytes; 81.84% used; 112500532 free inodes.

server1 `/home`: 325546311680 available bytes; 81.84% used; 112500532 free inodes.

server1 `/tmp`: 325546311680 available bytes; 81.84% used; 112500532 free inodes.

server1 `/var/tmp`: 325546311680 available bytes; 81.84% used; 112500532 free inodes.

server1 `/mnt/raid5`: 1120945954816 available bytes; 94.86% used; 337735075 free inodes.
| server2 | True | [] | [] |

server2 `/`: 40992727040 available bytes; 97.71% used; 110432319 free inodes.

server2 `/home`: 40992727040 available bytes; 97.71% used; 110432319 free inodes.

server2 `/tmp`: 40992727040 available bytes; 97.71% used; 110432319 free inodes.

server2 `/var/tmp`: 40992727040 available bytes; 97.71% used; 110432319 free inodes.

server2 `/mnt/raid5`: 532615290880 available bytes; 96.32% used; 445203152 free inodes.
| server3 | True | [] | ['/tmp', '/var/tmp'] |

server3 `/`: 292291411968 available bytes; 83.69% used; 114187576 free inodes.

server3 `/home`: 292291411968 available bytes; 83.69% used; 114187576 free inodes.

server3 `/data`: 82235248640 available bytes; 98.86% used; 225844117 free inodes.

server3 `/tmp`: 292291411968 available bytes; 83.69% used; 114187576 free inodes.

server3 `/var/tmp`: 292291411968 available bytes; 83.69% used; 114187576 free inodes.
| server4 | True | ['1', '3', '6', '7'] | ['/tmp', '/var/tmp'] |

server4 `/`: 106070556672 available bytes; 94.08% used; 114350198 free inodes.

server4 `/home`: 106070556672 available bytes; 94.08% used; 114350198 free inodes.

server4 `/data`: 292922855424 available bytes; 95.95% used; 225414581 free inodes.

server4 `/tmp`: 106070556672 available bytes; 94.08% used; 114350198 free inodes.

server4 `/var/tmp`: 106070556672 available bytes; 94.08% used; 114350198 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
