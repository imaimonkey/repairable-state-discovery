# V2R cluster inventory

2026-09-25T20:36:11.964941+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | [] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 318707904512 available bytes; 82.22% used; 112476322 free inodes.

server1 `/home`: 318707904512 available bytes; 82.22% used; 112476322 free inodes.

server1 `/tmp`: 318707904512 available bytes; 82.22% used; 112476322 free inodes.

server1 `/var/tmp`: 318707904512 available bytes; 82.22% used; 112476322 free inodes.

server1 `/mnt/raid5`: 369382027264 available bytes; 98.31% used; 337540453 free inodes.
| server2 | True | ['3', '4', '5', '6'] | [] | reference_compatible=False |

server2 `/`: 23046410240 available bytes; 98.71% used; 110407150 free inodes.

server2 `/home`: 23046410240 available bytes; 98.71% used; 110407150 free inodes.

server2 `/tmp`: 23046410240 available bytes; 98.71% used; 110407150 free inodes.

server2 `/var/tmp`: 23046410240 available bytes; 98.71% used; 110407150 free inodes.

server2 `/mnt/raid5`: 303110045696 available bytes; 97.91% used; 445057162 free inodes.
| server3 | True | [] | [] | reference_compatible=True |

server3 `/`: 84381241344 available bytes; 95.29% used; 114152624 free inodes.

server3 `/home`: 84381241344 available bytes; 95.29% used; 114152624 free inodes.

server3 `/data`: 127171497984 available bytes; 98.24% used; 225807938 free inodes.

server3 `/tmp`: 84381241344 available bytes; 95.29% used; 114152624 free inodes.

server3 `/var/tmp`: 84381241344 available bytes; 95.29% used; 114152624 free inodes.
| server4 | True | ['2', '3', '6', '7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 105655910400 available bytes; 94.10% used; 114349549 free inodes.

server4 `/home`: 105655910400 available bytes; 94.10% used; 114349549 free inodes.

server4 `/data`: 228333260800 available bytes; 96.84% used; 224928551 free inodes.

server4 `/tmp`: 105655910400 available bytes; 94.10% used; 114349549 free inodes.

server4 `/var/tmp`: 105655910400 available bytes; 94.10% used; 114349549 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
