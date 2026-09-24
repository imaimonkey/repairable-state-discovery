# V2R cluster inventory

2026-09-24T04:59:07.079084+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | ['7'] | ['/tmp', '/var/tmp'] |

server1 `/`: 324617633792 available bytes; 81.89% used; 112492730 free inodes.

server1 `/home`: 324617633792 available bytes; 81.89% used; 112492730 free inodes.

server1 `/tmp`: 324617633792 available bytes; 81.89% used; 112492730 free inodes.

server1 `/var/tmp`: 324617633792 available bytes; 81.89% used; 112492730 free inodes.

server1 `/mnt/raid5`: 479513120768 available bytes; 97.80% used; 337724564 free inodes.
| server2 | True | [] | [] |

server2 `/`: 40760074240 available bytes; 97.73% used; 110430424 free inodes.

server2 `/home`: 40760074240 available bytes; 97.73% used; 110430424 free inodes.

server2 `/tmp`: 40760074240 available bytes; 97.73% used; 110430424 free inodes.

server2 `/var/tmp`: 40760074240 available bytes; 97.73% used; 110430424 free inodes.

server2 `/mnt/raid5`: 523628048384 available bytes; 96.38% used; 445194723 free inodes.
| server3 | True | ['1'] | ['/tmp', '/var/tmp'] |

server3 `/`: 292406132736 available bytes; 83.68% used; 114200288 free inodes.

server3 `/home`: 292406132736 available bytes; 83.68% used; 114200288 free inodes.

server3 `/data`: 23300198400 available bytes; 99.68% used; 225840435 free inodes.

server3 `/tmp`: 292406132736 available bytes; 83.68% used; 114200288 free inodes.

server3 `/var/tmp`: 292406132736 available bytes; 83.68% used; 114200288 free inodes.
| server4 | True | ['7'] | ['/tmp', '/var/tmp'] |

server4 `/`: 105835601920 available bytes; 94.09% used; 114349396 free inodes.

server4 `/home`: 105835601920 available bytes; 94.09% used; 114349396 free inodes.

server4 `/data`: 252706758656 available bytes; 96.51% used; 225366821 free inodes.

server4 `/tmp`: 105835601920 available bytes; 94.09% used; 114349396 free inodes.

server4 `/var/tmp`: 105835601920 available bytes; 94.09% used; 114349396 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
