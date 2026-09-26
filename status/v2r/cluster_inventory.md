# V2R cluster inventory

2026-09-26T23:07:31.518914+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | ['0', '1', '2', '3', '4', '5', '6', '7'] | ['/tmp', '/var/tmp'] |

server1 `/`: 315468455936 available bytes; 82.40% used; 112445703 free inodes.

server1 `/home`: 315468455936 available bytes; 82.40% used; 112445703 free inodes.

server1 `/tmp`: 315468455936 available bytes; 82.40% used; 112445703 free inodes.

server1 `/var/tmp`: 315468455936 available bytes; 82.40% used; 112445703 free inodes.

server1 `/mnt/raid5`: 645833363456 available bytes; 97.04% used; 337467222 free inodes.
| server2 | True | ['2', '7'] | [] |

server2 `/`: 17940406272 available bytes; 99.00% used; 110367505 free inodes.

server2 `/home`: 17940406272 available bytes; 99.00% used; 110367505 free inodes.

server2 `/tmp`: 17940406272 available bytes; 99.00% used; 110367505 free inodes.

server2 `/var/tmp`: 17940406272 available bytes; 99.00% used; 110367505 free inodes.

server2 `/mnt/raid5`: 595703554048 available bytes; 95.88% used; 444959934 free inodes.
| server3 | True | ['2'] | [] |

server3 `/`: 81080188928 available bytes; 95.48% used; 114069879 free inodes.

server3 `/home`: 81080188928 available bytes; 95.48% used; 114069879 free inodes.

server3 `/data`: 1349239488512 available bytes; 81.35% used; 225826648 free inodes.

server3 `/tmp`: 81080188928 available bytes; 95.48% used; 114069879 free inodes.

server3 `/var/tmp`: 81080188928 available bytes; 95.48% used; 114069879 free inodes.
| server4 | True | ['2', '3', '5', '7'] | ['/tmp', '/var/tmp'] |

server4 `/`: 105898258432 available bytes; 94.09% used; 114347853 free inodes.

server4 `/home`: 105898258432 available bytes; 94.09% used; 114347853 free inodes.

server4 `/data`: 409613172736 available bytes; 94.34% used; 224823839 free inodes.

server4 `/tmp`: 105898258432 available bytes; 94.09% used; 114347853 free inodes.

server4 `/var/tmp`: 105898258432 available bytes; 94.09% used; 114347853 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
