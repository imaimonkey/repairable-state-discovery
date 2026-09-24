# V2R cluster inventory

2026-09-24T02:30:36.477714+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | ['7'] | ['/tmp', '/var/tmp'] |

server1 `/`: 325385187328 available bytes; 81.85% used; 112498865 free inodes.

server1 `/home`: 325385187328 available bytes; 81.85% used; 112498865 free inodes.

server1 `/tmp`: 325385187328 available bytes; 81.85% used; 112498865 free inodes.

server1 `/var/tmp`: 325385187328 available bytes; 81.85% used; 112498865 free inodes.

server1 `/mnt/raid5`: 645275484160 available bytes; 97.04% used; 337733214 free inodes.
| server2 | True | [] | [] |

server2 `/`: 40891285504 available bytes; 97.72% used; 110431534 free inodes.

server2 `/home`: 40891285504 available bytes; 97.72% used; 110431534 free inodes.

server2 `/tmp`: 40891285504 available bytes; 97.72% used; 110431534 free inodes.

server2 `/var/tmp`: 40891285504 available bytes; 97.72% used; 110431534 free inodes.

server2 `/mnt/raid5`: 528458612736 available bytes; 96.35% used; 445199633 free inodes.
| server3 | True | [] | ['/tmp', '/var/tmp'] |

server3 `/`: 291856695296 available bytes; 83.71% used; 114163142 free inodes.

server3 `/home`: 291856695296 available bytes; 83.71% used; 114163142 free inodes.

server3 `/data`: 39756505088 available bytes; 99.45% used; 225846369 free inodes.

server3 `/tmp`: 291856695296 available bytes; 83.71% used; 114163142 free inodes.

server3 `/var/tmp`: 291856695296 available bytes; 83.71% used; 114163142 free inodes.
| server4 | True | ['3', '7'] | ['/tmp', '/var/tmp'] |

server4 `/`: 106003714048 available bytes; 94.08% used; 114349842 free inodes.

server4 `/home`: 106003714048 available bytes; 94.08% used; 114349842 free inodes.

server4 `/data`: 289738186752 available bytes; 96.00% used; 225387512 free inodes.

server4 `/tmp`: 106003714048 available bytes; 94.08% used; 114349842 free inodes.

server4 `/var/tmp`: 106003714048 available bytes; 94.08% used; 114349842 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
