# V2R cluster inventory

2026-09-24T07:46:17.953941+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | ['5', '7'] | ['/tmp', '/var/tmp'] |

server1 `/`: 324433285120 available bytes; 81.90% used; 112490901 free inodes.

server1 `/home`: 324433285120 available bytes; 81.90% used; 112490901 free inodes.

server1 `/tmp`: 324433285120 available bytes; 81.90% used; 112490901 free inodes.

server1 `/var/tmp`: 324433285120 available bytes; 81.90% used; 112490901 free inodes.

server1 `/mnt/raid5`: 515632291840 available bytes; 97.63% used; 337722707 free inodes.
| server2 | True | [] | [] |

server2 `/`: 57833410560 available bytes; 96.77% used; 110431114 free inodes.

server2 `/home`: 57833410560 available bytes; 96.77% used; 110431114 free inodes.

server2 `/tmp`: 57833410560 available bytes; 96.77% used; 110431114 free inodes.

server2 `/var/tmp`: 57833410560 available bytes; 96.77% used; 110431114 free inodes.

server2 `/mnt/raid5`: 517257396224 available bytes; 96.43% used; 445181120 free inodes.
| server3 | True | ['3'] | ['/tmp', '/var/tmp'] |

server3 `/`: 127151230976 available bytes; 92.90% used; 114199802 free inodes.

server3 `/home`: 127151230976 available bytes; 92.90% used; 114199802 free inodes.

server3 `/data`: 137616007168 available bytes; 98.10% used; 225833399 free inodes.

server3 `/tmp`: 127151230976 available bytes; 92.90% used; 114199802 free inodes.

server3 `/var/tmp`: 127151230976 available bytes; 92.90% used; 114199802 free inodes.
| server4 | True | [] | ['/tmp', '/var/tmp'] |

server4 `/`: 105582002176 available bytes; 94.11% used; 114349171 free inodes.

server4 `/home`: 105582002176 available bytes; 94.11% used; 114349171 free inodes.

server4 `/data`: 285591609344 available bytes; 96.05% used; 225366733 free inodes.

server4 `/tmp`: 105582002176 available bytes; 94.11% used; 114349171 free inodes.

server4 `/var/tmp`: 105581998080 available bytes; 94.11% used; 114349171 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
