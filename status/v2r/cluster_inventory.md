# V2R cluster inventory

2026-09-24T23:40:58.042141+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | [] | ['/tmp', '/var/tmp'] |

server1 `/`: 319012147200 available bytes; 82.20% used; 112480778 free inodes.

server1 `/home`: 319012147200 available bytes; 82.20% used; 112480778 free inodes.

server1 `/tmp`: 319012147200 available bytes; 82.20% used; 112480778 free inodes.

server1 `/var/tmp`: 319012147200 available bytes; 82.20% used; 112480778 free inodes.

server1 `/mnt/raid5`: 415208386560 available bytes; 98.10% used; 337611954 free inodes.
| server2 | True | [] | [] |

server2 `/`: 23105675264 available bytes; 98.71% used; 110410808 free inodes.

server2 `/home`: 23105675264 available bytes; 98.71% used; 110410808 free inodes.

server2 `/tmp`: 23105675264 available bytes; 98.71% used; 110410808 free inodes.

server2 `/var/tmp`: 23105675264 available bytes; 98.71% used; 110410808 free inodes.

server2 `/mnt/raid5`: 486065143808 available bytes; 96.64% used; 445150701 free inodes.
| server3 | True | [] | [] |

server3 `/`: 84361027584 available bytes; 95.29% used; 114156081 free inodes.

server3 `/home`: 84361027584 available bytes; 95.29% used; 114156081 free inodes.

server3 `/data`: 148024786944 available bytes; 97.95% used; 225800718 free inodes.

server3 `/tmp`: 84361027584 available bytes; 95.29% used; 114156081 free inodes.

server3 `/var/tmp`: 84361027584 available bytes; 95.29% used; 114156081 free inodes.
| server4 | True | ['7'] | ['/tmp', '/var/tmp'] |

server4 `/`: 105799245824 available bytes; 94.10% used; 114348296 free inodes.

server4 `/home`: 105799245824 available bytes; 94.10% used; 114348296 free inodes.

server4 `/data`: 61074210816 available bytes; 99.16% used; 225131377 free inodes.

server4 `/tmp`: 105799245824 available bytes; 94.10% used; 114348296 free inodes.

server4 `/var/tmp`: 105799245824 available bytes; 94.10% used; 114348296 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
