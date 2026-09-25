# V2R cluster inventory

2026-09-25T09:44:54.557542+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | [] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 318837239808 available bytes; 82.21% used; 112480391 free inodes.

server1 `/home`: 318837239808 available bytes; 82.21% used; 112480391 free inodes.

server1 `/tmp`: 318837239808 available bytes; 82.21% used; 112480391 free inodes.

server1 `/var/tmp`: 318837239808 available bytes; 82.21% used; 112480391 free inodes.

server1 `/mnt/raid5`: 350357389312 available bytes; 98.39% used; 337556827 free inodes.
| server2 | True | ['6'] | [] | reference_compatible=False |

server2 `/`: 22836166656 available bytes; 98.73% used; 110410484 free inodes.

server2 `/home`: 22836166656 available bytes; 98.73% used; 110410484 free inodes.

server2 `/tmp`: 22836166656 available bytes; 98.73% used; 110410484 free inodes.

server2 `/var/tmp`: 22836166656 available bytes; 98.73% used; 110410484 free inodes.

server2 `/mnt/raid5`: 331294986240 available bytes; 97.71% used; 445091950 free inodes.
| server3 | True | [] | [] | reference_compatible=True |

server3 `/`: 84417728512 available bytes; 95.29% used; 114156043 free inodes.

server3 `/home`: 84417728512 available bytes; 95.29% used; 114156043 free inodes.

server3 `/data`: 142296440832 available bytes; 98.03% used; 225810410 free inodes.

server3 `/tmp`: 84417728512 available bytes; 95.29% used; 114156043 free inodes.

server3 `/var/tmp`: 84417728512 available bytes; 95.29% used; 114156043 free inodes.
| server4 | True | ['4'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 105623314432 available bytes; 94.11% used; 114350294 free inodes.

server4 `/home`: 105623314432 available bytes; 94.11% used; 114350294 free inodes.

server4 `/data`: 240047550464 available bytes; 96.68% used; 224993676 free inodes.

server4 `/tmp`: 105623314432 available bytes; 94.11% used; 114350294 free inodes.

server4 `/var/tmp`: 105623314432 available bytes; 94.11% used; 114350294 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
