# V2R cluster inventory

2026-09-26T10:11:19.007546+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | ['1', '4', '5', '6', '7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 318606958592 available bytes; 82.23% used; 112474984 free inodes.

server1 `/home`: 318606958592 available bytes; 82.23% used; 112474984 free inodes.

server1 `/tmp`: 318606958592 available bytes; 82.23% used; 112474984 free inodes.

server1 `/var/tmp`: 318606958592 available bytes; 82.23% used; 112474984 free inodes.

server1 `/mnt/raid5`: 218875011072 available bytes; 99.00% used; 337538446 free inodes.
| server2 | True | [] | [] | reference_compatible=False |

server2 `/`: 22297624576 available bytes; 98.76% used; 110402872 free inodes.

server2 `/home`: 22297624576 available bytes; 98.76% used; 110402872 free inodes.

server2 `/tmp`: 22297624576 available bytes; 98.76% used; 110402872 free inodes.

server2 `/var/tmp`: 22297624576 available bytes; 98.76% used; 110402872 free inodes.

server2 `/mnt/raid5`: 252176154624 available bytes; 98.26% used; 445021327 free inodes.
| server3 | True | [] | [] | reference_compatible=True |

server3 `/`: 82657046528 available bytes; 95.39% used; 114110823 free inodes.

server3 `/home`: 82657046528 available bytes; 95.39% used; 114110823 free inodes.

server3 `/data`: 123587158016 available bytes; 98.29% used; 225827114 free inodes.

server3 `/tmp`: 82657046528 available bytes; 95.39% used; 114110823 free inodes.

server3 `/var/tmp`: 82657046528 available bytes; 95.39% used; 114110823 free inodes.
| server4 | True | ['3', '5', '7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 105930915840 available bytes; 94.09% used; 114348032 free inodes.

server4 `/home`: 105930915840 available bytes; 94.09% used; 114348032 free inodes.

server4 `/data`: 89136881664 available bytes; 98.77% used; 224882039 free inodes.

server4 `/tmp`: 105930915840 available bytes; 94.09% used; 114348032 free inodes.

server4 `/var/tmp`: 105930915840 available bytes; 94.09% used; 114348032 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
