# V2R cluster inventory

2026-09-24T05:16:26.665948+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | ['7'] | ['/tmp', '/var/tmp'] |

server1 `/`: 324595154944 available bytes; 81.89% used; 112492524 free inodes.

server1 `/home`: 324595154944 available bytes; 81.89% used; 112492524 free inodes.

server1 `/tmp`: 324595154944 available bytes; 81.89% used; 112492524 free inodes.

server1 `/var/tmp`: 324595154944 available bytes; 81.89% used; 112492524 free inodes.

server1 `/mnt/raid5`: 500785258496 available bytes; 97.70% used; 337724533 free inodes.
| server2 | True | [] | [] |

server2 `/`: 40746385408 available bytes; 97.73% used; 110430360 free inodes.

server2 `/home`: 40746385408 available bytes; 97.73% used; 110430360 free inodes.

server2 `/tmp`: 40746385408 available bytes; 97.73% used; 110430360 free inodes.

server2 `/var/tmp`: 40746385408 available bytes; 97.73% used; 110430360 free inodes.

server2 `/mnt/raid5`: 522793984000 available bytes; 96.39% used; 445194126 free inodes.
| server3 | True | ['1'] | ['/tmp', '/var/tmp'] |

server3 `/`: 291964465152 available bytes; 83.71% used; 114174992 free inodes.

server3 `/home`: 291964465152 available bytes; 83.71% used; 114174992 free inodes.

server3 `/data`: 21157310464 available bytes; 99.71% used; 225839944 free inodes.

server3 `/tmp`: 291964465152 available bytes; 83.71% used; 114174992 free inodes.

server3 `/var/tmp`: 291964465152 available bytes; 83.71% used; 114174992 free inodes.
| server4 | True | ['7'] | ['/tmp', '/var/tmp'] |

server4 `/`: 105817841664 available bytes; 94.09% used; 114349379 free inodes.

server4 `/home`: 105817841664 available bytes; 94.09% used; 114349379 free inodes.

server4 `/data`: 252597792768 available bytes; 96.51% used; 225366782 free inodes.

server4 `/tmp`: 105817841664 available bytes; 94.09% used; 114349379 free inodes.

server4 `/var/tmp`: 105817841664 available bytes; 94.09% used; 114349379 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
