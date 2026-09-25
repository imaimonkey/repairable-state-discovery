# V2R cluster inventory

2026-09-25T06:29:04.072675+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | [] | ['/tmp', '/var/tmp'] |

server1 `/`: 318880231424 available bytes; 82.21% used; 112480350 free inodes.

server1 `/home`: 318880231424 available bytes; 82.21% used; 112480350 free inodes.

server1 `/tmp`: 318880231424 available bytes; 82.21% used; 112480350 free inodes.

server1 `/var/tmp`: 318880231424 available bytes; 82.21% used; 112480350 free inodes.

server1 `/mnt/raid5`: 399811710976 available bytes; 98.17% used; 337561445 free inodes.
| server2 | True | [] | [] |

server2 `/`: 22896861184 available bytes; 98.72% used; 110410520 free inodes.

server2 `/home`: 22896861184 available bytes; 98.72% used; 110410520 free inodes.

server2 `/tmp`: 22896861184 available bytes; 98.72% used; 110410520 free inodes.

server2 `/var/tmp`: 22896861184 available bytes; 98.72% used; 110410520 free inodes.

server2 `/mnt/raid5`: 370601668608 available bytes; 97.44% used; 445099670 free inodes.
| server3 | True | [] | [] |

server3 `/`: 84315303936 available bytes; 95.29% used; 114156029 free inodes.

server3 `/home`: 84315303936 available bytes; 95.29% used; 114156029 free inodes.

server3 `/data`: 142530932736 available bytes; 98.03% used; 225813807 free inodes.

server3 `/tmp`: 84315303936 available bytes; 95.29% used; 114156029 free inodes.

server3 `/var/tmp`: 84315303936 available bytes; 95.29% used; 114156029 free inodes.
| server4 | True | ['3'] | ['/tmp', '/var/tmp'] |

server4 `/`: 105648246784 available bytes; 94.10% used; 114350390 free inodes.

server4 `/home`: 105648246784 available bytes; 94.10% used; 114350390 free inodes.

server4 `/data`: 253850636288 available bytes; 96.49% used; 225020896 free inodes.

server4 `/tmp`: 105648246784 available bytes; 94.10% used; 114350390 free inodes.

server4 `/var/tmp`: 105648246784 available bytes; 94.10% used; 114350390 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
