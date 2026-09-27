# V2R cluster inventory

2026-09-27T06:59:03.229459+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | ['2', '3', '4', '5', '6', '7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 314487308288 available bytes; 82.46% used; 112440810 free inodes.

server1 `/home`: 314487308288 available bytes; 82.46% used; 112440810 free inodes.

server1 `/tmp`: 314487308288 available bytes; 82.46% used; 112440810 free inodes.

server1 `/var/tmp`: 314487308288 available bytes; 82.46% used; 112440810 free inodes.

server1 `/mnt/raid5`: 634668765184 available bytes; 97.09% used; 337400002 free inodes.
| server2 | True | [] | [] | reference_compatible=False |

server2 `/`: 17615609856 available bytes; 99.02% used; 110365001 free inodes.

server2 `/home`: 17615609856 available bytes; 99.02% used; 110365001 free inodes.

server2 `/tmp`: 17615609856 available bytes; 99.02% used; 110365001 free inodes.

server2 `/var/tmp`: 17615609856 available bytes; 99.02% used; 110365001 free inodes.

server2 `/mnt/raid5`: 571752603648 available bytes; 96.05% used; 444874946 free inodes.
| server3 | True | [] | [] | reference_compatible=True |

server3 `/`: 78574612480 available bytes; 95.62% used; 114062883 free inodes.

server3 `/home`: 78574612480 available bytes; 95.62% used; 114062883 free inodes.

server3 `/data`: 1333234245632 available bytes; 81.57% used; 225764728 free inodes.

server3 `/tmp`: 78574612480 available bytes; 95.62% used; 114062883 free inodes.

server3 `/var/tmp`: 78574612480 available bytes; 95.62% used; 114062883 free inodes.
| server4 | True | ['5'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 111071272960 available bytes; 93.80% used; 114372878 free inodes.

server4 `/home`: 111071272960 available bytes; 93.80% used; 114372878 free inodes.

server4 `/data`: 374347329536 available bytes; 94.83% used; 224771139 free inodes.

server4 `/tmp`: 111071272960 available bytes; 93.80% used; 114372878 free inodes.

server4 `/var/tmp`: 111071272960 available bytes; 93.80% used; 114372878 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
