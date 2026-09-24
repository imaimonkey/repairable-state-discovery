# V2R cluster inventory

2026-09-24T14:06:59.907480+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | [] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 324061249536 available bytes; 81.92% used; 112481656 free inodes.

server1 `/home`: 324061249536 available bytes; 81.92% used; 112481656 free inodes.

server1 `/tmp`: 324061249536 available bytes; 81.92% used; 112481656 free inodes.

server1 `/var/tmp`: 324061249536 available bytes; 81.92% used; 112481656 free inodes.

server1 `/mnt/raid5`: 416951988224 available bytes; 98.09% used; 337670909 free inodes.
| server2 | True | ['7'] | [] | reference_compatible=False |

server2 `/`: 57483182080 available bytes; 96.79% used; 110428343 free inodes.

server2 `/home`: 57483182080 available bytes; 96.79% used; 110428343 free inodes.

server2 `/tmp`: 57483182080 available bytes; 96.79% used; 110428343 free inodes.

server2 `/var/tmp`: 57483182080 available bytes; 96.79% used; 110428343 free inodes.

server2 `/mnt/raid5`: 505492090880 available bytes; 96.51% used; 445168933 free inodes.
| server3 | True | [] | [] | reference_compatible=True |

server3 `/`: 85084979200 available bytes; 95.25% used; 114190235 free inodes.

server3 `/home`: 85084979200 available bytes; 95.25% used; 114190235 free inodes.

server3 `/data`: 160993353728 available bytes; 97.78% used; 225802462 free inodes.

server3 `/tmp`: 85084979200 available bytes; 95.25% used; 114190235 free inodes.

server3 `/var/tmp`: 85084979200 available bytes; 95.25% used; 114190235 free inodes.
| server4 | True | [] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 105759866880 available bytes; 94.10% used; 114348708 free inodes.

server4 `/home`: 105759866880 available bytes; 94.10% used; 114348708 free inodes.

server4 `/data`: 69380747264 available bytes; 99.04% used; 225257111 free inodes.

server4 `/tmp`: 105759866880 available bytes; 94.10% used; 114348708 free inodes.

server4 `/var/tmp`: 105759866880 available bytes; 94.10% used; 114348708 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
