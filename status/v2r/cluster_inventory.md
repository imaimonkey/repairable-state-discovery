# V2R cluster inventory

2026-09-24T09:02:23.370757+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | [] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 324375101440 available bytes; 81.90% used; 112490132 free inodes.

server1 `/home`: 324375101440 available bytes; 81.90% used; 112490132 free inodes.

server1 `/tmp`: 324375101440 available bytes; 81.90% used; 112490132 free inodes.

server1 `/var/tmp`: 324375101440 available bytes; 81.90% used; 112490132 free inodes.

server1 `/mnt/raid5`: 498840719360 available bytes; 97.71% used; 337716672 free inodes.
| server2 | True | [] | [] | reference_compatible=False |

server2 `/`: 57787772928 available bytes; 96.78% used; 110430971 free inodes.

server2 `/home`: 57787772928 available bytes; 96.78% used; 110430971 free inodes.

server2 `/tmp`: 57787772928 available bytes; 96.78% used; 110430971 free inodes.

server2 `/var/tmp`: 57787772928 available bytes; 96.78% used; 110430971 free inodes.

server2 `/mnt/raid5`: 515456081920 available bytes; 96.44% used; 445178653 free inodes.
| server3 | True | ['0'] | [] | reference_compatible=True |

server3 `/`: 85900476416 available bytes; 95.21% used; 114199589 free inodes.

server3 `/home`: 85900476416 available bytes; 95.21% used; 114199589 free inodes.

server3 `/data`: 167055040512 available bytes; 97.69% used; 225821835 free inodes.

server3 `/tmp`: 85900476416 available bytes; 95.21% used; 114199589 free inodes.

server3 `/var/tmp`: 85900476416 available bytes; 95.21% used; 114199589 free inodes.
| server4 | True | [] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 105759260672 available bytes; 94.10% used; 114349077 free inodes.

server4 `/home`: 105759260672 available bytes; 94.10% used; 114349077 free inodes.

server4 `/data`: 319635300352 available bytes; 95.58% used; 225273398 free inodes.

server4 `/tmp`: 105759260672 available bytes; 94.10% used; 114349077 free inodes.

server4 `/var/tmp`: 105759260672 available bytes; 94.10% used; 114349077 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
