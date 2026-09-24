# V2R cluster inventory

2026-09-24T14:27:08.982208+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | [] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 324048494592 available bytes; 81.92% used; 112481456 free inodes.

server1 `/home`: 324048494592 available bytes; 81.92% used; 112481456 free inodes.

server1 `/tmp`: 324048494592 available bytes; 81.92% used; 112481456 free inodes.

server1 `/var/tmp`: 324048494592 available bytes; 81.92% used; 112481456 free inodes.

server1 `/mnt/raid5`: 416909004800 available bytes; 98.09% used; 337668558 free inodes.
| server2 | True | ['7'] | [] | reference_compatible=False |

server2 `/`: 57465430016 available bytes; 96.79% used; 110428147 free inodes.

server2 `/home`: 57465430016 available bytes; 96.79% used; 110428147 free inodes.

server2 `/tmp`: 57465430016 available bytes; 96.79% used; 110428147 free inodes.

server2 `/var/tmp`: 57465430016 available bytes; 96.79% used; 110428147 free inodes.

server2 `/mnt/raid5`: 504589570048 available bytes; 96.51% used; 445168042 free inodes.
| server3 | True | ['0'] | [] | reference_compatible=True |

server3 `/`: 84679307264 available bytes; 95.27% used; 114164935 free inodes.

server3 `/home`: 84679307264 available bytes; 95.27% used; 114164935 free inodes.

server3 `/data`: 160925249536 available bytes; 97.78% used; 225808607 free inodes.

server3 `/tmp`: 84679307264 available bytes; 95.27% used; 114164935 free inodes.

server3 `/var/tmp`: 84679307264 available bytes; 95.27% used; 114164935 free inodes.
| server4 | True | [] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 105759084544 available bytes; 94.10% used; 114348697 free inodes.

server4 `/home`: 105759084544 available bytes; 94.10% used; 114348697 free inodes.

server4 `/data`: 69351026688 available bytes; 99.04% used; 225257054 free inodes.

server4 `/tmp`: 105759084544 available bytes; 94.10% used; 114348697 free inodes.

server4 `/var/tmp`: 105759084544 available bytes; 94.10% used; 114348697 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
