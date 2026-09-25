# V2R cluster inventory

2026-09-25T04:48:28.753238+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | [] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 318909181952 available bytes; 82.21% used; 112480348 free inodes.

server1 `/home`: 318909181952 available bytes; 82.21% used; 112480348 free inodes.

server1 `/tmp`: 318909181952 available bytes; 82.21% used; 112480348 free inodes.

server1 `/var/tmp`: 318909181952 available bytes; 82.21% used; 112480348 free inodes.

server1 `/mnt/raid5`: 408678137856 available bytes; 98.13% used; 337589454 free inodes.
| server2 | True | [] | [] | reference_compatible=False |

server2 `/`: 22940991488 available bytes; 98.72% used; 110410438 free inodes.

server2 `/home`: 22940991488 available bytes; 98.72% used; 110410438 free inodes.

server2 `/tmp`: 22940991488 available bytes; 98.72% used; 110410438 free inodes.

server2 `/var/tmp`: 22940991488 available bytes; 98.72% used; 110410438 free inodes.

server2 `/mnt/raid5`: 462471643136 available bytes; 96.80% used; 445109279 free inodes.
| server3 | True | ['3'] | [] | reference_compatible=True |

server3 `/`: 84339449856 available bytes; 95.29% used; 114156096 free inodes.

server3 `/home`: 84339449856 available bytes; 95.29% used; 114156096 free inodes.

server3 `/data`: 143170506752 available bytes; 98.02% used; 225815806 free inodes.

server3 `/tmp`: 84339449856 available bytes; 95.29% used; 114156096 free inodes.

server3 `/var/tmp`: 84339449856 available bytes; 95.29% used; 114156096 free inodes.
| server4 | True | ['6', '7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 105663733760 available bytes; 94.10% used; 114350578 free inodes.

server4 `/home`: 105663733760 available bytes; 94.10% used; 114350578 free inodes.

server4 `/data`: 29552594944 available bytes; 99.59% used; 224961915 free inodes.

server4 `/tmp`: 105663733760 available bytes; 94.10% used; 114350578 free inodes.

server4 `/var/tmp`: 105663733760 available bytes; 94.10% used; 114350578 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
