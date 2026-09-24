# V2R cluster inventory

2026-09-24T17:39:55.941384+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | ['7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 324005126144 available bytes; 81.92% used; 112481432 free inodes.

server1 `/home`: 324005126144 available bytes; 81.92% used; 112481432 free inodes.

server1 `/tmp`: 324005126144 available bytes; 81.92% used; 112481432 free inodes.

server1 `/var/tmp`: 324005126144 available bytes; 81.92% used; 112481432 free inodes.

server1 `/mnt/raid5`: 416429436928 available bytes; 98.09% used; 337645235 free inodes.
| server2 | True | ['7'] | [] | reference_compatible=False |

server2 `/`: 56913534976 available bytes; 96.82% used; 110412422 free inodes.

server2 `/home`: 56913534976 available bytes; 96.82% used; 110412422 free inodes.

server2 `/tmp`: 56913534976 available bytes; 96.82% used; 110412422 free inodes.

server2 `/var/tmp`: 56913534976 available bytes; 96.82% used; 110412422 free inodes.

server2 `/mnt/raid5`: 498488889344 available bytes; 96.56% used; 445162144 free inodes.
| server3 | True | [] | [] | reference_compatible=True |

server3 `/`: 84408532992 available bytes; 95.29% used; 114156150 free inodes.

server3 `/home`: 84408532992 available bytes; 95.29% used; 114156150 free inodes.

server3 `/data`: 158860824576 available bytes; 97.80% used; 225786665 free inodes.

server3 `/tmp`: 84408532992 available bytes; 95.29% used; 114156150 free inodes.

server3 `/var/tmp`: 84408532992 available bytes; 95.29% used; 114156150 free inodes.
| server4 | True | [] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 105672744960 available bytes; 94.10% used; 114348559 free inodes.

server4 `/home`: 105672744960 available bytes; 94.10% used; 114348559 free inodes.

server4 `/data`: 89059512320 available bytes; 98.77% used; 225253764 free inodes.

server4 `/tmp`: 105672744960 available bytes; 94.10% used; 114348559 free inodes.

server4 `/var/tmp`: 105672744960 available bytes; 94.10% used; 114348559 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
