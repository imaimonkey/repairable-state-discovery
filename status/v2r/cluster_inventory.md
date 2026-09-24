# V2R cluster inventory

2026-09-24T14:25:36.293038+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | [] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 324056932352 available bytes; 81.92% used; 112481456 free inodes.

server1 `/home`: 324056932352 available bytes; 81.92% used; 112481456 free inodes.

server1 `/tmp`: 324056932352 available bytes; 81.92% used; 112481456 free inodes.

server1 `/var/tmp`: 324056932352 available bytes; 81.92% used; 112481456 free inodes.

server1 `/mnt/raid5`: 416909799424 available bytes; 98.09% used; 337668736 free inodes.
| server2 | True | ['7'] | [] | reference_compatible=False |

server2 `/`: 57466994688 available bytes; 96.79% used; 110428165 free inodes.

server2 `/home`: 57466994688 available bytes; 96.79% used; 110428165 free inodes.

server2 `/tmp`: 57466994688 available bytes; 96.79% used; 110428165 free inodes.

server2 `/var/tmp`: 57466994688 available bytes; 96.79% used; 110428165 free inodes.

server2 `/mnt/raid5`: 504091553792 available bytes; 96.52% used; 445168199 free inodes.
| server3 | True | ['0'] | [] | reference_compatible=True |

server3 `/`: 84688400384 available bytes; 95.27% used; 114164937 free inodes.

server3 `/home`: 84688400384 available bytes; 95.27% used; 114164937 free inodes.

server3 `/data`: 160940273664 available bytes; 97.78% used; 225808693 free inodes.

server3 `/tmp`: 84688400384 available bytes; 95.27% used; 114164937 free inodes.

server3 `/var/tmp`: 84688400384 available bytes; 95.27% used; 114164937 free inodes.
| server4 | True | [] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 105759170560 available bytes; 94.10% used; 114348699 free inodes.

server4 `/home`: 105759170560 available bytes; 94.10% used; 114348699 free inodes.

server4 `/data`: 69350875136 available bytes; 99.04% used; 225257063 free inodes.

server4 `/tmp`: 105759170560 available bytes; 94.10% used; 114348699 free inodes.

server4 `/var/tmp`: 105759170560 available bytes; 94.10% used; 114348699 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
