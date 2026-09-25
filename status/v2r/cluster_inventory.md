# V2R cluster inventory

2026-09-25T06:04:31.775501+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | [] | ['/tmp', '/var/tmp'] |

server1 `/`: 318873735168 available bytes; 82.21% used; 112480341 free inodes.

server1 `/home`: 318873735168 available bytes; 82.21% used; 112480341 free inodes.

server1 `/tmp`: 318873735168 available bytes; 82.21% used; 112480341 free inodes.

server1 `/var/tmp`: 318873735168 available bytes; 82.21% used; 112480341 free inodes.

server1 `/mnt/raid5`: 401519009792 available bytes; 98.16% used; 337564115 free inodes.
| server2 | True | [] | [] |

server2 `/`: 22901121024 available bytes; 98.72% used; 110410353 free inodes.

server2 `/home`: 22901121024 available bytes; 98.72% used; 110410353 free inodes.

server2 `/tmp`: 22901121024 available bytes; 98.72% used; 110410353 free inodes.

server2 `/var/tmp`: 22901121024 available bytes; 98.72% used; 110410353 free inodes.

server2 `/mnt/raid5`: 379971903488 available bytes; 97.37% used; 445100574 free inodes.
| server3 | True | [] | [] |

server3 `/`: 84318703616 available bytes; 95.29% used; 114156041 free inodes.

server3 `/home`: 84318703616 available bytes; 95.29% used; 114156041 free inodes.

server3 `/data`: 142774722560 available bytes; 98.03% used; 225814230 free inodes.

server3 `/tmp`: 84318703616 available bytes; 95.29% used; 114156041 free inodes.

server3 `/var/tmp`: 84318703616 available bytes; 95.29% used; 114156041 free inodes.
| server4 | True | ['3'] | ['/tmp', '/var/tmp'] |

server4 `/`: 105648975872 available bytes; 94.10% used; 114350386 free inodes.

server4 `/home`: 105648975872 available bytes; 94.10% used; 114350386 free inodes.

server4 `/data`: 256274272256 available bytes; 96.46% used; 225025122 free inodes.

server4 `/tmp`: 105648975872 available bytes; 94.10% used; 114350386 free inodes.

server4 `/var/tmp`: 105648975872 available bytes; 94.10% used; 114350386 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
