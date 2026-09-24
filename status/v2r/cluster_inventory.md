# V2R cluster inventory

2026-09-24T05:18:28.557789+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | ['7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 324590723072 available bytes; 81.89% used; 112492492 free inodes.

server1 `/home`: 324590723072 available bytes; 81.89% used; 112492492 free inodes.

server1 `/tmp`: 324590723072 available bytes; 81.89% used; 112492492 free inodes.

server1 `/var/tmp`: 324590723072 available bytes; 81.89% used; 112492492 free inodes.

server1 `/mnt/raid5`: 504918773760 available bytes; 97.68% used; 337724547 free inodes.
| server2 | True | [] | [] | reference_compatible=False |

server2 `/`: 40745709568 available bytes; 97.73% used; 110430352 free inodes.

server2 `/home`: 40745709568 available bytes; 97.73% used; 110430352 free inodes.

server2 `/tmp`: 40745709568 available bytes; 97.73% used; 110430352 free inodes.

server2 `/var/tmp`: 40745709568 available bytes; 97.73% used; 110430352 free inodes.

server2 `/mnt/raid5`: 522744283136 available bytes; 96.39% used; 445194276 free inodes.
| server3 | True | ['1'] | ['/tmp', '/var/tmp'] | reference_compatible=True |

server3 `/`: 291992956928 available bytes; 83.71% used; 114175930 free inodes.

server3 `/home`: 291992956928 available bytes; 83.71% used; 114175930 free inodes.

server3 `/data`: 21156855808 available bytes; 99.71% used; 225839893 free inodes.

server3 `/tmp`: 291992956928 available bytes; 83.71% used; 114175930 free inodes.

server3 `/var/tmp`: 291992956928 available bytes; 83.71% used; 114175930 free inodes.
| server4 | True | ['7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 105817767936 available bytes; 94.09% used; 114349379 free inodes.

server4 `/home`: 105817767936 available bytes; 94.09% used; 114349379 free inodes.

server4 `/data`: 252566020096 available bytes; 96.51% used; 225366597 free inodes.

server4 `/tmp`: 105817767936 available bytes; 94.09% used; 114349379 free inodes.

server4 `/var/tmp`: 105817767936 available bytes; 94.09% used; 114349379 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
