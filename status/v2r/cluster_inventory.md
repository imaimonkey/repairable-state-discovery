# V2R cluster inventory

2026-09-24T01:32:51.770466+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | ['4', '6', '7'] | ['/tmp', '/var/tmp'] |

server1 `/`: 325461188608 available bytes; 81.84% used; 112499599 free inodes.

server1 `/home`: 325461188608 available bytes; 81.84% used; 112499599 free inodes.

server1 `/tmp`: 325461188608 available bytes; 81.84% used; 112499599 free inodes.

server1 `/var/tmp`: 325461188608 available bytes; 81.84% used; 112499599 free inodes.

server1 `/mnt/raid5`: 886417977344 available bytes; 95.93% used; 337733984 free inodes.
| server2 | True | [] | [] |

server2 `/`: 40941056000 available bytes; 97.72% used; 110431972 free inodes.

server2 `/home`: 40941056000 available bytes; 97.72% used; 110431972 free inodes.

server2 `/tmp`: 40941056000 available bytes; 97.72% used; 110431972 free inodes.

server2 `/var/tmp`: 40941056000 available bytes; 97.72% used; 110431972 free inodes.

server2 `/mnt/raid5`: 530176221184 available bytes; 96.34% used; 445201328 free inodes.
| server3 | True | [] | ['/tmp', '/var/tmp'] |

server3 `/`: 292710662144 available bytes; 83.67% used; 114211187 free inodes.

server3 `/home`: 292710662144 available bytes; 83.67% used; 114211187 free inodes.

server3 `/data`: 82037272576 available bytes; 98.87% used; 225842212 free inodes.

server3 `/tmp`: 292710662144 available bytes; 83.67% used; 114211187 free inodes.

server3 `/var/tmp`: 292710662144 available bytes; 83.67% used; 114211187 free inodes.
| server4 | True | ['2', '3', '6', '7'] | ['/tmp', '/var/tmp'] |

server4 `/`: 105964163072 available bytes; 94.09% used; 114348780 free inodes.

server4 `/home`: 105964163072 available bytes; 94.09% used; 114348780 free inodes.

server4 `/data`: 290806341632 available bytes; 95.98% used; 225396965 free inodes.

server4 `/tmp`: 105964163072 available bytes; 94.09% used; 114348780 free inodes.

server4 `/var/tmp`: 105964163072 available bytes; 94.09% used; 114348780 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
