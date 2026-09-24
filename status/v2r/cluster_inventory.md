# V2R cluster inventory

2026-09-24T04:46:31.234021+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | ['7'] | ['/tmp', '/var/tmp'] |

server1 `/`: 324624035840 available bytes; 81.89% used; 112492829 free inodes.

server1 `/home`: 324624035840 available bytes; 81.89% used; 112492829 free inodes.

server1 `/tmp`: 324624035840 available bytes; 81.89% used; 112492829 free inodes.

server1 `/var/tmp`: 324624035840 available bytes; 81.89% used; 112492829 free inodes.

server1 `/mnt/raid5`: 464988839936 available bytes; 97.87% used; 337724624 free inodes.
| server2 | True | [] | [] |

server2 `/`: 40769363968 available bytes; 97.73% used; 110430470 free inodes.

server2 `/home`: 40769363968 available bytes; 97.73% used; 110430470 free inodes.

server2 `/tmp`: 40769363968 available bytes; 97.73% used; 110430470 free inodes.

server2 `/var/tmp`: 40769363968 available bytes; 97.73% used; 110430470 free inodes.

server2 `/mnt/raid5`: 524288864256 available bytes; 96.38% used; 445195408 free inodes.
| server3 | True | ['1'] | ['/tmp', '/var/tmp'] |

server3 `/`: 292400889856 available bytes; 83.68% used; 114200242 free inodes.

server3 `/home`: 292400889856 available bytes; 83.68% used; 114200242 free inodes.

server3 `/data`: 24359723008 available bytes; 99.66% used; 225840643 free inodes.

server3 `/tmp`: 292400889856 available bytes; 83.68% used; 114200242 free inodes.

server3 `/var/tmp`: 292400889856 available bytes; 83.68% used; 114200242 free inodes.
| server4 | True | ['7'] | ['/tmp', '/var/tmp'] |

server4 `/`: 105836142592 available bytes; 94.09% used; 114349396 free inodes.

server4 `/home`: 105836142592 available bytes; 94.09% used; 114349396 free inodes.

server4 `/data`: 253377552384 available bytes; 96.50% used; 225366841 free inodes.

server4 `/tmp`: 105836142592 available bytes; 94.09% used; 114349396 free inodes.

server4 `/var/tmp`: 105836142592 available bytes; 94.09% used; 114349396 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
