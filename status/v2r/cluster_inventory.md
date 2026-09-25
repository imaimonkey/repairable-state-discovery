# V2R cluster inventory

2026-09-25T05:55:12.710303+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | [] | ['/tmp', '/var/tmp'] |

server1 `/`: 318869434368 available bytes; 82.21% used; 112480336 free inodes.

server1 `/home`: 318869434368 available bytes; 82.21% used; 112480336 free inodes.

server1 `/tmp`: 318869434368 available bytes; 82.21% used; 112480336 free inodes.

server1 `/var/tmp`: 318869434368 available bytes; 82.21% used; 112480336 free inodes.

server1 `/mnt/raid5`: 408425197568 available bytes; 98.13% used; 337565283 free inodes.
| server2 | True | [] | [] |

server2 `/`: 22912057344 available bytes; 98.72% used; 110410371 free inodes.

server2 `/home`: 22912057344 available bytes; 98.72% used; 110410371 free inodes.

server2 `/tmp`: 22912057344 available bytes; 98.72% used; 110410371 free inodes.

server2 `/var/tmp`: 22912057344 available bytes; 98.72% used; 110410371 free inodes.

server2 `/mnt/raid5`: 393676500992 available bytes; 97.28% used; 445101367 free inodes.
| server3 | True | [] | [] |

server3 `/`: 84312170496 available bytes; 95.30% used; 114156039 free inodes.

server3 `/home`: 84312170496 available bytes; 95.30% used; 114156039 free inodes.

server3 `/data`: 142772957184 available bytes; 98.03% used; 225814375 free inodes.

server3 `/tmp`: 84312170496 available bytes; 95.30% used; 114156039 free inodes.

server3 `/var/tmp`: 84312170496 available bytes; 95.30% used; 114156039 free inodes.
| server4 | True | ['3'] | ['/tmp', '/var/tmp'] |

server4 `/`: 105649258496 available bytes; 94.10% used; 114350387 free inodes.

server4 `/home`: 105649258496 available bytes; 94.10% used; 114350387 free inodes.

server4 `/data`: 256297885696 available bytes; 96.46% used; 225026534 free inodes.

server4 `/tmp`: 105649258496 available bytes; 94.10% used; 114350387 free inodes.

server4 `/var/tmp`: 105649258496 available bytes; 94.10% used; 114350387 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
