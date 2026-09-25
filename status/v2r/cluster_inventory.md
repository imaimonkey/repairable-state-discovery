# V2R cluster inventory

2026-09-25T09:54:05.075169+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | [] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 318837510144 available bytes; 82.21% used; 112480393 free inodes.

server1 `/home`: 318837510144 available bytes; 82.21% used; 112480393 free inodes.

server1 `/tmp`: 318837510144 available bytes; 82.21% used; 112480393 free inodes.

server1 `/var/tmp`: 318837510144 available bytes; 82.21% used; 112480393 free inodes.

server1 `/mnt/raid5`: 357282250752 available bytes; 98.36% used; 337556894 free inodes.
| server2 | True | ['6'] | [] | reference_compatible=False |

server2 `/`: 22833541120 available bytes; 98.73% used; 110410482 free inodes.

server2 `/home`: 22833541120 available bytes; 98.73% used; 110410482 free inodes.

server2 `/tmp`: 22833541120 available bytes; 98.73% used; 110410482 free inodes.

server2 `/var/tmp`: 22833541120 available bytes; 98.73% used; 110410482 free inodes.

server2 `/mnt/raid5`: 310377852928 available bytes; 97.86% used; 445091780 free inodes.
| server3 | True | [] | [] | reference_compatible=True |

server3 `/`: 84417810432 available bytes; 95.29% used; 114156039 free inodes.

server3 `/home`: 84417810432 available bytes; 95.29% used; 114156039 free inodes.

server3 `/data`: 142294310912 available bytes; 98.03% used; 225810230 free inodes.

server3 `/tmp`: 84417810432 available bytes; 95.29% used; 114156039 free inodes.

server3 `/var/tmp`: 84417810432 available bytes; 95.29% used; 114156039 free inodes.
| server4 | True | [] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 105614581760 available bytes; 94.11% used; 114350276 free inodes.

server4 `/home`: 105614581760 available bytes; 94.11% used; 114350276 free inodes.

server4 `/data`: 240034328576 available bytes; 96.68% used; 224992508 free inodes.

server4 `/tmp`: 105614581760 available bytes; 94.11% used; 114350276 free inodes.

server4 `/var/tmp`: 105614581760 available bytes; 94.11% used; 114350276 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
