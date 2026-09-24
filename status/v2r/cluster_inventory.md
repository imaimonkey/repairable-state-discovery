# V2R cluster inventory

2026-09-24T13:01:30.765376+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | [] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 324039004160 available bytes; 81.92% used; 112481555 free inodes.

server1 `/home`: 324039004160 available bytes; 81.92% used; 112481555 free inodes.

server1 `/tmp`: 324039004160 available bytes; 81.92% used; 112481555 free inodes.

server1 `/var/tmp`: 324039004160 available bytes; 81.92% used; 112481555 free inodes.

server1 `/mnt/raid5`: 417084928000 available bytes; 98.09% used; 337678564 free inodes.
| server2 | True | ['7'] | [] | reference_compatible=False |

server2 `/`: 57558827008 available bytes; 96.79% used; 110429019 free inodes.

server2 `/home`: 57558827008 available bytes; 96.79% used; 110429019 free inodes.

server2 `/tmp`: 57558827008 available bytes; 96.79% used; 110429019 free inodes.

server2 `/var/tmp`: 57558827008 available bytes; 96.79% used; 110429019 free inodes.

server2 `/mnt/raid5`: 506987237376 available bytes; 96.50% used; 445171056 free inodes.
| server3 | True | [] | [] | reference_compatible=True |

server3 `/`: 85215682560 available bytes; 95.24% used; 114168919 free inodes.

server3 `/home`: 85215682560 available bytes; 95.24% used; 114168919 free inodes.

server3 `/data`: 163012132864 available bytes; 97.75% used; 225813722 free inodes.

server3 `/tmp`: 85215682560 available bytes; 95.24% used; 114168919 free inodes.

server3 `/var/tmp`: 85215682560 available bytes; 95.24% used; 114168919 free inodes.
| server4 | True | [] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 105779326976 available bytes; 94.10% used; 114348765 free inodes.

server4 `/home`: 105779326976 available bytes; 94.10% used; 114348765 free inodes.

server4 `/data`: 90023759872 available bytes; 98.76% used; 225257181 free inodes.

server4 `/tmp`: 105779326976 available bytes; 94.10% used; 114348765 free inodes.

server4 `/var/tmp`: 105779326976 available bytes; 94.10% used; 114348765 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
