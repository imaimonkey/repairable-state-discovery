# V2R cluster inventory

2026-09-25T21:46:46.073786+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | ['4', '6', '7'] | ['/tmp', '/var/tmp'] |

server1 `/`: 318706974720 available bytes; 82.22% used; 112476302 free inodes.

server1 `/home`: 318706974720 available bytes; 82.22% used; 112476302 free inodes.

server1 `/tmp`: 318706974720 available bytes; 82.22% used; 112476302 free inodes.

server1 `/var/tmp`: 318706974720 available bytes; 82.22% used; 112476302 free inodes.

server1 `/mnt/raid5`: 360323129344 available bytes; 98.35% used; 337539156 free inodes.
| server2 | True | [] | [] |

server2 `/`: 22899077120 available bytes; 98.72% used; 110405682 free inodes.

server2 `/home`: 22899077120 available bytes; 98.72% used; 110405682 free inodes.

server2 `/tmp`: 22899077120 available bytes; 98.72% used; 110405682 free inodes.

server2 `/var/tmp`: 22899077120 available bytes; 98.72% used; 110405682 free inodes.

server2 `/mnt/raid5`: 300770697216 available bytes; 97.92% used; 445053996 free inodes.
| server3 | True | [] | [] |

server3 `/`: 84368584704 available bytes; 95.29% used; 114152634 free inodes.

server3 `/home`: 84368584704 available bytes; 95.29% used; 114152634 free inodes.

server3 `/data`: 125887750144 available bytes; 98.26% used; 225806714 free inodes.

server3 `/tmp`: 84368584704 available bytes; 95.29% used; 114152634 free inodes.

server3 `/var/tmp`: 84368584704 available bytes; 95.29% used; 114152634 free inodes.
| server4 | True | ['3', '7'] | ['/tmp', '/var/tmp'] |

server4 `/`: 105388507136 available bytes; 94.12% used; 114347329 free inodes.

server4 `/home`: 105388507136 available bytes; 94.12% used; 114347329 free inodes.

server4 `/data`: 215895490560 available bytes; 97.02% used; 224919331 free inodes.

server4 `/tmp`: 105388507136 available bytes; 94.12% used; 114347329 free inodes.

server4 `/var/tmp`: 105388507136 available bytes; 94.12% used; 114347329 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
