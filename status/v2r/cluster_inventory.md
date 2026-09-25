# V2R cluster inventory

2026-09-25T02:39:07.964304+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | [] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 318959099904 available bytes; 82.21% used; 112480422 free inodes.

server1 `/home`: 318959099904 available bytes; 82.21% used; 112480422 free inodes.

server1 `/tmp`: 318959099904 available bytes; 82.21% used; 112480422 free inodes.

server1 `/var/tmp`: 318959099904 available bytes; 82.21% used; 112480422 free inodes.

server1 `/mnt/raid5`: 416192000000 available bytes; 98.09% used; 337604885 free inodes.
| server2 | True | [] | [] | reference_compatible=False |

server2 `/`: 23007940608 available bytes; 98.72% used; 110410439 free inodes.

server2 `/home`: 23007940608 available bytes; 98.72% used; 110410439 free inodes.

server2 `/tmp`: 23007940608 available bytes; 98.72% used; 110410439 free inodes.

server2 `/var/tmp`: 23007940608 available bytes; 98.72% used; 110410439 free inodes.

server2 `/mnt/raid5`: 482826977280 available bytes; 96.66% used; 445113440 free inodes.
| server3 | True | [] | [] | reference_compatible=True |

server3 `/`: 84350996480 available bytes; 95.29% used; 114156077 free inodes.

server3 `/home`: 84350996480 available bytes; 95.29% used; 114156077 free inodes.

server3 `/data`: 145446899712 available bytes; 97.99% used; 225811080 free inodes.

server3 `/tmp`: 84350996480 available bytes; 95.29% used; 114156077 free inodes.

server3 `/var/tmp`: 84350996480 available bytes; 95.29% used; 114156077 free inodes.
| server4 | True | ['0', '3', '5', '7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 105895559168 available bytes; 94.09% used; 114350970 free inodes.

server4 `/home`: 105895559168 available bytes; 94.09% used; 114350970 free inodes.

server4 `/data`: 1501597696 available bytes; 99.98% used; 224968858 free inodes.

server4 `/tmp`: 105895559168 available bytes; 94.09% used; 114350970 free inodes.

server4 `/var/tmp`: 105895559168 available bytes; 94.09% used; 114350970 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
