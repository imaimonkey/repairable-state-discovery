# V2R cluster inventory

2026-09-25T15:21:24.339783+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | [] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 319044276224 available bytes; 82.20% used; 112476399 free inodes.

server1 `/home`: 319044276224 available bytes; 82.20% used; 112476399 free inodes.

server1 `/tmp`: 319044276224 available bytes; 82.20% used; 112476399 free inodes.

server1 `/var/tmp`: 319044276224 available bytes; 82.20% used; 112476399 free inodes.

server1 `/mnt/raid5`: 364417892352 available bytes; 98.33% used; 337545361 free inodes.
| server2 | True | ['2', '3', '4', '5', '6'] | [] | reference_compatible=False |

server2 `/`: 23101870080 available bytes; 98.71% used; 110407940 free inodes.

server2 `/home`: 23101870080 available bytes; 98.71% used; 110407940 free inodes.

server2 `/tmp`: 23101870080 available bytes; 98.71% used; 110407940 free inodes.

server2 `/var/tmp`: 23101870080 available bytes; 98.71% used; 110407940 free inodes.

server2 `/mnt/raid5`: 320207867904 available bytes; 97.79% used; 445073261 free inodes.
| server3 | True | [] | [] | reference_compatible=True |

server3 `/`: 84424572928 available bytes; 95.29% used; 114153459 free inodes.

server3 `/home`: 84424572928 available bytes; 95.29% used; 114153459 free inodes.

server3 `/data`: 142178533376 available bytes; 98.04% used; 225807884 free inodes.

server3 `/tmp`: 84424572928 available bytes; 95.29% used; 114153459 free inodes.

server3 `/var/tmp`: 84424572928 available bytes; 95.29% used; 114153459 free inodes.
| server4 | True | ['3', '5'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 105638080512 available bytes; 94.11% used; 114349678 free inodes.

server4 `/home`: 105638080512 available bytes; 94.11% used; 114349678 free inodes.

server4 `/data`: 231286902784 available bytes; 96.80% used; 224944662 free inodes.

server4 `/tmp`: 105638080512 available bytes; 94.11% used; 114349678 free inodes.

server4 `/var/tmp`: 105638080512 available bytes; 94.11% used; 114349678 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
