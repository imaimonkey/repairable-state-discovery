# V2R cluster inventory

2026-09-27T05:45:26.381513+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | ['2', '3', '4', '5', '6', '7'] | ['/tmp', '/var/tmp'] |

server1 `/`: 314498838528 available bytes; 82.46% used; 112440829 free inodes.

server1 `/home`: 314498838528 available bytes; 82.46% used; 112440829 free inodes.

server1 `/tmp`: 314498838528 available bytes; 82.46% used; 112440829 free inodes.

server1 `/var/tmp`: 314498838528 available bytes; 82.46% used; 112440829 free inodes.

server1 `/mnt/raid5`: 634733408256 available bytes; 97.09% used; 337400015 free inodes.
| server2 | True | [] | [] |

server2 `/`: 17630257152 available bytes; 99.02% used; 110365006 free inodes.

server2 `/home`: 17630257152 available bytes; 99.02% used; 110365006 free inodes.

server2 `/tmp`: 17630257152 available bytes; 99.02% used; 110365006 free inodes.

server2 `/var/tmp`: 17630257152 available bytes; 99.02% used; 110365006 free inodes.

server2 `/mnt/raid5`: 574381948928 available bytes; 96.03% used; 444877162 free inodes.
| server3 | True | [] | [] |

server3 `/`: 78576939008 available bytes; 95.62% used; 114062907 free inodes.

server3 `/home`: 78576939008 available bytes; 95.62% used; 114062907 free inodes.

server3 `/data`: 1333325115392 available bytes; 81.57% used; 225766072 free inodes.

server3 `/tmp`: 78576939008 available bytes; 95.62% used; 114062907 free inodes.

server3 `/var/tmp`: 78576939008 available bytes; 95.62% used; 114062907 free inodes.
| server4 | True | [] | ['/tmp', '/var/tmp'] |

server4 `/`: 110999277568 available bytes; 93.81% used; 114372897 free inodes.

server4 `/home`: 110999277568 available bytes; 93.81% used; 114372897 free inodes.

server4 `/data`: 374549557248 available bytes; 94.82% used; 224771226 free inodes.

server4 `/tmp`: 110999277568 available bytes; 93.81% used; 114372897 free inodes.

server4 `/var/tmp`: 110999277568 available bytes; 93.81% used; 114372897 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
