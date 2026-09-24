# V2R cluster inventory

2026-09-24T14:02:18.512446+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | [] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 324063588352 available bytes; 81.92% used; 112481656 free inodes.

server1 `/home`: 324063588352 available bytes; 81.92% used; 112481656 free inodes.

server1 `/tmp`: 324063588352 available bytes; 81.92% used; 112481656 free inodes.

server1 `/var/tmp`: 324063588352 available bytes; 81.92% used; 112481656 free inodes.

server1 `/mnt/raid5`: 416961167360 available bytes; 98.09% used; 337671459 free inodes.
| server2 | True | ['7'] | [] | reference_compatible=False |

server2 `/`: 57488744448 available bytes; 96.79% used; 110428391 free inodes.

server2 `/home`: 57488744448 available bytes; 96.79% used; 110428391 free inodes.

server2 `/tmp`: 57488744448 available bytes; 96.79% used; 110428391 free inodes.

server2 `/var/tmp`: 57488744448 available bytes; 96.79% used; 110428391 free inodes.

server2 `/mnt/raid5`: 505620271104 available bytes; 96.51% used; 445168558 free inodes.
| server3 | True | [] | [] | reference_compatible=True |

server3 `/`: 85089550336 available bytes; 95.25% used; 114190416 free inodes.

server3 `/home`: 85089550336 available bytes; 95.25% used; 114190416 free inodes.

server3 `/data`: 161024835584 available bytes; 97.77% used; 225802546 free inodes.

server3 `/tmp`: 85089550336 available bytes; 95.25% used; 114190416 free inodes.

server3 `/var/tmp`: 85089550336 available bytes; 95.25% used; 114190416 free inodes.
| server4 | True | [] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 105760030720 available bytes; 94.10% used; 114348712 free inodes.

server4 `/home`: 105760030720 available bytes; 94.10% used; 114348712 free inodes.

server4 `/data`: 69381451776 available bytes; 99.04% used; 225257144 free inodes.

server4 `/tmp`: 105760030720 available bytes; 94.10% used; 114348712 free inodes.

server4 `/var/tmp`: 105760030720 available bytes; 94.10% used; 114348712 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
