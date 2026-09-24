# V2R cluster inventory

2026-09-24T04:05:44.374949+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | ['7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 324718264320 available bytes; 81.89% used; 112493481 free inodes.

server1 `/home`: 324718264320 available bytes; 81.89% used; 112493481 free inodes.

server1 `/tmp`: 324718264320 available bytes; 81.89% used; 112493481 free inodes.

server1 `/var/tmp`: 324718264320 available bytes; 81.89% used; 112493481 free inodes.

server1 `/mnt/raid5`: 421469937664 available bytes; 98.07% used; 337724767 free inodes.
| server2 | True | [] | [] | reference_compatible=False |

server2 `/`: 40804270080 available bytes; 97.72% used; 110430838 free inodes.

server2 `/home`: 40804270080 available bytes; 97.72% used; 110430838 free inodes.

server2 `/tmp`: 40804270080 available bytes; 97.72% used; 110430838 free inodes.

server2 `/var/tmp`: 40804270080 available bytes; 97.72% used; 110430838 free inodes.

server2 `/mnt/raid5`: 526124834816 available bytes; 96.36% used; 445196838 free inodes.
| server3 | True | ['1'] | ['/tmp', '/var/tmp'] | reference_compatible=True |

server3 `/`: 291977551872 available bytes; 83.71% used; 114176973 free inodes.

server3 `/home`: 291977551872 available bytes; 83.71% used; 114176973 free inodes.

server3 `/data`: 31740821504 available bytes; 99.56% used; 225841961 free inodes.

server3 `/tmp`: 291977551872 available bytes; 83.71% used; 114176973 free inodes.

server3 `/var/tmp`: 291977551872 available bytes; 83.71% used; 114176973 free inodes.
| server4 | True | ['7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 105791086592 available bytes; 94.10% used; 114349490 free inodes.

server4 `/home`: 105791086592 available bytes; 94.10% used; 114349490 free inodes.

server4 `/data`: 256728006656 available bytes; 96.45% used; 225381889 free inodes.

server4 `/tmp`: 105791086592 available bytes; 94.10% used; 114349490 free inodes.

server4 `/var/tmp`: 105791086592 available bytes; 94.10% used; 114349490 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
