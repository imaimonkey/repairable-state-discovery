# V2R cluster inventory

2026-09-24T02:28:19.341599+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | ['7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 325387669504 available bytes; 81.85% used; 112498897 free inodes.

server1 `/home`: 325387669504 available bytes; 81.85% used; 112498897 free inodes.

server1 `/tmp`: 325387669504 available bytes; 81.85% used; 112498897 free inodes.

server1 `/var/tmp`: 325387669504 available bytes; 81.85% used; 112498897 free inodes.

server1 `/mnt/raid5`: 654987407360 available bytes; 97.00% used; 337733245 free inodes.
| server2 | True | [] | [] | reference_compatible=False |

server2 `/`: 40891355136 available bytes; 97.72% used; 110431552 free inodes.

server2 `/home`: 40891355136 available bytes; 97.72% used; 110431552 free inodes.

server2 `/tmp`: 40891355136 available bytes; 97.72% used; 110431552 free inodes.

server2 `/var/tmp`: 40891355136 available bytes; 97.72% used; 110431552 free inodes.

server2 `/mnt/raid5`: 529078800384 available bytes; 96.34% used; 445199613 free inodes.
| server3 | True | [] | ['/tmp', '/var/tmp'] | reference_compatible=True |

server3 `/`: 291857297408 available bytes; 83.71% used; 114163146 free inodes.

server3 `/home`: 291857297408 available bytes; 83.71% used; 114163146 free inodes.

server3 `/data`: 39751430144 available bytes; 99.45% used; 225846426 free inodes.

server3 `/tmp`: 291857297408 available bytes; 83.71% used; 114163146 free inodes.

server3 `/var/tmp`: 291857297408 available bytes; 83.71% used; 114163146 free inodes.
| server4 | True | ['3', '7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 106003795968 available bytes; 94.08% used; 114349842 free inodes.

server4 `/home`: 106003795968 available bytes; 94.08% used; 114349842 free inodes.

server4 `/data`: 289735921664 available bytes; 96.00% used; 225387541 free inodes.

server4 `/tmp`: 106003795968 available bytes; 94.08% used; 114349842 free inodes.

server4 `/var/tmp`: 106003795968 available bytes; 94.08% used; 114349842 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
