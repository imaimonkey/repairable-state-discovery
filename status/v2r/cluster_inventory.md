# V2R cluster inventory

2026-09-24T04:23:08.484364+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | ['7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 324707663872 available bytes; 81.89% used; 112493302 free inodes.

server1 `/home`: 324707663872 available bytes; 81.89% used; 112493302 free inodes.

server1 `/tmp`: 324707663872 available bytes; 81.89% used; 112493302 free inodes.

server1 `/var/tmp`: 324707663872 available bytes; 81.89% used; 112493302 free inodes.

server1 `/mnt/raid5`: 440826327040 available bytes; 97.98% used; 337724702 free inodes.
| server2 | True | ['6'] | [] | reference_compatible=False |

server2 `/`: 40785485824 available bytes; 97.72% used; 110430658 free inodes.

server2 `/home`: 40785485824 available bytes; 97.72% used; 110430658 free inodes.

server2 `/tmp`: 40785485824 available bytes; 97.72% used; 110430658 free inodes.

server2 `/var/tmp`: 40785485824 available bytes; 97.72% used; 110430658 free inodes.

server2 `/mnt/raid5`: 525585743872 available bytes; 96.37% used; 445196041 free inodes.
| server3 | True | ['1'] | ['/tmp', '/var/tmp'] | reference_compatible=True |

server3 `/`: 292027023360 available bytes; 83.70% used; 114176946 free inodes.

server3 `/home`: 292027023360 available bytes; 83.70% used; 114176946 free inodes.

server3 `/data`: 31691272192 available bytes; 99.56% used; 225841536 free inodes.

server3 `/tmp`: 292027023360 available bytes; 83.70% used; 114176946 free inodes.

server3 `/var/tmp`: 292027023360 available bytes; 83.70% used; 114176946 free inodes.
| server4 | True | ['7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 105844768768 available bytes; 94.09% used; 114349421 free inodes.

server4 `/home`: 105844768768 available bytes; 94.09% used; 114349421 free inodes.

server4 `/data`: 256718327808 available bytes; 96.45% used; 225381784 free inodes.

server4 `/tmp`: 105844768768 available bytes; 94.09% used; 114349421 free inodes.

server4 `/var/tmp`: 105844768768 available bytes; 94.09% used; 114349421 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
