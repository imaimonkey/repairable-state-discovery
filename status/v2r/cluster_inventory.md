# V2R cluster inventory

2026-09-24T16:42:30.126227+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | ['7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 324026126336 available bytes; 81.92% used; 112481468 free inodes.

server1 `/home`: 324026126336 available bytes; 81.92% used; 112481468 free inodes.

server1 `/tmp`: 324026126336 available bytes; 81.92% used; 112481468 free inodes.

server1 `/var/tmp`: 324026126336 available bytes; 81.92% used; 112481468 free inodes.

server1 `/mnt/raid5`: 416548155392 available bytes; 98.09% used; 337651938 free inodes.
| server2 | True | ['7'] | [] | reference_compatible=False |

server2 `/`: 57087127552 available bytes; 96.82% used; 110418220 free inodes.

server2 `/home`: 57087127552 available bytes; 96.82% used; 110418220 free inodes.

server2 `/tmp`: 57087127552 available bytes; 96.82% used; 110418220 free inodes.

server2 `/var/tmp`: 57087127552 available bytes; 96.82% used; 110418220 free inodes.

server2 `/mnt/raid5`: 500552200192 available bytes; 96.54% used; 445163924 free inodes.
| server3 | True | [] | [] | reference_compatible=True |

server3 `/`: 84266876928 available bytes; 95.30% used; 114151530 free inodes.

server3 `/home`: 84266876928 available bytes; 95.30% used; 114151530 free inodes.

server3 `/data`: 159274283008 available bytes; 97.80% used; 225787728 free inodes.

server3 `/tmp`: 84266876928 available bytes; 95.30% used; 114151530 free inodes.

server3 `/var/tmp`: 84266876928 available bytes; 95.30% used; 114151530 free inodes.
| server4 | True | [] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 105683103744 available bytes; 94.10% used; 114348574 free inodes.

server4 `/home`: 105683103744 available bytes; 94.10% used; 114348574 free inodes.

server4 `/data`: 89265631232 available bytes; 98.77% used; 225255516 free inodes.

server4 `/tmp`: 105683103744 available bytes; 94.10% used; 114348574 free inodes.

server4 `/var/tmp`: 105683103744 available bytes; 94.10% used; 114348574 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
