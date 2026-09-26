# V2R cluster inventory

2026-09-26T12:51:29.219298+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | ['0', '1', '2', '3', '4', '5', '6', '7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 318166183936 available bytes; 82.25% used; 112474507 free inodes.

server1 `/home`: 318166183936 available bytes; 82.25% used; 112474507 free inodes.

server1 `/tmp`: 318166183936 available bytes; 82.25% used; 112474507 free inodes.

server1 `/var/tmp`: 318166183936 available bytes; 82.25% used; 112474507 free inodes.

server1 `/mnt/raid5`: 679644094464 available bytes; 96.88% used; 337537741 free inodes.
| server2 | True | ['2', '7'] | [] | reference_compatible=False |

server2 `/`: 19737698304 available bytes; 98.90% used; 110381958 free inodes.

server2 `/home`: 19737698304 available bytes; 98.90% used; 110381958 free inodes.

server2 `/tmp`: 19737698304 available bytes; 98.90% used; 110381958 free inodes.

server2 `/var/tmp`: 19737698304 available bytes; 98.90% used; 110381958 free inodes.

server2 `/mnt/raid5`: 637901881344 available bytes; 95.59% used; 444977863 free inodes.
| server3 | True | [] | [] | reference_compatible=True |

server3 `/`: 82648440832 available bytes; 95.39% used; 114110819 free inodes.

server3 `/home`: 82648440832 available bytes; 95.39% used; 114110819 free inodes.

server3 `/data`: 1347688972288 available bytes; 81.37% used; 225823463 free inodes.

server3 `/tmp`: 82648440832 available bytes; 95.39% used; 114110819 free inodes.

server3 `/var/tmp`: 82648440832 available bytes; 95.39% used; 114110819 free inodes.
| server4 | True | ['0', '3', '5', '7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 105899257856 available bytes; 94.09% used; 114347938 free inodes.

server4 `/home`: 105899257856 available bytes; 94.09% used; 114347938 free inodes.

server4 `/data`: 413545369600 available bytes; 94.28% used; 224847085 free inodes.

server4 `/tmp`: 105899257856 available bytes; 94.09% used; 114347938 free inodes.

server4 `/var/tmp`: 105899257856 available bytes; 94.09% used; 114347938 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
