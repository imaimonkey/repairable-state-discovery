# V2R cluster inventory

2026-09-24T05:10:39.836738+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | ['7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 324595134464 available bytes; 81.89% used; 112492564 free inodes.

server1 `/home`: 324595134464 available bytes; 81.89% used; 112492564 free inodes.

server1 `/tmp`: 324595134464 available bytes; 81.89% used; 112492564 free inodes.

server1 `/var/tmp`: 324595134464 available bytes; 81.89% used; 112492564 free inodes.

server1 `/mnt/raid5`: 494059204608 available bytes; 97.73% used; 337724551 free inodes.
| server2 | True | [] | [] | reference_compatible=False |

server2 `/`: 40756326400 available bytes; 97.73% used; 110430370 free inodes.

server2 `/home`: 40756326400 available bytes; 97.73% used; 110430370 free inodes.

server2 `/tmp`: 40756326400 available bytes; 97.73% used; 110430370 free inodes.

server2 `/var/tmp`: 40756326400 available bytes; 97.73% used; 110430370 free inodes.

server2 `/mnt/raid5`: 522978918400 available bytes; 96.39% used; 445194513 free inodes.
| server3 | True | ['1'] | ['/tmp', '/var/tmp'] | reference_compatible=True |

server3 `/`: 292144717824 available bytes; 83.70% used; 114191743 free inodes.

server3 `/home`: 292144717824 available bytes; 83.70% used; 114191743 free inodes.

server3 `/data`: 23285047296 available bytes; 99.68% used; 225840240 free inodes.

server3 `/tmp`: 292144717824 available bytes; 83.70% used; 114191743 free inodes.

server3 `/var/tmp`: 292144717824 available bytes; 83.70% used; 114191743 free inodes.
| server4 | True | ['7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 105826463744 available bytes; 94.09% used; 114349379 free inodes.

server4 `/home`: 105826463744 available bytes; 94.09% used; 114349379 free inodes.

server4 `/data`: 252610138112 available bytes; 96.51% used; 225366771 free inodes.

server4 `/tmp`: 105826463744 available bytes; 94.09% used; 114349379 free inodes.

server4 `/var/tmp`: 105826463744 available bytes; 94.09% used; 114349379 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
