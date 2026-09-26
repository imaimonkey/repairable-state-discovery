# V2R cluster inventory

2026-09-26T10:37:01.869242+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | ['1', '4', '5', '6', '7'] | ['/tmp', '/var/tmp'] |

server1 `/`: 318221262848 available bytes; 82.25% used; 112474852 free inodes.

server1 `/home`: 318221262848 available bytes; 82.25% used; 112474852 free inodes.

server1 `/tmp`: 318221262848 available bytes; 82.25% used; 112474852 free inodes.

server1 `/var/tmp`: 318221262848 available bytes; 82.25% used; 112474852 free inodes.

server1 `/mnt/raid5`: 218819989504 available bytes; 99.00% used; 337538335 free inodes.
| server2 | True | [] | [] |

server2 `/`: 19849981952 available bytes; 98.89% used; 110384911 free inodes.

server2 `/home`: 19849981952 available bytes; 98.89% used; 110384911 free inodes.

server2 `/tmp`: 19849981952 available bytes; 98.89% used; 110384911 free inodes.

server2 `/var/tmp`: 19849981952 available bytes; 98.89% used; 110384911 free inodes.

server2 `/mnt/raid5`: 242831335424 available bytes; 98.32% used; 444979642 free inodes.
| server3 | True | [] | [] |

server3 `/`: 82661400576 available bytes; 95.39% used; 114110825 free inodes.

server3 `/home`: 82661400576 available bytes; 95.39% used; 114110825 free inodes.

server3 `/data`: 123577552896 available bytes; 98.29% used; 225826683 free inodes.

server3 `/tmp`: 82661400576 available bytes; 95.39% used; 114110825 free inodes.

server3 `/var/tmp`: 82661400576 available bytes; 95.39% used; 114110825 free inodes.
| server4 | True | ['3', '5', '7'] | ['/tmp', '/var/tmp'] |

server4 `/`: 105927368704 available bytes; 94.09% used; 114347977 free inodes.

server4 `/home`: 105927368704 available bytes; 94.09% used; 114347977 free inodes.

server4 `/data`: 89074483200 available bytes; 98.77% used; 224881029 free inodes.

server4 `/tmp`: 105927368704 available bytes; 94.09% used; 114347977 free inodes.

server4 `/var/tmp`: 105927368704 available bytes; 94.09% used; 114347977 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
