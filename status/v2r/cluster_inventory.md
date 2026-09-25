# V2R cluster inventory

2026-09-25T00:52:59.135249+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | [] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 319088246784 available bytes; 82.20% used; 112480768 free inodes.

server1 `/home`: 319088246784 available bytes; 82.20% used; 112480768 free inodes.

server1 `/tmp`: 319088246784 available bytes; 82.20% used; 112480768 free inodes.

server1 `/var/tmp`: 319088246784 available bytes; 82.20% used; 112480768 free inodes.

server1 `/mnt/raid5`: 416813760512 available bytes; 98.09% used; 337617290 free inodes.
| server2 | True | [] | [] | reference_compatible=False |

server2 `/`: 23068332032 available bytes; 98.71% used; 110410767 free inodes.

server2 `/home`: 23068332032 available bytes; 98.71% used; 110410767 free inodes.

server2 `/tmp`: 23068332032 available bytes; 98.71% used; 110410767 free inodes.

server2 `/var/tmp`: 23068332032 available bytes; 98.71% used; 110410767 free inodes.

server2 `/mnt/raid5`: 501130235904 available bytes; 96.54% used; 445162690 free inodes.
| server3 | True | [] | [] | reference_compatible=True |

server3 `/`: 84356538368 available bytes; 95.29% used; 114156086 free inodes.

server3 `/home`: 84356538368 available bytes; 95.29% used; 114156086 free inodes.

server3 `/data`: 148509708288 available bytes; 97.95% used; 225813008 free inodes.

server3 `/tmp`: 84356538368 available bytes; 95.29% used; 114156086 free inodes.

server3 `/var/tmp`: 84356538368 available bytes; 95.29% used; 114156086 free inodes.
| server4 | True | ['0', '1', '4', '5', '7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 105788346368 available bytes; 94.10% used; 114348304 free inodes.

server4 `/home`: 105788346368 available bytes; 94.10% used; 114348304 free inodes.

server4 `/data`: 55624876032 available bytes; 99.23% used; 225031255 free inodes.

server4 `/tmp`: 105788346368 available bytes; 94.10% used; 114348304 free inodes.

server4 `/var/tmp`: 105788346368 available bytes; 94.10% used; 114348304 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
