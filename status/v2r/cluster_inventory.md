# V2R cluster inventory

2026-09-25T05:22:19.773477+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | [] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 318876323840 available bytes; 82.21% used; 112480262 free inodes.

server1 `/home`: 318876323840 available bytes; 82.21% used; 112480262 free inodes.

server1 `/tmp`: 318876323840 available bytes; 82.21% used; 112480262 free inodes.

server1 `/var/tmp`: 318876323840 available bytes; 82.21% used; 112480262 free inodes.

server1 `/mnt/raid5`: 408517877760 available bytes; 98.13% used; 337569222 free inodes.
| server2 | True | [] | [] | reference_compatible=False |

server2 `/`: 22925529088 available bytes; 98.72% used; 110410445 free inodes.

server2 `/home`: 22925529088 available bytes; 98.72% used; 110410445 free inodes.

server2 `/tmp`: 22925529088 available bytes; 98.72% used; 110410445 free inodes.

server2 `/var/tmp`: 22925529088 available bytes; 98.72% used; 110410445 free inodes.

server2 `/mnt/raid5`: 461425852416 available bytes; 96.81% used; 445108444 free inodes.
| server3 | True | [] | [] | reference_compatible=True |

server3 `/`: 84321079296 available bytes; 95.29% used; 114156042 free inodes.

server3 `/home`: 84321079296 available bytes; 95.29% used; 114156042 free inodes.

server3 `/data`: 142777921536 available bytes; 98.03% used; 225814967 free inodes.

server3 `/tmp`: 84321079296 available bytes; 95.29% used; 114156042 free inodes.

server3 `/var/tmp`: 84321079296 available bytes; 95.29% used; 114156042 free inodes.
| server4 | True | ['6', '7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 105658671104 available bytes; 94.10% used; 114350403 free inodes.

server4 `/home`: 105658671104 available bytes; 94.10% used; 114350403 free inodes.

server4 `/data`: 26284048384 available bytes; 99.64% used; 224959745 free inodes.

server4 `/tmp`: 105658671104 available bytes; 94.10% used; 114350403 free inodes.

server4 `/var/tmp`: 105658671104 available bytes; 94.10% used; 114350403 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
