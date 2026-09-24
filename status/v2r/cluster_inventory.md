# V2R cluster inventory

2026-09-24T03:34:19.702868+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | ['7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 324893581312 available bytes; 81.88% used; 112494759 free inodes.

server1 `/home`: 324893581312 available bytes; 81.88% used; 112494759 free inodes.

server1 `/tmp`: 324893581312 available bytes; 81.88% used; 112494759 free inodes.

server1 `/var/tmp`: 324893581312 available bytes; 81.88% used; 112494759 free inodes.

server1 `/mnt/raid5`: 397488328704 available bytes; 98.18% used; 337734004 free inodes.
| server2 | True | [] | [] | reference_compatible=False |

server2 `/`: 40831832064 available bytes; 97.72% used; 110431070 free inodes.

server2 `/home`: 40831832064 available bytes; 97.72% used; 110431070 free inodes.

server2 `/tmp`: 40831832064 available bytes; 97.72% used; 110431070 free inodes.

server2 `/var/tmp`: 40831832064 available bytes; 97.72% used; 110431070 free inodes.

server2 `/mnt/raid5`: 527086100480 available bytes; 96.36% used; 445197810 free inodes.
| server3 | True | ['1'] | ['/tmp', '/var/tmp'] | reference_compatible=True |

server3 `/`: 292355723264 available bytes; 83.69% used; 114199418 free inodes.

server3 `/home`: 292355723264 available bytes; 83.69% used; 114199418 free inodes.

server3 `/data`: 36006858752 available bytes; 99.50% used; 225842953 free inodes.

server3 `/tmp`: 292355723264 available bytes; 83.69% used; 114199418 free inodes.

server3 `/var/tmp`: 292355723264 available bytes; 83.69% used; 114199418 free inodes.
| server4 | True | ['3', '7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 105986785280 available bytes; 94.09% used; 114349597 free inodes.

server4 `/home`: 105986785280 available bytes; 94.09% used; 114349597 free inodes.

server4 `/data`: 281272999936 available bytes; 96.11% used; 225385421 free inodes.

server4 `/tmp`: 105986785280 available bytes; 94.09% used; 114349597 free inodes.

server4 `/var/tmp`: 105986785280 available bytes; 94.09% used; 114349597 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
