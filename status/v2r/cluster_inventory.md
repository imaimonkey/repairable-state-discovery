# V2R cluster inventory

2026-09-24T05:24:46.285913+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | ['7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 324556341248 available bytes; 81.89% used; 112492424 free inodes.

server1 `/home`: 324556341248 available bytes; 81.89% used; 112492424 free inodes.

server1 `/tmp`: 324556341248 available bytes; 81.89% used; 112492424 free inodes.

server1 `/var/tmp`: 324556341248 available bytes; 81.89% used; 112492424 free inodes.

server1 `/mnt/raid5`: 511832326144 available bytes; 97.65% used; 337724383 free inodes.
| server2 | True | [] | [] | reference_compatible=False |

server2 `/`: 40738832384 available bytes; 97.73% used; 110430307 free inodes.

server2 `/home`: 40738832384 available bytes; 97.73% used; 110430307 free inodes.

server2 `/tmp`: 40738832384 available bytes; 97.73% used; 110430307 free inodes.

server2 `/var/tmp`: 40738832384 available bytes; 97.73% used; 110430307 free inodes.

server2 `/mnt/raid5`: 522545451008 available bytes; 96.39% used; 445193829 free inodes.
| server3 | True | ['1'] | ['/tmp', '/var/tmp'] | reference_compatible=True |

server3 `/`: 292377866240 available bytes; 83.68% used; 114199791 free inodes.

server3 `/home`: 292377866240 available bytes; 83.68% used; 114199791 free inodes.

server3 `/data`: 21147250688 available bytes; 99.71% used; 225839751 free inodes.

server3 `/tmp`: 292377866240 available bytes; 83.68% used; 114199791 free inodes.

server3 `/var/tmp`: 292377866240 available bytes; 83.68% used; 114199791 free inodes.
| server4 | True | ['7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 105817321472 available bytes; 94.10% used; 114349367 free inodes.

server4 `/home`: 105817321472 available bytes; 94.10% used; 114349367 free inodes.

server4 `/data`: 252567236608 available bytes; 96.51% used; 225366563 free inodes.

server4 `/tmp`: 105817321472 available bytes; 94.10% used; 114349367 free inodes.

server4 `/var/tmp`: 105817321472 available bytes; 94.10% used; 114349367 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
