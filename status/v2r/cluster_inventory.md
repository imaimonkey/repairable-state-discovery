# V2R cluster inventory

2026-09-24T23:45:35.584067+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | [] | ['/tmp', '/var/tmp'] |

server1 `/`: 319018500096 available bytes; 82.20% used; 112480768 free inodes.

server1 `/home`: 319018500096 available bytes; 82.20% used; 112480768 free inodes.

server1 `/tmp`: 319018500096 available bytes; 82.20% used; 112480768 free inodes.

server1 `/var/tmp`: 319018500096 available bytes; 82.20% used; 112480768 free inodes.

server1 `/mnt/raid5`: 415192461312 available bytes; 98.10% used; 337611405 free inodes.
| server2 | True | [] | [] |

server2 `/`: 23102820352 available bytes; 98.71% used; 110410796 free inodes.

server2 `/home`: 23102820352 available bytes; 98.71% used; 110410796 free inodes.

server2 `/tmp`: 23102820352 available bytes; 98.71% used; 110410796 free inodes.

server2 `/var/tmp`: 23102820352 available bytes; 98.71% used; 110410796 free inodes.

server2 `/mnt/raid5`: 485998575616 available bytes; 96.64% used; 445150961 free inodes.
| server3 | True | [] | [] |

server3 `/`: 84361265152 available bytes; 95.29% used; 114156079 free inodes.

server3 `/home`: 84361265152 available bytes; 95.29% used; 114156079 free inodes.

server3 `/data`: 147944931328 available bytes; 97.96% used; 225800631 free inodes.

server3 `/tmp`: 84361265152 available bytes; 95.29% used; 114156079 free inodes.

server3 `/var/tmp`: 84361265152 available bytes; 95.29% used; 114156079 free inodes.
| server4 | True | ['7'] | ['/tmp', '/var/tmp'] |

server4 `/`: 105799127040 available bytes; 94.10% used; 114348296 free inodes.

server4 `/home`: 105799127040 available bytes; 94.10% used; 114348296 free inodes.

server4 `/data`: 60999245824 available bytes; 99.16% used; 225124730 free inodes.

server4 `/tmp`: 105799127040 available bytes; 94.10% used; 114348296 free inodes.

server4 `/var/tmp`: 105799127040 available bytes; 94.10% used; 114348296 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
