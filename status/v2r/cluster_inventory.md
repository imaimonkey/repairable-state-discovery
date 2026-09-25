# V2R cluster inventory

2026-09-25T12:23:54.591430+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | [] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 319188025344 available bytes; 82.19% used; 112477810 free inodes.

server1 `/home`: 319188025344 available bytes; 82.19% used; 112477810 free inodes.

server1 `/tmp`: 319188025344 available bytes; 82.19% used; 112477810 free inodes.

server1 `/var/tmp`: 319188025344 available bytes; 82.19% used; 112477810 free inodes.

server1 `/mnt/raid5`: 364264046592 available bytes; 98.33% used; 337548219 free inodes.
| server2 | True | ['2', '3', '4', '5', '6'] | [] | reference_compatible=False |

server2 `/`: 22903099392 available bytes; 98.72% used; 110409959 free inodes.

server2 `/home`: 22903099392 available bytes; 98.72% used; 110409959 free inodes.

server2 `/tmp`: 22903099392 available bytes; 98.72% used; 110409959 free inodes.

server2 `/var/tmp`: 22903099392 available bytes; 98.72% used; 110409959 free inodes.

server2 `/mnt/raid5`: 324062924800 available bytes; 97.76% used; 445080526 free inodes.
| server3 | True | [] | [] | reference_compatible=True |

server3 `/`: 84211036160 available bytes; 95.30% used; 114154978 free inodes.

server3 `/home`: 84211036160 available bytes; 95.30% used; 114154978 free inodes.

server3 `/data`: 142277963776 available bytes; 98.03% used; 225811240 free inodes.

server3 `/tmp`: 84211036160 available bytes; 95.30% used; 114154978 free inodes.

server3 `/var/tmp`: 84211036160 available bytes; 95.30% used; 114154978 free inodes.
| server4 | True | [] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 105666314240 available bytes; 94.10% used; 114349722 free inodes.

server4 `/home`: 105666314240 available bytes; 94.10% used; 114349722 free inodes.

server4 `/data`: 232035868672 available bytes; 96.79% used; 224965314 free inodes.

server4 `/tmp`: 105666314240 available bytes; 94.10% used; 114349722 free inodes.

server4 `/var/tmp`: 105666314240 available bytes; 94.10% used; 114349722 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
