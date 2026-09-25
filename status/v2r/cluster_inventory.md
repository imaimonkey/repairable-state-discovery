# V2R cluster inventory

2026-09-25T21:34:32.573439+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | ['4', '6', '7'] | ['/tmp', '/var/tmp'] |

server1 `/`: 318702137344 available bytes; 82.22% used; 112476318 free inodes.

server1 `/home`: 318702137344 available bytes; 82.22% used; 112476318 free inodes.

server1 `/tmp`: 318702137344 available bytes; 82.22% used; 112476318 free inodes.

server1 `/var/tmp`: 318702137344 available bytes; 82.22% used; 112476318 free inodes.

server1 `/mnt/raid5`: 360518975488 available bytes; 98.35% used; 337539260 free inodes.
| server2 | True | ['6'] | [] |

server2 `/`: 22905327616 available bytes; 98.72% used; 110405682 free inodes.

server2 `/home`: 22905327616 available bytes; 98.72% used; 110405682 free inodes.

server2 `/tmp`: 22905327616 available bytes; 98.72% used; 110405682 free inodes.

server2 `/var/tmp`: 22905327616 available bytes; 98.72% used; 110405682 free inodes.

server2 `/mnt/raid5`: 301122187264 available bytes; 97.92% used; 445054625 free inodes.
| server3 | True | [] | [] |

server3 `/`: 84367835136 available bytes; 95.29% used; 114152628 free inodes.

server3 `/home`: 84367835136 available bytes; 95.29% used; 114152628 free inodes.

server3 `/data`: 125893447680 available bytes; 98.26% used; 225806898 free inodes.

server3 `/tmp`: 84367835136 available bytes; 95.29% used; 114152628 free inodes.

server3 `/var/tmp`: 84367835136 available bytes; 95.29% used; 114152628 free inodes.
| server4 | True | ['3', '7'] | ['/tmp', '/var/tmp'] |

server4 `/`: 105388912640 available bytes; 94.12% used; 114347331 free inodes.

server4 `/home`: 105388912640 available bytes; 94.12% used; 114347331 free inodes.

server4 `/data`: 216842260480 available bytes; 97.00% used; 224919919 free inodes.

server4 `/tmp`: 105388912640 available bytes; 94.12% used; 114347331 free inodes.

server4 `/var/tmp`: 105388912640 available bytes; 94.12% used; 114347331 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
