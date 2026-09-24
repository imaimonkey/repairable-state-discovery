# V2R cluster inventory

2026-09-24T02:00:50.257242+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | ['4', '6', '7'] | ['/tmp', '/var/tmp'] |

server1 `/`: 325446070272 available bytes; 81.84% used; 112499300 free inodes.

server1 `/home`: 325446070272 available bytes; 81.84% used; 112499300 free inodes.

server1 `/tmp`: 325446070272 available bytes; 81.84% used; 112499300 free inodes.

server1 `/var/tmp`: 325446070272 available bytes; 81.84% used; 112499300 free inodes.

server1 `/mnt/raid5`: 771102011392 available bytes; 96.46% used; 337733637 free inodes.
| server2 | True | [] | [] |

server2 `/`: 40919994368 available bytes; 97.72% used; 110431753 free inodes.

server2 `/home`: 40919994368 available bytes; 97.72% used; 110431753 free inodes.

server2 `/tmp`: 40919994368 available bytes; 97.72% used; 110431753 free inodes.

server2 `/var/tmp`: 40919994368 available bytes; 97.72% used; 110431753 free inodes.

server2 `/mnt/raid5`: 529907265536 available bytes; 96.34% used; 445200433 free inodes.
| server3 | True | [] | ['/tmp', '/var/tmp'] |

server3 `/`: 292720508928 available bytes; 83.67% used; 114211171 free inodes.

server3 `/home`: 292720508928 available bytes; 83.67% used; 114211171 free inodes.

server3 `/data`: 60361027584 available bytes; 99.17% used; 225841664 free inodes.

server3 `/tmp`: 292720508928 available bytes; 83.67% used; 114211171 free inodes.

server3 `/var/tmp`: 292720508928 available bytes; 83.67% used; 114211171 free inodes.
| server4 | True | ['2', '3', '6', '7'] | ['/tmp', '/var/tmp'] |

server4 `/`: 105938292736 available bytes; 94.09% used; 114348463 free inodes.

server4 `/home`: 105938292736 available bytes; 94.09% used; 114348463 free inodes.

server4 `/data`: 289779494912 available bytes; 96.00% used; 225388486 free inodes.

server4 `/tmp`: 105938292736 available bytes; 94.09% used; 114348463 free inodes.

server4 `/var/tmp`: 105938292736 available bytes; 94.09% used; 114348463 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
