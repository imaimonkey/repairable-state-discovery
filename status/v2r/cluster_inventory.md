# V2R cluster inventory

2026-09-24T17:44:27.735210+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | ['7'] | ['/tmp', '/var/tmp'] |

server1 `/`: 324007727104 available bytes; 81.92% used; 112481435 free inodes.

server1 `/home`: 324007727104 available bytes; 81.92% used; 112481435 free inodes.

server1 `/tmp`: 324007727104 available bytes; 81.92% used; 112481435 free inodes.

server1 `/var/tmp`: 324007727104 available bytes; 81.92% used; 112481435 free inodes.

server1 `/mnt/raid5`: 416418471936 available bytes; 98.09% used; 337644710 free inodes.
| server2 | True | ['7'] | [] |

server2 `/`: 56905097216 available bytes; 96.83% used; 110412381 free inodes.

server2 `/home`: 56905097216 available bytes; 96.83% used; 110412381 free inodes.

server2 `/tmp`: 56905097216 available bytes; 96.83% used; 110412381 free inodes.

server2 `/var/tmp`: 56905097216 available bytes; 96.83% used; 110412381 free inodes.

server2 `/mnt/raid5`: 498350186496 available bytes; 96.56% used; 445161922 free inodes.
| server3 | True | ['1'] | [] |

server3 `/`: 84408938496 available bytes; 95.29% used; 114156150 free inodes.

server3 `/home`: 84408938496 available bytes; 95.29% used; 114156150 free inodes.

server3 `/data`: 151946989568 available bytes; 97.90% used; 225786545 free inodes.

server3 `/tmp`: 84408938496 available bytes; 95.29% used; 114156150 free inodes.

server3 `/var/tmp`: 84408938496 available bytes; 95.29% used; 114156150 free inodes.
| server4 | True | [] | ['/tmp', '/var/tmp'] |

server4 `/`: 105672585216 available bytes; 94.10% used; 114348559 free inodes.

server4 `/home`: 105672585216 available bytes; 94.10% used; 114348559 free inodes.

server4 `/data`: 89057419264 available bytes; 98.77% used; 225253753 free inodes.

server4 `/tmp`: 105672585216 available bytes; 94.10% used; 114348559 free inodes.

server4 `/var/tmp`: 105672585216 available bytes; 94.10% used; 114348559 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
