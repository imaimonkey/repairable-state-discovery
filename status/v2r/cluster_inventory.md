# V2R cluster inventory

2026-09-24T00:52:04.780193+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | [] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 325531172864 available bytes; 81.84% used; 112500358 free inodes.

server1 `/home`: 325531172864 available bytes; 81.84% used; 112500358 free inodes.

server1 `/tmp`: 325531172864 available bytes; 81.84% used; 112500358 free inodes.

server1 `/var/tmp`: 325531172864 available bytes; 81.84% used; 112500358 free inodes.

server1 `/mnt/raid5`: 1053121970176 available bytes; 95.17% used; 337734763 free inodes.
| server2 | True | [] | [] | reference_compatible=False |

server2 `/`: 40981598208 available bytes; 97.71% used; 110432256 free inodes.

server2 `/home`: 40981598208 available bytes; 97.71% used; 110432256 free inodes.

server2 `/tmp`: 40981598208 available bytes; 97.71% used; 110432256 free inodes.

server2 `/var/tmp`: 40981598208 available bytes; 97.71% used; 110432256 free inodes.

server2 `/mnt/raid5`: 532099072000 available bytes; 96.32% used; 445202566 free inodes.
| server3 | True | [] | ['/tmp', '/var/tmp'] | reference_compatible=True |

server3 `/`: 292341518336 available bytes; 83.69% used; 114188814 free inodes.

server3 `/home`: 292341518336 available bytes; 83.69% used; 114188814 free inodes.

server3 `/data`: 82164752384 available bytes; 98.86% used; 225843456 free inodes.

server3 `/tmp`: 292341518336 available bytes; 83.69% used; 114188814 free inodes.

server3 `/var/tmp`: 292341518336 available bytes; 83.69% used; 114188814 free inodes.
| server4 | True | ['1', '3', '6', '7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 106034216960 available bytes; 94.08% used; 114349761 free inodes.

server4 `/home`: 106034216960 available bytes; 94.08% used; 114349761 free inodes.

server4 `/data`: 292878843904 available bytes; 95.95% used; 225414555 free inodes.

server4 `/tmp`: 106034216960 available bytes; 94.08% used; 114349761 free inodes.

server4 `/var/tmp`: 106034216960 available bytes; 94.08% used; 114349761 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
