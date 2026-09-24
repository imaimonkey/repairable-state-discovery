# V2R cluster inventory

2026-09-24T13:06:15.241427+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | [] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 324040052736 available bytes; 81.92% used; 112481558 free inodes.

server1 `/home`: 324040052736 available bytes; 81.92% used; 112481558 free inodes.

server1 `/tmp`: 324040052736 available bytes; 81.92% used; 112481558 free inodes.

server1 `/var/tmp`: 324040052736 available bytes; 81.92% used; 112481558 free inodes.

server1 `/mnt/raid5`: 417078255616 available bytes; 98.09% used; 337678002 free inodes.
| server2 | True | ['7'] | [] | reference_compatible=False |

server2 `/`: 57554292736 available bytes; 96.79% used; 110428973 free inodes.

server2 `/home`: 57554292736 available bytes; 96.79% used; 110428973 free inodes.

server2 `/tmp`: 57554292736 available bytes; 96.79% used; 110428973 free inodes.

server2 `/var/tmp`: 57554292736 available bytes; 96.79% used; 110428973 free inodes.

server2 `/mnt/raid5`: 507373764608 available bytes; 96.49% used; 445170683 free inodes.
| server3 | True | [] | [] | reference_compatible=True |

server3 `/`: 85617123328 available bytes; 95.22% used; 114192925 free inodes.

server3 `/home`: 85617123328 available bytes; 95.22% used; 114192925 free inodes.

server3 `/data`: 162652753920 available bytes; 97.75% used; 225813021 free inodes.

server3 `/tmp`: 85617123328 available bytes; 95.22% used; 114192925 free inodes.

server3 `/var/tmp`: 85617123328 available bytes; 95.22% used; 114192925 free inodes.
| server4 | True | [] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 105770745856 available bytes; 94.10% used; 114348761 free inodes.

server4 `/home`: 105770745856 available bytes; 94.10% used; 114348761 free inodes.

server4 `/data`: 90037895168 available bytes; 98.76% used; 225257181 free inodes.

server4 `/tmp`: 105770745856 available bytes; 94.10% used; 114348761 free inodes.

server4 `/var/tmp`: 105770745856 available bytes; 94.10% used; 114348761 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
