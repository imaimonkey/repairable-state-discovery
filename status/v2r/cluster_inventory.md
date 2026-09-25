# V2R cluster inventory

2026-09-25T12:54:31.394466+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | [] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 319110995968 available bytes; 82.20% used; 112477584 free inodes.

server1 `/home`: 319110995968 available bytes; 82.20% used; 112477584 free inodes.

server1 `/tmp`: 319110995968 available bytes; 82.20% used; 112477584 free inodes.

server1 `/var/tmp`: 319110995968 available bytes; 82.20% used; 112477584 free inodes.

server1 `/mnt/raid5`: 364476469248 available bytes; 98.33% used; 337547954 free inodes.
| server2 | True | ['3', '4', '5', '6'] | [] | reference_compatible=False |

server2 `/`: 8814678016 available bytes; 99.51% used; 110408829 free inodes.

server2 `/home`: 8814678016 available bytes; 99.51% used; 110408829 free inodes.

server2 `/tmp`: 8814678016 available bytes; 99.51% used; 110408829 free inodes.

server2 `/var/tmp`: 8814678016 available bytes; 99.51% used; 110408829 free inodes.

server2 `/mnt/raid5`: 324499668992 available bytes; 97.76% used; 445078127 free inodes.
| server3 | True | [] | [] | reference_compatible=True |

server3 `/`: 84208099328 available bytes; 95.30% used; 114154980 free inodes.

server3 `/home`: 84208099328 available bytes; 95.30% used; 114154980 free inodes.

server3 `/data`: 142271815680 available bytes; 98.03% used; 225810810 free inodes.

server3 `/tmp`: 84208099328 available bytes; 95.30% used; 114154980 free inodes.

server3 `/var/tmp`: 84208099328 available bytes; 95.30% used; 114154980 free inodes.
| server4 | True | [] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 105665372160 available bytes; 94.10% used; 114349707 free inodes.

server4 `/home`: 105665372160 available bytes; 94.10% used; 114349707 free inodes.

server4 `/data`: 232006864896 available bytes; 96.79% used; 224960854 free inodes.

server4 `/tmp`: 105665372160 available bytes; 94.10% used; 114349707 free inodes.

server4 `/var/tmp`: 105665372160 available bytes; 94.10% used; 114349707 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
