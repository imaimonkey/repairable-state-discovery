# V2R cluster inventory

2026-09-24T23:20:54.857235+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | [] | ['/tmp', '/var/tmp'] |

server1 `/`: 319007858688 available bytes; 82.20% used; 112480798 free inodes.

server1 `/home`: 319007858688 available bytes; 82.20% used; 112480798 free inodes.

server1 `/tmp`: 319007858688 available bytes; 82.20% used; 112480798 free inodes.

server1 `/var/tmp`: 319007858688 available bytes; 82.20% used; 112480798 free inodes.

server1 `/mnt/raid5`: 415252090880 available bytes; 98.10% used; 337614284 free inodes.
| server2 | True | [] | [] |

server2 `/`: 23120228352 available bytes; 98.71% used; 110410814 free inodes.

server2 `/home`: 23120228352 available bytes; 98.71% used; 110410814 free inodes.

server2 `/tmp`: 23120228352 available bytes; 98.71% used; 110410814 free inodes.

server2 `/var/tmp`: 23120228352 available bytes; 98.71% used; 110410814 free inodes.

server2 `/mnt/raid5`: 486967365632 available bytes; 96.64% used; 445151505 free inodes.
| server3 | True | [] | [] |

server3 `/`: 84373671936 available bytes; 95.29% used; 114156087 free inodes.

server3 `/home`: 84373671936 available bytes; 95.29% used; 114156087 free inodes.

server3 `/data`: 148431519744 available bytes; 97.95% used; 225801078 free inodes.

server3 `/tmp`: 84373671936 available bytes; 95.29% used; 114156087 free inodes.

server3 `/var/tmp`: 84373671936 available bytes; 95.29% used; 114156087 free inodes.
| server4 | True | ['7'] | ['/tmp', '/var/tmp'] |

server4 `/`: 105799823360 available bytes; 94.10% used; 114348305 free inodes.

server4 `/home`: 105799823360 available bytes; 94.10% used; 114348305 free inodes.

server4 `/data`: 61493010432 available bytes; 99.15% used; 225160559 free inodes.

server4 `/tmp`: 105799823360 available bytes; 94.10% used; 114348305 free inodes.

server4 `/var/tmp`: 105799823360 available bytes; 94.10% used; 114348305 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
