# V2R cluster inventory

2026-09-23T21:48:37.442907+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | ['6', '7'] | ['/tmp', '/var/tmp', '/mnt/raid5'] | reference_compatible=False |

server1 `/`: 325714567168 available bytes; 81.83% used; 112501406 free inodes.

server1 `/home`: 325714567168 available bytes; 81.83% used; 112501406 free inodes.

server1 `/tmp`: 325714567168 available bytes; 81.83% used; 112501406 free inodes.

server1 `/var/tmp`: 325714567168 available bytes; 81.83% used; 112501406 free inodes.

server1 `/mnt/raid5`: 1388124778496 available bytes; 93.63% used; 337739916 free inodes.
| server2 | True | [] | [] | reference_compatible=False |

server2 `/`: 41107087360 available bytes; 97.71% used; 110432650 free inodes.

server2 `/home`: 41107087360 available bytes; 97.71% used; 110432650 free inodes.

server2 `/tmp`: 41107087360 available bytes; 97.71% used; 110432650 free inodes.

server2 `/var/tmp`: 41107087360 available bytes; 97.71% used; 110432650 free inodes.

server2 `/mnt/raid5`: 537942802432 available bytes; 96.28% used; 445207950 free inodes.
| server3 | True | [] | ['/tmp', '/var/tmp'] | reference_compatible=True |

server3 `/`: 292123734016 available bytes; 83.70% used; 114160157 free inodes.

server3 `/home`: 292123734016 available bytes; 83.70% used; 114160157 free inodes.

server3 `/data`: 82471501824 available bytes; 98.86% used; 225848095 free inodes.

server3 `/tmp`: 292123734016 available bytes; 83.70% used; 114160157 free inodes.

server3 `/var/tmp`: 292123734016 available bytes; 83.70% used; 114160157 free inodes.
| server4 | True | ['3', '5', '6', '7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 106466291712 available bytes; 94.06% used; 114355857 free inodes.

server4 `/home`: 106466291712 available bytes; 94.06% used; 114355857 free inodes.

server4 `/data`: 300239192064 available bytes; 95.85% used; 225447285 free inodes.

server4 `/tmp`: 106466291712 available bytes; 94.06% used; 114355857 free inodes.

server4 `/var/tmp`: 106466291712 available bytes; 94.06% used; 114355857 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
