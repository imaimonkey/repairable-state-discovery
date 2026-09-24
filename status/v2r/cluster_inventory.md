# V2R cluster inventory

2026-09-24T08:09:40.345770+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | ['7'] | ['/tmp', '/var/tmp'] |

server1 `/`: 324409294848 available bytes; 81.90% used; 112490676 free inodes.

server1 `/home`: 324409294848 available bytes; 81.90% used; 112490676 free inodes.

server1 `/tmp`: 324409294848 available bytes; 81.90% used; 112490676 free inodes.

server1 `/var/tmp`: 324409294848 available bytes; 81.90% used; 112490676 free inodes.

server1 `/mnt/raid5`: 496661880832 available bytes; 97.72% used; 337721387 free inodes.
| server2 | True | [] | [] |

server2 `/`: 57818300416 available bytes; 96.77% used; 110431050 free inodes.

server2 `/home`: 57818300416 available bytes; 96.77% used; 110431050 free inodes.

server2 `/tmp`: 57818300416 available bytes; 96.77% used; 110431050 free inodes.

server2 `/var/tmp`: 57818300416 available bytes; 96.77% used; 110431050 free inodes.

server2 `/mnt/raid5`: 517059624960 available bytes; 96.43% used; 445180250 free inodes.
| server3 | True | [] | [] |

server3 `/`: 85483769856 available bytes; 95.23% used; 114175168 free inodes.

server3 `/home`: 85483769856 available bytes; 95.23% used; 114175168 free inodes.

server3 `/data`: 177681260544 available bytes; 97.54% used; 225838285 free inodes.

server3 `/tmp`: 85483769856 available bytes; 95.23% used; 114175168 free inodes.

server3 `/var/tmp`: 85483769856 available bytes; 95.23% used; 114175168 free inodes.
| server4 | True | [] | ['/tmp', '/var/tmp'] |

server4 `/`: 105778814976 available bytes; 94.10% used; 114349157 free inodes.

server4 `/home`: 105778814976 available bytes; 94.10% used; 114349157 free inodes.

server4 `/data`: 284224860160 available bytes; 96.07% used; 225365829 free inodes.

server4 `/tmp`: 105778814976 available bytes; 94.10% used; 114349157 free inodes.

server4 `/var/tmp`: 105778814976 available bytes; 94.10% used; 114349157 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
