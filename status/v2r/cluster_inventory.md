# V2R cluster inventory

2026-09-24T08:25:29.643153+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | [] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 324404596736 available bytes; 81.90% used; 112490496 free inodes.

server1 `/home`: 324404596736 available bytes; 81.90% used; 112490496 free inodes.

server1 `/tmp`: 324404596736 available bytes; 81.90% used; 112490496 free inodes.

server1 `/var/tmp`: 324404596736 available bytes; 81.90% used; 112490496 free inodes.

server1 `/mnt/raid5`: 510195511296 available bytes; 97.66% used; 337721252 free inodes.
| server2 | True | [] | [] | reference_compatible=False |

server2 `/`: 57809973248 available bytes; 96.77% used; 110431012 free inodes.

server2 `/home`: 57809973248 available bytes; 96.77% used; 110431012 free inodes.

server2 `/tmp`: 57809973248 available bytes; 96.77% used; 110431012 free inodes.

server2 `/var/tmp`: 57809973248 available bytes; 96.77% used; 110431012 free inodes.

server2 `/mnt/raid5`: 516299505664 available bytes; 96.43% used; 445179762 free inodes.
| server3 | True | [] | [] | reference_compatible=True |

server3 `/`: 85483098112 available bytes; 95.23% used; 114174944 free inodes.

server3 `/home`: 85483098112 available bytes; 95.23% used; 114174944 free inodes.

server3 `/data`: 175107776512 available bytes; 97.58% used; 225823060 free inodes.

server3 `/tmp`: 85483098112 available bytes; 95.23% used; 114174944 free inodes.

server3 `/var/tmp`: 85483098112 available bytes; 95.23% used; 114174944 free inodes.
| server4 | True | [] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 105769459712 available bytes; 94.10% used; 114349122 free inodes.

server4 `/home`: 105769459712 available bytes; 94.10% used; 114349122 free inodes.

server4 `/data`: 280426012672 available bytes; 96.12% used; 225350794 free inodes.

server4 `/tmp`: 105769459712 available bytes; 94.10% used; 114349122 free inodes.

server4 `/var/tmp`: 105769459712 available bytes; 94.10% used; 114349122 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
