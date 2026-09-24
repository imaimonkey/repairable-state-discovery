# V2R cluster inventory

2026-09-24T12:02:07.307160+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | [] | ['/tmp', '/var/tmp'] |

server1 `/`: 324271939584 available bytes; 81.91% used; 112488379 free inodes.

server1 `/home`: 324271939584 available bytes; 81.91% used; 112488379 free inodes.

server1 `/tmp`: 324271939584 available bytes; 81.91% used; 112488379 free inodes.

server1 `/var/tmp`: 324271939584 available bytes; 81.91% used; 112488379 free inodes.

server1 `/mnt/raid5`: 406618275840 available bytes; 98.13% used; 337685637 free inodes.
| server2 | True | ['7'] | [] |

server2 `/`: 57626230784 available bytes; 96.79% used; 110429680 free inodes.

server2 `/home`: 57626230784 available bytes; 96.79% used; 110429680 free inodes.

server2 `/tmp`: 57626230784 available bytes; 96.79% used; 110429680 free inodes.

server2 `/var/tmp`: 57626230784 available bytes; 96.79% used; 110429680 free inodes.

server2 `/mnt/raid5`: 509375455232 available bytes; 96.48% used; 445172761 free inodes.
| server3 | True | [] | [] |

server3 `/`: 85748043776 available bytes; 95.21% used; 114198401 free inodes.

server3 `/home`: 85748043776 available bytes; 95.21% used; 114198401 free inodes.

server3 `/data`: 163570577408 available bytes; 97.74% used; 225815644 free inodes.

server3 `/tmp`: 85748043776 available bytes; 95.21% used; 114198401 free inodes.

server3 `/var/tmp`: 85748043776 available bytes; 95.21% used; 114198401 free inodes.
| server4 | True | [] | ['/tmp', '/var/tmp'] |

server4 `/`: 105718636544 available bytes; 94.10% used; 114348826 free inodes.

server4 `/home`: 105718636544 available bytes; 94.10% used; 114348826 free inodes.

server4 `/data`: 102326571008 available bytes; 98.59% used; 225257585 free inodes.

server4 `/tmp`: 105718636544 available bytes; 94.10% used; 114348826 free inodes.

server4 `/var/tmp`: 105718636544 available bytes; 94.10% used; 114348826 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
