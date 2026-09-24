# V2R cluster inventory

2026-09-24T14:49:03.498618+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | [] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 324050231296 available bytes; 81.92% used; 112481473 free inodes.

server1 `/home`: 324050231296 available bytes; 81.92% used; 112481473 free inodes.

server1 `/tmp`: 324050231296 available bytes; 81.92% used; 112481473 free inodes.

server1 `/var/tmp`: 324050231296 available bytes; 81.92% used; 112481473 free inodes.

server1 `/mnt/raid5`: 416852549632 available bytes; 98.09% used; 337666002 free inodes.
| server2 | True | ['7'] | [] | reference_compatible=False |

server2 `/`: 57437827072 available bytes; 96.80% used; 110427917 free inodes.

server2 `/home`: 57437827072 available bytes; 96.80% used; 110427917 free inodes.

server2 `/tmp`: 57437827072 available bytes; 96.80% used; 110427917 free inodes.

server2 `/var/tmp`: 57437827072 available bytes; 96.80% used; 110427917 free inodes.

server2 `/mnt/raid5`: 503900278784 available bytes; 96.52% used; 445167375 free inodes.
| server3 | True | ['0'] | [] | reference_compatible=True |

server3 `/`: 84874088448 available bytes; 95.26% used; 114184595 free inodes.

server3 `/home`: 84874088448 available bytes; 95.26% used; 114184595 free inodes.

server3 `/data`: 160685400064 available bytes; 97.78% used; 225807758 free inodes.

server3 `/tmp`: 84874088448 available bytes; 95.26% used; 114184595 free inodes.

server3 `/var/tmp`: 84874088448 available bytes; 95.26% used; 114184595 free inodes.
| server4 | True | [] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 105749839872 available bytes; 94.10% used; 114348683 free inodes.

server4 `/home`: 105749839872 available bytes; 94.10% used; 114348683 free inodes.

server4 `/data`: 69171994624 available bytes; 99.04% used; 225256991 free inodes.

server4 `/tmp`: 105749839872 available bytes; 94.10% used; 114348683 free inodes.

server4 `/var/tmp`: 105749839872 available bytes; 94.10% used; 114348683 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
