# V2R cluster inventory

2026-09-24T01:38:28.606118+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | ['4', '6', '7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 325459910656 available bytes; 81.84% used; 112499463 free inodes.

server1 `/home`: 325459910656 available bytes; 81.84% used; 112499463 free inodes.

server1 `/tmp`: 325459910656 available bytes; 81.84% used; 112499463 free inodes.

server1 `/var/tmp`: 325459910656 available bytes; 81.84% used; 112499463 free inodes.

server1 `/mnt/raid5`: 862877573120 available bytes; 96.04% used; 337733927 free inodes.
| server2 | True | [] | [] | reference_compatible=False |

server2 `/`: 40937496576 available bytes; 97.72% used; 110431931 free inodes.

server2 `/home`: 40937496576 available bytes; 97.72% used; 110431931 free inodes.

server2 `/tmp`: 40937496576 available bytes; 97.72% used; 110431931 free inodes.

server2 `/var/tmp`: 40937496576 available bytes; 97.72% used; 110431931 free inodes.

server2 `/mnt/raid5`: 530545655808 available bytes; 96.33% used; 445201235 free inodes.
| server3 | True | [] | ['/tmp', '/var/tmp'] | reference_compatible=True |

server3 `/`: 292723425280 available bytes; 83.66% used; 114211253 free inodes.

server3 `/home`: 292723425280 available bytes; 83.66% used; 114211253 free inodes.

server3 `/data`: 71405674496 available bytes; 99.01% used; 225842096 free inodes.

server3 `/tmp`: 292723425280 available bytes; 83.66% used; 114211253 free inodes.

server3 `/var/tmp`: 292723425280 available bytes; 83.66% used; 114211253 free inodes.
| server4 | True | ['2', '3', '6', '7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 105957285888 available bytes; 94.09% used; 114348671 free inodes.

server4 `/home`: 105957285888 available bytes; 94.09% used; 114348671 free inodes.

server4 `/data`: 290807820288 available bytes; 95.98% used; 225396938 free inodes.

server4 `/tmp`: 105957285888 available bytes; 94.09% used; 114348671 free inodes.

server4 `/var/tmp`: 105957285888 available bytes; 94.09% used; 114348671 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
