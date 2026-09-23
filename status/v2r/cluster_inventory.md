# V2R cluster inventory

2026-09-23T16:27:46.770121+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | False | [] | [] | reference_compatible=False |
| server2 | True | ['7'] | [] | reference_compatible=False |

server2 `/`: 41407557632 available bytes; 97.69% used; 110435426 free inodes.

server2 `/home`: 41407557632 available bytes; 97.69% used; 110435426 free inodes.

server2 `/tmp`: 41407557632 available bytes; 97.69% used; 110435426 free inodes.

server2 `/var/tmp`: 41407557632 available bytes; 97.69% used; 110435426 free inodes.

server2 `/mnt/raid5`: 548349394944 available bytes; 96.21% used; 445217708 free inodes.
| server3 | True | ['0'] | ['/tmp', '/var/tmp'] | reference_compatible=True |

server3 `/`: 299675303936 available bytes; 83.28% used; 114276494 free inodes.

server3 `/home`: 299675303936 available bytes; 83.28% used; 114276494 free inodes.

server3 `/data`: 95367233536 available bytes; 98.68% used; 225853868 free inodes.

server3 `/tmp`: 299675303936 available bytes; 83.28% used; 114276494 free inodes.

server3 `/var/tmp`: 299675303936 available bytes; 83.28% used; 114276494 free inodes.
| server4 | True | ['1', '2', '3', '5', '6'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 111498674176 available bytes; 93.78% used; 114375794 free inodes.

server4 `/home`: 111498674176 available bytes; 93.78% used; 114375794 free inodes.

server4 `/data`: 37295591424 available bytes; 99.48% used; 225486307 free inodes.

server4 `/tmp`: 111498674176 available bytes; 93.78% used; 114375794 free inodes.

server4 `/var/tmp`: 111498674176 available bytes; 93.78% used; 114375794 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
