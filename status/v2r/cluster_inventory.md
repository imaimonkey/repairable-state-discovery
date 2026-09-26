# V2R cluster inventory

2026-09-26T20:21:21.537185+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | ['0', '3', '4', '5', '6', '7'] | ['/tmp', '/var/tmp'] |

server1 `/`: 315483537408 available bytes; 82.40% used; 112444700 free inodes.

server1 `/home`: 315483537408 available bytes; 82.40% used; 112444700 free inodes.

server1 `/tmp`: 315483537408 available bytes; 82.40% used; 112444700 free inodes.

server1 `/var/tmp`: 315483537408 available bytes; 82.40% used; 112444700 free inodes.

server1 `/mnt/raid5`: 645854941184 available bytes; 97.04% used; 337467117 free inodes.
| server2 | True | ['2', '7'] | [] |

server2 `/`: 17983262720 available bytes; 99.00% used; 110367105 free inodes.

server2 `/home`: 17983262720 available bytes; 99.00% used; 110367105 free inodes.

server2 `/tmp`: 17983262720 available bytes; 99.00% used; 110367105 free inodes.

server2 `/var/tmp`: 17983262720 available bytes; 99.00% used; 110367105 free inodes.

server2 `/mnt/raid5`: 600941772800 available bytes; 95.85% used; 444964901 free inodes.
| server3 | True | [] | [] |

server3 `/`: 81262522368 available bytes; 95.47% used; 114065302 free inodes.

server3 `/home`: 81262522368 available bytes; 95.47% used; 114065302 free inodes.

server3 `/data`: 1348627525632 available bytes; 81.36% used; 225832130 free inodes.

server3 `/tmp`: 81262522368 available bytes; 95.47% used; 114065302 free inodes.

server3 `/var/tmp`: 81262522368 available bytes; 95.47% used; 114065302 free inodes.
| server4 | True | [] | ['/tmp', '/var/tmp'] |

server4 `/`: 105919242240 available bytes; 94.09% used; 114347833 free inodes.

server4 `/home`: 105919242240 available bytes; 94.09% used; 114347833 free inodes.

server4 `/data`: 410206744576 available bytes; 94.33% used; 224823722 free inodes.

server4 `/tmp`: 105919242240 available bytes; 94.09% used; 114347833 free inodes.

server4 `/var/tmp`: 105919242240 available bytes; 94.09% used; 114347833 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
