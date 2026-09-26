# V2R cluster inventory

2026-09-26T10:08:15.909117+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | ['1', '4', '5', '6', '7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 318609809408 available bytes; 82.23% used; 112475052 free inodes.

server1 `/home`: 318609809408 available bytes; 82.23% used; 112475052 free inodes.

server1 `/tmp`: 318609809408 available bytes; 82.23% used; 112475052 free inodes.

server1 `/var/tmp`: 318609809408 available bytes; 82.23% used; 112475052 free inodes.

server1 `/mnt/raid5`: 218883895296 available bytes; 99.00% used; 337538470 free inodes.
| server2 | True | [] | [] | reference_compatible=False |

server2 `/`: 22297763840 available bytes; 98.76% used; 110402879 free inodes.

server2 `/home`: 22297763840 available bytes; 98.76% used; 110402879 free inodes.

server2 `/tmp`: 22297763840 available bytes; 98.76% used; 110402879 free inodes.

server2 `/var/tmp`: 22297763840 available bytes; 98.76% used; 110402879 free inodes.

server2 `/mnt/raid5`: 252262170624 available bytes; 98.26% used; 445021456 free inodes.
| server3 | True | [] | [] | reference_compatible=True |

server3 `/`: 82657525760 available bytes; 95.39% used; 114110817 free inodes.

server3 `/home`: 82657525760 available bytes; 95.39% used; 114110817 free inodes.

server3 `/data`: 123588087808 available bytes; 98.29% used; 225827149 free inodes.

server3 `/tmp`: 82657525760 available bytes; 95.39% used; 114110817 free inodes.

server3 `/var/tmp`: 82657525760 available bytes; 95.39% used; 114110817 free inodes.
| server4 | True | ['3', '7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 105931026432 available bytes; 94.09% used; 114348027 free inodes.

server4 `/home`: 105931026432 available bytes; 94.09% used; 114348027 free inodes.

server4 `/data`: 89218367488 available bytes; 98.77% used; 224882047 free inodes.

server4 `/tmp`: 105931026432 available bytes; 94.09% used; 114348027 free inodes.

server4 `/var/tmp`: 105931026432 available bytes; 94.09% used; 114348027 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
