# V2R cluster inventory

2026-09-27T07:05:08.634279+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | ['2', '3', '4', '5', '6', '7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 314481774592 available bytes; 82.46% used; 112440816 free inodes.

server1 `/home`: 314481774592 available bytes; 82.46% used; 112440816 free inodes.

server1 `/tmp`: 314481774592 available bytes; 82.46% used; 112440816 free inodes.

server1 `/var/tmp`: 314481774592 available bytes; 82.46% used; 112440816 free inodes.

server1 `/mnt/raid5`: 634670112768 available bytes; 97.09% used; 337400004 free inodes.
| server2 | True | [] | [] | reference_compatible=False |

server2 `/`: 17614487552 available bytes; 99.02% used; 110365001 free inodes.

server2 `/home`: 17614487552 available bytes; 99.02% used; 110365001 free inodes.

server2 `/tmp`: 17614487552 available bytes; 99.02% used; 110365001 free inodes.

server2 `/var/tmp`: 17614487552 available bytes; 99.02% used; 110365001 free inodes.

server2 `/mnt/raid5`: 572107964416 available bytes; 96.05% used; 444874784 free inodes.
| server3 | True | [] | [] | reference_compatible=True |

server3 `/`: 78573953024 available bytes; 95.62% used; 114062883 free inodes.

server3 `/home`: 78573953024 available bytes; 95.62% used; 114062883 free inodes.

server3 `/data`: 1333230522368 available bytes; 81.57% used; 225764616 free inodes.

server3 `/tmp`: 78573953024 available bytes; 95.62% used; 114062883 free inodes.

server3 `/var/tmp`: 78573953024 available bytes; 95.62% used; 114062883 free inodes.
| server4 | True | ['5'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 111071141888 available bytes; 93.80% used; 114372892 free inodes.

server4 `/home`: 111071141888 available bytes; 93.80% used; 114372892 free inodes.

server4 `/data`: 374395961344 available bytes; 94.83% used; 224771411 free inodes.

server4 `/tmp`: 111071141888 available bytes; 93.80% used; 114372892 free inodes.

server4 `/var/tmp`: 111071141888 available bytes; 93.80% used; 114372892 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
