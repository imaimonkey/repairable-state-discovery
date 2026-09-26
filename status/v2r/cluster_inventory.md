# V2R cluster inventory

2026-09-26T21:31:28.885543+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | ['0', '1', '2', '3', '4', '5', '6', '7'] | ['/tmp', '/var/tmp'] |

server1 `/`: 315479871488 available bytes; 82.40% used; 112445690 free inodes.

server1 `/home`: 315479871488 available bytes; 82.40% used; 112445690 free inodes.

server1 `/tmp`: 315479871488 available bytes; 82.40% used; 112445690 free inodes.

server1 `/var/tmp`: 315479871488 available bytes; 82.40% used; 112445690 free inodes.

server1 `/mnt/raid5`: 645854470144 available bytes; 97.04% used; 337467239 free inodes.
| server2 | True | ['2', '7'] | [] |

server2 `/`: 17951162368 available bytes; 99.00% used; 110367531 free inodes.

server2 `/home`: 17951162368 available bytes; 99.00% used; 110367531 free inodes.

server2 `/tmp`: 17951162368 available bytes; 99.00% used; 110367531 free inodes.

server2 `/var/tmp`: 17951162368 available bytes; 99.00% used; 110367531 free inodes.

server2 `/mnt/raid5`: 598711205888 available bytes; 95.86% used; 444962575 free inodes.
| server3 | True | [] | [] |

server3 `/`: 81111486464 available bytes; 95.47% used; 114072905 free inodes.

server3 `/home`: 81111486464 available bytes; 95.47% used; 114072905 free inodes.

server3 `/data`: 1349635870720 available bytes; 81.35% used; 225827708 free inodes.

server3 `/tmp`: 81111486464 available bytes; 95.47% used; 114072905 free inodes.

server3 `/var/tmp`: 81111486464 available bytes; 95.47% used; 114072905 free inodes.
| server4 | True | ['5', '7'] | ['/tmp', '/var/tmp'] |

server4 `/`: 105909055488 available bytes; 94.09% used; 114347843 free inodes.

server4 `/home`: 105909055488 available bytes; 94.09% used; 114347843 free inodes.

server4 `/data`: 409895849984 available bytes; 94.34% used; 224823843 free inodes.

server4 `/tmp`: 105909055488 available bytes; 94.09% used; 114347843 free inodes.

server4 `/var/tmp`: 105909055488 available bytes; 94.09% used; 114347843 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
