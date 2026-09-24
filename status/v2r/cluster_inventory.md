# V2R cluster inventory

2026-09-24T09:41:41.728783+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | ['7'] | ['/tmp', '/var/tmp'] |

server1 `/`: 324454105088 available bytes; 81.90% used; 112489729 free inodes.

server1 `/home`: 324454105088 available bytes; 81.90% used; 112489729 free inodes.

server1 `/tmp`: 324454105088 available bytes; 81.90% used; 112489729 free inodes.

server1 `/var/tmp`: 324454105088 available bytes; 81.90% used; 112489729 free inodes.

server1 `/mnt/raid5`: 501805273088 available bytes; 97.70% used; 337711967 free inodes.
| server2 | True | [] | [] |

server2 `/`: 57762893824 available bytes; 96.78% used; 110430788 free inodes.

server2 `/home`: 57762893824 available bytes; 96.78% used; 110430788 free inodes.

server2 `/tmp`: 57762893824 available bytes; 96.78% used; 110430788 free inodes.

server2 `/var/tmp`: 57762893824 available bytes; 96.78% used; 110430788 free inodes.

server2 `/mnt/raid5`: 514247024640 available bytes; 96.45% used; 445177297 free inodes.
| server3 | True | [] | [] |

server3 `/`: 85767196672 available bytes; 95.21% used; 114196482 free inodes.

server3 `/home`: 85767196672 available bytes; 95.21% used; 114196482 free inodes.

server3 `/data`: 165702692864 available bytes; 97.71% used; 225819964 free inodes.

server3 `/tmp`: 85767196672 available bytes; 95.21% used; 114196482 free inodes.

server3 `/var/tmp`: 85767196672 available bytes; 95.21% used; 114196482 free inodes.
| server4 | True | [] | ['/tmp', '/var/tmp'] |

server4 `/`: 105757134848 available bytes; 94.10% used; 114349034 free inodes.

server4 `/home`: 105757134848 available bytes; 94.10% used; 114349034 free inodes.

server4 `/data`: 154560708608 available bytes; 97.86% used; 225273208 free inodes.

server4 `/tmp`: 105757134848 available bytes; 94.10% used; 114349034 free inodes.

server4 `/var/tmp`: 105757134848 available bytes; 94.10% used; 114349034 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
