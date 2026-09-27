# V2R cluster inventory

2026-09-27T06:45:20.798922+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | ['2', '3', '4', '5', '6', '7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 314487508992 available bytes; 82.46% used; 112440809 free inodes.

server1 `/home`: 314487508992 available bytes; 82.46% used; 112440809 free inodes.

server1 `/tmp`: 314487508992 available bytes; 82.46% used; 112440809 free inodes.

server1 `/var/tmp`: 314487508992 available bytes; 82.46% used; 112440809 free inodes.

server1 `/mnt/raid5`: 634673786880 available bytes; 97.09% used; 337400006 free inodes.
| server2 | True | [] | [] | reference_compatible=False |

server2 `/`: 17612120064 available bytes; 99.02% used; 110365003 free inodes.

server2 `/home`: 17612120064 available bytes; 99.02% used; 110365003 free inodes.

server2 `/tmp`: 17612120064 available bytes; 99.02% used; 110365003 free inodes.

server2 `/var/tmp`: 17612120064 available bytes; 99.02% used; 110365003 free inodes.

server2 `/mnt/raid5`: 572677689344 available bytes; 96.04% used; 444875590 free inodes.
| server3 | True | [] | [] | reference_compatible=True |

server3 `/`: 78582423552 available bytes; 95.61% used; 114062893 free inodes.

server3 `/home`: 78582423552 available bytes; 95.61% used; 114062893 free inodes.

server3 `/data`: 1333254594560 available bytes; 81.57% used; 225765068 free inodes.

server3 `/tmp`: 78582423552 available bytes; 95.61% used; 114062893 free inodes.

server3 `/var/tmp`: 78582423552 available bytes; 95.61% used; 114062893 free inodes.
| server4 | True | ['5'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 110980952064 available bytes; 93.81% used; 114372897 free inodes.

server4 `/home`: 110980952064 available bytes; 93.81% used; 114372897 free inodes.

server4 `/data`: 374443372544 available bytes; 94.83% used; 224771150 free inodes.

server4 `/tmp`: 110980952064 available bytes; 93.81% used; 114372897 free inodes.

server4 `/var/tmp`: 110980952064 available bytes; 93.81% used; 114372897 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
