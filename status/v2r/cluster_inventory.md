# V2R cluster inventory

2026-09-25T04:22:10.572010+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | [] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 318928805888 available bytes; 82.21% used; 112480373 free inodes.

server1 `/home`: 318928805888 available bytes; 82.21% used; 112480373 free inodes.

server1 `/tmp`: 318928805888 available bytes; 82.21% used; 112480373 free inodes.

server1 `/var/tmp`: 318928805888 available bytes; 82.21% used; 112480373 free inodes.

server1 `/mnt/raid5`: 369580507136 available bytes; 98.30% used; 337592660 free inodes.
| server2 | True | [] | [] | reference_compatible=False |

server2 `/`: 22956441600 available bytes; 98.72% used; 110410442 free inodes.

server2 `/home`: 22956441600 available bytes; 98.72% used; 110410442 free inodes.

server2 `/tmp`: 22956441600 available bytes; 98.72% used; 110410442 free inodes.

server2 `/var/tmp`: 22956441600 available bytes; 98.72% used; 110410442 free inodes.

server2 `/mnt/raid5`: 463286956032 available bytes; 96.80% used; 445110187 free inodes.
| server3 | True | [] | [] | reference_compatible=True |

server3 `/`: 84340539392 available bytes; 95.29% used; 114156072 free inodes.

server3 `/home`: 84340539392 available bytes; 95.29% used; 114156072 free inodes.

server3 `/data`: 143714693120 available bytes; 98.01% used; 225816292 free inodes.

server3 `/tmp`: 84340539392 available bytes; 95.29% used; 114156072 free inodes.

server3 `/var/tmp`: 84340539392 available bytes; 95.29% used; 114156072 free inodes.
| server4 | True | ['6', '7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 105673850880 available bytes; 94.10% used; 114350881 free inodes.

server4 `/home`: 105673850880 available bytes; 94.10% used; 114350881 free inodes.

server4 `/data`: 32811102208 available bytes; 99.55% used; 224963333 free inodes.

server4 `/tmp`: 105673850880 available bytes; 94.10% used; 114350881 free inodes.

server4 `/var/tmp`: 105673850880 available bytes; 94.10% used; 114350881 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
