# V2R cluster inventory

2026-09-24T21:08:08.748725+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | [] | ['/tmp', '/var/tmp'] |

server1 `/`: 323972374528 available bytes; 81.93% used; 112481421 free inodes.

server1 `/home`: 323972374528 available bytes; 81.93% used; 112481421 free inodes.

server1 `/tmp`: 323972374528 available bytes; 81.93% used; 112481421 free inodes.

server1 `/var/tmp`: 323972374528 available bytes; 81.93% used; 112481421 free inodes.

server1 `/mnt/raid5`: 415546699776 available bytes; 98.09% used; 337630022 free inodes.
| server2 | True | ['7'] | [] |

server2 `/`: 30134956032 available bytes; 98.32% used; 110411370 free inodes.

server2 `/home`: 30134956032 available bytes; 98.32% used; 110411370 free inodes.

server2 `/tmp`: 30134956032 available bytes; 98.32% used; 110411370 free inodes.

server2 `/var/tmp`: 30134956032 available bytes; 98.32% used; 110411370 free inodes.

server2 `/mnt/raid5`: 491082051584 available bytes; 96.61% used; 445155714 free inodes.
| server3 | True | [] | [] |

server3 `/`: 84384919552 available bytes; 95.29% used; 114156093 free inodes.

server3 `/home`: 84384919552 available bytes; 95.29% used; 114156093 free inodes.

server3 `/data`: 150744977408 available bytes; 97.92% used; 225803614 free inodes.

server3 `/tmp`: 84384919552 available bytes; 95.29% used; 114156093 free inodes.

server3 `/var/tmp`: 84384919552 available bytes; 95.29% used; 114156093 free inodes.
| server4 | True | ['4'] | ['/tmp', '/var/tmp'] |

server4 `/`: 105638395904 available bytes; 94.10% used; 114348361 free inodes.

server4 `/home`: 105638395904 available bytes; 94.10% used; 114348361 free inodes.

server4 `/data`: 73316290560 available bytes; 98.99% used; 225254024 free inodes.

server4 `/tmp`: 105638395904 available bytes; 94.10% used; 114348361 free inodes.

server4 `/var/tmp`: 105638395904 available bytes; 94.10% used; 114348361 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
