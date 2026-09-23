# V2R cluster inventory

2026-09-23T20:06:04.304126+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | ['3', '4', '7'] | ['/tmp', '/var/tmp', '/mnt/raid5'] | reference_compatible=False |

server1 `/`: 325738774528 available bytes; 81.83% used; 112501847 free inodes.

server1 `/home`: 325738774528 available bytes; 81.83% used; 112501847 free inodes.

server1 `/tmp`: 325738774528 available bytes; 81.83% used; 112501847 free inodes.

server1 `/var/tmp`: 325738774528 available bytes; 81.83% used; 112501847 free inodes.

server1 `/mnt/raid5`: 1388970115072 available bytes; 93.63% used; 337741143 free inodes.
| server2 | True | ['6', '7'] | [] | reference_compatible=False |

server2 `/`: 41270800384 available bytes; 97.70% used; 110434885 free inodes.

server2 `/home`: 41270800384 available bytes; 97.70% used; 110434885 free inodes.

server2 `/tmp`: 41270800384 available bytes; 97.70% used; 110434885 free inodes.

server2 `/var/tmp`: 41270800384 available bytes; 97.70% used; 110434885 free inodes.

server2 `/mnt/raid5`: 541634674688 available bytes; 96.26% used; 445211488 free inodes.
| server3 | True | [] | ['/tmp', '/var/tmp'] | reference_compatible=True |

server3 `/`: 293389246464 available bytes; 83.63% used; 114225790 free inodes.

server3 `/home`: 293389246464 available bytes; 83.63% used; 114225790 free inodes.

server3 `/data`: 52700368896 available bytes; 99.27% used; 225844521 free inodes.

server3 `/tmp`: 293389246464 available bytes; 83.63% used; 114225790 free inodes.

server3 `/var/tmp`: 293389246464 available bytes; 83.63% used; 114225790 free inodes.
| server4 | True | ['0', '1', '2', '3', '4', '5', '6', '7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 106528829440 available bytes; 94.06% used; 114356234 free inodes.

server4 `/home`: 106528829440 available bytes; 94.06% used; 114356234 free inodes.

server4 `/data`: 4247552 available bytes; 100.00% used; 225457630 free inodes.

server4 `/tmp`: 106528829440 available bytes; 94.06% used; 114356234 free inodes.

server4 `/var/tmp`: 106528829440 available bytes; 94.06% used; 114356234 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
