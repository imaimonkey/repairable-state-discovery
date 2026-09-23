# V2R cluster inventory

2026-09-23T21:14:47.237559+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | ['6', '7'] | ['/tmp', '/var/tmp', '/mnt/raid5'] | reference_compatible=False |

server1 `/`: 325722611712 available bytes; 81.83% used; 112501448 free inodes.

server1 `/home`: 325722611712 available bytes; 81.83% used; 112501448 free inodes.

server1 `/tmp`: 325722611712 available bytes; 81.83% used; 112501448 free inodes.

server1 `/var/tmp`: 325722611712 available bytes; 81.83% used; 112501448 free inodes.

server1 `/mnt/raid5`: 1388130349056 available bytes; 93.63% used; 337739964 free inodes.
| server2 | True | [] | [] | reference_compatible=False |

server2 `/`: 41112772608 available bytes; 97.71% used; 110432694 free inodes.

server2 `/home`: 41112772608 available bytes; 97.71% used; 110432694 free inodes.

server2 `/tmp`: 41112772608 available bytes; 97.71% used; 110432694 free inodes.

server2 `/var/tmp`: 41112772608 available bytes; 97.71% used; 110432694 free inodes.

server2 `/mnt/raid5`: 538998452224 available bytes; 96.28% used; 445209206 free inodes.
| server3 | True | [] | ['/tmp', '/var/tmp'] | reference_compatible=True |

server3 `/`: 293285666816 available bytes; 83.63% used; 114229258 free inodes.

server3 `/home`: 293285666816 available bytes; 83.63% used; 114229258 free inodes.

server3 `/data`: 52307881984 available bytes; 99.28% used; 225849442 free inodes.

server3 `/tmp`: 293285666816 available bytes; 83.63% used; 114229258 free inodes.

server3 `/var/tmp`: 293285666816 available bytes; 83.63% used; 114229258 free inodes.
| server4 | True | ['2', '3', '5', '6', '7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 106491191296 available bytes; 94.06% used; 114356035 free inodes.

server4 `/home`: 106491191296 available bytes; 94.06% used; 114356035 free inodes.

server4 `/data`: 300452163584 available bytes; 95.85% used; 225454045 free inodes.

server4 `/tmp`: 106491191296 available bytes; 94.06% used; 114356035 free inodes.

server4 `/var/tmp`: 106491191296 available bytes; 94.06% used; 114356035 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
