# V2R cluster inventory

2026-09-24T01:54:34.154713+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | ['4', '6', '7'] | ['/tmp', '/var/tmp'] |

server1 `/`: 325450895360 available bytes; 81.84% used; 112499401 free inodes.

server1 `/home`: 325450895360 available bytes; 81.84% used; 112499401 free inodes.

server1 `/tmp`: 325450895360 available bytes; 81.84% used; 112499401 free inodes.

server1 `/var/tmp`: 325450895360 available bytes; 81.84% used; 112499401 free inodes.

server1 `/mnt/raid5`: 796237135872 available bytes; 96.35% used; 337733652 free inodes.
| server2 | True | [] | [] |

server2 `/`: 40922284032 available bytes; 97.72% used; 110431807 free inodes.

server2 `/home`: 40922284032 available bytes; 97.72% used; 110431807 free inodes.

server2 `/tmp`: 40922284032 available bytes; 97.72% used; 110431807 free inodes.

server2 `/var/tmp`: 40922284032 available bytes; 97.72% used; 110431807 free inodes.

server2 `/mnt/raid5`: 530119892992 available bytes; 96.34% used; 445200736 free inodes.
| server3 | True | [] | ['/tmp', '/var/tmp'] |

server3 `/`: 292721160192 available bytes; 83.67% used; 114211098 free inodes.

server3 `/home`: 292721160192 available bytes; 83.67% used; 114211098 free inodes.

server3 `/data`: 60687360000 available bytes; 99.16% used; 225841790 free inodes.

server3 `/tmp`: 292721160192 available bytes; 83.67% used; 114211098 free inodes.

server3 `/var/tmp`: 292721160192 available bytes; 83.67% used; 114211098 free inodes.
| server4 | True | ['2', '3', '6', '7'] | ['/tmp', '/var/tmp'] |

server4 `/`: 105947279360 available bytes; 94.09% used; 114348512 free inodes.

server4 `/home`: 105947279360 available bytes; 94.09% used; 114348512 free inodes.

server4 `/data`: 289770770432 available bytes; 96.00% used; 225388495 free inodes.

server4 `/tmp`: 105947279360 available bytes; 94.09% used; 114348512 free inodes.

server4 `/var/tmp`: 105947279360 available bytes; 94.09% used; 114348512 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
