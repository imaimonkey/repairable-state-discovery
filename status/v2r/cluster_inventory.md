# V2R cluster inventory

2026-09-25T02:36:03.887396+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | [] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 318959624192 available bytes; 82.21% used; 112480422 free inodes.

server1 `/home`: 318959624192 available bytes; 82.21% used; 112480422 free inodes.

server1 `/tmp`: 318959624192 available bytes; 82.21% used; 112480422 free inodes.

server1 `/var/tmp`: 318959624192 available bytes; 82.21% used; 112480422 free inodes.

server1 `/mnt/raid5`: 416200364032 available bytes; 98.09% used; 337605246 free inodes.
| server2 | True | [] | [] | reference_compatible=False |

server2 `/`: 23008694272 available bytes; 98.72% used; 110410436 free inodes.

server2 `/home`: 23008694272 available bytes; 98.72% used; 110410436 free inodes.

server2 `/tmp`: 23008694272 available bytes; 98.72% used; 110410436 free inodes.

server2 `/var/tmp`: 23008694272 available bytes; 98.72% used; 110410436 free inodes.

server2 `/mnt/raid5`: 482919596032 available bytes; 96.66% used; 445113356 free inodes.
| server3 | True | [] | [] | reference_compatible=True |

server3 `/`: 84351385600 available bytes; 95.29% used; 114156075 free inodes.

server3 `/home`: 84351385600 available bytes; 95.29% used; 114156075 free inodes.

server3 `/data`: 145509322752 available bytes; 97.99% used; 225811139 free inodes.

server3 `/tmp`: 84351385600 available bytes; 95.29% used; 114156075 free inodes.

server3 `/var/tmp`: 84351385600 available bytes; 95.29% used; 114156075 free inodes.
| server4 | True | ['0', '3', '5', '7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 105895624704 available bytes; 94.09% used; 114350966 free inodes.

server4 `/home`: 105895624704 available bytes; 94.09% used; 114350966 free inodes.

server4 `/data`: 4640239616 available bytes; 99.94% used; 224968919 free inodes.

server4 `/tmp`: 105895624704 available bytes; 94.09% used; 114350966 free inodes.

server4 `/var/tmp`: 105895624704 available bytes; 94.09% used; 114350966 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
