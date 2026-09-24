# V2R cluster inventory

2026-09-24T23:02:15.694319+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | [] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 321175871488 available bytes; 82.08% used; 112480872 free inodes.

server1 `/home`: 321175871488 available bytes; 82.08% used; 112480872 free inodes.

server1 `/tmp`: 321175871488 available bytes; 82.08% used; 112480872 free inodes.

server1 `/var/tmp`: 321175871488 available bytes; 82.08% used; 112480872 free inodes.

server1 `/mnt/raid5`: 415288901632 available bytes; 98.09% used; 337616482 free inodes.
| server2 | True | [] | [] | reference_compatible=False |

server2 `/`: 23131684864 available bytes; 98.71% used; 110410816 free inodes.

server2 `/home`: 23131684864 available bytes; 98.71% used; 110410816 free inodes.

server2 `/tmp`: 23131684864 available bytes; 98.71% used; 110410816 free inodes.

server2 `/var/tmp`: 23131684864 available bytes; 98.71% used; 110410816 free inodes.

server2 `/mnt/raid5`: 487542685696 available bytes; 96.63% used; 445152201 free inodes.
| server3 | True | [] | [] | reference_compatible=True |

server3 `/`: 84369739776 available bytes; 95.29% used; 114156075 free inodes.

server3 `/home`: 84369739776 available bytes; 95.29% used; 114156075 free inodes.

server3 `/data`: 148748918784 available bytes; 97.94% used; 225801464 free inodes.

server3 `/tmp`: 84369739776 available bytes; 95.29% used; 114156075 free inodes.

server3 `/var/tmp`: 84369739776 available bytes; 95.29% used; 114156075 free inodes.
| server4 | True | ['0', '7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 105800765440 available bytes; 94.10% used; 114348315 free inodes.

server4 `/home`: 105800765440 available bytes; 94.10% used; 114348315 free inodes.

server4 `/data`: 61985841152 available bytes; 99.14% used; 225188567 free inodes.

server4 `/tmp`: 105800765440 available bytes; 94.10% used; 114348315 free inodes.

server4 `/var/tmp`: 105800765440 available bytes; 94.10% used; 114348315 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
