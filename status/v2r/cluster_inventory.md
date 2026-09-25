# V2R cluster inventory

2026-09-25T02:18:06.362429+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | [] | ['/tmp', '/var/tmp'] |

server1 `/`: 318970195968 available bytes; 82.21% used; 112480554 free inodes.

server1 `/home`: 318970195968 available bytes; 82.21% used; 112480554 free inodes.

server1 `/tmp`: 318970195968 available bytes; 82.21% used; 112480554 free inodes.

server1 `/var/tmp`: 318970195968 available bytes; 82.21% used; 112480554 free inodes.

server1 `/mnt/raid5`: 416237576192 available bytes; 98.09% used; 337607337 free inodes.
| server2 | True | [] | [] |

server2 `/`: 23016128512 available bytes; 98.72% used; 110410444 free inodes.

server2 `/home`: 23016128512 available bytes; 98.72% used; 110410444 free inodes.

server2 `/tmp`: 23016128512 available bytes; 98.72% used; 110410444 free inodes.

server2 `/var/tmp`: 23016128512 available bytes; 98.72% used; 110410444 free inodes.

server2 `/mnt/raid5`: 483779678208 available bytes; 96.66% used; 445113996 free inodes.
| server3 | True | [] | [] |

server3 `/`: 84350377984 available bytes; 95.29% used; 114156075 free inodes.

server3 `/home`: 84350377984 available bytes; 95.29% used; 114156075 free inodes.

server3 `/data`: 145787191296 available bytes; 97.99% used; 225811329 free inodes.

server3 `/tmp`: 84350377984 available bytes; 95.29% used; 114156075 free inodes.

server3 `/var/tmp`: 84350377984 available bytes; 95.29% used; 114156075 free inodes.
| server4 | True | ['0', '1', '4', '5', '7'] | ['/tmp', '/var/tmp'] |

server4 `/`: 105778769920 available bytes; 94.10% used; 114348290 free inodes.

server4 `/home`: 105778769920 available bytes; 94.10% used; 114348290 free inodes.

server4 `/data`: 38482395136 available bytes; 99.47% used; 224970360 free inodes.

server4 `/tmp`: 105778769920 available bytes; 94.10% used; 114348290 free inodes.

server4 `/var/tmp`: 105778769920 available bytes; 94.10% used; 114348290 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
