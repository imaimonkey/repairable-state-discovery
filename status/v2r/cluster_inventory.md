# V2R cluster inventory

2026-09-27T06:55:34.801772+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | ['2', '3', '4', '5', '6', '7'] | ['/tmp', '/var/tmp'] |

server1 `/`: 314488324096 available bytes; 82.46% used; 112440812 free inodes.

server1 `/home`: 314488324096 available bytes; 82.46% used; 112440812 free inodes.

server1 `/tmp`: 314488324096 available bytes; 82.46% used; 112440812 free inodes.

server1 `/var/tmp`: 314488324096 available bytes; 82.46% used; 112440812 free inodes.

server1 `/mnt/raid5`: 634668625920 available bytes; 97.09% used; 337400002 free inodes.
| server2 | True | [] | [] |

server2 `/`: 17616601088 available bytes; 99.02% used; 110365001 free inodes.

server2 `/home`: 17616601088 available bytes; 99.02% used; 110365001 free inodes.

server2 `/tmp`: 17616601088 available bytes; 99.02% used; 110365001 free inodes.

server2 `/var/tmp`: 17616601088 available bytes; 99.02% used; 110365001 free inodes.

server2 `/mnt/raid5`: 571854757888 available bytes; 96.05% used; 444875179 free inodes.
| server3 | True | [] | [] |

server3 `/`: 78582317056 available bytes; 95.61% used; 114062883 free inodes.

server3 `/home`: 78582317056 available bytes; 95.61% used; 114062883 free inodes.

server3 `/data`: 1333238173696 available bytes; 81.57% used; 225764814 free inodes.

server3 `/tmp`: 78582317056 available bytes; 95.61% used; 114062883 free inodes.

server3 `/var/tmp`: 78582317056 available bytes; 95.61% used; 114062883 free inodes.
| server4 | True | ['5'] | ['/tmp', '/var/tmp'] |

server4 `/`: 111071428608 available bytes; 93.80% used; 114372897 free inodes.

server4 `/home`: 111071428608 available bytes; 93.80% used; 114372897 free inodes.

server4 `/data`: 374418505728 available bytes; 94.83% used; 224771143 free inodes.

server4 `/tmp`: 111071428608 available bytes; 93.80% used; 114372897 free inodes.

server4 `/var/tmp`: 111071428608 available bytes; 93.80% used; 114372897 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
