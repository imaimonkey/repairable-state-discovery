# V2R cluster inventory

2026-09-25T00:07:13.989875+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | [] | ['/tmp', '/var/tmp'] |

server1 `/`: 319088427008 available bytes; 82.20% used; 112480784 free inodes.

server1 `/home`: 319088427008 available bytes; 82.20% used; 112480784 free inodes.

server1 `/tmp`: 319088427008 available bytes; 82.20% used; 112480784 free inodes.

server1 `/var/tmp`: 319088427008 available bytes; 82.20% used; 112480784 free inodes.

server1 `/mnt/raid5`: 416897404928 available bytes; 98.09% used; 337622537 free inodes.
| server2 | True | [] | [] |

server2 `/`: 23095431168 available bytes; 98.71% used; 110410786 free inodes.

server2 `/home`: 23095431168 available bytes; 98.71% used; 110410786 free inodes.

server2 `/tmp`: 23095431168 available bytes; 98.71% used; 110410786 free inodes.

server2 `/var/tmp`: 23095431168 available bytes; 98.71% used; 110410786 free inodes.

server2 `/mnt/raid5`: 486664417280 available bytes; 96.64% used; 445163682 free inodes.
| server3 | True | [] | [] |

server3 `/`: 84353601536 available bytes; 95.29% used; 114156084 free inodes.

server3 `/home`: 84353601536 available bytes; 95.29% used; 114156084 free inodes.

server3 `/data`: 149284446208 available bytes; 97.94% used; 225813873 free inodes.

server3 `/tmp`: 84353601536 available bytes; 95.29% used; 114156084 free inodes.

server3 `/var/tmp`: 84353601536 available bytes; 95.29% used; 114156084 free inodes.
| server4 | True | ['0', '5', '7'] | ['/tmp', '/var/tmp'] |

server4 `/`: 105797971968 available bytes; 94.10% used; 114348297 free inodes.

server4 `/home`: 105797971968 available bytes; 94.10% used; 114348297 free inodes.

server4 `/data`: 58831691776 available bytes; 99.19% used; 225091446 free inodes.

server4 `/tmp`: 105797971968 available bytes; 94.10% used; 114348297 free inodes.

server4 `/var/tmp`: 105797971968 available bytes; 94.10% used; 114348297 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
