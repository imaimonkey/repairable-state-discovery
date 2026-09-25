# V2R cluster inventory

2026-09-25T06:13:10.481360+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | [] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 318877667328 available bytes; 82.21% used; 112480344 free inodes.

server1 `/home`: 318877667328 available bytes; 82.21% used; 112480344 free inodes.

server1 `/tmp`: 318877667328 available bytes; 82.21% used; 112480344 free inodes.

server1 `/var/tmp`: 318877667328 available bytes; 82.21% used; 112480344 free inodes.

server1 `/mnt/raid5`: 401483534336 available bytes; 98.16% used; 337563077 free inodes.
| server2 | True | [] | [] | reference_compatible=False |

server2 `/`: 22900101120 available bytes; 98.72% used; 110410514 free inodes.

server2 `/home`: 22900101120 available bytes; 98.72% used; 110410514 free inodes.

server2 `/tmp`: 22900101120 available bytes; 98.72% used; 110410514 free inodes.

server2 `/var/tmp`: 22900101120 available bytes; 98.72% used; 110410514 free inodes.

server2 `/mnt/raid5`: 375186624512 available bytes; 97.41% used; 445100525 free inodes.
| server3 | True | [] | [] | reference_compatible=True |

server3 `/`: 84317155328 available bytes; 95.29% used; 114156043 free inodes.

server3 `/home`: 84317155328 available bytes; 95.29% used; 114156043 free inodes.

server3 `/data`: 142534475776 available bytes; 98.03% used; 225814089 free inodes.

server3 `/tmp`: 84317155328 available bytes; 95.29% used; 114156043 free inodes.

server3 `/var/tmp`: 84317155328 available bytes; 95.29% used; 114156043 free inodes.
| server4 | True | ['3'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 105648721920 available bytes; 94.10% used; 114350392 free inodes.

server4 `/home`: 105648721920 available bytes; 94.10% used; 114350392 free inodes.

server4 `/data`: 254655266816 available bytes; 96.48% used; 225023911 free inodes.

server4 `/tmp`: 105648721920 available bytes; 94.10% used; 114350392 free inodes.

server4 `/var/tmp`: 105648721920 available bytes; 94.10% used; 114350392 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
