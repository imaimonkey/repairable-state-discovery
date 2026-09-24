# V2R cluster inventory

2026-09-24T23:37:53.745553+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | [] | ['/tmp', '/var/tmp'] |

server1 `/`: 319011753984 available bytes; 82.20% used; 112480775 free inodes.

server1 `/home`: 319011753984 available bytes; 82.20% used; 112480775 free inodes.

server1 `/tmp`: 319011753984 available bytes; 82.20% used; 112480775 free inodes.

server1 `/var/tmp`: 319011753984 available bytes; 82.20% used; 112480775 free inodes.

server1 `/mnt/raid5`: 396285366272 available bytes; 98.18% used; 337612313 free inodes.
| server2 | True | [] | [] |

server2 `/`: 23112679424 available bytes; 98.71% used; 110410804 free inodes.

server2 `/home`: 23112679424 available bytes; 98.71% used; 110410804 free inodes.

server2 `/tmp`: 23112679424 available bytes; 98.71% used; 110410804 free inodes.

server2 `/var/tmp`: 23112679424 available bytes; 98.71% used; 110410804 free inodes.

server2 `/mnt/raid5`: 486164312064 available bytes; 96.64% used; 445150941 free inodes.
| server3 | True | [] | [] |

server3 `/`: 84361609216 available bytes; 95.29% used; 114156085 free inodes.

server3 `/home`: 84361609216 available bytes; 95.29% used; 114156085 free inodes.

server3 `/data`: 148071927808 available bytes; 97.95% used; 225800759 free inodes.

server3 `/tmp`: 84361609216 available bytes; 95.29% used; 114156085 free inodes.

server3 `/var/tmp`: 84361609216 available bytes; 95.29% used; 114156085 free inodes.
| server4 | True | ['7'] | ['/tmp', '/var/tmp'] |

server4 `/`: 105799368704 available bytes; 94.10% used; 114348296 free inodes.

server4 `/home`: 105799368704 available bytes; 94.10% used; 114348296 free inodes.

server4 `/data`: 61128433664 available bytes; 99.16% used; 225135917 free inodes.

server4 `/tmp`: 105799368704 available bytes; 94.10% used; 114348296 free inodes.

server4 `/var/tmp`: 105799368704 available bytes; 94.10% used; 114348296 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
