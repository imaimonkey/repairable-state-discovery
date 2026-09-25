# V2R cluster inventory

2026-09-25T05:59:52.365562+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | [] | ['/tmp', '/var/tmp'] |

server1 `/`: 318868652032 available bytes; 82.21% used; 112480336 free inodes.

server1 `/home`: 318868652032 available bytes; 82.21% used; 112480336 free inodes.

server1 `/tmp`: 318868652032 available bytes; 82.21% used; 112480336 free inodes.

server1 `/var/tmp`: 318868652032 available bytes; 82.21% used; 112480336 free inodes.

server1 `/mnt/raid5`: 408417214464 available bytes; 98.13% used; 337564738 free inodes.
| server2 | True | [] | [] |

server2 `/`: 22902980608 available bytes; 98.72% used; 110410369 free inodes.

server2 `/home`: 22902980608 available bytes; 98.72% used; 110410369 free inodes.

server2 `/tmp`: 22902980608 available bytes; 98.72% used; 110410369 free inodes.

server2 `/var/tmp`: 22902980608 available bytes; 98.72% used; 110410369 free inodes.

server2 `/mnt/raid5`: 391512211456 available bytes; 97.29% used; 445101103 free inodes.
| server3 | True | [] | [] |

server3 `/`: 84318261248 available bytes; 95.29% used; 114156041 free inodes.

server3 `/home`: 84318261248 available bytes; 95.29% used; 114156041 free inodes.

server3 `/data`: 142779240448 available bytes; 98.03% used; 225814308 free inodes.

server3 `/tmp`: 84318261248 available bytes; 95.29% used; 114156041 free inodes.

server3 `/var/tmp`: 84318261248 available bytes; 95.29% used; 114156041 free inodes.
| server4 | True | ['3'] | ['/tmp', '/var/tmp'] |

server4 `/`: 105649123328 available bytes; 94.10% used; 114350386 free inodes.

server4 `/home`: 105649123328 available bytes; 94.10% used; 114350386 free inodes.

server4 `/data`: 256288079872 available bytes; 96.46% used; 225025803 free inodes.

server4 `/tmp`: 105649123328 available bytes; 94.10% used; 114350386 free inodes.

server4 `/var/tmp`: 105649123328 available bytes; 94.10% used; 114350386 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
