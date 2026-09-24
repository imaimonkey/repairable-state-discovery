# V2R cluster inventory

2026-09-24T13:29:34.843273+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | [] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 324026228736 available bytes; 81.92% used; 112481477 free inodes.

server1 `/home`: 324026228736 available bytes; 81.92% used; 112481477 free inodes.

server1 `/tmp`: 324026228736 available bytes; 81.92% used; 112481477 free inodes.

server1 `/var/tmp`: 324026228736 available bytes; 81.92% used; 112481477 free inodes.

server1 `/mnt/raid5`: 417034432512 available bytes; 98.09% used; 337675263 free inodes.
| server2 | True | ['7'] | [] | reference_compatible=False |

server2 `/`: 57525760000 available bytes; 96.79% used; 110428729 free inodes.

server2 `/home`: 57525760000 available bytes; 96.79% used; 110428729 free inodes.

server2 `/tmp`: 57525760000 available bytes; 96.79% used; 110428729 free inodes.

server2 `/var/tmp`: 57525760000 available bytes; 96.79% used; 110428729 free inodes.

server2 `/mnt/raid5`: 506654830592 available bytes; 96.50% used; 445169809 free inodes.
| server3 | True | [] | [] | reference_compatible=True |

server3 `/`: 84705980416 available bytes; 95.27% used; 114165450 free inodes.

server3 `/home`: 84705980416 available bytes; 95.27% used; 114165450 free inodes.

server3 `/data`: 161270161408 available bytes; 97.77% used; 225803176 free inodes.

server3 `/tmp`: 84705980416 available bytes; 95.27% used; 114165450 free inodes.

server3 `/var/tmp`: 84705980416 available bytes; 95.27% used; 114165450 free inodes.
| server4 | True | [] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 105769738240 available bytes; 94.10% used; 114348741 free inodes.

server4 `/home`: 105769738240 available bytes; 94.10% used; 114348741 free inodes.

server4 `/data`: 90033119232 available bytes; 98.76% used; 225257178 free inodes.

server4 `/tmp`: 105769738240 available bytes; 94.10% used; 114348741 free inodes.

server4 `/var/tmp`: 105769738240 available bytes; 94.10% used; 114348741 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
