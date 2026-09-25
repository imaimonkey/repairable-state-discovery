# V2R cluster inventory

2026-09-25T04:10:25.786226+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | [] | ['/tmp', '/var/tmp'] |

server1 `/`: 318931116032 available bytes; 82.21% used; 112480381 free inodes.

server1 `/home`: 318931116032 available bytes; 82.21% used; 112480381 free inodes.

server1 `/tmp`: 318931116032 available bytes; 82.21% used; 112480381 free inodes.

server1 `/var/tmp`: 318931116032 available bytes; 82.21% used; 112480381 free inodes.

server1 `/mnt/raid5`: 379664748544 available bytes; 98.26% used; 337594085 free inodes.
| server2 | True | [] | [] |

server2 `/`: 22965690368 available bytes; 98.72% used; 110410444 free inodes.

server2 `/home`: 22965690368 available bytes; 98.72% used; 110410444 free inodes.

server2 `/tmp`: 22965690368 available bytes; 98.72% used; 110410444 free inodes.

server2 `/var/tmp`: 22965690368 available bytes; 98.72% used; 110410444 free inodes.

server2 `/mnt/raid5`: 463645810688 available bytes; 96.80% used; 445110550 free inodes.
| server3 | True | [] | [] |

server3 `/`: 84341092352 available bytes; 95.29% used; 114156072 free inodes.

server3 `/home`: 84341092352 available bytes; 95.29% used; 114156072 free inodes.

server3 `/data`: 143919935488 available bytes; 98.01% used; 225816549 free inodes.

server3 `/tmp`: 84341092352 available bytes; 95.29% used; 114156072 free inodes.

server3 `/var/tmp`: 84341092352 available bytes; 95.29% used; 114156072 free inodes.
| server4 | True | ['6', '7'] | ['/tmp', '/var/tmp'] |

server4 `/`: 105674166272 available bytes; 94.10% used; 114350879 free inodes.

server4 `/home`: 105674166272 available bytes; 94.10% used; 114350879 free inodes.

server4 `/data`: 33698799616 available bytes; 99.53% used; 224964009 free inodes.

server4 `/tmp`: 105674166272 available bytes; 94.10% used; 114350879 free inodes.

server4 `/var/tmp`: 105674166272 available bytes; 94.10% used; 114350879 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
