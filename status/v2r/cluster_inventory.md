# V2R cluster inventory

2026-09-24T09:58:46.309896+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | [] | ['/tmp', '/var/tmp'] |

server1 `/`: 324429955072 available bytes; 81.90% used; 112489541 free inodes.

server1 `/home`: 324429955072 available bytes; 81.90% used; 112489541 free inodes.

server1 `/tmp`: 324429955072 available bytes; 81.90% used; 112489541 free inodes.

server1 `/var/tmp`: 324429955072 available bytes; 81.90% used; 112489541 free inodes.

server1 `/mnt/raid5`: 500707717120 available bytes; 97.70% used; 337701517 free inodes.
| server2 | True | [] | [] |

server2 `/`: 57754386432 available bytes; 96.78% used; 110430741 free inodes.

server2 `/home`: 57754386432 available bytes; 96.78% used; 110430741 free inodes.

server2 `/tmp`: 57754386432 available bytes; 96.78% used; 110430741 free inodes.

server2 `/var/tmp`: 57754386432 available bytes; 96.78% used; 110430741 free inodes.

server2 `/mnt/raid5`: 513737129984 available bytes; 96.45% used; 445176919 free inodes.
| server3 | True | [] | [] |

server3 `/`: 85428252672 available bytes; 95.23% used; 114182452 free inodes.

server3 `/home`: 85428252672 available bytes; 95.23% used; 114182452 free inodes.

server3 `/data`: 165568499712 available bytes; 97.71% used; 225819645 free inodes.

server3 `/tmp`: 85428252672 available bytes; 95.23% used; 114182452 free inodes.

server3 `/var/tmp`: 85428252672 available bytes; 95.23% used; 114182452 free inodes.
| server4 | True | [] | ['/tmp', '/var/tmp'] |

server4 `/`: 105748172800 available bytes; 94.10% used; 114349034 free inodes.

server4 `/home`: 105748172800 available bytes; 94.10% used; 114349034 free inodes.

server4 `/data`: 154558734336 available bytes; 97.86% used; 225273208 free inodes.

server4 `/tmp`: 105748172800 available bytes; 94.10% used; 114349034 free inodes.

server4 `/var/tmp`: 105748172800 available bytes; 94.10% used; 114349034 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
