# V2R cluster inventory

2026-09-24T04:24:44.916070+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | ['7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 324702298112 available bytes; 81.89% used; 112493232 free inodes.

server1 `/home`: 324702298112 available bytes; 81.89% used; 112493232 free inodes.

server1 `/tmp`: 324702298112 available bytes; 81.89% used; 112493232 free inodes.

server1 `/var/tmp`: 324702298112 available bytes; 81.89% used; 112493232 free inodes.

server1 `/mnt/raid5`: 440822534144 available bytes; 97.98% used; 337724698 free inodes.
| server2 | True | ['6'] | [] | reference_compatible=False |

server2 `/`: 40784101376 available bytes; 97.72% used; 110430622 free inodes.

server2 `/home`: 40784101376 available bytes; 97.72% used; 110430622 free inodes.

server2 `/tmp`: 40784101376 available bytes; 97.72% used; 110430622 free inodes.

server2 `/var/tmp`: 40784101376 available bytes; 97.72% used; 110430622 free inodes.

server2 `/mnt/raid5`: 525535711232 available bytes; 96.37% used; 445195896 free inodes.
| server3 | True | [] | ['/tmp', '/var/tmp'] | reference_compatible=True |

server3 `/`: 292020899840 available bytes; 83.70% used; 114176631 free inodes.

server3 `/home`: 292020899840 available bytes; 83.70% used; 114176631 free inodes.

server3 `/data`: 31681613824 available bytes; 99.56% used; 225841173 free inodes.

server3 `/tmp`: 292020899840 available bytes; 83.70% used; 114176631 free inodes.

server3 `/var/tmp`: 292020899840 available bytes; 83.70% used; 114176631 free inodes.
| server4 | True | ['7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 105844715520 available bytes; 94.09% used; 114349421 free inodes.

server4 `/home`: 105844715520 available bytes; 94.09% used; 114349421 free inodes.

server4 `/data`: 256715608064 available bytes; 96.45% used; 225381783 free inodes.

server4 `/tmp`: 105844715520 available bytes; 94.09% used; 114349421 free inodes.

server4 `/var/tmp`: 105844715520 available bytes; 94.09% used; 114349421 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
