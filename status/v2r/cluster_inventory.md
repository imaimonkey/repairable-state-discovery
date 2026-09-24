# V2R cluster inventory

2026-09-24T18:52:24.530015+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | [] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 323997175808 available bytes; 81.93% used; 112481444 free inodes.

server1 `/home`: 323997175808 available bytes; 81.93% used; 112481444 free inodes.

server1 `/tmp`: 323997175808 available bytes; 81.93% used; 112481444 free inodes.

server1 `/var/tmp`: 323997175808 available bytes; 81.93% used; 112481444 free inodes.

server1 `/mnt/raid5`: 416268234752 available bytes; 98.09% used; 337636777 free inodes.
| server2 | True | ['7'] | [] | reference_compatible=False |

server2 `/`: 54471368704 available bytes; 96.96% used; 110411939 free inodes.

server2 `/home`: 54471368704 available bytes; 96.96% used; 110411939 free inodes.

server2 `/tmp`: 54471368704 available bytes; 96.96% used; 110411939 free inodes.

server2 `/var/tmp`: 54471368704 available bytes; 96.96% used; 110411939 free inodes.

server2 `/mnt/raid5`: 496034254848 available bytes; 96.57% used; 445159786 free inodes.
| server3 | True | ['1'] | [] | reference_compatible=True |

server3 `/`: 84407918592 available bytes; 95.29% used; 114156137 free inodes.

server3 `/home`: 84407918592 available bytes; 95.29% used; 114156137 free inodes.

server3 `/data`: 152673746944 available bytes; 97.89% used; 225800138 free inodes.

server3 `/tmp`: 84407918592 available bytes; 95.29% used; 114156137 free inodes.

server3 `/var/tmp`: 84407918592 available bytes; 95.29% used; 114156137 free inodes.
| server4 | True | ['3'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 105661407232 available bytes; 94.10% used; 114348502 free inodes.

server4 `/home`: 105661407232 available bytes; 94.10% used; 114348502 free inodes.

server4 `/data`: 89948676096 available bytes; 98.76% used; 225267574 free inodes.

server4 `/tmp`: 105661407232 available bytes; 94.10% used; 114348502 free inodes.

server4 `/var/tmp`: 105661407232 available bytes; 94.10% used; 114348502 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
