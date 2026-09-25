# V2R cluster inventory

2026-09-25T06:33:44.885630+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | [] | ['/tmp', '/var/tmp'] |

server1 `/`: 318873477120 available bytes; 82.21% used; 112480350 free inodes.

server1 `/home`: 318873477120 available bytes; 82.21% used; 112480350 free inodes.

server1 `/tmp`: 318873477120 available bytes; 82.21% used; 112480350 free inodes.

server1 `/var/tmp`: 318873477120 available bytes; 82.21% used; 112480350 free inodes.

server1 `/mnt/raid5`: 399805755392 available bytes; 98.17% used; 337561419 free inodes.
| server2 | True | [] | [] |

server2 `/`: 22888378368 available bytes; 98.72% used; 110410514 free inodes.

server2 `/home`: 22888378368 available bytes; 98.72% used; 110410514 free inodes.

server2 `/tmp`: 22888378368 available bytes; 98.72% used; 110410514 free inodes.

server2 `/var/tmp`: 22888378368 available bytes; 98.72% used; 110410514 free inodes.

server2 `/mnt/raid5`: 370428104704 available bytes; 97.44% used; 445099396 free inodes.
| server3 | True | [] | [] |

server3 `/`: 84449886208 available bytes; 95.29% used; 114156031 free inodes.

server3 `/home`: 84449886208 available bytes; 95.29% used; 114156031 free inodes.

server3 `/data`: 142536605696 available bytes; 98.03% used; 225813737 free inodes.

server3 `/tmp`: 84449886208 available bytes; 95.29% used; 114156031 free inodes.

server3 `/var/tmp`: 84449886208 available bytes; 95.29% used; 114156031 free inodes.
| server4 | True | ['3'] | ['/tmp', '/var/tmp'] |

server4 `/`: 105648054272 available bytes; 94.10% used; 114350388 free inodes.

server4 `/home`: 105648054272 available bytes; 94.10% used; 114350388 free inodes.

server4 `/data`: 252668489728 available bytes; 96.51% used; 225020082 free inodes.

server4 `/tmp`: 105648054272 available bytes; 94.10% used; 114350388 free inodes.

server4 `/var/tmp`: 105648054272 available bytes; 94.10% used; 114350388 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
