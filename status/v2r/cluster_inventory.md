# V2R cluster inventory

2026-09-25T10:43:03.122811+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | [] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 318990176256 available bytes; 82.20% used; 112479395 free inodes.

server1 `/home`: 318990176256 available bytes; 82.20% used; 112479395 free inodes.

server1 `/tmp`: 318990176256 available bytes; 82.20% used; 112479395 free inodes.

server1 `/var/tmp`: 318990176256 available bytes; 82.20% used; 112479395 free inodes.

server1 `/mnt/raid5`: 364830580736 available bytes; 98.33% used; 337555267 free inodes.
| server2 | True | ['0', '2', '3', '5', '6'] | [] | reference_compatible=False |

server2 `/`: 22826467328 available bytes; 98.73% used; 110410500 free inodes.

server2 `/home`: 22826467328 available bytes; 98.73% used; 110410500 free inodes.

server2 `/tmp`: 22826467328 available bytes; 98.73% used; 110410500 free inodes.

server2 `/var/tmp`: 22826467328 available bytes; 98.73% used; 110410500 free inodes.

server2 `/mnt/raid5`: 294659600384 available bytes; 97.96% used; 445089537 free inodes.
| server3 | True | [] | [] | reference_compatible=True |

server3 `/`: 84422119424 available bytes; 95.29% used; 114156041 free inodes.

server3 `/home`: 84422119424 available bytes; 95.29% used; 114156041 free inodes.

server3 `/data`: 142005428224 available bytes; 98.04% used; 225815517 free inodes.

server3 `/tmp`: 84422119424 available bytes; 95.29% used; 114156041 free inodes.

server3 `/var/tmp`: 84422119424 available bytes; 95.29% used; 114156041 free inodes.
| server4 | True | [] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 105612980224 available bytes; 94.11% used; 114350251 free inodes.

server4 `/home`: 105612980224 available bytes; 94.11% used; 114350251 free inodes.

server4 `/data`: 238512132096 available bytes; 96.70% used; 224985883 free inodes.

server4 `/tmp`: 105612980224 available bytes; 94.11% used; 114350251 free inodes.

server4 `/var/tmp`: 105612980224 available bytes; 94.11% used; 114350251 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
