# V2R cluster inventory

2026-09-25T00:02:37.511170+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | [] | ['/tmp', '/var/tmp'] |

server1 `/`: 319089684480 available bytes; 82.20% used; 112480778 free inodes.

server1 `/home`: 319089684480 available bytes; 82.20% used; 112480778 free inodes.

server1 `/tmp`: 319089684480 available bytes; 82.20% used; 112480778 free inodes.

server1 `/var/tmp`: 319089684480 available bytes; 82.20% used; 112480778 free inodes.

server1 `/mnt/raid5`: 416904863744 available bytes; 98.09% used; 337623069 free inodes.
| server2 | True | [] | [] |

server2 `/`: 23092092928 available bytes; 98.71% used; 110410784 free inodes.

server2 `/home`: 23092092928 available bytes; 98.71% used; 110410784 free inodes.

server2 `/tmp`: 23092092928 available bytes; 98.71% used; 110410784 free inodes.

server2 `/var/tmp`: 23092092928 available bytes; 98.71% used; 110410784 free inodes.

server2 `/mnt/raid5`: 487337275392 available bytes; 96.63% used; 445163852 free inodes.
| server3 | True | [] | [] |

server3 `/`: 84352851968 available bytes; 95.29% used; 114156084 free inodes.

server3 `/home`: 84352851968 available bytes; 95.29% used; 114156084 free inodes.

server3 `/data`: 149427994624 available bytes; 97.93% used; 225813947 free inodes.

server3 `/tmp`: 84352851968 available bytes; 95.29% used; 114156084 free inodes.

server3 `/var/tmp`: 84352851968 available bytes; 95.29% used; 114156084 free inodes.
| server4 | True | ['0', '5', '7'] | ['/tmp', '/var/tmp'] |

server4 `/`: 105798676480 available bytes; 94.10% used; 114348301 free inodes.

server4 `/home`: 105798676480 available bytes; 94.10% used; 114348301 free inodes.

server4 `/data`: 60449316864 available bytes; 99.16% used; 225098587 free inodes.

server4 `/tmp`: 105798676480 available bytes; 94.10% used; 114348301 free inodes.

server4 `/var/tmp`: 105798676480 available bytes; 94.10% used; 114348301 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
