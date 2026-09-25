# V2R cluster inventory

2026-09-25T06:21:23.719662+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | [] | ['/tmp', '/var/tmp'] |

server1 `/`: 318881533952 available bytes; 82.21% used; 112480351 free inodes.

server1 `/home`: 318881533952 available bytes; 82.21% used; 112480351 free inodes.

server1 `/tmp`: 318881533952 available bytes; 82.21% used; 112480351 free inodes.

server1 `/var/tmp`: 318881533952 available bytes; 82.21% used; 112480351 free inodes.

server1 `/mnt/raid5`: 401458135040 available bytes; 98.16% used; 337562095 free inodes.
| server2 | True | [] | [] |

server2 `/`: 22895116288 available bytes; 98.72% used; 110410534 free inodes.

server2 `/home`: 22895116288 available bytes; 98.72% used; 110410534 free inodes.

server2 `/tmp`: 22895116288 available bytes; 98.72% used; 110410534 free inodes.

server2 `/var/tmp`: 22895116288 available bytes; 98.72% used; 110410534 free inodes.

server2 `/mnt/raid5`: 372884787200 available bytes; 97.42% used; 445100154 free inodes.
| server3 | True | [] | [] |

server3 `/`: 84315889664 available bytes; 95.29% used; 114156037 free inodes.

server3 `/home`: 84315889664 available bytes; 95.29% used; 114156037 free inodes.

server3 `/data`: 142534156288 available bytes; 98.03% used; 225813932 free inodes.

server3 `/tmp`: 84315889664 available bytes; 95.29% used; 114156037 free inodes.

server3 `/var/tmp`: 84315889664 available bytes; 95.29% used; 114156037 free inodes.
| server4 | True | ['3'] | ['/tmp', '/var/tmp'] |

server4 `/`: 105648476160 available bytes; 94.10% used; 114350390 free inodes.

server4 `/home`: 105648476160 available bytes; 94.10% used; 114350390 free inodes.

server4 `/data`: 254606737408 available bytes; 96.48% used; 225022237 free inodes.

server4 `/tmp`: 105648476160 available bytes; 94.10% used; 114350390 free inodes.

server4 `/var/tmp`: 105648476160 available bytes; 94.10% used; 114350390 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
