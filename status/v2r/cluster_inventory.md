# V2R cluster inventory

2026-09-24T14:42:49.352932+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | [] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 324051603456 available bytes; 81.92% used; 112481472 free inodes.

server1 `/home`: 324051603456 available bytes; 81.92% used; 112481472 free inodes.

server1 `/tmp`: 324051603456 available bytes; 81.92% used; 112481472 free inodes.

server1 `/var/tmp`: 324051603456 available bytes; 81.92% used; 112481472 free inodes.

server1 `/mnt/raid5`: 416864514048 available bytes; 98.09% used; 337666726 free inodes.
| server2 | True | ['7'] | [] | reference_compatible=False |

server2 `/`: 57442934784 available bytes; 96.80% used; 110427981 free inodes.

server2 `/home`: 57442934784 available bytes; 96.80% used; 110427981 free inodes.

server2 `/tmp`: 57442934784 available bytes; 96.80% used; 110427981 free inodes.

server2 `/var/tmp`: 57442934784 available bytes; 96.80% used; 110427981 free inodes.

server2 `/mnt/raid5`: 504100495360 available bytes; 96.52% used; 445167579 free inodes.
| server3 | True | ['0'] | [] | reference_compatible=True |

server3 `/`: 84854468608 available bytes; 95.26% used; 114183847 free inodes.

server3 `/home`: 84854468608 available bytes; 95.26% used; 114183847 free inodes.

server3 `/data`: 160741146624 available bytes; 97.78% used; 225807886 free inodes.

server3 `/tmp`: 84854468608 available bytes; 95.26% used; 114183847 free inodes.

server3 `/var/tmp`: 84854468608 available bytes; 95.26% used; 114183847 free inodes.
| server4 | True | [] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 105758412800 available bytes; 94.10% used; 114348683 free inodes.

server4 `/home`: 105758412800 available bytes; 94.10% used; 114348683 free inodes.

server4 `/data`: 69180551168 available bytes; 99.04% used; 225257005 free inodes.

server4 `/tmp`: 105758412800 available bytes; 94.10% used; 114348683 free inodes.

server4 `/var/tmp`: 105758412800 available bytes; 94.10% used; 114348683 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
