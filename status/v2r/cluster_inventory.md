# V2R cluster inventory

2026-09-24T04:56:24.726342+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | ['7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 324619956224 available bytes; 81.89% used; 112492754 free inodes.

server1 `/home`: 324619956224 available bytes; 81.89% used; 112492754 free inodes.

server1 `/tmp`: 324619956224 available bytes; 81.89% used; 112492754 free inodes.

server1 `/var/tmp`: 324619956224 available bytes; 81.89% used; 112492754 free inodes.

server1 `/mnt/raid5`: 479516090368 available bytes; 97.80% used; 337724576 free inodes.
| server2 | True | [] | [] | reference_compatible=False |

server2 `/`: 40763121664 available bytes; 97.73% used; 110430436 free inodes.

server2 `/home`: 40763121664 available bytes; 97.73% used; 110430436 free inodes.

server2 `/tmp`: 40763121664 available bytes; 97.73% used; 110430436 free inodes.

server2 `/var/tmp`: 40763121664 available bytes; 97.73% used; 110430436 free inodes.

server2 `/mnt/raid5`: 523699535872 available bytes; 96.38% used; 445194837 free inodes.
| server3 | True | ['1'] | ['/tmp', '/var/tmp'] | reference_compatible=True |

server3 `/`: 292390449152 available bytes; 83.68% used; 114200015 free inodes.

server3 `/home`: 292390449152 available bytes; 83.68% used; 114200015 free inodes.

server3 `/data`: 23306448896 available bytes; 99.68% used; 225840472 free inodes.

server3 `/tmp`: 292390449152 available bytes; 83.68% used; 114200015 free inodes.

server3 `/var/tmp`: 292390449152 available bytes; 83.68% used; 114200015 free inodes.
| server4 | True | ['7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 105835704320 available bytes; 94.09% used; 114349396 free inodes.

server4 `/home`: 105835704320 available bytes; 94.09% used; 114349396 free inodes.

server4 `/data`: 252709879808 available bytes; 96.51% used; 225366830 free inodes.

server4 `/tmp`: 105835704320 available bytes; 94.09% used; 114349396 free inodes.

server4 `/var/tmp`: 105835704320 available bytes; 94.09% used; 114349396 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
