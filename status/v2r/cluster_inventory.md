# V2R cluster inventory

2026-09-25T03:48:55.993891+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | [] | ['/tmp', '/var/tmp'] |

server1 `/`: 318937100288 available bytes; 82.21% used; 112480348 free inodes.

server1 `/home`: 318937100288 available bytes; 82.21% used; 112480348 free inodes.

server1 `/tmp`: 318937100288 available bytes; 82.21% used; 112480348 free inodes.

server1 `/var/tmp`: 318937100288 available bytes; 82.21% used; 112480348 free inodes.

server1 `/mnt/raid5`: 415741652992 available bytes; 98.09% used; 337596658 free inodes.
| server2 | True | [] | [] |

server2 `/`: 22973358080 available bytes; 98.72% used; 110410440 free inodes.

server2 `/home`: 22973358080 available bytes; 98.72% used; 110410440 free inodes.

server2 `/tmp`: 22973358080 available bytes; 98.72% used; 110410440 free inodes.

server2 `/var/tmp`: 22973358080 available bytes; 98.72% used; 110410440 free inodes.

server2 `/mnt/raid5`: 464308658176 available bytes; 96.79% used; 445111107 free inodes.
| server3 | True | [] | [] |

server3 `/`: 84341039104 available bytes; 95.29% used; 114156066 free inodes.

server3 `/home`: 84341039104 available bytes; 95.29% used; 114156066 free inodes.

server3 `/data`: 144272773120 available bytes; 98.01% used; 225817055 free inodes.

server3 `/tmp`: 84341039104 available bytes; 95.29% used; 114156066 free inodes.

server3 `/var/tmp`: 84341039104 available bytes; 95.29% used; 114156066 free inodes.
| server4 | True | ['6', '7'] | ['/tmp', '/var/tmp'] |

server4 `/`: 105683296256 available bytes; 94.10% used; 114350901 free inodes.

server4 `/home`: 105683296256 available bytes; 94.10% used; 114350901 free inodes.

server4 `/data`: 38562045952 available bytes; 99.47% used; 224965143 free inodes.

server4 `/tmp`: 105683296256 available bytes; 94.10% used; 114350901 free inodes.

server4 `/var/tmp`: 105683296256 available bytes; 94.10% used; 114350901 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
