# V2R cluster inventory

2026-09-26T09:57:35.093479+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | ['1', '4', '5', '6', '7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 318613118976 available bytes; 82.23% used; 112475043 free inodes.

server1 `/home`: 318613118976 available bytes; 82.23% used; 112475043 free inodes.

server1 `/tmp`: 318613118976 available bytes; 82.23% used; 112475043 free inodes.

server1 `/var/tmp`: 318613118976 available bytes; 82.23% used; 112475043 free inodes.

server1 `/mnt/raid5`: 218904121344 available bytes; 99.00% used; 337538513 free inodes.
| server2 | True | [] | [] | reference_compatible=False |

server2 `/`: 22302859264 available bytes; 98.76% used; 110402878 free inodes.

server2 `/home`: 22302859264 available bytes; 98.76% used; 110402878 free inodes.

server2 `/tmp`: 22302859264 available bytes; 98.76% used; 110402878 free inodes.

server2 `/var/tmp`: 22302859264 available bytes; 98.76% used; 110402878 free inodes.

server2 `/mnt/raid5`: 252608118784 available bytes; 98.25% used; 445022028 free inodes.
| server3 | True | [] | [] | reference_compatible=True |

server3 `/`: 82662625280 available bytes; 95.39% used; 114110816 free inodes.

server3 `/home`: 82662625280 available bytes; 95.39% used; 114110816 free inodes.

server3 `/data`: 123593666560 available bytes; 98.29% used; 225827334 free inodes.

server3 `/tmp`: 82662625280 available bytes; 95.39% used; 114110816 free inodes.

server3 `/var/tmp`: 82662625280 available bytes; 95.39% used; 114110816 free inodes.
| server4 | True | ['3', '7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 105931350016 available bytes; 94.09% used; 114348027 free inodes.

server4 `/home`: 105931350016 available bytes; 94.09% used; 114348027 free inodes.

server4 `/data`: 89241059328 available bytes; 98.77% used; 224882270 free inodes.

server4 `/tmp`: 105931350016 available bytes; 94.09% used; 114348027 free inodes.

server4 `/var/tmp`: 105931350016 available bytes; 94.09% used; 114348027 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
