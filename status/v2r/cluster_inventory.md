# V2R cluster inventory

2026-09-24T23:33:13.198296+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | [] | ['/tmp', '/var/tmp'] |

server1 `/`: 319012315136 available bytes; 82.20% used; 112480782 free inodes.

server1 `/home`: 319012315136 available bytes; 82.20% used; 112480782 free inodes.

server1 `/tmp`: 319012315136 available bytes; 82.20% used; 112480782 free inodes.

server1 `/var/tmp`: 319012315136 available bytes; 82.20% used; 112480782 free inodes.

server1 `/mnt/raid5`: 415223922688 available bytes; 98.10% used; 337612851 free inodes.
| server2 | True | [] | [] |

server2 `/`: 23114358784 available bytes; 98.71% used; 110410808 free inodes.

server2 `/home`: 23114358784 available bytes; 98.71% used; 110410808 free inodes.

server2 `/tmp`: 23114358784 available bytes; 98.71% used; 110410808 free inodes.

server2 `/var/tmp`: 23114358784 available bytes; 98.71% used; 110410808 free inodes.

server2 `/mnt/raid5`: 486301147136 available bytes; 96.64% used; 445151203 free inodes.
| server3 | True | [] | [] |

server3 `/`: 84369014784 available bytes; 95.29% used; 114156083 free inodes.

server3 `/home`: 84369014784 available bytes; 95.29% used; 114156083 free inodes.

server3 `/data`: 148155932672 available bytes; 97.95% used; 225800859 free inodes.

server3 `/tmp`: 84369014784 available bytes; 95.29% used; 114156083 free inodes.

server3 `/var/tmp`: 84369014784 available bytes; 95.29% used; 114156083 free inodes.
| server4 | True | ['3', '7'] | ['/tmp', '/var/tmp'] |

server4 `/`: 105799516160 available bytes; 94.10% used; 114348314 free inodes.

server4 `/home`: 105799516160 available bytes; 94.10% used; 114348314 free inodes.

server4 `/data`: 61213163520 available bytes; 99.15% used; 225142956 free inodes.

server4 `/tmp`: 105799516160 available bytes; 94.10% used; 114348314 free inodes.

server4 `/var/tmp`: 105799516160 available bytes; 94.10% used; 114348314 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
