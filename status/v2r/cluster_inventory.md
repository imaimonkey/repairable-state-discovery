# V2R cluster inventory

2026-09-24T05:12:13.138081+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | ['7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 324593639424 available bytes; 81.89% used; 112492554 free inodes.

server1 `/home`: 324593639424 available bytes; 81.89% used; 112492554 free inodes.

server1 `/tmp`: 324593639424 available bytes; 81.89% used; 112492554 free inodes.

server1 `/var/tmp`: 324593639424 available bytes; 81.89% used; 112492554 free inodes.

server1 `/mnt/raid5`: 495969656832 available bytes; 97.72% used; 337724548 free inodes.
| server2 | True | [] | [] | reference_compatible=False |

server2 `/`: 40749330432 available bytes; 97.73% used; 110430366 free inodes.

server2 `/home`: 40749330432 available bytes; 97.73% used; 110430366 free inodes.

server2 `/tmp`: 40749330432 available bytes; 97.73% used; 110430366 free inodes.

server2 `/var/tmp`: 40749330432 available bytes; 97.73% used; 110430366 free inodes.

server2 `/mnt/raid5`: 522926141440 available bytes; 96.39% used; 445194355 free inodes.
| server3 | True | ['1'] | ['/tmp', '/var/tmp'] | reference_compatible=True |

server3 `/`: 291991769088 available bytes; 83.71% used; 114176018 free inodes.

server3 `/home`: 291991769088 available bytes; 83.71% used; 114176018 free inodes.

server3 `/data`: 23283437568 available bytes; 99.68% used; 225840221 free inodes.

server3 `/tmp`: 291991769088 available bytes; 83.71% used; 114176018 free inodes.

server3 `/var/tmp`: 291991769088 available bytes; 83.71% used; 114176018 free inodes.
| server4 | True | ['7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 105826402304 available bytes; 94.09% used; 114349379 free inodes.

server4 `/home`: 105826402304 available bytes; 94.09% used; 114349379 free inodes.

server4 `/data`: 252608602112 available bytes; 96.51% used; 225366777 free inodes.

server4 `/tmp`: 105826402304 available bytes; 94.09% used; 114349379 free inodes.

server4 `/var/tmp`: 105826402304 available bytes; 94.09% used; 114349379 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
