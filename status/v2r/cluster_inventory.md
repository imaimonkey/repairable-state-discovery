# V2R cluster inventory

2026-09-24T17:49:10.959174+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | ['7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 324006612992 available bytes; 81.92% used; 112481425 free inodes.

server1 `/home`: 324006612992 available bytes; 81.92% used; 112481425 free inodes.

server1 `/tmp`: 324006612992 available bytes; 81.92% used; 112481425 free inodes.

server1 `/var/tmp`: 324006612992 available bytes; 81.92% used; 112481425 free inodes.

server1 `/mnt/raid5`: 416405508096 available bytes; 98.09% used; 337644159 free inodes.
| server2 | True | [] | [] | reference_compatible=False |

server2 `/`: 56903340032 available bytes; 96.83% used; 110412358 free inodes.

server2 `/home`: 56903340032 available bytes; 96.83% used; 110412358 free inodes.

server2 `/tmp`: 56903340032 available bytes; 96.83% used; 110412358 free inodes.

server2 `/var/tmp`: 56903340032 available bytes; 96.83% used; 110412358 free inodes.

server2 `/mnt/raid5`: 498283257856 available bytes; 96.56% used; 445162123 free inodes.
| server3 | True | ['1'] | [] | reference_compatible=True |

server3 `/`: 84408221696 available bytes; 95.29% used; 114156138 free inodes.

server3 `/home`: 84408221696 available bytes; 95.29% used; 114156138 free inodes.

server3 `/data`: 151920840704 available bytes; 97.90% used; 225786438 free inodes.

server3 `/tmp`: 84408221696 available bytes; 95.29% used; 114156138 free inodes.

server3 `/var/tmp`: 84408221696 available bytes; 95.29% used; 114156138 free inodes.
| server4 | True | [] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 105672409088 available bytes; 94.10% used; 114348541 free inodes.

server4 `/home`: 105672409088 available bytes; 94.10% used; 114348541 free inodes.

server4 `/data`: 88702517248 available bytes; 98.77% used; 225253643 free inodes.

server4 `/tmp`: 105672409088 available bytes; 94.10% used; 114348541 free inodes.

server4 `/var/tmp`: 105672409088 available bytes; 94.10% used; 114348541 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
