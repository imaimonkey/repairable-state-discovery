# V2R cluster inventory

2026-09-24T06:03:35.500509+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | ['7'] | ['/tmp', '/var/tmp'] |

server1 `/`: 324528910336 available bytes; 81.90% used; 112491923 free inodes.

server1 `/home`: 324528910336 available bytes; 81.90% used; 112491923 free inodes.

server1 `/tmp`: 324528910336 available bytes; 81.90% used; 112491923 free inodes.

server1 `/var/tmp`: 324528910336 available bytes; 81.90% used; 112491923 free inodes.

server1 `/mnt/raid5`: 517611573248 available bytes; 97.63% used; 337723833 free inodes.
| server2 | True | [] | [] |

server2 `/`: 57898700800 available bytes; 96.77% used; 110431288 free inodes.

server2 `/home`: 57898700800 available bytes; 96.77% used; 110431288 free inodes.

server2 `/tmp`: 57898700800 available bytes; 96.77% used; 110431288 free inodes.

server2 `/var/tmp`: 57898700800 available bytes; 96.77% used; 110431288 free inodes.

server2 `/mnt/raid5`: 520516255744 available bytes; 96.40% used; 445192700 free inodes.
| server3 | True | [] | ['/tmp', '/var/tmp'] |

server3 `/`: 127187369984 available bytes; 92.90% used; 114200060 free inodes.

server3 `/home`: 127187369984 available bytes; 92.90% used; 114200060 free inodes.

server3 `/data`: 185840996352 available bytes; 97.43% used; 225838416 free inodes.

server3 `/tmp`: 127187369984 available bytes; 92.90% used; 114200060 free inodes.

server3 `/var/tmp`: 127187369984 available bytes; 92.90% used; 114200060 free inodes.
| server4 | True | ['1'] | ['/tmp', '/var/tmp'] |

server4 `/`: 105815277568 available bytes; 94.10% used; 114349323 free inodes.

server4 `/home`: 105815277568 available bytes; 94.10% used; 114349323 free inodes.

server4 `/data`: 339814744064 available bytes; 95.30% used; 225374523 free inodes.

server4 `/tmp`: 105815277568 available bytes; 94.10% used; 114349323 free inodes.

server4 `/var/tmp`: 105815277568 available bytes; 94.10% used; 114349323 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
