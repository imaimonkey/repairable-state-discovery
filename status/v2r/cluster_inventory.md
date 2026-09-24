# V2R cluster inventory

2026-09-24T01:15:49.521644+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | ['4'] | ['/tmp', '/var/tmp'] |

server1 `/`: 325476790272 available bytes; 81.84% used; 112499872 free inodes.

server1 `/home`: 325476790272 available bytes; 81.84% used; 112499872 free inodes.

server1 `/tmp`: 325476790272 available bytes; 81.84% used; 112499872 free inodes.

server1 `/var/tmp`: 325476790272 available bytes; 81.84% used; 112499872 free inodes.

server1 `/mnt/raid5`: 954902396928 available bytes; 95.62% used; 337734111 free inodes.
| server2 | True | [] | [] |

server2 `/`: 40954990592 available bytes; 97.72% used; 110432099 free inodes.

server2 `/home`: 40954990592 available bytes; 97.72% used; 110432099 free inodes.

server2 `/tmp`: 40954990592 available bytes; 97.72% used; 110432099 free inodes.

server2 `/var/tmp`: 40954990592 available bytes; 97.72% used; 110432099 free inodes.

server2 `/mnt/raid5`: 531386134528 available bytes; 96.33% used; 445201651 free inodes.
| server3 | True | [] | ['/tmp', '/var/tmp'] |

server3 `/`: 292359749632 available bytes; 83.69% used; 114188198 free inodes.

server3 `/home`: 292359749632 available bytes; 83.69% used; 114188198 free inodes.

server3 `/data`: 82067877888 available bytes; 98.87% used; 225842656 free inodes.

server3 `/tmp`: 292359749632 available bytes; 83.69% used; 114188198 free inodes.

server3 `/var/tmp`: 292359749632 available bytes; 83.69% used; 114188198 free inodes.
| server4 | True | ['1', '3', '6', '7'] | ['/tmp', '/var/tmp'] |

server4 `/`: 105993732096 available bytes; 94.09% used; 114349115 free inodes.

server4 `/home`: 105993732096 available bytes; 94.09% used; 114349115 free inodes.

server4 `/data`: 290838171648 available bytes; 95.98% used; 225397025 free inodes.

server4 `/tmp`: 105993732096 available bytes; 94.09% used; 114349115 free inodes.

server4 `/var/tmp`: 105993732096 available bytes; 94.09% used; 114349115 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
