# V2R cluster inventory

2026-09-25T01:47:17.674712+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | [] | ['/tmp', '/var/tmp'] |

server1 `/`: 319076696064 available bytes; 82.20% used; 112480772 free inodes.

server1 `/home`: 319076696064 available bytes; 82.20% used; 112480772 free inodes.

server1 `/tmp`: 319076696064 available bytes; 82.20% used; 112480772 free inodes.

server1 `/var/tmp`: 319076696064 available bytes; 82.20% used; 112480772 free inodes.

server1 `/mnt/raid5`: 416450748416 available bytes; 98.09% used; 337610949 free inodes.
| server2 | True | ['2', '3', '6'] | [] |

server2 `/`: 23042002944 available bytes; 98.71% used; 110410780 free inodes.

server2 `/home`: 23042002944 available bytes; 98.71% used; 110410780 free inodes.

server2 `/tmp`: 23042002944 available bytes; 98.71% used; 110410780 free inodes.

server2 `/var/tmp`: 23042002944 available bytes; 98.71% used; 110410780 free inodes.

server2 `/mnt/raid5`: 490564096000 available bytes; 96.61% used; 445160708 free inodes.
| server3 | True | [] | [] |

server3 `/`: 84353703936 available bytes; 95.29% used; 114156084 free inodes.

server3 `/home`: 84353703936 available bytes; 95.29% used; 114156084 free inodes.

server3 `/data`: 146400759808 available bytes; 97.98% used; 225811987 free inodes.

server3 `/tmp`: 84353703936 available bytes; 95.29% used; 114156084 free inodes.

server3 `/var/tmp`: 84353703936 available bytes; 95.29% used; 114156084 free inodes.
| server4 | True | ['0', '1', '4', '5', '7'] | ['/tmp', '/var/tmp'] |

server4 `/`: 105761587200 available bytes; 94.10% used; 114348275 free inodes.

server4 `/home`: 105761587200 available bytes; 94.10% used; 114348275 free inodes.

server4 `/data`: 53311225856 available bytes; 99.26% used; 225030550 free inodes.

server4 `/tmp`: 105761587200 available bytes; 94.10% used; 114348275 free inodes.

server4 `/var/tmp`: 105761587200 available bytes; 94.10% used; 114348275 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
