# V2R cluster inventory

2026-09-24T12:22:14.729822+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | [] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 324059377664 available bytes; 81.92% used; 112481570 free inodes.

server1 `/home`: 324059377664 available bytes; 81.92% used; 112481570 free inodes.

server1 `/tmp`: 324059377664 available bytes; 81.92% used; 112481570 free inodes.

server1 `/var/tmp`: 324059377664 available bytes; 81.92% used; 112481570 free inodes.

server1 `/mnt/raid5`: 405207670784 available bytes; 98.14% used; 337683301 free inodes.
| server2 | True | ['7'] | [] | reference_compatible=False |

server2 `/`: 57603117056 available bytes; 96.79% used; 110429484 free inodes.

server2 `/home`: 57603117056 available bytes; 96.79% used; 110429484 free inodes.

server2 `/tmp`: 57603117056 available bytes; 96.79% used; 110429484 free inodes.

server2 `/var/tmp`: 57603117056 available bytes; 96.79% used; 110429484 free inodes.

server2 `/mnt/raid5`: 508738293760 available bytes; 96.48% used; 445172003 free inodes.
| server3 | True | [] | [] | reference_compatible=True |

server3 `/`: 85308612608 available bytes; 95.24% used; 114172733 free inodes.

server3 `/home`: 85308612608 available bytes; 95.24% used; 114172733 free inodes.

server3 `/data`: 163425517568 available bytes; 97.74% used; 225814906 free inodes.

server3 `/tmp`: 85308612608 available bytes; 95.24% used; 114172733 free inodes.

server3 `/var/tmp`: 85308612608 available bytes; 95.24% used; 114172733 free inodes.
| server4 | True | [] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 105780973568 available bytes; 94.10% used; 114348801 free inodes.

server4 `/home`: 105780973568 available bytes; 94.10% used; 114348801 free inodes.

server4 `/data`: 90076192768 available bytes; 98.76% used; 225257308 free inodes.

server4 `/tmp`: 105780973568 available bytes; 94.10% used; 114348801 free inodes.

server4 `/var/tmp`: 105780973568 available bytes; 94.10% used; 114348801 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
