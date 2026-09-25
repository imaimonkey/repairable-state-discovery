# V2R cluster inventory

2026-09-25T05:40:50.908201+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | [] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 318871883776 available bytes; 82.21% used; 112480333 free inodes.

server1 `/home`: 318871883776 available bytes; 82.21% used; 112480333 free inodes.

server1 `/tmp`: 318871883776 available bytes; 82.21% used; 112480333 free inodes.

server1 `/var/tmp`: 318871883776 available bytes; 82.21% used; 112480333 free inodes.

server1 `/mnt/raid5`: 408466038784 available bytes; 98.13% used; 337566989 free inodes.
| server2 | True | [] | [] | reference_compatible=False |

server2 `/`: 22911823872 available bytes; 98.72% used; 110410433 free inodes.

server2 `/home`: 22911823872 available bytes; 98.72% used; 110410433 free inodes.

server2 `/tmp`: 22911823872 available bytes; 98.72% used; 110410433 free inodes.

server2 `/var/tmp`: 22911823872 available bytes; 98.72% used; 110410433 free inodes.

server2 `/mnt/raid5`: 440034910208 available bytes; 96.96% used; 445102617 free inodes.
| server3 | True | [] | [] | reference_compatible=True |

server3 `/`: 84313419776 available bytes; 95.30% used; 114156039 free inodes.

server3 `/home`: 84313419776 available bytes; 95.30% used; 114156039 free inodes.

server3 `/data`: 142777102336 available bytes; 98.03% used; 225814646 free inodes.

server3 `/tmp`: 84313419776 available bytes; 95.30% used; 114156039 free inodes.

server3 `/var/tmp`: 84313419776 available bytes; 95.30% used; 114156039 free inodes.
| server4 | True | ['3'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 105649680384 available bytes; 94.10% used; 114350392 free inodes.

server4 `/home`: 105649680384 available bytes; 94.10% used; 114350392 free inodes.

server4 `/data`: 24763396096 available bytes; 99.66% used; 224966446 free inodes.

server4 `/tmp`: 105649680384 available bytes; 94.10% used; 114350392 free inodes.

server4 `/var/tmp`: 105649680384 available bytes; 94.10% used; 114350392 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
