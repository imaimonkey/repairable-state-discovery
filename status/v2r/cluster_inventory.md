# V2R cluster inventory

2026-09-25T00:01:03.825902+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | [] | ['/tmp', '/var/tmp'] |

server1 `/`: 319090327552 available bytes; 82.20% used; 112480778 free inodes.

server1 `/home`: 319090327552 available bytes; 82.20% used; 112480778 free inodes.

server1 `/tmp`: 319090327552 available bytes; 82.20% used; 112480778 free inodes.

server1 `/var/tmp`: 319090327552 available bytes; 82.20% used; 112480778 free inodes.

server1 `/mnt/raid5`: 416909787136 available bytes; 98.09% used; 337623258 free inodes.
| server2 | True | [] | [] |

server2 `/`: 23092711424 available bytes; 98.71% used; 110410788 free inodes.

server2 `/home`: 23092711424 available bytes; 98.71% used; 110410788 free inodes.

server2 `/tmp`: 23092711424 available bytes; 98.71% used; 110410788 free inodes.

server2 `/var/tmp`: 23092711424 available bytes; 98.71% used; 110410788 free inodes.

server2 `/mnt/raid5`: 487395323904 available bytes; 96.63% used; 445164014 free inodes.
| server3 | True | [] | [] |

server3 `/`: 84353007616 available bytes; 95.29% used; 114156084 free inodes.

server3 `/home`: 84353007616 available bytes; 95.29% used; 114156084 free inodes.

server3 `/data`: 149454307328 available bytes; 97.93% used; 225813989 free inodes.

server3 `/tmp`: 84353007616 available bytes; 95.29% used; 114156084 free inodes.

server3 `/var/tmp`: 84353007616 available bytes; 95.29% used; 114156084 free inodes.
| server4 | True | ['0', '5', '7'] | ['/tmp', '/var/tmp'] |

server4 `/`: 105798721536 available bytes; 94.10% used; 114348302 free inodes.

server4 `/home`: 105798721536 available bytes; 94.10% used; 114348302 free inodes.

server4 `/data`: 60689747968 available bytes; 99.16% used; 225100991 free inodes.

server4 `/tmp`: 105798721536 available bytes; 94.10% used; 114348302 free inodes.

server4 `/var/tmp`: 105798721536 available bytes; 94.10% used; 114348302 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
