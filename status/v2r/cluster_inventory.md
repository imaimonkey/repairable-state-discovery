# V2R cluster inventory

2026-09-24T20:34:08.147188+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | [] | ['/tmp', '/var/tmp'] |

server1 `/`: 323982315520 available bytes; 81.93% used; 112481433 free inodes.

server1 `/home`: 323982315520 available bytes; 81.93% used; 112481433 free inodes.

server1 `/tmp`: 323982315520 available bytes; 81.93% used; 112481433 free inodes.

server1 `/var/tmp`: 323982315520 available bytes; 81.93% used; 112481433 free inodes.

server1 `/mnt/raid5`: 415614132224 available bytes; 98.09% used; 337633982 free inodes.
| server2 | True | ['7'] | [] |

server2 `/`: 30152802304 available bytes; 98.32% used; 110411376 free inodes.

server2 `/home`: 30152802304 available bytes; 98.32% used; 110411376 free inodes.

server2 `/tmp`: 30152802304 available bytes; 98.32% used; 110411376 free inodes.

server2 `/var/tmp`: 30152802304 available bytes; 98.32% used; 110411376 free inodes.

server2 `/mnt/raid5`: 492153626624 available bytes; 96.60% used; 445156972 free inodes.
| server3 | True | [] | [] |

server3 `/`: 84396838912 available bytes; 95.29% used; 114156106 free inodes.

server3 `/home`: 84396838912 available bytes; 95.29% used; 114156106 free inodes.

server3 `/data`: 151401668608 available bytes; 97.91% used; 225804308 free inodes.

server3 `/tmp`: 84396838912 available bytes; 95.29% used; 114156106 free inodes.

server3 `/var/tmp`: 84396838912 available bytes; 95.29% used; 114156106 free inodes.
| server4 | True | [] | ['/tmp', '/var/tmp'] |

server4 `/`: 105640071168 available bytes; 94.10% used; 114348380 free inodes.

server4 `/home`: 105640071168 available bytes; 94.10% used; 114348380 free inodes.

server4 `/data`: 85460312064 available bytes; 98.82% used; 225257647 free inodes.

server4 `/tmp`: 105640071168 available bytes; 94.10% used; 114348380 free inodes.

server4 `/var/tmp`: 105640071168 available bytes; 94.10% used; 114348380 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
