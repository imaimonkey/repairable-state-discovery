# V2R cluster inventory

2026-09-25T12:31:37.058934+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | [] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 319124942848 available bytes; 82.20% used; 112477609 free inodes.

server1 `/home`: 319124942848 available bytes; 82.20% used; 112477609 free inodes.

server1 `/tmp`: 319124942848 available bytes; 82.20% used; 112477609 free inodes.

server1 `/var/tmp`: 319124942848 available bytes; 82.20% used; 112477609 free inodes.

server1 `/mnt/raid5`: 364281757696 available bytes; 98.33% used; 337548126 free inodes.
| server2 | True | ['2', '3', '4', '5', '6'] | [] | reference_compatible=False |

server2 `/`: 22893793280 available bytes; 98.72% used; 110409951 free inodes.

server2 `/home`: 22893793280 available bytes; 98.72% used; 110409951 free inodes.

server2 `/tmp`: 22893793280 available bytes; 98.72% used; 110409951 free inodes.

server2 `/var/tmp`: 22893793280 available bytes; 98.72% used; 110409951 free inodes.

server2 `/mnt/raid5`: 324542894080 available bytes; 97.76% used; 445079559 free inodes.
| server3 | True | [] | [] | reference_compatible=True |

server3 `/`: 84210094080 available bytes; 95.30% used; 114154976 free inodes.

server3 `/home`: 84210094080 available bytes; 95.30% used; 114154976 free inodes.

server3 `/data`: 142279843840 available bytes; 98.03% used; 225811186 free inodes.

server3 `/tmp`: 84210094080 available bytes; 95.30% used; 114154976 free inodes.

server3 `/var/tmp`: 84210094080 available bytes; 95.30% used; 114154976 free inodes.
| server4 | True | [] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 105666097152 available bytes; 94.10% used; 114349722 free inodes.

server4 `/home`: 105666097152 available bytes; 94.10% used; 114349722 free inodes.

server4 `/data`: 232025993216 available bytes; 96.79% used; 224964323 free inodes.

server4 `/tmp`: 105666097152 available bytes; 94.10% used; 114349722 free inodes.

server4 `/var/tmp`: 105666097152 available bytes; 94.10% used; 114349722 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
