# V2R cluster inventory

2026-09-25T10:30:49.796910+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | [] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 318919233536 available bytes; 82.21% used; 112479892 free inodes.

server1 `/home`: 318919233536 available bytes; 82.21% used; 112479892 free inodes.

server1 `/tmp`: 318919233536 available bytes; 82.21% used; 112479892 free inodes.

server1 `/var/tmp`: 318919233536 available bytes; 82.21% used; 112479892 free inodes.

server1 `/mnt/raid5`: 364839342080 available bytes; 98.33% used; 337555271 free inodes.
| server2 | True | ['3', '5', '6'] | [] | reference_compatible=False |

server2 `/`: 22826024960 available bytes; 98.73% used; 110410492 free inodes.

server2 `/home`: 22826024960 available bytes; 98.73% used; 110410492 free inodes.

server2 `/tmp`: 22826024960 available bytes; 98.73% used; 110410492 free inodes.

server2 `/var/tmp`: 22826024960 available bytes; 98.73% used; 110410492 free inodes.

server2 `/mnt/raid5`: 316198989824 available bytes; 97.82% used; 445090085 free inodes.
| server3 | True | [] | [] | reference_compatible=True |

server3 `/`: 84417396736 available bytes; 95.29% used; 114156047 free inodes.

server3 `/home`: 84417396736 available bytes; 95.29% used; 114156047 free inodes.

server3 `/data`: 142018805760 available bytes; 98.04% used; 225815735 free inodes.

server3 `/tmp`: 84417396736 available bytes; 95.29% used; 114156047 free inodes.

server3 `/var/tmp`: 84417396736 available bytes; 95.29% used; 114156047 free inodes.
| server4 | True | [] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 105613332480 available bytes; 94.11% used; 114350251 free inodes.

server4 `/home`: 105613332480 available bytes; 94.11% used; 114350251 free inodes.

server4 `/data`: 238445121536 available bytes; 96.70% used; 224987525 free inodes.

server4 `/tmp`: 105613332480 available bytes; 94.11% used; 114350251 free inodes.

server4 `/var/tmp`: 105613332480 available bytes; 94.11% used; 114350251 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
