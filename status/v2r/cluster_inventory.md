# V2R cluster inventory

2026-09-24T16:29:59.942497+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | ['7'] | ['/tmp', '/var/tmp'] |

server1 `/`: 324023529472 available bytes; 81.92% used; 112481448 free inodes.

server1 `/home`: 324023529472 available bytes; 81.92% used; 112481448 free inodes.

server1 `/tmp`: 324023529472 available bytes; 81.92% used; 112481448 free inodes.

server1 `/var/tmp`: 324023529472 available bytes; 81.92% used; 112481448 free inodes.

server1 `/mnt/raid5`: 416571244544 available bytes; 98.09% used; 337653393 free inodes.
| server2 | True | ['7'] | [] |

server2 `/`: 57326759936 available bytes; 96.80% used; 110426887 free inodes.

server2 `/home`: 57326759936 available bytes; 96.80% used; 110426887 free inodes.

server2 `/tmp`: 57326759936 available bytes; 96.80% used; 110426887 free inodes.

server2 `/var/tmp`: 57326759936 available bytes; 96.80% used; 110426887 free inodes.

server2 `/mnt/raid5`: 500975685632 available bytes; 96.54% used; 445164691 free inodes.
| server3 | True | [] | [] |

server3 `/`: 84704444416 available bytes; 95.27% used; 114179290 free inodes.

server3 `/home`: 84704444416 available bytes; 95.27% used; 114179290 free inodes.

server3 `/data`: 159355990016 available bytes; 97.80% used; 225788043 free inodes.

server3 `/tmp`: 84704444416 available bytes; 95.27% used; 114179290 free inodes.

server3 `/var/tmp`: 84704444416 available bytes; 95.27% used; 114179290 free inodes.
| server4 | True | [] | ['/tmp', '/var/tmp'] |

server4 `/`: 105688727552 available bytes; 94.10% used; 114348602 free inodes.

server4 `/home`: 105688727552 available bytes; 94.10% used; 114348602 free inodes.

server4 `/data`: 89281789952 available bytes; 98.77% used; 225255848 free inodes.

server4 `/tmp`: 105688727552 available bytes; 94.10% used; 114348602 free inodes.

server4 `/var/tmp`: 105688727552 available bytes; 94.10% used; 114348602 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
