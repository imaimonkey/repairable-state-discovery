# V2R cluster inventory

2026-09-26T05:05:18.466036+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | ['1', '4', '5', '6', '7'] | ['/tmp', '/var/tmp'] |

server1 `/`: 318399107072 available bytes; 82.24% used; 112476272 free inodes.

server1 `/home`: 318399107072 available bytes; 82.24% used; 112476272 free inodes.

server1 `/tmp`: 318399107072 available bytes; 82.24% used; 112476272 free inodes.

server1 `/var/tmp`: 318399107072 available bytes; 82.24% used; 112476272 free inodes.

server1 `/mnt/raid5`: 329632845824 available bytes; 98.49% used; 337544636 free inodes.
| server2 | True | [] | [] |

server2 `/`: 22928699392 available bytes; 98.72% used; 110406196 free inodes.

server2 `/home`: 22928699392 available bytes; 98.72% used; 110406196 free inodes.

server2 `/tmp`: 22928699392 available bytes; 98.72% used; 110406196 free inodes.

server2 `/var/tmp`: 22928699392 available bytes; 98.72% used; 110406196 free inodes.

server2 `/mnt/raid5`: 284462231552 available bytes; 98.03% used; 445049630 free inodes.
| server3 | True | [] | [] |

server3 `/`: 84082098176 available bytes; 95.31% used; 114165979 free inodes.

server3 `/home`: 84082098176 available bytes; 95.31% used; 114165979 free inodes.

server3 `/data`: 124612550656 available bytes; 98.28% used; 225825397 free inodes.

server3 `/tmp`: 84082098176 available bytes; 95.31% used; 114165979 free inodes.

server3 `/var/tmp`: 84082098176 available bytes; 95.31% used; 114165979 free inodes.
| server4 | True | ['2', '3', '6', '7'] | ['/tmp', '/var/tmp'] |

server4 `/`: 105992998912 available bytes; 94.09% used; 114348206 free inodes.

server4 `/home`: 105992998912 available bytes; 94.09% used; 114348206 free inodes.

server4 `/data`: 106999738368 available bytes; 98.52% used; 224929217 free inodes.

server4 `/tmp`: 105992998912 available bytes; 94.09% used; 114348206 free inodes.

server4 `/var/tmp`: 105992998912 available bytes; 94.09% used; 114348206 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
