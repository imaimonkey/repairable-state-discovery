# V2R cluster inventory

2026-09-25T03:51:24.648110+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | [] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 318928265216 available bytes; 82.21% used; 112480352 free inodes.

server1 `/home`: 318928265216 available bytes; 82.21% used; 112480352 free inodes.

server1 `/tmp`: 318928265216 available bytes; 82.21% used; 112480352 free inodes.

server1 `/var/tmp`: 318928265216 available bytes; 82.21% used; 112480352 free inodes.

server1 `/mnt/raid5`: 415725641728 available bytes; 98.09% used; 337596345 free inodes.
| server2 | True | [] | [] | reference_compatible=False |

server2 `/`: 22972514304 available bytes; 98.72% used; 110410440 free inodes.

server2 `/home`: 22972514304 available bytes; 98.72% used; 110410440 free inodes.

server2 `/tmp`: 22972514304 available bytes; 98.72% used; 110410440 free inodes.

server2 `/var/tmp`: 22972514304 available bytes; 98.72% used; 110410440 free inodes.

server2 `/mnt/raid5`: 464241557504 available bytes; 96.79% used; 445111113 free inodes.
| server3 | True | [] | [] | reference_compatible=True |

server3 `/`: 84340916224 available bytes; 95.29% used; 114156062 free inodes.

server3 `/home`: 84340916224 available bytes; 95.29% used; 114156062 free inodes.

server3 `/data`: 144228536320 available bytes; 98.01% used; 225816968 free inodes.

server3 `/tmp`: 84340916224 available bytes; 95.29% used; 114156062 free inodes.

server3 `/var/tmp`: 84340916224 available bytes; 95.29% used; 114156062 free inodes.
| server4 | True | ['6', '7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 105683181568 available bytes; 94.10% used; 114350901 free inodes.

server4 `/home`: 105683181568 available bytes; 94.10% used; 114350901 free inodes.

server4 `/data`: 38557089792 available bytes; 99.47% used; 224965052 free inodes.

server4 `/tmp`: 105683181568 available bytes; 94.10% used; 114350901 free inodes.

server4 `/var/tmp`: 105683181568 available bytes; 94.10% used; 114350901 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
