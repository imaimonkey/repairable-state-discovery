# V2R cluster inventory

2026-09-25T14:11:01.116607+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | [] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 319152984064 available bytes; 82.20% used; 112476971 free inodes.

server1 `/home`: 319152984064 available bytes; 82.20% used; 112476971 free inodes.

server1 `/tmp`: 319152984064 available bytes; 82.20% used; 112476971 free inodes.

server1 `/var/tmp`: 319152984064 available bytes; 82.20% used; 112476971 free inodes.

server1 `/mnt/raid5`: 364072980480 available bytes; 98.33% used; 337547434 free inodes.
| server2 | True | ['3', '4', '5', '6'] | [] | reference_compatible=False |

server2 `/`: 4730859520 available bytes; 99.74% used; 110407467 free inodes.

server2 `/home`: 4730859520 available bytes; 99.74% used; 110407467 free inodes.

server2 `/tmp`: 4730859520 available bytes; 99.74% used; 110407467 free inodes.

server2 `/var/tmp`: 4730859520 available bytes; 99.74% used; 110407467 free inodes.

server2 `/mnt/raid5`: 321976115200 available bytes; 97.78% used; 445075986 free inodes.
| server3 | True | [] | [] | reference_compatible=True |

server3 `/`: 84280680448 available bytes; 95.30% used; 114154462 free inodes.

server3 `/home`: 84280680448 available bytes; 95.30% used; 114154462 free inodes.

server3 `/data`: 142218481664 available bytes; 98.03% used; 225809015 free inodes.

server3 `/tmp`: 84280680448 available bytes; 95.30% used; 114154462 free inodes.

server3 `/var/tmp`: 84280680448 available bytes; 95.30% used; 114154462 free inodes.
| server4 | True | ['2'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 105654829056 available bytes; 94.10% used; 114349705 free inodes.

server4 `/home`: 105654829056 available bytes; 94.10% used; 114349705 free inodes.

server4 `/data`: 231455166464 available bytes; 96.80% used; 224947511 free inodes.

server4 `/tmp`: 105654829056 available bytes; 94.10% used; 114349705 free inodes.

server4 `/var/tmp`: 105654829056 available bytes; 94.10% used; 114349705 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
