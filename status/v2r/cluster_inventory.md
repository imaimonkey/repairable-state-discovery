# V2R cluster inventory

2026-09-24T01:32:19.199918+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | ['4', '7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 325461745664 available bytes; 81.84% used; 112499618 free inodes.

server1 `/home`: 325461745664 available bytes; 81.84% used; 112499618 free inodes.

server1 `/tmp`: 325461745664 available bytes; 81.84% used; 112499618 free inodes.

server1 `/var/tmp`: 325461745664 available bytes; 81.84% used; 112499618 free inodes.

server1 `/mnt/raid5`: 888632029184 available bytes; 95.92% used; 337733966 free inodes.
| server2 | True | [] | [] | reference_compatible=False |

server2 `/`: 40941064192 available bytes; 97.72% used; 110431972 free inodes.

server2 `/home`: 40941064192 available bytes; 97.72% used; 110431972 free inodes.

server2 `/tmp`: 40941064192 available bytes; 97.72% used; 110431972 free inodes.

server2 `/var/tmp`: 40941064192 available bytes; 97.72% used; 110431972 free inodes.

server2 `/mnt/raid5`: 530728992768 available bytes; 96.33% used; 445201354 free inodes.
| server3 | True | [] | ['/tmp', '/var/tmp'] | reference_compatible=True |

server3 `/`: 292710793216 available bytes; 83.67% used; 114211199 free inodes.

server3 `/home`: 292710793216 available bytes; 83.67% used; 114211199 free inodes.

server3 `/data`: 82038165504 available bytes; 98.87% used; 225842231 free inodes.

server3 `/tmp`: 292710793216 available bytes; 83.67% used; 114211199 free inodes.

server3 `/var/tmp`: 292710793216 available bytes; 83.67% used; 114211199 free inodes.
| server4 | True | ['2', '3', '6', '7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 105964675072 available bytes; 94.09% used; 114348788 free inodes.

server4 `/home`: 105964675072 available bytes; 94.09% used; 114348788 free inodes.

server4 `/data`: 290806472704 available bytes; 95.98% used; 225396965 free inodes.

server4 `/tmp`: 105964675072 available bytes; 94.09% used; 114348788 free inodes.

server4 `/var/tmp`: 105964675072 available bytes; 94.09% used; 114348788 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
