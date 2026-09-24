# V2R cluster inventory

2026-09-24T09:32:21.923133+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | ['7'] | ['/tmp', '/var/tmp'] |

server1 `/`: 324457213952 available bytes; 81.90% used; 112489842 free inodes.

server1 `/home`: 324457213952 available bytes; 81.90% used; 112489842 free inodes.

server1 `/tmp`: 324457213952 available bytes; 81.90% used; 112489842 free inodes.

server1 `/var/tmp`: 324457213952 available bytes; 81.90% used; 112489842 free inodes.

server1 `/mnt/raid5`: 502501806080 available bytes; 97.69% used; 337713098 free inodes.
| server2 | True | [] | [] |

server2 `/`: 57767309312 available bytes; 96.78% used; 110430800 free inodes.

server2 `/home`: 57767309312 available bytes; 96.78% used; 110430800 free inodes.

server2 `/tmp`: 57767309312 available bytes; 96.78% used; 110430800 free inodes.

server2 `/var/tmp`: 57767309312 available bytes; 96.78% used; 110430800 free inodes.

server2 `/mnt/raid5`: 514526203904 available bytes; 96.44% used; 445177404 free inodes.
| server3 | True | [] | [] |

server3 `/`: 85435957248 available bytes; 95.23% used; 114174509 free inodes.

server3 `/home`: 85435957248 available bytes; 95.23% used; 114174509 free inodes.

server3 `/data`: 165793247232 available bytes; 97.71% used; 225820825 free inodes.

server3 `/tmp`: 85435957248 available bytes; 95.23% used; 114174509 free inodes.

server3 `/var/tmp`: 85435957248 available bytes; 95.23% used; 114174509 free inodes.
| server4 | True | [] | ['/tmp', '/var/tmp'] |

server4 `/`: 105757667328 available bytes; 94.10% used; 114349047 free inodes.

server4 `/home`: 105757667328 available bytes; 94.10% used; 114349047 free inodes.

server4 `/data`: 154586505216 available bytes; 97.86% used; 225273263 free inodes.

server4 `/tmp`: 105757667328 available bytes; 94.10% used; 114349047 free inodes.

server4 `/var/tmp`: 105757667328 available bytes; 94.10% used; 114349047 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
