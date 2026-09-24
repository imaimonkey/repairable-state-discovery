# V2R cluster inventory

2026-09-24T12:55:18.850447+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | ['4'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 324041330688 available bytes; 81.92% used; 112481553 free inodes.

server1 `/home`: 324041330688 available bytes; 81.92% used; 112481553 free inodes.

server1 `/tmp`: 324041330688 available bytes; 81.92% used; 112481553 free inodes.

server1 `/var/tmp`: 324041330688 available bytes; 81.92% used; 112481553 free inodes.

server1 `/mnt/raid5`: 417098969088 available bytes; 98.09% used; 337679278 free inodes.
| server2 | True | ['7'] | [] | reference_compatible=False |

server2 `/`: 57564254208 available bytes; 96.79% used; 110429081 free inodes.

server2 `/home`: 57564254208 available bytes; 96.79% used; 110429081 free inodes.

server2 `/tmp`: 57564254208 available bytes; 96.79% used; 110429081 free inodes.

server2 `/var/tmp`: 57564254208 available bytes; 96.79% used; 110429081 free inodes.

server2 `/mnt/raid5`: 507718103040 available bytes; 96.49% used; 445170858 free inodes.
| server3 | True | [] | [] | reference_compatible=True |

server3 `/`: 85071400960 available bytes; 95.25% used; 114163904 free inodes.

server3 `/home`: 85071400960 available bytes; 95.25% used; 114163904 free inodes.

server3 `/data`: 163053977600 available bytes; 97.75% used; 225813827 free inodes.

server3 `/tmp`: 85071400960 available bytes; 95.25% used; 114163904 free inodes.

server3 `/var/tmp`: 85071400960 available bytes; 95.25% used; 114163904 free inodes.
| server4 | True | [] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 105779605504 available bytes; 94.10% used; 114348776 free inodes.

server4 `/home`: 105779605504 available bytes; 94.10% used; 114348776 free inodes.

server4 `/data`: 90039463936 available bytes; 98.76% used; 225257189 free inodes.

server4 `/tmp`: 105779605504 available bytes; 94.10% used; 114348776 free inodes.

server4 `/var/tmp`: 105779605504 available bytes; 94.10% used; 114348776 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
