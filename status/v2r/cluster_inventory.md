# V2R cluster inventory

2026-09-24T06:08:42.397841+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | ['7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 324525191168 available bytes; 81.90% used; 112491864 free inodes.

server1 `/home`: 324525191168 available bytes; 81.90% used; 112491864 free inodes.

server1 `/tmp`: 324525191168 available bytes; 81.90% used; 112491864 free inodes.

server1 `/var/tmp`: 324525191168 available bytes; 81.90% used; 112491864 free inodes.

server1 `/mnt/raid5`: 517601800192 available bytes; 97.63% used; 337723793 free inodes.
| server2 | True | [] | [] | reference_compatible=False |

server2 `/`: 57895608320 available bytes; 96.77% used; 110431274 free inodes.

server2 `/home`: 57895608320 available bytes; 96.77% used; 110431274 free inodes.

server2 `/tmp`: 57895608320 available bytes; 96.77% used; 110431274 free inodes.

server2 `/var/tmp`: 57895608320 available bytes; 96.77% used; 110431274 free inodes.

server2 `/mnt/raid5`: 520893853696 available bytes; 96.40% used; 445192713 free inodes.
| server3 | True | [] | ['/tmp', '/var/tmp'] | reference_compatible=True |

server3 `/`: 127217135616 available bytes; 92.90% used; 114200479 free inodes.

server3 `/home`: 127217135616 available bytes; 92.90% used; 114200479 free inodes.

server3 `/data`: 165186318336 available bytes; 97.72% used; 225838291 free inodes.

server3 `/tmp`: 127217135616 available bytes; 92.90% used; 114200479 free inodes.

server3 `/var/tmp`: 127217135616 available bytes; 92.90% used; 114200479 free inodes.
| server4 | True | ['1'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 105815031808 available bytes; 94.10% used; 114349319 free inodes.

server4 `/home`: 105815031808 available bytes; 94.10% used; 114349319 free inodes.

server4 `/data`: 339783708672 available bytes; 95.30% used; 225374169 free inodes.

server4 `/tmp`: 105815031808 available bytes; 94.10% used; 114349319 free inodes.

server4 `/var/tmp`: 105815031808 available bytes; 94.10% used; 114349319 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
