# V2R cluster inventory

2026-09-26T06:35:36.234607+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | ['1', '4', '5', '6', '7'] | ['/tmp', '/var/tmp'] |

server1 `/`: 318768865280 available bytes; 82.22% used; 112476272 free inodes.

server1 `/home`: 318768865280 available bytes; 82.22% used; 112476272 free inodes.

server1 `/tmp`: 318768865280 available bytes; 82.22% used; 112476272 free inodes.

server1 `/var/tmp`: 318768865280 available bytes; 82.22% used; 112476272 free inodes.

server1 `/mnt/raid5`: 219542003712 available bytes; 98.99% used; 337539741 free inodes.
| server2 | True | [] | [] |

server2 `/`: 22313799680 available bytes; 98.76% used; 110403833 free inodes.

server2 `/home`: 22313799680 available bytes; 98.76% used; 110403833 free inodes.

server2 `/tmp`: 22313799680 available bytes; 98.76% used; 110403833 free inodes.

server2 `/var/tmp`: 22313799680 available bytes; 98.76% used; 110403833 free inodes.

server2 `/mnt/raid5`: 272850853888 available bytes; 98.11% used; 445028278 free inodes.
| server3 | True | [] | [] |

server3 `/`: 82564358144 available bytes; 95.39% used; 114110887 free inodes.

server3 `/home`: 82564358144 available bytes; 95.39% used; 114110887 free inodes.

server3 `/data`: 123993673728 available bytes; 98.29% used; 225822180 free inodes.

server3 `/tmp`: 82564358144 available bytes; 95.39% used; 114110887 free inodes.

server3 `/var/tmp`: 82564358144 available bytes; 95.39% used; 114110887 free inodes.
| server4 | True | ['2', '3', '6', '7'] | ['/tmp', '/var/tmp'] |

server4 `/`: 106076119040 available bytes; 94.08% used; 114348174 free inodes.

server4 `/home`: 106076119040 available bytes; 94.08% used; 114348174 free inodes.

server4 `/data`: 106039410688 available bytes; 98.53% used; 224923334 free inodes.

server4 `/tmp`: 106076119040 available bytes; 94.08% used; 114348174 free inodes.

server4 `/var/tmp`: 106076119040 available bytes; 94.08% used; 114348174 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
