# V2R cluster inventory

2026-09-24T04:10:28.460109+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | ['7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 324710989824 available bytes; 81.89% used; 112493429 free inodes.

server1 `/home`: 324710989824 available bytes; 81.89% used; 112493429 free inodes.

server1 `/tmp`: 324710989824 available bytes; 81.89% used; 112493429 free inodes.

server1 `/var/tmp`: 324710989824 available bytes; 81.89% used; 112493429 free inodes.

server1 `/mnt/raid5`: 426307858432 available bytes; 98.04% used; 337724760 free inodes.
| server2 | True | [] | [] | reference_compatible=False |

server2 `/`: 40799621120 available bytes; 97.72% used; 110430796 free inodes.

server2 `/home`: 40799621120 available bytes; 97.72% used; 110430796 free inodes.

server2 `/tmp`: 40799621120 available bytes; 97.72% used; 110430796 free inodes.

server2 `/var/tmp`: 40799621120 available bytes; 97.72% used; 110430796 free inodes.

server2 `/mnt/raid5`: 525968130048 available bytes; 96.37% used; 445196445 free inodes.
| server3 | True | ['1'] | ['/tmp', '/var/tmp'] | reference_compatible=True |

server3 `/`: 292025995264 available bytes; 83.70% used; 114176971 free inodes.

server3 `/home`: 292025995264 available bytes; 83.70% used; 114176971 free inodes.

server3 `/data`: 31738073088 available bytes; 99.56% used; 225841851 free inodes.

server3 `/tmp`: 292025995264 available bytes; 83.70% used; 114176971 free inodes.

server3 `/var/tmp`: 292025995264 available bytes; 83.70% used; 114176971 free inodes.
| server4 | True | ['7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 105790857216 available bytes; 94.10% used; 114349473 free inodes.

server4 `/home`: 105790857216 available bytes; 94.10% used; 114349473 free inodes.

server4 `/data`: 256722825216 available bytes; 96.45% used; 225381855 free inodes.

server4 `/tmp`: 105790857216 available bytes; 94.10% used; 114349473 free inodes.

server4 `/var/tmp`: 105790857216 available bytes; 94.10% used; 114349473 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
