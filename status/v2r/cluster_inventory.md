# V2R cluster inventory

2026-09-24T08:05:17.250900+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | ['7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 324412506112 available bytes; 81.90% used; 112490718 free inodes.

server1 `/home`: 324412506112 available bytes; 81.90% used; 112490718 free inodes.

server1 `/tmp`: 324412506112 available bytes; 81.90% used; 112490718 free inodes.

server1 `/var/tmp`: 324412506112 available bytes; 81.90% used; 112490718 free inodes.

server1 `/mnt/raid5`: 503434469376 available bytes; 97.69% used; 337721583 free inodes.
| server2 | True | [] | [] | reference_compatible=False |

server2 `/`: 57818128384 available bytes; 96.77% used; 110431060 free inodes.

server2 `/home`: 57818128384 available bytes; 96.77% used; 110431060 free inodes.

server2 `/tmp`: 57818128384 available bytes; 96.77% used; 110431060 free inodes.

server2 `/var/tmp`: 57818128384 available bytes; 96.77% used; 110431060 free inodes.

server2 `/mnt/raid5`: 517197922304 available bytes; 96.43% used; 445180517 free inodes.
| server3 | True | [] | [] | reference_compatible=True |

server3 `/`: 85483278336 available bytes; 95.23% used; 114175161 free inodes.

server3 `/home`: 85483278336 available bytes; 95.23% used; 114175161 free inodes.

server3 `/data`: 177766682624 available bytes; 97.54% used; 225837751 free inodes.

server3 `/tmp`: 85483278336 available bytes; 95.23% used; 114175161 free inodes.

server3 `/var/tmp`: 85483278336 available bytes; 95.23% used; 114175161 free inodes.
| server4 | True | [] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 105778966528 available bytes; 94.10% used; 114349156 free inodes.

server4 `/home`: 105778966528 available bytes; 94.10% used; 114349156 free inodes.

server4 `/data`: 284224069632 available bytes; 96.07% used; 225365933 free inodes.

server4 `/tmp`: 105778966528 available bytes; 94.10% used; 114349156 free inodes.

server4 `/var/tmp`: 105778966528 available bytes; 94.10% used; 114349156 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
