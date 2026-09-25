# V2R cluster inventory

2026-09-25T05:51:37.143864+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | [] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 318870167552 available bytes; 82.21% used; 112480335 free inodes.

server1 `/home`: 318870167552 available bytes; 82.21% used; 112480335 free inodes.

server1 `/tmp`: 318870167552 available bytes; 82.21% used; 112480335 free inodes.

server1 `/var/tmp`: 318870167552 available bytes; 82.21% used; 112480335 free inodes.

server1 `/mnt/raid5`: 408436396032 available bytes; 98.13% used; 337565706 free inodes.
| server2 | True | [] | [] | reference_compatible=False |

server2 `/`: 22911692800 available bytes; 98.72% used; 110410371 free inodes.

server2 `/home`: 22911692800 available bytes; 98.72% used; 110410371 free inodes.

server2 `/tmp`: 22911692800 available bytes; 98.72% used; 110410371 free inodes.

server2 `/var/tmp`: 22911692800 available bytes; 98.72% used; 110410371 free inodes.

server2 `/mnt/raid5`: 409015246848 available bytes; 97.17% used; 445101784 free inodes.
| server3 | True | [] | [] | reference_compatible=True |

server3 `/`: 84312788992 available bytes; 95.30% used; 114156039 free inodes.

server3 `/home`: 84312788992 available bytes; 95.30% used; 114156039 free inodes.

server3 `/data`: 142774509568 available bytes; 98.03% used; 225814444 free inodes.

server3 `/tmp`: 84312788992 available bytes; 95.30% used; 114156039 free inodes.

server3 `/var/tmp`: 84312788992 available bytes; 95.30% used; 114156039 free inodes.
| server4 | True | ['3'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 105649360896 available bytes; 94.10% used; 114350388 free inodes.

server4 `/home`: 105649360896 available bytes; 94.10% used; 114350388 free inodes.

server4 `/data`: 256306094080 available bytes; 96.46% used; 225027143 free inodes.

server4 `/tmp`: 105649360896 available bytes; 94.10% used; 114350388 free inodes.

server4 `/var/tmp`: 105649360896 available bytes; 94.10% used; 114350388 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
