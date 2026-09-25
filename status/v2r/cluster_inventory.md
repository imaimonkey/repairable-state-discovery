# V2R cluster inventory

2026-09-25T15:25:59.121171+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | [] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 318707372032 available bytes; 82.22% used; 112476525 free inodes.

server1 `/home`: 318707372032 available bytes; 82.22% used; 112476525 free inodes.

server1 `/tmp`: 318707380224 available bytes; 82.22% used; 112476526 free inodes.

server1 `/var/tmp`: 318707388416 available bytes; 82.22% used; 112476527 free inodes.

server1 `/mnt/raid5`: 363987218432 available bytes; 98.33% used; 337545327 free inodes.
| server2 | True | ['2', '3', '4', '5', '6'] | [] | reference_compatible=False |

server2 `/`: 23115202560 available bytes; 98.71% used; 110407944 free inodes.

server2 `/home`: 23115202560 available bytes; 98.71% used; 110407944 free inodes.

server2 `/tmp`: 23115202560 available bytes; 98.71% used; 110407944 free inodes.

server2 `/var/tmp`: 23115202560 available bytes; 98.71% used; 110407944 free inodes.

server2 `/mnt/raid5`: 320081760256 available bytes; 97.79% used; 445073254 free inodes.
| server3 | True | [] | [] | reference_compatible=True |

server3 `/`: 84423856128 available bytes; 95.29% used; 114153457 free inodes.

server3 `/home`: 84423856128 available bytes; 95.29% used; 114153457 free inodes.

server3 `/data`: 142173016064 available bytes; 98.04% used; 225807804 free inodes.

server3 `/tmp`: 84423856128 available bytes; 95.29% used; 114153457 free inodes.

server3 `/var/tmp`: 84423856128 available bytes; 95.29% used; 114153457 free inodes.
| server4 | True | ['3', '5'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 105637965824 available bytes; 94.11% used; 114349678 free inodes.

server4 `/home`: 105637965824 available bytes; 94.11% used; 114349678 free inodes.

server4 `/data`: 231358504960 available bytes; 96.80% used; 224944095 free inodes.

server4 `/tmp`: 105637965824 available bytes; 94.11% used; 114349678 free inodes.

server4 `/var/tmp`: 105637965824 available bytes; 94.11% used; 114349678 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
