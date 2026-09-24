# V2R cluster inventory

2026-09-24T16:40:57.599084+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | ['7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 324026380288 available bytes; 81.92% used; 112481465 free inodes.

server1 `/home`: 324026380288 available bytes; 81.92% used; 112481465 free inodes.

server1 `/tmp`: 324026380288 available bytes; 81.92% used; 112481465 free inodes.

server1 `/var/tmp`: 324026380288 available bytes; 81.92% used; 112481465 free inodes.

server1 `/mnt/raid5`: 416551518208 available bytes; 98.09% used; 337652116 free inodes.
| server2 | True | ['7'] | [] | reference_compatible=False |

server2 `/`: 57216692224 available bytes; 96.81% used; 110424869 free inodes.

server2 `/home`: 57216692224 available bytes; 96.81% used; 110424869 free inodes.

server2 `/tmp`: 57216692224 available bytes; 96.81% used; 110424869 free inodes.

server2 `/var/tmp`: 57216692224 available bytes; 96.81% used; 110424869 free inodes.

server2 `/mnt/raid5`: 500600422400 available bytes; 96.54% used; 445163994 free inodes.
| server3 | True | [] | [] | reference_compatible=True |

server3 `/`: 83942858752 available bytes; 95.32% used; 114135622 free inodes.

server3 `/home`: 83942858752 available bytes; 95.32% used; 114135622 free inodes.

server3 `/data`: 159285121024 available bytes; 97.80% used; 225787754 free inodes.

server3 `/tmp`: 83942858752 available bytes; 95.32% used; 114135622 free inodes.

server3 `/var/tmp`: 83942858752 available bytes; 95.32% used; 114135622 free inodes.
| server4 | True | [] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 105683140608 available bytes; 94.10% used; 114348574 free inodes.

server4 `/home`: 105683140608 available bytes; 94.10% used; 114348574 free inodes.

server4 `/data`: 89265082368 available bytes; 98.77% used; 225255518 free inodes.

server4 `/tmp`: 105683140608 available bytes; 94.10% used; 114348574 free inodes.

server4 `/var/tmp`: 105683140608 available bytes; 94.10% used; 114348574 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
