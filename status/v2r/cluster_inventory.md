# V2R cluster inventory

2026-09-24T04:21:32.360803+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | ['7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 324709404672 available bytes; 81.89% used; 112493317 free inodes.

server1 `/home`: 324709404672 available bytes; 81.89% used; 112493317 free inodes.

server1 `/tmp`: 324709404672 available bytes; 81.89% used; 112493317 free inodes.

server1 `/var/tmp`: 324709404672 available bytes; 81.89% used; 112493317 free inodes.

server1 `/mnt/raid5`: 435983937536 available bytes; 98.00% used; 337724708 free inodes.
| server2 | True | ['6'] | [] | reference_compatible=False |

server2 `/`: 40787898368 available bytes; 97.72% used; 110430690 free inodes.

server2 `/home`: 40787898368 available bytes; 97.72% used; 110430690 free inodes.

server2 `/tmp`: 40787898368 available bytes; 97.72% used; 110430690 free inodes.

server2 `/var/tmp`: 40787898368 available bytes; 97.72% used; 110430690 free inodes.

server2 `/mnt/raid5`: 525633032192 available bytes; 96.37% used; 445196214 free inodes.
| server3 | True | ['1'] | ['/tmp', '/var/tmp'] | reference_compatible=True |

server3 `/`: 291690827776 available bytes; 83.72% used; 114162409 free inodes.

server3 `/home`: 291690827776 available bytes; 83.72% used; 114162409 free inodes.

server3 `/data`: 31692619776 available bytes; 99.56% used; 225841580 free inodes.

server3 `/tmp`: 291690827776 available bytes; 83.72% used; 114162409 free inodes.

server3 `/var/tmp`: 291690827776 available bytes; 83.72% used; 114162409 free inodes.
| server4 | True | ['7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 105845469184 available bytes; 94.09% used; 114349452 free inodes.

server4 `/home`: 105845469184 available bytes; 94.09% used; 114349452 free inodes.

server4 `/data`: 256714641408 available bytes; 96.45% used; 225381784 free inodes.

server4 `/tmp`: 105845469184 available bytes; 94.09% used; 114349452 free inodes.

server4 `/var/tmp`: 105845469184 available bytes; 94.09% used; 114349452 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
