# V2R cluster inventory

2026-09-25T10:47:38.203934+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | [] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 318982176768 available bytes; 82.21% used; 112479397 free inodes.

server1 `/home`: 318982176768 available bytes; 82.21% used; 112479397 free inodes.

server1 `/tmp`: 318982176768 available bytes; 82.21% used; 112479397 free inodes.

server1 `/var/tmp`: 318982176768 available bytes; 82.21% used; 112479397 free inodes.

server1 `/mnt/raid5`: 365445943296 available bytes; 98.32% used; 337555246 free inodes.
| server2 | True | ['1', '2', '3', '5', '6'] | [] | reference_compatible=False |

server2 `/`: 22915305472 available bytes; 98.72% used; 110409990 free inodes.

server2 `/home`: 22915305472 available bytes; 98.72% used; 110409990 free inodes.

server2 `/tmp`: 22915305472 available bytes; 98.72% used; 110409990 free inodes.

server2 `/var/tmp`: 22915305472 available bytes; 98.72% used; 110409990 free inodes.

server2 `/mnt/raid5`: 329463701504 available bytes; 97.72% used; 445089414 free inodes.
| server3 | True | [] | [] | reference_compatible=True |

server3 `/`: 84421296128 available bytes; 95.29% used; 114156041 free inodes.

server3 `/home`: 84421296128 available bytes; 95.29% used; 114156041 free inodes.

server3 `/data`: 142012178432 available bytes; 98.04% used; 225815429 free inodes.

server3 `/tmp`: 84421296128 available bytes; 95.29% used; 114156041 free inodes.

server3 `/var/tmp`: 84421296128 available bytes; 95.29% used; 114156041 free inodes.
| server4 | True | [] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 105612861440 available bytes; 94.11% used; 114350251 free inodes.

server4 `/home`: 105612861440 available bytes; 94.11% used; 114350251 free inodes.

server4 `/data`: 238504853504 available bytes; 96.70% used; 224985543 free inodes.

server4 `/tmp`: 105612861440 available bytes; 94.11% used; 114350251 free inodes.

server4 `/var/tmp`: 105612861440 available bytes; 94.11% used; 114350251 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
