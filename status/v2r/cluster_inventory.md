# V2R cluster inventory

2026-09-23T23:08:36.183168+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | ['6', '7'] | ['/tmp', '/var/tmp', '/mnt/raid5'] | reference_compatible=False |

server1 `/`: 325672996864 available bytes; 81.83% used; 112501663 free inodes.

server1 `/home`: 325672996864 available bytes; 81.83% used; 112501663 free inodes.

server1 `/tmp`: 325672996864 available bytes; 81.83% used; 112501663 free inodes.

server1 `/var/tmp`: 325672996864 available bytes; 81.83% used; 112501663 free inodes.

server1 `/mnt/raid5`: 1387994042368 available bytes; 93.63% used; 337739775 free inodes.
| server2 | True | [] | [] | reference_compatible=False |

server2 `/`: 41058770944 available bytes; 97.71% used; 110432609 free inodes.

server2 `/home`: 41058770944 available bytes; 97.71% used; 110432609 free inodes.

server2 `/tmp`: 41058770944 available bytes; 97.71% used; 110432609 free inodes.

server2 `/var/tmp`: 41058770944 available bytes; 97.71% used; 110432609 free inodes.

server2 `/mnt/raid5`: 535132680192 available bytes; 96.30% used; 445205632 free inodes.
| server3 | True | ['3'] | ['/tmp', '/var/tmp'] | reference_compatible=True |

server3 `/`: 292552003584 available bytes; 83.67% used; 114189512 free inodes.

server3 `/home`: 292552003584 available bytes; 83.67% used; 114189512 free inodes.

server3 `/data`: 82346831872 available bytes; 98.86% used; 225846505 free inodes.

server3 `/tmp`: 292552003584 available bytes; 83.67% used; 114189512 free inodes.

server3 `/var/tmp`: 292552003584 available bytes; 83.67% used; 114189512 free inodes.
| server4 | True | ['3', '6', '7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 106277822464 available bytes; 94.07% used; 114353143 free inodes.

server4 `/home`: 106277822464 available bytes; 94.07% used; 114353143 free inodes.

server4 `/data`: 300050112512 available bytes; 95.85% used; 225430498 free inodes.

server4 `/tmp`: 106277822464 available bytes; 94.07% used; 114353143 free inodes.

server4 `/var/tmp`: 106277822464 available bytes; 94.07% used; 114353143 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
