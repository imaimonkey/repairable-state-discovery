# V2R cluster inventory

2026-09-25T04:49:05.890235+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | [] | ['/tmp', '/var/tmp'] |

server1 `/`: 318909001728 available bytes; 82.21% used; 112480364 free inodes.

server1 `/home`: 318909001728 available bytes; 82.21% used; 112480364 free inodes.

server1 `/tmp`: 318909001728 available bytes; 82.21% used; 112480364 free inodes.

server1 `/var/tmp`: 318909001728 available bytes; 82.21% used; 112480364 free inodes.

server1 `/mnt/raid5`: 408675868672 available bytes; 98.13% used; 337589373 free inodes.
| server2 | True | [] | [] |

server2 `/`: 22942339072 available bytes; 98.72% used; 110410440 free inodes.

server2 `/home`: 22942339072 available bytes; 98.72% used; 110410440 free inodes.

server2 `/tmp`: 22942339072 available bytes; 98.72% used; 110410440 free inodes.

server2 `/var/tmp`: 22942339072 available bytes; 98.72% used; 110410440 free inodes.

server2 `/mnt/raid5`: 462453981184 available bytes; 96.80% used; 445109347 free inodes.
| server3 | True | ['3'] | [] |

server3 `/`: 84339224576 available bytes; 95.29% used; 114156090 free inodes.

server3 `/home`: 84339224576 available bytes; 95.29% used; 114156090 free inodes.

server3 `/data`: 143152508928 available bytes; 98.02% used; 225815782 free inodes.

server3 `/tmp`: 84339224576 available bytes; 95.29% used; 114156090 free inodes.

server3 `/var/tmp`: 84339224576 available bytes; 95.29% used; 114156090 free inodes.
| server4 | True | ['6', '7'] | ['/tmp', '/var/tmp'] |

server4 `/`: 105661722624 available bytes; 94.10% used; 114350497 free inodes.

server4 `/home`: 105661722624 available bytes; 94.10% used; 114350497 free inodes.

server4 `/data`: 29551480832 available bytes; 99.59% used; 224961882 free inodes.

server4 `/tmp`: 105661722624 available bytes; 94.10% used; 114350497 free inodes.

server4 `/var/tmp`: 105661722624 available bytes; 94.10% used; 114350497 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
