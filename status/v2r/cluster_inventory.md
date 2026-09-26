# V2R cluster inventory

2026-09-26T05:19:45.511588+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | ['1', '4', '5', '6', '7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 318399942656 available bytes; 82.24% used; 112476279 free inodes.

server1 `/home`: 318399942656 available bytes; 82.24% used; 112476279 free inodes.

server1 `/tmp`: 318399942656 available bytes; 82.24% used; 112476279 free inodes.

server1 `/var/tmp`: 318399942656 available bytes; 82.24% used; 112476279 free inodes.

server1 `/mnt/raid5`: 298740850688 available bytes; 98.63% used; 337542750 free inodes.
| server2 | True | ['2'] | [] | reference_compatible=False |

server2 `/`: 22920712192 available bytes; 98.72% used; 110406207 free inodes.

server2 `/home`: 22920712192 available bytes; 98.72% used; 110406207 free inodes.

server2 `/tmp`: 22920712192 available bytes; 98.72% used; 110406207 free inodes.

server2 `/var/tmp`: 22920712192 available bytes; 98.72% used; 110406207 free inodes.

server2 `/mnt/raid5`: 283983163392 available bytes; 98.04% used; 445048994 free inodes.
| server3 | True | [] | [] | reference_compatible=True |

server3 `/`: 84086116352 available bytes; 95.31% used; 114166159 free inodes.

server3 `/home`: 84086116352 available bytes; 95.31% used; 114166159 free inodes.

server3 `/data`: 124361768960 available bytes; 98.28% used; 225824926 free inodes.

server3 `/tmp`: 84086116352 available bytes; 95.31% used; 114166159 free inodes.

server3 `/var/tmp`: 84086116352 available bytes; 95.31% used; 114166159 free inodes.
| server4 | True | ['2', '3', '6', '7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 106095230976 available bytes; 94.08% used; 114348206 free inodes.

server4 `/home`: 106095230976 available bytes; 94.08% used; 114348206 free inodes.

server4 `/data`: 106996502528 available bytes; 98.52% used; 224929211 free inodes.

server4 `/tmp`: 106095230976 available bytes; 94.08% used; 114348206 free inodes.

server4 `/var/tmp`: 106095230976 available bytes; 94.08% used; 114348206 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
