# V2R cluster inventory

2026-09-23T21:25:51.690853+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | ['6', '7'] | ['/tmp', '/var/tmp', '/mnt/raid5'] |

server1 `/`: 325718704128 available bytes; 81.83% used; 112501436 free inodes.

server1 `/home`: 325718704128 available bytes; 81.83% used; 112501436 free inodes.

server1 `/tmp`: 325718704128 available bytes; 81.83% used; 112501436 free inodes.

server1 `/var/tmp`: 325718704128 available bytes; 81.83% used; 112501436 free inodes.

server1 `/mnt/raid5`: 1367489179648 available bytes; 93.73% used; 337739966 free inodes.
| server2 | True | [] | [] |

server2 `/`: 41126641664 available bytes; 97.71% used; 110432683 free inodes.

server2 `/home`: 41126641664 available bytes; 97.71% used; 110432683 free inodes.

server2 `/tmp`: 41126641664 available bytes; 97.71% used; 110432683 free inodes.

server2 `/var/tmp`: 41126641664 available bytes; 97.71% used; 110432683 free inodes.

server2 `/mnt/raid5`: 538667421696 available bytes; 96.28% used; 445208972 free inodes.
| server3 | True | [] | ['/tmp', '/var/tmp'] |

server3 `/`: 292955492352 available bytes; 83.65% used; 114208562 free inodes.

server3 `/home`: 292955492352 available bytes; 83.65% used; 114208562 free inodes.

server3 `/data`: 52281454592 available bytes; 99.28% used; 225848873 free inodes.

server3 `/tmp`: 292955492352 available bytes; 83.65% used; 114208562 free inodes.

server3 `/var/tmp`: 292955492352 available bytes; 83.65% used; 114208562 free inodes.
| server4 | True | ['2', '3', '5', '6', '7'] | ['/tmp', '/var/tmp'] |

server4 `/`: 106483773440 available bytes; 94.06% used; 114356011 free inodes.

server4 `/home`: 106483773440 available bytes; 94.06% used; 114356011 free inodes.

server4 `/data`: 300362665984 available bytes; 95.85% used; 225451790 free inodes.

server4 `/tmp`: 106483773440 available bytes; 94.06% used; 114356011 free inodes.

server4 `/var/tmp`: 106483773440 available bytes; 94.06% used; 114356011 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
