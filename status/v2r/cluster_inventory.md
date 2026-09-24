# V2R cluster inventory

2026-09-24T13:56:04.730865+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | [] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 324066594816 available bytes; 81.92% used; 112481664 free inodes.

server1 `/home`: 324066594816 available bytes; 81.92% used; 112481664 free inodes.

server1 `/tmp`: 324066594816 available bytes; 81.92% used; 112481664 free inodes.

server1 `/var/tmp`: 324066594816 available bytes; 81.92% used; 112481664 free inodes.

server1 `/mnt/raid5`: 396325261312 available bytes; 98.18% used; 337672186 free inodes.
| server2 | True | ['7'] | [] | reference_compatible=False |

server2 `/`: 57500016640 available bytes; 96.79% used; 110428451 free inodes.

server2 `/home`: 57500016640 available bytes; 96.79% used; 110428451 free inodes.

server2 `/tmp`: 57500016640 available bytes; 96.79% used; 110428451 free inodes.

server2 `/var/tmp`: 57500016640 available bytes; 96.79% used; 110428451 free inodes.

server2 `/mnt/raid5`: 505825165312 available bytes; 96.50% used; 445168786 free inodes.
| server3 | True | [] | [] | reference_compatible=True |

server3 `/`: 85074591744 available bytes; 95.25% used; 114188112 free inodes.

server3 `/home`: 85074591744 available bytes; 95.25% used; 114188112 free inodes.

server3 `/data`: 161071271936 available bytes; 97.77% used; 225802660 free inodes.

server3 `/tmp`: 85074591744 available bytes; 95.25% used; 114188112 free inodes.

server3 `/var/tmp`: 85074591744 available bytes; 95.25% used; 114188112 free inodes.
| server4 | True | [] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 105760305152 available bytes; 94.10% used; 114348716 free inodes.

server4 `/home`: 105760305152 available bytes; 94.10% used; 114348716 free inodes.

server4 `/data`: 90037170176 available bytes; 98.76% used; 225257168 free inodes.

server4 `/tmp`: 105760305152 available bytes; 94.10% used; 114348716 free inodes.

server4 `/var/tmp`: 105760305152 available bytes; 94.10% used; 114348716 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
