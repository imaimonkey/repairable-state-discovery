# V2R cluster inventory

2026-09-24T15:55:55.647510+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | [] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 324025159680 available bytes; 81.92% used; 112481462 free inodes.

server1 `/home`: 324025159680 available bytes; 81.92% used; 112481462 free inodes.

server1 `/tmp`: 324025159680 available bytes; 81.92% used; 112481462 free inodes.

server1 `/var/tmp`: 324025159680 available bytes; 81.92% used; 112481462 free inodes.

server1 `/mnt/raid5`: 416699154432 available bytes; 98.09% used; 337658175 free inodes.
| server2 | True | ['7'] | [] | reference_compatible=False |

server2 `/`: 57365270528 available bytes; 96.80% used; 110427243 free inodes.

server2 `/home`: 57365270528 available bytes; 96.80% used; 110427243 free inodes.

server2 `/tmp`: 57365270528 available bytes; 96.80% used; 110427243 free inodes.

server2 `/var/tmp`: 57365270528 available bytes; 96.80% used; 110427243 free inodes.

server2 `/mnt/raid5`: 502000177152 available bytes; 96.53% used; 445165054 free inodes.
| server3 | True | ['0'] | [] | reference_compatible=True |

server3 `/`: 84471291904 available bytes; 95.29% used; 114157223 free inodes.

server3 `/home`: 84471291904 available bytes; 95.29% used; 114157223 free inodes.

server3 `/data`: 160111656960 available bytes; 97.79% used; 225806050 free inodes.

server3 `/tmp`: 84471291904 available bytes; 95.29% used; 114157223 free inodes.

server3 `/var/tmp`: 84471291904 available bytes; 95.29% used; 114157223 free inodes.
| server4 | True | [] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 105706762240 available bytes; 94.10% used; 114348610 free inodes.

server4 `/home`: 105706762240 available bytes; 94.10% used; 114348610 free inodes.

server4 `/data`: 89350103040 available bytes; 98.77% used; 225256456 free inodes.

server4 `/tmp`: 105706762240 available bytes; 94.10% used; 114348610 free inodes.

server4 `/var/tmp`: 105706762240 available bytes; 94.10% used; 114348610 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
