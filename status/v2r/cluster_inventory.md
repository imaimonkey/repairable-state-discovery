# V2R cluster inventory

2026-09-25T05:23:52.643119+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | [] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 318873591808 available bytes; 82.21% used; 112480261 free inodes.

server1 `/home`: 318873591808 available bytes; 82.21% used; 112480261 free inodes.

server1 `/tmp`: 318873591808 available bytes; 82.21% used; 112480261 free inodes.

server1 `/var/tmp`: 318873591808 available bytes; 82.21% used; 112480261 free inodes.

server1 `/mnt/raid5`: 408514732032 available bytes; 98.13% used; 337569035 free inodes.
| server2 | True | [] | [] | reference_compatible=False |

server2 `/`: 22924632064 available bytes; 98.72% used; 110410445 free inodes.

server2 `/home`: 22924632064 available bytes; 98.72% used; 110410445 free inodes.

server2 `/tmp`: 22924632064 available bytes; 98.72% used; 110410445 free inodes.

server2 `/var/tmp`: 22924632064 available bytes; 98.72% used; 110410445 free inodes.

server2 `/mnt/raid5`: 461376970752 available bytes; 96.81% used; 445108373 free inodes.
| server3 | True | [] | [] | reference_compatible=True |

server3 `/`: 84312428544 available bytes; 95.30% used; 114156042 free inodes.

server3 `/home`: 84312428544 available bytes; 95.30% used; 114156042 free inodes.

server3 `/data`: 142777438208 available bytes; 98.03% used; 225814934 free inodes.

server3 `/tmp`: 84312428544 available bytes; 95.30% used; 114156042 free inodes.

server3 `/var/tmp`: 84312428544 available bytes; 95.30% used; 114156042 free inodes.
| server4 | True | ['6', '7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 105658626048 available bytes; 94.10% used; 114350403 free inodes.

server4 `/home`: 105658626048 available bytes; 94.10% used; 114350403 free inodes.

server4 `/data`: 26279231488 available bytes; 99.64% used; 224959583 free inodes.

server4 `/tmp`: 105658626048 available bytes; 94.10% used; 114350403 free inodes.

server4 `/var/tmp`: 105658626048 available bytes; 94.10% used; 114350403 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
