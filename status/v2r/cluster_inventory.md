# V2R cluster inventory

2026-09-24T13:49:49.080618+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | [] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 324066451456 available bytes; 81.92% used; 112481662 free inodes.

server1 `/home`: 324066451456 available bytes; 81.92% used; 112481662 free inodes.

server1 `/tmp`: 324066451456 available bytes; 81.92% used; 112481662 free inodes.

server1 `/var/tmp`: 324066451456 available bytes; 81.92% used; 112481662 free inodes.

server1 `/mnt/raid5`: 416984068096 available bytes; 98.09% used; 337672905 free inodes.
| server2 | True | ['7'] | [] | reference_compatible=False |

server2 `/`: 57504972800 available bytes; 96.79% used; 110428517 free inodes.

server2 `/home`: 57504972800 available bytes; 96.79% used; 110428517 free inodes.

server2 `/tmp`: 57504972800 available bytes; 96.79% used; 110428517 free inodes.

server2 `/var/tmp`: 57504972800 available bytes; 96.79% used; 110428517 free inodes.

server2 `/mnt/raid5`: 506031624192 available bytes; 96.50% used; 445169315 free inodes.
| server3 | True | [] | [] | reference_compatible=True |

server3 `/`: 85098909696 available bytes; 95.25% used; 114190490 free inodes.

server3 `/home`: 85098909696 available bytes; 95.25% used; 114190490 free inodes.

server3 `/data`: 161116155904 available bytes; 97.77% used; 225802785 free inodes.

server3 `/tmp`: 85098909696 available bytes; 95.25% used; 114190490 free inodes.

server3 `/var/tmp`: 85098909696 available bytes; 95.25% used; 114190490 free inodes.
| server4 | True | [] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 105760534528 available bytes; 94.10% used; 114348718 free inodes.

server4 `/home`: 105760534528 available bytes; 94.10% used; 114348718 free inodes.

server4 `/data`: 90038841344 available bytes; 98.76% used; 225257168 free inodes.

server4 `/tmp`: 105760534528 available bytes; 94.10% used; 114348718 free inodes.

server4 `/var/tmp`: 105760534528 available bytes; 94.10% used; 114348718 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
