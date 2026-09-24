# V2R cluster inventory

2026-09-24T21:34:37.853465+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | [] | ['/tmp', '/var/tmp'] |

server1 `/`: 323955732480 available bytes; 81.93% used; 112481418 free inodes.

server1 `/home`: 323955732480 available bytes; 81.93% used; 112481418 free inodes.

server1 `/tmp`: 323955732480 available bytes; 81.93% used; 112481418 free inodes.

server1 `/var/tmp`: 323955732480 available bytes; 81.93% used; 112481418 free inodes.

server1 `/mnt/raid5`: 415490527232 available bytes; 98.09% used; 337626937 free inodes.
| server2 | True | [] | [] |

server2 `/`: 30138875904 available bytes; 98.32% used; 110411326 free inodes.

server2 `/home`: 30138875904 available bytes; 98.32% used; 110411326 free inodes.

server2 `/tmp`: 30138875904 available bytes; 98.32% used; 110411326 free inodes.

server2 `/var/tmp`: 30138875904 available bytes; 98.32% used; 110411326 free inodes.

server2 `/mnt/raid5`: 489725820928 available bytes; 96.62% used; 445155106 free inodes.
| server3 | True | [] | [] |

server3 `/`: 84386762752 available bytes; 95.29% used; 114156093 free inodes.

server3 `/home`: 84386762752 available bytes; 95.29% used; 114156093 free inodes.

server3 `/data`: 150222491648 available bytes; 97.92% used; 225803109 free inodes.

server3 `/tmp`: 84386762752 available bytes; 95.29% used; 114156093 free inodes.

server3 `/var/tmp`: 84386762752 available bytes; 95.29% used; 114156093 free inodes.
| server4 | True | ['1', '4', '5'] | ['/tmp', '/var/tmp'] |

server4 `/`: 105630044160 available bytes; 94.11% used; 114348350 free inodes.

server4 `/home`: 105630044160 available bytes; 94.11% used; 114348350 free inodes.

server4 `/data`: 82893295616 available bytes; 98.85% used; 225252543 free inodes.

server4 `/tmp`: 105630044160 available bytes; 94.11% used; 114348350 free inodes.

server4 `/var/tmp`: 105630044160 available bytes; 94.11% used; 114348350 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
