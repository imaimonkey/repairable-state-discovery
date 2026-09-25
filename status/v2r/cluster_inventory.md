# V2R cluster inventory

2026-09-25T07:01:32.785614+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | [] | ['/tmp', '/var/tmp'] |

server1 `/`: 318871277568 available bytes; 82.21% used; 112480379 free inodes.

server1 `/home`: 318871277568 available bytes; 82.21% used; 112480379 free inodes.

server1 `/tmp`: 318871277568 available bytes; 82.21% used; 112480379 free inodes.

server1 `/var/tmp`: 318871277568 available bytes; 82.21% used; 112480379 free inodes.

server1 `/mnt/raid5`: 399703863296 available bytes; 98.17% used; 337560459 free inodes.
| server2 | True | [] | [] |

server2 `/`: 22879350784 available bytes; 98.72% used; 110410550 free inodes.

server2 `/home`: 22879350784 available bytes; 98.72% used; 110410550 free inodes.

server2 `/tmp`: 22879350784 available bytes; 98.72% used; 110410550 free inodes.

server2 `/var/tmp`: 22879350784 available bytes; 98.72% used; 110410550 free inodes.

server2 `/mnt/raid5`: 335386796032 available bytes; 97.68% used; 445098304 free inodes.
| server3 | True | [] | [] |

server3 `/`: 84447510528 available bytes; 95.29% used; 114156031 free inodes.

server3 `/home`: 84447510528 available bytes; 95.29% used; 114156031 free inodes.

server3 `/data`: 142453268480 available bytes; 98.03% used; 225813200 free inodes.

server3 `/tmp`: 84447510528 available bytes; 95.29% used; 114156031 free inodes.

server3 `/var/tmp`: 84447510528 available bytes; 95.29% used; 114156031 free inodes.
| server4 | True | ['3'] | ['/tmp', '/var/tmp'] |

server4 `/`: 105638739968 available bytes; 94.10% used; 114350361 free inodes.

server4 `/home`: 105638739968 available bytes; 94.10% used; 114350361 free inodes.

server4 `/data`: 249497640960 available bytes; 96.55% used; 225017129 free inodes.

server4 `/tmp`: 105638739968 available bytes; 94.10% used; 114350361 free inodes.

server4 `/var/tmp`: 105638739968 available bytes; 94.10% used; 114350361 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
