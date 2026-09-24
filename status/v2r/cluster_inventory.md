# V2R cluster inventory

2026-09-24T12:09:52.981777+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | [] | ['/tmp', '/var/tmp'] |

server1 `/`: 322685038592 available bytes; 82.00% used; 112464406 free inodes.

server1 `/home`: 322685038592 available bytes; 82.00% used; 112464406 free inodes.

server1 `/tmp`: 322685038592 available bytes; 82.00% used; 112464406 free inodes.

server1 `/var/tmp`: 322685038592 available bytes; 82.00% used; 112464406 free inodes.

server1 `/mnt/raid5`: 405247086592 available bytes; 98.14% used; 337684762 free inodes.
| server2 | True | ['7'] | [] |

server2 `/`: 57622433792 available bytes; 96.79% used; 110429608 free inodes.

server2 `/home`: 57622433792 available bytes; 96.79% used; 110429608 free inodes.

server2 `/tmp`: 57622433792 available bytes; 96.79% used; 110429608 free inodes.

server2 `/var/tmp`: 57622433792 available bytes; 96.79% used; 110429608 free inodes.

server2 `/mnt/raid5`: 509120827392 available bytes; 96.48% used; 445172490 free inodes.
| server3 | True | [] | [] |

server3 `/`: 85493829632 available bytes; 95.23% used; 114189333 free inodes.

server3 `/home`: 85493829632 available bytes; 95.23% used; 114189333 free inodes.

server3 `/data`: 163528577024 available bytes; 97.74% used; 225815513 free inodes.

server3 `/tmp`: 85493829632 available bytes; 95.23% used; 114189333 free inodes.

server3 `/var/tmp`: 85493829632 available bytes; 95.23% used; 114189333 free inodes.
| server4 | True | [] | ['/tmp', '/var/tmp'] |

server4 `/`: 105781493760 available bytes; 94.10% used; 114348814 free inodes.

server4 `/home`: 105781493760 available bytes; 94.10% used; 114348814 free inodes.

server4 `/data`: 90428743680 available bytes; 98.75% used; 225257318 free inodes.

server4 `/tmp`: 105781493760 available bytes; 94.10% used; 114348814 free inodes.

server4 `/var/tmp`: 105781493760 available bytes; 94.10% used; 114348814 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
