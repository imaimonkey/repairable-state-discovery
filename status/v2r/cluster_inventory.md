# V2R cluster inventory

2026-09-27T07:03:37.307081+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | ['2', '3', '4', '5', '6', '7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 314478964736 available bytes; 82.46% used; 112440812 free inodes.

server1 `/home`: 314478964736 available bytes; 82.46% used; 112440812 free inodes.

server1 `/tmp`: 314478964736 available bytes; 82.46% used; 112440812 free inodes.

server1 `/var/tmp`: 314478964736 available bytes; 82.46% used; 112440812 free inodes.

server1 `/mnt/raid5`: 634670632960 available bytes; 97.09% used; 337400006 free inodes.
| server2 | True | [] | [] | reference_compatible=False |

server2 `/`: 17614794752 available bytes; 99.02% used; 110365001 free inodes.

server2 `/home`: 17614794752 available bytes; 99.02% used; 110365001 free inodes.

server2 `/tmp`: 17614794752 available bytes; 99.02% used; 110365001 free inodes.

server2 `/var/tmp`: 17614794752 available bytes; 99.02% used; 110365001 free inodes.

server2 `/mnt/raid5`: 572148334592 available bytes; 96.05% used; 444874828 free inodes.
| server3 | True | [] | [] | reference_compatible=True |

server3 `/`: 78574137344 available bytes; 95.62% used; 114062881 free inodes.

server3 `/home`: 78574137344 available bytes; 95.62% used; 114062881 free inodes.

server3 `/data`: 1333232992256 available bytes; 81.57% used; 225764638 free inodes.

server3 `/tmp`: 78574137344 available bytes; 95.62% used; 114062881 free inodes.

server3 `/var/tmp`: 78574137344 available bytes; 95.62% used; 114062881 free inodes.
| server4 | True | ['5'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 111071182848 available bytes; 93.80% used; 114372891 free inodes.

server4 `/home`: 111071182848 available bytes; 93.80% used; 114372891 free inodes.

server4 `/data`: 374400372736 available bytes; 94.83% used; 224771427 free inodes.

server4 `/tmp`: 111071182848 available bytes; 93.80% used; 114372891 free inodes.

server4 `/var/tmp`: 111071182848 available bytes; 93.80% used; 114372891 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
