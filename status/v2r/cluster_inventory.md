# V2R cluster inventory

2026-09-24T07:01:07.007770+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | ['5', '7'] | ['/tmp', '/var/tmp'] |

server1 `/`: 324483776512 available bytes; 81.90% used; 112491370 free inodes.

server1 `/home`: 324483776512 available bytes; 81.90% used; 112491370 free inodes.

server1 `/tmp`: 324483776512 available bytes; 81.90% used; 112491370 free inodes.

server1 `/var/tmp`: 324483776512 available bytes; 81.90% used; 112491370 free inodes.

server1 `/mnt/raid5`: 496775532544 available bytes; 97.72% used; 337722842 free inodes.
| server2 | True | [] | [] |

server2 `/`: 57863069696 available bytes; 96.77% used; 110431179 free inodes.

server2 `/home`: 57863069696 available bytes; 96.77% used; 110431179 free inodes.

server2 `/tmp`: 57863069696 available bytes; 96.77% used; 110431179 free inodes.

server2 `/var/tmp`: 57863069696 available bytes; 96.77% used; 110431179 free inodes.

server2 `/mnt/raid5`: 519283261440 available bytes; 96.41% used; 445191085 free inodes.
| server3 | True | [] | ['/tmp', '/var/tmp'] |

server3 `/`: 126756716544 available bytes; 92.93% used; 114175146 free inodes.

server3 `/home`: 126756716544 available bytes; 92.93% used; 114175146 free inodes.

server3 `/data`: 139199287296 available bytes; 98.08% used; 225834747 free inodes.

server3 `/tmp`: 126756716544 available bytes; 92.93% used; 114175146 free inodes.

server3 `/var/tmp`: 126756716544 available bytes; 92.93% used; 114175146 free inodes.
| server4 | True | [] | ['/tmp', '/var/tmp'] |

server4 `/`: 105790365696 available bytes; 94.10% used; 114349211 free inodes.

server4 `/home`: 105790365696 available bytes; 94.10% used; 114349211 free inodes.

server4 `/data`: 303079071744 available bytes; 95.81% used; 225367737 free inodes.

server4 `/tmp`: 105790365696 available bytes; 94.10% used; 114349211 free inodes.

server4 `/var/tmp`: 105790365696 available bytes; 94.10% used; 114349211 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
