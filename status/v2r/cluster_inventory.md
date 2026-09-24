# V2R cluster inventory

2026-09-24T06:06:42.381575+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | ['7'] | ['/tmp', '/var/tmp'] |

server1 `/`: 324527022080 available bytes; 81.90% used; 112491887 free inodes.

server1 `/home`: 324527022080 available bytes; 81.90% used; 112491887 free inodes.

server1 `/tmp`: 324527022080 available bytes; 81.90% used; 112491887 free inodes.

server1 `/var/tmp`: 324527022080 available bytes; 81.90% used; 112491887 free inodes.

server1 `/mnt/raid5`: 517606850560 available bytes; 97.63% used; 337723820 free inodes.
| server2 | True | [] | [] |

server2 `/`: 57896259584 available bytes; 96.77% used; 110431278 free inodes.

server2 `/home`: 57896259584 available bytes; 96.77% used; 110431278 free inodes.

server2 `/tmp`: 57896259584 available bytes; 96.77% used; 110431278 free inodes.

server2 `/var/tmp`: 57896259584 available bytes; 96.77% used; 110431278 free inodes.

server2 `/mnt/raid5`: 520966602752 available bytes; 96.40% used; 445192895 free inodes.
| server3 | True | [] | ['/tmp', '/var/tmp'] |

server3 `/`: 127197818880 available bytes; 92.90% used; 114197356 free inodes.

server3 `/home`: 127197818880 available bytes; 92.90% used; 114197356 free inodes.

server3 `/data`: 185833336832 available bytes; 97.43% used; 225838356 free inodes.

server3 `/tmp`: 127197818880 available bytes; 92.90% used; 114197356 free inodes.

server3 `/var/tmp`: 127197818880 available bytes; 92.90% used; 114197356 free inodes.
| server4 | True | ['1'] | ['/tmp', '/var/tmp'] |

server4 `/`: 105815109632 available bytes; 94.10% used; 114349319 free inodes.

server4 `/home`: 105815109632 available bytes; 94.10% used; 114349319 free inodes.

server4 `/data`: 339785555968 available bytes; 95.30% used; 225374266 free inodes.

server4 `/tmp`: 105815109632 available bytes; 94.10% used; 114349319 free inodes.

server4 `/var/tmp`: 105815109632 available bytes; 94.10% used; 114349319 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
