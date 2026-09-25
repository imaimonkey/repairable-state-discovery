# V2R cluster inventory

2026-09-25T06:35:17.805955+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | [] | ['/tmp', '/var/tmp'] |

server1 `/`: 318873264128 available bytes; 82.21% used; 112480354 free inodes.

server1 `/home`: 318873264128 available bytes; 82.21% used; 112480354 free inodes.

server1 `/tmp`: 318873264128 available bytes; 82.21% used; 112480354 free inodes.

server1 `/var/tmp`: 318873264128 available bytes; 82.21% used; 112480354 free inodes.

server1 `/mnt/raid5`: 399805689856 available bytes; 98.17% used; 337561420 free inodes.
| server2 | True | [] | [] |

server2 `/`: 22888067072 available bytes; 98.72% used; 110410514 free inodes.

server2 `/home`: 22888067072 available bytes; 98.72% used; 110410514 free inodes.

server2 `/tmp`: 22888067072 available bytes; 98.72% used; 110410514 free inodes.

server2 `/var/tmp`: 22888067072 available bytes; 98.72% used; 110410514 free inodes.

server2 `/mnt/raid5`: 369842638848 available bytes; 97.44% used; 445099215 free inodes.
| server3 | True | [] | [] |

server3 `/`: 84449427456 available bytes; 95.29% used; 114156031 free inodes.

server3 `/home`: 84449427456 available bytes; 95.29% used; 114156031 free inodes.

server3 `/data`: 142535081984 available bytes; 98.03% used; 225813702 free inodes.

server3 `/tmp`: 84449427456 available bytes; 95.29% used; 114156031 free inodes.

server3 `/var/tmp`: 84449427456 available bytes; 95.29% used; 114156031 free inodes.
| server4 | True | ['3'] | ['/tmp', '/var/tmp'] |

server4 `/`: 105639628800 available bytes; 94.10% used; 114350387 free inodes.

server4 `/home`: 105639628800 available bytes; 94.10% used; 114350387 free inodes.

server4 `/data`: 251915374592 available bytes; 96.52% used; 225019822 free inodes.

server4 `/tmp`: 105639628800 available bytes; 94.10% used; 114350387 free inodes.

server4 `/var/tmp`: 105639628800 available bytes; 94.10% used; 114350387 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
