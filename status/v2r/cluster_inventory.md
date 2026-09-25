# V2R cluster inventory

2026-09-25T05:49:04.472841+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | [] | ['/tmp', '/var/tmp'] |

server1 `/`: 318872621056 available bytes; 82.21% used; 112480351 free inodes.

server1 `/home`: 318872621056 available bytes; 82.21% used; 112480351 free inodes.

server1 `/tmp`: 318872621056 available bytes; 82.21% used; 112480351 free inodes.

server1 `/var/tmp`: 318872621056 available bytes; 82.21% used; 112480351 free inodes.

server1 `/mnt/raid5`: 408440598528 available bytes; 98.13% used; 337566008 free inodes.
| server2 | True | [] | [] |

server2 `/`: 22910939136 available bytes; 98.72% used; 110410371 free inodes.

server2 `/home`: 22910939136 available bytes; 98.72% used; 110410371 free inodes.

server2 `/tmp`: 22910939136 available bytes; 98.72% used; 110410371 free inodes.

server2 `/var/tmp`: 22910939136 available bytes; 98.72% used; 110410371 free inodes.

server2 `/mnt/raid5`: 418157006848 available bytes; 97.11% used; 445102085 free inodes.
| server3 | True | [] | [] |

server3 `/`: 84312592384 available bytes; 95.30% used; 114156039 free inodes.

server3 `/home`: 84312592384 available bytes; 95.30% used; 114156039 free inodes.

server3 `/data`: 142777040896 available bytes; 98.03% used; 225814501 free inodes.

server3 `/tmp`: 84312592384 available bytes; 95.30% used; 114156039 free inodes.

server3 `/var/tmp`: 84312592384 available bytes; 95.30% used; 114156039 free inodes.
| server4 | True | ['3'] | ['/tmp', '/var/tmp'] |

server4 `/`: 105649463296 available bytes; 94.10% used; 114350388 free inodes.

server4 `/home`: 105649463296 available bytes; 94.10% used; 114350388 free inodes.

server4 `/data`: 252492410880 available bytes; 96.51% used; 225009205 free inodes.

server4 `/tmp`: 105649463296 available bytes; 94.10% used; 114350388 free inodes.

server4 `/var/tmp`: 105649463296 available bytes; 94.10% used; 114350388 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
