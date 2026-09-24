# V2R cluster inventory

2026-09-24T20:54:17.726719+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | [] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 323978547200 available bytes; 81.93% used; 112481430 free inodes.

server1 `/home`: 323978547200 available bytes; 81.93% used; 112481430 free inodes.

server1 `/tmp`: 323978547200 available bytes; 81.93% used; 112481430 free inodes.

server1 `/var/tmp`: 323978547200 available bytes; 81.93% used; 112481430 free inodes.

server1 `/mnt/raid5`: 415573209088 available bytes; 98.09% used; 337631635 free inodes.
| server2 | True | ['7'] | [] | reference_compatible=False |

server2 `/`: 30144413696 available bytes; 98.32% used; 110411380 free inodes.

server2 `/home`: 30144413696 available bytes; 98.32% used; 110411380 free inodes.

server2 `/tmp`: 30144413696 available bytes; 98.32% used; 110411380 free inodes.

server2 `/var/tmp`: 30144413696 available bytes; 98.32% used; 110411380 free inodes.

server2 `/mnt/raid5`: 491536101376 available bytes; 96.60% used; 445156226 free inodes.
| server3 | True | [] | [] | reference_compatible=True |

server3 `/`: 84386230272 available bytes; 95.29% used; 114156105 free inodes.

server3 `/home`: 84386230272 available bytes; 95.29% used; 114156105 free inodes.

server3 `/data`: 151056281600 available bytes; 97.91% used; 225803869 free inodes.

server3 `/tmp`: 84386230272 available bytes; 95.29% used; 114156105 free inodes.

server3 `/var/tmp`: 84386230272 available bytes; 95.29% used; 114156105 free inodes.
| server4 | True | ['4'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 105639325696 available bytes; 94.10% used; 114348379 free inodes.

server4 `/home`: 105639325696 available bytes; 94.10% used; 114348379 free inodes.

server4 `/data`: 78613176320 available bytes; 98.91% used; 225255663 free inodes.

server4 `/tmp`: 105639325696 available bytes; 94.10% used; 114348379 free inodes.

server4 `/var/tmp`: 105639325696 available bytes; 94.10% used; 114348379 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
