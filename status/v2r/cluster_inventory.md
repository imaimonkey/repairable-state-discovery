# V2R cluster inventory

2026-09-26T14:45:46.107473+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | ['3', '4', '5', '6', '7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 318123339776 available bytes; 82.25% used; 112474358 free inodes.

server1 `/home`: 318123339776 available bytes; 82.25% used; 112474358 free inodes.

server1 `/tmp`: 318123339776 available bytes; 82.25% used; 112474358 free inodes.

server1 `/var/tmp`: 318123339776 available bytes; 82.25% used; 112474358 free inodes.

server1 `/mnt/raid5`: 671830822912 available bytes; 96.92% used; 337531898 free inodes.
| server2 | True | ['7'] | [] | reference_compatible=False |

server2 `/`: 14054387712 available bytes; 99.22% used; 110378814 free inodes.

server2 `/home`: 14054387712 available bytes; 99.22% used; 110378814 free inodes.

server2 `/tmp`: 14054387712 available bytes; 99.22% used; 110378814 free inodes.

server2 `/var/tmp`: 14054387712 available bytes; 99.22% used; 110378814 free inodes.

server2 `/mnt/raid5`: 634497040384 available bytes; 95.62% used; 444974288 free inodes.
| server3 | True | [] | [] | reference_compatible=True |

server3 `/`: 82627776512 available bytes; 95.39% used; 114110775 free inodes.

server3 `/home`: 82627776512 available bytes; 95.39% used; 114110775 free inodes.

server3 `/data`: 1346875019264 available bytes; 81.39% used; 225805048 free inodes.

server3 `/tmp`: 82627776512 available bytes; 95.39% used; 114110775 free inodes.

server3 `/var/tmp`: 82627776512 available bytes; 95.39% used; 114110775 free inodes.
| server4 | True | ['3', '5', '7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 105886543872 available bytes; 94.09% used; 114347840 free inodes.

server4 `/home`: 105886543872 available bytes; 94.09% used; 114347840 free inodes.

server4 `/data`: 410991271936 available bytes; 94.32% used; 224826428 free inodes.

server4 `/tmp`: 105886543872 available bytes; 94.09% used; 114347840 free inodes.

server4 `/var/tmp`: 105886543872 available bytes; 94.09% used; 114347840 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
