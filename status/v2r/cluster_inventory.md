# V2R cluster inventory

2026-09-24T18:00:01.745877+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | ['7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 324009410560 available bytes; 81.92% used; 112481435 free inodes.

server1 `/home`: 324009410560 available bytes; 81.92% used; 112481435 free inodes.

server1 `/tmp`: 324009410560 available bytes; 81.92% used; 112481435 free inodes.

server1 `/var/tmp`: 324009410560 available bytes; 81.92% used; 112481435 free inodes.

server1 `/mnt/raid5`: 416384843776 available bytes; 98.09% used; 337642899 free inodes.
| server2 | True | [] | [] | reference_compatible=False |

server2 `/`: 56892948480 available bytes; 96.83% used; 110412298 free inodes.

server2 `/home`: 56892948480 available bytes; 96.83% used; 110412298 free inodes.

server2 `/tmp`: 56892948480 available bytes; 96.83% used; 110412298 free inodes.

server2 `/var/tmp`: 56892948480 available bytes; 96.83% used; 110412298 free inodes.

server2 `/mnt/raid5`: 497950588928 available bytes; 96.56% used; 445161508 free inodes.
| server3 | True | ['1'] | [] | reference_compatible=True |

server3 `/`: 84410433536 available bytes; 95.29% used; 114156136 free inodes.

server3 `/home`: 84410433536 available bytes; 95.29% used; 114156136 free inodes.

server3 `/data`: 151802712064 available bytes; 97.90% used; 225786254 free inodes.

server3 `/tmp`: 84410433536 available bytes; 95.29% used; 114156136 free inodes.

server3 `/var/tmp`: 84410433536 available bytes; 95.29% used; 114156136 free inodes.
| server4 | True | [] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 105671970816 available bytes; 94.10% used; 114348536 free inodes.

server4 `/home`: 105671970816 available bytes; 94.10% used; 114348536 free inodes.

server4 `/data`: 88685481984 available bytes; 98.77% used; 225253448 free inodes.

server4 `/tmp`: 105671970816 available bytes; 94.10% used; 114348536 free inodes.

server4 `/var/tmp`: 105671970816 available bytes; 94.10% used; 114348536 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
