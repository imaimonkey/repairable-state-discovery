# V2R cluster inventory

2026-09-24T20:09:28.802551+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | [] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 323989745664 available bytes; 81.93% used; 112481427 free inodes.

server1 `/home`: 323989745664 available bytes; 81.93% used; 112481427 free inodes.

server1 `/tmp`: 323989745664 available bytes; 81.93% used; 112481427 free inodes.

server1 `/var/tmp`: 323989745664 available bytes; 81.93% used; 112481427 free inodes.

server1 `/mnt/raid5`: 415537397760 available bytes; 98.09% used; 337627773 free inodes.
| server2 | True | ['7'] | [] | reference_compatible=False |

server2 `/`: 30175592448 available bytes; 98.32% used; 110411376 free inodes.

server2 `/home`: 30175592448 available bytes; 98.32% used; 110411376 free inodes.

server2 `/tmp`: 30175592448 available bytes; 98.32% used; 110411376 free inodes.

server2 `/var/tmp`: 30175592448 available bytes; 98.32% used; 110411376 free inodes.

server2 `/mnt/raid5`: 493524082688 available bytes; 96.59% used; 445157460 free inodes.
| server3 | True | [] | [] | reference_compatible=True |

server3 `/`: 84399947776 available bytes; 95.29% used; 114156128 free inodes.

server3 `/home`: 84399947776 available bytes; 95.29% used; 114156128 free inodes.

server3 `/data`: 151769681920 available bytes; 97.90% used; 225798773 free inodes.

server3 `/tmp`: 84399947776 available bytes; 95.29% used; 114156128 free inodes.

server3 `/var/tmp`: 84399947776 available bytes; 95.29% used; 114156128 free inodes.
| server4 | True | [] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 105641308160 available bytes; 94.10% used; 114348411 free inodes.

server4 `/home`: 105641308160 available bytes; 94.10% used; 114348411 free inodes.

server4 `/data`: 89791606784 available bytes; 98.76% used; 225266160 free inodes.

server4 `/tmp`: 105641308160 available bytes; 94.10% used; 114348411 free inodes.

server4 `/var/tmp`: 105641308160 available bytes; 94.10% used; 114348411 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
