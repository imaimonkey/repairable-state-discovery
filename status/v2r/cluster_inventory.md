# V2R cluster inventory

2026-09-24T17:08:57.454340+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | ['7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 324016193536 available bytes; 81.92% used; 112481440 free inodes.

server1 `/home`: 324016193536 available bytes; 81.92% used; 112481440 free inodes.

server1 `/tmp`: 324016193536 available bytes; 81.92% used; 112481440 free inodes.

server1 `/var/tmp`: 324016193536 available bytes; 81.92% used; 112481440 free inodes.

server1 `/mnt/raid5`: 416495779840 available bytes; 98.09% used; 337648844 free inodes.
| server2 | True | ['7'] | [] | reference_compatible=False |

server2 `/`: 57055014912 available bytes; 96.82% used; 110417920 free inodes.

server2 `/home`: 57055014912 available bytes; 96.82% used; 110417920 free inodes.

server2 `/tmp`: 57055014912 available bytes; 96.82% used; 110417920 free inodes.

server2 `/var/tmp`: 57055014912 available bytes; 96.82% used; 110417920 free inodes.

server2 `/mnt/raid5`: 499721699328 available bytes; 96.55% used; 445163006 free inodes.
| server3 | True | [] | [] | reference_compatible=True |

server3 `/`: 84409749504 available bytes; 95.29% used; 114156152 free inodes.

server3 `/home`: 84409749504 available bytes; 95.29% used; 114156152 free inodes.

server3 `/data`: 159078973440 available bytes; 97.80% used; 225787241 free inodes.

server3 `/tmp`: 84409749504 available bytes; 95.29% used; 114156152 free inodes.

server3 `/var/tmp`: 84409749504 available bytes; 95.29% used; 114156152 free inodes.
| server4 | True | [] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 105682165760 available bytes; 94.10% used; 114348569 free inodes.

server4 `/home`: 105682165760 available bytes; 94.10% used; 114348569 free inodes.

server4 `/data`: 89163538432 available bytes; 98.77% used; 225254659 free inodes.

server4 `/tmp`: 105682165760 available bytes; 94.10% used; 114348569 free inodes.

server4 `/var/tmp`: 105682165760 available bytes; 94.10% used; 114348569 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
