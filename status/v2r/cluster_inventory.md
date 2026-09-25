# V2R cluster inventory

2026-09-25T05:48:32.185018+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | [] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 318874472448 available bytes; 82.21% used; 112480335 free inodes.

server1 `/home`: 318874472448 available bytes; 82.21% used; 112480335 free inodes.

server1 `/tmp`: 318874472448 available bytes; 82.21% used; 112480335 free inodes.

server1 `/var/tmp`: 318874472448 available bytes; 82.21% used; 112480335 free inodes.

server1 `/mnt/raid5`: 408444915712 available bytes; 98.13% used; 337566077 free inodes.
| server2 | True | [] | [] | reference_compatible=False |

server2 `/`: 22909706240 available bytes; 98.72% used; 110410369 free inodes.

server2 `/home`: 22909706240 available bytes; 98.72% used; 110410369 free inodes.

server2 `/tmp`: 22909706240 available bytes; 98.72% used; 110410369 free inodes.

server2 `/var/tmp`: 22909706240 available bytes; 98.72% used; 110410369 free inodes.

server2 `/mnt/raid5`: 418154360832 available bytes; 97.11% used; 445101774 free inodes.
| server3 | True | [] | [] | reference_compatible=True |

server3 `/`: 84312698880 available bytes; 95.30% used; 114156039 free inodes.

server3 `/home`: 84312698880 available bytes; 95.30% used; 114156039 free inodes.

server3 `/data`: 142777745408 available bytes; 98.03% used; 225814518 free inodes.

server3 `/tmp`: 84312698880 available bytes; 95.30% used; 114156039 free inodes.

server3 `/var/tmp`: 84312698880 available bytes; 95.30% used; 114156039 free inodes.
| server4 | True | ['3'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 105649471488 available bytes; 94.10% used; 114350388 free inodes.

server4 `/home`: 105649471488 available bytes; 94.10% used; 114350388 free inodes.

server4 `/data`: 24709095424 available bytes; 99.66% used; 224964932 free inodes.

server4 `/tmp`: 105649471488 available bytes; 94.10% used; 114350388 free inodes.

server4 `/var/tmp`: 105649471488 available bytes; 94.10% used; 114350388 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
