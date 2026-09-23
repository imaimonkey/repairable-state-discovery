# V2R cluster inventory

2026-09-23T14:18:28.361717+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | False | [] | [] |
| server2 | True | ['7'] | [] |

server2 `/`: 41461985280 available bytes; 97.69% used; 110435208 free inodes.

server2 `/home`: 41461985280 available bytes; 97.69% used; 110435208 free inodes.

server2 `/tmp`: 41461985280 available bytes; 97.69% used; 110435208 free inodes.

server2 `/var/tmp`: 41461985280 available bytes; 97.69% used; 110435208 free inodes.

server2 `/mnt/raid5`: 553440587776 available bytes; 96.18% used; 445225622 free inodes.
| server3 | True | ['0'] | ['/tmp', '/var/tmp'] |

server3 `/`: 378049667072 available bytes; 78.90% used; 114315914 free inodes.

server3 `/home`: 378049667072 available bytes; 78.90% used; 114315914 free inodes.

server3 `/data`: 133305856000 available bytes; 98.16% used; 225844144 free inodes.

server3 `/tmp`: 378049667072 available bytes; 78.90% used; 114315914 free inodes.

server3 `/var/tmp`: 378049667072 available bytes; 78.90% used; 114315914 free inodes.
| server4 | True | [] | ['/tmp', '/var/tmp'] |

server4 `/`: 111676108800 available bytes; 93.77% used; 114378461 free inodes.

server4 `/home`: 111676108800 available bytes; 93.77% used; 114378461 free inodes.

server4 `/data`: 70395777024 available bytes; 99.03% used; 225533662 free inodes.

server4 `/tmp`: 111676108800 available bytes; 93.77% used; 114378461 free inodes.

server4 `/var/tmp`: 111676108800 available bytes; 93.77% used; 114378461 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
