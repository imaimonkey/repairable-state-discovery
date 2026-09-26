# V2R cluster inventory

2026-09-26T16:35:41.985520+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | ['0', '3', '4', '5', '6', '7'] | ['/tmp', '/var/tmp'] |

server1 `/`: 318130438144 available bytes; 82.25% used; 112473835 free inodes.

server1 `/home`: 318130438144 available bytes; 82.25% used; 112473835 free inodes.

server1 `/tmp`: 318130438144 available bytes; 82.25% used; 112473835 free inodes.

server1 `/var/tmp`: 318130438144 available bytes; 82.25% used; 112473835 free inodes.

server1 `/mnt/raid5`: 654102437888 available bytes; 97.00% used; 337531408 free inodes.
| server2 | True | ['2', '7'] | [] |

server2 `/`: 18030968832 available bytes; 98.99% used; 110367557 free inodes.

server2 `/home`: 18030968832 available bytes; 98.99% used; 110367557 free inodes.

server2 `/tmp`: 18030968832 available bytes; 98.99% used; 110367557 free inodes.

server2 `/var/tmp`: 18030968832 available bytes; 98.99% used; 110367557 free inodes.

server2 `/mnt/raid5`: 607546560512 available bytes; 95.80% used; 444970960 free inodes.
| server3 | True | [] | [] |

server3 `/`: 82006384640 available bytes; 95.42% used; 114106866 free inodes.

server3 `/home`: 82006384640 available bytes; 95.42% used; 114106866 free inodes.

server3 `/data`: 1349332131840 available bytes; 81.35% used; 225830583 free inodes.

server3 `/tmp`: 82006384640 available bytes; 95.42% used; 114106866 free inodes.

server3 `/var/tmp`: 82006384640 available bytes; 95.42% used; 114106866 free inodes.
| server4 | True | ['0', '2', '3', '4', '5', '7'] | ['/tmp', '/var/tmp'] |

server4 `/`: 105953431552 available bytes; 94.09% used; 114347873 free inodes.

server4 `/home`: 105953431552 available bytes; 94.09% used; 114347873 free inodes.

server4 `/data`: 410600927232 available bytes; 94.33% used; 224824663 free inodes.

server4 `/tmp`: 105953431552 available bytes; 94.09% used; 114347873 free inodes.

server4 `/var/tmp`: 105953431552 available bytes; 94.09% used; 114347873 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
