# V2R cluster inventory

2026-09-24T22:26:49.233988+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | [] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 323945553920 available bytes; 81.93% used; 112481420 free inodes.

server1 `/home`: 323945553920 available bytes; 81.93% used; 112481420 free inodes.

server1 `/tmp`: 323945553920 available bytes; 81.93% used; 112481420 free inodes.

server1 `/var/tmp`: 323945553920 available bytes; 81.93% used; 112481420 free inodes.

server1 `/mnt/raid5`: 415379795968 available bytes; 98.09% used; 337620713 free inodes.
| server2 | True | [] | [] | reference_compatible=False |

server2 `/`: 23575371776 available bytes; 98.68% used; 110410980 free inodes.

server2 `/home`: 23575371776 available bytes; 98.68% used; 110410980 free inodes.

server2 `/tmp`: 23575371776 available bytes; 98.68% used; 110410980 free inodes.

server2 `/var/tmp`: 23575371776 available bytes; 98.68% used; 110410980 free inodes.

server2 `/mnt/raid5`: 488650121216 available bytes; 96.62% used; 445153150 free inodes.
| server3 | True | [] | [] | reference_compatible=True |

server3 `/`: 84378148864 available bytes; 95.29% used; 114156085 free inodes.

server3 `/home`: 84378148864 available bytes; 95.29% used; 114156085 free inodes.

server3 `/data`: 149346885632 available bytes; 97.94% used; 225802140 free inodes.

server3 `/tmp`: 84378148864 available bytes; 95.29% used; 114156085 free inodes.

server3 `/var/tmp`: 84378148864 available bytes; 95.29% used; 114156085 free inodes.
| server4 | True | ['5'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 105810444288 available bytes; 94.10% used; 114348322 free inodes.

server4 `/home`: 105810444288 available bytes; 94.10% used; 114348322 free inodes.

server4 `/data`: 73304059904 available bytes; 98.99% used; 225227606 free inodes.

server4 `/tmp`: 105810444288 available bytes; 94.10% used; 114348322 free inodes.

server4 `/var/tmp`: 105810444288 available bytes; 94.10% used; 114348322 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
