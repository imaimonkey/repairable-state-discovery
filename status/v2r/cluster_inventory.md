# V2R cluster inventory

2026-09-24T05:07:28.568610+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | ['7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 324597903360 available bytes; 81.89% used; 112492596 free inodes.

server1 `/home`: 324597903360 available bytes; 81.89% used; 112492596 free inodes.

server1 `/tmp`: 324597903360 available bytes; 81.89% used; 112492596 free inodes.

server1 `/var/tmp`: 324597903360 available bytes; 81.89% used; 112492596 free inodes.

server1 `/mnt/raid5`: 489209991168 available bytes; 97.76% used; 337724556 free inodes.
| server2 | True | [] | [] | reference_compatible=False |

server2 `/`: 40757616640 available bytes; 97.73% used; 110430388 free inodes.

server2 `/home`: 40757616640 available bytes; 97.73% used; 110430388 free inodes.

server2 `/tmp`: 40757616640 available bytes; 97.73% used; 110430388 free inodes.

server2 `/var/tmp`: 40757616640 available bytes; 97.73% used; 110430388 free inodes.

server2 `/mnt/raid5`: 523354005504 available bytes; 96.38% used; 445194591 free inodes.
| server3 | True | ['1'] | ['/tmp', '/var/tmp'] | reference_compatible=True |

server3 `/`: 291603095552 available bytes; 83.73% used; 114152011 free inodes.

server3 `/home`: 291603095552 available bytes; 83.73% used; 114152011 free inodes.

server3 `/data`: 23288242176 available bytes; 99.68% used; 225840286 free inodes.

server3 `/tmp`: 291603095552 available bytes; 83.73% used; 114152011 free inodes.

server3 `/var/tmp`: 291603095552 available bytes; 83.73% used; 114152011 free inodes.
| server4 | True | ['7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 105826668544 available bytes; 94.09% used; 114349383 free inodes.

server4 `/home`: 105826668544 available bytes; 94.09% used; 114349383 free inodes.

server4 `/data`: 252615852032 available bytes; 96.51% used; 225366770 free inodes.

server4 `/tmp`: 105826668544 available bytes; 94.09% used; 114349383 free inodes.

server4 `/var/tmp`: 105826668544 available bytes; 94.09% used; 114349383 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
