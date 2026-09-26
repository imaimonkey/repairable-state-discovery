# V2R cluster inventory

2026-09-26T04:45:27.309429+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | ['1', '4', '5', '6', '7'] | ['/tmp', '/var/tmp'] |

server1 `/`: 318401093632 available bytes; 82.24% used; 112476284 free inodes.

server1 `/home`: 318401093632 available bytes; 82.24% used; 112476284 free inodes.

server1 `/tmp`: 318401093632 available bytes; 82.24% used; 112476284 free inodes.

server1 `/var/tmp`: 318401093632 available bytes; 82.24% used; 112476284 free inodes.

server1 `/mnt/raid5`: 330479742976 available bytes; 98.48% used; 337545373 free inodes.
| server2 | True | [] | [] |

server2 `/`: 22937317376 available bytes; 98.72% used; 110406198 free inodes.

server2 `/home`: 22937317376 available bytes; 98.72% used; 110406198 free inodes.

server2 `/tmp`: 22937317376 available bytes; 98.72% used; 110406198 free inodes.

server2 `/var/tmp`: 22937317376 available bytes; 98.72% used; 110406198 free inodes.

server2 `/mnt/raid5`: 285060493312 available bytes; 98.03% used; 445050386 free inodes.
| server3 | True | [] | [] |

server3 `/`: 84514172928 available bytes; 95.28% used; 114173867 free inodes.

server3 `/home`: 84514172928 available bytes; 95.28% used; 114173867 free inodes.

server3 `/data`: 124391542784 available bytes; 98.28% used; 225817504 free inodes.

server3 `/tmp`: 84514172928 available bytes; 95.28% used; 114173867 free inodes.

server3 `/var/tmp`: 84514172928 available bytes; 95.28% used; 114173867 free inodes.
| server4 | True | ['2', '3', '6', '7'] | ['/tmp', '/var/tmp'] |

server4 `/`: 106001973248 available bytes; 94.08% used; 114348204 free inodes.

server4 `/home`: 106001973248 available bytes; 94.08% used; 114348204 free inodes.

server4 `/data`: 107064975360 available bytes; 98.52% used; 224929362 free inodes.

server4 `/tmp`: 106001973248 available bytes; 94.08% used; 114348204 free inodes.

server4 `/var/tmp`: 106001973248 available bytes; 94.08% used; 114348204 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
