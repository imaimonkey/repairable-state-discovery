# V2R cluster inventory

2026-09-24T18:06:11.258438+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | ['7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 324007755776 available bytes; 81.92% used; 112481435 free inodes.

server1 `/home`: 324007755776 available bytes; 81.92% used; 112481435 free inodes.

server1 `/tmp`: 324007755776 available bytes; 81.92% used; 112481435 free inodes.

server1 `/var/tmp`: 324007755776 available bytes; 81.92% used; 112481435 free inodes.

server1 `/mnt/raid5`: 416374861824 available bytes; 98.09% used; 337642174 free inodes.
| server2 | True | ['7'] | [] | reference_compatible=False |

server2 `/`: 54508216320 available bytes; 96.96% used; 110412120 free inodes.

server2 `/home`: 54508216320 available bytes; 96.96% used; 110412120 free inodes.

server2 `/tmp`: 54508216320 available bytes; 96.96% used; 110412120 free inodes.

server2 `/var/tmp`: 54508216320 available bytes; 96.96% used; 110412120 free inodes.

server2 `/mnt/raid5`: 496928280576 available bytes; 96.57% used; 445161361 free inodes.
| server3 | True | ['1'] | [] | reference_compatible=True |

server3 `/`: 84407554048 available bytes; 95.29% used; 114156134 free inodes.

server3 `/home`: 84407554048 available bytes; 95.29% used; 114156134 free inodes.

server3 `/data`: 151750139904 available bytes; 97.90% used; 225786151 free inodes.

server3 `/tmp`: 84407554048 available bytes; 95.29% used; 114156134 free inodes.

server3 `/var/tmp`: 84407554048 available bytes; 95.29% used; 114156134 free inodes.
| server4 | True | [] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 105663311872 available bytes; 94.10% used; 114348531 free inodes.

server4 `/home`: 105663311872 available bytes; 94.10% used; 114348531 free inodes.

server4 `/data`: 88680824832 available bytes; 98.77% used; 225253416 free inodes.

server4 `/tmp`: 105663311872 available bytes; 94.10% used; 114348531 free inodes.

server4 `/var/tmp`: 105663311872 available bytes; 94.10% used; 114348531 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
