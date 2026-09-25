# V2R cluster inventory

2026-09-25T07:00:00.986303+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | [] | ['/tmp', '/var/tmp'] |

server1 `/`: 318871494656 available bytes; 82.21% used; 112480376 free inodes.

server1 `/home`: 318871494656 available bytes; 82.21% used; 112480376 free inodes.

server1 `/tmp`: 318871494656 available bytes; 82.21% used; 112480376 free inodes.

server1 `/var/tmp`: 318871494656 available bytes; 82.21% used; 112480376 free inodes.

server1 `/mnt/raid5`: 399711186944 available bytes; 98.17% used; 337560481 free inodes.
| server2 | True | [] | [] |

server2 `/`: 22878154752 available bytes; 98.72% used; 110410530 free inodes.

server2 `/home`: 22878154752 available bytes; 98.72% used; 110410530 free inodes.

server2 `/tmp`: 22878154752 available bytes; 98.72% used; 110410530 free inodes.

server2 `/var/tmp`: 22878154752 available bytes; 98.72% used; 110410530 free inodes.

server2 `/mnt/raid5`: 336796319744 available bytes; 97.67% used; 445098277 free inodes.
| server3 | True | [] | [] |

server3 `/`: 84447653888 available bytes; 95.29% used; 114156031 free inodes.

server3 `/home`: 84447653888 available bytes; 95.29% used; 114156031 free inodes.

server3 `/data`: 142449352704 available bytes; 98.03% used; 225813212 free inodes.

server3 `/tmp`: 84447653888 available bytes; 95.29% used; 114156031 free inodes.

server3 `/var/tmp`: 84447653888 available bytes; 95.29% used; 114156031 free inodes.
| server4 | True | ['3'] | ['/tmp', '/var/tmp'] |

server4 `/`: 105638776832 available bytes; 94.10% used; 114350361 free inodes.

server4 `/home`: 105638776832 available bytes; 94.10% used; 114350361 free inodes.

server4 `/data`: 249500180480 available bytes; 96.55% used; 225017208 free inodes.

server4 `/tmp`: 105638776832 available bytes; 94.10% used; 114350361 free inodes.

server4 `/var/tmp`: 105638776832 available bytes; 94.10% used; 114350361 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
