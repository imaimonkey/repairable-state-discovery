# V2R cluster inventory

2026-09-25T04:18:07.262874+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | [] | ['/tmp', '/var/tmp'] |

server1 `/`: 318929604608 available bytes; 82.21% used; 112480382 free inodes.

server1 `/home`: 318929604608 available bytes; 82.21% used; 112480382 free inodes.

server1 `/tmp`: 318929604608 available bytes; 82.21% used; 112480382 free inodes.

server1 `/var/tmp`: 318929604608 available bytes; 82.21% used; 112480382 free inodes.

server1 `/mnt/raid5`: 388123869184 available bytes; 98.22% used; 337593151 free inodes.
| server2 | True | [] | [] |

server2 `/`: 22957842432 available bytes; 98.72% used; 110410442 free inodes.

server2 `/home`: 22957842432 available bytes; 98.72% used; 110410442 free inodes.

server2 `/tmp`: 22957842432 available bytes; 98.72% used; 110410442 free inodes.

server2 `/var/tmp`: 22957842432 available bytes; 98.72% used; 110410442 free inodes.

server2 `/mnt/raid5`: 463406485504 available bytes; 96.80% used; 445110312 free inodes.
| server3 | True | [] | [] |

server3 `/`: 84340334592 available bytes; 95.29% used; 114156072 free inodes.

server3 `/home`: 84340334592 available bytes; 95.29% used; 114156072 free inodes.

server3 `/data`: 143790465024 available bytes; 98.01% used; 225816403 free inodes.

server3 `/tmp`: 84340334592 available bytes; 95.29% used; 114156072 free inodes.

server3 `/var/tmp`: 84340334592 available bytes; 95.29% used; 114156072 free inodes.
| server4 | True | ['6', '7'] | ['/tmp', '/var/tmp'] |

server4 `/`: 105673969664 available bytes; 94.10% used; 114350881 free inodes.

server4 `/home`: 105673969664 available bytes; 94.10% used; 114350881 free inodes.

server4 `/data`: 33677832192 available bytes; 99.53% used; 224963710 free inodes.

server4 `/tmp`: 105673969664 available bytes; 94.10% used; 114350881 free inodes.

server4 `/var/tmp`: 105673969664 available bytes; 94.10% used; 114350881 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
