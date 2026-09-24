# V2R cluster inventory

2026-09-24T04:54:48.456576+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | ['7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 324620144640 available bytes; 81.89% used; 112492763 free inodes.

server1 `/home`: 324620144640 available bytes; 81.89% used; 112492763 free inodes.

server1 `/tmp`: 324620144640 available bytes; 81.89% used; 112492763 free inodes.

server1 `/var/tmp`: 324620144640 available bytes; 81.89% used; 112492763 free inodes.

server1 `/mnt/raid5`: 474673725440 available bytes; 97.82% used; 337724577 free inodes.
| server2 | True | [] | [] | reference_compatible=False |

server2 `/`: 40760950784 available bytes; 97.73% used; 110430438 free inodes.

server2 `/home`: 40760950784 available bytes; 97.73% used; 110430438 free inodes.

server2 `/tmp`: 40760950784 available bytes; 97.73% used; 110430438 free inodes.

server2 `/var/tmp`: 40760950784 available bytes; 97.73% used; 110430438 free inodes.

server2 `/mnt/raid5`: 523761561600 available bytes; 96.38% used; 445195008 free inodes.
| server3 | True | ['1'] | ['/tmp', '/var/tmp'] | reference_compatible=True |

server3 `/`: 292389617664 available bytes; 83.68% used; 114199964 free inodes.

server3 `/home`: 292389617664 available bytes; 83.68% used; 114199964 free inodes.

server3 `/data`: 23312179200 available bytes; 99.68% used; 225840519 free inodes.

server3 `/tmp`: 292389617664 available bytes; 83.68% used; 114199964 free inodes.

server3 `/var/tmp`: 292389617664 available bytes; 83.68% used; 114199964 free inodes.
| server4 | True | ['7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 105835778048 available bytes; 94.09% used; 114349396 free inodes.

server4 `/home`: 105835778048 available bytes; 94.09% used; 114349396 free inodes.

server4 `/data`: 252713476096 available bytes; 96.51% used; 225366847 free inodes.

server4 `/tmp`: 105835778048 available bytes; 94.09% used; 114349396 free inodes.

server4 `/var/tmp`: 105835778048 available bytes; 94.09% used; 114349396 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
