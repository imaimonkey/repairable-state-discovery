# V2R cluster inventory

2026-09-27T07:01:41.498782+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | ['2', '3', '4', '5', '6', '7'] | ['/tmp', '/var/tmp'] |

server1 `/`: 314486616064 available bytes; 82.46% used; 112440810 free inodes.

server1 `/home`: 314486616064 available bytes; 82.46% used; 112440810 free inodes.

server1 `/tmp`: 314486616064 available bytes; 82.46% used; 112440810 free inodes.

server1 `/var/tmp`: 314486616064 available bytes; 82.46% used; 112440810 free inodes.

server1 `/mnt/raid5`: 634669490176 available bytes; 97.09% used; 337400008 free inodes.
| server2 | True | [] | [] |

server2 `/`: 17615360000 available bytes; 99.02% used; 110365001 free inodes.

server2 `/home`: 17615360000 available bytes; 99.02% used; 110365001 free inodes.

server2 `/tmp`: 17615360000 available bytes; 99.02% used; 110365001 free inodes.

server2 `/var/tmp`: 17615360000 available bytes; 99.02% used; 110365001 free inodes.

server2 `/mnt/raid5`: 572209901568 available bytes; 96.05% used; 444875021 free inodes.
| server3 | True | [] | [] |

server3 `/`: 78574444544 available bytes; 95.62% used; 114062884 free inodes.

server3 `/home`: 78574444544 available bytes; 95.62% used; 114062884 free inodes.

server3 `/data`: 1333232193536 available bytes; 81.57% used; 225764704 free inodes.

server3 `/tmp`: 78574444544 available bytes; 95.62% used; 114062884 free inodes.

server3 `/var/tmp`: 78574444544 available bytes; 95.62% used; 114062884 free inodes.
| server4 | True | ['5'] | ['/tmp', '/var/tmp'] |

server4 `/`: 111071256576 available bytes; 93.80% used; 114372894 free inodes.

server4 `/home`: 111071256576 available bytes; 93.80% used; 114372894 free inodes.

server4 `/data`: 374372773888 available bytes; 94.83% used; 224771474 free inodes.

server4 `/tmp`: 111071256576 available bytes; 93.80% used; 114372894 free inodes.

server4 `/var/tmp`: 111071256576 available bytes; 93.80% used; 114372894 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
