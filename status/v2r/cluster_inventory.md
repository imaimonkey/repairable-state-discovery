# V2R cluster inventory

2026-09-24T13:59:12.512234+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | [] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 324070449152 available bytes; 81.92% used; 112481666 free inodes.

server1 `/home`: 324070449152 available bytes; 81.92% used; 112481666 free inodes.

server1 `/tmp`: 324070449152 available bytes; 81.92% used; 112481666 free inodes.

server1 `/var/tmp`: 324070449152 available bytes; 81.92% used; 112481666 free inodes.

server1 `/mnt/raid5`: 416970219520 available bytes; 98.09% used; 337671821 free inodes.
| server2 | True | ['7'] | [] | reference_compatible=False |

server2 `/`: 57497243648 available bytes; 96.79% used; 110428419 free inodes.

server2 `/home`: 57497243648 available bytes; 96.79% used; 110428419 free inodes.

server2 `/tmp`: 57497243648 available bytes; 96.79% used; 110428419 free inodes.

server2 `/var/tmp`: 57497243648 available bytes; 96.79% used; 110428419 free inodes.

server2 `/mnt/raid5`: 505731686400 available bytes; 96.51% used; 445168758 free inodes.
| server3 | True | [] | [] | reference_compatible=True |

server3 `/`: 85092675584 available bytes; 95.25% used; 114190422 free inodes.

server3 `/home`: 85092675584 available bytes; 95.25% used; 114190422 free inodes.

server3 `/data`: 161038135296 available bytes; 97.77% used; 225802603 free inodes.

server3 `/tmp`: 85092675584 available bytes; 95.25% used; 114190422 free inodes.

server3 `/var/tmp`: 85092675584 available bytes; 95.25% used; 114190422 free inodes.
| server4 | True | [] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 105760215040 available bytes; 94.10% used; 114348716 free inodes.

server4 `/home`: 105760215040 available bytes; 94.10% used; 114348716 free inodes.

server4 `/data`: 69387137024 available bytes; 99.04% used; 225257160 free inodes.

server4 `/tmp`: 105760215040 available bytes; 94.10% used; 114348716 free inodes.

server4 `/var/tmp`: 105760215040 available bytes; 94.10% used; 114348716 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
