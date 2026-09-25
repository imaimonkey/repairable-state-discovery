# V2R cluster inventory

2026-09-25T05:27:32.890034+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | [] | ['/tmp', '/var/tmp'] |

server1 `/`: 318871371776 available bytes; 82.21% used; 112480348 free inodes.

server1 `/home`: 318871371776 available bytes; 82.21% used; 112480348 free inodes.

server1 `/tmp`: 318871371776 available bytes; 82.21% used; 112480348 free inodes.

server1 `/var/tmp`: 318871371776 available bytes; 82.21% used; 112480348 free inodes.

server1 `/mnt/raid5`: 408498196480 available bytes; 98.13% used; 337568576 free inodes.
| server2 | True | [] | [] |

server2 `/`: 22922424320 available bytes; 98.72% used; 110410451 free inodes.

server2 `/home`: 22922424320 available bytes; 98.72% used; 110410451 free inodes.

server2 `/tmp`: 22922424320 available bytes; 98.72% used; 110410451 free inodes.

server2 `/var/tmp`: 22922424320 available bytes; 98.72% used; 110410451 free inodes.

server2 `/mnt/raid5`: 461261500416 available bytes; 96.81% used; 445108258 free inodes.
| server3 | True | [] | [] |

server3 `/`: 84316651520 available bytes; 95.29% used; 114156052 free inodes.

server3 `/home`: 84316651520 available bytes; 95.29% used; 114156052 free inodes.

server3 `/data`: 142775660544 available bytes; 98.03% used; 225814851 free inodes.

server3 `/tmp`: 84316651520 available bytes; 95.29% used; 114156052 free inodes.

server3 `/var/tmp`: 84316651520 available bytes; 95.29% used; 114156052 free inodes.
| server4 | True | ['6', '7'] | ['/tmp', '/var/tmp'] |

server4 `/`: 105658511360 available bytes; 94.10% used; 114350397 free inodes.

server4 `/home`: 105658511360 available bytes; 94.10% used; 114350397 free inodes.

server4 `/data`: 26412171264 available bytes; 99.63% used; 224968469 free inodes.

server4 `/tmp`: 105658511360 available bytes; 94.10% used; 114350397 free inodes.

server4 `/var/tmp`: 105658511360 available bytes; 94.10% used; 114350397 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
