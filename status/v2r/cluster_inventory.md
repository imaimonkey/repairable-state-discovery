# V2R cluster inventory

2026-09-23T16:01:45.659211+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | False | [] | [] | reference_compatible=False |
| server2 | True | ['7'] | [] | reference_compatible=False |

server2 `/`: 41416822784 available bytes; 97.69% used; 110435187 free inodes.

server2 `/home`: 41416822784 available bytes; 97.69% used; 110435187 free inodes.

server2 `/tmp`: 41416822784 available bytes; 97.69% used; 110435187 free inodes.

server2 `/var/tmp`: 41416822784 available bytes; 97.69% used; 110435187 free inodes.

server2 `/mnt/raid5`: 549636386816 available bytes; 96.20% used; 445218725 free inodes.
| server3 | True | ['0'] | ['/tmp', '/var/tmp'] | reference_compatible=True |

server3 `/`: 358646530048 available bytes; 79.99% used; 114296127 free inodes.

server3 `/home`: 358646530048 available bytes; 79.99% used; 114296127 free inodes.

server3 `/data`: 125331468288 available bytes; 98.27% used; 225854585 free inodes.

server3 `/tmp`: 358646530048 available bytes; 79.99% used; 114296127 free inodes.

server3 `/var/tmp`: 358646530048 available bytes; 79.99% used; 114296127 free inodes.
| server4 | True | ['3', '5', '6'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 111499071488 available bytes; 93.78% used; 114375780 free inodes.

server4 `/home`: 111499071488 available bytes; 93.78% used; 114375780 free inodes.

server4 `/data`: 37523869696 available bytes; 99.48% used; 225486642 free inodes.

server4 `/tmp`: 111499071488 available bytes; 93.78% used; 114375780 free inodes.

server4 `/var/tmp`: 111499071488 available bytes; 93.78% used; 114375780 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
