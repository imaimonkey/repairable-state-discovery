# V2R cluster inventory

2026-09-23T20:36:48.500243+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | ['4', '7'] | ['/tmp', '/var/tmp', '/mnt/raid5'] |

server1 `/`: 325733302272 available bytes; 81.83% used; 112501761 free inodes.

server1 `/home`: 325733302272 available bytes; 81.83% used; 112501761 free inodes.

server1 `/tmp`: 325733302272 available bytes; 81.83% used; 112501761 free inodes.

server1 `/var/tmp`: 325733302272 available bytes; 81.83% used; 112501761 free inodes.

server1 `/mnt/raid5`: 1367612870656 available bytes; 93.73% used; 337740918 free inodes.
| server2 | True | ['7'] | [] |

server2 `/`: 41138728960 available bytes; 97.71% used; 110432794 free inodes.

server2 `/home`: 41138728960 available bytes; 97.71% used; 110432794 free inodes.

server2 `/tmp`: 41138728960 available bytes; 97.71% used; 110432794 free inodes.

server2 `/var/tmp`: 41138728960 available bytes; 97.71% used; 110432794 free inodes.

server2 `/mnt/raid5`: 539611361280 available bytes; 96.27% used; 445210267 free inodes.
| server3 | True | [] | ['/tmp', '/var/tmp'] |

server3 `/`: 292914319360 available bytes; 83.65% used; 114207418 free inodes.

server3 `/home`: 292914319360 available bytes; 83.65% used; 114207418 free inodes.

server3 `/data`: 52584386560 available bytes; 99.27% used; 225843230 free inodes.

server3 `/tmp`: 292914319360 available bytes; 83.65% used; 114207418 free inodes.

server3 `/var/tmp`: 292914319360 available bytes; 83.65% used; 114207418 free inodes.
| server4 | True | ['0', '1', '2', '3', '5', '6', '7'] | ['/tmp', '/var/tmp'] |

server4 `/`: 106524565504 available bytes; 94.06% used; 114356142 free inodes.

server4 `/home`: 106524565504 available bytes; 94.06% used; 114356142 free inodes.

server4 `/data`: 300723421184 available bytes; 95.84% used; 225461442 free inodes.

server4 `/tmp`: 106524565504 available bytes; 94.06% used; 114356142 free inodes.

server4 `/var/tmp`: 106524565504 available bytes; 94.06% used; 114356142 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
