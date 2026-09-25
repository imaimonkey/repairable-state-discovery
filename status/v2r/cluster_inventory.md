# V2R cluster inventory

2026-09-25T00:41:02.845536+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | [] | ['/tmp', '/var/tmp'] |

server1 `/`: 319087128576 available bytes; 82.20% used; 112480770 free inodes.

server1 `/home`: 319087128576 available bytes; 82.20% used; 112480770 free inodes.

server1 `/tmp`: 319087128576 available bytes; 82.20% used; 112480770 free inodes.

server1 `/var/tmp`: 319087128576 available bytes; 82.20% used; 112480770 free inodes.

server1 `/mnt/raid5`: 416834093056 available bytes; 98.09% used; 337618602 free inodes.
| server2 | True | [] | [] |

server2 `/`: 23076872192 available bytes; 98.71% used; 110410769 free inodes.

server2 `/home`: 23076872192 available bytes; 98.71% used; 110410769 free inodes.

server2 `/tmp`: 23076872192 available bytes; 98.71% used; 110410769 free inodes.

server2 `/var/tmp`: 23076872192 available bytes; 98.71% used; 110410769 free inodes.

server2 `/mnt/raid5`: 501482110976 available bytes; 96.53% used; 445162475 free inodes.
| server3 | True | [] | [] |

server3 `/`: 84351188992 available bytes; 95.29% used; 114156088 free inodes.

server3 `/home`: 84351188992 available bytes; 95.29% used; 114156088 free inodes.

server3 `/data`: 148697579520 available bytes; 97.94% used; 225813250 free inodes.

server3 `/tmp`: 84351188992 available bytes; 95.29% used; 114156088 free inodes.

server3 `/var/tmp`: 84351188992 available bytes; 95.29% used; 114156088 free inodes.
| server4 | True | ['0', '5', '7'] | ['/tmp', '/var/tmp'] |

server4 `/`: 105788641280 available bytes; 94.10% used; 114348296 free inodes.

server4 `/home`: 105788641280 available bytes; 94.10% used; 114348296 free inodes.

server4 `/data`: 56494366720 available bytes; 99.22% used; 225043529 free inodes.

server4 `/tmp`: 105788641280 available bytes; 94.10% used; 114348296 free inodes.

server4 `/var/tmp`: 105788641280 available bytes; 94.10% used; 114348296 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
