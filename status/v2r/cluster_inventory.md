# V2R cluster inventory

2026-09-24T14:05:23.054028+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | [] | ['/tmp', '/var/tmp'] |

server1 `/`: 324061958144 available bytes; 81.92% used; 112481656 free inodes.

server1 `/home`: 324061958144 available bytes; 81.92% used; 112481656 free inodes.

server1 `/tmp`: 324061958144 available bytes; 81.92% used; 112481656 free inodes.

server1 `/var/tmp`: 324061958144 available bytes; 81.92% used; 112481656 free inodes.

server1 `/mnt/raid5`: 416952524800 available bytes; 98.09% used; 337671091 free inodes.
| server2 | True | ['7'] | [] |

server2 `/`: 57484709888 available bytes; 96.79% used; 110428359 free inodes.

server2 `/home`: 57484709888 available bytes; 96.79% used; 110428359 free inodes.

server2 `/tmp`: 57484709888 available bytes; 96.79% used; 110428359 free inodes.

server2 `/var/tmp`: 57484709888 available bytes; 96.79% used; 110428359 free inodes.

server2 `/mnt/raid5`: 505541652480 available bytes; 96.51% used; 445169087 free inodes.
| server3 | True | [] | [] |

server3 `/`: 85086584832 available bytes; 95.25% used; 114190405 free inodes.

server3 `/home`: 85086584832 available bytes; 95.25% used; 114190405 free inodes.

server3 `/data`: 161001787392 available bytes; 97.77% used; 225802499 free inodes.

server3 `/tmp`: 85086584832 available bytes; 95.25% used; 114190405 free inodes.

server3 `/var/tmp`: 85086584832 available bytes; 95.25% used; 114190405 free inodes.
| server4 | True | [] | ['/tmp', '/var/tmp'] |

server4 `/`: 105759895552 available bytes; 94.10% used; 114348708 free inodes.

server4 `/home`: 105759895552 available bytes; 94.10% used; 114348708 free inodes.

server4 `/data`: 69386145792 available bytes; 99.04% used; 225257118 free inodes.

server4 `/tmp`: 105759895552 available bytes; 94.10% used; 114348708 free inodes.

server4 `/var/tmp`: 105759895552 available bytes; 94.10% used; 114348708 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
