# V2R cluster inventory

2026-09-25T10:30:15.582399+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | [] | ['/tmp', '/var/tmp'] |

server1 `/`: 318919323648 available bytes; 82.21% used; 112479892 free inodes.

server1 `/home`: 318919323648 available bytes; 82.21% used; 112479892 free inodes.

server1 `/tmp`: 318919323648 available bytes; 82.21% used; 112479892 free inodes.

server1 `/var/tmp`: 318919323648 available bytes; 82.21% used; 112479892 free inodes.

server1 `/mnt/raid5`: 364838604800 available bytes; 98.33% used; 337555268 free inodes.
| server2 | True | ['3', '5', '6'] | [] |

server2 `/`: 22826258432 available bytes; 98.73% used; 110410492 free inodes.

server2 `/home`: 22826258432 available bytes; 98.73% used; 110410492 free inodes.

server2 `/tmp`: 22826258432 available bytes; 98.73% used; 110410492 free inodes.

server2 `/var/tmp`: 22826258432 available bytes; 98.73% used; 110410492 free inodes.

server2 `/mnt/raid5`: 316215586816 available bytes; 97.82% used; 445090101 free inodes.
| server3 | True | [] | [] |

server3 `/`: 84417859584 available bytes; 95.29% used; 114156047 free inodes.

server3 `/home`: 84417859584 available bytes; 95.29% used; 114156047 free inodes.

server3 `/data`: 142019567616 available bytes; 98.04% used; 225815759 free inodes.

server3 `/tmp`: 84417859584 available bytes; 95.29% used; 114156047 free inodes.

server3 `/var/tmp`: 84417859584 available bytes; 95.29% used; 114156047 free inodes.
| server4 | True | [] | ['/tmp', '/var/tmp'] |

server4 `/`: 105613352960 available bytes; 94.11% used; 114350251 free inodes.

server4 `/home`: 105613352960 available bytes; 94.11% used; 114350251 free inodes.

server4 `/data`: 238446493696 available bytes; 96.70% used; 224987582 free inodes.

server4 `/tmp`: 105613352960 available bytes; 94.11% used; 114350251 free inodes.

server4 `/var/tmp`: 105613352960 available bytes; 94.11% used; 114350251 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
