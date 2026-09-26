# V2R cluster inventory

2026-09-26T11:38:09.410449+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | ['1', '4', '5', '6', '7'] | ['/tmp', '/var/tmp'] |

server1 `/`: 318197301248 available bytes; 82.25% used; 112474814 free inodes.

server1 `/home`: 318197301248 available bytes; 82.25% used; 112474814 free inodes.

server1 `/tmp`: 318197301248 available bytes; 82.25% used; 112474814 free inodes.

server1 `/var/tmp`: 318197301248 available bytes; 82.25% used; 112474814 free inodes.

server1 `/mnt/raid5`: 218676785152 available bytes; 99.00% used; 337538039 free inodes.
| server2 | True | [] | [] |

server2 `/`: 19790020608 available bytes; 98.90% used; 110383617 free inodes.

server2 `/home`: 19790020608 available bytes; 98.90% used; 110383617 free inodes.

server2 `/tmp`: 19790020608 available bytes; 98.90% used; 110383617 free inodes.

server2 `/var/tmp`: 19790020608 available bytes; 98.90% used; 110383617 free inodes.

server2 `/mnt/raid5`: 241178431488 available bytes; 98.33% used; 444977728 free inodes.
| server3 | True | [] | [] |

server3 `/`: 82649702400 available bytes; 95.39% used; 114110823 free inodes.

server3 `/home`: 82649702400 available bytes; 95.39% used; 114110823 free inodes.

server3 `/data`: 123436908544 available bytes; 98.29% used; 225825387 free inodes.

server3 `/tmp`: 82649702400 available bytes; 95.39% used; 114110823 free inodes.

server3 `/var/tmp`: 82649702400 available bytes; 95.39% used; 114110823 free inodes.
| server4 | True | ['0', '3', '5', '7'] | ['/tmp', '/var/tmp'] |

server4 `/`: 105901002752 available bytes; 94.09% used; 114347938 free inodes.

server4 `/home`: 105901002752 available bytes; 94.09% used; 114347938 free inodes.

server4 `/data`: 88638623744 available bytes; 98.77% used; 224879407 free inodes.

server4 `/tmp`: 105901002752 available bytes; 94.09% used; 114347938 free inodes.

server4 `/var/tmp`: 105901002752 available bytes; 94.09% used; 114347938 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
