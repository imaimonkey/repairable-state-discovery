# V2R cluster inventory

2026-09-24T07:12:02.899357+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | ['5', '7'] | ['/tmp', '/var/tmp'] |

server1 `/`: 324456988672 available bytes; 81.90% used; 112491252 free inodes.

server1 `/home`: 324456988672 available bytes; 81.90% used; 112491252 free inodes.

server1 `/tmp`: 324456988672 available bytes; 81.90% used; 112491252 free inodes.

server1 `/var/tmp`: 324456988672 available bytes; 81.90% used; 112491252 free inodes.

server1 `/mnt/raid5`: 517427040256 available bytes; 97.63% used; 337722824 free inodes.
| server2 | True | [] | [] |

server2 `/`: 57855303680 available bytes; 96.77% used; 110431147 free inodes.

server2 `/home`: 57855303680 available bytes; 96.77% used; 110431147 free inodes.

server2 `/tmp`: 57855303680 available bytes; 96.77% used; 110431147 free inodes.

server2 `/var/tmp`: 57855303680 available bytes; 96.77% used; 110431147 free inodes.

server2 `/mnt/raid5`: 518831620096 available bytes; 96.42% used; 445181545 free inodes.
| server3 | True | [] | ['/tmp', '/var/tmp'] |

server3 `/`: 127195426816 available bytes; 92.90% used; 114200105 free inodes.

server3 `/home`: 127195426816 available bytes; 92.90% used; 114200105 free inodes.

server3 `/data`: 139110772736 available bytes; 98.08% used; 225834507 free inodes.

server3 `/tmp`: 127195426816 available bytes; 92.90% used; 114200105 free inodes.

server3 `/var/tmp`: 127195426816 available bytes; 92.90% used; 114200105 free inodes.
| server4 | True | [] | ['/tmp', '/var/tmp'] |

server4 `/`: 105789984768 available bytes; 94.10% used; 114349211 free inodes.

server4 `/home`: 105789984768 available bytes; 94.10% used; 114349211 free inodes.

server4 `/data`: 295567912960 available bytes; 95.92% used; 225367346 free inodes.

server4 `/tmp`: 105789984768 available bytes; 94.10% used; 114349211 free inodes.

server4 `/var/tmp`: 105789984768 available bytes; 94.10% used; 114349211 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
