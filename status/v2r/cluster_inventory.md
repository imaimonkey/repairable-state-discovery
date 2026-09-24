# V2R cluster inventory

2026-09-24T20:21:49.876001+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | [] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 323979046912 available bytes; 81.93% used; 112481432 free inodes.

server1 `/home`: 323979046912 available bytes; 81.93% used; 112481432 free inodes.

server1 `/tmp`: 323979046912 available bytes; 81.93% used; 112481432 free inodes.

server1 `/var/tmp`: 323979046912 available bytes; 81.93% used; 112481432 free inodes.

server1 `/mnt/raid5`: 415659286528 available bytes; 98.09% used; 337635414 free inodes.
| server2 | True | ['7'] | [] | reference_compatible=False |

server2 `/`: 30161428480 available bytes; 98.32% used; 110411376 free inodes.

server2 `/home`: 30161428480 available bytes; 98.32% used; 110411376 free inodes.

server2 `/tmp`: 30161428480 available bytes; 98.32% used; 110411376 free inodes.

server2 `/var/tmp`: 30161428480 available bytes; 98.32% used; 110411376 free inodes.

server2 `/mnt/raid5`: 492534906880 available bytes; 96.60% used; 445157067 free inodes.
| server3 | True | [] | [] | reference_compatible=True |

server3 `/`: 84392505344 available bytes; 95.29% used; 114156113 free inodes.

server3 `/home`: 84392505344 available bytes; 95.29% used; 114156113 free inodes.

server3 `/data`: 151614332928 available bytes; 97.90% used; 225804599 free inodes.

server3 `/tmp`: 84392505344 available bytes; 95.29% used; 114156113 free inodes.

server3 `/var/tmp`: 84392505344 available bytes; 95.29% used; 114156113 free inodes.
| server4 | True | [] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 105640701952 available bytes; 94.10% used; 114348392 free inodes.

server4 `/home`: 105640701952 available bytes; 94.10% used; 114348392 free inodes.

server4 `/data`: 85700669440 available bytes; 98.82% used; 225258345 free inodes.

server4 `/tmp`: 105640701952 available bytes; 94.10% used; 114348392 free inodes.

server4 `/var/tmp`: 105640701952 available bytes; 94.10% used; 114348392 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
