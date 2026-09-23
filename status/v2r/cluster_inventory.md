# V2R cluster inventory

2026-09-23T19:51:41.263392+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | ['4', '7'] | ['/tmp', '/var/tmp', '/mnt/raid5'] | reference_compatible=False |

server1 `/`: 325748682752 available bytes; 81.83% used; 112501851 free inodes.

server1 `/home`: 325748682752 available bytes; 81.83% used; 112501851 free inodes.

server1 `/tmp`: 325748682752 available bytes; 81.83% used; 112501851 free inodes.

server1 `/var/tmp`: 325748682752 available bytes; 81.83% used; 112501851 free inodes.

server1 `/mnt/raid5`: 1384989974528 available bytes; 93.65% used; 337741273 free inodes.
| server2 | True | ['6', '7'] | [] | reference_compatible=False |

server2 `/`: 41316405248 available bytes; 97.70% used; 110435432 free inodes.

server2 `/home`: 41316405248 available bytes; 97.70% used; 110435432 free inodes.

server2 `/tmp`: 41316405248 available bytes; 97.70% used; 110435432 free inodes.

server2 `/var/tmp`: 41316405248 available bytes; 97.70% used; 110435432 free inodes.

server2 `/mnt/raid5`: 542069735424 available bytes; 96.25% used; 445211752 free inodes.
| server3 | True | [] | ['/tmp', '/var/tmp'] | reference_compatible=True |

server3 `/`: 293701349376 available bytes; 83.61% used; 114247582 free inodes.

server3 `/home`: 293701349376 available bytes; 83.61% used; 114247582 free inodes.

server3 `/data`: 52712497152 available bytes; 99.27% used; 225844789 free inodes.

server3 `/tmp`: 293701349376 available bytes; 83.61% used; 114247582 free inodes.

server3 `/var/tmp`: 293701349376 available bytes; 83.61% used; 114247582 free inodes.
| server4 | True | ['0', '1', '2', '3', '4', '5', '6', '7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 106528645120 available bytes; 94.06% used; 114356235 free inodes.

server4 `/home`: 106528645120 available bytes; 94.06% used; 114356235 free inodes.

server4 `/data`: 4067328 available bytes; 100.00% used; 225457640 free inodes.

server4 `/tmp`: 106528645120 available bytes; 94.06% used; 114356235 free inodes.

server4 `/var/tmp`: 106528645120 available bytes; 94.06% used; 114356235 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
