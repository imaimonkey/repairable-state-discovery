# V2R cluster inventory

2026-09-25T14:55:21.294438+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | [] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 319145594880 available bytes; 82.20% used; 112476964 free inodes.

server1 `/home`: 319145594880 available bytes; 82.20% used; 112476964 free inodes.

server1 `/tmp`: 319145594880 available bytes; 82.20% used; 112476964 free inodes.

server1 `/var/tmp`: 319145594880 available bytes; 82.20% used; 112476964 free inodes.

server1 `/mnt/raid5`: 364017311744 available bytes; 98.33% used; 337546366 free inodes.
| server2 | True | ['3', '4', '5', '6'] | [] | reference_compatible=False |

server2 `/`: 14380068864 available bytes; 99.20% used; 110407658 free inodes.

server2 `/home`: 14380068864 available bytes; 99.20% used; 110407658 free inodes.

server2 `/tmp`: 14380068864 available bytes; 99.20% used; 110407658 free inodes.

server2 `/var/tmp`: 14380068864 available bytes; 99.20% used; 110407658 free inodes.

server2 `/mnt/raid5`: 320980443136 available bytes; 97.78% used; 445074157 free inodes.
| server3 | True | [] | [] | reference_compatible=True |

server3 `/`: 84345364480 available bytes; 95.29% used; 114153954 free inodes.

server3 `/home`: 84345364480 available bytes; 95.29% used; 114153954 free inodes.

server3 `/data`: 142190690304 available bytes; 98.03% used; 225808298 free inodes.

server3 `/tmp`: 84345364480 available bytes; 95.29% used; 114153954 free inodes.

server3 `/var/tmp`: 84345364480 available bytes; 95.29% used; 114153954 free inodes.
| server4 | True | ['2', '3'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 105645219840 available bytes; 94.10% used; 114349709 free inodes.

server4 `/home`: 105645219840 available bytes; 94.10% used; 114349709 free inodes.

server4 `/data`: 231418912768 available bytes; 96.80% used; 224945299 free inodes.

server4 `/tmp`: 105645219840 available bytes; 94.10% used; 114349709 free inodes.

server4 `/var/tmp`: 105645219840 available bytes; 94.10% used; 114349709 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
