# V2R cluster inventory

2026-09-24T05:16:54.151730+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | ['7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 324594642944 available bytes; 81.89% used; 112492516 free inodes.

server1 `/home`: 324594642944 available bytes; 81.89% used; 112492516 free inodes.

server1 `/tmp`: 324594642944 available bytes; 81.89% used; 112492516 free inodes.

server1 `/var/tmp`: 324594642944 available bytes; 81.89% used; 112492516 free inodes.

server1 `/mnt/raid5`: 502625546240 available bytes; 97.69% used; 337724535 free inodes.
| server2 | True | [] | [] | reference_compatible=False |

server2 `/`: 40746008576 available bytes; 97.73% used; 110430356 free inodes.

server2 `/home`: 40746008576 available bytes; 97.73% used; 110430356 free inodes.

server2 `/tmp`: 40746008576 available bytes; 97.73% used; 110430356 free inodes.

server2 `/var/tmp`: 40746008576 available bytes; 97.73% used; 110430356 free inodes.

server2 `/mnt/raid5`: 522779762688 available bytes; 96.39% used; 445194113 free inodes.
| server3 | True | ['1'] | ['/tmp', '/var/tmp'] | reference_compatible=True |

server3 `/`: 291993149440 available bytes; 83.71% used; 114175932 free inodes.

server3 `/home`: 291993149440 available bytes; 83.71% used; 114175932 free inodes.

server3 `/data`: 21157752832 available bytes; 99.71% used; 225839941 free inodes.

server3 `/tmp`: 291993149440 available bytes; 83.71% used; 114175932 free inodes.

server3 `/var/tmp`: 291993149440 available bytes; 83.71% used; 114175932 free inodes.
| server4 | True | ['7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 105817829376 available bytes; 94.09% used; 114349379 free inodes.

server4 `/home`: 105817829376 available bytes; 94.09% used; 114349379 free inodes.

server4 `/data`: 252569726976 available bytes; 96.51% used; 225366604 free inodes.

server4 `/tmp`: 105817829376 available bytes; 94.09% used; 114349379 free inodes.

server4 `/var/tmp`: 105817829376 available bytes; 94.09% used; 114349379 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
