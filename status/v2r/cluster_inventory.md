# V2R cluster inventory

2026-09-23T22:44:26.222179+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | ['6', '7'] | ['/tmp', '/var/tmp', '/mnt/raid5'] |

server1 `/`: 325746507776 available bytes; 81.83% used; 112501729 free inodes.

server1 `/home`: 325746507776 available bytes; 81.83% used; 112501729 free inodes.

server1 `/tmp`: 325746507776 available bytes; 81.83% used; 112501729 free inodes.

server1 `/var/tmp`: 325746507776 available bytes; 81.83% used; 112501729 free inodes.

server1 `/mnt/raid5`: 1388116750336 available bytes; 93.63% used; 337739963 free inodes.
| server2 | True | [] | [] |

server2 `/`: 41073688576 available bytes; 97.71% used; 110432623 free inodes.

server2 `/home`: 41073688576 available bytes; 97.71% used; 110432623 free inodes.

server2 `/tmp`: 41073688576 available bytes; 97.71% used; 110432623 free inodes.

server2 `/var/tmp`: 41073688576 available bytes; 97.71% used; 110432623 free inodes.

server2 `/mnt/raid5`: 536238415872 available bytes; 96.29% used; 445206398 free inodes.
| server3 | True | ['3'] | ['/tmp', '/var/tmp'] |

server3 `/`: 292718964736 available bytes; 83.67% used; 114209285 free inodes.

server3 `/home`: 292718964736 available bytes; 83.67% used; 114209285 free inodes.

server3 `/data`: 82448920576 available bytes; 98.86% used; 225847220 free inodes.

server3 `/tmp`: 292718964736 available bytes; 83.67% used; 114209285 free inodes.

server3 `/var/tmp`: 292718964736 available bytes; 83.67% used; 114209285 free inodes.
| server4 | True | ['3', '6', '7'] | ['/tmp', '/var/tmp'] |

server4 `/`: 106332200960 available bytes; 94.07% used; 114354011 free inodes.

server4 `/home`: 106332200960 available bytes; 94.07% used; 114354011 free inodes.

server4 `/data`: 300115398656 available bytes; 95.85% used; 225435035 free inodes.

server4 `/tmp`: 106332200960 available bytes; 94.07% used; 114354011 free inodes.

server4 `/var/tmp`: 106332200960 available bytes; 94.07% used; 114354011 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
