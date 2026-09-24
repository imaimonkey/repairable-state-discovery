# V2R cluster inventory

2026-09-24T22:29:58.661831+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | [] | ['/tmp', '/var/tmp'] |

server1 `/`: 323945033728 available bytes; 81.93% used; 112481420 free inodes.

server1 `/home`: 323945033728 available bytes; 81.93% used; 112481420 free inodes.

server1 `/tmp`: 323945033728 available bytes; 81.93% used; 112481420 free inodes.

server1 `/var/tmp`: 323945033728 available bytes; 81.93% used; 112481420 free inodes.

server1 `/mnt/raid5`: 415373012992 available bytes; 98.09% used; 337620341 free inodes.
| server2 | True | ['4'] | [] |

server2 `/`: 23208112128 available bytes; 98.71% used; 110410941 free inodes.

server2 `/home`: 23208112128 available bytes; 98.71% used; 110410941 free inodes.

server2 `/tmp`: 23208112128 available bytes; 98.71% used; 110410941 free inodes.

server2 `/var/tmp`: 23208112128 available bytes; 98.71% used; 110410941 free inodes.

server2 `/mnt/raid5`: 488551100416 available bytes; 96.62% used; 445153153 free inodes.
| server3 | True | [] | [] |

server3 `/`: 84377722880 available bytes; 95.29% used; 114156081 free inodes.

server3 `/home`: 84377722880 available bytes; 95.29% used; 114156081 free inodes.

server3 `/data`: 149301166080 available bytes; 97.94% used; 225802080 free inodes.

server3 `/tmp`: 84377722880 available bytes; 95.29% used; 114156081 free inodes.

server3 `/var/tmp`: 84377722880 available bytes; 95.29% used; 114156081 free inodes.
| server4 | True | ['0', '5'] | ['/tmp', '/var/tmp'] |

server4 `/`: 105801990144 available bytes; 94.10% used; 114348328 free inodes.

server4 `/home`: 105801990144 available bytes; 94.10% used; 114348328 free inodes.

server4 `/data`: 73284378624 available bytes; 98.99% used; 225226424 free inodes.

server4 `/tmp`: 105801990144 available bytes; 94.10% used; 114348328 free inodes.

server4 `/var/tmp`: 105801990144 available bytes; 94.10% used; 114348328 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
