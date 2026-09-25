# V2R cluster inventory

2026-09-25T02:47:20.087499+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | [] | ['/tmp', '/var/tmp'] |

server1 `/`: 318959616000 available bytes; 82.21% used; 112480441 free inodes.

server1 `/home`: 318959616000 available bytes; 82.21% used; 112480441 free inodes.

server1 `/tmp`: 318959616000 available bytes; 82.21% used; 112480441 free inodes.

server1 `/var/tmp`: 318959616000 available bytes; 82.21% used; 112480441 free inodes.

server1 `/mnt/raid5`: 416178282496 available bytes; 98.09% used; 337603925 free inodes.
| server2 | True | [] | [] |

server2 `/`: 23006191616 available bytes; 98.72% used; 110410439 free inodes.

server2 `/home`: 23006191616 available bytes; 98.72% used; 110410439 free inodes.

server2 `/tmp`: 23006191616 available bytes; 98.72% used; 110410439 free inodes.

server2 `/var/tmp`: 23006191616 available bytes; 98.72% used; 110410439 free inodes.

server2 `/mnt/raid5`: 482579017728 available bytes; 96.67% used; 445113066 free inodes.
| server3 | True | [] | [] |

server3 `/`: 84350054400 available bytes; 95.29% used; 114156075 free inodes.

server3 `/home`: 84350054400 available bytes; 95.29% used; 114156075 free inodes.

server3 `/data`: 145249959936 available bytes; 97.99% used; 225810911 free inodes.

server3 `/tmp`: 84350054400 available bytes; 95.29% used; 114156075 free inodes.

server3 `/var/tmp`: 84350054400 available bytes; 95.29% used; 114156075 free inodes.
| server4 | True | ['0', '1', '2', '3', '4', '5', '6', '7'] | ['/tmp', '/var/tmp'] |

server4 `/`: 101969174528 available bytes; 94.31% used; 114350975 free inodes.

server4 `/home`: 101969174528 available bytes; 94.31% used; 114350975 free inodes.

server4 `/data`: 58925932544 available bytes; 99.19% used; 224968791 free inodes.

server4 `/tmp`: 101969174528 available bytes; 94.31% used; 114350975 free inodes.

server4 `/var/tmp`: 101969174528 available bytes; 94.31% used; 114350975 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
