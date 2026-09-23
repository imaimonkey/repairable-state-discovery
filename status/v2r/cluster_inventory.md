# V2R cluster inventory

2026-09-23T21:25:33.249283+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | ['6', '7'] | ['/tmp', '/var/tmp', '/mnt/raid5'] | reference_compatible=False |

server1 `/`: 325718700032 available bytes; 81.83% used; 112501436 free inodes.

server1 `/home`: 325718700032 available bytes; 81.83% used; 112501436 free inodes.

server1 `/tmp`: 325718700032 available bytes; 81.83% used; 112501436 free inodes.

server1 `/var/tmp`: 325718700032 available bytes; 81.83% used; 112501436 free inodes.

server1 `/mnt/raid5`: 1367489183744 available bytes; 93.73% used; 337739966 free inodes.
| server2 | True | [] | [] | reference_compatible=False |

server2 `/`: 41126952960 available bytes; 97.71% used; 110432685 free inodes.

server2 `/home`: 41126952960 available bytes; 97.71% used; 110432685 free inodes.

server2 `/tmp`: 41126952960 available bytes; 97.71% used; 110432685 free inodes.

server2 `/var/tmp`: 41126952960 available bytes; 97.71% used; 110432685 free inodes.

server2 `/mnt/raid5`: 538685575168 available bytes; 96.28% used; 445208994 free inodes.
| server3 | True | [] | ['/tmp', '/var/tmp'] | reference_compatible=True |

server3 `/`: 292955500544 available bytes; 83.65% used; 114208562 free inodes.

server3 `/home`: 292955500544 available bytes; 83.65% used; 114208562 free inodes.

server3 `/data`: 52282200064 available bytes; 99.28% used; 225848894 free inodes.

server3 `/tmp`: 292955500544 available bytes; 83.65% used; 114208562 free inodes.

server3 `/var/tmp`: 292955500544 available bytes; 83.65% used; 114208562 free inodes.
| server4 | True | ['2', '3', '5', '6', '7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 106484080640 available bytes; 94.06% used; 114356012 free inodes.

server4 `/home`: 106484080640 available bytes; 94.06% used; 114356012 free inodes.

server4 `/data`: 300365369344 available bytes; 95.85% used; 225451849 free inodes.

server4 `/tmp`: 106484080640 available bytes; 94.06% used; 114356012 free inodes.

server4 `/var/tmp`: 106484080640 available bytes; 94.06% used; 114356012 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
