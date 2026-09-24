# V2R cluster inventory

2026-09-24T06:02:29.613046+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | ['7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 324529664000 available bytes; 81.90% used; 112491932 free inodes.

server1 `/home`: 324529664000 available bytes; 81.90% used; 112491932 free inodes.

server1 `/tmp`: 324529664000 available bytes; 81.90% used; 112491932 free inodes.

server1 `/var/tmp`: 324529664000 available bytes; 81.90% used; 112491932 free inodes.

server1 `/mnt/raid5`: 517607186432 available bytes; 97.63% used; 337723833 free inodes.
| server2 | True | [] | [] | reference_compatible=False |

server2 `/`: 57904648192 available bytes; 96.77% used; 110431292 free inodes.

server2 `/home`: 57904648192 available bytes; 96.77% used; 110431292 free inodes.

server2 `/tmp`: 57904648192 available bytes; 96.77% used; 110431292 free inodes.

server2 `/var/tmp`: 57904648192 available bytes; 96.77% used; 110431292 free inodes.

server2 `/mnt/raid5`: 521086889984 available bytes; 96.40% used; 445192758 free inodes.
| server3 | True | [] | ['/tmp', '/var/tmp'] | reference_compatible=True |

server3 `/`: 127214436352 available bytes; 92.90% used; 114200040 free inodes.

server3 `/home`: 127214436352 available bytes; 92.90% used; 114200040 free inodes.

server3 `/data`: 185843036160 available bytes; 97.43% used; 225838438 free inodes.

server3 `/tmp`: 127214436352 available bytes; 92.90% used; 114200040 free inodes.

server3 `/var/tmp`: 127214436352 available bytes; 92.90% used; 114200040 free inodes.
| server4 | True | ['1'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 105815298048 available bytes; 94.10% used; 114349323 free inodes.

server4 `/home`: 105815298048 available bytes; 94.10% used; 114349323 free inodes.

server4 `/data`: 339823706112 available bytes; 95.30% used; 225374703 free inodes.

server4 `/tmp`: 105815298048 available bytes; 94.10% used; 114349323 free inodes.

server4 `/var/tmp`: 105815298048 available bytes; 94.10% used; 114349323 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
