# V2R cluster inventory

2026-09-24T10:03:26.185210+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | [] | ['/tmp', '/var/tmp'] |

server1 `/`: 324427001856 available bytes; 81.90% used; 112489487 free inodes.

server1 `/home`: 324427001856 available bytes; 81.90% used; 112489487 free inodes.

server1 `/tmp`: 324427001856 available bytes; 81.90% used; 112489487 free inodes.

server1 `/var/tmp`: 324427001856 available bytes; 81.90% used; 112489487 free inodes.

server1 `/mnt/raid5`: 500690386944 available bytes; 97.70% used; 337700967 free inodes.
| server2 | True | [] | [] |

server2 `/`: 57749823488 available bytes; 96.78% used; 110430732 free inodes.

server2 `/home`: 57749823488 available bytes; 96.78% used; 110430732 free inodes.

server2 `/tmp`: 57749823488 available bytes; 96.78% used; 110430732 free inodes.

server2 `/var/tmp`: 57749823488 available bytes; 96.78% used; 110430732 free inodes.

server2 `/mnt/raid5`: 513559842816 available bytes; 96.45% used; 445176626 free inodes.
| server3 | True | [] | [] |

server3 `/`: 85383213056 available bytes; 95.24% used; 114173558 free inodes.

server3 `/home`: 85383213056 available bytes; 95.24% used; 114173558 free inodes.

server3 `/data`: 164478763008 available bytes; 97.73% used; 225819207 free inodes.

server3 `/tmp`: 85383213056 available bytes; 95.24% used; 114173558 free inodes.

server3 `/var/tmp`: 85383213056 available bytes; 95.24% used; 114173558 free inodes.
| server4 | True | [] | ['/tmp', '/var/tmp'] |

server4 `/`: 105747816448 available bytes; 94.10% used; 114349019 free inodes.

server4 `/home`: 105747816448 available bytes; 94.10% used; 114349019 free inodes.

server4 `/data`: 154567278592 available bytes; 97.86% used; 225273203 free inodes.

server4 `/tmp`: 105747816448 available bytes; 94.10% used; 114349019 free inodes.

server4 `/var/tmp`: 105747816448 available bytes; 94.10% used; 114349019 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
