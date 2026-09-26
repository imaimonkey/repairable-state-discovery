# V2R cluster inventory

2026-09-26T08:24:07.082187+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | ['1', '4', '5', '6', '7'] | ['/tmp', '/var/tmp'] |

server1 `/`: 318746738688 available bytes; 82.22% used; 112475801 free inodes.

server1 `/home`: 318746738688 available bytes; 82.22% used; 112475801 free inodes.

server1 `/tmp`: 318746738688 available bytes; 82.22% used; 112475801 free inodes.

server1 `/var/tmp`: 318746738688 available bytes; 82.22% used; 112475801 free inodes.

server1 `/mnt/raid5`: 219116396544 available bytes; 98.99% used; 337538965 free inodes.
| server2 | True | [] | [] |

server2 `/`: 22318342144 available bytes; 98.75% used; 110403904 free inodes.

server2 `/home`: 22318342144 available bytes; 98.75% used; 110403904 free inodes.

server2 `/tmp`: 22318342144 available bytes; 98.75% used; 110403904 free inodes.

server2 `/var/tmp`: 22318342144 available bytes; 98.75% used; 110403904 free inodes.

server2 `/mnt/raid5`: 255892430848 available bytes; 98.23% used; 445024940 free inodes.
| server3 | True | [] | [] |

server3 `/`: 82679648256 available bytes; 95.39% used; 114110811 free inodes.

server3 `/home`: 82679648256 available bytes; 95.39% used; 114110811 free inodes.

server3 `/data`: 123913469952 available bytes; 98.29% used; 225829013 free inodes.

server3 `/tmp`: 82679648256 available bytes; 95.39% used; 114110811 free inodes.

server3 `/var/tmp`: 82679648256 available bytes; 95.39% used; 114110811 free inodes.
| server4 | True | ['3', '7'] | ['/tmp', '/var/tmp'] |

server4 `/`: 106064297984 available bytes; 94.08% used; 114348133 free inodes.

server4 `/home`: 106064297984 available bytes; 94.08% used; 114348133 free inodes.

server4 `/data`: 89382584320 available bytes; 98.76% used; 224883413 free inodes.

server4 `/tmp`: 106064297984 available bytes; 94.08% used; 114348133 free inodes.

server4 `/var/tmp`: 106064297984 available bytes; 94.08% used; 114348133 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
