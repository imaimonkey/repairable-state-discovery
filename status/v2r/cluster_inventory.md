# V2R cluster inventory

2026-09-25T01:27:19.845483+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | ['2'] | ['/tmp', '/var/tmp'] |

server1 `/`: 319078010880 available bytes; 82.20% used; 112480768 free inodes.

server1 `/home`: 319078010880 available bytes; 82.20% used; 112480768 free inodes.

server1 `/tmp`: 319078010880 available bytes; 82.20% used; 112480768 free inodes.

server1 `/var/tmp`: 319078010880 available bytes; 82.20% used; 112480768 free inodes.

server1 `/mnt/raid5`: 416489611264 available bytes; 98.09% used; 337613272 free inodes.
| server2 | True | ['2', '6'] | [] |

server2 `/`: 23049826304 available bytes; 98.71% used; 110410774 free inodes.

server2 `/home`: 23049826304 available bytes; 98.71% used; 110410774 free inodes.

server2 `/tmp`: 23049826304 available bytes; 98.71% used; 110410774 free inodes.

server2 `/var/tmp`: 23049826304 available bytes; 98.71% used; 110410774 free inodes.

server2 `/mnt/raid5`: 491209355264 available bytes; 96.61% used; 445161586 free inodes.
| server3 | True | [] | [] |

server3 `/`: 84356034560 available bytes; 95.29% used; 114156079 free inodes.

server3 `/home`: 84356034560 available bytes; 95.29% used; 114156079 free inodes.

server3 `/data`: 146739167232 available bytes; 97.97% used; 225812360 free inodes.

server3 `/tmp`: 84356034560 available bytes; 95.29% used; 114156079 free inodes.

server3 `/var/tmp`: 84356034560 available bytes; 95.29% used; 114156079 free inodes.
| server4 | True | ['0', '1', '4', '5', '7'] | ['/tmp', '/var/tmp'] |

server4 `/`: 105778946048 available bytes; 94.10% used; 114348290 free inodes.

server4 `/home`: 105778946048 available bytes; 94.10% used; 114348290 free inodes.

server4 `/data`: 53320437760 available bytes; 99.26% used; 225030684 free inodes.

server4 `/tmp`: 105778946048 available bytes; 94.10% used; 114348290 free inodes.

server4 `/var/tmp`: 105778946048 available bytes; 94.10% used; 114348290 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
