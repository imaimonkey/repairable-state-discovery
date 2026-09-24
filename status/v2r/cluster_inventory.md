# V2R cluster inventory

2026-09-24T07:34:13.545665+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | ['5', '7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 324450082816 available bytes; 81.90% used; 112491105 free inodes.

server1 `/home`: 324450082816 available bytes; 81.90% used; 112491105 free inodes.

server1 `/tmp`: 324450082816 available bytes; 81.90% used; 112491105 free inodes.

server1 `/var/tmp`: 324450082816 available bytes; 81.90% used; 112491105 free inodes.

server1 `/mnt/raid5`: 517412065280 available bytes; 97.63% used; 337722785 free inodes.
| server2 | True | [] | [] | reference_compatible=False |

server2 `/`: 57841889280 available bytes; 96.77% used; 110431154 free inodes.

server2 `/home`: 57841889280 available bytes; 96.77% used; 110431154 free inodes.

server2 `/tmp`: 57841889280 available bytes; 96.77% used; 110431154 free inodes.

server2 `/var/tmp`: 57841889280 available bytes; 96.77% used; 110431154 free inodes.

server2 `/mnt/raid5`: 518134771712 available bytes; 96.42% used; 445180695 free inodes.
| server3 | True | [] | ['/tmp', '/var/tmp'] | reference_compatible=True |

server3 `/`: 126782291968 available bytes; 92.93% used; 114174982 free inodes.

server3 `/home`: 126782291968 available bytes; 92.93% used; 114174982 free inodes.

server3 `/data`: 138754916352 available bytes; 98.08% used; 225833685 free inodes.

server3 `/tmp`: 126782291968 available bytes; 92.93% used; 114174982 free inodes.

server3 `/var/tmp`: 126782291968 available bytes; 92.93% used; 114174982 free inodes.
| server4 | True | [] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 105780572160 available bytes; 94.10% used; 114349185 free inodes.

server4 `/home`: 105780572160 available bytes; 94.10% used; 114349185 free inodes.

server4 `/data`: 285806592000 available bytes; 96.05% used; 225366870 free inodes.

server4 `/tmp`: 105780572160 available bytes; 94.10% used; 114349185 free inodes.

server4 `/var/tmp`: 105780572160 available bytes; 94.10% used; 114349185 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
