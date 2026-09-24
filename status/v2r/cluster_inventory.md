# V2R cluster inventory

2026-09-24T23:51:44.186217+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | [] | ['/tmp', '/var/tmp'] |

server1 `/`: 319007932416 available bytes; 82.20% used; 112480779 free inodes.

server1 `/home`: 319007932416 available bytes; 82.20% used; 112480779 free inodes.

server1 `/tmp`: 319007932416 available bytes; 82.20% used; 112480779 free inodes.

server1 `/var/tmp`: 319007932416 available bytes; 82.20% used; 112480779 free inodes.

server1 `/mnt/raid5`: 415177089024 available bytes; 98.10% used; 337610689 free inodes.
| server2 | True | [] | [] |

server2 `/`: 23100366848 available bytes; 98.71% used; 110410799 free inodes.

server2 `/home`: 23100366848 available bytes; 98.71% used; 110410799 free inodes.

server2 `/tmp`: 23100366848 available bytes; 98.71% used; 110410799 free inodes.

server2 `/var/tmp`: 23100366848 available bytes; 98.71% used; 110410799 free inodes.

server2 `/mnt/raid5`: 485808095232 available bytes; 96.64% used; 445150639 free inodes.
| server3 | True | [] | [] |

server3 `/`: 84363878400 available bytes; 95.29% used; 114156079 free inodes.

server3 `/home`: 84363878400 available bytes; 95.29% used; 114156079 free inodes.

server3 `/data`: 147839336448 available bytes; 97.96% used; 225800500 free inodes.

server3 `/tmp`: 84363878400 available bytes; 95.29% used; 114156079 free inodes.

server3 `/var/tmp`: 84363878400 available bytes; 95.29% used; 114156079 free inodes.
| server4 | True | ['7'] | ['/tmp', '/var/tmp'] |

server4 `/`: 105798975488 available bytes; 94.10% used; 114348296 free inodes.

server4 `/home`: 105798975488 available bytes; 94.10% used; 114348296 free inodes.

server4 `/data`: 60890537984 available bytes; 99.16% used; 225115602 free inodes.

server4 `/tmp`: 105798975488 available bytes; 94.10% used; 114348296 free inodes.

server4 `/var/tmp`: 105798975488 available bytes; 94.10% used; 114348296 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
