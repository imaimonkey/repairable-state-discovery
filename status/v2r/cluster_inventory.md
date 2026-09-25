# V2R cluster inventory

2026-09-25T00:08:46.130194+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | [] | ['/tmp', '/var/tmp'] |

server1 `/`: 319089106944 available bytes; 82.20% used; 112480786 free inodes.

server1 `/home`: 319089106944 available bytes; 82.20% used; 112480786 free inodes.

server1 `/tmp`: 319089106944 available bytes; 82.20% used; 112480786 free inodes.

server1 `/var/tmp`: 319089106944 available bytes; 82.20% used; 112480786 free inodes.

server1 `/mnt/raid5`: 416894439424 available bytes; 98.09% used; 337622359 free inodes.
| server2 | True | [] | [] |

server2 `/`: 23094738944 available bytes; 98.71% used; 110410784 free inodes.

server2 `/home`: 23094738944 available bytes; 98.71% used; 110410784 free inodes.

server2 `/tmp`: 23094738944 available bytes; 98.71% used; 110410784 free inodes.

server2 `/var/tmp`: 23094738944 available bytes; 98.71% used; 110410784 free inodes.

server2 `/mnt/raid5`: 487142858752 available bytes; 96.63% used; 445163540 free inodes.
| server3 | True | [] | [] |

server3 `/`: 84352991232 available bytes; 95.29% used; 114156083 free inodes.

server3 `/home`: 84352991232 available bytes; 95.29% used; 114156083 free inodes.

server3 `/data`: 149257900032 available bytes; 97.94% used; 225813847 free inodes.

server3 `/tmp`: 84352991232 available bytes; 95.29% used; 114156083 free inodes.

server3 `/var/tmp`: 84352991232 available bytes; 95.29% used; 114156083 free inodes.
| server4 | True | ['0', '5', '7'] | ['/tmp', '/var/tmp'] |

server4 `/`: 105797931008 available bytes; 94.10% used; 114348297 free inodes.

server4 `/home`: 105797931008 available bytes; 94.10% used; 114348297 free inodes.

server4 `/data`: 58284605440 available bytes; 99.19% used; 225089263 free inodes.

server4 `/tmp`: 105797931008 available bytes; 94.10% used; 114348297 free inodes.

server4 `/var/tmp`: 105797931008 available bytes; 94.10% used; 114348297 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
