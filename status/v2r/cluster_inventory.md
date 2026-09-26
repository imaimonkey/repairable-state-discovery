# V2R cluster inventory

2026-09-26T09:59:06.565806+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | ['1', '4', '5', '6', '7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 318612946944 available bytes; 82.23% used; 112475043 free inodes.

server1 `/home`: 318612946944 available bytes; 82.23% used; 112475043 free inodes.

server1 `/tmp`: 318612946944 available bytes; 82.23% used; 112475043 free inodes.

server1 `/var/tmp`: 318612946944 available bytes; 82.23% used; 112475043 free inodes.

server1 `/mnt/raid5`: 218902609920 available bytes; 99.00% used; 337538505 free inodes.
| server2 | True | [] | [] | reference_compatible=False |

server2 `/`: 22302527488 available bytes; 98.76% used; 110402878 free inodes.

server2 `/home`: 22302527488 available bytes; 98.76% used; 110402878 free inodes.

server2 `/tmp`: 22302527488 available bytes; 98.76% used; 110402878 free inodes.

server2 `/var/tmp`: 22302527488 available bytes; 98.76% used; 110402878 free inodes.

server2 `/mnt/raid5`: 252563234816 available bytes; 98.25% used; 445021859 free inodes.
| server3 | True | [] | [] | reference_compatible=True |

server3 `/`: 82662268928 available bytes; 95.39% used; 114110816 free inodes.

server3 `/home`: 82662268928 available bytes; 95.39% used; 114110816 free inodes.

server3 `/data`: 123592105984 available bytes; 98.29% used; 225827318 free inodes.

server3 `/tmp`: 82662268928 available bytes; 95.39% used; 114110816 free inodes.

server3 `/var/tmp`: 82662268928 available bytes; 95.39% used; 114110816 free inodes.
| server4 | True | ['3', '7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 105931317248 available bytes; 94.09% used; 114348027 free inodes.

server4 `/home`: 105931317248 available bytes; 94.09% used; 114348027 free inodes.

server4 `/data`: 89232818176 available bytes; 98.77% used; 224882266 free inodes.

server4 `/tmp`: 105931317248 available bytes; 94.09% used; 114348027 free inodes.

server4 `/var/tmp`: 105931317248 available bytes; 94.09% used; 114348027 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
