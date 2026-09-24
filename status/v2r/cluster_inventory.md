# V2R cluster inventory

2026-09-24T05:49:25.398121+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | ['7'] | ['/tmp', '/var/tmp'] |

server1 `/`: 324528078848 available bytes; 81.90% used; 112492046 free inodes.

server1 `/home`: 324528078848 available bytes; 81.90% used; 112492046 free inodes.

server1 `/tmp`: 324528078848 available bytes; 81.90% used; 112492046 free inodes.

server1 `/var/tmp`: 324528078848 available bytes; 81.90% used; 112492046 free inodes.

server1 `/mnt/raid5`: 517615112192 available bytes; 97.63% used; 337723903 free inodes.
| server2 | True | [] | [] |

server2 `/`: 57906163712 available bytes; 96.77% used; 110431322 free inodes.

server2 `/home`: 57906163712 available bytes; 96.77% used; 110431322 free inodes.

server2 `/tmp`: 57906163712 available bytes; 96.77% used; 110431322 free inodes.

server2 `/var/tmp`: 57906163712 available bytes; 96.77% used; 110431322 free inodes.

server2 `/mnt/raid5`: 521791893504 available bytes; 96.39% used; 445193535 free inodes.
| server3 | True | [] | ['/tmp', '/var/tmp'] |

server3 `/`: 126807015424 available bytes; 92.92% used; 114175497 free inodes.

server3 `/home`: 126807015424 available bytes; 92.92% used; 114175497 free inodes.

server3 `/data`: 185220050944 available bytes; 97.44% used; 225838642 free inodes.

server3 `/tmp`: 126807015424 available bytes; 92.92% used; 114175497 free inodes.

server3 `/var/tmp`: 126807015424 available bytes; 92.92% used; 114175497 free inodes.
| server4 | True | ['7'] | ['/tmp', '/var/tmp'] |

server4 `/`: 105816018944 available bytes; 94.10% used; 114349347 free inodes.

server4 `/home`: 105816018944 available bytes; 94.10% used; 114349347 free inodes.

server4 `/data`: 251480080384 available bytes; 96.52% used; 225357942 free inodes.

server4 `/tmp`: 105816018944 available bytes; 94.10% used; 114349347 free inodes.

server4 `/var/tmp`: 105816018944 available bytes; 94.10% used; 114349347 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
