# V2R cluster inventory

2026-09-24T09:23:02.821235+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | ['7'] | ['/tmp', '/var/tmp'] |

server1 `/`: 324462776320 available bytes; 81.90% used; 112489925 free inodes.

server1 `/home`: 324462776320 available bytes; 81.90% used; 112489925 free inodes.

server1 `/tmp`: 324462776320 available bytes; 81.90% used; 112489925 free inodes.

server1 `/var/tmp`: 324462776320 available bytes; 81.90% used; 112489925 free inodes.

server1 `/mnt/raid5`: 503184719872 available bytes; 97.69% used; 337714196 free inodes.
| server2 | True | [] | [] |

server2 `/`: 57775362048 available bytes; 96.78% used; 110430834 free inodes.

server2 `/home`: 57775362048 available bytes; 96.78% used; 110430834 free inodes.

server2 `/tmp`: 57775362048 available bytes; 96.78% used; 110430834 free inodes.

server2 `/var/tmp`: 57775362048 available bytes; 96.78% used; 110430834 free inodes.

server2 `/mnt/raid5`: 514277658624 available bytes; 96.45% used; 445177864 free inodes.
| server3 | True | [] | [] |

server3 `/`: 85859168256 available bytes; 95.21% used; 114199111 free inodes.

server3 `/home`: 85859168256 available bytes; 95.21% used; 114199111 free inodes.

server3 `/data`: 165851262976 available bytes; 97.71% used; 225821008 free inodes.

server3 `/tmp`: 85859168256 available bytes; 95.21% used; 114199111 free inodes.

server3 `/var/tmp`: 85859168256 available bytes; 95.21% used; 114199111 free inodes.
| server4 | True | [] | ['/tmp', '/var/tmp'] |

server4 `/`: 105758023680 available bytes; 94.10% used; 114349051 free inodes.

server4 `/home`: 105758023680 available bytes; 94.10% used; 114349051 free inodes.

server4 `/data`: 231444488192 available bytes; 96.80% used; 225273306 free inodes.

server4 `/tmp`: 105758023680 available bytes; 94.10% used; 114349051 free inodes.

server4 `/var/tmp`: 105758023680 available bytes; 94.10% used; 114349051 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
