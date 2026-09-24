# V2R cluster inventory

2026-09-24T01:31:19.093839+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | ['4'] | ['/tmp', '/var/tmp'] |

server1 `/`: 325462847488 available bytes; 81.84% used; 112499644 free inodes.

server1 `/home`: 325462847488 available bytes; 81.84% used; 112499644 free inodes.

server1 `/tmp`: 325462847488 available bytes; 81.84% used; 112499644 free inodes.

server1 `/var/tmp`: 325462847488 available bytes; 81.84% used; 112499644 free inodes.

server1 `/mnt/raid5`: 892492296192 available bytes; 95.91% used; 337733980 free inodes.
| server2 | True | [] | [] |

server2 `/`: 40943001600 available bytes; 97.72% used; 110431987 free inodes.

server2 `/home`: 40943001600 available bytes; 97.72% used; 110431987 free inodes.

server2 `/tmp`: 40943001600 available bytes; 97.72% used; 110431987 free inodes.

server2 `/var/tmp`: 40943001600 available bytes; 97.72% used; 110431987 free inodes.

server2 `/mnt/raid5`: 530364047360 available bytes; 96.34% used; 445201436 free inodes.
| server3 | True | [] | ['/tmp', '/var/tmp'] |

server3 `/`: 292711010304 available bytes; 83.67% used; 114211199 free inodes.

server3 `/home`: 292711010304 available bytes; 83.67% used; 114211199 free inodes.

server3 `/data`: 82039115776 available bytes; 98.87% used; 225842252 free inodes.

server3 `/tmp`: 292711010304 available bytes; 83.67% used; 114211199 free inodes.

server3 `/var/tmp`: 292711010304 available bytes; 83.67% used; 114211199 free inodes.
| server4 | True | ['2', '3', '6', '7'] | ['/tmp', '/var/tmp'] |

server4 `/`: 105965699072 available bytes; 94.09% used; 114348804 free inodes.

server4 `/home`: 105965699072 available bytes; 94.09% used; 114348804 free inodes.

server4 `/data`: 290808623104 available bytes; 95.98% used; 225396965 free inodes.

server4 `/tmp`: 105965699072 available bytes; 94.09% used; 114348804 free inodes.

server4 `/var/tmp`: 105965699072 available bytes; 94.09% used; 114348804 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
