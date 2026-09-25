# V2R cluster inventory

2026-09-25T21:33:01.011228+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | ['0', '4', '6', '7'] | ['/tmp', '/var/tmp'] |

server1 `/`: 318702596096 available bytes; 82.22% used; 112476331 free inodes.

server1 `/home`: 318702596096 available bytes; 82.22% used; 112476331 free inodes.

server1 `/tmp`: 318702596096 available bytes; 82.22% used; 112476331 free inodes.

server1 `/var/tmp`: 318702596096 available bytes; 82.22% used; 112476331 free inodes.

server1 `/mnt/raid5`: 367405469696 available bytes; 98.31% used; 337539287 free inodes.
| server2 | True | ['6'] | [] |

server2 `/`: 22905888768 available bytes; 98.72% used; 110405682 free inodes.

server2 `/home`: 22905888768 available bytes; 98.72% used; 110405682 free inodes.

server2 `/tmp`: 22905888768 available bytes; 98.72% used; 110405682 free inodes.

server2 `/var/tmp`: 22905888768 available bytes; 98.72% used; 110405682 free inodes.

server2 `/mnt/raid5`: 301160943616 available bytes; 97.92% used; 445054750 free inodes.
| server3 | True | [] | [] |

server3 `/`: 84368154624 available bytes; 95.29% used; 114152624 free inodes.

server3 `/home`: 84368154624 available bytes; 95.29% used; 114152624 free inodes.

server3 `/data`: 125897183232 available bytes; 98.26% used; 225806935 free inodes.

server3 `/tmp`: 84368154624 available bytes; 95.29% used; 114152624 free inodes.

server3 `/var/tmp`: 84368154624 available bytes; 95.29% used; 114152624 free inodes.
| server4 | True | ['3', '7'] | ['/tmp', '/var/tmp'] |

server4 `/`: 105388941312 available bytes; 94.12% used; 114347331 free inodes.

server4 `/home`: 105388941312 available bytes; 94.12% used; 114347331 free inodes.

server4 `/data`: 216842895360 available bytes; 97.00% used; 224919925 free inodes.

server4 `/tmp`: 105388941312 available bytes; 94.12% used; 114347331 free inodes.

server4 `/var/tmp`: 105388941312 available bytes; 94.12% used; 114347331 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
