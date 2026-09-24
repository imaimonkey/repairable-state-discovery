# V2R cluster inventory

2026-09-24T20:17:12.439582+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | [] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 323988250624 available bytes; 81.93% used; 112481427 free inodes.

server1 `/home`: 323988250624 available bytes; 81.93% used; 112481427 free inodes.

server1 `/tmp`: 323988250624 available bytes; 81.93% used; 112481427 free inodes.

server1 `/var/tmp`: 323988250624 available bytes; 81.93% used; 112481427 free inodes.

server1 `/mnt/raid5`: 415671123968 available bytes; 98.09% used; 337635950 free inodes.
| server2 | True | ['7'] | [] | reference_compatible=False |

server2 `/`: 30172745728 available bytes; 98.32% used; 110411378 free inodes.

server2 `/home`: 30172745728 available bytes; 98.32% used; 110411378 free inodes.

server2 `/tmp`: 30172745728 available bytes; 98.32% used; 110411378 free inodes.

server2 `/var/tmp`: 30172745728 available bytes; 98.32% used; 110411378 free inodes.

server2 `/mnt/raid5`: 492944093184 available bytes; 96.59% used; 445157202 free inodes.
| server3 | True | [] | [] | reference_compatible=True |

server3 `/`: 84398682112 available bytes; 95.29% used; 114156109 free inodes.

server3 `/home`: 84398682112 available bytes; 95.29% used; 114156109 free inodes.

server3 `/data`: 151703080960 available bytes; 97.90% used; 225804729 free inodes.

server3 `/tmp`: 84398682112 available bytes; 95.29% used; 114156109 free inodes.

server3 `/var/tmp`: 84398682112 available bytes; 95.29% used; 114156109 free inodes.
| server4 | True | [] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 105640976384 available bytes; 94.10% used; 114348398 free inodes.

server4 `/home`: 105640976384 available bytes; 94.10% used; 114348398 free inodes.

server4 `/data`: 87965306880 available bytes; 98.78% used; 225258781 free inodes.

server4 `/tmp`: 105640976384 available bytes; 94.10% used; 114348398 free inodes.

server4 `/var/tmp`: 105640976384 available bytes; 94.10% used; 114348398 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
