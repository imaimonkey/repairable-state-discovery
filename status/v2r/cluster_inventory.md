# V2R cluster inventory

2026-09-24T00:17:01.953143+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | [] | ['/tmp', '/var/tmp', '/mnt/raid5'] |

server1 `/`: 325559824384 available bytes; 81.84% used; 112500732 free inodes.

server1 `/home`: 325559824384 available bytes; 81.84% used; 112500732 free inodes.

server1 `/tmp`: 325559824384 available bytes; 81.84% used; 112500732 free inodes.

server1 `/var/tmp`: 325559824384 available bytes; 81.84% used; 112500732 free inodes.

server1 `/mnt/raid5`: 1196671754240 available bytes; 94.51% used; 337735266 free inodes.
| server2 | True | [] | [] |

server2 `/`: 41008914432 available bytes; 97.71% used; 110432395 free inodes.

server2 `/home`: 41008914432 available bytes; 97.71% used; 110432395 free inodes.

server2 `/tmp`: 41008914432 available bytes; 97.71% used; 110432395 free inodes.

server2 `/var/tmp`: 41008914432 available bytes; 97.71% used; 110432395 free inodes.

server2 `/mnt/raid5`: 533205094400 available bytes; 96.32% used; 445203984 free inodes.
| server3 | True | [] | ['/tmp', '/var/tmp'] |

server3 `/`: 292594683904 available bytes; 83.67% used; 114206619 free inodes.

server3 `/home`: 292594683904 available bytes; 83.67% used; 114206619 free inodes.

server3 `/data`: 82249977856 available bytes; 98.86% used; 225844456 free inodes.

server3 `/tmp`: 292594683904 available bytes; 83.67% used; 114206619 free inodes.

server3 `/var/tmp`: 292594683904 available bytes; 83.67% used; 114206619 free inodes.
| server4 | True | ['1', '3', '6', '7'] | ['/tmp', '/var/tmp'] |

server4 `/`: 106102177792 available bytes; 94.08% used; 114350691 free inodes.

server4 `/home`: 106102177792 available bytes; 94.08% used; 114350691 free inodes.

server4 `/data`: 292911845376 available bytes; 95.95% used; 225414568 free inodes.

server4 `/tmp`: 106102177792 available bytes; 94.08% used; 114350691 free inodes.

server4 `/var/tmp`: 106102177792 available bytes; 94.08% used; 114350691 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
