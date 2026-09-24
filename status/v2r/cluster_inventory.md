# V2R cluster inventory

2026-09-24T09:47:54.086951+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | [] | ['/tmp', '/var/tmp'] |

server1 `/`: 324447973376 available bytes; 81.90% used; 112489654 free inodes.

server1 `/home`: 324447973376 available bytes; 81.90% used; 112489654 free inodes.

server1 `/tmp`: 324447973376 available bytes; 81.90% used; 112489654 free inodes.

server1 `/var/tmp`: 324447973376 available bytes; 81.90% used; 112489654 free inodes.

server1 `/mnt/raid5`: 500748869632 available bytes; 97.70% used; 337702850 free inodes.
| server2 | True | [] | [] |

server2 `/`: 57754546176 available bytes; 96.78% used; 110430769 free inodes.

server2 `/home`: 57754546176 available bytes; 96.78% used; 110430769 free inodes.

server2 `/tmp`: 57754546176 available bytes; 96.78% used; 110430769 free inodes.

server2 `/var/tmp`: 57754546176 available bytes; 96.78% used; 110430769 free inodes.

server2 `/mnt/raid5`: 514044121088 available bytes; 96.45% used; 445176838 free inodes.
| server3 | True | [] | [] |

server3 `/`: 85829095424 available bytes; 95.21% used; 114199391 free inodes.

server3 `/home`: 85829095424 available bytes; 95.21% used; 114199391 free inodes.

server3 `/data`: 165651152896 available bytes; 97.71% used; 225819845 free inodes.

server3 `/tmp`: 85829095424 available bytes; 95.21% used; 114199391 free inodes.

server3 `/var/tmp`: 85829095424 available bytes; 95.21% used; 114199391 free inodes.
| server4 | True | [] | ['/tmp', '/var/tmp'] |

server4 `/`: 105748570112 available bytes; 94.10% used; 114349035 free inodes.

server4 `/home`: 105748570112 available bytes; 94.10% used; 114349035 free inodes.

server4 `/data`: 154559537152 available bytes; 97.86% used; 225273219 free inodes.

server4 `/tmp`: 105748570112 available bytes; 94.10% used; 114349035 free inodes.

server4 `/var/tmp`: 105748570112 available bytes; 94.10% used; 114349035 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
