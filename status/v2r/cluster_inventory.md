# V2R cluster inventory

2026-09-24T03:11:24.765546+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | ['7'] | ['/tmp', '/var/tmp'] |

server1 `/`: 325369466880 available bytes; 81.85% used; 112498418 free inodes.

server1 `/home`: 325369466880 available bytes; 81.85% used; 112498418 free inodes.

server1 `/tmp`: 325369466880 available bytes; 81.85% used; 112498418 free inodes.

server1 `/var/tmp`: 325369466880 available bytes; 81.85% used; 112498418 free inodes.

server1 `/mnt/raid5`: 471212666880 available bytes; 97.84% used; 337732228 free inodes.
| server2 | True | [] | [] |

server2 `/`: 40857194496 available bytes; 97.72% used; 110431242 free inodes.

server2 `/home`: 40857194496 available bytes; 97.72% used; 110431242 free inodes.

server2 `/tmp`: 40857194496 available bytes; 97.72% used; 110431242 free inodes.

server2 `/var/tmp`: 40857194496 available bytes; 97.72% used; 110431242 free inodes.

server2 `/mnt/raid5`: 527728889856 available bytes; 96.35% used; 445198241 free inodes.
| server3 | True | [] | ['/tmp', '/var/tmp'] |

server3 `/`: 292294062080 available bytes; 83.69% used; 114187091 free inodes.

server3 `/home`: 292294062080 available bytes; 83.69% used; 114187091 free inodes.

server3 `/data`: 39681609728 available bytes; 99.45% used; 225844769 free inodes.

server3 `/tmp`: 292294062080 available bytes; 83.69% used; 114187091 free inodes.

server3 `/var/tmp`: 292294062080 available bytes; 83.69% used; 114187091 free inodes.
| server4 | True | ['3', '7'] | ['/tmp', '/var/tmp'] |

server4 `/`: 105987969024 available bytes; 94.09% used; 114349625 free inodes.

server4 `/home`: 105987969024 available bytes; 94.09% used; 114349625 free inodes.

server4 `/data`: 289700347904 available bytes; 96.00% used; 225386846 free inodes.

server4 `/tmp`: 105987969024 available bytes; 94.09% used; 114349625 free inodes.

server4 `/var/tmp`: 105987969024 available bytes; 94.09% used; 114349625 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
