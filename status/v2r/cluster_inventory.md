# V2R cluster inventory

2026-09-24T18:10:48.576696+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | ['7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 324007096320 available bytes; 81.92% used; 112481437 free inodes.

server1 `/home`: 324007096320 available bytes; 81.92% used; 112481437 free inodes.

server1 `/tmp`: 324007096320 available bytes; 81.92% used; 112481437 free inodes.

server1 `/var/tmp`: 324007096320 available bytes; 81.92% used; 112481437 free inodes.

server1 `/mnt/raid5`: 416362315776 available bytes; 98.09% used; 337641634 free inodes.
| server2 | True | ['7'] | [] | reference_compatible=False |

server2 `/`: 54506659840 available bytes; 96.96% used; 110412098 free inodes.

server2 `/home`: 54506659840 available bytes; 96.96% used; 110412098 free inodes.

server2 `/tmp`: 54506659840 available bytes; 96.96% used; 110412098 free inodes.

server2 `/var/tmp`: 54506659840 available bytes; 96.96% used; 110412098 free inodes.

server2 `/mnt/raid5`: 497325297664 available bytes; 96.56% used; 445161106 free inodes.
| server3 | True | ['1'] | [] | reference_compatible=True |

server3 `/`: 84407070720 available bytes; 95.29% used; 114156134 free inodes.

server3 `/home`: 84407070720 available bytes; 95.29% used; 114156134 free inodes.

server3 `/data`: 151698276352 available bytes; 97.90% used; 225786074 free inodes.

server3 `/tmp`: 84407070720 available bytes; 95.29% used; 114156134 free inodes.

server3 `/var/tmp`: 84407070720 available bytes; 95.29% used; 114156134 free inodes.
| server4 | True | [] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 105663143936 available bytes; 94.10% used; 114348531 free inodes.

server4 `/home`: 105663143936 available bytes; 94.10% used; 114348531 free inodes.

server4 `/data`: 88666775552 available bytes; 98.77% used; 225253285 free inodes.

server4 `/tmp`: 105663143936 available bytes; 94.10% used; 114348531 free inodes.

server4 `/var/tmp`: 105663143936 available bytes; 94.10% used; 114348531 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
