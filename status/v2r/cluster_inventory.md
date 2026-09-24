# V2R cluster inventory

2026-09-24T23:25:32.246477+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | [] | ['/tmp', '/var/tmp'] |

server1 `/`: 319014477824 available bytes; 82.20% used; 112480781 free inodes.

server1 `/home`: 319014477824 available bytes; 82.20% used; 112480781 free inodes.

server1 `/tmp`: 319014477824 available bytes; 82.20% used; 112480781 free inodes.

server1 `/var/tmp`: 319014477824 available bytes; 82.20% used; 112480781 free inodes.

server1 `/mnt/raid5`: 415242399744 available bytes; 98.10% used; 337613748 free inodes.
| server2 | True | [] | [] |

server2 `/`: 23112220672 available bytes; 98.71% used; 110410804 free inodes.

server2 `/home`: 23112220672 available bytes; 98.71% used; 110410804 free inodes.

server2 `/tmp`: 23112220672 available bytes; 98.71% used; 110410804 free inodes.

server2 `/var/tmp`: 23112220672 available bytes; 98.71% used; 110410804 free inodes.

server2 `/mnt/raid5`: 486553321472 available bytes; 96.64% used; 445151578 free inodes.
| server3 | True | [] | [] |

server3 `/`: 84369833984 available bytes; 95.29% used; 114156075 free inodes.

server3 `/home`: 84369833984 available bytes; 95.29% used; 114156075 free inodes.

server3 `/data`: 148356542464 available bytes; 97.95% used; 225801001 free inodes.

server3 `/tmp`: 84369833984 available bytes; 95.29% used; 114156075 free inodes.

server3 `/var/tmp`: 84369833984 available bytes; 95.29% used; 114156075 free inodes.
| server4 | True | ['7'] | ['/tmp', '/var/tmp'] |

server4 `/`: 105799704576 available bytes; 94.10% used; 114348305 free inodes.

server4 `/home`: 105799704576 available bytes; 94.10% used; 114348305 free inodes.

server4 `/data`: 61416333312 available bytes; 99.15% used; 225153903 free inodes.

server4 `/tmp`: 105799704576 available bytes; 94.10% used; 114348305 free inodes.

server4 `/var/tmp`: 105799704576 available bytes; 94.10% used; 114348305 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
