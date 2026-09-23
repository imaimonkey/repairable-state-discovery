# V2R cluster inventory

2026-09-23T20:38:20.109051+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | ['4', '7'] | ['/tmp', '/var/tmp', '/mnt/raid5'] |

server1 `/`: 325732548608 available bytes; 81.83% used; 112501740 free inodes.

server1 `/home`: 325732548608 available bytes; 81.83% used; 112501740 free inodes.

server1 `/tmp`: 325732548608 available bytes; 81.83% used; 112501740 free inodes.

server1 `/var/tmp`: 325732548608 available bytes; 81.83% used; 112501740 free inodes.

server1 `/mnt/raid5`: 1388258512896 available bytes; 93.63% used; 337740914 free inodes.
| server2 | True | ['7'] | [] |

server2 `/`: 41137995776 available bytes; 97.71% used; 110432779 free inodes.

server2 `/home`: 41137995776 available bytes; 97.71% used; 110432779 free inodes.

server2 `/tmp`: 41137995776 available bytes; 97.71% used; 110432779 free inodes.

server2 `/var/tmp`: 41137995776 available bytes; 97.71% used; 110432779 free inodes.

server2 `/mnt/raid5`: 540113932288 available bytes; 96.27% used; 445210327 free inodes.
| server3 | True | [] | ['/tmp', '/var/tmp'] |

server3 `/`: 293131616256 available bytes; 83.64% used; 114216733 free inodes.

server3 `/home`: 293131616256 available bytes; 83.64% used; 114216733 free inodes.

server3 `/data`: 52584640512 available bytes; 99.27% used; 225843197 free inodes.

server3 `/tmp`: 293131616256 available bytes; 83.64% used; 114216733 free inodes.

server3 `/var/tmp`: 293131616256 available bytes; 83.64% used; 114216733 free inodes.
| server4 | True | ['1', '2', '3', '5', '6', '7'] | ['/tmp', '/var/tmp'] |

server4 `/`: 106524766208 available bytes; 94.06% used; 114356131 free inodes.

server4 `/home`: 106524766208 available bytes; 94.06% used; 114356131 free inodes.

server4 `/data`: 300719284224 available bytes; 95.84% used; 225461375 free inodes.

server4 `/tmp`: 106524766208 available bytes; 94.06% used; 114356131 free inodes.

server4 `/var/tmp`: 106524766208 available bytes; 94.06% used; 114356131 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
