# V2R cluster inventory

2026-09-25T06:56:57.321215+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | [] | ['/tmp', '/var/tmp'] |

server1 `/`: 318871281664 available bytes; 82.21% used; 112480374 free inodes.

server1 `/home`: 318871281664 available bytes; 82.21% used; 112480374 free inodes.

server1 `/tmp`: 318871281664 available bytes; 82.21% used; 112480374 free inodes.

server1 `/var/tmp`: 318871281664 available bytes; 82.21% used; 112480374 free inodes.

server1 `/mnt/raid5`: 399712763904 available bytes; 98.17% used; 337560483 free inodes.
| server2 | True | [] | [] |

server2 `/`: 22878150656 available bytes; 98.72% used; 110410526 free inodes.

server2 `/home`: 22878150656 available bytes; 98.72% used; 110410526 free inodes.

server2 `/tmp`: 22878150656 available bytes; 98.72% used; 110410526 free inodes.

server2 `/var/tmp`: 22878150656 available bytes; 98.72% used; 110410526 free inodes.

server2 `/mnt/raid5`: 337422888960 available bytes; 97.67% used; 445098409 free inodes.
| server3 | True | [] | [] |

server3 `/`: 84450537472 available bytes; 95.29% used; 114156029 free inodes.

server3 `/home`: 84450537472 available bytes; 95.29% used; 114156029 free inodes.

server3 `/data`: 142450495488 available bytes; 98.03% used; 225813269 free inodes.

server3 `/tmp`: 84450537472 available bytes; 95.29% used; 114156029 free inodes.

server3 `/var/tmp`: 84450537472 available bytes; 95.29% used; 114156029 free inodes.
| server4 | True | ['3'] | ['/tmp', '/var/tmp'] |

server4 `/`: 105638866944 available bytes; 94.10% used; 114350361 free inodes.

server4 `/home`: 105638866944 available bytes; 94.10% used; 114350361 free inodes.

server4 `/data`: 249503383552 available bytes; 96.55% used; 225017409 free inodes.

server4 `/tmp`: 105638866944 available bytes; 94.10% used; 114350361 free inodes.

server4 `/var/tmp`: 105638866944 available bytes; 94.10% used; 114350361 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
