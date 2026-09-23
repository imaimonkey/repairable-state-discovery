# V2R cluster inventory

2026-09-23T16:36:57.204835+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | False | [] | [] | reference_compatible=False |
| server2 | True | ['7'] | [] | reference_compatible=False |

server2 `/`: 41405431808 available bytes; 97.69% used; 110435426 free inodes.

server2 `/home`: 41405431808 available bytes; 97.69% used; 110435426 free inodes.

server2 `/tmp`: 41405431808 available bytes; 97.69% used; 110435426 free inodes.

server2 `/var/tmp`: 41405431808 available bytes; 97.69% used; 110435426 free inodes.

server2 `/mnt/raid5`: 548600414208 available bytes; 96.21% used; 445217353 free inodes.
| server3 | True | ['0'] | ['/tmp', '/var/tmp'] | reference_compatible=True |

server3 `/`: 299454726144 available bytes; 83.29% used; 114267303 free inodes.

server3 `/home`: 299454726144 available bytes; 83.29% used; 114267303 free inodes.

server3 `/data`: 95362416640 available bytes; 98.68% used; 225853678 free inodes.

server3 `/tmp`: 299454726144 available bytes; 83.29% used; 114267303 free inodes.

server3 `/var/tmp`: 299454726144 available bytes; 83.29% used; 114267303 free inodes.
| server4 | True | ['1', '2', '3', '5', '6'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 111498473472 available bytes; 93.78% used; 114375794 free inodes.

server4 `/home`: 111498473472 available bytes; 93.78% used; 114375794 free inodes.

server4 `/data`: 36204396544 available bytes; 99.50% used; 225477990 free inodes.

server4 `/tmp`: 111498473472 available bytes; 93.78% used; 114375794 free inodes.

server4 `/var/tmp`: 111498473472 available bytes; 93.78% used; 114375794 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
