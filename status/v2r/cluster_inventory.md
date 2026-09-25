# V2R cluster inventory

2026-09-25T01:11:56.126268+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | [] | ['/tmp', '/var/tmp'] |

server1 `/`: 319076855808 available bytes; 82.20% used; 112480767 free inodes.

server1 `/home`: 319076855808 available bytes; 82.20% used; 112480767 free inodes.

server1 `/tmp`: 319076855808 available bytes; 82.20% used; 112480767 free inodes.

server1 `/var/tmp`: 319076855808 available bytes; 82.20% used; 112480767 free inodes.

server1 `/mnt/raid5`: 416522338304 available bytes; 98.09% used; 337615076 free inodes.
| server2 | True | ['2'] | [] |

server2 `/`: 23059988480 available bytes; 98.71% used; 110410772 free inodes.

server2 `/home`: 23059988480 available bytes; 98.71% used; 110410772 free inodes.

server2 `/tmp`: 23059988480 available bytes; 98.71% used; 110410772 free inodes.

server2 `/var/tmp`: 23059988480 available bytes; 98.71% used; 110410772 free inodes.

server2 `/mnt/raid5`: 477483442176 available bytes; 96.70% used; 445162062 free inodes.
| server3 | True | [] | [] |

server3 `/`: 84352655360 available bytes; 95.29% used; 114156085 free inodes.

server3 `/home`: 84352655360 available bytes; 95.29% used; 114156085 free inodes.

server3 `/data`: 147005734912 available bytes; 97.97% used; 225812663 free inodes.

server3 `/tmp`: 84352655360 available bytes; 95.29% used; 114156085 free inodes.

server3 `/var/tmp`: 84352655360 available bytes; 95.29% used; 114156085 free inodes.
| server4 | True | ['0', '1', '4', '5', '7'] | ['/tmp', '/var/tmp'] |

server4 `/`: 105779421184 available bytes; 94.10% used; 114348299 free inodes.

server4 `/home`: 105779421184 available bytes; 94.10% used; 114348299 free inodes.

server4 `/data`: 53330149376 available bytes; 99.26% used; 225030780 free inodes.

server4 `/tmp`: 105779421184 available bytes; 94.10% used; 114348299 free inodes.

server4 `/var/tmp`: 105779421184 available bytes; 94.10% used; 114348299 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
