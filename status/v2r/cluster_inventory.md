# V2R cluster inventory

2026-09-24T08:17:43.983653+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | ['7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 324406706176 available bytes; 81.90% used; 112490598 free inodes.

server1 `/home`: 324406706176 available bytes; 81.90% used; 112490598 free inodes.

server1 `/tmp`: 324406706176 available bytes; 81.90% used; 112490598 free inodes.

server1 `/var/tmp`: 324406706176 available bytes; 81.90% used; 112490598 free inodes.

server1 `/mnt/raid5`: 489668046848 available bytes; 97.75% used; 337721326 free inodes.
| server2 | True | [] | [] | reference_compatible=False |

server2 `/`: 57818181632 available bytes; 96.77% used; 110431030 free inodes.

server2 `/home`: 57818181632 available bytes; 96.77% used; 110431030 free inodes.

server2 `/tmp`: 57818181632 available bytes; 96.77% used; 110431030 free inodes.

server2 `/var/tmp`: 57818181632 available bytes; 96.77% used; 110431030 free inodes.

server2 `/mnt/raid5`: 516543062016 available bytes; 96.43% used; 445180135 free inodes.
| server3 | True | [] | [] | reference_compatible=True |

server3 `/`: 85898375168 available bytes; 95.21% used; 114200334 free inodes.

server3 `/home`: 85898375168 available bytes; 95.21% used; 114200334 free inodes.

server3 `/data`: 175166914560 available bytes; 97.58% used; 225823229 free inodes.

server3 `/tmp`: 85898375168 available bytes; 95.21% used; 114200334 free inodes.

server3 `/var/tmp`: 85898375168 available bytes; 95.21% used; 114200334 free inodes.
| server4 | True | [] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 105778397184 available bytes; 94.10% used; 114349149 free inodes.

server4 `/home`: 105778397184 available bytes; 94.10% used; 114349149 free inodes.

server4 `/data`: 281292935168 available bytes; 96.11% used; 225350873 free inodes.

server4 `/tmp`: 105778397184 available bytes; 94.10% used; 114349149 free inodes.

server4 `/var/tmp`: 105778397184 available bytes; 94.10% used; 114349149 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
