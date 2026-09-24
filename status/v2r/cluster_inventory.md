# V2R cluster inventory

2026-09-24T01:14:16.737478+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | ['4'] | ['/tmp', '/var/tmp'] |

server1 `/`: 325478400000 available bytes; 81.84% used; 112499891 free inodes.

server1 `/home`: 325478400000 available bytes; 81.84% used; 112499891 free inodes.

server1 `/tmp`: 325478400000 available bytes; 81.84% used; 112499891 free inodes.

server1 `/var/tmp`: 325478400000 available bytes; 81.84% used; 112499891 free inodes.

server1 `/mnt/raid5`: 961090088960 available bytes; 95.59% used; 337734120 free inodes.
| server2 | True | [] | [] |

server2 `/`: 40957267968 available bytes; 97.72% used; 110432115 free inodes.

server2 `/home`: 40957267968 available bytes; 97.72% used; 110432115 free inodes.

server2 `/tmp`: 40957267968 available bytes; 97.72% used; 110432115 free inodes.

server2 `/var/tmp`: 40957267968 available bytes; 97.72% used; 110432115 free inodes.

server2 `/mnt/raid5`: 531431272448 available bytes; 96.33% used; 445201714 free inodes.
| server3 | True | [] | ['/tmp', '/var/tmp'] |

server3 `/`: 292360159232 available bytes; 83.69% used; 114188200 free inodes.

server3 `/home`: 292360159232 available bytes; 83.69% used; 114188200 free inodes.

server3 `/data`: 82068328448 available bytes; 98.87% used; 225842694 free inodes.

server3 `/tmp`: 292360159232 available bytes; 83.69% used; 114188200 free inodes.

server3 `/var/tmp`: 292360159232 available bytes; 83.69% used; 114188200 free inodes.
| server4 | True | ['1', '3', '6', '7'] | ['/tmp', '/var/tmp'] |

server4 `/`: 105996341248 available bytes; 94.09% used; 114349155 free inodes.

server4 `/home`: 105996341248 available bytes; 94.09% used; 114349155 free inodes.

server4 `/data`: 291864694784 available bytes; 95.97% used; 225405339 free inodes.

server4 `/tmp`: 105996341248 available bytes; 94.09% used; 114349155 free inodes.

server4 `/var/tmp`: 105996341248 available bytes; 94.09% used; 114349155 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
