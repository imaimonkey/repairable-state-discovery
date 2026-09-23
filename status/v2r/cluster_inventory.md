# V2R cluster inventory

2026-09-23T21:56:42.127254+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | ['6', '7'] | ['/tmp', '/var/tmp', '/mnt/raid5'] |

server1 `/`: 325711122432 available bytes; 81.83% used; 112501407 free inodes.

server1 `/home`: 325711122432 available bytes; 81.83% used; 112501407 free inodes.

server1 `/tmp`: 325711122432 available bytes; 81.83% used; 112501407 free inodes.

server1 `/var/tmp`: 325711122432 available bytes; 81.83% used; 112501407 free inodes.

server1 `/mnt/raid5`: 1388117311488 available bytes; 93.63% used; 337739902 free inodes.
| server2 | True | [] | [] |

server2 `/`: 41104965632 available bytes; 97.71% used; 110432648 free inodes.

server2 `/home`: 41104965632 available bytes; 97.71% used; 110432648 free inodes.

server2 `/tmp`: 41104965632 available bytes; 97.71% used; 110432648 free inodes.

server2 `/var/tmp`: 41104965632 available bytes; 97.71% used; 110432648 free inodes.

server2 `/mnt/raid5`: 537704288256 available bytes; 96.28% used; 445207681 free inodes.
| server3 | True | [] | ['/tmp', '/var/tmp'] |

server3 `/`: 293043740672 available bytes; 83.65% used; 114223447 free inodes.

server3 `/home`: 293043740672 available bytes; 83.65% used; 114223447 free inodes.

server3 `/data`: 82459291648 available bytes; 98.86% used; 225847941 free inodes.

server3 `/tmp`: 293043740672 available bytes; 83.65% used; 114223447 free inodes.

server3 `/var/tmp`: 293043740672 available bytes; 83.65% used; 114223447 free inodes.
| server4 | True | ['3', '5', '6', '7'] | ['/tmp', '/var/tmp'] |

server4 `/`: 106454265856 available bytes; 94.06% used; 114355696 free inodes.

server4 `/home`: 106454265856 available bytes; 94.06% used; 114355696 free inodes.

server4 `/data`: 300216266752 available bytes; 95.85% used; 225445771 free inodes.

server4 `/tmp`: 106454265856 available bytes; 94.06% used; 114355696 free inodes.

server4 `/var/tmp`: 106454265856 available bytes; 94.06% used; 114355696 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
