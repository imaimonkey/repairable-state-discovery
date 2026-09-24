# V2R cluster inventory

2026-09-24T23:42:30.102604+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | [] | ['/tmp', '/var/tmp'] |

server1 `/`: 319011827712 available bytes; 82.20% used; 112480761 free inodes.

server1 `/home`: 319011827712 available bytes; 82.20% used; 112480761 free inodes.

server1 `/tmp`: 319011827712 available bytes; 82.20% used; 112480761 free inodes.

server1 `/var/tmp`: 319011827712 available bytes; 82.20% used; 112480761 free inodes.

server1 `/mnt/raid5`: 415206739968 available bytes; 98.10% used; 337611774 free inodes.
| server2 | True | [] | [] |

server2 `/`: 23104794624 available bytes; 98.71% used; 110410812 free inodes.

server2 `/home`: 23104794624 available bytes; 98.71% used; 110410812 free inodes.

server2 `/tmp`: 23104794624 available bytes; 98.71% used; 110410812 free inodes.

server2 `/var/tmp`: 23104794624 available bytes; 98.71% used; 110410812 free inodes.

server2 `/mnt/raid5`: 486091739136 available bytes; 96.64% used; 445151071 free inodes.
| server3 | True | [] | [] |

server3 `/`: 84360699904 available bytes; 95.29% used; 114156079 free inodes.

server3 `/home`: 84360699904 available bytes; 95.29% used; 114156079 free inodes.

server3 `/data`: 147992825856 available bytes; 97.95% used; 225800685 free inodes.

server3 `/tmp`: 84360699904 available bytes; 95.29% used; 114156079 free inodes.

server3 `/var/tmp`: 84360699904 available bytes; 95.29% used; 114156079 free inodes.
| server4 | True | ['7'] | ['/tmp', '/var/tmp'] |

server4 `/`: 105799213056 available bytes; 94.10% used; 114348296 free inodes.

server4 `/home`: 105799213056 available bytes; 94.10% used; 114348296 free inodes.

server4 `/data`: 61048389632 available bytes; 99.16% used; 225129181 free inodes.

server4 `/tmp`: 105799213056 available bytes; 94.10% used; 114348296 free inodes.

server4 `/var/tmp`: 105799213056 available bytes; 94.10% used; 114348296 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
