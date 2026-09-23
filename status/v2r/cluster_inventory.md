# V2R cluster inventory

2026-09-23T23:07:03.911073+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | ['6', '7'] | ['/tmp', '/var/tmp', '/mnt/raid5'] | reference_compatible=False |

server1 `/`: 325741121536 available bytes; 81.83% used; 112501692 free inodes.

server1 `/home`: 325741121536 available bytes; 81.83% used; 112501692 free inodes.

server1 `/tmp`: 325741121536 available bytes; 81.83% used; 112501692 free inodes.

server1 `/var/tmp`: 325741121536 available bytes; 81.83% used; 112501692 free inodes.

server1 `/mnt/raid5`: 1387998208000 available bytes; 93.63% used; 337739785 free inodes.
| server2 | True | [] | [] | reference_compatible=False |

server2 `/`: 41059422208 available bytes; 97.71% used; 110432610 free inodes.

server2 `/home`: 41059422208 available bytes; 97.71% used; 110432610 free inodes.

server2 `/tmp`: 41059422208 available bytes; 97.71% used; 110432610 free inodes.

server2 `/var/tmp`: 41059422208 available bytes; 97.71% used; 110432610 free inodes.

server2 `/mnt/raid5`: 535180451840 available bytes; 96.30% used; 445205641 free inodes.
| server3 | True | ['3'] | ['/tmp', '/var/tmp'] | reference_compatible=True |

server3 `/`: 292608901120 available bytes; 83.67% used; 114198847 free inodes.

server3 `/home`: 292608901120 available bytes; 83.67% used; 114198847 free inodes.

server3 `/data`: 82345615360 available bytes; 98.86% used; 225846523 free inodes.

server3 `/tmp`: 292608901120 available bytes; 83.67% used; 114198847 free inodes.

server3 `/var/tmp`: 292608901120 available bytes; 83.67% used; 114198847 free inodes.
| server4 | True | ['3', '6', '7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 106281336832 available bytes; 94.07% used; 114353199 free inodes.

server4 `/home`: 106281336832 available bytes; 94.07% used; 114353199 free inodes.

server4 `/data`: 300055932928 available bytes; 95.85% used; 225430786 free inodes.

server4 `/tmp`: 106281336832 available bytes; 94.07% used; 114353199 free inodes.

server4 `/var/tmp`: 106281336832 available bytes; 94.07% used; 114353199 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
