# V2R cluster inventory

2026-09-24T06:14:55.071225+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | ['7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 324517658624 available bytes; 81.90% used; 112491804 free inodes.

server1 `/home`: 324517658624 available bytes; 81.90% used; 112491804 free inodes.

server1 `/tmp`: 324517658624 available bytes; 81.90% used; 112491804 free inodes.

server1 `/var/tmp`: 324517658624 available bytes; 81.90% used; 112491804 free inodes.

server1 `/mnt/raid5`: 517597470720 available bytes; 97.63% used; 337723776 free inodes.
| server2 | True | [] | [] | reference_compatible=False |

server2 `/`: 57894703104 available bytes; 96.77% used; 110431258 free inodes.

server2 `/home`: 57894703104 available bytes; 96.77% used; 110431258 free inodes.

server2 `/tmp`: 57894703104 available bytes; 96.77% used; 110431258 free inodes.

server2 `/var/tmp`: 57894703104 available bytes; 96.77% used; 110431258 free inodes.

server2 `/mnt/raid5`: 520710135808 available bytes; 96.40% used; 445192507 free inodes.
| server3 | True | [] | ['/tmp', '/var/tmp'] | reference_compatible=True |

server3 `/`: 126802534400 available bytes; 92.92% used; 114174277 free inodes.

server3 `/home`: 126802534400 available bytes; 92.92% used; 114174277 free inodes.

server3 `/data`: 161276936192 available bytes; 97.77% used; 225836048 free inodes.

server3 `/tmp`: 126802534400 available bytes; 92.92% used; 114174277 free inodes.

server3 `/var/tmp`: 126802534400 available bytes; 92.92% used; 114174277 free inodes.
| server4 | True | ['1'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 105806413824 available bytes; 94.10% used; 114349319 free inodes.

server4 `/home`: 105806413824 available bytes; 94.10% used; 114349319 free inodes.

server4 `/data`: 339172642816 available bytes; 95.31% used; 225373833 free inodes.

server4 `/tmp`: 105806413824 available bytes; 94.10% used; 114349319 free inodes.

server4 `/var/tmp`: 105806413824 available bytes; 94.10% used; 114349319 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
