# V2R cluster inventory

2026-09-25T12:16:16.713063+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | [] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 319200706560 available bytes; 82.19% used; 112477784 free inodes.

server1 `/home`: 319200706560 available bytes; 82.19% used; 112477784 free inodes.

server1 `/tmp`: 319200706560 available bytes; 82.19% used; 112477784 free inodes.

server1 `/var/tmp`: 319200706560 available bytes; 82.19% used; 112477784 free inodes.

server1 `/mnt/raid5`: 364316028928 available bytes; 98.33% used; 337548293 free inodes.
| server2 | True | ['2', '3', '4', '5', '6'] | [] | reference_compatible=False |

server2 `/`: 22901760000 available bytes; 98.72% used; 110409955 free inodes.

server2 `/home`: 22901760000 available bytes; 98.72% used; 110409955 free inodes.

server2 `/tmp`: 22901760000 available bytes; 98.72% used; 110409955 free inodes.

server2 `/var/tmp`: 22901760000 available bytes; 98.72% used; 110409955 free inodes.

server2 `/mnt/raid5`: 325355249664 available bytes; 97.75% used; 445080813 free inodes.
| server3 | True | [] | [] | reference_compatible=True |

server3 `/`: 84210286592 available bytes; 95.30% used; 114154982 free inodes.

server3 `/home`: 84210286592 available bytes; 95.30% used; 114154982 free inodes.

server3 `/data`: 142279897088 available bytes; 98.03% used; 225811358 free inodes.

server3 `/tmp`: 84210286592 available bytes; 95.30% used; 114154982 free inodes.

server3 `/var/tmp`: 84210286592 available bytes; 95.30% used; 114154982 free inodes.
| server4 | True | ['3'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 105666572288 available bytes; 94.10% used; 114349724 free inodes.

server4 `/home`: 105666572288 available bytes; 94.10% used; 114349724 free inodes.

server4 `/data`: 232051892224 available bytes; 96.79% used; 224966183 free inodes.

server4 `/tmp`: 105666572288 available bytes; 94.10% used; 114349724 free inodes.

server4 `/var/tmp`: 105666572288 available bytes; 94.10% used; 114349724 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
