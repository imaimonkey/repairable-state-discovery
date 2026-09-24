# V2R cluster inventory

2026-09-24T04:28:00.730980+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | ['7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 324699492352 available bytes; 81.89% used; 112493185 free inodes.

server1 `/home`: 324699492352 available bytes; 81.89% used; 112493185 free inodes.

server1 `/tmp`: 324699492352 available bytes; 81.89% used; 112493185 free inodes.

server1 `/var/tmp`: 324699492352 available bytes; 81.89% used; 112493185 free inodes.

server1 `/mnt/raid5`: 445657104384 available bytes; 97.96% used; 337724689 free inodes.
| server2 | True | [] | [] | reference_compatible=False |

server2 `/`: 40784351232 available bytes; 97.72% used; 110430562 free inodes.

server2 `/home`: 40784351232 available bytes; 97.72% used; 110430562 free inodes.

server2 `/tmp`: 40784351232 available bytes; 97.72% used; 110430562 free inodes.

server2 `/var/tmp`: 40784351232 available bytes; 97.72% used; 110430562 free inodes.

server2 `/mnt/raid5`: 524897193984 available bytes; 96.37% used; 445195744 free inodes.
| server3 | True | ['1'] | ['/tmp', '/var/tmp'] | reference_compatible=True |

server3 `/`: 292001841152 available bytes; 83.71% used; 114176140 free inodes.

server3 `/home`: 292001841152 available bytes; 83.71% used; 114176140 free inodes.

server3 `/data`: 29605855232 available bytes; 99.59% used; 225841056 free inodes.

server3 `/tmp`: 292001841152 available bytes; 83.71% used; 114176140 free inodes.

server3 `/var/tmp`: 292001841152 available bytes; 83.71% used; 114176140 free inodes.
| server4 | True | ['7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 105844596736 available bytes; 94.09% used; 114349421 free inodes.

server4 `/home`: 105844596736 available bytes; 94.09% used; 114349421 free inodes.

server4 `/data`: 253766041600 available bytes; 96.49% used; 225381266 free inodes.

server4 `/tmp`: 105844596736 available bytes; 94.09% used; 114349421 free inodes.

server4 `/var/tmp`: 105844596736 available bytes; 94.09% used; 114349421 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
