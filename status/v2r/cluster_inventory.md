# V2R cluster inventory

2026-09-24T10:22:05.219483+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | [] | ['/tmp', '/var/tmp'] |

server1 `/`: 324416389120 available bytes; 81.90% used; 112489339 free inodes.

server1 `/home`: 324416389120 available bytes; 81.90% used; 112489339 free inodes.

server1 `/tmp`: 324416389120 available bytes; 81.90% used; 112489339 free inodes.

server1 `/var/tmp`: 324416389120 available bytes; 81.90% used; 112489339 free inodes.

server1 `/mnt/raid5`: 500628324352 available bytes; 97.70% used; 337698775 free inodes.
| server2 | True | [] | [] |

server2 `/`: 57734594560 available bytes; 96.78% used; 110430679 free inodes.

server2 `/home`: 57734594560 available bytes; 96.78% used; 110430679 free inodes.

server2 `/tmp`: 57734594560 available bytes; 96.78% used; 110430679 free inodes.

server2 `/var/tmp`: 57734594560 available bytes; 96.78% used; 110430679 free inodes.

server2 `/mnt/raid5`: 512984596480 available bytes; 96.46% used; 445175829 free inodes.
| server3 | True | [] | [] |

server3 `/`: 85810552832 available bytes; 95.21% used; 114198664 free inodes.

server3 `/home`: 85810552832 available bytes; 95.21% used; 114198664 free inodes.

server3 `/data`: 164362567680 available bytes; 97.73% used; 225818780 free inodes.

server3 `/tmp`: 85810552832 available bytes; 95.21% used; 114198664 free inodes.

server3 `/var/tmp`: 85810552832 available bytes; 95.21% used; 114198664 free inodes.
| server4 | True | [] | ['/tmp', '/var/tmp'] |

server4 `/`: 105747013632 available bytes; 94.10% used; 114348987 free inodes.

server4 `/home`: 105747013632 available bytes; 94.10% used; 114348987 free inodes.

server4 `/data`: 153478459392 available bytes; 97.88% used; 225258413 free inodes.

server4 `/tmp`: 105747013632 available bytes; 94.10% used; 114348987 free inodes.

server4 `/var/tmp`: 105747013632 available bytes; 94.10% used; 114348987 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
