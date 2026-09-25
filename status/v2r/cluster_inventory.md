# V2R cluster inventory

2026-09-25T05:29:04.878219+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | [] | ['/tmp', '/var/tmp'] |

server1 `/`: 318860001280 available bytes; 82.21% used; 112480347 free inodes.

server1 `/home`: 318860001280 available bytes; 82.21% used; 112480347 free inodes.

server1 `/tmp`: 318860001280 available bytes; 82.21% used; 112480347 free inodes.

server1 `/var/tmp`: 318860001280 available bytes; 82.21% used; 112480347 free inodes.

server1 `/mnt/raid5`: 408497344512 available bytes; 98.13% used; 337568394 free inodes.
| server2 | True | [] | [] |

server2 `/`: 22921629696 available bytes; 98.72% used; 110410445 free inodes.

server2 `/home`: 22921629696 available bytes; 98.72% used; 110410445 free inodes.

server2 `/tmp`: 22921629696 available bytes; 98.72% used; 110410445 free inodes.

server2 `/var/tmp`: 22921629696 available bytes; 98.72% used; 110410445 free inodes.

server2 `/mnt/raid5`: 461217865728 available bytes; 96.81% used; 445108216 free inodes.
| server3 | True | [] | [] |

server3 `/`: 84313280512 available bytes; 95.30% used; 114156043 free inodes.

server3 `/home`: 84313280512 available bytes; 95.30% used; 114156043 free inodes.

server3 `/data`: 142779043840 available bytes; 98.03% used; 225814834 free inodes.

server3 `/tmp`: 84313280512 available bytes; 95.30% used; 114156043 free inodes.

server3 `/var/tmp`: 84313280512 available bytes; 95.30% used; 114156043 free inodes.
| server4 | True | ['6', '7'] | ['/tmp', '/var/tmp'] |

server4 `/`: 105658445824 available bytes; 94.10% used; 114350397 free inodes.

server4 `/home`: 105658445824 available bytes; 94.10% used; 114350397 free inodes.

server4 `/data`: 26409259008 available bytes; 99.64% used; 224968361 free inodes.

server4 `/tmp`: 105658445824 available bytes; 94.10% used; 114350397 free inodes.

server4 `/var/tmp`: 105658445824 available bytes; 94.10% used; 114350397 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
