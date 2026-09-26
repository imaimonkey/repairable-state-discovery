# V2R cluster inventory

2026-09-26T10:40:18.724078+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | ['1', '4', '5', '6', '7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 318219595776 available bytes; 82.25% used; 112474765 free inodes.

server1 `/home`: 318219595776 available bytes; 82.25% used; 112474765 free inodes.

server1 `/tmp`: 318219595776 available bytes; 82.25% used; 112474765 free inodes.

server1 `/var/tmp`: 318219595776 available bytes; 82.25% used; 112474765 free inodes.

server1 `/mnt/raid5`: 218814148608 available bytes; 99.00% used; 337538322 free inodes.
| server2 | True | [] | [] | reference_compatible=False |

server2 `/`: 19847954432 available bytes; 98.89% used; 110384913 free inodes.

server2 `/home`: 19847954432 available bytes; 98.89% used; 110384913 free inodes.

server2 `/tmp`: 19847954432 available bytes; 98.89% used; 110384913 free inodes.

server2 `/var/tmp`: 19847954432 available bytes; 98.89% used; 110384913 free inodes.

server2 `/mnt/raid5`: 243247071232 available bytes; 98.32% used; 444979279 free inodes.
| server3 | True | [] | [] | reference_compatible=True |

server3 `/`: 82660716544 available bytes; 95.39% used; 114110825 free inodes.

server3 `/home`: 82660716544 available bytes; 95.39% used; 114110825 free inodes.

server3 `/data`: 123575844864 available bytes; 98.29% used; 225826610 free inodes.

server3 `/tmp`: 82660716544 available bytes; 95.39% used; 114110825 free inodes.

server3 `/var/tmp`: 82660716544 available bytes; 95.39% used; 114110825 free inodes.
| server4 | True | ['3', '5', '7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 105927278592 available bytes; 94.09% used; 114347977 free inodes.

server4 `/home`: 105927278592 available bytes; 94.09% used; 114347977 free inodes.

server4 `/data`: 89074503680 available bytes; 98.77% used; 224881019 free inodes.

server4 `/tmp`: 105927278592 available bytes; 94.09% used; 114347977 free inodes.

server4 `/var/tmp`: 105927278592 available bytes; 94.09% used; 114347977 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
