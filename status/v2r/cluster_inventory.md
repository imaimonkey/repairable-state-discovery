# V2R cluster inventory

2026-09-24T05:21:38.001776+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | ['7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 324564066304 available bytes; 81.89% used; 112492457 free inodes.

server1 `/home`: 324564066304 available bytes; 81.89% used; 112492457 free inodes.

server1 `/tmp`: 324564066304 available bytes; 81.89% used; 112492457 free inodes.

server1 `/var/tmp`: 324564066304 available bytes; 81.89% used; 112492457 free inodes.

server1 `/mnt/raid5`: 508006952960 available bytes; 97.67% used; 337724524 free inodes.
| server2 | True | [] | [] | reference_compatible=False |

server2 `/`: 40747327488 available bytes; 97.73% used; 110430340 free inodes.

server2 `/home`: 40747327488 available bytes; 97.73% used; 110430340 free inodes.

server2 `/tmp`: 40747327488 available bytes; 97.73% used; 110430340 free inodes.

server2 `/var/tmp`: 40747327488 available bytes; 97.73% used; 110430340 free inodes.

server2 `/mnt/raid5`: 522642202624 available bytes; 96.39% used; 445194154 free inodes.
| server3 | True | ['1'] | ['/tmp', '/var/tmp'] | reference_compatible=True |

server3 `/`: 291992326144 available bytes; 83.71% used; 114175930 free inodes.

server3 `/home`: 291992326144 available bytes; 83.71% used; 114175930 free inodes.

server3 `/data`: 21149417472 available bytes; 99.71% used; 225839810 free inodes.

server3 `/tmp`: 291992326144 available bytes; 83.71% used; 114175930 free inodes.

server3 `/var/tmp`: 291992326144 available bytes; 83.71% used; 114175930 free inodes.
| server4 | True | ['7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 105817444352 available bytes; 94.09% used; 114349367 free inodes.

server4 `/home`: 105817444352 available bytes; 94.09% used; 114349367 free inodes.

server4 `/data`: 252562571264 available bytes; 96.51% used; 225366568 free inodes.

server4 `/tmp`: 105817444352 available bytes; 94.09% used; 114349367 free inodes.

server4 `/var/tmp`: 105817444352 available bytes; 94.09% used; 114349367 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
