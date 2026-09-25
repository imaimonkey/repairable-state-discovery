# V2R cluster inventory

2026-09-25T21:08:15.623537+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | ['4', '6', '7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 318697693184 available bytes; 82.22% used; 112476322 free inodes.

server1 `/home`: 318697693184 available bytes; 82.22% used; 112476322 free inodes.

server1 `/tmp`: 318697693184 available bytes; 82.22% used; 112476322 free inodes.

server1 `/var/tmp`: 318697693184 available bytes; 82.22% used; 112476322 free inodes.

server1 `/mnt/raid5`: 368604471296 available bytes; 98.31% used; 337539496 free inodes.
| server2 | True | ['6'] | [] | reference_compatible=False |

server2 `/`: 22889598976 available bytes; 98.72% used; 110405682 free inodes.

server2 `/home`: 22889598976 available bytes; 98.72% used; 110405682 free inodes.

server2 `/tmp`: 22889598976 available bytes; 98.72% used; 110405682 free inodes.

server2 `/var/tmp`: 22889598976 available bytes; 98.72% used; 110405682 free inodes.

server2 `/mnt/raid5`: 302175989760 available bytes; 97.91% used; 445055728 free inodes.
| server3 | True | [] | [] | reference_compatible=True |

server3 `/`: 84366389248 available bytes; 95.29% used; 114152624 free inodes.

server3 `/home`: 84366389248 available bytes; 95.29% used; 114152624 free inodes.

server3 `/data`: 125906354176 available bytes; 98.26% used; 225807355 free inodes.

server3 `/tmp`: 84366389248 available bytes; 95.29% used; 114152624 free inodes.

server3 `/var/tmp`: 84366389248 available bytes; 95.29% used; 114152624 free inodes.
| server4 | True | ['3', '7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 105388191744 available bytes; 94.12% used; 114347327 free inodes.

server4 `/home`: 105388191744 available bytes; 94.12% used; 114347327 free inodes.

server4 `/data`: 218508353536 available bytes; 96.98% used; 224920839 free inodes.

server4 `/tmp`: 105388191744 available bytes; 94.12% used; 114347327 free inodes.

server4 `/var/tmp`: 105388191744 available bytes; 94.12% used; 114347327 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
