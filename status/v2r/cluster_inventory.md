# V2R cluster inventory

2026-09-24T17:16:47.275394+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | ['7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 324007493632 available bytes; 81.92% used; 112481439 free inodes.

server1 `/home`: 324007493632 available bytes; 81.92% used; 112481439 free inodes.

server1 `/tmp`: 324007493632 available bytes; 81.92% used; 112481439 free inodes.

server1 `/var/tmp`: 324007493632 available bytes; 81.92% used; 112481439 free inodes.

server1 `/mnt/raid5`: 416473509888 available bytes; 98.09% used; 337647928 free inodes.
| server2 | True | ['7'] | [] | reference_compatible=False |

server2 `/`: 57048510464 available bytes; 96.82% used; 110417836 free inodes.

server2 `/home`: 57048510464 available bytes; 96.82% used; 110417836 free inodes.

server2 `/tmp`: 57048510464 available bytes; 96.82% used; 110417836 free inodes.

server2 `/var/tmp`: 57048510464 available bytes; 96.82% used; 110417836 free inodes.

server2 `/mnt/raid5`: 499491041280 available bytes; 96.55% used; 445162711 free inodes.
| server3 | True | [] | [] | reference_compatible=True |

server3 `/`: 84409024512 available bytes; 95.29% used; 114156150 free inodes.

server3 `/home`: 84409024512 available bytes; 95.29% used; 114156150 free inodes.

server3 `/data`: 159034077184 available bytes; 97.80% used; 225787075 free inodes.

server3 `/tmp`: 84409024512 available bytes; 95.29% used; 114156150 free inodes.

server3 `/var/tmp`: 84409024512 available bytes; 95.29% used; 114156150 free inodes.
| server4 | True | [] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 105681952768 available bytes; 94.10% used; 114348569 free inodes.

server4 `/home`: 105681952768 available bytes; 94.10% used; 114348569 free inodes.

server4 `/data`: 89149997056 available bytes; 98.77% used; 225254577 free inodes.

server4 `/tmp`: 105681952768 available bytes; 94.10% used; 114348569 free inodes.

server4 `/var/tmp`: 105681952768 available bytes; 94.10% used; 114348569 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
