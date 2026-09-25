# V2R cluster inventory

2026-09-25T05:10:33.982928+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | [] | ['/tmp', '/var/tmp'] |

server1 `/`: 318895153152 available bytes; 82.21% used; 112480296 free inodes.

server1 `/home`: 318895153152 available bytes; 82.21% used; 112480296 free inodes.

server1 `/tmp`: 318895153152 available bytes; 82.21% used; 112480296 free inodes.

server1 `/var/tmp`: 318895153152 available bytes; 82.21% used; 112480296 free inodes.

server1 `/mnt/raid5`: 408592404480 available bytes; 98.13% used; 337570744 free inodes.
| server2 | True | [] | [] |

server2 `/`: 22930214912 available bytes; 98.72% used; 110410436 free inodes.

server2 `/home`: 22930214912 available bytes; 98.72% used; 110410436 free inodes.

server2 `/tmp`: 22930214912 available bytes; 98.72% used; 110410436 free inodes.

server2 `/var/tmp`: 22930214912 available bytes; 98.72% used; 110410436 free inodes.

server2 `/mnt/raid5`: 461792153600 available bytes; 96.81% used; 445108979 free inodes.
| server3 | True | ['0'] | [] |

server3 `/`: 84339187712 available bytes; 95.29% used; 114156074 free inodes.

server3 `/home`: 84339187712 available bytes; 95.29% used; 114156074 free inodes.

server3 `/data`: 142794383360 available bytes; 98.03% used; 225815304 free inodes.

server3 `/tmp`: 84339187712 available bytes; 95.29% used; 114156074 free inodes.

server3 `/var/tmp`: 84339187712 available bytes; 95.29% used; 114156074 free inodes.
| server4 | True | ['6', '7'] | ['/tmp', '/var/tmp'] |

server4 `/`: 105659035648 available bytes; 94.10% used; 114350409 free inodes.

server4 `/home`: 105659035648 available bytes; 94.10% used; 114350409 free inodes.

server4 `/data`: 27927986176 available bytes; 99.61% used; 224960622 free inodes.

server4 `/tmp`: 105659035648 available bytes; 94.10% used; 114350409 free inodes.

server4 `/var/tmp`: 105659035648 available bytes; 94.10% used; 114350409 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
