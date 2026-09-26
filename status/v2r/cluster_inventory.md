# V2R cluster inventory

2026-09-26T20:15:15.513273+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | ['0', '3', '4', '5', '6', '7'] | ['/tmp', '/var/tmp'] |

server1 `/`: 315539845120 available bytes; 82.40% used; 112445142 free inodes.

server1 `/home`: 315539845120 available bytes; 82.40% used; 112445142 free inodes.

server1 `/tmp`: 315539845120 available bytes; 82.40% used; 112445142 free inodes.

server1 `/var/tmp`: 315539845120 available bytes; 82.40% used; 112445142 free inodes.

server1 `/mnt/raid5`: 645854314496 available bytes; 97.04% used; 337467119 free inodes.
| server2 | True | ['2', '7'] | [] |

server2 `/`: 18021171200 available bytes; 98.99% used; 110367553 free inodes.

server2 `/home`: 18021171200 available bytes; 98.99% used; 110367553 free inodes.

server2 `/tmp`: 18021171200 available bytes; 98.99% used; 110367553 free inodes.

server2 `/var/tmp`: 18021171200 available bytes; 98.99% used; 110367553 free inodes.

server2 `/mnt/raid5`: 601108439040 available bytes; 95.85% used; 444965072 free inodes.
| server3 | True | [] | [] |

server3 `/`: 81263210496 available bytes; 95.47% used; 114065301 free inodes.

server3 `/home`: 81263210496 available bytes; 95.47% used; 114065301 free inodes.

server3 `/data`: 1348717158400 available bytes; 81.36% used; 225832758 free inodes.

server3 `/tmp`: 81263210496 available bytes; 95.47% used; 114065301 free inodes.

server3 `/var/tmp`: 81263210496 available bytes; 95.47% used; 114065301 free inodes.
| server4 | True | [] | ['/tmp', '/var/tmp'] |

server4 `/`: 105919438848 available bytes; 94.09% used; 114347833 free inodes.

server4 `/home`: 105919438848 available bytes; 94.09% used; 114347833 free inodes.

server4 `/data`: 410260873216 available bytes; 94.33% used; 224824171 free inodes.

server4 `/tmp`: 105919438848 available bytes; 94.09% used; 114347833 free inodes.

server4 `/var/tmp`: 105919438848 available bytes; 94.09% used; 114347833 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
