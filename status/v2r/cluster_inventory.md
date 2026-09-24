# V2R cluster inventory

2026-09-24T04:19:59.273809+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | ['7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 324707852288 available bytes; 81.89% used; 112493330 free inodes.

server1 `/home`: 324707852288 available bytes; 81.89% used; 112493330 free inodes.

server1 `/tmp`: 324707852288 available bytes; 81.89% used; 112493330 free inodes.

server1 `/var/tmp`: 324707852288 available bytes; 81.89% used; 112493330 free inodes.

server1 `/mnt/raid5`: 435984998400 available bytes; 98.00% used; 337724718 free inodes.
| server2 | True | ['6'] | [] | reference_compatible=False |

server2 `/`: 40794497024 available bytes; 97.72% used; 110430728 free inodes.

server2 `/home`: 40794497024 available bytes; 97.72% used; 110430728 free inodes.

server2 `/tmp`: 40794497024 available bytes; 97.72% used; 110430728 free inodes.

server2 `/var/tmp`: 40794497024 available bytes; 97.72% used; 110430728 free inodes.

server2 `/mnt/raid5`: 525677817856 available bytes; 96.37% used; 445196134 free inodes.
| server3 | True | ['1'] | ['/tmp', '/var/tmp'] | reference_compatible=True |

server3 `/`: 292026454016 available bytes; 83.70% used; 114176834 free inodes.

server3 `/home`: 292026454016 available bytes; 83.70% used; 114176834 free inodes.

server3 `/data`: 31694909440 available bytes; 99.56% used; 225841621 free inodes.

server3 `/tmp`: 292026454016 available bytes; 83.70% used; 114176834 free inodes.

server3 `/var/tmp`: 292026454016 available bytes; 83.70% used; 114176834 free inodes.
| server4 | True | ['7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 105845538816 available bytes; 94.09% used; 114349452 free inodes.

server4 `/home`: 105845538816 available bytes; 94.09% used; 114349452 free inodes.

server4 `/data`: 256705208320 available bytes; 96.45% used; 225381780 free inodes.

server4 `/tmp`: 105845538816 available bytes; 94.09% used; 114349452 free inodes.

server4 `/var/tmp`: 105845538816 available bytes; 94.09% used; 114349452 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
