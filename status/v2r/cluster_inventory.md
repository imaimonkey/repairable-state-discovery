# V2R cluster inventory

2026-09-27T05:31:42.985432+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | ['0', '2', '3', '4', '5', '6', '7'] | ['/tmp', '/var/tmp'] |

server1 `/`: 314496155648 available bytes; 82.46% used; 112440824 free inodes.

server1 `/home`: 314496155648 available bytes; 82.46% used; 112440824 free inodes.

server1 `/tmp`: 314496155648 available bytes; 82.46% used; 112440824 free inodes.

server1 `/var/tmp`: 314496155648 available bytes; 82.46% used; 112440824 free inodes.

server1 `/mnt/raid5`: 634736988160 available bytes; 97.09% used; 337400011 free inodes.
| server2 | True | [] | [] |

server2 `/`: 17619976192 available bytes; 99.02% used; 110364998 free inodes.

server2 `/home`: 17619976192 available bytes; 99.02% used; 110364998 free inodes.

server2 `/tmp`: 17619976192 available bytes; 99.02% used; 110364998 free inodes.

server2 `/var/tmp`: 17619976192 available bytes; 99.02% used; 110364998 free inodes.

server2 `/mnt/raid5`: 575036526592 available bytes; 96.03% used; 444877405 free inodes.
| server3 | True | [] | [] |

server3 `/`: 78575583232 available bytes; 95.62% used; 114062913 free inodes.

server3 `/home`: 78575583232 available bytes; 95.62% used; 114062913 free inodes.

server3 `/data`: 1333009600512 available bytes; 81.58% used; 225766300 free inodes.

server3 `/tmp`: 78575583232 available bytes; 95.62% used; 114062913 free inodes.

server3 `/var/tmp`: 78575583232 available bytes; 95.62% used; 114062913 free inodes.
| server4 | True | [] | ['/tmp', '/var/tmp'] |

server4 `/`: 110999629824 available bytes; 93.81% used; 114372900 free inodes.

server4 `/home`: 110999629824 available bytes; 93.81% used; 114372900 free inodes.

server4 `/data`: 374585077760 available bytes; 94.82% used; 224771223 free inodes.

server4 `/tmp`: 110999629824 available bytes; 93.81% used; 114372900 free inodes.

server4 `/var/tmp`: 110999629824 available bytes; 93.81% used; 114372900 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
