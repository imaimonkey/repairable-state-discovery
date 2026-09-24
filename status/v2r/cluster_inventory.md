# V2R cluster inventory

2026-09-24T05:04:18.796532+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | ['7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 324609654784 available bytes; 81.89% used; 112492652 free inodes.

server1 `/home`: 324609654784 available bytes; 81.89% used; 112492652 free inodes.

server1 `/tmp`: 324609654784 available bytes; 81.89% used; 112492652 free inodes.

server1 `/var/tmp`: 324609654784 available bytes; 81.89% used; 112492652 free inodes.

server1 `/mnt/raid5`: 484371398656 available bytes; 97.78% used; 337724567 free inodes.
| server2 | True | [] | [] | reference_compatible=False |

server2 `/`: 40759070720 available bytes; 97.73% used; 110430398 free inodes.

server2 `/home`: 40759070720 available bytes; 97.73% used; 110430398 free inodes.

server2 `/tmp`: 40759070720 available bytes; 97.73% used; 110430398 free inodes.

server2 `/var/tmp`: 40759070720 available bytes; 97.73% used; 110430398 free inodes.

server2 `/mnt/raid5`: 522917732352 available bytes; 96.39% used; 445194726 free inodes.
| server3 | True | ['1'] | ['/tmp', '/var/tmp'] | reference_compatible=True |

server3 `/`: 291602268160 available bytes; 83.73% used; 114152013 free inodes.

server3 `/home`: 291602268160 available bytes; 83.73% used; 114152013 free inodes.

server3 `/data`: 23290384384 available bytes; 99.68% used; 225840360 free inodes.

server3 `/tmp`: 291602268160 available bytes; 83.73% used; 114152013 free inodes.

server3 `/var/tmp`: 291602268160 available bytes; 83.73% used; 114152013 free inodes.
| server4 | True | ['7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 105826791424 available bytes; 94.09% used; 114349383 free inodes.

server4 `/home`: 105826791424 available bytes; 94.09% used; 114349383 free inodes.

server4 `/data`: 252698132480 available bytes; 96.51% used; 225366792 free inodes.

server4 `/tmp`: 105826791424 available bytes; 94.09% used; 114349383 free inodes.

server4 `/var/tmp`: 105826791424 available bytes; 94.09% used; 114349383 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
