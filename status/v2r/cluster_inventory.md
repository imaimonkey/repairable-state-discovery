# V2R cluster inventory

2026-09-25T01:41:08.986054+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | [] | ['/tmp', '/var/tmp'] |

server1 `/`: 319076040704 available bytes; 82.20% used; 112480771 free inodes.

server1 `/home`: 319076040704 available bytes; 82.20% used; 112480771 free inodes.

server1 `/tmp`: 319076040704 available bytes; 82.20% used; 112480771 free inodes.

server1 `/var/tmp`: 319076040704 available bytes; 82.20% used; 112480771 free inodes.

server1 `/mnt/raid5`: 416461537280 available bytes; 98.09% used; 337611663 free inodes.
| server2 | True | ['2', '3', '6'] | [] |

server2 `/`: 23043080192 available bytes; 98.71% used; 110410778 free inodes.

server2 `/home`: 23043080192 available bytes; 98.71% used; 110410778 free inodes.

server2 `/tmp`: 23043080192 available bytes; 98.71% used; 110410778 free inodes.

server2 `/var/tmp`: 23043080192 available bytes; 98.71% used; 110410778 free inodes.

server2 `/mnt/raid5`: 490765869056 available bytes; 96.61% used; 445161163 free inodes.
| server3 | True | [] | [] |

server3 `/`: 84353138688 available bytes; 95.29% used; 114156083 free inodes.

server3 `/home`: 84353138688 available bytes; 95.29% used; 114156083 free inodes.

server3 `/data`: 146504241152 available bytes; 97.98% used; 225812088 free inodes.

server3 `/tmp`: 84353138688 available bytes; 95.29% used; 114156083 free inodes.

server3 `/var/tmp`: 84353138688 available bytes; 95.29% used; 114156083 free inodes.
| server4 | True | ['0', '1', '4', '5', '7'] | ['/tmp', '/var/tmp'] |

server4 `/`: 105770172416 available bytes; 94.10% used; 114348287 free inodes.

server4 `/home`: 105770172416 available bytes; 94.10% used; 114348287 free inodes.

server4 `/data`: 53309513728 available bytes; 99.26% used; 225030621 free inodes.

server4 `/tmp`: 105770172416 available bytes; 94.10% used; 114348287 free inodes.

server4 `/var/tmp`: 105770172416 available bytes; 94.10% used; 114348287 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
