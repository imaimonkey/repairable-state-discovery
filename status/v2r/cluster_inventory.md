# V2R cluster inventory

2026-09-24T00:18:34.805473+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | [] | ['/tmp', '/var/tmp', '/mnt/raid5'] |

server1 `/`: 325558710272 available bytes; 81.84% used; 112500720 free inodes.

server1 `/home`: 325558710272 available bytes; 81.84% used; 112500720 free inodes.

server1 `/tmp`: 325558710272 available bytes; 81.84% used; 112500720 free inodes.

server1 `/var/tmp`: 325558710272 available bytes; 81.84% used; 112500720 free inodes.

server1 `/mnt/raid5`: 1170890493952 available bytes; 94.63% used; 337735200 free inodes.
| server2 | True | [] | [] |

server2 `/`: 41007656960 available bytes; 97.71% used; 110432380 free inodes.

server2 `/home`: 41007656960 available bytes; 97.71% used; 110432380 free inodes.

server2 `/tmp`: 41007656960 available bytes; 97.71% used; 110432380 free inodes.

server2 `/var/tmp`: 41007656960 available bytes; 97.71% used; 110432380 free inodes.

server2 `/mnt/raid5`: 533145452544 available bytes; 96.32% used; 445203802 free inodes.
| server3 | True | [] | ['/tmp', '/var/tmp'] |

server3 `/`: 292588908544 available bytes; 83.67% used; 114206289 free inodes.

server3 `/home`: 292588908544 available bytes; 83.67% used; 114206289 free inodes.

server3 `/data`: 82248761344 available bytes; 98.86% used; 225844423 free inodes.

server3 `/tmp`: 292588908544 available bytes; 83.67% used; 114206289 free inodes.

server3 `/var/tmp`: 292588908544 available bytes; 83.67% used; 114206289 free inodes.
| server4 | True | ['1', '3', '6', '7'] | ['/tmp', '/var/tmp'] |

server4 `/`: 106099589120 available bytes; 94.08% used; 114350651 free inodes.

server4 `/home`: 106099589120 available bytes; 94.08% used; 114350651 free inodes.

server4 `/data`: 292914528256 available bytes; 95.95% used; 225414570 free inodes.

server4 `/tmp`: 106099589120 available bytes; 94.08% used; 114350651 free inodes.

server4 `/var/tmp`: 106099589120 available bytes; 94.08% used; 114350651 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
