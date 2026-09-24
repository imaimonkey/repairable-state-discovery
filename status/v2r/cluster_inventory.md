# V2R cluster inventory

2026-09-24T23:53:17.118809+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | [] | ['/tmp', '/var/tmp'] |

server1 `/`: 319007232000 available bytes; 82.20% used; 112480782 free inodes.

server1 `/home`: 319007232000 available bytes; 82.20% used; 112480782 free inodes.

server1 `/tmp`: 319007232000 available bytes; 82.20% used; 112480782 free inodes.

server1 `/var/tmp`: 319007232000 available bytes; 82.20% used; 112480782 free inodes.

server1 `/mnt/raid5`: 415171121152 available bytes; 98.10% used; 337610502 free inodes.
| server2 | True | [] | [] |

server2 `/`: 23100850176 available bytes; 98.71% used; 110410785 free inodes.

server2 `/home`: 23100850176 available bytes; 98.71% used; 110410785 free inodes.

server2 `/tmp`: 23100850176 available bytes; 98.71% used; 110410785 free inodes.

server2 `/var/tmp`: 23100850176 available bytes; 98.71% used; 110410785 free inodes.

server2 `/mnt/raid5`: 485767577600 available bytes; 96.64% used; 445150599 free inodes.
| server3 | True | [] | [] |

server3 `/`: 84363608064 available bytes; 95.29% used; 114156079 free inodes.

server3 `/home`: 84363608064 available bytes; 95.29% used; 114156079 free inodes.

server3 `/data`: 147807531008 available bytes; 97.96% used; 225800464 free inodes.

server3 `/tmp`: 84363608064 available bytes; 95.29% used; 114156079 free inodes.

server3 `/var/tmp`: 84363608064 available bytes; 95.29% used; 114156079 free inodes.
| server4 | True | ['7'] | ['/tmp', '/var/tmp'] |

server4 `/`: 105798930432 available bytes; 94.10% used; 114348296 free inodes.

server4 `/home`: 105798930432 available bytes; 94.10% used; 114348296 free inodes.

server4 `/data`: 60865757184 available bytes; 99.16% used; 225113110 free inodes.

server4 `/tmp`: 105798930432 available bytes; 94.10% used; 114348296 free inodes.

server4 `/var/tmp`: 105798930432 available bytes; 94.10% used; 114348296 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
