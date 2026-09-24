# V2R cluster inventory

2026-09-24T08:11:30.449966+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | ['7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 324407169024 available bytes; 81.90% used; 112490652 free inodes.

server1 `/home`: 324407169024 available bytes; 81.90% used; 112490652 free inodes.

server1 `/tmp`: 324407169024 available bytes; 81.90% used; 112490652 free inodes.

server1 `/var/tmp`: 324407169024 available bytes; 81.90% used; 112490652 free inodes.

server1 `/mnt/raid5`: 496634347520 available bytes; 97.72% used; 337721370 free inodes.
| server2 | True | [] | [] | reference_compatible=False |

server2 `/`: 57818550272 available bytes; 96.77% used; 110431044 free inodes.

server2 `/home`: 57818550272 available bytes; 96.77% used; 110431044 free inodes.

server2 `/tmp`: 57818550272 available bytes; 96.77% used; 110431044 free inodes.

server2 `/var/tmp`: 57818550272 available bytes; 96.77% used; 110431044 free inodes.

server2 `/mnt/raid5`: 516718473216 available bytes; 96.43% used; 445180055 free inodes.
| server3 | True | [] | [] | reference_compatible=True |

server3 `/`: 85483134976 available bytes; 95.23% used; 114175164 free inodes.

server3 `/home`: 85483134976 available bytes; 95.23% used; 114175164 free inodes.

server3 `/data`: 155617730560 available bytes; 97.85% used; 225838170 free inodes.

server3 `/tmp`: 85483134976 available bytes; 95.23% used; 114175164 free inodes.

server3 `/var/tmp`: 85483134976 available bytes; 95.23% used; 114175164 free inodes.
| server4 | True | [] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 105778642944 available bytes; 94.10% used; 114349150 free inodes.

server4 `/home`: 105778642944 available bytes; 94.10% used; 114349150 free inodes.

server4 `/data`: 283895066624 available bytes; 96.08% used; 225365774 free inodes.

server4 `/tmp`: 105778642944 available bytes; 94.10% used; 114349150 free inodes.

server4 `/var/tmp`: 105778642944 available bytes; 94.10% used; 114349150 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
