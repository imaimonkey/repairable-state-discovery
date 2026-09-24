# V2R cluster inventory

2026-09-24T04:25:43.947156+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | ['7'] | ['/tmp', '/var/tmp'] |

server1 `/`: 324701732864 available bytes; 81.89% used; 112493215 free inodes.

server1 `/home`: 324701732864 available bytes; 81.89% used; 112493215 free inodes.

server1 `/tmp`: 324701732864 available bytes; 81.89% used; 112493215 free inodes.

server1 `/var/tmp`: 324701732864 available bytes; 81.89% used; 112493215 free inodes.

server1 `/mnt/raid5`: 440820535296 available bytes; 97.98% used; 337724698 free inodes.
| server2 | True | ['6'] | [] |

server2 `/`: 40785096704 available bytes; 97.72% used; 110430608 free inodes.

server2 `/home`: 40785096704 available bytes; 97.72% used; 110430608 free inodes.

server2 `/tmp`: 40785096704 available bytes; 97.72% used; 110430608 free inodes.

server2 `/var/tmp`: 40785096704 available bytes; 97.72% used; 110430608 free inodes.

server2 `/mnt/raid5`: 525498466304 available bytes; 96.37% used; 445195948 free inodes.
| server3 | True | [] | ['/tmp', '/var/tmp'] |

server3 `/`: 292003631104 available bytes; 83.71% used; 114176192 free inodes.

server3 `/home`: 292003631104 available bytes; 83.71% used; 114176192 free inodes.

server3 `/data`: 31676981248 available bytes; 99.56% used; 225841133 free inodes.

server3 `/tmp`: 292003631104 available bytes; 83.71% used; 114176192 free inodes.

server3 `/var/tmp`: 292003631104 available bytes; 83.71% used; 114176192 free inodes.
| server4 | True | ['7'] | ['/tmp', '/var/tmp'] |

server4 `/`: 105844682752 available bytes; 94.09% used; 114349421 free inodes.

server4 `/home`: 105844682752 available bytes; 94.09% used; 114349421 free inodes.

server4 `/data`: 256715247616 available bytes; 96.45% used; 225381768 free inodes.

server4 `/tmp`: 105844682752 available bytes; 94.09% used; 114349421 free inodes.

server4 `/var/tmp`: 105844682752 available bytes; 94.09% used; 114349421 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
