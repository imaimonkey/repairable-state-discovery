# V2R cluster inventory

2026-09-25T06:34:49.880269+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | [] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 318873341952 available bytes; 82.21% used; 112480350 free inodes.

server1 `/home`: 318873341952 available bytes; 82.21% used; 112480350 free inodes.

server1 `/tmp`: 318873341952 available bytes; 82.21% used; 112480350 free inodes.

server1 `/var/tmp`: 318873341952 available bytes; 82.21% used; 112480350 free inodes.

server1 `/mnt/raid5`: 399806226432 available bytes; 98.17% used; 337561423 free inodes.
| server2 | True | [] | [] | reference_compatible=False |

server2 `/`: 22888095744 available bytes; 98.72% used; 110410514 free inodes.

server2 `/home`: 22888095744 available bytes; 98.72% used; 110410514 free inodes.

server2 `/tmp`: 22888095744 available bytes; 98.72% used; 110410514 free inodes.

server2 `/var/tmp`: 22888095744 available bytes; 98.72% used; 110410514 free inodes.

server2 `/mnt/raid5`: 370393554944 available bytes; 97.44% used; 445099252 free inodes.
| server3 | True | [] | [] | reference_compatible=True |

server3 `/`: 84449538048 available bytes; 95.29% used; 114156031 free inodes.

server3 `/home`: 84449538048 available bytes; 95.29% used; 114156031 free inodes.

server3 `/data`: 142535667712 available bytes; 98.03% used; 225813717 free inodes.

server3 `/tmp`: 84449538048 available bytes; 95.29% used; 114156031 free inodes.

server3 `/var/tmp`: 84449538048 available bytes; 95.29% used; 114156031 free inodes.
| server4 | True | ['3'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 105639649280 available bytes; 94.10% used; 114350388 free inodes.

server4 `/home`: 105639649280 available bytes; 94.10% used; 114350388 free inodes.

server4 `/data`: 252206411776 available bytes; 96.51% used; 225019906 free inodes.

server4 `/tmp`: 105639649280 available bytes; 94.10% used; 114350388 free inodes.

server4 `/var/tmp`: 105639649280 available bytes; 94.10% used; 114350388 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
