# V2R cluster inventory

2026-09-24T07:21:22.615105+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | ['5', '7'] | ['/tmp', '/var/tmp'] |

server1 `/`: 324449021952 available bytes; 81.90% used; 112491216 free inodes.

server1 `/home`: 324449021952 available bytes; 81.90% used; 112491216 free inodes.

server1 `/tmp`: 324449021952 available bytes; 81.90% used; 112491216 free inodes.

server1 `/var/tmp`: 324449021952 available bytes; 81.90% used; 112491216 free inodes.

server1 `/mnt/raid5`: 517416833024 available bytes; 97.63% used; 337722820 free inodes.
| server2 | True | [] | [] |

server2 `/`: 57852198912 available bytes; 96.77% used; 110431123 free inodes.

server2 `/home`: 57852198912 available bytes; 96.77% used; 110431123 free inodes.

server2 `/tmp`: 57852198912 available bytes; 96.77% used; 110431123 free inodes.

server2 `/var/tmp`: 57852198912 available bytes; 96.77% used; 110431123 free inodes.

server2 `/mnt/raid5`: 518552797184 available bytes; 96.42% used; 445181210 free inodes.
| server3 | True | [] | ['/tmp', '/var/tmp'] |

server3 `/`: 127188004864 available bytes; 92.90% used; 114199250 free inodes.

server3 `/home`: 127188004864 available bytes; 92.90% used; 114199250 free inodes.

server3 `/data`: 139055316992 available bytes; 98.08% used; 225834306 free inodes.

server3 `/tmp`: 127188004864 available bytes; 92.90% used; 114199250 free inodes.

server3 `/var/tmp`: 127188004864 available bytes; 92.90% used; 114199250 free inodes.
| server4 | True | [] | ['/tmp', '/var/tmp'] |

server4 `/`: 105781059584 available bytes; 94.10% used; 114349193 free inodes.

server4 `/home`: 105781059584 available bytes; 94.10% used; 114349193 free inodes.

server4 `/data`: 289003790336 available bytes; 96.01% used; 225366995 free inodes.

server4 `/tmp`: 105781059584 available bytes; 94.10% used; 114349193 free inodes.

server4 `/var/tmp`: 105781059584 available bytes; 94.10% used; 114349193 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
