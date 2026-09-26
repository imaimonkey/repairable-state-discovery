# V2R cluster inventory

2026-09-26T05:04:28.720808+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | ['1', '4', '5', '6', '7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 318397755392 available bytes; 82.24% used; 112476272 free inodes.

server1 `/home`: 318397755392 available bytes; 82.24% used; 112476272 free inodes.

server1 `/tmp`: 318397755392 available bytes; 82.24% used; 112476272 free inodes.

server1 `/var/tmp`: 318397755392 available bytes; 82.24% used; 112476272 free inodes.

server1 `/mnt/raid5`: 329904590848 available bytes; 98.49% used; 337544667 free inodes.
| server2 | True | [] | [] | reference_compatible=False |

server2 `/`: 22928748544 available bytes; 98.72% used; 110406196 free inodes.

server2 `/home`: 22928748544 available bytes; 98.72% used; 110406196 free inodes.

server2 `/tmp`: 22928748544 available bytes; 98.72% used; 110406196 free inodes.

server2 `/var/tmp`: 22928748544 available bytes; 98.72% used; 110406196 free inodes.

server2 `/mnt/raid5`: 284477931520 available bytes; 98.03% used; 445049557 free inodes.
| server3 | True | [] | [] | reference_compatible=True |

server3 `/`: 83690729472 available bytes; 95.33% used; 114139129 free inodes.

server3 `/home`: 83690729472 available bytes; 95.33% used; 114139129 free inodes.

server3 `/data`: 124614287360 available bytes; 98.28% used; 225825471 free inodes.

server3 `/tmp`: 83690729472 available bytes; 95.33% used; 114139129 free inodes.

server3 `/var/tmp`: 83690729472 available bytes; 95.33% used; 114139129 free inodes.
| server4 | True | ['2', '3', '6', '7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 105993039872 available bytes; 94.09% used; 114348206 free inodes.

server4 `/home`: 105993039872 available bytes; 94.09% used; 114348206 free inodes.

server4 `/data`: 107000123392 available bytes; 98.52% used; 224929215 free inodes.

server4 `/tmp`: 105993039872 available bytes; 94.09% used; 114348206 free inodes.

server4 `/var/tmp`: 105993039872 available bytes; 94.09% used; 114348206 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
