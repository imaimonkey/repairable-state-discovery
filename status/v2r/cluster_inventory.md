# V2R cluster inventory

2026-09-25T07:16:19.992791+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | [] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 318872420352 available bytes; 82.21% used; 112480376 free inodes.

server1 `/home`: 318872420352 available bytes; 82.21% used; 112480376 free inodes.

server1 `/tmp`: 318872420352 available bytes; 82.21% used; 112480376 free inodes.

server1 `/var/tmp`: 318872420352 available bytes; 82.21% used; 112480376 free inodes.

server1 `/mnt/raid5`: 385928798208 available bytes; 98.23% used; 337558516 free inodes.
| server2 | True | ['7'] | [] | reference_compatible=False |

server2 `/`: 22867582976 available bytes; 98.72% used; 110410498 free inodes.

server2 `/home`: 22867582976 available bytes; 98.72% used; 110410498 free inodes.

server2 `/tmp`: 22867582976 available bytes; 98.72% used; 110410498 free inodes.

server2 `/var/tmp`: 22867582976 available bytes; 98.72% used; 110410498 free inodes.

server2 `/mnt/raid5`: 350468722688 available bytes; 97.58% used; 445097817 free inodes.
| server3 | True | [] | [] | reference_compatible=True |

server3 `/`: 84447490048 available bytes; 95.29% used; 114156017 free inodes.

server3 `/home`: 84447490048 available bytes; 95.29% used; 114156017 free inodes.

server3 `/data`: 142459121664 available bytes; 98.03% used; 225812960 free inodes.

server3 `/tmp`: 84447490048 available bytes; 95.29% used; 114156017 free inodes.

server3 `/var/tmp`: 84447490048 available bytes; 95.29% used; 114156017 free inodes.
| server4 | True | ['3'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 105638309888 available bytes; 94.10% used; 114350361 free inodes.

server4 `/home`: 105638309888 available bytes; 94.10% used; 114350361 free inodes.

server4 `/data`: 249488048128 available bytes; 96.55% used; 225015915 free inodes.

server4 `/tmp`: 105638309888 available bytes; 94.10% used; 114350361 free inodes.

server4 `/var/tmp`: 105638309888 available bytes; 94.10% used; 114350361 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
