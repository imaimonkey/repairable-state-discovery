# V2R cluster inventory

2026-09-23T21:32:02.909485+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | ['6', '7'] | ['/tmp', '/var/tmp', '/mnt/raid5'] |

server1 `/`: 325718122496 available bytes; 81.83% used; 112501427 free inodes.

server1 `/home`: 325718122496 available bytes; 81.83% used; 112501427 free inodes.

server1 `/tmp`: 325718122496 available bytes; 81.83% used; 112501427 free inodes.

server1 `/var/tmp`: 325718122496 available bytes; 81.83% used; 112501427 free inodes.

server1 `/mnt/raid5`: 1388140294144 available bytes; 93.63% used; 337739956 free inodes.
| server2 | True | [] | [] |

server2 `/`: 41122508800 available bytes; 97.71% used; 110432692 free inodes.

server2 `/home`: 41122508800 available bytes; 97.71% used; 110432692 free inodes.

server2 `/tmp`: 41122508800 available bytes; 97.71% used; 110432692 free inodes.

server2 `/var/tmp`: 41122508800 available bytes; 97.71% used; 110432692 free inodes.

server2 `/mnt/raid5`: 538444025856 available bytes; 96.28% used; 445208482 free inodes.
| server3 | True | [] | ['/tmp', '/var/tmp'] |

server3 `/`: 293246189568 available bytes; 83.64% used; 114229089 free inodes.

server3 `/home`: 293246189568 available bytes; 83.64% used; 114229089 free inodes.

server3 `/data`: 52275433472 available bytes; 99.28% used; 225848752 free inodes.

server3 `/tmp`: 293246189568 available bytes; 83.64% used; 114229089 free inodes.

server3 `/var/tmp`: 293246189568 available bytes; 83.64% used; 114229089 free inodes.
| server4 | True | ['2', '3', '5', '6', '7'] | ['/tmp', '/var/tmp'] |

server4 `/`: 106479501312 available bytes; 94.06% used; 114355997 free inodes.

server4 `/home`: 106479501312 available bytes; 94.06% used; 114355997 free inodes.

server4 `/data`: 300307636224 available bytes; 95.85% used; 225450518 free inodes.

server4 `/tmp`: 106479501312 available bytes; 94.06% used; 114355997 free inodes.

server4 `/var/tmp`: 106479501312 available bytes; 94.06% used; 114355997 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
