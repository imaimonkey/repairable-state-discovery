# V2R cluster inventory

2026-09-25T03:05:47.899634+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | [] | ['/tmp', '/var/tmp'] |

server1 `/`: 318941646848 available bytes; 82.21% used; 112480388 free inodes.

server1 `/home`: 318941646848 available bytes; 82.21% used; 112480388 free inodes.

server1 `/tmp`: 318941646848 available bytes; 82.21% used; 112480388 free inodes.

server1 `/var/tmp`: 318941646848 available bytes; 82.21% used; 112480388 free inodes.

server1 `/mnt/raid5`: 416134750208 available bytes; 98.09% used; 337601763 free inodes.
| server2 | True | [] | [] |

server2 `/`: 22993661952 available bytes; 98.72% used; 110410440 free inodes.

server2 `/home`: 22993661952 available bytes; 98.72% used; 110410440 free inodes.

server2 `/tmp`: 22993661952 available bytes; 98.72% used; 110410440 free inodes.

server2 `/var/tmp`: 22993661952 available bytes; 98.72% used; 110410440 free inodes.

server2 `/mnt/raid5`: 465926332416 available bytes; 96.78% used; 445112752 free inodes.
| server3 | True | [] | [] |

server3 `/`: 84344901632 available bytes; 95.29% used; 114156075 free inodes.

server3 `/home`: 84344901632 available bytes; 95.29% used; 114156075 free inodes.

server3 `/data`: 144926470144 available bytes; 98.00% used; 225810357 free inodes.

server3 `/tmp`: 84344901632 available bytes; 95.29% used; 114156075 free inodes.

server3 `/var/tmp`: 84344901632 available bytes; 95.29% used; 114156075 free inodes.
| server4 | True | ['2', '3', '6', '7'] | ['/tmp', '/var/tmp'] |

server4 `/`: 105693093888 available bytes; 94.10% used; 114350903 free inodes.

server4 `/home`: 105693093888 available bytes; 94.10% used; 114350903 free inodes.

server4 `/data`: 50258919424 available bytes; 99.31% used; 224967430 free inodes.

server4 `/tmp`: 105693093888 available bytes; 94.10% used; 114350903 free inodes.

server4 `/var/tmp`: 105693093888 available bytes; 94.10% used; 114350903 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
