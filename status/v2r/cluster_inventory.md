# V2R cluster inventory

2026-09-24T16:48:45.123130+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | ['7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 324024520704 available bytes; 81.92% used; 112481460 free inodes.

server1 `/home`: 324024520704 available bytes; 81.92% used; 112481460 free inodes.

server1 `/tmp`: 324024520704 available bytes; 81.92% used; 112481460 free inodes.

server1 `/var/tmp`: 324024520704 available bytes; 81.92% used; 112481460 free inodes.

server1 `/mnt/raid5`: 416529702912 available bytes; 98.09% used; 337651196 free inodes.
| server2 | True | ['7'] | [] | reference_compatible=False |

server2 `/`: 57082105856 available bytes; 96.82% used; 110418146 free inodes.

server2 `/home`: 57082105856 available bytes; 96.82% used; 110418146 free inodes.

server2 `/tmp`: 57082105856 available bytes; 96.82% used; 110418146 free inodes.

server2 `/var/tmp`: 57082105856 available bytes; 96.82% used; 110418146 free inodes.

server2 `/mnt/raid5`: 500366491648 available bytes; 96.54% used; 445163893 free inodes.
| server3 | True | [] | [] | reference_compatible=True |

server3 `/`: 84416806912 available bytes; 95.29% used; 114156148 free inodes.

server3 `/home`: 84416806912 available bytes; 95.29% used; 114156148 free inodes.

server3 `/data`: 159222190080 available bytes; 97.80% used; 225787605 free inodes.

server3 `/tmp`: 84416806912 available bytes; 95.29% used; 114156148 free inodes.

server3 `/var/tmp`: 84416806912 available bytes; 95.29% used; 114156148 free inodes.
| server4 | True | [] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 105682898944 available bytes; 94.10% used; 114348575 free inodes.

server4 `/home`: 105682898944 available bytes; 94.10% used; 114348575 free inodes.

server4 `/data`: 89222549504 available bytes; 98.77% used; 225255317 free inodes.

server4 `/tmp`: 105682898944 available bytes; 94.10% used; 114348575 free inodes.

server4 `/var/tmp`: 105682898944 available bytes; 94.10% used; 114348575 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
