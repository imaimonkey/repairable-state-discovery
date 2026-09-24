# V2R cluster inventory

2026-09-24T01:35:24.113579+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | ['4', '6', '7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 325460828160 available bytes; 81.84% used; 112499523 free inodes.

server1 `/home`: 325460828160 available bytes; 81.84% used; 112499523 free inodes.

server1 `/tmp`: 325460828160 available bytes; 81.84% used; 112499523 free inodes.

server1 `/var/tmp`: 325460828160 available bytes; 81.84% used; 112499523 free inodes.

server1 `/mnt/raid5`: 875278622720 available bytes; 95.98% used; 337733933 free inodes.
| server2 | True | [] | [] | reference_compatible=False |

server2 `/`: 40938975232 available bytes; 97.72% used; 110431947 free inodes.

server2 `/home`: 40938975232 available bytes; 97.72% used; 110431947 free inodes.

server2 `/tmp`: 40938975232 available bytes; 97.72% used; 110431947 free inodes.

server2 `/var/tmp`: 40938975232 available bytes; 97.72% used; 110431947 free inodes.

server2 `/mnt/raid5`: 530633625600 available bytes; 96.33% used; 445201432 free inodes.
| server3 | True | [] | ['/tmp', '/var/tmp'] | reference_compatible=True |

server3 `/`: 292716011520 available bytes; 83.67% used; 114211223 free inodes.

server3 `/home`: 292716011520 available bytes; 83.67% used; 114211223 free inodes.

server3 `/data`: 61155442688 available bytes; 99.15% used; 225842149 free inodes.

server3 `/tmp`: 292716011520 available bytes; 83.67% used; 114211223 free inodes.

server3 `/var/tmp`: 292716011520 available bytes; 83.67% used; 114211223 free inodes.
| server4 | True | ['2', '3', '6', '7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 105961009152 available bytes; 94.09% used; 114348732 free inodes.

server4 `/home`: 105961009152 available bytes; 94.09% used; 114348732 free inodes.

server4 `/data`: 290804764672 available bytes; 95.98% used; 225396965 free inodes.

server4 `/tmp`: 105961009152 available bytes; 94.09% used; 114348732 free inodes.

server4 `/var/tmp`: 105961009152 available bytes; 94.09% used; 114348732 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
