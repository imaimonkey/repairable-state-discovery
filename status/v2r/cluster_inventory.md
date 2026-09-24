# V2R cluster inventory

2026-09-24T10:23:38.365206+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | [] | ['/tmp', '/var/tmp'] |

server1 `/`: 324415201280 available bytes; 81.90% used; 112489319 free inodes.

server1 `/home`: 324415201280 available bytes; 81.90% used; 112489319 free inodes.

server1 `/tmp`: 324415201280 available bytes; 81.90% used; 112489319 free inodes.

server1 `/var/tmp`: 324415201280 available bytes; 81.90% used; 112489319 free inodes.

server1 `/mnt/raid5`: 500178448384 available bytes; 97.71% used; 337698590 free inodes.
| server2 | True | [] | [] |

server2 `/`: 57733648384 available bytes; 96.78% used; 110430675 free inodes.

server2 `/home`: 57733648384 available bytes; 96.78% used; 110430675 free inodes.

server2 `/tmp`: 57733648384 available bytes; 96.78% used; 110430675 free inodes.

server2 `/var/tmp`: 57733648384 available bytes; 96.78% used; 110430675 free inodes.

server2 `/mnt/raid5`: 512943181824 available bytes; 96.46% used; 445175771 free inodes.
| server3 | True | [] | [] |

server3 `/`: 85807419392 available bytes; 95.21% used; 114198654 free inodes.

server3 `/home`: 85807419392 available bytes; 95.21% used; 114198654 free inodes.

server3 `/data`: 164354531328 available bytes; 97.73% used; 225818755 free inodes.

server3 `/tmp`: 85807419392 available bytes; 95.21% used; 114198654 free inodes.

server3 `/var/tmp`: 85807419392 available bytes; 95.21% used; 114198654 free inodes.
| server4 | True | ['2'] | ['/tmp', '/var/tmp'] |

server4 `/`: 105744969728 available bytes; 94.10% used; 114348988 free inodes.

server4 `/home`: 105744969728 available bytes; 94.10% used; 114348988 free inodes.

server4 `/data`: 153472987136 available bytes; 97.88% used; 225258400 free inodes.

server4 `/tmp`: 105744969728 available bytes; 94.10% used; 114348988 free inodes.

server4 `/var/tmp`: 105744969728 available bytes; 94.10% used; 114348988 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
