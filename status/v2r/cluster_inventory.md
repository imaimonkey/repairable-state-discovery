# V2R cluster inventory

2026-09-24T16:39:25.005754+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | ['7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 324026855424 available bytes; 81.92% used; 112481458 free inodes.

server1 `/home`: 324026855424 available bytes; 81.92% used; 112481458 free inodes.

server1 `/tmp`: 324026855424 available bytes; 81.92% used; 112481458 free inodes.

server1 `/var/tmp`: 324026855424 available bytes; 81.92% used; 112481458 free inodes.

server1 `/mnt/raid5`: 416554377216 available bytes; 98.09% used; 337652289 free inodes.
| server2 | True | ['7'] | [] | reference_compatible=False |

server2 `/`: 57313128448 available bytes; 96.80% used; 110426791 free inodes.

server2 `/home`: 57313128448 available bytes; 96.80% used; 110426791 free inodes.

server2 `/tmp`: 57313128448 available bytes; 96.80% used; 110426791 free inodes.

server2 `/var/tmp`: 57313128448 available bytes; 96.80% used; 110426791 free inodes.

server2 `/mnt/raid5`: 500649283584 available bytes; 96.54% used; 445164131 free inodes.
| server3 | True | [] | [] | reference_compatible=True |

server3 `/`: 84152991744 available bytes; 95.30% used; 114144747 free inodes.

server3 `/home`: 84152999936 available bytes; 95.30% used; 114144749 free inodes.

server3 `/data`: 159283150848 available bytes; 97.80% used; 225787497 free inodes.

server3 `/tmp`: 84153008128 available bytes; 95.30% used; 114144752 free inodes.

server3 `/var/tmp`: 84153008128 available bytes; 95.30% used; 114144752 free inodes.
| server4 | True | [] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 105683193856 available bytes; 94.10% used; 114348574 free inodes.

server4 `/home`: 105683193856 available bytes; 94.10% used; 114348574 free inodes.

server4 `/data`: 89267208192 available bytes; 98.77% used; 225255602 free inodes.

server4 `/tmp`: 105683193856 available bytes; 94.10% used; 114348574 free inodes.

server4 `/var/tmp`: 105683193856 available bytes; 94.10% used; 114348574 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
