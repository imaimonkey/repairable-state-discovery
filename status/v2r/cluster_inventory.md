# V2R cluster inventory

2026-09-24T21:20:34.769389+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | [] | ['/tmp', '/var/tmp'] |

server1 `/`: 323961532416 available bytes; 81.93% used; 112481402 free inodes.

server1 `/home`: 323961532416 available bytes; 81.93% used; 112481402 free inodes.

server1 `/tmp`: 323961532416 available bytes; 81.93% used; 112481402 free inodes.

server1 `/var/tmp`: 323961532416 available bytes; 81.93% used; 112481402 free inodes.

server1 `/mnt/raid5`: 415521775616 available bytes; 98.09% used; 337628573 free inodes.
| server2 | True | [] | [] |

server2 `/`: 30136946688 available bytes; 98.32% used; 110411348 free inodes.

server2 `/home`: 30136946688 available bytes; 98.32% used; 110411348 free inodes.

server2 `/tmp`: 30136946688 available bytes; 98.32% used; 110411348 free inodes.

server2 `/var/tmp`: 30136946688 available bytes; 98.32% used; 110411348 free inodes.

server2 `/mnt/raid5`: 490710593536 available bytes; 96.61% used; 445155319 free inodes.
| server3 | True | [] | [] |

server3 `/`: 84383072256 available bytes; 95.29% used; 114156095 free inodes.

server3 `/home`: 84383072256 available bytes; 95.29% used; 114156095 free inodes.

server3 `/data`: 150463397888 available bytes; 97.92% used; 225803355 free inodes.

server3 `/tmp`: 84383072256 available bytes; 95.29% used; 114156095 free inodes.

server3 `/var/tmp`: 84383072256 available bytes; 95.29% used; 114156095 free inodes.
| server4 | True | [] | ['/tmp', '/var/tmp'] |

server4 `/`: 105632378880 available bytes; 94.11% used; 114348349 free inodes.

server4 `/home`: 105632378880 available bytes; 94.11% used; 114348349 free inodes.

server4 `/data`: 64563998720 available bytes; 99.11% used; 225253257 free inodes.

server4 `/tmp`: 105632378880 available bytes; 94.11% used; 114348349 free inodes.

server4 `/var/tmp`: 105632378880 available bytes; 94.11% used; 114348349 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
