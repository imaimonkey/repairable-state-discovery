# V2R cluster inventory

2026-09-24T03:32:04.565736+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | ['7'] | ['/tmp', '/var/tmp'] |

server1 `/`: 325150498816 available bytes; 81.86% used; 112497300 free inodes.

server1 `/home`: 325150498816 available bytes; 81.86% used; 112497300 free inodes.

server1 `/tmp`: 325150498816 available bytes; 81.86% used; 112497300 free inodes.

server1 `/var/tmp`: 325150498816 available bytes; 81.86% used; 112497300 free inodes.

server1 `/mnt/raid5`: 397557075968 available bytes; 98.18% used; 337734030 free inodes.
| server2 | True | [] | [] |

server2 `/`: 40833245184 available bytes; 97.72% used; 110431088 free inodes.

server2 `/home`: 40833245184 available bytes; 97.72% used; 110431088 free inodes.

server2 `/tmp`: 40833245184 available bytes; 97.72% used; 110431088 free inodes.

server2 `/var/tmp`: 40833245184 available bytes; 97.72% used; 110431088 free inodes.

server2 `/mnt/raid5`: 527150366720 available bytes; 96.36% used; 445197791 free inodes.
| server3 | True | ['1'] | ['/tmp', '/var/tmp'] |

server3 `/`: 292364673024 available bytes; 83.68% used; 114200778 free inodes.

server3 `/home`: 292364673024 available bytes; 83.68% used; 114200778 free inodes.

server3 `/data`: 36012015616 available bytes; 99.50% used; 225842994 free inodes.

server3 `/tmp`: 292364673024 available bytes; 83.68% used; 114200778 free inodes.

server3 `/var/tmp`: 292364673024 available bytes; 83.68% used; 114200778 free inodes.
| server4 | True | ['3', '7'] | ['/tmp', '/var/tmp'] |

server4 `/`: 105986990080 available bytes; 94.09% used; 114349606 free inodes.

server4 `/home`: 105986990080 available bytes; 94.09% used; 114349606 free inodes.

server4 `/data`: 282052677632 available bytes; 96.10% used; 225385493 free inodes.

server4 `/tmp`: 105986990080 available bytes; 94.09% used; 114349606 free inodes.

server4 `/var/tmp`: 105986990080 available bytes; 94.09% used; 114349606 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
