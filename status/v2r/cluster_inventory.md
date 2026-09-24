# V2R cluster inventory

2026-09-24T05:05:24.769577+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | ['7'] | ['/tmp', '/var/tmp'] |

server1 `/`: 324608454656 available bytes; 81.89% used; 112492648 free inodes.

server1 `/home`: 324608454656 available bytes; 81.89% used; 112492648 free inodes.

server1 `/tmp`: 324608454656 available bytes; 81.89% used; 112492648 free inodes.

server1 `/var/tmp`: 324608454656 available bytes; 81.89% used; 112492648 free inodes.

server1 `/mnt/raid5`: 489213100032 available bytes; 97.76% used; 337724561 free inodes.
| server2 | True | [] | [] |

server2 `/`: 40758927360 available bytes; 97.73% used; 110430398 free inodes.

server2 `/home`: 40758927360 available bytes; 97.73% used; 110430398 free inodes.

server2 `/tmp`: 40758927360 available bytes; 97.73% used; 110430398 free inodes.

server2 `/var/tmp`: 40758927360 available bytes; 97.73% used; 110430398 free inodes.

server2 `/mnt/raid5`: 522891440128 available bytes; 96.39% used; 445194789 free inodes.
| server3 | True | ['1'] | ['/tmp', '/var/tmp'] |

server3 `/`: 291604230144 available bytes; 83.73% used; 114152015 free inodes.

server3 `/home`: 291604230144 available bytes; 83.73% used; 114152015 free inodes.

server3 `/data`: 23288508416 available bytes; 99.68% used; 225840341 free inodes.

server3 `/tmp`: 291604230144 available bytes; 83.73% used; 114152015 free inodes.

server3 `/var/tmp`: 291604230144 available bytes; 83.73% used; 114152015 free inodes.
| server4 | True | ['7'] | ['/tmp', '/var/tmp'] |

server4 `/`: 105826754560 available bytes; 94.09% used; 114349383 free inodes.

server4 `/home`: 105826754560 available bytes; 94.09% used; 114349383 free inodes.

server4 `/data`: 252697141248 available bytes; 96.51% used; 225366792 free inodes.

server4 `/tmp`: 105826754560 available bytes; 94.09% used; 114349383 free inodes.

server4 `/var/tmp`: 105826754560 available bytes; 94.09% used; 114349383 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
