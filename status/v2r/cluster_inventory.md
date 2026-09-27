# V2R cluster inventory

2026-09-27T00:55:45.765784+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | ['2', '3', '4', '5', '6', '7'] | ['/tmp', '/var/tmp'] |

server1 `/`: 315158368256 available bytes; 82.42% used; 112443457 free inodes.

server1 `/home`: 315158368256 available bytes; 82.42% used; 112443457 free inodes.

server1 `/tmp`: 315158368256 available bytes; 82.42% used; 112443457 free inodes.

server1 `/var/tmp`: 315158368256 available bytes; 82.42% used; 112443457 free inodes.

server1 `/mnt/raid5`: 637563486208 available bytes; 97.08% used; 337405789 free inodes.
| server2 | True | [] | [] |

server2 `/`: 17632534528 available bytes; 99.02% used; 110365003 free inodes.

server2 `/home`: 17632534528 available bytes; 99.02% used; 110365003 free inodes.

server2 `/tmp`: 17632534528 available bytes; 99.02% used; 110365003 free inodes.

server2 `/var/tmp`: 17632534528 available bytes; 99.02% used; 110365003 free inodes.

server2 `/mnt/raid5`: 584250679296 available bytes; 95.96% used; 444887540 free inodes.
| server3 | True | ['0', '3'] | [] |

server3 `/`: 79500742656 available bytes; 95.56% used; 114068702 free inodes.

server3 `/home`: 79500742656 available bytes; 95.56% used; 114068702 free inodes.

server3 `/data`: 1342484746240 available bytes; 81.45% used; 225764077 free inodes.

server3 `/tmp`: 79500742656 available bytes; 95.56% used; 114068702 free inodes.

server3 `/var/tmp`: 79500742656 available bytes; 95.56% used; 114068702 free inodes.
| server4 | True | ['3', '6', '7'] | ['/tmp', '/var/tmp'] |

server4 `/`: 105878663168 available bytes; 94.09% used; 114347835 free inodes.

server4 `/home`: 105878663168 available bytes; 94.09% used; 114347835 free inodes.

server4 `/data`: 406586769408 available bytes; 94.38% used; 224782996 free inodes.

server4 `/tmp`: 105878663168 available bytes; 94.09% used; 114347835 free inodes.

server4 `/var/tmp`: 105878663168 available bytes; 94.09% used; 114347835 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
