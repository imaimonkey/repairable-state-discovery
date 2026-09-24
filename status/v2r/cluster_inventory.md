# V2R cluster inventory

2026-09-24T08:23:41.178023+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | ['6'] | ['/tmp', '/var/tmp'] |

server1 `/`: 324401434624 available bytes; 81.90% used; 112490511 free inodes.

server1 `/home`: 324401434624 available bytes; 81.90% used; 112490511 free inodes.

server1 `/tmp`: 324401434624 available bytes; 81.90% used; 112490511 free inodes.

server1 `/var/tmp`: 324401434624 available bytes; 81.90% used; 112490511 free inodes.

server1 `/mnt/raid5`: 510226227200 available bytes; 97.66% used; 337721269 free inodes.
| server2 | True | [] | [] |

server2 `/`: 57810718720 available bytes; 96.77% used; 110431016 free inodes.

server2 `/home`: 57810718720 available bytes; 96.77% used; 110431016 free inodes.

server2 `/tmp`: 57810718720 available bytes; 96.77% used; 110431016 free inodes.

server2 `/var/tmp`: 57810718720 available bytes; 96.77% used; 110431016 free inodes.

server2 `/mnt/raid5`: 516348452864 available bytes; 96.43% used; 445179812 free inodes.
| server3 | True | [] | [] |

server3 `/`: 85480644608 available bytes; 95.23% used; 114174940 free inodes.

server3 `/home`: 85480644608 available bytes; 95.23% used; 114174940 free inodes.

server3 `/data`: 175124070400 available bytes; 97.58% used; 225823103 free inodes.

server3 `/tmp`: 85480644608 available bytes; 95.23% used; 114174940 free inodes.

server3 `/var/tmp`: 85480644608 available bytes; 95.23% used; 114174940 free inodes.
| server4 | True | [] | ['/tmp', '/var/tmp'] |

server4 `/`: 105769521152 available bytes; 94.10% used; 114349122 free inodes.

server4 `/home`: 105769521152 available bytes; 94.10% used; 114349122 free inodes.

server4 `/data`: 280472276992 available bytes; 96.12% used; 225350818 free inodes.

server4 `/tmp`: 105769521152 available bytes; 94.10% used; 114349122 free inodes.

server4 `/var/tmp`: 105769521152 available bytes; 94.10% used; 114349122 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
