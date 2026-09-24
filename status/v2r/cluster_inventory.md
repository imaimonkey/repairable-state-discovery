# V2R cluster inventory

2026-09-24T03:23:12.218339+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | ['7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 325359284224 available bytes; 81.85% used; 112498234 free inodes.

server1 `/home`: 325359284224 available bytes; 81.85% used; 112498234 free inodes.

server1 `/tmp`: 325359284224 available bytes; 81.85% used; 112498234 free inodes.

server1 `/var/tmp`: 325359284224 available bytes; 81.85% used; 112498234 free inodes.

server1 `/mnt/raid5`: 427272269824 available bytes; 98.04% used; 337732672 free inodes.
| server2 | True | [] | [] | reference_compatible=False |

server2 `/`: 40844378112 available bytes; 97.72% used; 110431148 free inodes.

server2 `/home`: 40844378112 available bytes; 97.72% used; 110431148 free inodes.

server2 `/tmp`: 40844378112 available bytes; 97.72% used; 110431148 free inodes.

server2 `/var/tmp`: 40844378112 available bytes; 97.72% used; 110431148 free inodes.

server2 `/mnt/raid5`: 526825504768 available bytes; 96.36% used; 445197613 free inodes.
| server3 | True | [] | ['/tmp', '/var/tmp'] | reference_compatible=True |

server3 `/`: 292387381248 available bytes; 83.68% used; 114201034 free inodes.

server3 `/home`: 292387381248 available bytes; 83.68% used; 114201034 free inodes.

server3 `/data`: 39589117952 available bytes; 99.45% used; 225844036 free inodes.

server3 `/tmp`: 292387381248 available bytes; 83.68% used; 114201034 free inodes.

server3 `/var/tmp`: 292387381248 available bytes; 83.68% used; 114201034 free inodes.
| server4 | True | ['3', '7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 105987379200 available bytes; 94.09% used; 114349611 free inodes.

server4 `/home`: 105987379200 available bytes; 94.09% used; 114349611 free inodes.

server4 `/data`: 286969663488 available bytes; 96.03% used; 225386342 free inodes.

server4 `/tmp`: 105987379200 available bytes; 94.09% used; 114349611 free inodes.

server4 `/var/tmp`: 105987379200 available bytes; 94.09% used; 114349611 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
