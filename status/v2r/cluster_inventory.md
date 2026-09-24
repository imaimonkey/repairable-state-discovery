# V2R cluster inventory

2026-09-24T05:19:37.377996+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | ['7'] | ['/tmp', '/var/tmp'] |

server1 `/`: 324571357184 available bytes; 81.89% used; 112492483 free inodes.

server1 `/home`: 324571357184 available bytes; 81.89% used; 112492483 free inodes.

server1 `/tmp`: 324571357184 available bytes; 81.89% used; 112492483 free inodes.

server1 `/var/tmp`: 324571357184 available bytes; 81.89% used; 112492483 free inodes.

server1 `/mnt/raid5`: 505684381696 available bytes; 97.68% used; 337724531 free inodes.
| server2 | True | [] | [] |

server2 `/`: 40745070592 available bytes; 97.73% used; 110430348 free inodes.

server2 `/home`: 40745070592 available bytes; 97.73% used; 110430348 free inodes.

server2 `/tmp`: 40745070592 available bytes; 97.73% used; 110430348 free inodes.

server2 `/var/tmp`: 40745070592 available bytes; 97.73% used; 110430348 free inodes.

server2 `/mnt/raid5`: 522705973248 available bytes; 96.39% used; 445194220 free inodes.
| server3 | True | ['1'] | ['/tmp', '/var/tmp'] |

server3 `/`: 291992592384 available bytes; 83.71% used; 114175930 free inodes.

server3 `/home`: 291992592384 available bytes; 83.71% used; 114175930 free inodes.

server3 `/data`: 21154525184 available bytes; 99.71% used; 225839869 free inodes.

server3 `/tmp`: 291992592384 available bytes; 83.71% used; 114175930 free inodes.

server3 `/var/tmp`: 291992592384 available bytes; 83.71% used; 114175930 free inodes.
| server4 | True | ['7'] | ['/tmp', '/var/tmp'] |

server4 `/`: 105817612288 available bytes; 94.09% used; 114349371 free inodes.

server4 `/home`: 105817612288 available bytes; 94.09% used; 114349371 free inodes.

server4 `/data`: 252566867968 available bytes; 96.51% used; 225366596 free inodes.

server4 `/tmp`: 105817612288 available bytes; 94.09% used; 114349371 free inodes.

server4 `/var/tmp`: 105817612288 available bytes; 94.09% used; 114349371 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
