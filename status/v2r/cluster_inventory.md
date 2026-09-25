# V2R cluster inventory

2026-09-25T07:02:33.635209+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | [] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 318872055808 available bytes; 82.21% used; 112480377 free inodes.

server1 `/home`: 318872055808 available bytes; 82.21% used; 112480377 free inodes.

server1 `/tmp`: 318872055808 available bytes; 82.21% used; 112480377 free inodes.

server1 `/var/tmp`: 318872055808 available bytes; 82.21% used; 112480377 free inodes.

server1 `/mnt/raid5`: 399696494592 available bytes; 98.17% used; 337560450 free inodes.
| server2 | True | [] | [] | reference_compatible=False |

server2 `/`: 22879191040 available bytes; 98.72% used; 110410548 free inodes.

server2 `/home`: 22879191040 available bytes; 98.72% used; 110410548 free inodes.

server2 `/tmp`: 22879191040 available bytes; 98.72% used; 110410548 free inodes.

server2 `/var/tmp`: 22879191040 available bytes; 98.72% used; 110410548 free inodes.

server2 `/mnt/raid5`: 331707428864 available bytes; 97.71% used; 445098099 free inodes.
| server3 | True | [] | [] | reference_compatible=True |

server3 `/`: 84447113216 available bytes; 95.29% used; 114156029 free inodes.

server3 `/home`: 84447113216 available bytes; 95.29% used; 114156029 free inodes.

server3 `/data`: 142456655872 available bytes; 98.03% used; 225813178 free inodes.

server3 `/tmp`: 84447113216 available bytes; 95.29% used; 114156029 free inodes.

server3 `/var/tmp`: 84447113216 available bytes; 95.29% used; 114156029 free inodes.
| server4 | True | ['3'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 105638703104 available bytes; 94.10% used; 114350361 free inodes.

server4 `/home`: 105638703104 available bytes; 94.10% used; 114350361 free inodes.

server4 `/data`: 249495543808 available bytes; 96.55% used; 225017075 free inodes.

server4 `/tmp`: 105638703104 available bytes; 94.10% used; 114350361 free inodes.

server4 `/var/tmp`: 105638703104 available bytes; 94.10% used; 114350361 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
