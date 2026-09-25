# V2R cluster inventory

2026-09-25T06:02:57.778521+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | [] | ['/tmp', '/var/tmp'] |

server1 `/`: 318874267648 available bytes; 82.21% used; 112480342 free inodes.

server1 `/home`: 318874267648 available bytes; 82.21% used; 112480342 free inodes.

server1 `/tmp`: 318874267648 available bytes; 82.21% used; 112480342 free inodes.

server1 `/var/tmp`: 318874267648 available bytes; 82.21% used; 112480342 free inodes.

server1 `/mnt/raid5`: 407032848384 available bytes; 98.13% used; 337564306 free inodes.
| server2 | True | ['6'] | [] |

server2 `/`: 22901874688 available bytes; 98.72% used; 110410373 free inodes.

server2 `/home`: 22901874688 available bytes; 98.72% used; 110410373 free inodes.

server2 `/tmp`: 22901874688 available bytes; 98.72% used; 110410373 free inodes.

server2 `/var/tmp`: 22901874688 available bytes; 98.72% used; 110410373 free inodes.

server2 `/mnt/raid5`: 386139668480 available bytes; 97.33% used; 445100798 free inodes.
| server3 | True | [] | [] |

server3 `/`: 84317560832 available bytes; 95.29% used; 114156039 free inodes.

server3 `/home`: 84317560832 available bytes; 95.29% used; 114156039 free inodes.

server3 `/data`: 142778707968 available bytes; 98.03% used; 225814245 free inodes.

server3 `/tmp`: 84317560832 available bytes; 95.29% used; 114156039 free inodes.

server3 `/var/tmp`: 84317560832 available bytes; 95.29% used; 114156039 free inodes.
| server4 | True | ['3'] | ['/tmp', '/var/tmp'] |

server4 `/`: 105649037312 available bytes; 94.10% used; 114350386 free inodes.

server4 `/home`: 105649037312 available bytes; 94.10% used; 114350386 free inodes.

server4 `/data`: 256277688320 available bytes; 96.46% used; 225025353 free inodes.

server4 `/tmp`: 105649037312 available bytes; 94.10% used; 114350386 free inodes.

server4 `/var/tmp`: 105649037312 available bytes; 94.10% used; 114350386 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
