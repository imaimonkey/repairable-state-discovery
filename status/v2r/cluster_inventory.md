# V2R cluster inventory

2026-09-24T23:59:06.947805+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | [] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 319090663424 available bytes; 82.20% used; 112480778 free inodes.

server1 `/home`: 319090663424 available bytes; 82.20% used; 112480778 free inodes.

server1 `/tmp`: 319090663424 available bytes; 82.20% used; 112480778 free inodes.

server1 `/var/tmp`: 319090663424 available bytes; 82.20% used; 112480778 free inodes.

server1 `/mnt/raid5`: 416914378752 available bytes; 98.09% used; 337623488 free inodes.
| server2 | True | [] | [] | reference_compatible=False |

server2 `/`: 23092625408 available bytes; 98.71% used; 110410789 free inodes.

server2 `/home`: 23092625408 available bytes; 98.71% used; 110410789 free inodes.

server2 `/tmp`: 23092625408 available bytes; 98.71% used; 110410789 free inodes.

server2 `/var/tmp`: 23092625408 available bytes; 98.71% used; 110410789 free inodes.

server2 `/mnt/raid5`: 487397658624 available bytes; 96.63% used; 445164101 free inodes.
| server3 | True | [] | [] | reference_compatible=True |

server3 `/`: 84353679360 available bytes; 95.29% used; 114156084 free inodes.

server3 `/home`: 84353679360 available bytes; 95.29% used; 114156084 free inodes.

server3 `/data`: 149486194688 available bytes; 97.93% used; 225814021 free inodes.

server3 `/tmp`: 84353679360 available bytes; 95.29% used; 114156084 free inodes.

server3 `/var/tmp`: 84353679360 available bytes; 95.29% used; 114156084 free inodes.
| server4 | True | ['7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 105798774784 available bytes; 94.10% used; 114348295 free inodes.

server4 `/home`: 105798774784 available bytes; 94.10% used; 114348295 free inodes.

server4 `/data`: 60760031232 available bytes; 99.16% used; 225104165 free inodes.

server4 `/tmp`: 105798774784 available bytes; 94.10% used; 114348295 free inodes.

server4 `/var/tmp`: 105798774784 available bytes; 94.10% used; 114348295 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
