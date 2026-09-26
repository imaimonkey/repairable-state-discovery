# V2R cluster inventory

2026-09-26T09:56:03.598277+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | ['1', '4', '5', '6', '7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 318613368832 available bytes; 82.23% used; 112475044 free inodes.

server1 `/home`: 318613368832 available bytes; 82.23% used; 112475044 free inodes.

server1 `/tmp`: 318613368832 available bytes; 82.23% used; 112475044 free inodes.

server1 `/var/tmp`: 318613368832 available bytes; 82.23% used; 112475044 free inodes.

server1 `/mnt/raid5`: 218909966336 available bytes; 99.00% used; 337538526 free inodes.
| server2 | True | [] | [] | reference_compatible=False |

server2 `/`: 22303105024 available bytes; 98.76% used; 110402878 free inodes.

server2 `/home`: 22303105024 available bytes; 98.76% used; 110402878 free inodes.

server2 `/tmp`: 22303105024 available bytes; 98.76% used; 110402878 free inodes.

server2 `/var/tmp`: 22303105024 available bytes; 98.76% used; 110402878 free inodes.

server2 `/mnt/raid5`: 252111982592 available bytes; 98.26% used; 445021862 free inodes.
| server3 | True | [] | [] | reference_compatible=True |

server3 `/`: 82662993920 available bytes; 95.39% used; 114110816 free inodes.

server3 `/home`: 82662993920 available bytes; 95.39% used; 114110816 free inodes.

server3 `/data`: 123593711616 available bytes; 98.29% used; 225827368 free inodes.

server3 `/tmp`: 82662993920 available bytes; 95.39% used; 114110816 free inodes.

server3 `/var/tmp`: 82662993920 available bytes; 95.39% used; 114110816 free inodes.
| server4 | True | ['3', '7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 105931390976 available bytes; 94.09% used; 114348027 free inodes.

server4 `/home`: 105931390976 available bytes; 94.09% used; 114348027 free inodes.

server4 `/data`: 89246117888 available bytes; 98.77% used; 224882302 free inodes.

server4 `/tmp`: 105931390976 available bytes; 94.09% used; 114348027 free inodes.

server4 `/var/tmp`: 105931390976 available bytes; 94.09% used; 114348027 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
