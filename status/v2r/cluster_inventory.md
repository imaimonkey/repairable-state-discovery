# V2R cluster inventory

2026-09-24T04:37:29.792767+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | ['7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 324628287488 available bytes; 81.89% used; 112492927 free inodes.

server1 `/home`: 324628287488 available bytes; 81.89% used; 112492927 free inodes.

server1 `/tmp`: 324628287488 available bytes; 81.89% used; 112492927 free inodes.

server1 `/var/tmp`: 324628287488 available bytes; 81.89% used; 112492927 free inodes.

server1 `/mnt/raid5`: 455306960896 available bytes; 97.91% used; 337724646 free inodes.
| server2 | True | [] | [] | reference_compatible=False |

server2 `/`: 40774627328 available bytes; 97.73% used; 110430504 free inodes.

server2 `/home`: 40774627328 available bytes; 97.73% used; 110430504 free inodes.

server2 `/tmp`: 40774627328 available bytes; 97.73% used; 110430504 free inodes.

server2 `/var/tmp`: 40774627328 available bytes; 97.73% used; 110430504 free inodes.

server2 `/mnt/raid5`: 524848308224 available bytes; 96.37% used; 445195818 free inodes.
| server3 | True | ['1'] | ['/tmp', '/var/tmp'] | reference_compatible=True |

server3 `/`: 292004016128 available bytes; 83.71% used; 114176140 free inodes.

server3 `/home`: 292004016128 available bytes; 83.71% used; 114176140 free inodes.

server3 `/data`: 24377012224 available bytes; 99.66% used; 225840789 free inodes.

server3 `/tmp`: 292004016128 available bytes; 83.71% used; 114176140 free inodes.

server3 `/var/tmp`: 292004016128 available bytes; 83.71% used; 114176140 free inodes.
| server4 | True | ['7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 105844170752 available bytes; 94.09% used; 114349416 free inodes.

server4 `/home`: 105844170752 available bytes; 94.09% used; 114349416 free inodes.

server4 `/data`: 253398691840 available bytes; 96.50% used; 225366872 free inodes.

server4 `/tmp`: 105844170752 available bytes; 94.09% used; 114349416 free inodes.

server4 `/var/tmp`: 105844170752 available bytes; 94.09% used; 114349416 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
