# V2R cluster inventory

2026-09-24T13:45:08.373277+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | [] | ['/tmp', '/var/tmp'] |

server1 `/`: 324031647744 available bytes; 81.92% used; 112481506 free inodes.

server1 `/home`: 324031647744 available bytes; 81.92% used; 112481506 free inodes.

server1 `/tmp`: 324031647744 available bytes; 81.92% used; 112481506 free inodes.

server1 `/var/tmp`: 324031647744 available bytes; 81.92% used; 112481506 free inodes.

server1 `/mnt/raid5`: 416997814272 available bytes; 98.09% used; 337673461 free inodes.
| server2 | True | ['7'] | [] |

server2 `/`: 57506557952 available bytes; 96.79% used; 110428566 free inodes.

server2 `/home`: 57506557952 available bytes; 96.79% used; 110428566 free inodes.

server2 `/tmp`: 57506557952 available bytes; 96.79% used; 110428566 free inodes.

server2 `/var/tmp`: 57506557952 available bytes; 96.79% used; 110428566 free inodes.

server2 `/mnt/raid5`: 506172256256 available bytes; 96.50% used; 445169329 free inodes.
| server3 | True | [] | [] |

server3 `/`: 85069643776 available bytes; 95.25% used; 114189944 free inodes.

server3 `/home`: 85069643776 available bytes; 95.25% used; 114189944 free inodes.

server3 `/data`: 161150312448 available bytes; 97.77% used; 225802864 free inodes.

server3 `/tmp`: 85069643776 available bytes; 95.25% used; 114189944 free inodes.

server3 `/var/tmp`: 85069643776 available bytes; 95.25% used; 114189944 free inodes.
| server4 | True | [] | ['/tmp', '/var/tmp'] |

server4 `/`: 105760755712 available bytes; 94.10% used; 114348729 free inodes.

server4 `/home`: 105760755712 available bytes; 94.10% used; 114348729 free inodes.

server4 `/data`: 90041196544 available bytes; 98.76% used; 225257170 free inodes.

server4 `/tmp`: 105760755712 available bytes; 94.10% used; 114348729 free inodes.

server4 `/var/tmp`: 105760755712 available bytes; 94.10% used; 114348729 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
