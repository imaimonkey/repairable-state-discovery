# V2R cluster inventory

2026-09-24T12:17:38.413999+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | [] | ['/tmp', '/var/tmp'] |

server1 `/`: 324057366528 available bytes; 81.92% used; 112481566 free inodes.

server1 `/home`: 324057366528 available bytes; 81.92% used; 112481566 free inodes.

server1 `/tmp`: 324057366528 available bytes; 81.92% used; 112481566 free inodes.

server1 `/var/tmp`: 324057366528 available bytes; 81.92% used; 112481566 free inodes.

server1 `/mnt/raid5`: 405220798464 available bytes; 98.14% used; 337683850 free inodes.
| server2 | True | ['7'] | [] |

server2 `/`: 57614315520 available bytes; 96.79% used; 110429524 free inodes.

server2 `/home`: 57614315520 available bytes; 96.79% used; 110429524 free inodes.

server2 `/tmp`: 57614315520 available bytes; 96.79% used; 110429524 free inodes.

server2 `/var/tmp`: 57614315520 available bytes; 96.79% used; 110429524 free inodes.

server2 `/mnt/raid5`: 508890902528 available bytes; 96.48% used; 445172264 free inodes.
| server3 | True | [] | [] |

server3 `/`: 85316476928 available bytes; 95.24% used; 114172781 free inodes.

server3 `/home`: 85316476928 available bytes; 95.24% used; 114172781 free inodes.

server3 `/data`: 163457114112 available bytes; 97.74% used; 225814988 free inodes.

server3 `/tmp`: 85316476928 available bytes; 95.24% used; 114172781 free inodes.

server3 `/var/tmp`: 85316476928 available bytes; 95.24% used; 114172781 free inodes.
| server4 | True | [] | ['/tmp', '/var/tmp'] |

server4 `/`: 105781190656 available bytes; 94.10% used; 114348812 free inodes.

server4 `/home`: 105781190656 available bytes; 94.10% used; 114348812 free inodes.

server4 `/data`: 90076659712 available bytes; 98.76% used; 225257316 free inodes.

server4 `/tmp`: 105781190656 available bytes; 94.10% used; 114348812 free inodes.

server4 `/var/tmp`: 105781190656 available bytes; 94.10% used; 114348812 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
