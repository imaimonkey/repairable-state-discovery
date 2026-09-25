# V2R cluster inventory

2026-09-25T06:24:28.557810+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | [] | ['/tmp', '/var/tmp'] |

server1 `/`: 318880460800 available bytes; 82.21% used; 112480350 free inodes.

server1 `/home`: 318880460800 available bytes; 82.21% used; 112480350 free inodes.

server1 `/tmp`: 318880460800 available bytes; 82.21% used; 112480350 free inodes.

server1 `/var/tmp`: 318880460800 available bytes; 82.21% used; 112480350 free inodes.

server1 `/mnt/raid5`: 401444728832 available bytes; 98.16% used; 337561714 free inodes.
| server2 | True | [] | [] |

server2 `/`: 22893854720 available bytes; 98.72% used; 110410514 free inodes.

server2 `/home`: 22893854720 available bytes; 98.72% used; 110410514 free inodes.

server2 `/tmp`: 22893854720 available bytes; 98.72% used; 110410514 free inodes.

server2 `/var/tmp`: 22893854720 available bytes; 98.72% used; 110410514 free inodes.

server2 `/mnt/raid5`: 372786171904 available bytes; 97.42% used; 445099844 free inodes.
| server3 | True | [] | [] |

server3 `/`: 84316114944 available bytes; 95.29% used; 114156039 free inodes.

server3 `/home`: 84316114944 available bytes; 95.29% used; 114156039 free inodes.

server3 `/data`: 142532108288 available bytes; 98.03% used; 225813873 free inodes.

server3 `/tmp`: 84316114944 available bytes; 95.29% used; 114156039 free inodes.

server3 `/var/tmp`: 84316114944 available bytes; 95.29% used; 114156039 free inodes.
| server4 | True | ['3'] | ['/tmp', '/var/tmp'] |

server4 `/`: 105648390144 available bytes; 94.10% used; 114350390 free inodes.

server4 `/home`: 105648390144 available bytes; 94.10% used; 114350390 free inodes.

server4 `/data`: 254600093696 available bytes; 96.48% used; 225021711 free inodes.

server4 `/tmp`: 105648390144 available bytes; 94.10% used; 114350390 free inodes.

server4 `/var/tmp`: 105648390144 available bytes; 94.10% used; 114350390 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
