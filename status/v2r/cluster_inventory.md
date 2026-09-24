# V2R cluster inventory

2026-09-24T03:39:01.286951+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | ['7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 324741611520 available bytes; 81.88% used; 112493792 free inodes.

server1 `/home`: 324741611520 available bytes; 81.88% used; 112493792 free inodes.

server1 `/tmp`: 324741611520 available bytes; 81.88% used; 112493792 free inodes.

server1 `/var/tmp`: 324741611520 available bytes; 81.88% used; 112493792 free inodes.

server1 `/mnt/raid5`: 402133016576 available bytes; 98.16% used; 337724849 free inodes.
| server2 | True | [] | [] | reference_compatible=False |

server2 `/`: 40828846080 available bytes; 97.72% used; 110431038 free inodes.

server2 `/home`: 40828846080 available bytes; 97.72% used; 110431038 free inodes.

server2 `/tmp`: 40828846080 available bytes; 97.72% used; 110431038 free inodes.

server2 `/var/tmp`: 40828846080 available bytes; 97.72% used; 110431038 free inodes.

server2 `/mnt/raid5`: 526407385088 available bytes; 96.36% used; 445197533 free inodes.
| server3 | True | ['1'] | ['/tmp', '/var/tmp'] | reference_compatible=True |

server3 `/`: 291966316544 available bytes; 83.71% used; 114174467 free inodes.

server3 `/home`: 291966316544 available bytes; 83.71% used; 114174467 free inodes.

server3 `/data`: 36003905536 available bytes; 99.50% used; 225842823 free inodes.

server3 `/tmp`: 291966316544 available bytes; 83.71% used; 114174467 free inodes.

server3 `/var/tmp`: 291966316544 available bytes; 83.71% used; 114174467 free inodes.
| server4 | True | ['3', '7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 105793052672 available bytes; 94.10% used; 114349571 free inodes.

server4 `/home`: 105793052672 available bytes; 94.10% used; 114349571 free inodes.

server4 `/data`: 279289196544 available bytes; 96.14% used; 225384460 free inodes.

server4 `/tmp`: 105793052672 available bytes; 94.10% used; 114349571 free inodes.

server4 `/var/tmp`: 105793052672 available bytes; 94.10% used; 114349571 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
