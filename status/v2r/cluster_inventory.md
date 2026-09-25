# V2R cluster inventory

2026-09-25T10:27:44.651804+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | [] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 318835879936 available bytes; 82.21% used; 112480397 free inodes.

server1 `/home`: 318835879936 available bytes; 82.21% used; 112480397 free inodes.

server1 `/tmp`: 318835879936 available bytes; 82.21% used; 112480397 free inodes.

server1 `/var/tmp`: 318835879936 available bytes; 82.21% used; 112480397 free inodes.

server1 `/mnt/raid5`: 365195907072 available bytes; 98.32% used; 337555296 free inodes.
| server2 | True | ['3', '5', '6'] | [] | reference_compatible=False |

server2 `/`: 22831808512 available bytes; 98.73% used; 110410490 free inodes.

server2 `/home`: 22831808512 available bytes; 98.73% used; 110410490 free inodes.

server2 `/tmp`: 22831808512 available bytes; 98.73% used; 110410490 free inodes.

server2 `/var/tmp`: 22831808512 available bytes; 98.73% used; 110410490 free inodes.

server2 `/mnt/raid5`: 316230422528 available bytes; 97.81% used; 445090681 free inodes.
| server3 | True | [] | [] | reference_compatible=True |

server3 `/`: 84420878336 available bytes; 95.29% used; 114156051 free inodes.

server3 `/home`: 84420878336 available bytes; 95.29% used; 114156051 free inodes.

server3 `/data`: 142020448256 available bytes; 98.04% used; 225815810 free inodes.

server3 `/tmp`: 84420878336 available bytes; 95.29% used; 114156051 free inodes.

server3 `/var/tmp`: 84420878336 available bytes; 95.29% used; 114156051 free inodes.
| server4 | True | [] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 105613430784 available bytes; 94.11% used; 114350252 free inodes.

server4 `/home`: 105613430784 available bytes; 94.11% used; 114350252 free inodes.

server4 `/data`: 238447284224 available bytes; 96.70% used; 224987893 free inodes.

server4 `/tmp`: 105613430784 available bytes; 94.11% used; 114350252 free inodes.

server4 `/var/tmp`: 105613430784 available bytes; 94.11% used; 114350252 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
