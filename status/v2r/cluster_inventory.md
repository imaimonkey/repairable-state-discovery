# V2R cluster inventory

2026-09-24T12:16:05.321651+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | [] | ['/tmp', '/var/tmp'] |

server1 `/`: 324057927680 available bytes; 81.92% used; 112481588 free inodes.

server1 `/home`: 324057927680 available bytes; 81.92% used; 112481588 free inodes.

server1 `/tmp`: 324057927680 available bytes; 81.92% used; 112481588 free inodes.

server1 `/var/tmp`: 324057927680 available bytes; 81.92% used; 112481588 free inodes.

server1 `/mnt/raid5`: 405218816000 available bytes; 98.14% used; 337684025 free inodes.
| server2 | True | ['7'] | [] |

server2 `/`: 57615642624 available bytes; 96.79% used; 110429540 free inodes.

server2 `/home`: 57615642624 available bytes; 96.79% used; 110429540 free inodes.

server2 `/tmp`: 57615642624 available bytes; 96.79% used; 110429540 free inodes.

server2 `/var/tmp`: 57615642624 available bytes; 96.79% used; 110429540 free inodes.

server2 `/mnt/raid5`: 508927557632 available bytes; 96.48% used; 445172211 free inodes.
| server3 | True | [] | [] |

server3 `/`: 85132038144 available bytes; 95.25% used; 114164759 free inodes.

server3 `/home`: 85132038144 available bytes; 95.25% used; 114164759 free inodes.

server3 `/data`: 163466809344 available bytes; 97.74% used; 225815012 free inodes.

server3 `/tmp`: 85132038144 available bytes; 95.25% used; 114164759 free inodes.

server3 `/var/tmp`: 85132038144 available bytes; 95.25% used; 114164759 free inodes.
| server4 | True | [] | ['/tmp', '/var/tmp'] |

server4 `/`: 105781243904 available bytes; 94.10% used; 114348812 free inodes.

server4 `/home`: 105781243904 available bytes; 94.10% used; 114348812 free inodes.

server4 `/data`: 90424041472 available bytes; 98.75% used; 225257319 free inodes.

server4 `/tmp`: 105781243904 available bytes; 94.10% used; 114348812 free inodes.

server4 `/var/tmp`: 105781243904 available bytes; 94.10% used; 114348812 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
