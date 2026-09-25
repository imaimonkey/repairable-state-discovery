# V2R cluster inventory

2026-09-25T02:08:25.394251+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | [] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 319023124480 available bytes; 82.20% used; 112480582 free inodes.

server1 `/home`: 319023124480 available bytes; 82.20% used; 112480582 free inodes.

server1 `/tmp`: 319023124480 available bytes; 82.20% used; 112480582 free inodes.

server1 `/var/tmp`: 319023124480 available bytes; 82.20% used; 112480582 free inodes.

server1 `/mnt/raid5`: 416257327104 available bytes; 98.09% used; 337608468 free inodes.
| server2 | True | [] | [] | reference_compatible=False |

server2 `/`: 23024607232 available bytes; 98.72% used; 110410440 free inodes.

server2 `/home`: 23024607232 available bytes; 98.72% used; 110410440 free inodes.

server2 `/tmp`: 23024607232 available bytes; 98.72% used; 110410440 free inodes.

server2 `/var/tmp`: 23024607232 available bytes; 98.72% used; 110410440 free inodes.

server2 `/mnt/raid5`: 484065964032 available bytes; 96.66% used; 445114445 free inodes.
| server3 | True | [] | [] | reference_compatible=True |

server3 `/`: 84351844352 available bytes; 95.29% used; 114156074 free inodes.

server3 `/home`: 84351844352 available bytes; 95.29% used; 114156074 free inodes.

server3 `/data`: 145970642944 available bytes; 97.98% used; 225811573 free inodes.

server3 `/tmp`: 84351844352 available bytes; 95.29% used; 114156074 free inodes.

server3 `/var/tmp`: 84351844352 available bytes; 95.29% used; 114156074 free inodes.
| server4 | True | ['0', '1', '4', '5', '7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 105752494080 available bytes; 94.10% used; 114348241 free inodes.

server4 `/home`: 105752494080 available bytes; 94.10% used; 114348241 free inodes.

server4 `/data`: 46699937792 available bytes; 99.35% used; 225023393 free inodes.

server4 `/tmp`: 105752494080 available bytes; 94.10% used; 114348241 free inodes.

server4 `/var/tmp`: 105752494080 available bytes; 94.10% used; 114348241 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
