# V2R cluster inventory

2026-09-24T05:43:40.172601+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | ['7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 324527882240 available bytes; 81.90% used; 112492128 free inodes.

server1 `/home`: 324527882240 available bytes; 81.90% used; 112492128 free inodes.

server1 `/tmp`: 324527882240 available bytes; 81.90% used; 112492128 free inodes.

server1 `/var/tmp`: 324527882240 available bytes; 81.90% used; 112492128 free inodes.

server1 `/mnt/raid5`: 517628198912 available bytes; 97.63% used; 337723939 free inodes.
| server2 | True | [] | [] | reference_compatible=False |

server2 `/`: 57914814464 available bytes; 96.77% used; 110431334 free inodes.

server2 `/home`: 57914814464 available bytes; 96.77% used; 110431334 free inodes.

server2 `/tmp`: 57914814464 available bytes; 96.77% used; 110431334 free inodes.

server2 `/var/tmp`: 57914814464 available bytes; 96.77% used; 110431334 free inodes.

server2 `/mnt/raid5`: 521428217856 available bytes; 96.40% used; 445193591 free inodes.
| server3 | True | [] | ['/tmp', '/var/tmp'] | reference_compatible=True |

server3 `/`: 126850949120 available bytes; 92.92% used; 114184793 free inodes.

server3 `/home`: 126850949120 available bytes; 92.92% used; 114184793 free inodes.

server3 `/data`: 185239236608 available bytes; 97.44% used; 225839114 free inodes.

server3 `/tmp`: 126850949120 available bytes; 92.92% used; 114184793 free inodes.

server3 `/var/tmp`: 126850949120 available bytes; 92.92% used; 114184793 free inodes.
| server4 | True | ['7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 105816322048 available bytes; 94.10% used; 114349351 free inodes.

server4 `/home`: 105816322048 available bytes; 94.10% used; 114349351 free inodes.

server4 `/data`: 251473874944 available bytes; 96.52% used; 225358017 free inodes.

server4 `/tmp`: 105816322048 available bytes; 94.10% used; 114349351 free inodes.

server4 `/var/tmp`: 105816322048 available bytes; 94.10% used; 114349351 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
