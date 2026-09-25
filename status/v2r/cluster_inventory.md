# V2R cluster inventory

2026-09-25T11:01:23.057236+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | [] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 319063728128 available bytes; 82.20% used; 112478858 free inodes.

server1 `/home`: 319063728128 available bytes; 82.20% used; 112478858 free inodes.

server1 `/tmp`: 319063728128 available bytes; 82.20% used; 112478858 free inodes.

server1 `/var/tmp`: 319063728128 available bytes; 82.20% used; 112478858 free inodes.

server1 `/mnt/raid5`: 364841152512 available bytes; 98.33% used; 337555174 free inodes.
| server2 | True | ['1', '2', '3', '4', '5', '6'] | [] | reference_compatible=False |

server2 `/`: 22911729664 available bytes; 98.72% used; 110409988 free inodes.

server2 `/home`: 22911729664 available bytes; 98.72% used; 110409988 free inodes.

server2 `/tmp`: 22911729664 available bytes; 98.72% used; 110409988 free inodes.

server2 `/var/tmp`: 22911729664 available bytes; 98.72% used; 110409988 free inodes.

server2 `/mnt/raid5`: 329059028992 available bytes; 97.73% used; 445089139 free inodes.
| server3 | True | [] | [] | reference_compatible=True |

server3 `/`: 84502069248 available bytes; 95.28% used; 114155531 free inodes.

server3 `/home`: 84502069248 available bytes; 95.28% used; 114155531 free inodes.

server3 `/data`: 142003974144 available bytes; 98.04% used; 225815185 free inodes.

server3 `/tmp`: 84502069248 available bytes; 95.28% used; 114155531 free inodes.

server3 `/var/tmp`: 84502069248 available bytes; 95.28% used; 114155531 free inodes.
| server4 | True | ['7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 105446670336 available bytes; 94.12% used; 114350250 free inodes.

server4 `/home`: 105446670336 available bytes; 94.12% used; 114350250 free inodes.

server4 `/data`: 238574477312 available bytes; 96.70% used; 224984013 free inodes.

server4 `/tmp`: 105446670336 available bytes; 94.12% used; 114350250 free inodes.

server4 `/var/tmp`: 105446662144 available bytes; 94.12% used; 114350250 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
