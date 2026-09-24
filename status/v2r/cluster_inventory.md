# V2R cluster inventory

2026-09-24T18:18:30.967152+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | ['7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 324010102784 available bytes; 81.92% used; 112481443 free inodes.

server1 `/home`: 324010102784 available bytes; 81.92% used; 112481443 free inodes.

server1 `/tmp`: 324010102784 available bytes; 81.92% used; 112481443 free inodes.

server1 `/var/tmp`: 324010102784 available bytes; 81.92% used; 112481443 free inodes.

server1 `/mnt/raid5`: 416343023616 available bytes; 98.09% used; 337640736 free inodes.
| server2 | True | [] | [] | reference_compatible=False |

server2 `/`: 54496288768 available bytes; 96.96% used; 110412038 free inodes.

server2 `/home`: 54496288768 available bytes; 96.96% used; 110412038 free inodes.

server2 `/tmp`: 54496288768 available bytes; 96.96% used; 110412038 free inodes.

server2 `/var/tmp`: 54496288768 available bytes; 96.96% used; 110412038 free inodes.

server2 `/mnt/raid5`: 497079177216 available bytes; 96.57% used; 445160727 free inodes.
| server3 | True | ['1'] | [] | reference_compatible=True |

server3 `/`: 84408504320 available bytes; 95.29% used; 114156135 free inodes.

server3 `/home`: 84408504320 available bytes; 95.29% used; 114156135 free inodes.

server3 `/data`: 153041420288 available bytes; 97.88% used; 225800727 free inodes.

server3 `/tmp`: 84408504320 available bytes; 95.29% used; 114156135 free inodes.

server3 `/var/tmp`: 84408504320 available bytes; 95.29% used; 114156135 free inodes.
| server4 | True | [] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 105662775296 available bytes; 94.10% used; 114348516 free inodes.

server4 `/home`: 105662775296 available bytes; 94.10% used; 114348516 free inodes.

server4 `/data`: 90068934656 available bytes; 98.76% used; 225268134 free inodes.

server4 `/tmp`: 105662775296 available bytes; 94.10% used; 114348516 free inodes.

server4 `/var/tmp`: 105662775296 available bytes; 94.10% used; 114348516 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
