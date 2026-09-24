# V2R cluster inventory

2026-09-24T22:48:19.760402+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | [] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 323933315072 available bytes; 81.93% used; 112481415 free inodes.

server1 `/home`: 323933315072 available bytes; 81.93% used; 112481415 free inodes.

server1 `/tmp`: 323933315072 available bytes; 81.93% used; 112481415 free inodes.

server1 `/var/tmp`: 323933315072 available bytes; 81.93% used; 112481415 free inodes.

server1 `/mnt/raid5`: 415333568512 available bytes; 98.09% used; 337618168 free inodes.
| server2 | True | [] | [] | reference_compatible=False |

server2 `/`: 23159951360 available bytes; 98.71% used; 110410910 free inodes.

server2 `/home`: 23159951360 available bytes; 98.71% used; 110410910 free inodes.

server2 `/tmp`: 23159951360 available bytes; 98.71% used; 110410910 free inodes.

server2 `/var/tmp`: 23159951360 available bytes; 98.71% used; 110410910 free inodes.

server2 `/mnt/raid5`: 487985819648 available bytes; 96.63% used; 445152635 free inodes.
| server3 | True | [] | [] | reference_compatible=True |

server3 `/`: 84372316160 available bytes; 95.29% used; 114156075 free inodes.

server3 `/home`: 84372316160 available bytes; 95.29% used; 114156075 free inodes.

server3 `/data`: 148973944832 available bytes; 97.94% used; 225801729 free inodes.

server3 `/tmp`: 84372316160 available bytes; 95.29% used; 114156075 free inodes.

server3 `/var/tmp`: 84372316160 available bytes; 95.29% used; 114156075 free inodes.
| server4 | True | ['0', '7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 105801162752 available bytes; 94.10% used; 114348320 free inodes.

server4 `/home`: 105801162752 available bytes; 94.10% used; 114348320 free inodes.

server4 `/data`: 62820708352 available bytes; 99.13% used; 225206728 free inodes.

server4 `/tmp`: 105801162752 available bytes; 94.10% used; 114348320 free inodes.

server4 `/var/tmp`: 105801162752 available bytes; 94.10% used; 114348320 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
