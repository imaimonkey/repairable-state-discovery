# V2R cluster inventory

2026-09-26T15:14:52.651317+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | ['3', '4', '5', '6', '7'] | ['/tmp', '/var/tmp'] |

server1 `/`: 318155137024 available bytes; 82.25% used; 112473934 free inodes.

server1 `/home`: 318155137024 available bytes; 82.25% used; 112473934 free inodes.

server1 `/tmp`: 318155137024 available bytes; 82.25% used; 112473934 free inodes.

server1 `/var/tmp`: 318155137024 available bytes; 82.25% used; 112473934 free inodes.

server1 `/mnt/raid5`: 654209032192 available bytes; 97.00% used; 337531779 free inodes.
| server2 | True | ['7'] | [] |

server2 `/`: 7158579200 available bytes; 99.60% used; 110367251 free inodes.

server2 `/home`: 7158579200 available bytes; 99.60% used; 110367251 free inodes.

server2 `/tmp`: 7158579200 available bytes; 99.60% used; 110367251 free inodes.

server2 `/var/tmp`: 7158579200 available bytes; 99.60% used; 110367251 free inodes.

server2 `/mnt/raid5`: 609852719104 available bytes; 95.79% used; 444973470 free inodes.
| server3 | True | [] | [] |

server3 `/`: 82442956800 available bytes; 95.40% used; 114101904 free inodes.

server3 `/home`: 82442956800 available bytes; 95.40% used; 114101904 free inodes.

server3 `/data`: 1346906898432 available bytes; 81.39% used; 225810015 free inodes.

server3 `/tmp`: 82442956800 available bytes; 95.40% used; 114101904 free inodes.

server3 `/var/tmp`: 82442956800 available bytes; 95.40% used; 114101904 free inodes.
| server4 | True | ['3', '5', '7'] | ['/tmp', '/var/tmp'] |

server4 `/`: 105955033088 available bytes; 94.09% used; 114347840 free inodes.

server4 `/home`: 105955033088 available bytes; 94.09% used; 114347840 free inodes.

server4 `/data`: 410808856576 available bytes; 94.32% used; 224826079 free inodes.

server4 `/tmp`: 105955033088 available bytes; 94.09% used; 114347840 free inodes.

server4 `/var/tmp`: 105955033088 available bytes; 94.09% used; 114347840 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
