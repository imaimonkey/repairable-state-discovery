# V2R cluster inventory

2026-09-24T05:23:12.570036+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | ['7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 324559101952 available bytes; 81.89% used; 112492440 free inodes.

server1 `/home`: 324559101952 available bytes; 81.89% used; 112492440 free inodes.

server1 `/tmp`: 324559101952 available bytes; 81.89% used; 112492440 free inodes.

server1 `/var/tmp`: 324559101952 available bytes; 81.89% used; 112492440 free inodes.

server1 `/mnt/raid5`: 510290845696 available bytes; 97.66% used; 337724464 free inodes.
| server2 | True | [] | [] | reference_compatible=False |

server2 `/`: 40738865152 available bytes; 97.73% used; 110430322 free inodes.

server2 `/home`: 40738865152 available bytes; 97.73% used; 110430322 free inodes.

server2 `/tmp`: 40738865152 available bytes; 97.73% used; 110430322 free inodes.

server2 `/var/tmp`: 40738865152 available bytes; 97.73% used; 110430322 free inodes.

server2 `/mnt/raid5`: 522598969344 available bytes; 96.39% used; 445193988 free inodes.
| server3 | True | ['1'] | ['/tmp', '/var/tmp'] | reference_compatible=True |

server3 `/`: 291991961600 available bytes; 83.71% used; 114175930 free inodes.

server3 `/home`: 291991961600 available bytes; 83.71% used; 114175930 free inodes.

server3 `/data`: 21146275840 available bytes; 99.71% used; 225839778 free inodes.

server3 `/tmp`: 291991961600 available bytes; 83.71% used; 114175930 free inodes.

server3 `/var/tmp`: 291991961600 available bytes; 83.71% used; 114175930 free inodes.
| server4 | True | ['7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 105817387008 available bytes; 94.10% used; 114349367 free inodes.

server4 `/home`: 105817387008 available bytes; 94.10% used; 114349367 free inodes.

server4 `/data`: 252561846272 available bytes; 96.51% used; 225366568 free inodes.

server4 `/tmp`: 105817387008 available bytes; 94.10% used; 114349367 free inodes.

server4 `/var/tmp`: 105817387008 available bytes; 94.10% used; 114349367 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
