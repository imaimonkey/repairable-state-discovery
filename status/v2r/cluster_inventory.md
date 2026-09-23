# V2R cluster inventory

2026-09-23T19:20:29.817607+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | ['4', '7'] | ['/tmp', '/var/tmp', '/mnt/raid5'] |

server1 `/`: 325752446976 available bytes; 81.83% used; 112501860 free inodes.

server1 `/home`: 325752446976 available bytes; 81.83% used; 112501860 free inodes.

server1 `/tmp`: 325752446976 available bytes; 81.83% used; 112501860 free inodes.

server1 `/var/tmp`: 325752446976 available bytes; 81.83% used; 112501860 free inodes.

server1 `/mnt/raid5`: 1385397833728 available bytes; 93.64% used; 337741369 free inodes.
| server2 | True | ['6', '7'] | [] |

server2 `/`: 41328680960 available bytes; 97.69% used; 110435428 free inodes.

server2 `/home`: 41328680960 available bytes; 97.69% used; 110435428 free inodes.

server2 `/tmp`: 41328680960 available bytes; 97.69% used; 110435428 free inodes.

server2 `/var/tmp`: 41328680960 available bytes; 97.69% used; 110435428 free inodes.

server2 `/mnt/raid5`: 543445843968 available bytes; 96.24% used; 445212733 free inodes.
| server3 | True | [] | ['/tmp', '/var/tmp'] |

server3 `/`: 293891145728 available bytes; 83.60% used; 114253793 free inodes.

server3 `/home`: 293891145728 available bytes; 83.60% used; 114253793 free inodes.

server3 `/data`: 52755345408 available bytes; 99.27% used; 225845691 free inodes.

server3 `/tmp`: 293891145728 available bytes; 83.60% used; 114253793 free inodes.

server3 `/var/tmp`: 293891145728 available bytes; 83.60% used; 114253793 free inodes.
| server4 | True | ['0', '1', '2', '3', '4', '5', '6'] | ['/tmp', '/var/tmp'] |

server4 `/`: 106529415168 available bytes; 94.06% used; 114356234 free inodes.

server4 `/home`: 106529415168 available bytes; 94.06% used; 114356234 free inodes.

server4 `/data`: 5857280 available bytes; 100.00% used; 225457645 free inodes.

server4 `/tmp`: 106529415168 available bytes; 94.06% used; 114356234 free inodes.

server4 `/var/tmp`: 106529415168 available bytes; 94.06% used; 114356234 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
