# V2R cluster inventory

2026-09-24T17:24:30.093916+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | ['7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 324005744640 available bytes; 81.92% used; 112481437 free inodes.

server1 `/home`: 324005744640 available bytes; 81.92% used; 112481437 free inodes.

server1 `/tmp`: 324005744640 available bytes; 81.92% used; 112481437 free inodes.

server1 `/var/tmp`: 324005744640 available bytes; 81.92% used; 112481437 free inodes.

server1 `/mnt/raid5`: 416456630272 available bytes; 98.09% used; 337647036 free inodes.
| server2 | True | ['7'] | [] | reference_compatible=False |

server2 `/`: 57042079744 available bytes; 96.82% used; 110417753 free inodes.

server2 `/home`: 57042079744 available bytes; 96.82% used; 110417753 free inodes.

server2 `/tmp`: 57042079744 available bytes; 96.82% used; 110417753 free inodes.

server2 `/var/tmp`: 57042079744 available bytes; 96.82% used; 110417753 free inodes.

server2 `/mnt/raid5`: 498983981056 available bytes; 96.55% used; 445162684 free inodes.
| server3 | True | [] | [] | reference_compatible=True |

server3 `/`: 84407918592 available bytes; 95.29% used; 114156148 free inodes.

server3 `/home`: 84407918592 available bytes; 95.29% used; 114156148 free inodes.

server3 `/data`: 158975025152 available bytes; 97.80% used; 225786937 free inodes.

server3 `/tmp`: 84407918592 available bytes; 95.29% used; 114156148 free inodes.

server3 `/var/tmp`: 84407918592 available bytes; 95.29% used; 114156148 free inodes.
| server4 | True | [] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 105681719296 available bytes; 94.10% used; 114348569 free inodes.

server4 `/home`: 105681719296 available bytes; 94.10% used; 114348569 free inodes.

server4 `/data`: 89075400704 available bytes; 98.77% used; 225254170 free inodes.

server4 `/tmp`: 105681719296 available bytes; 94.10% used; 114348569 free inodes.

server4 `/var/tmp`: 105681719296 available bytes; 94.10% used; 114348569 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
