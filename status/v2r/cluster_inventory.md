# V2R cluster inventory

2026-09-25T07:04:36.557636+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | [] | ['/tmp', '/var/tmp'] |

server1 `/`: 318871773184 available bytes; 82.21% used; 112480377 free inodes.

server1 `/home`: 318871773184 available bytes; 82.21% used; 112480377 free inodes.

server1 `/tmp`: 318871773184 available bytes; 82.21% used; 112480377 free inodes.

server1 `/var/tmp`: 318871773184 available bytes; 82.21% used; 112480377 free inodes.

server1 `/mnt/raid5`: 399692587008 available bytes; 98.17% used; 337560444 free inodes.
| server2 | True | [] | [] |

server2 `/`: 22878785536 available bytes; 98.72% used; 110410548 free inodes.

server2 `/home`: 22878785536 available bytes; 98.72% used; 110410548 free inodes.

server2 `/tmp`: 22878785536 available bytes; 98.72% used; 110410548 free inodes.

server2 `/var/tmp`: 22878785536 available bytes; 98.72% used; 110410548 free inodes.

server2 `/mnt/raid5`: 330436939776 available bytes; 97.72% used; 445097911 free inodes.
| server3 | True | [] | [] |

server3 `/`: 84446683136 available bytes; 95.29% used; 114156029 free inodes.

server3 `/home`: 84446683136 available bytes; 95.29% used; 114156029 free inodes.

server3 `/data`: 142455934976 available bytes; 98.03% used; 225813148 free inodes.

server3 `/tmp`: 84446683136 available bytes; 95.29% used; 114156029 free inodes.

server3 `/var/tmp`: 84446683136 available bytes; 95.29% used; 114156029 free inodes.
| server4 | True | ['3'] | ['/tmp', '/var/tmp'] |

server4 `/`: 105638641664 available bytes; 94.10% used; 114350361 free inodes.

server4 `/home`: 105638641664 available bytes; 94.10% used; 114350361 free inodes.

server4 `/data`: 249493835776 available bytes; 96.55% used; 225016943 free inodes.

server4 `/tmp`: 105638641664 available bytes; 94.10% used; 114350361 free inodes.

server4 `/var/tmp`: 105638641664 available bytes; 94.10% used; 114350361 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
