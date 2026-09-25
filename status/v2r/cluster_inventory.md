# V2R cluster inventory

2026-09-25T06:46:12.887039+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | [] | ['/tmp', '/var/tmp'] |

server1 `/`: 318872301568 available bytes; 82.21% used; 112480357 free inodes.

server1 `/home`: 318872301568 available bytes; 82.21% used; 112480357 free inodes.

server1 `/tmp`: 318872301568 available bytes; 82.21% used; 112480357 free inodes.

server1 `/var/tmp`: 318872301568 available bytes; 82.21% used; 112480357 free inodes.

server1 `/mnt/raid5`: 379133730816 available bytes; 98.26% used; 337561358 free inodes.
| server2 | True | [] | [] |

server2 `/`: 22884347904 available bytes; 98.72% used; 110410526 free inodes.

server2 `/home`: 22884347904 available bytes; 98.72% used; 110410526 free inodes.

server2 `/tmp`: 22884347904 available bytes; 98.72% used; 110410526 free inodes.

server2 `/var/tmp`: 22884347904 available bytes; 98.72% used; 110410526 free inodes.

server2 `/mnt/raid5`: 353518530560 available bytes; 97.56% used; 445098844 free inodes.
| server3 | True | [] | [] |

server3 `/`: 84449308672 available bytes; 95.29% used; 114156031 free inodes.

server3 `/home`: 84449308672 available bytes; 95.29% used; 114156031 free inodes.

server3 `/data`: 142530019328 available bytes; 98.03% used; 225813479 free inodes.

server3 `/tmp`: 84449308672 available bytes; 95.29% used; 114156031 free inodes.

server3 `/var/tmp`: 84449308672 available bytes; 95.29% used; 114156031 free inodes.
| server4 | True | ['3'] | ['/tmp', '/var/tmp'] |

server4 `/`: 105639292928 available bytes; 94.10% used; 114350382 free inodes.

server4 `/home`: 105639292928 available bytes; 94.10% used; 114350382 free inodes.

server4 `/data`: 251118751744 available bytes; 96.53% used; 225018396 free inodes.

server4 `/tmp`: 105639292928 available bytes; 94.10% used; 114350382 free inodes.

server4 `/var/tmp`: 105639292928 available bytes; 94.10% used; 114350382 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
