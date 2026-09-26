# V2R cluster inventory

2026-09-26T19:59:34.538137+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | ['0', '3', '4', '5', '6', '7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 315538595840 available bytes; 82.40% used; 112445150 free inodes.

server1 `/home`: 315538595840 available bytes; 82.40% used; 112445150 free inodes.

server1 `/tmp`: 315538595840 available bytes; 82.40% used; 112445150 free inodes.

server1 `/var/tmp`: 315538595840 available bytes; 82.40% used; 112445150 free inodes.

server1 `/mnt/raid5`: 645853962240 available bytes; 97.04% used; 337467122 free inodes.
| server2 | True | ['2', '7'] | [] | reference_compatible=False |

server2 `/`: 18031161344 available bytes; 98.99% used; 110367561 free inodes.

server2 `/home`: 18031161344 available bytes; 98.99% used; 110367561 free inodes.

server2 `/tmp`: 18031161344 available bytes; 98.99% used; 110367561 free inodes.

server2 `/var/tmp`: 18031161344 available bytes; 98.99% used; 110367561 free inodes.

server2 `/mnt/raid5`: 601569816576 available bytes; 95.84% used; 444965639 free inodes.
| server3 | True | [] | [] | reference_compatible=True |

server3 `/`: 81265115136 available bytes; 95.47% used; 114065302 free inodes.

server3 `/home`: 81265115136 available bytes; 95.47% used; 114065302 free inodes.

server3 `/data`: 1348735021056 available bytes; 81.36% used; 225833121 free inodes.

server3 `/tmp`: 81265115136 available bytes; 95.47% used; 114065302 free inodes.

server3 `/var/tmp`: 81265115136 available bytes; 95.47% used; 114065302 free inodes.
| server4 | True | [] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 105919803392 available bytes; 94.09% used; 114347834 free inodes.

server4 `/home`: 105919803392 available bytes; 94.09% used; 114347834 free inodes.

server4 `/data`: 410278977536 available bytes; 94.33% used; 224824175 free inodes.

server4 `/tmp`: 105919803392 available bytes; 94.09% used; 114347834 free inodes.

server4 `/var/tmp`: 105919803392 available bytes; 94.09% used; 114347834 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
