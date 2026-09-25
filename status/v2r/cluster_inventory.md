# V2R cluster inventory

2026-09-25T00:50:17.262556+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | [] | ['/tmp', '/var/tmp'] |

server1 `/`: 319088791552 available bytes; 82.20% used; 112480770 free inodes.

server1 `/home`: 319088791552 available bytes; 82.20% used; 112480770 free inodes.

server1 `/tmp`: 319088791552 available bytes; 82.20% used; 112480770 free inodes.

server1 `/var/tmp`: 319088791552 available bytes; 82.20% used; 112480770 free inodes.

server1 `/mnt/raid5`: 416821424128 available bytes; 98.09% used; 337617611 free inodes.
| server2 | True | [] | [] |

server2 `/`: 23069765632 available bytes; 98.71% used; 110410767 free inodes.

server2 `/home`: 23069765632 available bytes; 98.71% used; 110410767 free inodes.

server2 `/tmp`: 23069765632 available bytes; 98.71% used; 110410767 free inodes.

server2 `/var/tmp`: 23069765632 available bytes; 98.71% used; 110410767 free inodes.

server2 `/mnt/raid5`: 501216051200 available bytes; 96.54% used; 445162868 free inodes.
| server3 | True | [] | [] |

server3 `/`: 84357193728 available bytes; 95.29% used; 114156088 free inodes.

server3 `/home`: 84357193728 available bytes; 95.29% used; 114156088 free inodes.

server3 `/data`: 148559597568 available bytes; 97.95% used; 225813053 free inodes.

server3 `/tmp`: 84357193728 available bytes; 95.29% used; 114156088 free inodes.

server3 `/var/tmp`: 84357193728 available bytes; 95.29% used; 114156088 free inodes.
| server4 | True | ['0', '1', '4', '5', '7'] | ['/tmp', '/var/tmp'] |

server4 `/`: 105788416000 available bytes; 94.10% used; 114348304 free inodes.

server4 `/home`: 105788416000 available bytes; 94.10% used; 114348304 free inodes.

server4 `/data`: 56349917184 available bytes; 99.22% used; 225031277 free inodes.

server4 `/tmp`: 105788416000 available bytes; 94.10% used; 114348304 free inodes.

server4 `/var/tmp`: 105788416000 available bytes; 94.10% used; 114348304 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
