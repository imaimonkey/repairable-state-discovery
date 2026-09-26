# V2R cluster inventory

2026-09-26T09:46:36.954150+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | ['1', '4', '5', '6', '7'] | ['/tmp', '/var/tmp'] |

server1 `/`: 318617481216 available bytes; 82.23% used; 112475084 free inodes.

server1 `/home`: 318617481216 available bytes; 82.23% used; 112475084 free inodes.

server1 `/tmp`: 318617481216 available bytes; 82.23% used; 112475084 free inodes.

server1 `/var/tmp`: 318617481216 available bytes; 82.23% used; 112475084 free inodes.

server1 `/mnt/raid5`: 218930016256 available bytes; 99.00% used; 337538572 free inodes.
| server2 | True | [] | [] |

server2 `/`: 22314774528 available bytes; 98.76% used; 110403886 free inodes.

server2 `/home`: 22314774528 available bytes; 98.76% used; 110403886 free inodes.

server2 `/tmp`: 22314774528 available bytes; 98.76% used; 110403886 free inodes.

server2 `/var/tmp`: 22314774528 available bytes; 98.76% used; 110403886 free inodes.

server2 `/mnt/raid5`: 253706022912 available bytes; 98.25% used; 445022139 free inodes.
| server3 | True | [] | [] |

server3 `/`: 82659676160 available bytes; 95.39% used; 114110805 free inodes.

server3 `/home`: 82659676160 available bytes; 95.39% used; 114110805 free inodes.

server3 `/data`: 123595718656 available bytes; 98.29% used; 225827527 free inodes.

server3 `/tmp`: 82659676160 available bytes; 95.39% used; 114110805 free inodes.

server3 `/var/tmp`: 82659676160 available bytes; 95.39% used; 114110805 free inodes.
| server4 | True | ['3', '7'] | ['/tmp', '/var/tmp'] |

server4 `/`: 105932218368 available bytes; 94.09% used; 114348032 free inodes.

server4 `/home`: 105932218368 available bytes; 94.09% used; 114348032 free inodes.

server4 `/data`: 89265463296 available bytes; 98.77% used; 224882605 free inodes.

server4 `/tmp`: 105932218368 available bytes; 94.09% used; 114348032 free inodes.

server4 `/var/tmp`: 105932218368 available bytes; 94.09% used; 114348032 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
