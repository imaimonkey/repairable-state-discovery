# V2R cluster inventory

2026-09-24T05:35:46.445798+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | ['7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 324534980608 available bytes; 81.90% used; 112492255 free inodes.

server1 `/home`: 324534980608 available bytes; 81.90% used; 112492255 free inodes.

server1 `/tmp`: 324534980608 available bytes; 81.90% used; 112492255 free inodes.

server1 `/var/tmp`: 324534980608 available bytes; 81.90% used; 112492255 free inodes.

server1 `/mnt/raid5`: 517643755520 available bytes; 97.63% used; 337724003 free inodes.
| server2 | True | [] | [] | reference_compatible=False |

server2 `/`: 57915883520 available bytes; 96.77% used; 110431354 free inodes.

server2 `/home`: 57915883520 available bytes; 96.77% used; 110431354 free inodes.

server2 `/tmp`: 57915883520 available bytes; 96.77% used; 110431354 free inodes.

server2 `/var/tmp`: 57915883520 available bytes; 96.77% used; 110431354 free inodes.

server2 `/mnt/raid5`: 522200211456 available bytes; 96.39% used; 445193958 free inodes.
| server3 | True | [] | ['/tmp', '/var/tmp'] | reference_compatible=True |

server3 `/`: 127211196416 available bytes; 92.90% used; 114200242 free inodes.

server3 `/home`: 127211196416 available bytes; 92.90% used; 114200242 free inodes.

server3 `/data`: 185260908544 available bytes; 97.44% used; 225839299 free inodes.

server3 `/tmp`: 127211196416 available bytes; 92.90% used; 114200242 free inodes.

server3 `/var/tmp`: 127211196416 available bytes; 92.90% used; 114200242 free inodes.
| server4 | True | ['7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 105816813568 available bytes; 94.10% used; 114349365 free inodes.

server4 `/home`: 105816813568 available bytes; 94.10% used; 114349365 free inodes.

server4 `/data`: 251510075392 available bytes; 96.52% used; 225358078 free inodes.

server4 `/tmp`: 105816813568 available bytes; 94.10% used; 114349365 free inodes.

server4 `/var/tmp`: 105816813568 available bytes; 94.10% used; 114349365 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
