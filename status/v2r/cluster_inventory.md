# V2R cluster inventory

2026-09-25T15:13:45.857112+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | ['4'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 319044091904 available bytes; 82.20% used; 112476393 free inodes.

server1 `/home`: 319044091904 available bytes; 82.20% used; 112476393 free inodes.

server1 `/tmp`: 319044091904 available bytes; 82.20% used; 112476393 free inodes.

server1 `/var/tmp`: 319044091904 available bytes; 82.20% used; 112476393 free inodes.

server1 `/mnt/raid5`: 343319486464 available bytes; 98.43% used; 337545942 free inodes.
| server2 | True | ['2', '3', '4', '5', '6'] | [] | reference_compatible=False |

server2 `/`: 23109763072 available bytes; 98.71% used; 110407927 free inodes.

server2 `/home`: 23109763072 available bytes; 98.71% used; 110407927 free inodes.

server2 `/tmp`: 23109763072 available bytes; 98.71% used; 110407927 free inodes.

server2 `/var/tmp`: 23109763072 available bytes; 98.71% used; 110407927 free inodes.

server2 `/mnt/raid5`: 320431292416 available bytes; 97.79% used; 445073621 free inodes.
| server3 | True | [] | [] | reference_compatible=True |

server3 `/`: 84426088448 available bytes; 95.29% used; 114153450 free inodes.

server3 `/home`: 84426088448 available bytes; 95.29% used; 114153450 free inodes.

server3 `/data`: 142181494784 available bytes; 98.03% used; 225807999 free inodes.

server3 `/tmp`: 84426088448 available bytes; 95.29% used; 114153450 free inodes.

server3 `/var/tmp`: 84426088448 available bytes; 95.29% used; 114153450 free inodes.
| server4 | True | ['3', '5'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 105638400000 available bytes; 94.10% used; 114349692 free inodes.

server4 `/home`: 105638400000 available bytes; 94.10% used; 114349692 free inodes.

server4 `/data`: 231348285440 available bytes; 96.80% used; 224944763 free inodes.

server4 `/tmp`: 105638400000 available bytes; 94.10% used; 114349692 free inodes.

server4 `/var/tmp`: 105638400000 available bytes; 94.10% used; 114349692 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
