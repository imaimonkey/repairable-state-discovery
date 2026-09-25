# V2R cluster inventory

2026-09-25T12:46:36.873984+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | [] | ['/tmp', '/var/tmp'] |

server1 `/`: 319118725120 available bytes; 82.20% used; 112477583 free inodes.

server1 `/home`: 319118725120 available bytes; 82.20% used; 112477583 free inodes.

server1 `/tmp`: 319118725120 available bytes; 82.20% used; 112477583 free inodes.

server1 `/var/tmp`: 319118725120 available bytes; 82.20% used; 112477583 free inodes.

server1 `/mnt/raid5`: 364247547904 available bytes; 98.33% used; 337548044 free inodes.
| server2 | True | ['2', '3', '4', '5', '6'] | [] |

server2 `/`: 20264267776 available bytes; 98.87% used; 110409427 free inodes.

server2 `/home`: 20264267776 available bytes; 98.87% used; 110409427 free inodes.

server2 `/tmp`: 20264267776 available bytes; 98.87% used; 110409427 free inodes.

server2 `/var/tmp`: 20264267776 available bytes; 98.87% used; 110409427 free inodes.

server2 `/mnt/raid5`: 324646371328 available bytes; 97.76% used; 445078998 free inodes.
| server3 | True | [] | [] |

server3 `/`: 84208115712 available bytes; 95.30% used; 114154972 free inodes.

server3 `/home`: 84208115712 available bytes; 95.30% used; 114154972 free inodes.

server3 `/data`: 142275088384 available bytes; 98.03% used; 225810946 free inodes.

server3 `/tmp`: 84208115712 available bytes; 95.30% used; 114154972 free inodes.

server3 `/var/tmp`: 84208115712 available bytes; 95.30% used; 114154972 free inodes.
| server4 | True | [] | ['/tmp', '/var/tmp'] |

server4 `/`: 105665601536 available bytes; 94.10% used; 114349707 free inodes.

server4 `/home`: 105665601536 available bytes; 94.10% used; 114349707 free inodes.

server4 `/data`: 232021295104 available bytes; 96.79% used; 224961861 free inodes.

server4 `/tmp`: 105665601536 available bytes; 94.10% used; 114349707 free inodes.

server4 `/var/tmp`: 105665601536 available bytes; 94.10% used; 114349707 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
