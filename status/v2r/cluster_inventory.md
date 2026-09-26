# V2R cluster inventory

2026-09-26T05:38:57.518026+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | ['1', '4', '5', '6', '7'] | ['/tmp', '/var/tmp'] |

server1 `/`: 318783348736 available bytes; 82.22% used; 112476274 free inodes.

server1 `/home`: 318783348736 available bytes; 82.22% used; 112476274 free inodes.

server1 `/tmp`: 318783348736 available bytes; 82.22% used; 112476274 free inodes.

server1 `/var/tmp`: 318783348736 available bytes; 82.22% used; 112476274 free inodes.

server1 `/mnt/raid5`: 244354510848 available bytes; 98.88% used; 337540172 free inodes.
| server2 | True | [] | [] |

server2 `/`: 22927425536 available bytes; 98.72% used; 110406217 free inodes.

server2 `/home`: 22927425536 available bytes; 98.72% used; 110406217 free inodes.

server2 `/tmp`: 22927425536 available bytes; 98.72% used; 110406217 free inodes.

server2 `/var/tmp`: 22927425536 available bytes; 98.72% used; 110406217 free inodes.

server2 `/mnt/raid5`: 276315090944 available bytes; 98.09% used; 445048389 free inodes.
| server3 | True | [] | [] |

server3 `/`: 83220455424 available bytes; 95.36% used; 114150415 free inodes.

server3 `/home`: 83220455424 available bytes; 95.36% used; 114150415 free inodes.

server3 `/data`: 124339482624 available bytes; 98.28% used; 225824096 free inodes.

server3 `/tmp`: 83220455424 available bytes; 95.36% used; 114150415 free inodes.

server3 `/var/tmp`: 83220455424 available bytes; 95.36% used; 114150415 free inodes.
| server4 | True | ['2', '3', '6', '7'] | ['/tmp', '/var/tmp'] |

server4 `/`: 106094682112 available bytes; 94.08% used; 114348208 free inodes.

server4 `/home`: 106094682112 available bytes; 94.08% used; 114348208 free inodes.

server4 `/data`: 106991886336 available bytes; 98.52% used; 224929134 free inodes.

server4 `/tmp`: 106094682112 available bytes; 94.08% used; 114348208 free inodes.

server4 `/var/tmp`: 106094682112 available bytes; 94.08% used; 114348208 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
