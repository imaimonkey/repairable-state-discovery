# V2R cluster inventory

2026-09-26T08:13:24.405273+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | ['1', '4', '5', '6', '7'] | ['/tmp', '/var/tmp'] |

server1 `/`: 318747549696 available bytes; 82.22% used; 112475793 free inodes.

server1 `/home`: 318747549696 available bytes; 82.22% used; 112475793 free inodes.

server1 `/tmp`: 318747549696 available bytes; 82.22% used; 112475793 free inodes.

server1 `/var/tmp`: 318747549696 available bytes; 82.22% used; 112475793 free inodes.

server1 `/mnt/raid5`: 219142057984 available bytes; 98.99% used; 337539019 free inodes.
| server2 | True | [] | [] |

server2 `/`: 22313164800 available bytes; 98.76% used; 110403905 free inodes.

server2 `/home`: 22313164800 available bytes; 98.76% used; 110403905 free inodes.

server2 `/tmp`: 22313164800 available bytes; 98.76% used; 110403905 free inodes.

server2 `/var/tmp`: 22313164800 available bytes; 98.76% used; 110403905 free inodes.

server2 `/mnt/raid5`: 256218783744 available bytes; 98.23% used; 445025645 free inodes.
| server3 | True | [] | [] |

server3 `/`: 82678992896 available bytes; 95.39% used; 114110814 free inodes.

server3 `/home`: 82678992896 available bytes; 95.39% used; 114110814 free inodes.

server3 `/data`: 123919798272 available bytes; 98.29% used; 225829271 free inodes.

server3 `/tmp`: 82678992896 available bytes; 95.39% used; 114110814 free inodes.

server3 `/var/tmp`: 82678992896 available bytes; 95.39% used; 114110814 free inodes.
| server4 | True | ['2', '3', '6', '7'] | ['/tmp', '/var/tmp'] |

server4 `/`: 106064691200 available bytes; 94.08% used; 114348149 free inodes.

server4 `/home`: 106064691200 available bytes; 94.08% used; 114348149 free inodes.

server4 `/data`: 89390239744 available bytes; 98.76% used; 224883485 free inodes.

server4 `/tmp`: 106064691200 available bytes; 94.08% used; 114348149 free inodes.

server4 `/var/tmp`: 106064691200 available bytes; 94.08% used; 114348149 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
