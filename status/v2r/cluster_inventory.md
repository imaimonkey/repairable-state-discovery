# V2R cluster inventory

2026-09-24T09:35:28.336930+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | ['7'] | ['/tmp', '/var/tmp'] |

server1 `/`: 324454404096 available bytes; 81.90% used; 112489813 free inodes.

server1 `/home`: 324454404096 available bytes; 81.90% used; 112489813 free inodes.

server1 `/tmp`: 324454404096 available bytes; 81.90% used; 112489813 free inodes.

server1 `/var/tmp`: 324454404096 available bytes; 81.90% used; 112489813 free inodes.

server1 `/mnt/raid5`: 502492205056 available bytes; 97.69% used; 337712741 free inodes.
| server2 | True | [] | [] |

server2 `/`: 57765896192 available bytes; 96.78% used; 110430800 free inodes.

server2 `/home`: 57765896192 available bytes; 96.78% used; 110430800 free inodes.

server2 `/tmp`: 57765896192 available bytes; 96.78% used; 110430800 free inodes.

server2 `/var/tmp`: 57765896192 available bytes; 96.78% used; 110430800 free inodes.

server2 `/mnt/raid5`: 514429943808 available bytes; 96.45% used; 445177491 free inodes.
| server3 | True | [] | [] |

server3 `/`: 85433286656 available bytes; 95.23% used; 114174476 free inodes.

server3 `/home`: 85433286656 available bytes; 95.23% used; 114174476 free inodes.

server3 `/data`: 165754675200 available bytes; 97.71% used; 225820453 free inodes.

server3 `/tmp`: 85433286656 available bytes; 95.23% used; 114174476 free inodes.

server3 `/var/tmp`: 85433286656 available bytes; 95.23% used; 114174476 free inodes.
| server4 | True | [] | ['/tmp', '/var/tmp'] |

server4 `/`: 105757577216 available bytes; 94.10% used; 114349047 free inodes.

server4 `/home`: 105757577216 available bytes; 94.10% used; 114349047 free inodes.

server4 `/data`: 154576027648 available bytes; 97.86% used; 225273239 free inodes.

server4 `/tmp`: 105757577216 available bytes; 94.10% used; 114349047 free inodes.

server4 `/var/tmp`: 105757577216 available bytes; 94.10% used; 114349047 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
