# V2R cluster inventory

2026-09-24T20:52:45.527483+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | [] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 323978805248 available bytes; 81.93% used; 112481427 free inodes.

server1 `/home`: 323978805248 available bytes; 81.93% used; 112481427 free inodes.

server1 `/tmp`: 323978805248 available bytes; 81.93% used; 112481427 free inodes.

server1 `/var/tmp`: 323978805248 available bytes; 81.93% used; 112481427 free inodes.

server1 `/mnt/raid5`: 415575961600 available bytes; 98.09% used; 337631813 free inodes.
| server2 | True | ['7'] | [] | reference_compatible=False |

server2 `/`: 30145835008 available bytes; 98.32% used; 110411380 free inodes.

server2 `/home`: 30145835008 available bytes; 98.32% used; 110411380 free inodes.

server2 `/tmp`: 30145835008 available bytes; 98.32% used; 110411380 free inodes.

server2 `/var/tmp`: 30145835008 available bytes; 98.32% used; 110411380 free inodes.

server2 `/mnt/raid5`: 491572244480 available bytes; 96.60% used; 445156179 free inodes.
| server3 | True | [] | [] | reference_compatible=True |

server3 `/`: 84384436224 available bytes; 95.29% used; 114156101 free inodes.

server3 `/home`: 84384436224 available bytes; 95.29% used; 114156101 free inodes.

server3 `/data`: 151085494272 available bytes; 97.91% used; 225803895 free inodes.

server3 `/tmp`: 84384436224 available bytes; 95.29% used; 114156101 free inodes.

server3 `/var/tmp`: 84384436224 available bytes; 95.29% used; 114156101 free inodes.
| server4 | True | ['4'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 105639374848 available bytes; 94.10% used; 114348380 free inodes.

server4 `/home`: 105639374848 available bytes; 94.10% used; 114348380 free inodes.

server4 `/data`: 78619877376 available bytes; 98.91% used; 225255757 free inodes.

server4 `/tmp`: 105639374848 available bytes; 94.10% used; 114348380 free inodes.

server4 `/var/tmp`: 105639374848 available bytes; 94.10% used; 114348380 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
