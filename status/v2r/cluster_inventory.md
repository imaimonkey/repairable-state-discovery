# V2R cluster inventory

2026-09-25T10:23:09.646211+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | [] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 318836928512 available bytes; 82.21% used; 112480393 free inodes.

server1 `/home`: 318836928512 available bytes; 82.21% used; 112480393 free inodes.

server1 `/tmp`: 318836928512 available bytes; 82.21% used; 112480393 free inodes.

server1 `/var/tmp`: 318836928512 available bytes; 82.21% used; 112480393 free inodes.

server1 `/mnt/raid5`: 364750299136 available bytes; 98.33% used; 337555816 free inodes.
| server2 | True | ['3', '5', '6'] | [] | reference_compatible=False |

server2 `/`: 22833238016 available bytes; 98.73% used; 110410492 free inodes.

server2 `/home`: 22833238016 available bytes; 98.73% used; 110410492 free inodes.

server2 `/tmp`: 22833238016 available bytes; 98.73% used; 110410492 free inodes.

server2 `/var/tmp`: 22833238016 available bytes; 98.73% used; 110410492 free inodes.

server2 `/mnt/raid5`: 316368785408 available bytes; 97.81% used; 445090951 free inodes.
| server3 | True | [] | [] | reference_compatible=True |

server3 `/`: 84416380928 available bytes; 95.29% used; 114156047 free inodes.

server3 `/home`: 84416380928 available bytes; 95.29% used; 114156047 free inodes.

server3 `/data`: 142023249920 available bytes; 98.04% used; 225815934 free inodes.

server3 `/tmp`: 84416380928 available bytes; 95.29% used; 114156047 free inodes.

server3 `/var/tmp`: 84416380928 available bytes; 95.29% used; 114156047 free inodes.
| server4 | True | [] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 105613582336 available bytes; 94.11% used; 114350255 free inodes.

server4 `/home`: 105613582336 available bytes; 94.11% used; 114350255 free inodes.

server4 `/data`: 238453592064 available bytes; 96.70% used; 224988464 free inodes.

server4 `/tmp`: 105613582336 available bytes; 94.11% used; 114350255 free inodes.

server4 `/var/tmp`: 105613582336 available bytes; 94.11% used; 114350255 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
