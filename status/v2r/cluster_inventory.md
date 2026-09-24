# V2R cluster inventory

2026-09-24T07:55:57.370070+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | ['7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 324417150976 available bytes; 81.90% used; 112490808 free inodes.

server1 `/home`: 324417150976 available bytes; 81.90% used; 112490808 free inodes.

server1 `/tmp`: 324417150976 available bytes; 81.90% used; 112490808 free inodes.

server1 `/var/tmp`: 324417150976 available bytes; 81.90% used; 112490808 free inodes.

server1 `/mnt/raid5`: 508292829184 available bytes; 97.67% used; 337722374 free inodes.
| server2 | True | [] | [] | reference_compatible=False |

server2 `/`: 57829093376 available bytes; 96.77% used; 110431084 free inodes.

server2 `/home`: 57829093376 available bytes; 96.77% used; 110431084 free inodes.

server2 `/tmp`: 57829093376 available bytes; 96.77% used; 110431084 free inodes.

server2 `/var/tmp`: 57829093376 available bytes; 96.77% used; 110431084 free inodes.

server2 `/mnt/raid5`: 516959547392 available bytes; 96.43% used; 445180663 free inodes.
| server3 | True | [] | [] | reference_compatible=True |

server3 `/`: 85485256704 available bytes; 95.23% used; 114175054 free inodes.

server3 `/home`: 85485256704 available bytes; 95.23% used; 114175054 free inodes.

server3 `/data`: 177874432000 available bytes; 97.54% used; 225839060 free inodes.

server3 `/tmp`: 85485256704 available bytes; 95.23% used; 114175054 free inodes.

server3 `/var/tmp`: 85485256704 available bytes; 95.23% used; 114175054 free inodes.
| server4 | True | [] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 105779453952 available bytes; 94.10% used; 114349166 free inodes.

server4 `/home`: 105779453952 available bytes; 94.10% used; 114349166 free inodes.

server4 `/data`: 284238512128 available bytes; 96.07% used; 225366085 free inodes.

server4 `/tmp`: 105779453952 available bytes; 94.10% used; 114349166 free inodes.

server4 `/var/tmp`: 105779453952 available bytes; 94.10% used; 114349166 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
