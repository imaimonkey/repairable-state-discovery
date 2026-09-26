# V2R cluster inventory

2026-09-26T04:22:32.389730+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | ['1', '4', '5', '6', '7'] | ['/tmp', '/var/tmp'] |

server1 `/`: 318409736192 available bytes; 82.24% used; 112476273 free inodes.

server1 `/home`: 318409736192 available bytes; 82.24% used; 112476273 free inodes.

server1 `/tmp`: 318409736192 available bytes; 82.24% used; 112476273 free inodes.

server1 `/var/tmp`: 318409736192 available bytes; 82.24% used; 112476273 free inodes.

server1 `/mnt/raid5`: 330537238528 available bytes; 98.48% used; 337545502 free inodes.
| server2 | True | [] | [] |

server2 `/`: 22939250688 available bytes; 98.72% used; 110406204 free inodes.

server2 `/home`: 22939250688 available bytes; 98.72% used; 110406204 free inodes.

server2 `/tmp`: 22939250688 available bytes; 98.72% used; 110406204 free inodes.

server2 `/var/tmp`: 22939250688 available bytes; 98.72% used; 110406204 free inodes.

server2 `/mnt/raid5`: 285184434176 available bytes; 98.03% used; 445050694 free inodes.
| server3 | True | [] | [] |

server3 `/`: 84141756416 available bytes; 95.30% used; 114148305 free inodes.

server3 `/home`: 84141756416 available bytes; 95.30% used; 114148305 free inodes.

server3 `/data`: 124581634048 available bytes; 98.28% used; 225819649 free inodes.

server3 `/tmp`: 84141756416 available bytes; 95.30% used; 114148305 free inodes.

server3 `/var/tmp`: 84141756416 available bytes; 95.30% used; 114148305 free inodes.
| server4 | True | ['2', '3', '6', '7'] | ['/tmp', '/var/tmp'] |

server4 `/`: 106002649088 available bytes; 94.08% used; 114348208 free inodes.

server4 `/home`: 106002649088 available bytes; 94.08% used; 114348208 free inodes.

server4 `/data`: 107386904576 available bytes; 98.52% used; 224929413 free inodes.

server4 `/tmp`: 106002649088 available bytes; 94.08% used; 114348208 free inodes.

server4 `/var/tmp`: 106002649088 available bytes; 94.08% used; 114348208 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
