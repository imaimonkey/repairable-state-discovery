# V2R cluster inventory

2026-09-24T04:51:40.665246+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | ['7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 324621000704 available bytes; 81.89% used; 112492793 free inodes.

server1 `/home`: 324621000704 available bytes; 81.89% used; 112492793 free inodes.

server1 `/tmp`: 324621000704 available bytes; 81.89% used; 112492793 free inodes.

server1 `/var/tmp`: 324621000704 available bytes; 81.89% used; 112492793 free inodes.

server1 `/mnt/raid5`: 474677075968 available bytes; 97.82% used; 337724585 free inodes.
| server2 | True | [] | [] | reference_compatible=False |

server2 `/`: 40767987712 available bytes; 97.73% used; 110430452 free inodes.

server2 `/home`: 40767987712 available bytes; 97.73% used; 110430452 free inodes.

server2 `/tmp`: 40767987712 available bytes; 97.73% used; 110430452 free inodes.

server2 `/var/tmp`: 40767987712 available bytes; 97.73% used; 110430452 free inodes.

server2 `/mnt/raid5`: 523846094848 available bytes; 96.38% used; 445195079 free inodes.
| server3 | True | ['1'] | ['/tmp', '/var/tmp'] | reference_compatible=True |

server3 `/`: 292379635712 available bytes; 83.68% used; 114199922 free inodes.

server3 `/home`: 292379635712 available bytes; 83.68% used; 114199922 free inodes.

server3 `/data`: 24356597760 available bytes; 99.66% used; 225840588 free inodes.

server3 `/tmp`: 292379635712 available bytes; 83.68% used; 114199922 free inodes.

server3 `/var/tmp`: 292379635712 available bytes; 83.68% used; 114199922 free inodes.
| server4 | True | ['7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 105835880448 available bytes; 94.09% used; 114349393 free inodes.

server4 `/home`: 105835880448 available bytes; 94.09% used; 114349393 free inodes.

server4 `/data`: 253376630784 available bytes; 96.50% used; 225366843 free inodes.

server4 `/tmp`: 105835880448 available bytes; 94.09% used; 114349393 free inodes.

server4 `/var/tmp`: 105835880448 available bytes; 94.09% used; 114349393 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
