# V2R cluster inventory

2026-09-25T00:56:27.946732+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | [] | ['/tmp', '/var/tmp'] |

server1 `/`: 319087443968 available bytes; 82.20% used; 112480774 free inodes.

server1 `/home`: 319087443968 available bytes; 82.20% used; 112480774 free inodes.

server1 `/tmp`: 319087443968 available bytes; 82.20% used; 112480774 free inodes.

server1 `/var/tmp`: 319087443968 available bytes; 82.20% used; 112480774 free inodes.

server1 `/mnt/raid5`: 416804290560 available bytes; 98.09% used; 337616886 free inodes.
| server2 | True | [] | [] |

server2 `/`: 23067148288 available bytes; 98.71% used; 110410767 free inodes.

server2 `/home`: 23067148288 available bytes; 98.71% used; 110410767 free inodes.

server2 `/tmp`: 23067148288 available bytes; 98.71% used; 110410767 free inodes.

server2 `/var/tmp`: 23067148288 available bytes; 98.71% used; 110410767 free inodes.

server2 `/mnt/raid5`: 498534219776 available bytes; 96.56% used; 445162562 free inodes.
| server3 | True | [] | [] |

server3 `/`: 84356009984 available bytes; 95.29% used; 114156085 free inodes.

server3 `/home`: 84356009984 available bytes; 95.29% used; 114156085 free inodes.

server3 `/data`: 148448194560 available bytes; 97.95% used; 225812932 free inodes.

server3 `/tmp`: 84356009984 available bytes; 95.29% used; 114156085 free inodes.

server3 `/var/tmp`: 84356009984 available bytes; 95.29% used; 114156085 free inodes.
| server4 | True | ['0', '1', '4', '5', '7'] | ['/tmp', '/var/tmp'] |

server4 `/`: 105788256256 available bytes; 94.10% used; 114348304 free inodes.

server4 `/home`: 105788256256 available bytes; 94.10% used; 114348304 free inodes.

server4 `/data`: 55626833920 available bytes; 99.23% used; 225031244 free inodes.

server4 `/tmp`: 105788256256 available bytes; 94.10% used; 114348304 free inodes.

server4 `/var/tmp`: 105788256256 available bytes; 94.10% used; 114348304 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
