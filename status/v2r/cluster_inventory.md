# V2R cluster inventory

2026-09-25T01:10:21.958615+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | [] | ['/tmp', '/var/tmp'] |

server1 `/`: 319077343232 available bytes; 82.20% used; 112480767 free inodes.

server1 `/home`: 319077343232 available bytes; 82.20% used; 112480767 free inodes.

server1 `/tmp`: 319077343232 available bytes; 82.20% used; 112480767 free inodes.

server1 `/var/tmp`: 319077343232 available bytes; 82.20% used; 112480767 free inodes.

server1 `/mnt/raid5`: 416526016512 available bytes; 98.09% used; 337615256 free inodes.
| server2 | True | ['2'] | [] |

server2 `/`: 23059537920 available bytes; 98.71% used; 110410770 free inodes.

server2 `/home`: 23059537920 available bytes; 98.71% used; 110410770 free inodes.

server2 `/tmp`: 23059537920 available bytes; 98.71% used; 110410770 free inodes.

server2 `/var/tmp`: 23059537920 available bytes; 98.71% used; 110410770 free inodes.

server2 `/mnt/raid5`: 498175234048 available bytes; 96.56% used; 445162125 free inodes.
| server3 | True | [] | [] |

server3 `/`: 84352942080 available bytes; 95.29% used; 114156085 free inodes.

server3 `/home`: 84352942080 available bytes; 95.29% used; 114156085 free inodes.

server3 `/data`: 147025018880 available bytes; 97.97% used; 225812696 free inodes.

server3 `/tmp`: 84352942080 available bytes; 95.29% used; 114156085 free inodes.

server3 `/var/tmp`: 84352942080 available bytes; 95.29% used; 114156085 free inodes.
| server4 | True | ['0', '1', '4', '5', '7'] | ['/tmp', '/var/tmp'] |

server4 `/`: 105779466240 available bytes; 94.10% used; 114348300 free inodes.

server4 `/home`: 105779466240 available bytes; 94.10% used; 114348300 free inodes.

server4 `/data`: 53341704192 available bytes; 99.26% used; 225030810 free inodes.

server4 `/tmp`: 105779466240 available bytes; 94.10% used; 114348300 free inodes.

server4 `/var/tmp`: 105779466240 available bytes; 94.10% used; 114348300 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
