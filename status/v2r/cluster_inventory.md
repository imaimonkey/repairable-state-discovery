# V2R cluster inventory

2026-09-24T20:23:23.182863+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | [] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 323980292096 available bytes; 81.93% used; 112481434 free inodes.

server1 `/home`: 323980292096 available bytes; 81.93% used; 112481434 free inodes.

server1 `/tmp`: 323980292096 available bytes; 81.93% used; 112481434 free inodes.

server1 `/var/tmp`: 323980292096 available bytes; 81.93% used; 112481434 free inodes.

server1 `/mnt/raid5`: 415654379520 available bytes; 98.09% used; 337635230 free inodes.
| server2 | True | ['3', '7'] | [] | reference_compatible=False |

server2 `/`: 30160867328 available bytes; 98.32% used; 110411380 free inodes.

server2 `/home`: 30160867328 available bytes; 98.32% used; 110411380 free inodes.

server2 `/tmp`: 30160867328 available bytes; 98.32% used; 110411380 free inodes.

server2 `/var/tmp`: 30160867328 available bytes; 98.32% used; 110411380 free inodes.

server2 `/mnt/raid5`: 492476694528 available bytes; 96.60% used; 445156882 free inodes.
| server3 | True | [] | [] | reference_compatible=True |

server3 `/`: 84392132608 available bytes; 95.29% used; 114156111 free inodes.

server3 `/home`: 84392132608 available bytes; 95.29% used; 114156111 free inodes.

server3 `/data`: 151581667328 available bytes; 97.91% used; 225804562 free inodes.

server3 `/tmp`: 84392132608 available bytes; 95.29% used; 114156111 free inodes.

server3 `/var/tmp`: 84392132608 available bytes; 95.29% used; 114156111 free inodes.
| server4 | True | [] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 105640640512 available bytes; 94.10% used; 114348392 free inodes.

server4 `/home`: 105640640512 available bytes; 94.10% used; 114348392 free inodes.

server4 `/data`: 85512503296 available bytes; 98.82% used; 225258329 free inodes.

server4 `/tmp`: 105640640512 available bytes; 94.10% used; 114348392 free inodes.

server4 `/var/tmp`: 105640640512 available bytes; 94.10% used; 114348392 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
