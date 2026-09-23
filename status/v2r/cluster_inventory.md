# V2R cluster inventory

2026-09-23T16:26:15.141845+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | False | [] | [] | reference_compatible=False |
| server2 | True | ['7'] | [] | reference_compatible=False |

server2 `/`: 41408274432 available bytes; 97.69% used; 110435426 free inodes.

server2 `/home`: 41408274432 available bytes; 97.69% used; 110435426 free inodes.

server2 `/tmp`: 41408274432 available bytes; 97.69% used; 110435426 free inodes.

server2 `/var/tmp`: 41408274432 available bytes; 97.69% used; 110435426 free inodes.

server2 `/mnt/raid5`: 548929126400 available bytes; 96.21% used; 445217773 free inodes.
| server3 | True | ['0'] | ['/tmp', '/var/tmp'] | reference_compatible=True |

server3 `/`: 299683942400 available bytes; 83.28% used; 114277810 free inodes.

server3 `/home`: 299683942400 available bytes; 83.28% used; 114277810 free inodes.

server3 `/data`: 102685847552 available bytes; 98.58% used; 225853888 free inodes.

server3 `/tmp`: 299683942400 available bytes; 83.28% used; 114277810 free inodes.

server3 `/var/tmp`: 299683942400 available bytes; 83.28% used; 114277810 free inodes.
| server4 | True | ['1', '2', '3', '5', '6'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 111498698752 available bytes; 93.78% used; 114375794 free inodes.

server4 `/home`: 111498698752 available bytes; 93.78% used; 114375794 free inodes.

server4 `/data`: 37332320256 available bytes; 99.48% used; 225486405 free inodes.

server4 `/tmp`: 111498698752 available bytes; 93.78% used; 114375794 free inodes.

server4 `/var/tmp`: 111498698752 available bytes; 93.78% used; 114375794 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
