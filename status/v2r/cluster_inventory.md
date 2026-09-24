# V2R cluster inventory

2026-09-24T04:59:33.747021+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | ['7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 324616638464 available bytes; 81.89% used; 112492718 free inodes.

server1 `/home`: 324616638464 available bytes; 81.89% used; 112492718 free inodes.

server1 `/tmp`: 324616638464 available bytes; 81.89% used; 112492718 free inodes.

server1 `/var/tmp`: 324616638464 available bytes; 81.89% used; 112492718 free inodes.

server1 `/mnt/raid5`: 479514591232 available bytes; 97.80% used; 337724566 free inodes.
| server2 | True | [] | [] | reference_compatible=False |

server2 `/`: 40760070144 available bytes; 97.73% used; 110430424 free inodes.

server2 `/home`: 40760070144 available bytes; 97.73% used; 110430424 free inodes.

server2 `/tmp`: 40760070144 available bytes; 97.73% used; 110430424 free inodes.

server2 `/var/tmp`: 40760070144 available bytes; 97.73% used; 110430424 free inodes.

server2 `/mnt/raid5`: 523078832128 available bytes; 96.39% used; 445194705 free inodes.
| server3 | True | ['1'] | ['/tmp', '/var/tmp'] | reference_compatible=True |

server3 `/`: 292382568448 available bytes; 83.68% used; 114199928 free inodes.

server3 `/home`: 292382568448 available bytes; 83.68% used; 114199928 free inodes.

server3 `/data`: 23299837952 available bytes; 99.68% used; 225840421 free inodes.

server3 `/tmp`: 292382568448 available bytes; 83.68% used; 114199928 free inodes.

server3 `/var/tmp`: 292382568448 available bytes; 83.68% used; 114199928 free inodes.
| server4 | True | ['7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 105835520000 available bytes; 94.09% used; 114349392 free inodes.

server4 `/home`: 105835520000 available bytes; 94.09% used; 114349392 free inodes.

server4 `/data`: 252706271232 available bytes; 96.51% used; 225366819 free inodes.

server4 `/tmp`: 105835520000 available bytes; 94.09% used; 114349392 free inodes.

server4 `/var/tmp`: 105835520000 available bytes; 94.09% used; 114349392 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
