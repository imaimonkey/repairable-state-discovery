# V2R cluster inventory

2026-09-25T02:53:28.577795+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | [] | ['/tmp', '/var/tmp'] |

server1 `/`: 318950801408 available bytes; 82.21% used; 112480428 free inodes.

server1 `/home`: 318950801408 available bytes; 82.21% used; 112480428 free inodes.

server1 `/tmp`: 318950801408 available bytes; 82.21% used; 112480428 free inodes.

server1 `/var/tmp`: 318950801408 available bytes; 82.21% used; 112480428 free inodes.

server1 `/mnt/raid5`: 416165732352 available bytes; 98.09% used; 337603212 free inodes.
| server2 | True | [] | [] |

server2 `/`: 22998892544 available bytes; 98.72% used; 110410441 free inodes.

server2 `/home`: 22998892544 available bytes; 98.72% used; 110410441 free inodes.

server2 `/tmp`: 22998892544 available bytes; 98.72% used; 110410441 free inodes.

server2 `/var/tmp`: 22998892544 available bytes; 98.72% used; 110410441 free inodes.

server2 `/mnt/raid5`: 482414034944 available bytes; 96.67% used; 445113408 free inodes.
| server3 | True | [] | [] |

server3 `/`: 84346724352 available bytes; 95.29% used; 114156075 free inodes.

server3 `/home`: 84346724352 available bytes; 95.29% used; 114156075 free inodes.

server3 `/data`: 145145692160 available bytes; 97.99% used; 225810792 free inodes.

server3 `/tmp`: 84346724352 available bytes; 95.29% used; 114156075 free inodes.

server3 `/var/tmp`: 84346724352 available bytes; 95.29% used; 114156075 free inodes.
| server4 | True | ['2', '3', '6', '7'] | ['/tmp', '/var/tmp'] |

server4 `/`: 105693593600 available bytes; 94.10% used; 114350921 free inodes.

server4 `/home`: 105693593600 available bytes; 94.10% used; 114350921 free inodes.

server4 `/data`: 54989344768 available bytes; 99.24% used; 224967542 free inodes.

server4 `/tmp`: 105693593600 available bytes; 94.10% used; 114350921 free inodes.

server4 `/var/tmp`: 105693593600 available bytes; 94.10% used; 114350921 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
