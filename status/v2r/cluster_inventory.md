# V2R cluster inventory

2026-09-24T06:19:34.611643+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | ['3', '7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 324514729984 available bytes; 81.90% used; 112491755 free inodes.

server1 `/home`: 324514729984 available bytes; 81.90% used; 112491755 free inodes.

server1 `/tmp`: 324514729984 available bytes; 81.90% used; 112491755 free inodes.

server1 `/var/tmp`: 324514729984 available bytes; 81.90% used; 112491755 free inodes.

server1 `/mnt/raid5`: 517576441856 available bytes; 97.63% used; 337723766 free inodes.
| server2 | True | [] | [] | reference_compatible=False |

server2 `/`: 57892052992 available bytes; 96.77% used; 110431235 free inodes.

server2 `/home`: 57892052992 available bytes; 96.77% used; 110431235 free inodes.

server2 `/tmp`: 57892052992 available bytes; 96.77% used; 110431235 free inodes.

server2 `/var/tmp`: 57892052992 available bytes; 96.77% used; 110431235 free inodes.

server2 `/mnt/raid5`: 520575651840 available bytes; 96.40% used; 445192226 free inodes.
| server3 | True | [] | ['/tmp', '/var/tmp'] | reference_compatible=True |

server3 `/`: 127167819776 available bytes; 92.90% used; 114196692 free inodes.

server3 `/home`: 127167819776 available bytes; 92.90% used; 114196692 free inodes.

server3 `/data`: 140599058432 available bytes; 98.06% used; 225835967 free inodes.

server3 `/tmp`: 127167819776 available bytes; 92.90% used; 114196692 free inodes.

server3 `/var/tmp`: 127167819776 available bytes; 92.90% used; 114196692 free inodes.
| server4 | True | ['1'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 105806000128 available bytes; 94.10% used; 114349291 free inodes.

server4 `/home`: 105806000128 available bytes; 94.10% used; 114349291 free inodes.

server4 `/data`: 335896752128 available bytes; 95.36% used; 225373593 free inodes.

server4 `/tmp`: 105806000128 available bytes; 94.10% used; 114349291 free inodes.

server4 `/var/tmp`: 105806000128 available bytes; 94.10% used; 114349291 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
