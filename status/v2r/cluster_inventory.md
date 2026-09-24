# V2R cluster inventory

2026-09-24T17:35:18.635360+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | ['7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 324004409344 available bytes; 81.92% used; 112481448 free inodes.

server1 `/home`: 324004409344 available bytes; 81.92% used; 112481448 free inodes.

server1 `/tmp`: 324004409344 available bytes; 81.92% used; 112481448 free inodes.

server1 `/var/tmp`: 324004409344 available bytes; 81.92% used; 112481448 free inodes.

server1 `/mnt/raid5`: 416440168448 available bytes; 98.09% used; 337645770 free inodes.
| server2 | True | [] | [] | reference_compatible=False |

server2 `/`: 56915464192 available bytes; 96.82% used; 110412465 free inodes.

server2 `/home`: 56915464192 available bytes; 96.82% used; 110412465 free inodes.

server2 `/tmp`: 56915464192 available bytes; 96.82% used; 110412465 free inodes.

server2 `/var/tmp`: 56915464192 available bytes; 96.82% used; 110412465 free inodes.

server2 `/mnt/raid5`: 498641907712 available bytes; 96.55% used; 445162424 free inodes.
| server3 | True | [] | [] | reference_compatible=True |

server3 `/`: 84407824384 available bytes; 95.29% used; 114156150 free inodes.

server3 `/home`: 84407824384 available bytes; 95.29% used; 114156150 free inodes.

server3 `/data`: 158898974720 available bytes; 97.80% used; 225786744 free inodes.

server3 `/tmp`: 84407824384 available bytes; 95.29% used; 114156150 free inodes.

server3 `/var/tmp`: 84407824384 available bytes; 95.29% used; 114156150 free inodes.
| server4 | True | [] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 105681264640 available bytes; 94.10% used; 114348559 free inodes.

server4 `/home`: 105681264640 available bytes; 94.10% used; 114348559 free inodes.

server4 `/data`: 89056657408 available bytes; 98.77% used; 225253875 free inodes.

server4 `/tmp`: 105681264640 available bytes; 94.10% used; 114348559 free inodes.

server4 `/var/tmp`: 105681264640 available bytes; 94.10% used; 114348559 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
