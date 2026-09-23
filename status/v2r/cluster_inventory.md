# V2R cluster inventory

2026-09-23T16:32:22.497132+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | False | [] | [] | reference_compatible=False |
| server2 | True | ['7'] | [] | reference_compatible=False |

server2 `/`: 41406185472 available bytes; 97.69% used; 110435426 free inodes.

server2 `/home`: 41406185472 available bytes; 97.69% used; 110435426 free inodes.

server2 `/tmp`: 41406185472 available bytes; 97.69% used; 110435426 free inodes.

server2 `/var/tmp`: 41406185472 available bytes; 97.69% used; 110435426 free inodes.

server2 `/mnt/raid5`: 548736917504 available bytes; 96.21% used; 445217603 free inodes.
| server3 | True | ['0'] | ['/tmp', '/var/tmp'] | reference_compatible=True |

server3 `/`: 299459080192 available bytes; 83.29% used; 114267355 free inodes.

server3 `/home`: 299459080192 available bytes; 83.29% used; 114267355 free inodes.

server3 `/data`: 95365263360 available bytes; 98.68% used; 225853750 free inodes.

server3 `/tmp`: 299459080192 available bytes; 83.29% used; 114267355 free inodes.

server3 `/var/tmp`: 299459080192 available bytes; 83.29% used; 114267355 free inodes.
| server4 | True | ['1', '2', '3', '5', '6'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 111498575872 available bytes; 93.78% used; 114375794 free inodes.

server4 `/home`: 111498575872 available bytes; 93.78% used; 114375794 free inodes.

server4 `/data`: 36263301120 available bytes; 99.50% used; 225478010 free inodes.

server4 `/tmp`: 111498575872 available bytes; 93.78% used; 114375794 free inodes.

server4 `/var/tmp`: 111498575872 available bytes; 93.78% used; 114375794 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
